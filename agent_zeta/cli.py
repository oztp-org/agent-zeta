"""
Agent Zeta CLI — interactive Zero Trust Maturity Assessment.
"""
import json
import os
import sys
from datetime import date
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.rule import Rule
from rich.table import Table

from .advisor import AgentZeta
from .assessment.engine import AssessmentResult, OrgContext, PillarResponse
from .assessment.ztmm import PILLARS
from .providers import build_provider

console = Console()

BANNER = """\
[bold cyan]    _                    _     ______     _
   / \\   __ _  ___ _ __ | |_  |__  / ___| |_ __ _
  / _ \\ / _` |/ _ \\ '_ \\| __|   / / |_  __/ _` |
 / ___ \\ (_| |  __/ | | | |_   / /|  _|| || (_| |
/_/   \\_\\__, |\\___|_| |_|\\__| /____\\_|   \\__\\__,_|
        |___/                                      [/bold cyan]
[dim]Open Zero Trust Project — AI Zero Trust Architecture Advisor[/dim]
[dim]Framework: CISA ZTMM v2.0 | NIST SP 800-207 | CIS Controls v8[/dim]"""

ANSWER_HINT = "[bold green]Y[/bold green]es / [bold yellow]P[/bold yellow]artial / [bold red]N[/bold red]o"


def _load_config(config_path: str) -> dict:
    path = Path(config_path)
    if not path.exists():
        console.print(f"[red]Config file not found:[/red] {config_path}")
        console.print("Copy [cyan]agent-zeta.example.json[/cyan] to [cyan]agent-zeta.json[/cyan] and set your provider.")
        sys.exit(1)
    with open(path) as f:
        data = json.load(f)
    # Strip _comment keys
    return {k: v for k, v in data.items() if not k.startswith("_")}


def _ask_yn_partial(question: str, index: int, total: int) -> str:
    console.print(f"\n  [dim][{index}/{total}][/dim] {question}")
    console.print(f"  {ANSWER_HINT}  ", end="")
    while True:
        raw = input().strip().lower()
        if raw in ("y", "yes"):
            return "yes"
        elif raw in ("p", "partial"):
            return "partial"
        elif raw in ("n", "no"):
            return "no"
        elif raw == "":
            return "no"
        console.print(f"  Please enter Y, P, or N: ", end="")


def _gather_org_context() -> OrgContext:
    console.print(Rule("[bold]Organization Profile[/bold]"))
    console.print("[dim]Help Agent Zeta tailor its recommendations to your organization.[/dim]\n")

    ctx = OrgContext()
    ctx.org_name = Prompt.ask("  Organization name", default="")
    ctx.industry = Prompt.ask("  Industry / sector (e.g. healthcare, finance, manufacturing)", default="")
    ctx.employee_count = Prompt.ask("  Approximate number of employees", default="")
    ctx.current_tools = Prompt.ask(
        "  Key security tools in use today (e.g. Microsoft 365, CrowdStrike, Palo Alto)", default="None listed"
    )
    ctx.top_concerns = Prompt.ask(
        "  Top security concerns or incidents in the past 12 months", default="None listed"
    )
    ctx.compliance_requirements = Prompt.ask(
        "  Active compliance requirements (e.g. HIPAA, PCI-DSS, SOC 2, CMMC)", default="None"
    )
    return ctx


def _assess_pillar(pillar_index: int, pillar) -> PillarResponse:
    total = len(PILLARS)
    console.print(Rule(f"[bold]Pillar {pillar_index}/{total}: {pillar.name}[/bold]"))
    console.print(f"[italic]{pillar.description}[/italic]\n")
    console.print(f"Answer each question: {ANSWER_HINT}\n")

    answers: dict[str, str] = {}
    for i, question in enumerate(pillar.questions, start=1):
        answer = _ask_yn_partial(question, i, len(pillar.questions))
        answers[question] = answer

    notes = Prompt.ask(
        "\n  [dim]Any additional context for this pillar? (optional, press Enter to skip)[/dim]",
        default="",
    )
    return PillarResponse(pillar_name=pillar.name, answers=answers, notes=notes)


def _print_score_table(result: AssessmentResult) -> None:
    table = Table(title="Maturity Scores", show_header=True, header_style="bold cyan")
    table.add_column("Pillar", style="bold")
    table.add_column("Score", justify="center")
    table.add_column("Level", justify="center")

    level_colors = {
        "Traditional": "red",
        "Initial": "yellow",
        "Advanced": "cyan",
        "Optimal": "green",
    }

    for row in result.summary_table():
        color = level_colors.get(row["level"], "white")
        table.add_row(
            row["pillar"],
            f"{row['score']:.1f} / 4.0",
            f"[{color}]{row['level']}[/{color}]",
        )

    overall = result.overall_score()
    overall_level = result.overall_level()
    color = level_colors.get(overall_level.label, "white")
    table.add_section()
    table.add_row(
        "[bold]OVERALL[/bold]",
        f"[bold]{overall:.1f} / 4.0[/bold]",
        f"[bold {color}]{overall_level.label}[/bold {color}]",
    )
    console.print(table)


def _save_report(report: str, org_name: str, output_dir: str) -> Path:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    safe_name = "".join(c if c.isalnum() else "_" for c in (org_name or "org"))
    filename = f"zt_assessment_{safe_name}_{date.today().isoformat()}.md"
    filepath = Path(output_dir) / filename
    with open(filepath, "w") as f:
        f.write(f"# Zero Trust Maturity Assessment\n")
        f.write(f"**Organization**: {org_name or 'Unknown'}  \n")
        f.write(f"**Date**: {date.today().isoformat()}  \n")
        f.write(f"**Advisor**: Agent Zeta (OZTP)  \n\n---\n\n")
        f.write(report)
    return filepath


def run_assessment(config_path: str = "agent-zeta.json") -> None:
    config = _load_config(config_path)
    provider = build_provider(config)
    advisor = AgentZeta(provider)
    output_dir = config.get("output_dir", "reports")

    console.print(BANNER)
    console.print()
    console.print(Panel(
        f"Provider: [cyan]{provider.provider_label}[/cyan]\n"
        "This assessment follows the [bold]CISA Zero Trust Maturity Model v2.0[/bold] (5 pillars, 4 levels).\n"
        "It takes approximately 10-15 minutes. Your answers guide a tailored recommendation report.",
        title="Welcome",
        border_style="cyan",
    ))
    console.print()

    if not Confirm.ask("Ready to begin?", default=True):
        console.print("Assessment cancelled.")
        return

    # Phase 1: Org context
    org = _gather_org_context()

    # Phase 2: Pillar assessments
    console.print()
    console.print(Panel(
        "You will now answer questions for each of the 5 CISA ZTMM pillars.\n"
        f"Answer with {ANSWER_HINT} for each question.",
        title="Pillar Assessment",
        border_style="cyan",
    ))

    pillar_responses: list[PillarResponse] = []
    for i, pillar in enumerate(PILLARS, start=1):
        console.print()
        resp = _assess_pillar(i, pillar)
        pillar_responses.append(resp)

    result = AssessmentResult(org=org, pillar_responses=pillar_responses)

    # Phase 3: Scores
    console.print()
    console.print(Rule("[bold]Preliminary Scores[/bold]"))
    _print_score_table(result)

    # Phase 4: LLM report
    console.print()
    console.print(Rule("[bold]Generating Report[/bold]"))
    console.print(f"\n[dim]Agent Zeta ({provider.provider_label}) is analyzing your results...[/dim]\n")

    with console.status("[bold cyan]Analyzing assessment and generating recommendations...[/bold cyan]"):
        report = advisor.generate_report(result)

    console.print(Markdown(report))

    # Phase 5: Save
    report_path = _save_report(report, org.org_name, output_dir)
    console.print()
    console.print(Panel(
        f"Report saved to: [bold cyan]{report_path}[/bold cyan]",
        title="Saved",
        border_style="green",
    ))

    # Phase 6: Optional follow-up questions
    console.print()
    if Confirm.ask("Would you like to ask Agent Zeta follow-up questions?", default=True):
        console.print("[dim]Type your question and press Enter. Type 'exit' to quit.[/dim]\n")
        while True:
            question = Prompt.ask("[bold cyan]You[/bold cyan]")
            if question.strip().lower() in ("exit", "quit", "q"):
                break
            with console.status("[bold cyan]Thinking...[/bold cyan]"):
                answer = advisor.ask(question)
            console.print()
            console.print(Panel(Markdown(answer), title="Agent Zeta", border_style="cyan"))
            console.print()

    console.print("\n[bold green]Assessment complete. Stay zero-trust![/bold green]\n")


def run_chat(config_path: str = "agent-zeta.json") -> None:
    """Lightweight chat mode — no assessment, just advisory Q&A."""
    config = _load_config(config_path)
    provider = build_provider(config)
    advisor = AgentZeta(provider)

    console.print(BANNER)
    console.print(Panel(
        f"Provider: [cyan]{provider.provider_label}[/cyan]\n"
        "Chat mode — ask any Zero Trust Architecture question.\n"
        "Type [bold]exit[/bold] to quit.",
        title="Agent Zeta Chat",
        border_style="cyan",
    ))
    console.print()

    while True:
        question = Prompt.ask("[bold cyan]You[/bold cyan]")
        if question.strip().lower() in ("exit", "quit", "q"):
            break
        with console.status("[bold cyan]Thinking...[/bold cyan]"):
            answer = advisor.ask(question)
        console.print()
        console.print(Panel(Markdown(answer), title="Agent Zeta", border_style="cyan"))
        console.print()

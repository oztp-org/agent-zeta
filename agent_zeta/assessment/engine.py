"""
Assessment engine: collects org context and pillar responses, scores maturity.
The LLM-generated report (in advisor.py) adds nuance; this provides the raw inputs.
"""
from dataclasses import dataclass, field

from .ztmm import MaturityLevel, Pillar, PILLARS


@dataclass
class PillarResponse:
    pillar_name: str
    answers: dict[str, str]  # question -> "yes" | "partial" | "no"
    notes: str = ""

    @property
    def score(self) -> float:
        """Rough 1-4 maturity score from yes/partial/no answers."""
        if not self.answers:
            return 1.0
        points = sum(
            {"yes": 1.0, "partial": 0.5, "no": 0.0}.get(v.lower(), 0.0)
            for v in self.answers.values()
        )
        ratio = points / len(self.answers)
        if ratio < 0.25:
            return 1.0
        elif ratio < 0.50:
            return 2.0
        elif ratio < 0.75:
            return 3.0
        else:
            return 4.0

    @property
    def level(self) -> MaturityLevel:
        return MaturityLevel(max(1, min(4, int(self.score))))


@dataclass
class OrgContext:
    org_name: str = ""
    industry: str = ""
    employee_count: str = ""
    current_tools: str = ""
    top_concerns: str = ""
    compliance_requirements: str = ""


@dataclass
class AssessmentResult:
    org: OrgContext
    pillar_responses: list[PillarResponse] = field(default_factory=list)

    def overall_score(self) -> float:
        if not self.pillar_responses:
            return 1.0
        return sum(r.score for r in self.pillar_responses) / len(self.pillar_responses)

    def overall_level(self) -> MaturityLevel:
        return MaturityLevel(max(1, min(4, round(self.overall_score()))))

    def summary_table(self) -> list[dict]:
        return [
            {
                "pillar": r.pillar_name,
                "score": r.score,
                "level": r.level.label,
            }
            for r in self.pillar_responses
        ]

    def to_prompt_context(self) -> str:
        """Serialize assessment results into a structured string for the LLM."""
        lines = [
            "## Organization",
            f"- Name: {self.org.org_name or 'Not specified'}",
            f"- Industry: {self.org.industry or 'Not specified'}",
            f"- Size: {self.org.employee_count or 'Not specified'}",
            f"- Current security tools: {self.org.current_tools or 'Not specified'}",
            f"- Top security concerns: {self.org.top_concerns or 'Not specified'}",
            f"- Compliance requirements: {self.org.compliance_requirements or 'None specified'}",
            "",
            "## Pillar Assessment Results",
        ]

        pillar_map: dict[str, Pillar] = {p.name: p for p in PILLARS}

        for resp in self.pillar_responses:
            pillar = pillar_map.get(resp.pillar_name)
            lines.append(f"\n### {resp.pillar_name} — Score: {resp.score:.1f}/4.0 ({resp.level.label})")
            if pillar:
                for q, a in zip(pillar.questions, resp.answers.values()):
                    lines.append(f"- [{a.upper()}] {q}")
            if resp.notes:
                lines.append(f"- Additional context: {resp.notes}")

        lines += [
            "",
            f"## Overall Score: {self.overall_score():.1f}/4.0 ({self.overall_level().label})",
        ]
        return "\n".join(lines)

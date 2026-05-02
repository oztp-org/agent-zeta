#!/usr/bin/env python3
"""
Agent Zeta entry point.

Usage:
  python run.py                    # full ZTMM assessment
  python run.py --chat             # advisory chat mode only
  python run.py --config my.json   # use a specific config file
"""
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Agent Zeta — AI Zero Trust Architecture Advisor (OZTP)"
    )
    parser.add_argument(
        "--config",
        default="agent-zeta.json",
        help="Path to config JSON file (default: agent-zeta.json)",
    )
    parser.add_argument(
        "--chat",
        action="store_true",
        help="Launch in chat mode (no assessment questionnaire)",
    )
    args = parser.parse_args()

    try:
        from agent_zeta.cli import run_assessment, run_chat

        if args.chat:
            run_chat(config_path=args.config)
        else:
            run_assessment(config_path=args.config)
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye.")
        sys.exit(0)


if __name__ == "__main__":
    main()

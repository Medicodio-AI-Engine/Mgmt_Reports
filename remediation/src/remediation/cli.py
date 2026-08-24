"""Command line entry point.

    python -m remediation run [--report-date YYYY-MM-DD] [--repository-root PATH]
    python -m remediation discover
    python -m remediation decisions
    python -m remediation validate

``run`` is dry-run by default. ``--allow-writes`` exists only so the flag has to be
typed deliberately; it still refuses unless a repository is allowlisted in config.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import config as config_module
from . import discovery, pipeline, playbooks, review, schema
from .naming import run_id

EXPECTED_FAILURES = (
    discovery.DiscoveryError,
    pipeline.PipelineError,
    schema.SchemaValidationError,
    config_module.ConfigError,
)


def _repository_root(value: str | None) -> Path:
    if value:
        return Path(value).expanduser().resolve()
    # remediation/src/remediation/cli.py -> repository root
    return Path(__file__).resolve().parents[3]


def _load(args: argparse.Namespace) -> config_module.Config:
    overrides: dict[str, object] = {}
    if getattr(args, "allow_writes", False):
        overrides["dry_run_mode"] = False
    if getattr(args, "artifact_root", None):
        overrides["artifact_root_directory"] = args.artifact_root
    return config_module.load(
        Path(args.config).expanduser() if args.config else None, overrides=overrides
    )


def cmd_run(args: argparse.Namespace) -> int:
    config = _load(args)
    root = _repository_root(args.repository_root)
    result = pipeline.run(
        config,
        report_date=args.report_date,
        repository_root=root,
        limit=args.limit,
    )
    print(f"run {result.run_context.run_id} report_date {result.run_context.report_date}")
    print(f"completeness {result.run_context.completeness.value}")
    print(f"issues {result.metrics['issues_total']}")
    print(f"dry_run {config.dry_run_mode}")
    print(f"artifacts {result.paths.root}")
    for warning in result.run_context.warnings:
        print(f"warning: {warning}", file=sys.stderr)
    return 0


def cmd_discover(args: argparse.Namespace) -> int:
    config = _load(args)
    root = _repository_root(args.repository_root)
    context = discovery.assemble(
        config,
        root / config.mgmt_reports_directory,
        run_id(0),
        requested_report_date=args.report_date,
    )
    print(json.dumps(context.manifest(config), indent=2, sort_keys=True))
    return 0 if context.processable else 1


def cmd_decisions(args: argparse.Namespace) -> int:
    config = _load(args)
    decisions = review.load_decisions(config.artifact_root_directory)
    if not decisions:
        print("no DECISION blocks found")
        return 0
    for _, decision in sorted(decisions.items()):
        print(json.dumps(decision.as_dict(), sort_keys=True))
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    config = _load(args)
    registry = playbooks.load_registry(config)
    print(f"org playbooks {len(registry.org)}, general playbooks {len(registry.general)}")
    print(f"skills registered {len(registry.skills)}")
    for name in schema.SCHEMAS:
        schema.load_schema(name)
        print(f"schema loaded: {name}")
    print(f"dry_run_mode {config.dry_run_mode}")
    print(f"approval_mechanism {config.approval_mechanism}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="remediation", description=__doc__)
    parser.add_argument("--config", help="path to config.yaml")
    parser.add_argument("--artifact-root", help="override the artifact output directory")
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="execute the Version 1 flow for one report date")
    run_parser.add_argument(
        "--report-date", help="YYYY-MM-DD or YYYY_MM_DD; default: latest complete"
    )
    run_parser.add_argument("--repository-root", help="path to the Mgmt_Reports checkout")
    run_parser.add_argument(
        "--limit", type=int, default=10, help="candidates to select for attention"
    )
    run_parser.add_argument(
        "--allow-writes",
        action="store_true",
        help="disable dry-run (still refuses unless a repository is allowlisted)",
    )
    run_parser.set_defaults(func=cmd_run)

    discover_parser = subparsers.add_parser("discover", help="print the source manifest only")
    discover_parser.add_argument("--report-date")
    discover_parser.add_argument("--repository-root")
    discover_parser.set_defaults(func=cmd_discover)

    decisions_parser = subparsers.add_parser(
        "decisions", help="print every DECISION block found in the artifacts"
    )
    decisions_parser.set_defaults(func=cmd_decisions)

    validate_parser = subparsers.add_parser(
        "validate", help="load configuration, playbooks, skills, and schemas"
    )
    validate_parser.set_defaults(func=cmd_validate)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except EXPECTED_FAILURES as error:
        # A refusal is an expected outcome, not a crash: report it in one line.
        print(f"{type(error).__name__}: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

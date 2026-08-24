"""Remediation planning (stage 03_PLAN).

Produces the plan a human reviews: the proposed action, ordered steps taken from
the matched playbook, the tests that would prove the fix, the verification
commands, the rollback plan, and the explicit stop conditions. Planning is
read-only and happens even when execution is not permitted, because the plan is
the deliverable of a dry run.
"""

from __future__ import annotations

from typing import Any

from .autonomy import Decision
from .config import Config
from .guardrails import Violation
from .playbooks import Match

CANDIDATE_LIMIT = 10


def _test_plan(issue: dict[str, Any], match: Match) -> list[dict[str, Any]]:
    if match.playbook is None:
        return []
    if issue["category"] == "MISSING_TEST":
        surface = issue.get("title") or "the reported behavior"
        return [
            {
                "test_id": f"{issue['issue_id']}_T01",
                "intent": f"Fail when {surface} regresses",
                "kind": "REGRESSION",
                "would_run": True,
                "generated": False,
                "reason_not_generated": "dry-run: no repository is written",
            }
        ]
    if issue["category"] == "SECURITY_TENANCY":
        return [
            {
                "test_id": f"{issue['issue_id']}_T01",
                "intent": "Assert cross-tenant access is denied (read-only)",
                "kind": "ISOLATION",
                "would_run": True,
                "generated": False,
                "reason_not_generated": "human-owned surface: inspection and proposal only",
            }
        ]
    if issue["category"] in {"MECHANICAL_MIGRATION", "CODE_QUALITY"}:
        return [
            {
                "test_id": f"{issue['issue_id']}_T01",
                "intent": "Existing suites must pass unchanged (no behavior change)",
                "kind": "EXISTING_SUITE",
                "would_run": True,
                "generated": False,
                "reason_not_generated": "dry-run: no repository is written",
            }
        ]
    return []


def _commands(issue: dict[str, Any], config: Config) -> list[dict[str, Any]]:
    commands = config.commands_for(issue.get("repository"))
    planned: list[dict[str, Any]] = []
    for phase, values in (
        ("TARGETED_TEST", commands.test),
        ("BUILD", commands.build),
        ("TYPECHECK", commands.typecheck),
        ("STATIC_ANALYSIS", commands.static_analysis),
    ):
        for command in values:
            planned.append({"phase": phase, "command": command, "executed": False})
    if not planned:
        planned.append(
            {
                "phase": "TARGETED_TEST",
                "command": None,
                "executed": False,
                "note": (
                    "No verification commands are configured for this repository; a human must "
                    "supply them before any execution is permitted."
                ),
            }
        )
    return planned


def _rollback(issue: dict[str, Any], decision: Decision) -> str:
    if decision.tier in {"C", "D"}:
        return (
            "Nothing to roll back: this issue is proposal-only, so no repository state is changed."
        )
    return (
        "Revert the working branch commit(s) for "
        f"{issue['attempt_id']}; no other system state is touched. The branch is never merged "
        "without human approval."
    )


def plan(
    issue: dict[str, Any],
    match: Match,
    decision: Decision,
    violations: list[Violation],
    config: Config,
) -> dict[str, Any]:
    """Build the implementation plan for one issue."""
    blocked = bool(violations)
    steps = list(match.playbook.steps) if match.playbook else []
    if blocked:
        proposed = "STOP: guardrail violation; human action required before any work."
    elif match.playbook is None:
        proposed = "PROPOSE: no approved playbook matched; request human direction."
    elif decision.tier == "D":
        proposed = "DOCUMENT ONLY: human-owned surface; produce findings and a proposal."
    elif decision.tier == "C":
        proposed = "INVESTIGATE AND PROPOSE: no implementation until a human approves."
    elif decision.tier == "B":
        proposed = (
            "IMPLEMENT UNDER APPROVAL: prepare the change and tests; a human must approve before "
            "merge."
        )
    else:
        proposed = "IMPLEMENT: mechanical, reversible change with test evidence."

    return {
        "proposed_action": proposed,
        "implementation_plan": steps,
        "acceptance_criteria": list(match.playbook.review_checklist) if match.playbook else [],
        "test_plan": _test_plan(issue, match),
        "verification_commands": _commands(issue, config),
        "rollback_plan": _rollback(issue, decision),
        "stop_conditions": decision.stop_conditions
        + [violation.stop_reason for violation in violations]
        + (list(match.playbook.stop_conditions) if match.playbook else []),
        "execution_allowed": decision.execution_allowed and not blocked,
        "dry_run": config.dry_run_mode,
    }


def select_candidates(issues: list[dict[str, Any]], limit: int = CANDIDATE_LIMIT) -> list[str]:
    """Order issues for attention: highest priority, then lowest complexity.

    Selection is ordering only. It confers no permission: the autonomy tier and the
    guardrail engine decide what may be done with a selected issue.
    """
    ranked = sorted(
        issues,
        key=lambda issue: (
            -(issue.get("priority", {}).get("score") or 0),
            issue.get("complexity", {}).get("score") or 10,
            issue["issue_id"],
        ),
    )
    return [issue["issue_id"] for issue in ranked[:limit]]

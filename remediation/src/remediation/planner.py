"""Remediation planning (stage 03_PLAN).

Produces the plan a human reviews: the proposed action, ordered steps taken from
the matched playbook, the tests that would prove the fix, the verification
commands, the rollback plan, and the explicit stop conditions. Planning is
read-only and happens even when execution is not permitted, because the plan is
the deliverable of a dry run.
"""

from __future__ import annotations

from typing import Any

from . import scope as scope_module
from .autonomy import Decision
from .config import Config
from .guardrails import Violation
from .playbooks import Match

TIER_ACTIONS: dict[str, str] = {
    "D": "DOCUMENT ONLY: human-owned surface; produce findings and a proposal.",
    "C": "INVESTIGATE AND PROPOSE: no implementation until a human approves.",
    "B": (
        "IMPLEMENT UNDER APPROVAL: prepare the change and tests; a human must approve before merge."
    ),
    "A": "IMPLEMENT: mechanical, reversible change with test evidence.",
}

CANDIDATE_LIMIT = 10


DRY_RUN_REASON = "dry-run: no repository is written"

# category -> (test kind, intent template, reason it is not generated)
TEST_INTENTS: dict[str, tuple[str, str, str]] = {
    "MISSING_TEST": ("REGRESSION", "Fail when {surface} regresses", DRY_RUN_REASON),
    "SECURITY_TENANCY": (
        "ISOLATION",
        "Assert cross-tenant access is denied (read-only)",
        "human-owned surface: inspection and proposal only",
    ),
    "MECHANICAL_MIGRATION": (
        "EXISTING_SUITE",
        "Existing suites must pass unchanged (no behavior change)",
        DRY_RUN_REASON,
    ),
    "CODE_QUALITY": (
        "EXISTING_SUITE",
        "Existing suites must pass unchanged (no behavior change)",
        DRY_RUN_REASON,
    ),
}


def _planned_test(issue: dict[str, Any], spec: tuple[str, str, str]) -> dict[str, Any]:
    kind, intent, reason = spec
    surface = issue.get("title") or "the reported behavior"
    return {
        "test_id": f"{issue['issue_id']}_T01",
        "intent": intent.format(surface=surface),
        "kind": kind,
        "would_run": True,
        "generated": False,
        "reason_not_generated": reason,
    }


def _test_plan(issue: dict[str, Any], match: Match) -> list[dict[str, Any]]:
    """The test that would prove the fix, if this category has a provable one."""
    spec = TEST_INTENTS.get(issue["category"])
    if match.playbook is None or spec is None:
        return []
    return [_planned_test(issue, spec)]


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


def proposed_action(match: Match, decision: Decision, blocked: bool) -> str:
    """The one-line instruction a reviewer reads first."""
    if blocked:
        return "STOP: guardrail violation; human action required before any work."
    if match.playbook is None:
        return "PROPOSE: no approved playbook matched; request human direction."
    return TIER_ACTIONS.get(decision.tier, TIER_ACTIONS["A"])


def _stop_conditions(match: Match, decision: Decision, violations: list[Violation]) -> list[str]:
    playbook_stops = list(match.playbook.stop_conditions) if match.playbook else []
    return decision.stop_conditions + [v.stop_reason for v in violations] + playbook_stops


def plan(
    issue: dict[str, Any],
    match: Match,
    decision: Decision,
    violations: list[Violation],
    config: Config,
) -> dict[str, Any]:
    """Build the implementation plan for one issue."""
    blocked = bool(violations)
    return {
        "proposed_action": proposed_action(match, decision, blocked),
        "implementation_plan": list(match.playbook.steps) if match.playbook else [],
        "acceptance_criteria": list(match.playbook.review_checklist) if match.playbook else [],
        "test_plan": _test_plan(issue, match),
        "verification_commands": _commands(issue, config),
        "rollback_plan": _rollback(issue, decision),
        "stop_conditions": _stop_conditions(match, decision, violations),
        "execution_allowed": decision.execution_allowed and not blocked,
        "dry_run": config.dry_run_mode,
    }


def _rank_key(issue: dict[str, Any]) -> tuple[int, int, str]:
    return (
        -(issue.get("priority", {}).get("score") or 0),
        issue.get("complexity", {}).get("score") or 10,
        issue["issue_id"],
    )


def in_pilot_scope(issue: dict[str, Any]) -> bool:
    """Out-of-scope issues stay recorded as evidence but are never worked on."""
    return issue.get("analysis_scope") != scope_module.OUT_OF_SCOPE


def select_candidates(issues: list[dict[str, Any]], limit: int = CANDIDATE_LIMIT) -> list[str]:
    """Order in-scope issues for attention: highest priority, then lowest complexity.

    Selection is ordering only. It confers no permission: the autonomy tier and the
    guardrail engine decide what may be done with a selected issue.
    """
    ranked = sorted(
        [issue for issue in issues if in_pilot_scope(issue)],
        key=lambda issue: (
            -(issue.get("priority", {}).get("score") or 0),
            issue.get("complexity", {}).get("score") or 10,
            issue["issue_id"],
        ),
    )
    return [issue["issue_id"] for issue in ranked[:limit]]

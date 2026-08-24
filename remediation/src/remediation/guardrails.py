"""Guardrail engine.

Enforced in code, not left to prompt discipline. Each rule that fires records the
stop reason, the evidence it fired on, the human action required, and the state
the issue is forced into. A single violation is enough to stop the issue.
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from .autonomy import Decision
from .config import Config
from .playbooks import Match
from .states import State

FORBIDDEN_PATTERNS: tuple[tuple[str, str, str], ...] = (
    (
        "SECURITY_POLICY_DECISION",
        r"security policy|threat model|risk accept|waiver",
        "A human security owner must decide; the platform never sets security policy.",
    ),
    (
        "PHI_ACCESS_RULE",
        r"\bphi\b|protected health|hipaa",
        "A human compliance owner must decide any PHI access change.",
    ),
    (
        "AUTH_POLICY",
        r"authenticat\w+ policy|authoriz\w+ policy|rbac policy|permission model",
        "A human owner must decide authentication/authorization policy.",
    ),
    (
        "TENANT_ISOLATION",
        r"tenant isolation|row level security|\brls\b|cross-tenant",
        "Tenant isolation semantics are human-owned; inspection and tests only.",
    ),
    (
        "MONEY_SEMANTICS",
        r"billing|invoice|payment|pricing|refund",
        "A human owner must decide any change to money semantics.",
    ),
    (
        "SECRET_MODIFICATION",
        r"rotate (the )?secret|change (the )?credential|update api key|\.env\b",
        "Secrets change only through the approved secret-management mechanism.",
    ),
    (
        "DESTRUCTIVE_OPERATION",
        r"drop table|truncate|delete all|force[- ]push|purge",
        "Destructive operations require explicit human execution.",
    ),
    (
        "IRREVERSIBLE_MIGRATION",
        r"irreversible|backfill|data migration|schema migration",
        "Irreversible or data migrations require human ownership.",
    ),
    (
        "COMPLIANCE_DECISION",
        r"compliance decision|audit finding acceptance|regulatory",
        "Compliance decisions are human-owned.",
    ),
)


@dataclass
class Violation:
    rule: str
    stop_reason: str
    evidence: list[str]
    required_human_action: str
    forced_state: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "rule": self.rule,
            "stop_reason": self.stop_reason,
            "evidence": self.evidence,
            "required_human_action": self.required_human_action,
            "forced_state": self.forced_state,
        }


def _text(issue: dict[str, Any]) -> str:
    return " ".join(
        filter(
            None,
            [
                issue.get("title") or "",
                issue.get("description") or "",
                issue.get("recommended_action") or "",
                " ".join(issue.get("files") or []),
            ],
        )
    ).lower()


@dataclass(frozen=True)
class Subject:
    """One issue with the decision and configuration it is being checked against."""

    issue: dict[str, Any]
    match: Match
    decision: Decision
    config: Config

    @property
    def locator(self) -> str:
        return self.issue.get("source_reference") or self.issue["issue_id"]

    @property
    def text(self) -> str:
        return _text(self.issue)

    @property
    def implementable(self) -> bool:
        """Tier C and D are already restricted to inspection and proposal."""
        return self.decision.tier in {"A", "B"}


def _violation(rule: str, reason: str, evidence: str, action: str) -> Violation:
    return Violation(
        rule=rule,
        stop_reason=reason,
        evidence=[evidence],
        required_human_action=action,
        forced_state=State.BLOCKED.value,
    )


def _forbidden_domains(subject: Subject) -> list[Violation]:
    """Human-owned domains block only work that could otherwise be implemented."""
    if not subject.implementable:
        return []
    found = [
        (rule, re.search(pattern, subject.text), action)
        for rule, pattern, action in FORBIDDEN_PATTERNS
    ]
    return [
        _violation(
            rule,
            f"Issue text matches the human-owned domain {rule}; autonomous change is prohibited.",
            f"{subject.locator}: matched {hit.group(0)!r}",
            action,
        )
        for rule, hit, action in found
        if hit
    ]


def _environment_as_defect(subject: Subject) -> Violation | None:
    if not subject.issue.get("environment_signal"):
        return None
    if subject.issue.get("remediable") != "CODE_CHANGE":
        return None
    return _violation(
        "ENVIRONMENT_AS_CODE_DEFECT",
        "An environment/infrastructure failure was classified as a code change without "
        "independent verification.",
        f"{subject.locator}: environment_signal set with remediable=CODE_CHANGE",
        "Verify the infrastructure failure before opening code work.",
    )


def _rating_as_evidence(subject: Subject) -> Violation | None:
    if not subject.issue.get("corroborating_only"):
        return None
    if subject.issue.get("remediable") != "CODE_CHANGE":
        return None
    return _violation(
        "RATING_AS_DEFECT_EVIDENCE",
        "Employee rating data was used as evidence of a software defect.",
        f"{subject.locator}: corroborating_only source proposed as a code change",
        "Provide defect evidence independent of rating cards.",
    )


def _org_candidate_rejected(match: Match) -> bool:
    return any(entry.split(":", 1)[0].startswith("ORG_PB") for entry in match.rejected)


def _generic_over_org(subject: Subject) -> Violation | None:
    playbook = subject.match.playbook
    if playbook is None or playbook.scope != "GENERAL" or not subject.implementable:
        return None
    if not _org_candidate_rejected(subject.match):
        return None
    return _violation(
        "GENERIC_OVER_ORG_PLAYBOOK",
        "A general playbook was selected while an organization playbook was a candidate for "
        "the same issue.",
        f"{subject.locator}: rejected org candidates {subject.match.rejected}",
        "Resolve which organization playbook governs this issue.",
    )


def _dry_run_execution(subject: Subject) -> Violation | None:
    if not (subject.decision.execution_allowed and subject.config.dry_run_mode):
        return None
    return _violation(
        "DRY_RUN_EXECUTION_ATTEMPT",
        "Execution was marked allowed while dry-run mode is enabled.",
        f"{subject.locator}: dry_run_mode=True with execution_allowed=True",
        "Disable dry-run explicitly before any execution.",
    )


def _needs_failing_test(subject: Subject) -> bool:
    playbook = subject.match.playbook
    if playbook is None or not playbook.requires_failing_test_first:
        return False
    if subject.decision.tier != "A" or subject.issue.get("category") == "MISSING_TEST":
        return False
    return not (subject.issue.get("reproduction") or {}).get("available")


def _promotion_without_tests(subject: Subject) -> Violation | None:
    if not _needs_failing_test(subject):
        return None
    return _violation(
        "PROMOTION_WITHOUT_TESTS",
        "Playbook requires a failing test before the fix and no pre-fix failure exists.",
        f"{subject.locator}: requires_failing_test_first with no reproduction",
        "Produce the failing test evidence first.",
    )


CHECKS: tuple[Callable[[Subject], Violation | None], ...] = (
    _environment_as_defect,
    _rating_as_evidence,
    _generic_over_org,
    _dry_run_execution,
    _promotion_without_tests,
)


def evaluate(
    issue: dict[str, Any],
    match: Match,
    decision: Decision,
    config: Config,
) -> list[Violation]:
    """Return every guardrail violation for one issue."""
    subject = Subject(issue=issue, match=match, decision=decision, config=config)
    found = [check(subject) for check in CHECKS]
    return _forbidden_domains(subject) + [item for item in found if item is not None]

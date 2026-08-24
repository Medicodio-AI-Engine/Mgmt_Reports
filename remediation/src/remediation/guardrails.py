"""Guardrail engine.

Enforced in code, not left to prompt discipline. Each rule that fires records the
stop reason, the evidence it fired on, the human action required, and the state
the issue is forced into. A single violation is enough to stop the issue.
"""

from __future__ import annotations

import re
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


def evaluate(
    issue: dict[str, Any],
    match: Match,
    decision: Decision,
    config: Config,
) -> list[Violation]:
    """Return every guardrail violation for one issue."""
    violations: list[Violation] = []
    text = _text(issue)
    locator = issue.get("source_reference") or issue["issue_id"]

    # A human-owned domain only needs blocking when the issue could otherwise be
    # implemented. Tier C and D issues are already restricted to inspection and
    # proposal, which the specification explicitly permits on these surfaces.
    implementable = decision.tier in {"A", "B"}

    for rule, pattern, action in FORBIDDEN_PATTERNS:
        found = re.search(pattern, text)
        if not found or not implementable:
            continue
        violations.append(
            Violation(
                rule=rule,
                stop_reason=(
                    f"Issue text matches the human-owned domain {rule}; autonomous change is "
                    "prohibited."
                ),
                evidence=[f"{locator}: matched {found.group(0)!r}"],
                required_human_action=action,
                forced_state=State.BLOCKED.value,
            )
        )

    if issue.get("environment_signal") and issue.get("remediable") == "CODE_CHANGE":
        violations.append(
            Violation(
                rule="ENVIRONMENT_AS_CODE_DEFECT",
                stop_reason=(
                    "An environment/infrastructure failure was classified as a code change without "
                    "independent verification."
                ),
                evidence=[f"{locator}: environment_signal set with remediable=CODE_CHANGE"],
                required_human_action="Verify the infrastructure failure before opening code work.",
                forced_state=State.BLOCKED.value,
            )
        )

    if issue.get("corroborating_only") and issue.get("remediable") == "CODE_CHANGE":
        violations.append(
            Violation(
                rule="RATING_AS_DEFECT_EVIDENCE",
                stop_reason="Employee rating data was used as evidence of a software defect.",
                evidence=[f"{locator}: corroborating_only source proposed as a code change"],
                required_human_action="Provide defect evidence independent of rating cards.",
                forced_state=State.BLOCKED.value,
            )
        )

    if (
        match.playbook is not None
        and match.playbook.scope == "GENERAL"
        and any(candidate.split(":", 1)[0].startswith("ORG_PB") for candidate in match.rejected)
        and decision.tier in {"A", "B"}
    ):
        violations.append(
            Violation(
                rule="GENERIC_OVER_ORG_PLAYBOOK",
                stop_reason=(
                    "A general playbook was selected while an organization playbook was a "
                    "candidate for the same issue."
                ),
                evidence=[f"{locator}: rejected org candidates {match.rejected}"],
                required_human_action="Resolve which organization playbook governs this issue.",
                forced_state=State.BLOCKED.value,
            )
        )

    if decision.execution_allowed and config.dry_run_mode:
        violations.append(
            Violation(
                rule="DRY_RUN_EXECUTION_ATTEMPT",
                stop_reason="Execution was marked allowed while dry-run mode is enabled.",
                evidence=[f"{locator}: dry_run_mode=True with execution_allowed=True"],
                required_human_action="Disable dry-run explicitly before any execution.",
                forced_state=State.BLOCKED.value,
            )
        )

    if (
        match.playbook is not None
        and match.playbook.requires_failing_test_first
        and decision.tier == "A"
        and not (issue.get("reproduction") or {}).get("available")
        and issue.get("category") != "MISSING_TEST"
    ):
        violations.append(
            Violation(
                rule="PROMOTION_WITHOUT_TESTS",
                stop_reason=(
                    "Playbook requires a failing test before the fix and no pre-fix failure exists."
                ),
                evidence=[f"{locator}: requires_failing_test_first with no reproduction"],
                required_human_action="Produce the failing test evidence first.",
                forced_state=State.BLOCKED.value,
            )
        )

    return violations

"""Autonomy classification.

Tiers:

* ``A`` autonomous execution allowed (mechanical, deterministic, reversible)
* ``B`` implementation allowed, human approval mandatory before merge
* ``C`` investigation and proposal only until a human approves
* ``D`` human-owned; no autonomous modification at all

Priority and complexity never authorize remediation on their own. A tier can only
be lowered from the playbook default here, never raised.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .config import Config
from .playbooks import Match, Registry, missing_skill_reasons

TIER_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}

HUMAN_OWNED_SCOPES = frozenset(
    {"PHI", "SECRETS", "BILLING", "TENANT_ISOLATION", "AUTHENTICATION", "AUTHORIZATION"}
)
HUMAN_OWNED_CATEGORIES = frozenset({"SECURITY_TENANCY"})


@dataclass
class Decision:
    tier: str
    reasons: list[str] = field(default_factory=list)
    stop_conditions: list[str] = field(default_factory=list)
    execution_allowed: bool = False
    approval_required: bool = True

    def as_dict(self) -> dict[str, Any]:
        return {
            "autonomy_tier": self.tier,
            "autonomy_reasons": self.reasons,
            "execution_allowed": self.execution_allowed,
            "approval_required": self.approval_required,
            "stop_conditions": self.stop_conditions,
        }


def _lower_to(current: str, floor: str) -> str:
    return floor if TIER_ORDER[floor] > TIER_ORDER[current] else current


def classify(
    issue: dict[str, Any],
    match: Match,
    registry: Registry,
    config: Config,
) -> Decision:
    reasons: list[str] = []
    stops: list[str] = []

    if match.playbook is None:
        return Decision(
            tier="C",
            reasons=["no approved playbook matched; investigation and proposal only"],
            stop_conditions=["NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook"],
            execution_allowed=False,
            approval_required=True,
        )

    tier = match.playbook.default_autonomy_tier
    reasons.append(f"playbook {match.playbook.playbook_id} default tier {tier}")

    scope = issue.get("security_scope") or "UNKNOWN"
    if scope in HUMAN_OWNED_SCOPES or issue.get("category") in HUMAN_OWNED_CATEGORIES:
        tier = _lower_to(tier, "D")
        reasons.append(f"security-sensitive surface ({scope}) is human-owned")
        stops.append(f"HUMAN_OWNED_SURFACE: {scope} semantics require a human decision")
    elif scope == "UNKNOWN":
        tier = _lower_to(tier, "B")
        reasons.append("security scope could not be determined from the evidence")
        stops.append(
            "SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive"
        )

    if issue.get("environment_signal"):
        tier = _lower_to(tier, "C")
        reasons.append("environment signal must be verified as infrastructure before any code work")
        stops.append(
            "ENVIRONMENT_NOT_VERIFIED: confirm the failure is infrastructure, not a code defect"
        )

    remediable = issue.get("remediable")
    if remediable in {"NON_CODE_PROCESS", "UNKNOWN"}:
        tier = _lower_to(tier, "C")
        reasons.append(
            f"remediability {remediable}: no code change is justified from this evidence"
        )

    if issue.get("corroborating_only"):
        tier = _lower_to(tier, "C")
        reasons.append("rating-card corroboration only; not evidence of a software defect")
        stops.append("INSUFFICIENT_EVIDENCE: rating data cannot justify a change")

    complexity = (issue.get("complexity") or {}).get("score")
    if isinstance(complexity, int) and complexity > config.max_complexity_for_autonomy:
        tier = _lower_to(tier, "B")
        reasons.append(
            f"complexity {complexity} exceeds the autonomous ceiling "
            f"{config.max_complexity_for_autonomy}"
        )

    if issue.get("repository") is None:
        tier = _lower_to(tier, "C")
        reasons.append("target repository could not be determined from the report")
        stops.append("TARGET_UNRESOLVED: confirm the repository before any implementation")

    if match.missing_skills:
        tier = _lower_to(tier, "C")
        reasons.append("required capabilities are unavailable: " + ", ".join(match.missing_skills))
        stops.extend(
            f"MISSING_CAPABILITY: {reason}"
            for reason in missing_skill_reasons(match.missing_skills, registry)
        )

    if match.playbook.requires_reproduction and not (issue.get("reproduction") or {}).get(
        "available"
    ):
        tier = _lower_to(tier, "C")
        reasons.append("playbook requires a reproduction and none is available")
        stops.append("NO_REPRODUCTION: playbook requires a verified reproduction first")

    execution_allowed = (
        tier == "A" and not stops and config.remediation_allowed(issue.get("repository"))
    )
    if tier == "A" and not config.remediation_allowed(issue.get("repository")):
        reasons.append(
            "dry-run mode or repository not allowlisted: execution suppressed, plan only"
        )

    return Decision(
        tier=tier,
        reasons=reasons,
        stop_conditions=stops,
        execution_allowed=execution_allowed,
        approval_required=tier != "A",
    )

"""Autonomy classification.

Tiers:

* ``A`` autonomous execution allowed (mechanical, deterministic, reversible)
* ``B`` implementation allowed, human approval mandatory before merge
* ``C`` investigation and proposal only until a human approves
* ``D`` human-owned; no autonomous modification at all

Priority and complexity never authorize remediation on their own. A tier can only
be lowered from the playbook default here, never raised.

Each downgrade is one rule function returning a :class:`Constraint`. Adding a
safety rule means adding one small function to ``RULES`` — the classifier itself
does not change.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from . import scope as scope_module
from .config import Config
from .playbooks import Match, Registry, missing_skill_reasons

TIER_ORDER = {"A": 0, "B": 1, "C": 2, "D": 3}

HUMAN_OWNED_SCOPES = frozenset(
    {"PHI", "SECRETS", "BILLING", "TENANT_ISOLATION", "AUTHENTICATION", "AUTHORIZATION"}
)
HUMAN_OWNED_CATEGORIES = frozenset({"SECURITY_TENANCY"})
NON_CODE_REMEDIABILITY = frozenset({"NON_CODE_PROCESS", "UNKNOWN"})


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


@dataclass(frozen=True)
class Constraint:
    """One reason a tier is lowered, with the stop conditions it imposes."""

    floor: str
    reason: str
    stops: tuple[str, ...] = ()


@dataclass(frozen=True)
class Inputs:
    """Everything the rules may look at."""

    issue: dict[str, Any]
    match: Match
    registry: Registry
    config: Config


Rule = Callable[[Inputs], Constraint | None]


def _lower_to(current: str, floor: str) -> str:
    return floor if TIER_ORDER[floor] > TIER_ORDER[current] else current


def _no_playbook_decision() -> Decision:
    return Decision(
        tier="C",
        reasons=["no approved playbook matched; investigation and proposal only"],
        stop_conditions=["NO_PLAYBOOK_MATCH: human must approve an approach or add a playbook"],
        execution_allowed=False,
        approval_required=True,
    )


def _human_owned_rule(data: Inputs) -> Constraint | None:
    """Security-sensitive surfaces are never modified autonomously."""
    marker = data.issue.get("security_scope") or "UNKNOWN"
    if (
        marker not in HUMAN_OWNED_SCOPES
        and data.issue.get("category") not in HUMAN_OWNED_CATEGORIES
    ):
        return None
    return Constraint(
        floor="D",
        reason=f"security-sensitive surface ({marker}) is human-owned",
        stops=(f"HUMAN_OWNED_SURFACE: {marker} semantics require a human decision",),
    )


def _unverified_scope_rule(data: Inputs) -> Constraint | None:
    """An undetermined security surface may be prepared but not merged unreviewed."""
    if (data.issue.get("security_scope") or "UNKNOWN") != "UNKNOWN":
        return None
    return Constraint(
        floor="B",
        reason="security scope could not be determined from the evidence",
        stops=(
            "SECURITY_SCOPE_UNVERIFIED: a human must confirm the surface is not security-sensitive",
        ),
    )


def _environment_rule(data: Inputs) -> Constraint | None:
    if not data.issue.get("environment_signal"):
        return None
    return Constraint(
        floor="C",
        reason="environment signal must be verified as infrastructure before any code work",
        stops=(
            "ENVIRONMENT_NOT_VERIFIED: confirm the failure is infrastructure, not a code defect",
        ),
    )


def _remediability_rule(data: Inputs) -> Constraint | None:
    remediable = data.issue.get("remediable")
    if remediable not in NON_CODE_REMEDIABILITY:
        return None
    reason = f"remediability {remediable}: no code change is justified from this evidence"
    return Constraint(floor="C", reason=reason)


def _corroboration_rule(data: Inputs) -> Constraint | None:
    if not data.issue.get("corroborating_only"):
        return None
    return Constraint(
        floor="C",
        reason="rating-card corroboration only; not evidence of a software defect",
        stops=("INSUFFICIENT_EVIDENCE: rating data cannot justify a change",),
    )


def _complexity_rule(data: Inputs) -> Constraint | None:
    ceiling = data.config.max_complexity_for_autonomy
    complexity = (data.issue.get("complexity") or {}).get("score")
    if not isinstance(complexity, int) or complexity <= ceiling:
        return None
    return Constraint(
        floor="B", reason=f"complexity {complexity} exceeds the autonomous ceiling {ceiling}"
    )


def _target_rule(data: Inputs) -> Constraint | None:
    if data.issue.get("repository") is not None:
        return None
    return Constraint(
        floor="C",
        reason="target repository could not be determined from the report",
        stops=("TARGET_UNRESOLVED: confirm the repository before any implementation",),
    )


def _pilot_scope_rule(data: Inputs) -> Constraint | None:
    """Repositories outside the pilot are analysed but never touched."""
    if data.issue.get("analysis_scope") != scope_module.OUT_OF_SCOPE:
        return None
    return Constraint(
        floor="D",
        reason=str(data.issue.get("scope_reason") or "repository is outside the pilot scope"),
        stops=("OUT_OF_PILOT_SCOPE: widening the pilot is a human decision",),
    )


def _capability_rule(data: Inputs) -> Constraint | None:
    missing = data.match.missing_skills
    if not missing:
        return None
    return Constraint(
        floor="C",
        reason="required capabilities are unavailable: " + ", ".join(missing),
        stops=tuple(
            f"MISSING_CAPABILITY: {reason}"
            for reason in missing_skill_reasons(missing, data.registry)
        ),
    )


def _reproduction_rule(data: Inputs) -> Constraint | None:
    playbook = data.match.playbook
    if playbook is None or not playbook.requires_reproduction:
        return None
    if (data.issue.get("reproduction") or {}).get("available"):
        return None
    return Constraint(
        floor="C",
        reason="playbook requires a reproduction and none is available",
        stops=("NO_REPRODUCTION: playbook requires a verified reproduction first",),
    )


RULES: tuple[Rule, ...] = (
    _human_owned_rule,
    _unverified_scope_rule,
    _environment_rule,
    _remediability_rule,
    _corroboration_rule,
    _complexity_rule,
    _target_rule,
    _pilot_scope_rule,
    _capability_rule,
    _reproduction_rule,
)


def constraints(data: Inputs) -> list[Constraint]:
    """Every applicable downgrade, in rule order."""
    applied = [rule(data) for rule in RULES]
    return [constraint for constraint in applied if constraint is not None]


def _apply(tier: str, found: list[Constraint]) -> str:
    for constraint in found:
        tier = _lower_to(tier, constraint.floor)
    return tier


def _suppression_reason(data: Inputs, tier: str) -> list[str]:
    if tier != "A" or data.config.remediation_allowed(data.issue.get("repository")):
        return []
    return ["dry-run mode or repository not allowlisted: execution suppressed, plan only"]


def classify(
    issue: dict[str, Any],
    match: Match,
    registry: Registry,
    config: Config,
) -> Decision:
    """Decide how much autonomy one issue may be given."""
    if match.playbook is None:
        return _no_playbook_decision()
    data = Inputs(issue=issue, match=match, registry=registry, config=config)
    found = constraints(data)
    default = match.playbook.default_autonomy_tier
    tier = _apply(default, found)
    stops = [stop for constraint in found for stop in constraint.stops]
    reasons = [f"playbook {match.playbook.playbook_id} default tier {default}"]
    reasons += [constraint.reason for constraint in found] + _suppression_reason(data, tier)
    return Decision(
        tier=tier,
        reasons=reasons,
        stop_conditions=stops,
        execution_allowed=tier == "A"
        and not stops
        and config.remediation_allowed(issue.get("repository")),
        approval_required=tier != "A",
    )

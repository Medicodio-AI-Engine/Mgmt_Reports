"""Time-to-fix estimates in ``HH:MM``.

Three estimates per issue: human-only, AI-only, and human-with-AI. They are
derived deterministically from the analysed complexity, the remediability and the
autonomy tier — they are planning figures, not measurements, and the supervisor
report says so.

Where autonomy policy forbids AI execution (tier C and D), the AI figure covers
investigation and proposal only, and the joint figure carries the human decision
time that must follow.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

# Minutes of human work for one complexity point, by remediability.
HUMAN_MINUTES_PER_POINT: dict[str, int] = {
    "CODE_CHANGE": 60,
    "TOOLING_AUTOMATION": 50,
    "NON_CODE_PROCESS": 30,
    "UNKNOWN": 45,
}
# Share of the human time an AI run needs for the same work.
AI_SHARE: dict[str, float] = {
    "CODE_CHANGE": 0.35,
    "TOOLING_AUTOMATION": 0.30,
    "NON_CODE_PROCESS": 0.50,
    "UNKNOWN": 0.60,
}
# Fixed human review time added to any AI-produced result, in minutes.
REVIEW_MINUTES = 30
# Tiers where the AI may investigate and propose but not implement.
PROPOSAL_ONLY_TIERS = frozenset({"C", "D"})


@dataclass(frozen=True)
class Estimate:
    """Three ``HH:MM`` figures and the basis they were derived from."""

    human: str
    ai: str
    joint: str
    basis: tuple[str, ...]

    def as_dict(self) -> dict[str, Any]:
        return {
            "time_human": self.human,
            "time_ai": self.ai,
            "time_human_ai": self.joint,
            "estimate_basis": list(self.basis),
        }


def as_hhmm(minutes: int) -> str:
    """Format whole minutes as ``HH:MM``."""
    if minutes < 0:
        raise ValueError("minutes cannot be negative")
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def _round_to_quarter(minutes: float) -> int:
    return max(15, round(minutes / 15.0) * 15)


def _human_minutes(complexity: int, remediable: str) -> int:
    per_point = HUMAN_MINUTES_PER_POINT.get(remediable, HUMAN_MINUTES_PER_POINT["UNKNOWN"])
    return _round_to_quarter(per_point * max(1, complexity))


def _ai_minutes(human_minutes: int, remediable: str, proposal_only: bool) -> int:
    share = AI_SHARE.get(remediable, AI_SHARE["UNKNOWN"])
    return _round_to_quarter(human_minutes * (0.25 if proposal_only else share))


def _joint_minutes(ai_minutes: int, human_minutes: int, proposal_only: bool) -> int:
    if proposal_only:
        # The AI prepares evidence; a human still does the change and the decision.
        return _round_to_quarter(ai_minutes + human_minutes)
    return _round_to_quarter(ai_minutes + REVIEW_MINUTES)


def _basis(
    complexity: int, remediable: str, tier: str | None, proposal_only: bool
) -> tuple[str, ...]:
    basis = [
        f"complexity {complexity}",
        f"remediability {remediable}",
        f"autonomy tier {tier or '—'}",
    ]
    if proposal_only:
        basis.append("tier permits investigation and proposal only, so a human does the change")
    return tuple(basis)


def estimate(complexity: int, remediable: str, tier: str | None) -> Estimate:
    """Estimate human, AI, and joint time for one issue."""
    proposal_only = (tier or "").upper() in PROPOSAL_ONLY_TIERS
    human = _human_minutes(complexity, remediable)
    ai = _ai_minutes(human, remediable, proposal_only)
    return Estimate(
        human=as_hhmm(human),
        ai=as_hhmm(ai),
        joint=as_hhmm(_joint_minutes(ai, human, proposal_only)),
        basis=_basis(complexity, remediable, tier, proposal_only),
    )


def for_issue(issue: dict[str, Any]) -> Estimate:
    """Estimate from a normalized, scored, classified issue."""
    complexity = int((issue.get("complexity") or {}).get("score", 5))
    tier = issue.get("autonomy_tier")
    remediable = str(issue.get("remediable") or "UNKNOWN")
    return estimate(complexity, remediable, str(tier) if tier else None)

"""Time-to-fix estimates in ``HH:MM``.

Three estimates per issue: the time a person needs alone, the time Devin needs
alone, and the elapsed time when the two collaborate. They are derived
deterministically from the analysed complexity, the remediability and the
autonomy tier — they are planning figures, not measurements, and the supervisor
report says so.

The collaboration figure is deliberately **not** the sum of the other two: the
AI drafts and the person directs and reviews, so the person spends a share of
what they would spend alone. It is capped at the solo-human figure, because
collaborating is never presented as slower than doing it yourself.

Where autonomy policy forbids AI execution (tier C and D), the AI figure covers
investigation and proposal only, and the person still makes the change — with
the investigation already done for them.

The AI figures are a small fraction of the human ones: writing and changing code
is the part it does fastest, so a task a person spends hours on is minutes of AI
work plus the review the person owns.
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
# Share of the human time an AI run needs for the same work. Writing the code is
# where the AI is fastest, so these are small; process and judgement work, where
# the words matter more than the typing, gains less.
AI_SHARE: dict[str, float] = {
    "CODE_CHANGE": 0.12,
    "TOOLING_AUTOMATION": 0.12,
    "NON_CODE_PROCESS": 0.25,
    "UNKNOWN": 0.20,
}
# Share of the human time the AI needs to investigate and write up a proposal on a
# change policy forbids it from making itself.
PROPOSAL_SHARE = 0.08
# Fixed human review time added to any AI-produced result, in minutes.
REVIEW_MINUTES = 30
# Share of the solo-human time a person still spends while collaborating: directing
# and reviewing the AI's work on a change policy will not let the AI land itself.
# Below 1.0 because the investigation and the draft arrive already done.
COLLABORATION_HUMAN_SHARE = 0.5
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
    return _round_to_quarter(human_minutes * (PROPOSAL_SHARE if proposal_only else share))


def _joint_minutes(ai_minutes: int, human_minutes: int, proposal_only: bool) -> int:
    """Elapsed collaboration time: a share of the solo-human time, never the sum."""
    if proposal_only:
        # The AI investigates and proposes; the person makes the change from there.
        together = ai_minutes + COLLABORATION_HUMAN_SHARE * human_minutes
    else:
        together = ai_minutes + REVIEW_MINUTES
    return min(_round_to_quarter(together), human_minutes)


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

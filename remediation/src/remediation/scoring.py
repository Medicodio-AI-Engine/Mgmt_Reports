"""Priority and complexity scoring.

Two independent 1–10 scores, each with the factors that produced it. Neither
score authorizes remediation; they only order the work. Priority answers "how
much does this matter"; complexity answers "how hard and how risky is the change".
"""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

_NUMBER = re.compile(r"\d+")

# One score adjustment: how much, and the factor text that explains it.
Adjustment = tuple[int, str]
Rule = Callable[[dict[str, Any]], "Adjustment | None"]

PRIORITY_BASE = 3

SECURITY_WEIGHT = {
    "PHI": 4,
    "TENANT_ISOLATION": 4,
    "AUTHORIZATION": 3,
    "AUTHENTICATION": 3,
    "SECRETS": 3,
    "BILLING": 3,
    "UNKNOWN": 0,
    "NONE": 0,
}

CATEGORY_PRIORITY = {
    "CODE_DEFECT": 3,
    "SECURITY_TENANCY": 4,
    "CI_FAILURE": 3,
    "MISSING_TEST": 2,
    "QA_FINDING": 2,
    "MECHANICAL_MIGRATION": 1,
    "REVIEW_FINDING": 1,
    "CODE_QUALITY": 1,
    "AUTOMATION_OPPORTUNITY": 1,
    "PROCESS_PRACTICE": 0,
    "UNKNOWN": 0,
}

CATEGORY_COMPLEXITY = {
    "MISSING_TEST": 3,
    "MECHANICAL_MIGRATION": 4,
    "CODE_QUALITY": 4,
    "AUTOMATION_OPPORTUNITY": 4,
    "QA_FINDING": 5,
    "REVIEW_FINDING": 4,
    "CODE_DEFECT": 6,
    "CI_FAILURE": 7,
    "SECURITY_TENANCY": 9,
    "PROCESS_PRACTICE": 5,
    "UNKNOWN": 7,
}


@dataclass
class Score:
    value: int
    factors: list[str] = field(default_factory=list)
    rationale: str = ""
    confidence: float = 0.5

    def as_dict(self) -> dict[str, Any]:
        return {
            "score": self.value,
            "factors": self.factors,
            "rationale": self.rationale,
            "confidence": self.confidence,
        }


def _clamp(value: int) -> int:
    return max(1, min(10, value))


def _largest_number(text: str | None) -> int | None:
    if not text:
        return None
    values = [int(value) for value in _NUMBER.findall(text)]
    return max(values) if values else None


def _category_priority(issue: dict[str, Any]) -> Adjustment | None:
    category = issue["category"]
    bump = CATEGORY_PRIORITY.get(category, 0)
    return (bump, f"category {category} (+{bump})") if bump else None


def _security_priority(issue: dict[str, Any]) -> Adjustment | None:
    marker = issue["security_scope"]
    weight = SECURITY_WEIGHT.get(marker, 0)
    return (weight, f"security scope {marker} (+{weight})") if weight else None


def _support_priority(issue: dict[str, Any]) -> Adjustment | None:
    """Repeated independent reporting raises priority."""
    support = len(issue.get("merged_sources") or [])
    if support >= 3:
        return (2, f"reported {support} times across sources (+2)")
    return (1, "reported twice across sources (+1)") if support == 2 else None


def _frequency_priority(issue: dict[str, Any]) -> Adjustment | None:
    if not (issue.get("recommended_action") and issue.get("frequency")):
        return None
    occurrences = _largest_number(issue["frequency"])
    if not occurrences or occurrences < 10:
        return None
    return (1, f"high reported frequency ({occurrences}) (+1)")


def _non_code_priority(issue: dict[str, Any]) -> Adjustment | None:
    if issue["remediable"] != "NON_CODE_PROCESS":
        return None
    return (-1, "non-code process item, no software risk (-1)")


def _corroboration_priority(issue: dict[str, Any]) -> Adjustment | None:
    if not issue.get("corroborating_only"):
        return None
    return (-2, "rating-card corroboration only, not defect evidence (-2)")


PRIORITY_RULES: tuple[Rule, ...] = (
    _category_priority,
    _security_priority,
    _support_priority,
    _frequency_priority,
    _non_code_priority,
    _corroboration_priority,
)


def _unresolved_repository_complexity(issue: dict[str, Any]) -> Adjustment | None:
    if issue["repository"] is not None:
        return None
    return (2, "target repository not determined from the report (+2)")


def _no_paths_complexity(issue: dict[str, Any]) -> Adjustment | None:
    return None if issue["files"] else (1, "no file paths identified (+1)")


def _security_complexity(issue: dict[str, Any]) -> Adjustment | None:
    marker = issue["security_scope"]
    if marker in {"NONE", "UNKNOWN"}:
        return None
    return (2, f"security-sensitive surface {marker} (+2)")


def _multi_repository_complexity(issue: dict[str, Any]) -> Adjustment | None:
    if len(issue.get("candidate_repositories") or []) <= 1:
        return None
    return (1, "spans multiple candidate repositories (+1)")


def _environment_complexity(issue: dict[str, Any]) -> Adjustment | None:
    if not issue.get("environment_signal"):
        return None
    return (1, "depends on infrastructure outside the codebase (+1)")


def _known_target_complexity(issue: dict[str, Any]) -> Adjustment | None:
    if not (issue["files"] and issue["repository"]):
        return None
    return (-1, "repository and paths both known (-1)")


COMPLEXITY_RULES: tuple[Rule, ...] = (
    _unresolved_repository_complexity,
    _no_paths_complexity,
    _security_complexity,
    _multi_repository_complexity,
    _environment_complexity,
    _known_target_complexity,
)


def adjustments(issue: dict[str, Any], rules: tuple[Rule, ...]) -> list[Adjustment]:
    """Every applicable adjustment, in rule order."""
    applied = [rule(issue) for rule in rules]
    return [item for item in applied if item is not None]


def _total(base: int, applied: list[Adjustment]) -> int:
    return _clamp(base + sum(delta for delta, _ in applied))


def priority(issue: dict[str, Any]) -> Score:
    """How much this issue matters, 1–10."""
    applied = adjustments(issue, PRIORITY_RULES)
    factors = [factor for _, factor in applied]
    value = _total(PRIORITY_BASE, applied)
    detail = "; ".join(factors) if factors else "no adjusting factors"
    return Score(
        value=value,
        factors=factors,
        rationale=f"Priority {value}/10 from base {PRIORITY_BASE} adjusted by: {detail}.",
        confidence=float(issue.get("confidence") or 0.5),
    )


def complexity(issue: dict[str, Any]) -> Score:
    """How hard and how risky the change is, 1–10."""
    base = CATEGORY_COMPLEXITY.get(issue["category"], 7)
    applied = adjustments(issue, COMPLEXITY_RULES)
    factors = [f"category {issue['category']} base {base}"] + [f for _, f in applied]
    value = _total(base, applied)
    return Score(
        value=value,
        factors=factors,
        rationale=f"Complexity {value}/10 from: " + "; ".join(factors) + ".",
        confidence=round(min(0.8, float(issue.get("confidence") or 0.5) + 0.1), 2),
    )


def score(issue: dict[str, Any]) -> dict[str, Any]:
    return {"priority": priority(issue).as_dict(), "complexity": complexity(issue).as_dict()}

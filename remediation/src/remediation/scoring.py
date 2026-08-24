"""Priority and complexity scoring.

Two independent 1–10 scores, each with the factors that produced it. Neither
score authorizes remediation; they only order the work. Priority answers "how
much does this matter"; complexity answers "how hard and how risky is the change".
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

_NUMBER = re.compile(r"\d+")

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


def priority(issue: dict[str, Any]) -> Score:
    factors: list[str] = []
    score = 3
    category = issue["category"]
    bump = CATEGORY_PRIORITY.get(category, 0)
    if bump:
        score += bump
        factors.append(f"category {category} (+{bump})")

    scope = issue["security_scope"]
    weight = SECURITY_WEIGHT.get(scope, 0)
    if weight:
        score += weight
        factors.append(f"security scope {scope} (+{weight})")

    support = len(issue.get("merged_sources") or [])
    if support >= 3:
        score += 2
        factors.append(f"reported {support} times across sources (+2)")
    elif support == 2:
        score += 1
        factors.append("reported twice across sources (+1)")

    if issue.get("recommended_action") and issue.get("frequency"):
        occurrences = _largest_number(issue["frequency"])
        if occurrences and occurrences >= 10:
            score += 1
            factors.append(f"high reported frequency ({occurrences}) (+1)")

    if issue["remediable"] == "NON_CODE_PROCESS":
        score -= 1
        factors.append("non-code process item, no software risk (-1)")

    if issue.get("corroborating_only"):
        score -= 2
        factors.append("rating-card corroboration only, not defect evidence (-2)")

    value = _clamp(score)
    rationale = (
        f"Priority {value}/10 from base 3 adjusted by: "
        + ("; ".join(factors) if factors else "no adjusting factors")
        + "."
    )
    return Score(
        value=value,
        factors=factors,
        rationale=rationale,
        confidence=float(issue.get("confidence") or 0.5),
    )


def complexity(issue: dict[str, Any]) -> Score:
    factors: list[str] = []
    score = CATEGORY_COMPLEXITY.get(issue["category"], 7)
    factors.append(f"category {issue['category']} base {score}")

    if issue["repository"] is None:
        score += 2
        factors.append("target repository not determined from the report (+2)")
    if not issue["files"]:
        score += 1
        factors.append("no file paths identified (+1)")
    if issue["security_scope"] not in {"NONE", "UNKNOWN"}:
        score += 2
        factors.append(f"security-sensitive surface {issue['security_scope']} (+2)")
    if len(issue.get("candidate_repositories") or []) > 1:
        score += 1
        factors.append("spans multiple candidate repositories (+1)")
    if issue.get("environment_signal"):
        score += 1
        factors.append("depends on infrastructure outside the codebase (+1)")
    if issue["files"] and issue["repository"]:
        score -= 1
        factors.append("repository and paths both known (-1)")

    value = _clamp(score)
    rationale = f"Complexity {value}/10 from: " + "; ".join(factors) + "."
    return Score(
        value=value,
        factors=factors,
        rationale=rationale,
        confidence=round(min(0.8, float(issue.get("confidence") or 0.5) + 0.1), 2),
    )


def score(issue: dict[str, Any]) -> dict[str, Any]:
    return {"priority": priority(issue).as_dict(), "complexity": complexity(issue).as_dict()}

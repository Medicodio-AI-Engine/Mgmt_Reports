"""Bug versus enhancement, as reported and as analysed.

Two independent labels per issue:

* ``reported`` — what the report's own wording implies.
* ``revised`` — what the evidence supports after analysis.

A *bug* is functionality that exists and does not work. An *enhancement* is
functionality that does not exist yet and has to be built. A report often files
an enhancement as a bug, so the two labels are produced separately and compared;
``Category_Match`` is simply whether they agree.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

BUG = "BUG"
ENHANCEMENT = "ENHANCEMENT"

DEFECT_WORDS = re.compile(
    r"\b(fail(s|ed|ing|ure)?|break(s|ing)?|broken|error(s)?|bug(s)?|defect(s)?|regress(ion|ed)?"
    r"|incorrect|wrong|crash(es|ed)?|blocked|cancelled|drift(ed|ing)?|stale|mismatch)\b",
    re.IGNORECASE,
)

# Categories where the capability itself has to be built before anything can be
# fixed, so the honest label is enhancement even when the report says otherwise.
ENHANCEMENT_CATEGORIES = frozenset(
    {
        "MISSING_TEST",
        "AUTOMATION_OPPORTUNITY",
        "MECHANICAL_MIGRATION",
        "PROCESS_PRACTICE",
        "SECURITY_TENANCY",
    }
)
BUG_CATEGORIES = frozenset({"CODE_DEFECT", "CI_FAILURE"})


@dataclass(frozen=True)
class Categories:
    """The reported label, the analysed label, and whether they agree."""

    reported: str
    revised: str
    rationale: str

    @property
    def matched(self) -> bool:
        return self.reported == self.revised

    def as_dict(self) -> dict[str, object]:
        return {
            "reported_category": self.reported,
            "revised_category": self.revised,
            "category_match": self.matched,
            "category_rationale": self.rationale,
        }


def reported(text: str) -> str:
    """Label from the report's wording alone.

    Defect wording wins over absence wording: a report claiming something fails is
    filed as a bug, and analysis is what may later revise it to an enhancement.
    """
    return BUG if DEFECT_WORDS.search(text) else ENHANCEMENT


def _revised_from_category(category: str) -> str | None:
    if category in BUG_CATEGORIES:
        return BUG
    if category in ENHANCEMENT_CATEGORIES:
        return ENHANCEMENT
    return None


def revised(category: str, text: str) -> str:
    """Label from the analysed category, falling back to the wording."""
    from_category = _revised_from_category(category)
    return from_category if from_category is not None else reported(text)


def _rationale(reported_label: str, revised_label: str, category: str) -> str:
    if reported_label == revised_label:
        return f"category {category} confirms the reported {reported_label.lower()}"
    return (
        f"reported as {reported_label.lower()} but category {category} shows "
        f"{'existing behaviour is broken' if revised_label == BUG else 'the capability does not exist yet'}"
        f", so it is an {revised_label.lower()}"
    )


def evaluate(category: str, text: str) -> Categories:
    """Produce both labels and the reason they agree or differ."""
    reported_label = reported(text)
    revised_label = revised(category, text)
    return Categories(
        reported=reported_label,
        revised=revised_label,
        rationale=_rationale(reported_label, revised_label, category),
    )

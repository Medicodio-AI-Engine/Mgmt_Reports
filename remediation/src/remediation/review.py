"""Human review (stage 05_DEV_REVIEW).

Review happens through a ``DECISION`` block committed into the stage artifact in
this repository. Exactly three outcomes are accepted: ``APPROVE``,
``REVIEW`` (ask a question), and ``REJECT``. Anything else, including an empty or
malformed block, is treated as ``PENDING`` and nothing advances.

A block is addressed to one attempt, so a decision applies once: a rejection
committed against ``ATTEMPT_01`` does not re-reject the attempt it opened.

Version 1 never promotes an approved issue past ``DEV_REVIEW``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

from .naming import next_attempt
from .states import State, transition

BLOCK_HEADING = re.compile(
    r"^#{1,6}\s*DECISION:\s*(ISSUE_\d{6})(_ATTEMPT_\d{2})?\s*$", re.MULTILINE
)
FIELD = re.compile(r"^(DECISION|REVIEWER|COMMENTS|QUESTIONS|ANSWERS)\s*:\s*(.*)$", re.IGNORECASE)


class Outcome(str, Enum):
    APPROVE = "APPROVE"
    REVIEW = "REVIEW"
    REJECT = "REJECT"
    PENDING = "PENDING"


_ALIASES = {
    "APPROVE": Outcome.APPROVE,
    "APPROVED": Outcome.APPROVE,
    "REVIEW": Outcome.REVIEW,
    "ASK QUESTION": Outcome.REVIEW,
    "ASK": Outcome.REVIEW,
    "QUESTION": Outcome.REVIEW,
    "REJECT": Outcome.REJECT,
    "REJECTED": Outcome.REJECT,
}


@dataclass
class Decision:
    issue_id: str
    outcome: Outcome
    attempt_id: str | None = None
    reviewer: str | None = None
    comments: list[str] = field(default_factory=list)
    questions: list[str] = field(default_factory=list)
    answers: list[str] = field(default_factory=list)
    malformed: str | None = None
    source_file: str | None = None

    @property
    def key(self) -> str:
        """The attempt this decision is addressed to, or the issue if unscoped."""
        return self.attempt_id or self.issue_id

    def as_dict(self) -> dict[str, Any]:
        return {
            "issue_id": self.issue_id,
            "attempt_id": self.attempt_id,
            "human_review_result": self.outcome.value,
            "reviewer": self.reviewer,
            "reviewer_comments": self.comments,
            "questions": self.questions,
            "answers": self.answers,
            "malformed": self.malformed,
            "source_file": self.source_file,
        }


def _split_items(value: str) -> list[str]:
    parts = [part.strip(" -•\t") for part in re.split(r"\s*(?:\||;|\n)\s*", value)]
    return [part for part in parts if part]


def parse_decisions(text: str, *, source_file: str | None = None) -> dict[str, Decision]:
    """Parse every ``DECISION`` block in an artifact file."""
    decisions: dict[str, Decision] = {}
    matches = list(BLOCK_HEADING.finditer(text))
    for index, match in enumerate(matches):
        issue = match.group(1)
        attempt = f"{issue}{match.group(2)}" if match.group(2) else None
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.end() : end]
        raw: dict[str, str] = {}
        for line in body.splitlines():
            field_match = FIELD.match(line.strip())
            if field_match:
                key = field_match.group(1).upper()
                raw[key] = f"{raw.get(key, '')} {field_match.group(2)}".strip()
        stated = re.sub(r"#.*$", "", raw.get("DECISION", "")).strip().upper()
        outcome = _ALIASES.get(stated, Outcome.PENDING)
        malformed = None
        if "DECISION" not in raw:
            # Every generated block carries `DECISION: PENDING`, so a block without the
            # line has been edited into a state the reviewer cannot see is broken.
            malformed = "block has no DECISION: line; treated as PENDING"
        elif stated and outcome is Outcome.PENDING and stated != "PENDING":
            malformed = f"unrecognized decision value {stated!r}; treated as PENDING"
        questions = _split_items(raw.get("QUESTIONS", ""))
        if outcome is Outcome.REVIEW and not questions:
            malformed = "REVIEW requires at least one question; treated as PENDING"
            outcome = Outcome.PENDING
        decisions[attempt or issue] = Decision(
            issue_id=issue,
            attempt_id=attempt,
            outcome=outcome,
            reviewer=raw.get("REVIEWER") or None,
            comments=_split_items(raw.get("COMMENTS", "")),
            questions=questions,
            answers=_split_items(raw.get("ANSWERS", "")),
            malformed=malformed,
            source_file=source_file,
        )
    return decisions


def load_decisions(directory: Path) -> dict[str, Decision]:
    """Collect decisions from every markdown artifact under ``directory``.

    Keyed by attempt id where the block names one, so an older attempt's decision
    never leaks onto a newer attempt.
    """
    collected: dict[str, Decision] = {}
    if not directory.is_dir():
        return collected
    for path in sorted(directory.rglob("*.md")):
        for key, decision in parse_decisions(
            path.read_text(encoding="utf-8", errors="replace"), source_file=str(path)
        ).items():
            existing = collected.get(key)
            if existing is None or existing.outcome is Outcome.PENDING:
                collected[key] = decision
    return collected


def decision_block(attempt_id: str, title: str) -> str:
    """The block a reviewer edits in place, addressed to one attempt."""
    return "\n".join(
        [
            f"### DECISION: {attempt_id}",
            f"<!-- {title} -->",
            "<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->",
            "DECISION: PENDING",
            "REVIEWER:",
            "COMMENTS:",
            "QUESTIONS:",
            "",
        ]
    )


def apply_decision(issue: dict[str, Any], decision: Decision) -> dict[str, Any]:
    """Apply a review outcome. Approval does not promote past DEV_REVIEW in V1."""
    current = State(issue.get("state", State.DEV_REVIEW.value))
    result: dict[str, Any] = {
        "human_review_result": decision.outcome.value,
        "reviewer": decision.reviewer,
        "reviewer_comments": decision.comments,
        "questions": decision.questions,
        "answers": decision.answers,
        "attempt_id": issue["attempt_id"],
        "state": current.value,
        "next_state": current.value,
        "notes": [],
    }
    if decision.malformed:
        result["notes"].append(decision.malformed)

    if decision.outcome is Outcome.APPROVE:
        result["notes"].append(
            "Approved. Version 1 stops at DEV_REVIEW: promotion to QA, UAT, and release remains "
            "disabled and human-owned."
        )
        return result

    if decision.outcome is Outcome.REVIEW:
        result["notes"].append(
            "Questions recorded. The issue stays in DEV_REVIEW until they are answered."
        )
        return result

    if decision.outcome is Outcome.REJECT:
        record = transition(current, State.DEV_FIXING, "review rejected; new attempt opened")
        new_attempt = next_attempt(issue["attempt_id"])
        result.update(
            {
                "attempt_id": new_attempt,
                "superseded_attempt_id": issue["attempt_id"],
                "state": record.to_state.value,
                "next_state": record.to_state.value,
            }
        )
        result["notes"].append(
            f"Rejected. {issue['attempt_id']} is preserved immutably; {new_attempt} opened in "
            "DEV_FIXING. Corrections are applied only where the autonomy policy permits."
        )
        return result

    result["notes"].append("No decision recorded; nothing advances.")
    return result

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


def _fields(body: str) -> dict[str, str]:
    """The ``KEY: value`` lines of one block, repeated keys joined."""
    raw: dict[str, str] = {}
    for line in body.splitlines():
        field_match = FIELD.match(line.strip())
        if field_match is None:
            continue
        key = field_match.group(1).upper()
        raw[key] = f"{raw.get(key, '')} {field_match.group(2)}".strip()
    return raw


def _stated_value(raw: dict[str, str]) -> str:
    """The DECISION value with any trailing comment stripped."""
    return re.sub(r"#.*$", "", raw.get("DECISION", "")).strip().upper()


def _malformed_reason(raw: dict[str, str], stated: str, outcome: Outcome) -> str | None:
    if "DECISION" not in raw:
        # Every generated block carries `DECISION: PENDING`, so a block without the
        # line has been edited into a state the reviewer cannot see is broken.
        return "block has no DECISION: line; treated as PENDING"
    if stated and outcome is Outcome.PENDING and stated != "PENDING":
        return f"unrecognized decision value {stated!r}; treated as PENDING"
    return None


def _resolve_outcome(raw: dict[str, str], questions: list[str]) -> tuple[Outcome, str | None]:
    """The accepted outcome, and why it was downgraded if it was."""
    stated = _stated_value(raw)
    outcome = _ALIASES.get(stated, Outcome.PENDING)
    if outcome is Outcome.REVIEW and not questions:
        return Outcome.PENDING, "REVIEW requires at least one question; treated as PENDING"
    return outcome, _malformed_reason(raw, stated, outcome)


def _block_decision(
    issue: str, attempt: str | None, body: str, source_file: str | None
) -> Decision:
    raw = _fields(body)
    questions = _split_items(raw.get("QUESTIONS", ""))
    outcome, malformed = _resolve_outcome(raw, questions)
    return Decision(
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


def _block_bounds(matches: list[re.Match[str]], index: int, text: str) -> tuple[int, int]:
    following = matches[index + 1].start() if index + 1 < len(matches) else len(text)
    return matches[index].end(), following


def parse_decisions(text: str, *, source_file: str | None = None) -> dict[str, Decision]:
    """Parse every ``DECISION`` block in an artifact file."""
    decisions: dict[str, Decision] = {}
    matches = list(BLOCK_HEADING.finditer(text))
    for index, match in enumerate(matches):
        issue = match.group(1)
        attempt = f"{issue}{match.group(2)}" if match.group(2) else None
        start, end = _block_bounds(matches, index, text)
        decisions[attempt or issue] = _block_decision(issue, attempt, text[start:end], source_file)
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


APPROVE_NOTE = (
    "Approved. Version 1 stops at DEV_REVIEW: promotion to QA, UAT, and release remains "
    "disabled and human-owned."
)
REVIEW_NOTE = "Questions recorded. The issue stays in DEV_REVIEW until they are answered."
PENDING_NOTE = "No decision recorded; nothing advances."


def _base_result(issue: dict[str, Any], decision: Decision, current: State) -> dict[str, Any]:
    return {
        "human_review_result": decision.outcome.value,
        "reviewer": decision.reviewer,
        "reviewer_comments": decision.comments,
        "questions": decision.questions,
        "answers": decision.answers,
        "attempt_id": issue["attempt_id"],
        "state": current.value,
        "next_state": current.value,
        "notes": [decision.malformed] if decision.malformed else [],
    }


def _reject(issue: dict[str, Any], result: dict[str, Any], current: State) -> None:
    """Preserve the rejected attempt and open its successor in DEV_FIXING."""
    record = transition(current, State.DEV_FIXING, "review rejected; new attempt opened")
    new_attempt = next_attempt(issue["attempt_id"])
    result["attempt_id"] = new_attempt
    result["superseded_attempt_id"] = issue["attempt_id"]
    result["state"] = record.to_state.value
    result["next_state"] = record.to_state.value
    result["notes"].append(
        f"Rejected. {issue['attempt_id']} is preserved immutably; {new_attempt} opened in "
        "DEV_FIXING. Corrections are applied only where the autonomy policy permits."
    )


def apply_decision(issue: dict[str, Any], decision: Decision) -> dict[str, Any]:
    """Apply a review outcome. Approval does not promote past DEV_REVIEW in V1."""
    current = State(issue.get("state", State.DEV_REVIEW.value))
    result = _base_result(issue, decision, current)
    if decision.outcome is Outcome.REJECT:
        _reject(issue, result, current)
        return result
    notes = {Outcome.APPROVE: APPROVE_NOTE, Outcome.REVIEW: REVIEW_NOTE}
    result["notes"].append(notes.get(decision.outcome, PENDING_NOTE))
    return result

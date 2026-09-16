"""Immutable attempt history.

The store is append-only JSONL holding two kinds of record:

``ATTEMPT_OPENED``
    One per attempt, written once. A rejection never rewrites it; it opens the
    next attempt instead, so what was tried and why it was refused survives.
``REVIEW_DECISION``
    One per (attempt, outcome). The decision is a separate fact about an attempt
    rather than a mutation of it.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .naming import ATTEMPT_ID

ATTEMPT_OPENED = "ATTEMPT_OPENED"
REVIEW_DECISION = "REVIEW_DECISION"


class AttemptImmutabilityError(RuntimeError):
    """Raised on any attempt to modify a recorded attempt."""


def _number(attempt_id: str) -> int:
    return int(attempt_id.rsplit("_", 1)[1])


@dataclass
class AttemptStore:
    path: Path

    def __post_init__(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def all(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        return [
            json.loads(line)
            for line in self.path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def attempts(self) -> list[dict[str, Any]]:
        return [record for record in self.all() if record.get("kind") == ATTEMPT_OPENED]

    def decisions(self) -> list[dict[str, Any]]:
        return [record for record in self.all() if record.get("kind") == REVIEW_DECISION]

    def for_issue(self, issue_id: str) -> list[dict[str, Any]]:
        return [record for record in self.attempts() if record["issue_id"] == issue_id]

    def latest(self, issue_id: str) -> dict[str, Any] | None:
        records = self.for_issue(issue_id)
        return records[-1] if records else None

    def next_number(self, issue_id: str) -> int:
        """The number a brand-new attempt for ``issue_id`` should carry."""
        return max((_number(r["attempt_id"]) for r in self.for_issue(issue_id)), default=0) + 1

    def current_number(self, issue_id: str) -> int:
        """The attempt an incoming run should write to.

        Re-analyzing an issue nobody has rejected stays on the open attempt; a
        rejection is what opens the next one.
        """
        opened = max((_number(r["attempt_id"]) for r in self.for_issue(issue_id)), default=0)
        if opened == 0:
            return 1
        rejected = {
            _number(record["attempt_id"])
            for record in self.decisions()
            if record["issue_id"] == issue_id and record.get("result") == "REJECT"
        }
        return opened + 1 if opened in rejected else opened

    def open_attempt(self, record: dict[str, Any]) -> dict[str, Any]:
        """Record a new attempt. Raises if the attempt id already exists."""
        attempt_id = record.get("attempt_id")
        if not attempt_id or not ATTEMPT_ID.match(attempt_id):
            raise AttemptImmutabilityError(f"invalid attempt id {attempt_id!r}")
        if any(existing["attempt_id"] == attempt_id for existing in self.attempts()):
            raise AttemptImmutabilityError(
                f"{attempt_id} already recorded; attempts are immutable — open a new attempt"
            )
        return self._write({**record, "kind": ATTEMPT_OPENED})

    def open_attempt_if_absent(self, record: dict[str, Any]) -> dict[str, Any] | None:
        """Record a new attempt unless its id is already on file."""
        if any(existing["attempt_id"] == record.get("attempt_id") for existing in self.attempts()):
            return None
        return self.open_attempt(record)

    def record_decision(
        self,
        *,
        attempt_id: str,
        issue_id: str,
        run_id: str,
        result: str,
        reviewer: str | None = None,
        comments: list[str] | None = None,
        questions: list[str] | None = None,
    ) -> dict[str, Any] | None:
        """Record a review outcome for an attempt, once per (attempt, outcome)."""
        if any(
            record["attempt_id"] == attempt_id and record.get("result") == result
            for record in self.decisions()
        ):
            return None
        return self._write(
            {
                "kind": REVIEW_DECISION,
                "attempt_id": attempt_id,
                "issue_id": issue_id,
                "run_id": run_id,
                "result": result,
                "reviewer": reviewer,
                "comments": comments or [],
                "questions": questions or [],
            }
        )

    def rejection_history(self, issue_id: str) -> list[dict[str, Any]]:
        return [
            {
                "attempt_id": record["attempt_id"],
                "result": record["result"],
                "reviewer": record.get("reviewer"),
                "comments": record.get("comments") or [],
                "recorded_at": record.get("recorded_at"),
            }
            for record in self.decisions()
            if record["issue_id"] == issue_id and record.get("result") == "REJECT"
        ]

    def _write(self, record: dict[str, Any]) -> dict[str, Any]:
        entry = {"recorded_at": datetime.now(UTC).isoformat(timespec="seconds"), **record}
        with os.fdopen(
            os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600), "a", encoding="utf-8"
        ) as handle:
            handle.write(json.dumps(entry, sort_keys=True) + "\n")
        return entry

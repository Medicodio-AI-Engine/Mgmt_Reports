"""Append-only audit log.

Every action the pipeline takes is appended as one JSON object per line. Records
are never rewritten or deleted, so the whole lifecycle of a run can be
reconstructed from this file alone.
"""

from __future__ import annotations

import datetime as dt
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_SECRET_KEY_HINTS = ("token", "secret", "password", "api_key", "apikey", "credential")
REDACTED = "[REDACTED]"


def _scrub(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: (REDACTED if any(h in key.lower() for h in _SECRET_KEY_HINTS) else _scrub(item))
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [_scrub(item) for item in value]
    return value


@dataclass
class AuditLog:
    """Append-only JSONL audit log for one run."""

    path: Path
    run_id: str

    def __post_init__(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def record(
        self,
        event: str,
        *,
        issue_id: str | None = None,
        attempt_id: str | None = None,
        stage: str | None = None,
        detail: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        entry = {
            "timestamp": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
            "run_id": self.run_id,
            "event": event,
            "issue_id": issue_id,
            "attempt_id": attempt_id,
            "stage": stage,
            "detail": _scrub(detail or {}),
        }
        line = json.dumps(entry, sort_keys=True)
        # O_APPEND keeps concurrent writers from interleaving partial lines.
        with os.fdopen(
            os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644), "a", encoding="utf-8"
        ) as handle:
            handle.write(line + "\n")
        return entry

    def entries(self) -> list[dict[str, Any]]:
        if not self.path.exists():
            return []
        return [
            json.loads(line)
            for line in self.path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

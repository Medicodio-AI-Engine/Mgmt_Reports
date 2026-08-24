"""Stable issue identity across runs.

An issue id must mean the same finding tomorrow as it does today, because human
``DECISION:`` blocks reference it by id. Ids are therefore allocated once per
dedupe signature and persisted, never derived from a position in a list.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .naming import issue_id


@dataclass
class IssueRegistry:
    """Persistent ``dedupe signature -> issue id`` map."""

    path: Path
    assigned: dict[str, str] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> IssueRegistry:
        if not path.exists():
            return cls(path=path)
        raw = json.loads(path.read_text(encoding="utf-8"))
        return cls(path=path, assigned=dict(raw.get("issues") or {}))

    def _next_number(self) -> int:
        numbers = [int(value.removeprefix("ISSUE_")) for value in self.assigned.values()]
        return max(numbers, default=0) + 1

    def resolve(self, signature: str) -> str:
        """Return the existing id for ``signature``, allocating one if it is new."""
        existing = self.assigned.get(signature)
        if existing is not None:
            return existing
        allocated = issue_id(self._next_number())
        self.assigned[signature] = allocated
        return allocated

    def save(self) -> Path:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        document = {"issues": dict(sorted(self.assigned.items(), key=lambda item: item[1]))}
        self.path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
        return self.path

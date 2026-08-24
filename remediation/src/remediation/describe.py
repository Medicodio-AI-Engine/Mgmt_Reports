"""The task description column: what the work actually is.

The title names the task; the description says what was observed, what would be
done about it, and where. It is assembled from the issue's own fields plus the
read-only code review, so it never asserts anything the run did not establish.

One sentence group per question, joined into a single table cell:
``Observed: … | Proposed: … | Code: … | Steps: …``.
"""

from __future__ import annotations

from typing import Any

from . import codebase

MAX_LENGTH = 700
MAX_STEPS = 3


def _flatten(text: str) -> str:
    """Table cells are one line, so newlines and pipes cannot survive."""
    return " ".join(text.replace("|", "/").split())


def _clip(text: str) -> str:
    if len(text) <= MAX_LENGTH:
        return text
    return text[: MAX_LENGTH - 1].rstrip() + "…"


def _observed(issue: dict[str, Any]) -> str:
    stated = str(issue.get("description") or issue.get("title") or "").strip()
    return f"Observed: {stated}" if stated else ""


def _proposed(issue: dict[str, Any]) -> str:
    plan = issue.get("plan") or {}
    action = issue.get("recommended_action") or plan.get("proposed_action") or ""
    return f"Proposed: {str(action).strip()}" if action else ""


def _step_text(steps: list[str]) -> str:
    """The first few steps only; the plan file holds the rest."""
    shown = "; ".join(steps[:MAX_STEPS])
    rest = len(steps) - MAX_STEPS
    return f"{shown} (+{rest} more in the plan)" if rest > 0 else shown


def _steps(issue: dict[str, Any]) -> str:
    plan = issue.get("plan") or {}
    steps = [str(step) for step in (plan.get("implementation_plan") or [])]
    return "Steps: " + _step_text(steps) if steps else ""


def _code(issue: dict[str, Any]) -> str:
    reviews = issue.get("code_review")
    if not isinstance(reviews, list) or not reviews:
        return ""
    summaries = [codebase.summary(_context_of(raw)) for raw in reviews if isinstance(raw, dict)]
    return "Code: " + "; ".join(summaries) if summaries else ""


def _context_of(raw: dict[str, Any]) -> codebase.CodeContext:
    """Rebuild the inspection result the run recorded for this issue."""
    return codebase.CodeContext(
        repository=raw.get("repository"),
        checkout_available=bool(raw.get("checkout_available")),
        present_paths=tuple(raw.get("present_paths") or ()),
        missing_paths=tuple(raw.get("missing_paths") or ()),
        source_file_count=raw.get("source_file_count"),
    )


def describe(issue: dict[str, Any]) -> str:
    """The task description for one analysed issue."""
    parts = [_observed(issue), _proposed(issue), _code(issue), _steps(issue)]
    return _clip(_flatten(" | ".join(part for part in parts if part)))

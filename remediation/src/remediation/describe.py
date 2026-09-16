"""The task description column: the work that was carried out.

The description is about the engineer's or Devin's work, not about this
pipeline. It leads with what the repository's own history shows landed on the
report date — commits, whose, and how far the code moved against the version
before that day — then what the code looks like now, then the report's own
statement and the action it recommended.

This pipeline's plan steps are deliberately absent: they describe what the
platform would do next, which is not what a supervisor is asking of this column.

Assembled into one table cell:
``Work carried out: … | Code now: … | Reported: … | Recommended: …``.
"""

from __future__ import annotations

from typing import Any

from . import codebase, history

MAX_LENGTH = 700


def _flatten(text: str) -> str:
    """Table cells are one line, so newlines and pipes cannot survive."""
    return " ".join(text.replace("|", "/").split())


def _clip(text: str) -> str:
    if len(text) <= MAX_LENGTH:
        return text
    return text[: MAX_LENGTH - 1].rstrip() + "…"


def _reviews(issue: dict[str, Any]) -> list[dict[str, Any]]:
    reviews = issue.get("code_review")
    return (
        [entry for entry in reviews if isinstance(entry, dict)] if isinstance(reviews, list) else []
    )


def _state_of(raw: dict[str, Any]) -> codebase.CodeContext:
    """Rebuild the current-state inspection the run recorded."""
    return codebase.CodeContext(
        repository=raw.get("repository"),
        checkout_available=bool(raw.get("checkout_available")),
        present_paths=tuple(raw.get("present_paths") or ()),
        missing_paths=tuple(raw.get("missing_paths") or ()),
        source_file_count=raw.get("source_file_count"),
    )


def _work_of(raw: dict[str, Any]) -> history.WorkDone:
    """Rebuild the history reading the run recorded."""
    done = raw.get("work_done") or {}
    return history.WorkDone(
        date=str(done.get("date") or ""),
        author=done.get("author"),
        commit_count=int(done.get("commit_count") or 0),
        subjects=tuple(done.get("subjects") or ()),
        files_changed=done.get("files_changed"),
        insertions=done.get("insertions"),
        deletions=done.get("deletions"),
        history_available=bool(done.get("history_available")),
    )


def _repository_of(raw: dict[str, Any]) -> str:
    return str(raw.get("repository") or "unresolved repository")


def _work_note(raw: dict[str, Any]) -> str:
    return f"{_repository_of(raw)}: {history.summary(_work_of(raw))}"


def _work(issue: dict[str, Any]) -> str:
    """What the repositories show was actually done that day."""
    notes = [_work_note(raw) for raw in _reviews(issue)]
    return "Work carried out: " + "; ".join(notes) if notes else ""


def _code(issue: dict[str, Any]) -> str:
    """What the code looks like now, after that work."""
    notes = [codebase.summary(_state_of(raw)) for raw in _reviews(issue)]
    return "Code now: " + "; ".join(notes) if notes else ""


def _first_sentence(text: str) -> str:
    """The report's own claim, without the evidence paragraph behind it."""
    head, separator, _ = text.partition(". ")
    return (head + ".") if separator else text


def _reported(issue: dict[str, Any]) -> str:
    stated = str(issue.get("description") or issue.get("title") or "").strip()
    return f"Reported: {_first_sentence(stated)}" if stated else ""


def _recommended(issue: dict[str, Any]) -> str:
    plan = issue.get("plan") or {}
    action = issue.get("recommended_action") or plan.get("proposed_action") or ""
    return f"Recommended: {str(action).strip()}" if action else ""


def describe(issue: dict[str, Any]) -> str:
    """The task description for one analysed issue."""
    parts = [_work(issue), _code(issue), _reported(issue), _recommended(issue)]
    return _clip(_flatten(" | ".join(part for part in parts if part)))

"""What was actually done in the target repository, read from its history.

The management report says a person (or Devin) did something on a date. This
module reads the repository's own history for that date and states what landed:
how many commits, whose, which subjects, and how much the code moved compared
with the version immediately before that day's work.

Read-only by construction: only ``git log``, ``git diff --shortstat`` and
``git rev-parse`` are ever run, always with ``-C <checkout>``, never with a flag
that writes. Nothing is fetched, checked out, staged or committed, and no file in
the target repository is opened for writing. A shallow clone, a repository with
no history for that date, or a missing checkout each report themselves plainly
instead of guessing (a shallow clone can still list the day's commits; only the
before/after comparison needs the parent commit to be present).
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

READ_ONLY_COMMANDS = frozenset({"log", "diff", "rev-parse"})
MAX_SUBJECTS = 3
MAX_DIFFED = 10
TIMEOUT_SECONDS = 20


@dataclass(frozen=True)
class WorkDone:
    """The work the repository's own history shows for one report date."""

    date: str
    author: str | None = None
    commit_count: int = 0
    subjects: tuple[str, ...] = ()
    files_changed: int | None = None
    insertions: int | None = None
    deletions: int | None = None
    history_available: bool = False

    def as_dict(self) -> dict[str, object]:
        return {
            "date": self.date,
            "author": self.author,
            "commit_count": self.commit_count,
            "subjects": list(self.subjects),
            "files_changed": self.files_changed,
            "insertions": self.insertions,
            "deletions": self.deletions,
            "history_available": self.history_available,
        }


def _git(checkout: Path, arguments: list[str]) -> str | None:
    """Run one read-only git query; ``None`` when it cannot be answered."""
    if not arguments or arguments[0] not in READ_ONLY_COMMANDS:
        raise ValueError(f"refusing to run git {arguments[0] if arguments else ''}")
    command = ["git", "-C", str(checkout), *arguments]
    finished = subprocess.run(
        command, capture_output=True, text=True, timeout=TIMEOUT_SECONDS, check=False
    )
    return finished.stdout if finished.returncode == 0 else None


def _has_history(checkout: Path) -> bool:
    """Whether this directory is a git checkout whose log can be read."""
    return _git(checkout, ["log", "-1", "--format=%H"]) is not None


def _window(date: str) -> list[str]:
    """Restrict a query to the calendar day the report covers."""
    day = date.replace("_", "-")
    return [f"--since={day} 00:00", f"--until={day} 23:59"]


def _author_filter(author: str | None) -> list[str]:
    return [f"--author={author}"] if author else []


def _commits(checkout: Path, date: str, author: str | None) -> list[str]:
    """The commit hashes and subjects landed on ``date``, newest first."""
    query = [
        "log",
        "--all",
        "--no-merges",
        "--format=%H%x1f%s",
        *_window(date),
        *_author_filter(author),
    ]
    output = _git(checkout, query)
    return [line for line in (output or "").splitlines() if line.strip()]


def _subjects(lines: list[str]) -> tuple[str, ...]:
    return tuple(line.split("\x1f", 1)[-1] for line in lines[:MAX_SUBJECTS])


def _shortstat(checkout: Path, commit: str) -> str | None:
    """How far one commit moved the code from the version just before it."""
    return _git(checkout, ["diff", "--shortstat", f"{commit}^", commit])


def _number_before(text: str, word: str) -> int | None:
    """The count git printed before ``word`` in a ``--shortstat`` line."""
    words = text.replace(",", " ").split()
    for index, token in enumerate(words):
        if token.startswith(word) and index and words[index - 1].isdigit():
            return int(words[index - 1])
    return None


def _counts(stat: str) -> tuple[int, int, int]:
    """Files, insertions and deletions in one ``--shortstat`` line."""
    return (
        _number_before(stat, "file") or 0,
        _number_before(stat, "insertion") or 0,
        _number_before(stat, "deletion") or 0,
    )


def _movement(checkout: Path, lines: list[str]) -> tuple[int | None, int | None, int | None]:
    """Files changed, insertions and deletions across the day's own commits."""
    stats = [_shortstat(checkout, line.split("\x1f", 1)[0]) for line in lines[:MAX_DIFFED]]
    counted = [_counts(stat) for stat in stats if stat]
    if not counted:
        return None, None, None
    return tuple(sum(column) for column in zip(*counted, strict=True))  # type: ignore[return-value]


def _found(checkout: Path, date: str, author: str | None, lines: list[str]) -> WorkDone:
    files, insertions, deletions = _movement(checkout, lines)
    return WorkDone(
        date=date,
        author=author,
        commit_count=len(lines),
        subjects=_subjects(lines),
        files_changed=files,
        insertions=insertions,
        deletions=deletions,
        history_available=True,
    )


def _named(lines: list[str], subjects: tuple[str, ...]) -> list[str]:
    """The day's commits the finding itself quoted, when it quoted any."""
    wanted = [subject.strip().lower() for subject in subjects if subject.strip()]
    return [
        line for line in lines if any(hint in line.split("\x1f", 1)[-1].lower() for hint in wanted)
    ]


def work_done(
    checkout: Path | None,
    date: str,
    author: str | None = None,
    subjects: tuple[str, ...] = (),
) -> WorkDone:
    """What ``checkout`` shows was done on ``date``, narrowed as far as it can be."""
    if checkout is None or not _has_history(checkout):
        return WorkDone(date=date, author=author)
    everyone = _commits(checkout, date, None)
    if not everyone:
        return WorkDone(date=date, author=author, history_available=True)
    return _found(checkout, date, *_narrowed(checkout, date, author, subjects, everyone))


def _narrowed(
    checkout: Path,
    date: str,
    author: str | None,
    subjects: tuple[str, ...],
    everyone: list[str],
) -> tuple[str | None, list[str]]:
    """The commits closest to the finding: the ones it quoted, else its author's."""
    quoted = _named(everyone, subjects)
    if quoted:
        return author, quoted
    theirs = _commits(checkout, date, author) if author else []
    return (author, theirs) if theirs else (None, everyone)


def _movement_note(work: WorkDone) -> str:
    """The size of the change each commit made to the version before it."""
    if work.files_changed is None:
        return ""
    moved = f"{work.insertions or 0} insertion(s), {work.deletions or 0} deletion(s)"
    return f" changing {work.files_changed} file(s) ({moved}) against the previous version"


def summary(work: WorkDone) -> str:
    """One sentence stating what the history shows was done that day."""
    if not work.history_available:
        return "repository history was not read (no local checkout with history)"
    if not work.commit_count:
        return f"repository history shows no commits on {work.date.replace('_', '-')}"
    who = f" by {work.author}" if work.author else ""
    landed = f"{work.commit_count} commit(s){who} landed{_movement_note(work)}"
    return f"{landed}: " + "; ".join(f'"{subject}"' for subject in work.subjects)

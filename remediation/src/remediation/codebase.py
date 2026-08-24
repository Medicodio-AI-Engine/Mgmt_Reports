"""Read-only inspection of the repositories a finding points at.

A report statement says what someone did; it does not say what the code looks
like today. This module answers the little that can be answered safely: is the
repository checked out here, do the paths the report named still exist, and how
large is the area. That is enough to turn "mirror KB wizard changes by hand"
into a task description a supervisor can act on.

Read-only by construction: it only asks the filesystem whether paths exist and
counts entries. Nothing here opens a file for writing, runs a command, or
touches git. ``repository_root`` is unset by default, in which case every
inspection reports "not inspected" rather than guessing.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

MAX_LISTED_PATHS = 5


@dataclass(frozen=True)
class CodeContext:
    """What a read-only look at the target repository found."""

    repository: str | None
    checkout_available: bool
    present_paths: tuple[str, ...] = ()
    missing_paths: tuple[str, ...] = ()
    source_file_count: int | None = None

    def as_dict(self) -> dict[str, object]:
        return {
            "repository": self.repository,
            "checkout_available": self.checkout_available,
            "present_paths": list(self.present_paths),
            "missing_paths": list(self.missing_paths),
            "source_file_count": self.source_file_count,
        }


def checkout(root: Path | None, repository: str | None) -> Path | None:
    """The local checkout of ``repository``, when one is available to read."""
    if root is None or not repository:
        return None
    candidate = root / repository.split("/")[-1]
    return candidate if candidate.is_dir() else None


def _exists(checkout: Path, path: str) -> bool:
    return (checkout / path.lstrip("/")).exists()


def _split_paths(checkout: Path, paths: tuple[str, ...]) -> tuple[list[str], list[str]]:
    """The named paths that still exist, and those that no longer do."""
    present = [path for path in paths if _exists(checkout, path)]
    missing = [path for path in paths if path not in present]
    return present[:MAX_LISTED_PATHS], missing[:MAX_LISTED_PATHS]


def _source_files(checkout: Path) -> int:
    """Tracked-looking source files, ignoring dependency and metadata trees."""
    skipped = {".git", "node_modules", ".venv", "dist", "build", "__pycache__"}
    return sum(
        1 for path in checkout.rglob("*") if path.is_file() and not skipped.intersection(path.parts)
    )


def inspect(root: Path | None, repository: str | None, paths: tuple[str, ...] = ()) -> CodeContext:
    """Look at ``repository`` without changing anything in it."""
    local = checkout(root, repository)
    if local is None:
        return CodeContext(repository=repository, checkout_available=False)
    present, missing = _split_paths(local, paths)
    return CodeContext(
        repository=repository,
        checkout_available=True,
        present_paths=tuple(present),
        missing_paths=tuple(missing),
        source_file_count=_source_files(local),
    )


def _path_note(context: CodeContext) -> str:
    """What the reported paths look like now, when any were reported."""
    if context.present_paths:
        return "reported paths still present: " + ", ".join(context.present_paths)
    if context.missing_paths:
        return "reported paths no longer present: " + ", ".join(context.missing_paths)
    return "no file paths were reported"


def summary(context: CodeContext) -> str:
    """One sentence a supervisor can read, stating what was inspected."""
    if not context.repository:
        return "target repository unresolved, so no code was inspected"
    if not context.checkout_available:
        return f"{context.repository} was not inspected (no local checkout configured)"
    size = f"{context.source_file_count} source file(s)"
    return f"{context.repository} reviewed read-only ({size}); {_path_note(context)}"

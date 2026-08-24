"""The read-only code review that feeds the task description."""

from __future__ import annotations

import stat
from pathlib import Path

from remediation import codebase


def _checkout(root: Path, name: str) -> Path:
    repo = root / name
    (repo / "src").mkdir(parents=True)
    (repo / "src" / "wizard.ts").write_text("export const wizard = 1;\n", encoding="utf-8")
    return repo


def test_missing_root_reports_not_inspected_rather_than_guessing() -> None:
    context = codebase.inspect(None, "medicodio-nextgen-app-react", ("src/wizard.ts",))
    assert context.checkout_available is False
    assert "not inspected" in codebase.summary(context)


def test_unresolved_repository_inspects_nothing(tmp_path: Path) -> None:
    context = codebase.inspect(tmp_path, None)
    assert context.checkout_available is False
    assert "unresolved" in codebase.summary(context)


def test_present_and_missing_paths_are_reported_separately(tmp_path: Path) -> None:
    _checkout(tmp_path, "medicodio-nextgen-app-react")
    context = codebase.inspect(
        tmp_path, "medicodio-nextgen-app-react", ("src/wizard.ts", "src/gone.ts")
    )
    assert context.present_paths == ("src/wizard.ts",)
    assert context.missing_paths == ("src/gone.ts",)
    assert "reported paths still present: src/wizard.ts" in codebase.summary(context)


def test_owner_prefixed_repository_name_finds_the_checkout(tmp_path: Path) -> None:
    _checkout(tmp_path, "medicodio-nextgen-integration")
    context = codebase.inspect(tmp_path, "Medicodio-AI-Engine/medicodio-nextgen-integration")
    assert context.checkout_available is True
    assert context.source_file_count == 1


def test_inspection_leaves_the_checkout_untouched(tmp_path: Path) -> None:
    repo = _checkout(tmp_path, "medicodio-paperclip")
    before = {
        path: (path.stat()[stat.ST_MTIME], path.read_bytes())
        for path in repo.rglob("*")
        if path.is_file()
    }
    codebase.inspect(tmp_path, "medicodio-paperclip", ("src/wizard.ts",))
    after = {
        path: (path.stat()[stat.ST_MTIME], path.read_bytes())
        for path in repo.rglob("*")
        if path.is_file()
    }
    assert after == before


def test_dependency_trees_are_not_counted_as_source(tmp_path: Path) -> None:
    repo = _checkout(tmp_path, "nextgen-codio-engine")
    (repo / "node_modules" / "dep").mkdir(parents=True)
    (repo / "node_modules" / "dep" / "index.js").write_text("x\n", encoding="utf-8")
    assert codebase.inspect(tmp_path, "nextgen-codio-engine").source_file_count == 1

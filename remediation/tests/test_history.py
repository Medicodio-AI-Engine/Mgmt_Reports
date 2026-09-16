"""Reading what was done in a target repository, without changing it."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

from remediation import history


def _git(repo: Path, *arguments: str, when: str | None = None) -> None:
    environment = {**os.environ, "GIT_COMMITTER_DATE": when} if when else None
    subprocess.run(
        ["git", "-C", str(repo), *arguments], check=True, capture_output=True, env=environment
    )


def _commit(repo: Path, name: str, body: str, subject: str, when: str) -> None:
    (repo / name).write_text(body, encoding="utf-8")
    _git(repo, "add", name)
    _git(
        repo,
        "-c",
        "user.name=Asha",
        "-c",
        "user.email=asha@example.com",
        "commit",
        "-m",
        subject,
        "--date",
        when,
        when=when,
    )


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    checkout = tmp_path / "medicodio-nextgen-app-react"
    checkout.mkdir()
    _git(checkout, "init", "-q", "-b", "main")
    _commit(checkout, "wizard.ts", "one\n", "Earlier version", "2026-08-20T10:00:00")
    _commit(checkout, "wizard.ts", "one\ntwo\n", "Add payer scope", "2026-08-23T10:00:00")
    _commit(
        checkout, "wizard.ts", "one\ntwo\nthree\n", "Mirror it in the UI", "2026-08-23T14:00:00"
    )
    return checkout


def test_no_checkout_says_history_was_not_read() -> None:
    work = history.work_done(None, "2026_08_23", "asha")
    assert work.history_available is False
    assert "not read" in history.summary(work)


def test_day_with_no_commits_is_reported_as_such(repo: Path) -> None:
    work = history.work_done(repo, "2026_08_22")
    assert (work.history_available, work.commit_count) == (True, 0)
    assert "no commits on 2026-08-22" in history.summary(work)


def test_the_days_commits_are_compared_with_the_earlier_version(repo: Path) -> None:
    work = history.work_done(repo, "2026_08_23")
    assert work.commit_count == 2
    assert work.subjects == ("Mirror it in the UI", "Add payer scope")
    assert (work.files_changed, work.insertions, work.deletions) == (2, 2, 0)
    assert (
        "2 commit(s) landed changing 2 file(s) (2 insertion(s), 0 deletion(s)) "
        "against the previous version" in history.summary(work)
    )


def test_a_quoted_commit_subject_narrows_the_history(repo: Path) -> None:
    work = history.work_done(repo, "2026_08_23", "Asha", ("Mirror it in the UI",))
    assert work.commit_count == 1
    assert work.subjects == ("Mirror it in the UI",)


def test_an_author_the_history_does_not_know_falls_back_to_everyone(repo: Path) -> None:
    work = history.work_done(repo, "2026_08_23", "nobody-by-that-name")
    assert work.commit_count == 2
    assert work.author is None


def test_a_matching_author_is_named(repo: Path) -> None:
    work = history.work_done(repo, "2026_08_23", "Asha")
    assert work.author == "Asha"
    assert "by Asha" in history.summary(work)


def test_reading_the_history_changes_nothing(repo: Path) -> None:
    before = _git_state(repo)
    history.work_done(repo, "2026_08_23", "Asha")
    assert _git_state(repo) == before


def _git_state(repo: Path) -> tuple[str, str]:
    def read(*arguments: str) -> str:
        finished = subprocess.run(
            ["git", "-C", str(repo), *arguments], check=True, capture_output=True, text=True
        )
        return finished.stdout

    return read("log", "--all", "--format=%H"), read("status", "--porcelain")


def test_only_read_only_git_queries_are_permitted(repo: Path) -> None:
    with pytest.raises(ValueError, match="refusing to run git"):
        history._git(repo, ["commit", "--allow-empty", "-m", "no"])

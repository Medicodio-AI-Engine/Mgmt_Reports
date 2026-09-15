"""The safety properties the review findings on the pilot pointed at.

Each test states one property a supervisor relies on: a report cell cannot make
the platform look outside a checkout, a run cannot overwrite another run's
artifacts, and no environment variable can quietly turn writing on.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

from remediation import codebase, discovery, history, pipeline
from remediation import config as config_module

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _checkout(root: Path, name: str) -> Path:
    repo = root / name
    (repo / ".git").mkdir(parents=True)
    (repo / "app.ts").write_text("export const app = 1;\n", encoding="utf-8")
    return repo


def test_reported_path_leaving_the_checkout_is_not_answered(tmp_path: Path) -> None:
    _checkout(tmp_path, "medicodio-nextgen-app-react")
    (tmp_path / "secret.txt").write_text("outside\n", encoding="utf-8")
    context = codebase.inspect(
        tmp_path, "medicodio-nextgen-app-react", ("../secret.txt", "/etc/passwd")
    )
    assert context.present_paths == ()
    assert context.missing_paths == ("../secret.txt", "/etc/passwd")


def test_repository_name_cannot_point_outside_the_configured_root(tmp_path: Path) -> None:
    _checkout(tmp_path, "elsewhere")
    root = tmp_path / "checkouts"
    root.mkdir()
    assert codebase.checkout(root, "owner/../elsewhere") is None


def test_directory_without_git_metadata_is_not_treated_as_a_checkout(tmp_path: Path) -> None:
    (tmp_path / "medicodio-planted").mkdir()
    assert codebase.checkout(tmp_path, "medicodio-planted") is None


def test_history_window_states_utc_so_the_runner_timezone_cannot_shift_a_day() -> None:
    since, until = history._window("2026_08_23")
    assert since.endswith("+0000")
    assert until.endswith("+0000")


def test_late_utc_commit_is_filed_under_its_utc_day(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True)
    (repo / "a.txt").write_text("a\n", encoding="utf-8")
    subprocess.run(["git", "-C", str(repo), "add", "a.txt"], check=True)
    subprocess.run(
        ["git", "-C", str(repo), "commit", "-q", "-m", "late"],
        check=True,
        env={
            **os.environ,
            "GIT_AUTHOR_DATE": "2026-08-23T23:30:00+0000",
            "GIT_COMMITTER_DATE": "2026-08-23T23:30:00+0000",
            "GIT_AUTHOR_NAME": "Asha",
            "GIT_AUTHOR_EMAIL": "asha@example.com",
            "GIT_COMMITTER_NAME": "Asha",
            "GIT_COMMITTER_EMAIL": "asha@example.com",
            "TZ": "Asia/Kolkata",
        },
    )
    assert history.work_done(repo, "2026_08_23").commit_count == 1


def test_two_runs_never_claim_the_same_run_directory(tmp_path: Path) -> None:
    first, first_dir = pipeline.claim_run(tmp_path, "2026_08_23")
    second, second_dir = pipeline.claim_run(tmp_path, "2026_08_23")
    assert first != second
    assert first_dir != second_dir
    assert first_dir.is_dir() and second_dir.is_dir()


def test_claimed_run_id_continues_past_an_existing_directory(tmp_path: Path) -> None:
    (tmp_path / "2026_08_19" / "RUN_0007").mkdir(parents=True)
    claimed, _ = pipeline.claim_run(tmp_path, "2026_08_23")
    assert claimed == "RUN_0008"


def test_environment_overrides_the_configuration_file(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MGMT_REPORTS_DIRECTORY", "Ai_Engr_Rpt/Daily/medicodio/Other")
    loaded = config_module.load(PROJECT_ROOT / "config" / "config.yaml")
    assert loaded.mgmt_reports_directory == "Ai_Engr_Rpt/Daily/medicodio/Other"


def test_stated_override_wins_over_the_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("MGMT_REPORTS_DIRECTORY", "from/environment")
    loaded = config_module.load(
        PROJECT_ROOT / "config" / "config.yaml",
        overrides={"mgmt_reports_directory": "from/argument"},
    )
    assert loaded.mgmt_reports_directory == "from/argument"


def test_environment_cannot_turn_dry_run_off(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DRY_RUN_MODE", "false")
    loaded = config_module.load(PROJECT_ROOT / "config" / "config.yaml")
    assert loaded.dry_run_mode is True


def test_source_dated_only_by_its_filename_is_flagged(report_directory: Path) -> None:
    (report_directory / "mgmt-activity-report-2026-08-23.md").write_text(
        "# Daily Team Summary\n\nActivities completed\nDevin usage\n", encoding="utf-8"
    )
    (report_directory / "employee-rating-cards-2026-08-23.md").write_text(
        "# Employee Rating Cards\n\n**Review Day:** 2026-08-23 UTC\n\nSummary grid\n",
        encoding="utf-8",
    )
    context = discovery.assemble(
        config_module.load(PROJECT_ROOT / "config" / "config.yaml"),
        report_directory,
        "RUN_0001",
    )
    flagged = [warning for warning in context.warnings if warning.startswith("DATE_UNVERIFIED")]
    assert flagged and "mgmt-activity-report-2026-08-23.md" in flagged[0]

from __future__ import annotations

import pytest

from remediation import dates


@pytest.mark.parametrize(
    "raw",
    ["2026-08-23", "2026_08_23", "2026/08/23", "20260823"],
)
def test_normalize_accepts_every_written_form(raw: str) -> None:
    assert dates.normalize(raw) == "2026_08_23"


@pytest.mark.parametrize("raw", ["", "2026-8-3", "23-08-2026", "not-a-date", "2026_13_01"])
def test_normalize_rejects_anything_else(raw: str) -> None:
    with pytest.raises(dates.DateNormalizationError):
        dates.normalize(raw)


def test_find_date_reads_a_kebab_case_filename() -> None:
    assert dates.find_date("mgmt-activity-report-2026-08-23.md") == "2026_08_23"


def test_find_date_returns_none_when_absent() -> None:
    assert dates.find_date("README.md") is None


def test_find_content_review_date_prefers_the_declared_review_date() -> None:
    text = "**Review date:** 2026-08-23 (Sunday, UTC) · **Run date:** 2026-08-24 UTC"
    assert dates.find_content_review_date(text) == "2026_08_23"


def test_find_content_review_date_ignores_a_run_date_alone() -> None:
    assert dates.find_content_review_date("**Run date:** 2026-08-24 UTC") is None

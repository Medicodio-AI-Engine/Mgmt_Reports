"""Fixture report builders shared by the tests."""

from __future__ import annotations

from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def write_detail_report(directory: Path, date: str = "2026-08-23") -> Path:
    path = directory / f"mgmt-activity-report-{date}.md"
    path.write_text(
        (FIXTURES / "detail_report.md").read_text(encoding="utf-8").replace("{{DATE}}", date),
        encoding="utf-8",
    )
    return path


def write_cards_report(directory: Path, date: str = "2026-08-23") -> Path:
    path = directory / f"employee-rating-cards-{date}.md"
    path.write_text(
        (FIXTURES / "rating_cards.md").read_text(encoding="utf-8").replace("{{DATE}}", date),
        encoding="utf-8",
    )
    return path

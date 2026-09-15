"""Reading rating cards, grouping them into weeks, and comparing the weeks."""

from __future__ import annotations

from pathlib import Path

from remediation import ratings, trend, trendreport

CARD_A = """# Employee Rating Cards — Review Day 2026-08-05 (UTC)

## Summary Grid

| # | Member | Product | Overall (1-10) | Band | Delivery | Rigor | Review | Devin | Automation | Consistency |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | asha | Medicodio | **7.0** | Solid | 7 | 7 | 7 | 6 | 5 | 8 |
| 2 | bhanu | Medicodio | **5.0** | Mixed | 5 | 5 | NR | 4 | 4 | 6 |
"""

CARD_B = """# Employee Rating Cards — 2026-08-12

**Review date:** 2026-08-12 (Wednesday, UTC)

## Summary grid

| Member | Product | Delivery | Rigor | Review | Devin | Automation | Consistency | Overall | Band |
| ------ | ------- | -------- | ----- | ------ | ----- | ---------- | ----------- | ------- | ---- |
| asha | Medicodio | 8 | 8 | 7 | 7 | 5 | 8 | **7.6** | Solid |
| chandra | Global Codio | 6 | 6 | 5 | 4 | 4 | 6 | **5.4** | Mixed |
"""


CARD_C = """# Employee Rating Cards — 2026-08-14

**Review date:** 2026-08-14 (Friday, UTC)

## Summary grid

| Member | Product | Delivery | Rigor | Review | Devin | Automation | Consistency | Overall | Band |
| ------ | ------- | -------- | ----- | ------ | ----- | ---------- | ----------- | ------- | ---- |
| asha | Medicodio | 8 | 8 | 8 | 7 | 6 | 8 | **7.9** | Solid |
"""


CARD_WEIGHTED = """# Employee Rating Cards — 2026-08-22

**Review date:** 2026-08-22 (Saturday, UTC)

## Summary grid

| Member | Product | Delivery | Rigor | Review | Devin | Automation | Consistency | Weighted | Band |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| asha | Medicodio | 9 | 9 | NR | 5 | 4 | 9 | 7.7 | Solid |
"""


def _cards(tmp_path: Path) -> list[ratings.CardSet]:
    (tmp_path / "employee-rating-cards-2026-08-05.md").write_text(CARD_A, encoding="utf-8")
    (tmp_path / "employee-rating-cards-2026-08-12.md").write_text(CARD_B, encoding="utf-8")
    (tmp_path / "mgmt-activity-report-2026-08-12.md").write_text("# not a card\n", encoding="utf-8")
    return ratings.read_all(tmp_path)


def test_reads_both_grid_layouts(tmp_path: Path) -> None:
    first, second = _cards(tmp_path)
    assert [card_set.date for card_set in (first, second)] == ["2026_08_05", "2026_08_12"]
    assert first.by_member()["asha"].overall == 7.0
    assert first.by_member()["bhanu"].scores["Review"] is None
    assert second.by_member()["asha"].scores["Rigor"] == 8


def test_reads_weighted_column_as_overall(tmp_path: Path) -> None:
    """Some review days head the same figure ``Weighted`` instead of ``Overall``."""
    path = tmp_path / "2026_08_22_Employee_Rating_Cards.md"
    path.write_text(CARD_WEIGHTED, encoding="utf-8")
    card = ratings.read(path).by_member()["asha"]
    assert (card.overall, card.scores["Review"]) == (7.7, None)


def test_activity_reports_are_not_cards(tmp_path: Path) -> None:
    assert len(_cards(tmp_path)) == 2


def test_series_keeps_missing_weeks(tmp_path: Path) -> None:
    weeks = trend.series(_cards(tmp_path), 4)
    assert [week.key for week in weeks] == ["2026-W30", "2026-W31", "2026-W32", "2026-W33"]
    assert [week.covered for week in weeks] == [False, False, True, True]


def test_week_over_week_movement(tmp_path: Path) -> None:
    weeks = trend.series(_cards(tmp_path), 4)
    changes = {change.member: change for change in trend.compare(weeks[2], weeks[3]).changes}
    assert changes["asha"].delta == 0.6
    assert changes["chandra"].status == "NEW"
    assert changes["bhanu"].status == "NOT_RATED"
    assert changes["bhanu"].delta is None


def test_uncovered_pairs_are_not_comparable(tmp_path: Path) -> None:
    weeks = trend.series(_cards(tmp_path), 4)
    assert [item.comparable for item in trend.comparisons(weeks)] == [False, False, True]


def test_report_states_coverage_and_values(tmp_path: Path) -> None:
    weeks = trend.series(_cards(tmp_path), 4)
    report = trendreport.render(weeks, generated="2026_08_13")
    assert "no rating card in the repository" in report.markdown
    assert "2026-W30, 2026-W31" in report.markdown
    assert "+0.6" in report.markdown
    assert report.data["missing_weeks"] == ["2026-W30", "2026-W31"]


def _weekly_cards(tmp_path: Path) -> list[ratings.CardSet]:
    """Two review days in one ISO week, filed under the repository's naming convention."""
    (tmp_path / "2026_08_12_Employee_Rating_Cards.md").write_text(CARD_B, encoding="utf-8")
    (tmp_path / "2026_08_14_Employee_Rating_Cards.md").write_text(CARD_C, encoding="utf-8")
    return ratings.read_all(tmp_path)


def test_reads_underscored_card_filenames(tmp_path: Path) -> None:
    assert [card_set.date for card_set in _weekly_cards(tmp_path)] == ["2026_08_12", "2026_08_14"]


def test_daily_matrix_lists_every_review_day(tmp_path: Path) -> None:
    weeks = trend.series(_weekly_cards(tmp_path), 2)
    report = trendreport.render(weeks, generated="2026_08_15")
    assert "## Day-by-day scores within a week" in report.markdown
    assert "| asha | 7.6 | 7.9 |" in report.markdown
    assert "| chandra | 5.4 | NR |" in report.markdown
    assert report.data["weeks"][-1]["daily_overall"]["asha"] == ["7.6", "7.9"]


def test_within_week_needs_two_cards(tmp_path: Path) -> None:
    weeks = trend.series(_cards(tmp_path), 4)
    assert trend.within_week(weeks[3]) is None
    single = trendreport.render(weeks, generated="2026_08_13")
    assert "## Within-week movement" not in single.markdown


def test_write_emits_markdown_and_json(tmp_path: Path) -> None:
    weeks = trend.series(_cards(tmp_path), 2)
    written = trendreport.write(trendreport.render(weeks), tmp_path / "out", "rating-trend")
    assert [path.name for path in written] == ["rating-trend.md", "rating-trend.json"]
    assert all(path.exists() for path in written)

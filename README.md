# Reports

Management reporting artifacts produced by the daily engineering review automation.

## Layout

```
Ai_Engr_Rpt/Daily/medicodio/Detail/
  YYYY_MM_DD_Mgmt_Activity_Report.md
  YYYY_MM_DD_Employee_Rating_Cards.md
```

`YYYY_MM_DD` is the **review date** (the UTC day the report covers), not the run date. The date
comes first so files list in chronological order, with each day's reports side by side.

Every run of the daily review commits **both** files for its review date. One file per report type
per day is the intended steady state.

## Re-runs: never overwrite

If a file for that review date already exists, the new one is written alongside it with an
incrementing suffix rather than replacing it:

```
2026_08_23_Mgmt_Activity_Report.md      first run for the day
2026_08_23_Mgmt_Activity_Report_2.md    a second run for the same day
2026_08_23_Mgmt_Activity_Report_3.md    a third, and so on
```

The unsuffixed file therefore always holds the first report produced for that day, and the presence
of suffixed files is itself the signal that the day was reviewed more than once — worth
investigating, since a duplicate run usually means the schedule fired twice or a run was retried.

## Coverage

Reports start at review date 2026-08-19. That day has rating cards only: its management report was
produced before reports were stored in Git and is no longer recoverable.

## Format

Markdown is the stored format. It renders in the GitHub UI, is searchable, and day-over-day
changes in findings and ratings are visible in `git diff`. PDFs are generated on demand from
these files for distribution and are not committed, so the repository stays diffable and small.

## Confidentiality

These files name individual engineers and contain per-person ratings. Access should be
restricted to management.

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

## Format

Markdown is the stored format. It renders in the GitHub UI, is searchable, and day-over-day
changes in findings and ratings are visible in `git diff`. PDFs are generated on demand from
these files for distribution and are not committed, so the repository stays diffable and small.

## Confidentiality

These files name individual engineers and contain per-person ratings. Access should be
restricted to management.

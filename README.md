# Reports

Management reporting artifacts produced by the daily engineering review automation.

## Layout

```
Ai_Engr_Rpt/Daily/medicodio/Detail/
  Mgmt_Activity_Report_YYYY_MM_DD.md
  Employee_Rating_Cards_YYYY_MM_DD.md
```

`YYYY_MM_DD` is the **review date** (the UTC day the report covers), not the run date. The date
comes last so files group by report type and then sort chronologically within each type.

## Format

Markdown is the stored format. It renders in the GitHub UI, is searchable, and day-over-day
changes in findings and ratings are visible in `git diff`. PDFs are generated on demand from
these files for distribution and are not committed, so the repository stays diffable and small.

## Confidentiality

These files name individual engineers and contain per-person ratings. Access should be
restricted to management.

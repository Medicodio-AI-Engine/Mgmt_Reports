# Reports

Management reporting artifacts produced by the daily engineering review automation.

## Layout

```
Ai_Engr_Rpt/Daily/medicodio/Detail/
  mgmt-activity-report-YYYY-MM-DD.md
  employee-rating-cards-YYYY-MM-DD.md
Ai_Engr_Rpt/Daily/medicodio/Remediation/YYYY_MM_DD/RUN_NNNN/
  per-stage remediation run artifacts
remediation/
  the remediation platform that reads the reports above
```

`YYYY-MM-DD` is the **review date** (the UTC day the report covers), not the run date.

## Remediation platform

[`remediation/`](remediation/README.md) turns these reports into normalized, prioritized,
playbook-matched remediation proposals and stops at human review. The pilot is dry-run only: it
modifies no engineering repository and creates no commits or pull requests. Review decisions are
`DECISION:` blocks committed into the `05_DEV_REVIEW` artifact.

## Format

Markdown is the stored format. It renders in the GitHub UI, is searchable, and day-over-day
changes in findings and ratings are visible in `git diff`. PDFs are generated on demand from
these files for distribution and are not committed, so the repository stays diffable and small.

## Confidentiality

These files name individual engineers and contain per-person ratings. Access should be
restricted to management.

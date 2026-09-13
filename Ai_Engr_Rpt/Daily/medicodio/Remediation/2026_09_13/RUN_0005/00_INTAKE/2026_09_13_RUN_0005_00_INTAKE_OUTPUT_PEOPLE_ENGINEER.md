# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-13 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_13_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_13_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-fixing another member's findings, then approving and merging | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000283` | `docs(review-logs)` commits written by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Re-running the 37-gate matrix and transcribing results into prose | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`,  | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000286` | Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is ne | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Reviewer remediates, approves, then merges | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Merged over the approver's own written blocker | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Post-merge QA-gate verdict unactioned in-window | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Ad-hoc per-component timestamp formatting | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Branch carried without a PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC se | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000294` | Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Work carried on a branch with no PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Large single PR (73 files) awaiting a human reviewer | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000298` | Author absent while another member remediates and merges his PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migra | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Decision items on his PRs resolved without him | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | PR-description accuracy | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

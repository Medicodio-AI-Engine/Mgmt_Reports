# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-19 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_19_Employee_Rating_Cards.md, 2026_09_19_Mgmt_Activity_Report.md; dated by filename only, no stated review date

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_19_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_19_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Review-log / standards-log / atlas refresh commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | "Repair what the pre-push gate surfaced" (type errors, imports, JSX) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Function-header relocation/restoration | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Reviewer pushes 20–44 fix commits to a peer's PR then merges it | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Hand Devin the 11 "Remaining items — author/user decision" from her own log as bounded PRs (R16 enforcement on two CREATE paths; single owner for the three regi | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Devin-generated review-log/atlas commit from gate output, replacing 7 hand commits per PR. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000288` | Run the Devin QA gate against the PR's preview before approval; paste the verdict into the approval body. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Reviewer remediates, then approves and merges (no independent approver) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Merge with own open pre-merge list | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | QA verdict consumed after merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Header relocation / review-log commits by hand | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Gate-surfaced repair commits after push | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Oversized single PR (>200 files) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000295` | Devin drafts the §12.4/§12.5 measurement PR (read-only queries, p50/p95 harness) — well-defined, bounded. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000296` | Devin opens one PR per "major" (#5–#11 in the review) with the acceptance test stated in the log. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Devin regression tests for the demotion-rejection and inheritance/PII-exclusion paths the QA gate could not exercise (7f items). | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000298` | Oversized single PR | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000299` | Author's own findings dispositioned by reviewer | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-05 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_05_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_05_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Fixing another author's PR to merge-readiness, then approving it | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000283` | Backfilling "mandatory function headers" and `docs(headers)` commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Repairing specs broken by fix commits (`realign five specs`, `repair three specs the gate run surfaced`) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | `docs(review-logs): record …` commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000286` | Merging `dev` into a 100+-file feature branch and repairing the merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Good Devin Candidate — "Convert the 20-blocker list from the `#1305` review into an automated DVR pre-review checklist (tenancy predicate on every firm-scoped q | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000288` | Good Devin Candidate — "Write a regression test that fails when a `dev` merge into a feature branch reduces the `onRowClick`/fix count on files touched by both  | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000289` | Possible Devin Candidate — "Propose a ≤ 60-file split plan for the next letter-groups/support-letter feature along the shared-types → db → api → web seam" — hum | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000290` | > 100-file feature PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000291` | Remediate-then-approve (non-independent review) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Approve with own open blockers/decisions | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Repairing test mocks/fixtures after interface changes (`repair stale test mocks`, `repair 3 pre-existing test-fixture bugs`, `repair gate-failing test/registry drift`) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Fixing the blocker in a PR she is reviewing | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Standards-audit log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Good Devin Candidate — "Re-run the 39/42 quality gates on the `#1305`/`#1318` merge commits and post the raw table to the PR; open issues for any gate that is n | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so t | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000298` | Possible Devin Candidate — "Implement the four open decisions on `#1305` (owned-rule guidance columns, canonical tier precedence, N+1 in the interactive tx, `Do | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | 100+-file PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000300` | Reviewer fixes the blocker, then approves | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | PR-body claims not matching verification | SECURITY_TENANCY | globalcodio-monorepo | — | — | — | CODE_CHANGE |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-07 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_07_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_07_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000283` | Recording review passes as `docs(review-logs)` commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000285` | Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number f | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inher | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the co | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Approves and merges a branch he remediated | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Own "needs decision" items left open at merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | `#1278` `importSession` SEV-High finding without fix or waiver | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Large unreviewed branches | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000293` | Insufficient data — one commit in the week | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Devin findings on own PR unanswered | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Open PR not progressed by its author | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-08-30 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_08_30_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_08_30_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000002` | Low automation-adoption signal for akanksh-rv | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000282` | Hand-writing the `/check` → `/fix` remediation commits after each gate run | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Authoring the review-log markdown for each gate pass | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Re-deriving whether a Devin finding is real | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Delegate a permission/scope matrix suite for `MyAiWorkService` — one case per (caller permission × instance filter) combination. Two of this window's bugs and o | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Delegate the `data_flows.md` AI Case Manager entity section, the one gap her own review left open and recommended as a fast follow-up. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Delegate the `/fix` remediation pass on her next feature close-out and keep the review for herself, so verification and remediation are not done by the same han | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Approve-and-merge within seconds of the last automated report | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000289` | Reviewer and remediator are the same person | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Hand-fixing blockers found by his own audit pass on a Devin-authored branch | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000291` | Re-running and re-recording gate results across three review logs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Discovering that a spec suite mocks the data layer and therefore cannot fail | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Delegate a non-mocked content-sync integration suite (export → bundle → import → rollback against a real schema). This is the highest-value delegable suite in G | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000294` | Delegate the export/import round-trip fixtures for every registry table, including the JSON-expression natural key case that failed. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Delegate the six `[needs decision]` items as one scoped follow-up PR with his decisions written as acceptance criteria — they are currently merged and unresolve | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Reviewer-of-own-work | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Very large PR instead of a reviewable series | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000298` | Merge with `[needs decision]` items open | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Implementing near-identical subscriber + notification + repository-hook trios per AI skill | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000300` | Accumulating many phases on one branch before opening a PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Hand-writing per-phase tests unevenly (3 of 8 commits) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000302` | Delegate the subscriber/notification test matrix for the draft-letter skill (fired / not fired / duplicate / permission-denied), covering the paths the AI Revie | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000303` | Delegate the AI-skill registry contract test so any new skill provider must satisfy the same interface the `DraftStepStartedSubscriber` rewire assumes. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000304` | Delegate phase-by-phase PR preparation: each numbered phase becomes its own small PR with the acceptance criteria you already write in the commit subject. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | One very large PR instead of a reviewable series | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000306` | Tests that encode current behaviour rather than intended behaviour | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | No observable Devin leverage | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000308` | Signing off large merges with a one-word body | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000309` | Manually judging whether a large PR is safe to merge | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000310` | Assembling the release/promotion summary | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000311` | Delegate a pre-merge gate check — a small CI job (Devin can write it in one scoped session) that blocks merge while any Devin Review finding or `[needs decision | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Delegate generation of the merge/promotion summary from the commit range so the approval body is substantive by construction. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000313` | Approval without content on a very large PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Merge over an unresolved findings/decision set | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-04 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_04_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_04_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Function-header / design-token / a11y backfill before approving | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Writing review-log files for `/check`, `/fix`, `/architect-review` | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Approving with the word `approved` after a long COMMENTED review | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Delegate the regression tests for the two NEEDS-DECISION items she verified on `#1280` (`{{{x}}}` triple-brace scan, uppercase-scalar → Gemini routing) so the d | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000286` | Delegate the mechanical `/fix` remediation on incoming PRs and review the result, instead of authoring 16–20 commits per PR herself. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Split `#1305` (109 files) with Devin extracting the shared-types/db layers into a first PR. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000288` | Reviews and merges a branch after authoring a large share of its final commits | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Syncing long-lived branches with `dev` and hand-resolving semantic conflicts | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000290` | Restoring capabilities lost in syncs | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000291` | Standards/architect/PR review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Delegate the `importSession` infinite-spinner fix from the `#1278` gate (reproduction and severity already documented by the gate). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Delegate a branch-drift check that comments on a PR when its head is > 100 commits behind `dev`. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Delegate the content-sync bundle-corpus integration suite (named 08-30 and 09-03, still absent). | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000295` | Approves/merges a branch he remediated | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | `#1278` NOT READY verdict unaddressed | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | 0-char approvals on train promotions | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000298` | Closing stale Devin QA-report PRs by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000299` | Merging `dev` into `feat/qa-automation` (`#1299`, `#1296`, `#1250`) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000300` | Delegate a persona-credential preflight that runs before every gate and posts one org-admin blocker instead of five identical no-verdict comments. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Delegate the PR body for `#1314` from the diff + PRD deviations he recorded in commit messages. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Delegate the attachment-scan-never-runs regression test (the bug he fixed at 18:51). | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000303` | Empty approval on a production promotion | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000304` | Template-only PR body | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000305` | QA gate verdict not on the promotion path | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000306` | PRD decision-log commits (`record D25`, `record D26`) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | Merging `dev` into a 160-file feature branch | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Delegate splitting the next feature (letter groups had a clean shared-types/db/api/web layering) into ≤ 60-file PRs. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000309` | Delegate the letter-group tenancy/IDOR probes the gate could not run. | SECURITY_TENANCY | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000310` | Delegate the "cloned Process Types" and "dismissed items" progress tests saijyoti had to write for him. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | > 100-file feature PR | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000312` | Seven `/fix` remediation passes on one PR | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000313` | `dev` merge into the feature branch (313 files) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Delegate a ledger-consistency test: N recipients → N rows all reach a terminal state on success and failure paths. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Delegate the BCC-visibility authorisation test across the three viewer roles. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Delegate the flaky-gate investigation for the compose recipient arrays. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | None supported by history | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000318` | Reviewer completes the PR (16 of 22 commits) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000319` | Large style-only commits (`rounded-sm`, 10 files) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000320` | Delegate the CAS fix + test on `incrementFailedAttempts`. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Delegate a Devin standards pass before opening the PR so the reviewer's commit share drops. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Split the 57-file `mobbin-trails` commit before it becomes a 100-file PR. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000323` | Reviewer authors the majority of final commits | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Fixing spec compile errors after `dev` merges (7 spec files) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000325` | Replying "Fixed in <sha>" per thread | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000326` | Delegate the two oversized-file refactors logged as deferred (`organization-detail-page-client.tsx` > 700 lines). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000327` | Delegate a split plan for `#1284` (145 files, two days open). | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000328` | Delegate the entity-status DTO shape test across the four entities. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000329` | > 100-file PR with template header | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000330` | None in-window | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000331` | Delegate the merge-token regression test named on 09-03 for `#1288`. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000332` | One-word approvals on promotions | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000333` | Empty approvals on `Dev_1.0` merges | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000334` | Badge-only PR bodies on his own PRs | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000335` | Parallel nodejs + react commits for the same change | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000336` | Delegate a deploy-failure watcher that comments on the merged PR when `Trigger Deployment` fails (would have surfaced today's two failures). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000337` | Delegate PR-body generation for `#249`-style multi-week PRs. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000338` | Delegate a coder-performance dedupe regression test (the bug he fixed today). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000339` | Empty approvals within minutes | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000340` | Badge-only bodies | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000341` | Promotion PRs with badge-only bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000117` | `lgtm` approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000342` | Delegate the promotion-body generator for `#608`/`#536`. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000343` | Delegate the analytics BE↔FE taxonomy contract test (named 09-02 and 09-03, still absent). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000344` | Delegate answering the 12 findings on `#608` before it is merged to production. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000345` | One-word / empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Badge-only promotion bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000347` | KB dataset loader + page pairs (`kb-asc`, earlier `invoicing-billing-suite`) | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000348` | Delegate a golden-file test for the ASC addenda loader (no tests in either PR). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Delegate the 10 Devin findings as a follow-up PR. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000350` | None supported by history | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000351` | `okay` approval + merge + immediate prod promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000352` | `okay` approvals on production merges | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000353` | Badge-only body on a prod promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000354` | Multi-concern commits | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000355` | Delegate additional-code range fixtures per specialty (Pediatrics first). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000356` | Delegate answering the 14 open findings before the next promotion. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000357` | Template/badge-only body on prod promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000358` | None supported in-window | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000359` | Delegate the regression test over the 821 parents he counted. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000360` | None | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000361` | Delegate a property test for the conservation guard (every line lost from `others` appears in an accepted destination). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000362` | Template body on prod promotion | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000363` | None supported | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000364` | Delegate the 99205/99215 minutes-table test (named 09-03; still absent). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000365` | None with history | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000366` | Same-day `Dev → Uat → prod` promotion with badge bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000367` | Delegate golden-file tests for the `others` parser and the Trinity/PPV parsers named 09-03. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-22 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_22_Employee_Rating_Cards.md, 2026_09_22_Mgmt_Activity_Report.md; dated by filename only, no stated review date

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_066 | EMPLOYEE_RATING_CARDS | `2026_09_22_Employee_Rating_Cards.md` | no |
| SOURCE_067 | DAILY_ENGINEERING_DETAIL | `2026_09_22_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-written `docs(review)` audit/architect/gate-result logs committed to the feature branch | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | Bulk-closing Devin QA/report PRs without a note | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000284` | Self-authored review + self-merge on own PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Delegate the F-6/F-1 items Devin already documented (`#1398`, `#1401` DEV-FIX-LIST #9 "Unclassified" grouping in `apps/web`) as scoped Devin fix PRs instead of  | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Use Devin to generate the review log from the PR thread rather than committing it — Good Devin Candidate. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000287` | Keep architectural decisions (`ADR-0058`, strategy-chain design) human-owned — Primarily Human-Owned; no change recommended. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Author merges own PR into `dev` after self-review | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Devin PRs closed without disposition | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000290` | 0-character approvals given/received | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Manual live A/B repro writing for each QA finding, committed as markdown | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Merging large PRs with a 0-char approval | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Devin to write the org-scope/data_scope authorization regression suite for `/cases/:id/steps` and the `#1398` F-1 endpoint together — Good Devin Candidate (both | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000294` | Devin to open the `#1362` `ACR_NAME` prerequisite fix and a `dry_run` dispatch test — Good Devin Candidate (Devin already diagnosed it). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Triage of the 14 `#1394` findings — Possible Devin Candidate (Devin drafts dispositions; author decides). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | 0-character approval on large PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Workflow shipped without its documented prerequisite | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000298` | Long-lived feature branch without PR until very large | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Devin to write component/render tests for DOCX export and toolbar — Good Devin Candidate. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000300` | Open a draft PR now so Devin Review runs on each push — Good Devin Candidate (process). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | (none confirmed today) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Empty approval on a peer PR with open Devin findings | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Devin to generate API contract tests for the service-provider module before PR — Good Devin Candidate. | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000304` | (none confirmed) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Post-merge audit reports as markdown | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000306` | Devin to implement the `batchUpsertForceOverride` party-identity fix now that a pinning test exists — Good Devin Candidate. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | Decision items left open after merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Reviewer remediates peer PR with 20–44 commits then approves/merges (Saijyoti) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000309` | Devin to fix the `#1398` F-1 module-access bypass with regression test — Good Devin Candidate (Saahil/Saijyoti to review). | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000310` | Post-merge NOT READY verdict unacknowledged | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000311` | Manual prompt-surface audits (orphans, dead registry rows, spelling) | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000312` | Manual dx-vs-px consistency checks on empty/edge documents | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000313` | Devin to build the regression harness around `_stage_io.json` captures (golden per-stage outputs on a fixed chart set) — Good Devin Candidate. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000314` | Devin to generate the prompt-registry lint — Good Devin Candidate. | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000315` | Clinical vocabulary decisions (approach taxonomy, CARE-STATUS rule) — Primarily Human-Owned. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000316` | `feat/inpatient-engine` without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Bulk prompt version swaps (15 prompts) without recorded output diff | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000318` | Prompt A/B diff harness — Good Devin Candidate. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000319` | Branch without PR (shared) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000320` | Prompt edits with contentless commit messages | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Devin to summarise a prompt diff into a commit message — Good Devin Candidate. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Low-information commit messages | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Feature → `uat` → prod on the same day with the same reviewer and one-word approvals | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000324` | Devin to disposition the 8 `#467`/`#468` findings (fix or reasoned rejection) — Good Devin Candidate; the SEC items need human sign-off. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000325` | Devin to add unit tests for the empty-slice guard described in the body — Good Devin Candidate. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000326` | Prod promotion with unanswered Devin findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000327` | Promotion PR with empty body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000328` | Promotion-body generation — Good Devin Candidate. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000329` | Facility-scope billing rules — Primarily Human-Owned (correctly human). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000330` | Prod promotion merged within seconds | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000331` | One-word approval + immediate merge as gatekeeper for `uat`/prod | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Devin pre-merge summary comment listing open findings per PR so the gatekeeper has a checklist — Good Devin Candidate. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000333` | One-word approval on prod promotion with open findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000334` | Manual `apps/backend | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000335` | Regenerated `repo-structure.md` commits | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000336` | Prod promotion PRs with badge-only bodies | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000337` | Scheduled Dev_1.0 → application-2.0 sync PR — Good Devin Candidate. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000338` | Disposition of the 9 promotion findings — Possible Devin Candidate (Devin drafts, human decides for prod). | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000339` | 0-char approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000340` | Prod promotion with unanswered Devin findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000341` | Instant 0-char approve + merge of promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000342` | Devin to write pg-notify reconnection/cache-invalidation integration tests for `#660` — Good Devin Candidate. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000343` | 0-char approve + merge of peer prod promotions within minutes | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000344` | Self-merge after peer approval | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000345` | Payer/back-port fixes landing without PR or via self-merge | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Contract test for the RPA webhook payload — Good Devin Candidate. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | (none confirmed today) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000348` | Self-merged PRs without review in this repo | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Enable Devin Review on the repo — Good Devin Candidate (config). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000350` | (none new) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000129` | — | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000351` | `#435` without reviewer | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

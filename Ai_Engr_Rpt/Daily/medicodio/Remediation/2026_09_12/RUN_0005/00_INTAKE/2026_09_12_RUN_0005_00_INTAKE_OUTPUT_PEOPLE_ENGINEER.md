# Intake — normalized findings

**Run:** `RUN_0005` · **Report date:** 2026-09-12 · **Stage:** `00_INTAKE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

## Sources

| Source | Type | File | Date verified |
| ------ | ---- | ---- | ------------- |
| SOURCE_010 | EMPLOYEE_RATING_CARDS | `2026_09_12_Employee_Rating_Cards.md` | no |
| SOURCE_011 | DAILY_ENGINEERING_DETAIL | `2026_09_12_Mgmt_Activity_Report.md` | no |

Completeness: **COMPLETE**

## Normalized issues

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Header / PRD-status / review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | dev→uat→main promotion PRs with template body | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000284` | Lockfile churn undo (`fix(deps): restore the minimal lockfile`, `revert the package.json export-map re-sort`) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Devin-generated regression tests for the cookie/CSRF auth path — five session-correctness defects were found and fixed in one commit at 16:42; each should be pi | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000286` | Delegate the 16 still-open Devin findings on `#1363` as a bounded remediation batch, with anirudh reviewing rather than fixing. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Devin drafts the release note for `#1361` (647 commits to `main`) — currently the body is the untouched template. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000288` | None recurring today — 09-11 Repeat Patterns (REQUEST CHANGES → own approve; remediate-approve-merge) did not occur | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000289` | `docs(review-logs)` / tech-debt ledgers | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000290` | Restoring review-log files overwritten by a merge (2 commits) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000291` | Remediating other authors' PRs to merge | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Run the Devin QA gate on the `#1366` branch before merge — two consecutive post-merge NOT READY verdicts (`#1316`, `#1322`) each produced a Devin fix PR that a  | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Delegate the standards-audit fix list (header corrections, unused imports, stacking-context isolation) to Devin; keep herself on the Architect+EM review. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000294` | Have Devin generate the review-log ledger from the gate run instead of hand-writing it. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000295` | Repeat Pattern: reviewer remediates, approves and merges the same PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Repeat Pattern: QA gate runs after merge and returns NOT READY | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000297` | PRD/changelog reconciliation ("reconcile the PRDs with what shipped") | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | Review-log ledgers (2 today) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000299` | Merging `dev` into feature branch (2 today) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Delegate the 3 SEC + 3 BUG findings on `#1367` to Devin with acceptance tests, then review the diff — the surface (reading client email, proposing actions) warr | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Devin writes the e2e regression pack from the "nine defects" list. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Repeat Pattern: remediator on another author's PR (approve/merge half did not occur today) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Timestamp-display migration | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000304` | Role/permission matrix moves between portals (3 `refactor(` commits) | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Merging `dev` into `feat/hr-portal-revamp` | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Open `feat/hr-portal-revamp` as a draft PR so the same finding→fix loop that worked on `#1365` runs on ~7k lines of HR role/permission code (security-relevant). | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000307` | Devin generates permission-matrix tests for the HR implicit baseline ("let an employee through without one"). | MISSING_TEST | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000308` | Emerging (not yet Repeat): `feat/hr-portal-revamp` without a PR | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000309` | Spec-mock repairs "so tests reach the code they name" | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000310` | React duplicate-key / label-as-key fixes | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000311` | Devin sweeps `apps/web` for other components keyed by display label (the `#1364` body says "A label is …" not unique) — same shape as the timezone sweep. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Delegate the 2 open audit-SQL findings on `#1360`. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000313` | None meeting the recurrence bar | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Approving promotion PRs 0-char (`#1361` today) | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000315` | Change digest + test plan per merged PR | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000316` | Devin adds a dry-run test for `acr-purge.sh` (live-revision guard) before it runs against the registry. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Formalise the split observed today: Devin writes the QA digest (`#1368`), ragha82 adjudicates. | MECHANICAL_MIGRATION | globalcodio-monorepo | — | — | — | CODE_CHANGE |
| `ISSUE_000318` | Insufficient data | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000319` | Review `#1358` — the failures are in surfaces this author built. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000320` | Repeat Pattern: absent from follow-up on own PRs | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Review `#1369` (2 fixes to his feature) — it needs "a human call" per Devin's own comment on the size-0 semantics. | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Repeat Pattern: long-open PR advanced to merge by others | PROCESS_PRACTICE | globalcodio-monorepo | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Same fix as two PRs (Dev + UAT): `#638`/`#641`, `#570`/`#572` | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000324` | dev→uat promotion PRs "dev to uat" | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000325` | Reciprocal 0-char approvals with Jatin | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000326` | Devin-generated regression tests for the provider-override marker lifecycle — 6 fix commits today on the same marker (hide/keep/clear/first-service leak). | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000327` | Devin triages the 9 findings on `#308` (prompt-registry sync script) into fix/no-fix before human review. | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000328` | Devin drafts the release note for `#626` (37 files to prod) from its 43 commits. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000329` | Repeat Pattern: empty-body approvals on PRs with open Devin findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000330` | Same removal as two PRs (Node `#639` + React `#571`) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000331` | Reciprocal 0-char approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Promotion PRs with badge-only body | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000333` | Devin writes the migration safety note for `20260911_001_system_actor_users.sql` and `20260911_002_client_columns_cleanup.sql` — both got ANALYSIS/BUG findings  | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000334` | Devin drafts release notes for `#626`/`#557` (102 files to prod today, badge-only bodies). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000335` | Repeat Pattern: merge/approve before or immediately after Devin posts findings | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000336` | Repeat Pattern: empty approvals | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000337` | UAT → prod → Dev back-port of the same change (3 PRs + 1 abandoned sync) | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000338` | Design-doc + QA-report per feature | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000339` | Devin writes retry/timeout unit tests for `http_retry.py` — 3 BUG findings on it across `#309`/`#310`/`#312`, none answered. | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000340` | Devin drafts the `#314` body (66 files to UAT) from the 78 commits. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000341` | Repeat Pattern: manual UAT→Dev back-port | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000342` | Repeat Pattern: prod promotion before/with un-dispositioned findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000343` | E&M mapping-table edits | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000344` | Deleting obsolete standalone test runners | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000345` | Devin generates the E&M level-selection test matrix from the rank tables in `service_registry.py` (the max-code and rank-lookup bugs Devin found are exactly mat | MISSING_TEST | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000346` | None meeting the recurrence bar | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000347` | "okay" approvals on promotions | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000348` | Batch-closing stale engine PRs | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Devin summarises each `uat → release/prod_3.0` PR's findings into a go/no-go line for him to sign. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000350` | Repeat Pattern: "okay" approvals on prod promotions before/with open findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000351` | UAT→prod promotion PRs | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000352` | Devin validates client config files against schema before promotion (carried from 09-11). | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000353` | Repeat Pattern: prod promotion with open Devin findings | MECHANICAL_MIGRATION | unresolved | — | — | — | CODE_CHANGE |
| `ISSUE_000354` | PCS guideline rule → code + fixture | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000355` | Diagnosing "X never saw Y" key mismatches (3 today) | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000356` | Devin writes a contract test between the extraction output and PCS input — three of today's bugs were key-name/shape mismatches ("PCS never saw the approach", " | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000357` | Draft PR so Devin Review covers the +4.4k lines added this week. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000358` | Repeat Pattern: inpatient engine branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000359` | Answer-key / seed fixes bundled into feature commits | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000360` | Long-running branch without PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000361` | Devin maintains the answer keys from the case specs (carried). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000362` | Draft PR so a 49-file commit is not the first thing a reviewer sees at merge time. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000363` | Repeat Pattern: inpatient work on long-lived branches without a PR | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000364` | Insufficient data today | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000365` | Devin diff-summarises prompt changes into commit bodies (carried). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000366` | Repeat Pattern: low-information commit messages (did not recur today) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000367` | Excel formatting of POC output | AUTOMATION_OPPORTUNITY | unresolved | — | — | — | TOOLING_AUTOMATION |
| `ISSUE_000368` | Devin writes the Excel export formatter with a snapshot test so "beautify" commits stop. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000369` | Repeat Pattern: low-information / typo commit messages | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000128` | Insufficient data | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000370` | Devin rebases `#435` and summarises what of `#382`/`#434` it supersedes. | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000371` | Enable Devin Review on the RPA repository (carried; not observable as done). | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |
| `ISSUE_000372` | Repeat Pattern: RPA self-merge (no occurrence today — no PRs) | PROCESS_PRACTICE | unresolved | — | — | — | NON_CODE_PROCESS |

Findings derived only from employee rating cards are marked corroborating-only and cannot justify a code change on their own.

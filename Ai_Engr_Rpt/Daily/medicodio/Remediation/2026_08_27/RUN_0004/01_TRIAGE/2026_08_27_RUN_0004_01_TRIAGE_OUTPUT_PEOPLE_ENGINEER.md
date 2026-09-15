# Triage — priority and complexity

**Run:** `RUN_0004` · **Report date:** 2026-08-27 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000001` | Low automation-adoption signal for SaijyotiMeti | PROCESS_PRACTICE | unresolved | 1 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000050` | Low automation-adoption signal for jatinkushwaha-medicodio | PROCESS_PRACTICE | unresolved | 1 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000198` | Low automation-adoption signal for amit-pandey-medicodio | PROCESS_PRACTICE | unresolved | 1 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000199` | Hand-writing `/check` + `/fix` review-log markdown | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000200` | Backfilling tests that the original branch omitted | MISSING_TEST | globalcodio-monorepo | 6 | 4 | — | CODE_CHANGE |
| `ISSUE_000201` | RBAC gate-parity sweeps (read paths missing a guard) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 8 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000202` | Delegate #1245 (idempotency keys on five note-creation endpoints) to Devin with the acceptance criteria already in the issue — it is bounded, repetitive across  | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000203` | Delegate a repo-wide "controller methods without an authz decorator" audit; she has now found this class of gap on three separate branches. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000204` | Have Devin produce the review-log entry from the gate output at the end of each `/fix` cycle instead of writing it manually. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000205` | Review quality concentrated in one or two people | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000206` | Post-hoc remediation of someone else's large branch | PROCESS_PRACTICE | globalcodio-monorepo | 6 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000207` | Bounding unbounded list reads | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000208` | Regenerating architecture docs (`screen_index`, `module_map`, `data_flows`) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000209` | Split #1244 into reviewable slices (schema + sync engine + admin surface) and let Devin do the mechanical split, so a second person can actually review it. | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000210` | Delegate the repo-wide unbounded-read audit — he has now fixed eight instances by hand in one day. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000211` | Delegate architecture-doc regeneration as a recurring session. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000212` | Very large PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000213` | Review record kept off the PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000214` | Fixing the same class of Devin Review finding across create dialogs / read surfaces | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000215` | Re-stating firm-scoped settings reads per surface | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000216` | Ask Devin for the collision/scoping test matrix (manual vs generated, org vs firm scope, settings loading) before implementation — it would have pre-empted seve | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000217` | Open a Devin session to rebase and slice #1239 into reviewable parts so it can land. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000218` | Delegate the "read display settings under the caller's org scope" audit across the remaining portals. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000219` | Devin PR left open without a reviewer | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000220` | Many review cycles caused by unstated acceptance criteria | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000221` | Large feature branch remediated by a reviewer after the fact | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 8 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000222` | Run a Devin session against the diff before opening a PR of this size, with the repo's own gate rules as acceptance criteria. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000223` | Delegate the audit-row and authz-decorator coverage checks that anirudh had to add by hand. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000224` | Very large single PR | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000225` | QA defects filed as issues that no one picks up | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000226` | Delegate #1242 (partial-success sheet state) to Devin directly from the issue — it is a bounded frontend state bug. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000227` | Delegate #1240 (pre-filled emails on new templates) the same way. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000228` | Use Devin to write the regression test for #1241 (questionnaire bundle import performance) before optimising it. | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000229` | QA issues filed but not delegated | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000230` | Section/field rename fixes in chart-fetch (`emr_appointment_type` → `emr_visit_type`) | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000231` | UAT→prod promotion PRs | MECHANICAL_MIGRATION | unresolved | 5 | 7 | — | CODE_CHANGE |
| `ISSUE_000232` | Delegate regression tests for the exclusion-validation lane — the fix changed lane wiring with no test commit. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000233` | Delegate an EMR section-alias test so the next rename fails in CI rather than in charts. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000234` | Devin Review findings unaddressed at merge | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000235` | Long-lived `feat/guideline` branch landed as one 223-file PR | PROCESS_PRACTICE | unresolved | 3 | 7 | — | NON_CODE_PROCESS |
| `ISSUE_000236` | Non-descriptive commit messages ("Testing the ggl changes") | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000237` | Delegate a regression test for the single-anchor `linking_removal` path — the bug was that a whole chart class was skipped, which is exactly what a test pins. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000238` | Delegate splitting the next guideline change into reviewable slices. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000239` | Delegate a diff summary for the prod promotion PR body so the reviewer has something to read. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000240` | Oversized change promoted straight to prod | PROCESS_PRACTICE | unresolved | 2 | 7 | — | NON_CODE_PROCESS |
| `ISSUE_000241` | Non-descriptive commit messages | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000242` | Approving and merging promotion PRs with a one-word body | MECHANICAL_MIGRATION | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000243` | Manual UAT→prod promotion PRs | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000244` | Low-information approvals as the review record | MECHANICAL_MIGRATION | unresolved | 4 | 6 | — | CODE_CHANGE |
| `ISSUE_000245` | Prod promotion within minutes of UAT | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000246` | Long-lived draft PR with slow trickle of commits | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000247` | Write the remaining scope of #393 as acceptance criteria and hand the mechanical parts (persistence, retrieval tests) to Devin. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000248` | Delegate a benchmark/test harness for recall quality so the draft can be evaluated rather than debated. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000249` | Removing PHI/sensitive columns from API responses one endpoint at a time | AUTOMATION_OPPORTUNITY | unresolved | 9 | 9 | — | TOOLING_AUTOMATION |
| `ISSUE_000250` | Syncing `Dev_1.0` into the feature branch by hand | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000251` | `lgtm` approvals on prod promotions | MECHANICAL_MIGRATION | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000252` | Delegate a PHI-masking regression suite covering masked date formatting, dispatch-batch responses and grant-based unmasking — the three defects he fixed by hand | MISSING_TEST | unresolved | 9 | 8 | — | CODE_CHANGE |
| `ISSUE_000253` | Delegate the remaining "dialog dropdowns → portalled `AnchoredPanel`" migration across other dialogs. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000254` | Delegate the dashboards documentation sync that consumed three separate PRs on one branch. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000255` | `lgtm` as the review record on prod-path PRs | PROCESS_PRACTICE | unresolved | 2 | 7 | — | NON_CODE_PROCESS |
| `ISSUE_000256` | Self-merge | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000257` | No tests with behaviour changes | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000258` | Opening UAT→prod promotion PRs across two repos | MECHANICAL_MIGRATION | unresolved | 5 | 7 | — | CODE_CHANGE |
| `ISSUE_000259` | Approving with an empty body | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000260` | Delegate generation of the promotion PR body: changed areas, migrations included, risk and rollback — today's promotions shipped 100+ files across two repos wit | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000261` | Delegate tests for #248's new insurance-created flag before it merges (35 files, no test commits). | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000262` | Delegate a "release notes from the diff" session for each promotion pair. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000263` | Empty approvals as the review record | PROCESS_PRACTICE | unresolved | 2 | 7 | — | NON_CODE_PROCESS |
| `ISSUE_000264` | Promotion PRs with no written risk/rollback note | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000265` | Applying the same dropdown/portal pattern across dialogs | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000266` | Long-lived personal feature branches (`hitesh/...-20260825`, `hitesh/invoicing-billing-suite-20260807`) | PROCESS_PRACTICE | unresolved | 6 | 9 | — | NON_CODE_PROCESS |
| `ISSUE_000267` | Delegate the remaining dialog→portalled-dropdown migration, using #499 as the reference diff. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000268` | Delegate component tests for the Prediction Trail redesign (38 files, no test commits observed). | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000269` | Open a draft PR (or a Devin session) for the long-lived invoicing/billing branch. | PROCESS_PRACTICE | unresolved | 5 | 10 | — | NON_CODE_PROCESS |
| `ISSUE_000270` | Manual repetitive UI pattern migration | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000271` | Promotion fan-out: the same change carried through `import_main` → `Uat_1.0` → `release/prod_1.0` as separate PRs | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 5 | 3 | — | CODE_CHANGE |
| `ISSUE_000272` | Re-deciding batch-status semantics case by case | MISSING_TEST | medicodio-nextgen-integration | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000273` | Hotfix pairs (prod fix + backport) | PROCESS_PRACTICE | medicodio-nextgen-integration | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000274` | Delegate a pytest suite for the four batch-status invariants (failed-preprocess, never-run, re-run subset, max-wins counts) — they are now precisely specified i | MISSING_TEST | medicodio-nextgen-integration | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000275` | Delegate a promotion script/workflow that opens the `import_main`→UAT→prod chain with diff summaries. | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000276` | Delegate a repo scan for other secret-bearing file patterns after the `.pem` fix. | PROCESS_PRACTICE | medicodio-nextgen-integration | 5 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000277` | Self-merge into `import_main` | PROCESS_PRACTICE | medicodio-nextgen-integration | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000278` | Behaviour changes with no tests | PROCESS_PRACTICE | medicodio-nextgen-integration | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000279` | Manual promotion fan-out | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000280` | One-word approvals on promotion/hotfix PRs | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000281` | Approvals with no content | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |

## Scoring rationale

### `ISSUE_000001` Low automation-adoption signal for SaijyotiMeti

- Priority: Priority 1/10 from base 3 adjusted by: non-code process item, no software risk (-1); rating-card corroboration only, not defect evidence (-2).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.3

### `ISSUE_000050` Low automation-adoption signal for jatinkushwaha-medicodio

- Priority: Priority 1/10 from base 3 adjusted by: non-code process item, no software risk (-1); rating-card corroboration only, not defect evidence (-2).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.3

### `ISSUE_000198` Low automation-adoption signal for amit-pandey-medicodio

- Priority: Priority 1/10 from base 3 adjusted by: non-code process item, no software risk (-1); rating-card corroboration only, not defect evidence (-2).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.3

### `ISSUE_000199` Hand-writing `/check` + `/fix` review-log markdown

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (23) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000200` Backfilling tests that the original branch omitted

- Priority: Priority 6/10 from base 3 adjusted by: category MISSING_TEST (+2); high reported frequency (23) (+1).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000201` RBAC gate-parity sweeps (read paths missing a guard)

- Priority: Priority 8/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); security scope AUTHORIZATION (+3); high reported frequency (25) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1); security-sensitive surface AUTHORIZATION (+2).
- Confidence: 0.55

### `ISSUE_000202` Delegate #1245 (idempotency keys on five note-creation endpoints) to Devin with the acceptance criteria already in the issue — it is bounded, repetitive across 

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000203` Delegate a repo-wide "controller methods without an authz decorator" audit; she has now found this class of gap on three separate branches.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000204` Have Devin produce the review-log entry from the gate output at the end of each `/fix` cycle instead of writing it manually.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000205` Review quality concentrated in one or two people

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000206` Post-hoc remediation of someone else's large branch

- Priority: Priority 6/10 from base 3 adjusted by: security scope AUTHORIZATION (+3); high reported frequency (1238) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1); security-sensitive surface AUTHORIZATION (+2).
- Confidence: 0.65

### `ISSUE_000207` Bounding unbounded list reads

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000208` Regenerating architecture docs (`screen_index`, `module_map`, `data_flows`)

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (22) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000209` Split #1244 into reviewable slices (schema + sync engine + admin surface) and let Devin do the mechanical split, so a second person can actually review it.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000210` Delegate the repo-wide unbounded-read audit — he has now fixed eight instances by hand in one day.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000211` Delegate architecture-doc regeneration as a recurring session.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000212` Very large PRs

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000213` Review record kept off the PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000214` Fixing the same class of Devin Review finding across create dialogs / read surfaces

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1243) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000215` Re-stating firm-scoped settings reads per surface

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000216` Ask Devin for the collision/scoping test matrix (manual vs generated, org vs firm scope, settings loading) before implementation — it would have pre-empted seve

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000217` Open a Devin session to rebase and slice #1239 into reviewable parts so it can land.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000218` Delegate the "read display settings under the caller's org scope" audit across the remaining portals.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000219` Devin PR left open without a reviewer

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000220` Many review cycles caused by unstated acceptance criteria

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000221` Large feature branch remediated by a reviewer after the fact

- Priority: Priority 8/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); security scope AUTHORIZATION (+3); high reported frequency (1238) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1); security-sensitive surface AUTHORIZATION (+2).
- Confidence: 0.65

### `ISSUE_000222` Run a Devin session against the diff before opening a PR of this size, with the repo's own gate rules as acceptance criteria.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000223` Delegate the audit-row and authz-decorator coverage checks that anirudh had to add by hand.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000224` Very large single PR

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000225` QA defects filed as issues that no one picks up

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (1242) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000226` Delegate #1242 (partial-success sheet state) to Devin directly from the issue — it is a bounded frontend state bug.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000227` Delegate #1240 (pre-filled emails on new templates) the same way.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000228` Use Devin to write the regression test for #1241 (questionnaire bundle import performance) before optimising it.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000229` QA issues filed but not delegated

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000230` Section/field rename fixes in chart-fetch (`emr_appointment_type` → `emr_visit_type`)

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000231` UAT→prod promotion PRs

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (399) (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000232` Delegate regression tests for the exclusion-validation lane — the fix changed lane wiring with no test commit.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000233` Delegate an EMR section-alias test so the next rename fails in CI rather than in charts.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000234` Devin Review findings unaddressed at merge

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000235` Long-lived `feat/guideline` branch landed as one 223-file PR

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (25) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 7/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2).
- Confidence: 0.65

### `ISSUE_000236` Non-descriptive commit messages ("Testing the ggl changes")

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000237` Delegate a regression test for the single-anchor `linking_removal` path — the bug was that a whole chart class was skipped, which is exactly what a test pins.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000238` Delegate splitting the next guideline change into reviewable slices.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000239` Delegate a diff summary for the prod promotion PR body so the reviewer has something to read.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000240` Oversized change promoted straight to prod

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 7/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2).
- Confidence: 0.65

### `ISSUE_000241` Non-descriptive commit messages

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000242` Approving and merging promotion PRs with a one-word body

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (25) (+1).
- Complexity: Complexity 6/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2).
- Confidence: 0.65

### `ISSUE_000243` Manual UAT→prod promotion PRs

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000244` Low-information approvals as the review record

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 6/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2).
- Confidence: 0.65

### `ISSUE_000245` Prod promotion within minutes of UAT

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000246` Long-lived draft PR with slow trickle of commits

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (393) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000247` Write the remaining scope of #393 as acceptance criteria and hand the mechanical parts (persistence, retrieval tests) to Devin.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000248` Delegate a benchmark/test harness for recall quality so the draft can be evaluated rather than debated.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000249` Removing PHI/sensitive columns from API responses one endpoint at a time

- Priority: Priority 9/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); security scope PHI (+4); high reported frequency (25) (+1).
- Complexity: Complexity 9/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1); security-sensitive surface PHI (+2).
- Confidence: 0.55

### `ISSUE_000250` Syncing `Dev_1.0` into the feature branch by hand

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000251` `lgtm` approvals on prod promotions

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (577) (+1).
- Complexity: Complexity 6/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2).
- Confidence: 0.75

### `ISSUE_000252` Delegate a PHI-masking regression suite covering masked date formatting, dispatch-batch responses and grant-based unmasking — the three defects he fixed by hand

- Priority: Priority 9/10 from base 3 adjusted by: category MISSING_TEST (+2); security scope PHI (+4).
- Complexity: Complexity 8/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1); security-sensitive surface PHI (+2).
- Confidence: 0.5

### `ISSUE_000253` Delegate the remaining "dialog dropdowns → portalled `AnchoredPanel`" migration across other dialogs.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000254` Delegate the dashboards documentation sync that consumed three separate PRs on one branch.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000255` `lgtm` as the review record on prod-path PRs

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 7/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2).
- Confidence: 0.75

### `ISSUE_000256` Self-merge

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000257` No tests with behaviour changes

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000258` Opening UAT→prod promotion PRs across two repos

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (577) (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000259` Approving with an empty body

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (25) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000260` Delegate generation of the promotion PR body: changed areas, migrations included, risk and rollback — today's promotions shipped 100+ files across two repos wit

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000261` Delegate tests for #248's new insurance-created flag before it merges (35 files, no test commits).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000262` Delegate a "release notes from the diff" session for each promotion pair.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000263` Empty approvals as the review record

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 7/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2).
- Confidence: 0.65

### `ISSUE_000264` Promotion PRs with no written risk/rollback note

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000265` Applying the same dropdown/portal pattern across dialogs

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (499) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000266` Long-lived personal feature branches (`hitesh/...-20260825`, `hitesh/invoicing-billing-suite-20260807`)

- Priority: Priority 6/10 from base 3 adjusted by: security scope BILLING (+3); high reported frequency (25) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 9/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); security-sensitive surface BILLING (+2).
- Confidence: 0.65

### `ISSUE_000267` Delegate the remaining dialog→portalled-dropdown migration, using #499 as the reference diff.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000268` Delegate component tests for the Prediction Trail redesign (38 files, no test commits observed).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000269` Open a draft PR (or a Devin session) for the long-lived invoicing/billing branch.

- Priority: Priority 5/10 from base 3 adjusted by: security scope BILLING (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 10/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1); security-sensitive surface BILLING (+2).
- Confidence: 0.5

### `ISSUE_000270` Manual repetitive UI pattern migration

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000271` Promotion fan-out: the same change carried through `import_main` → `Uat_1.0` → `release/prod_1.0` as separate PRs

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (25) (+1).
- Complexity: Complexity 3/10 from: category MECHANICAL_MIGRATION base 4; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000272` Re-deciding batch-status semantics case by case

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000273` Hotfix pairs (prod fix + backport)

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (246) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000274` Delegate a pytest suite for the four batch-status invariants (failed-preprocess, never-run, re-run subset, max-wins counts) — they are now precisely specified i

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000275` Delegate a promotion script/workflow that opens the `import_main`→UAT→prod chain with diff summaries.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000276` Delegate a repo scan for other secret-bearing file patterns after the `.pem` fix.

- Priority: Priority 5/10 from base 3 adjusted by: security scope SECRETS (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1); security-sensitive surface SECRETS (+2).
- Confidence: 0.5

### `ISSUE_000277` Self-merge into `import_main`

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000278` Behaviour changes with no tests

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000279` Manual promotion fan-out

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000280` One-word approvals on promotion/hotfix PRs

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000281` Approvals with no content

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

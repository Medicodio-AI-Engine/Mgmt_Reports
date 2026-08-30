# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-08-29 · **Stage:** `01_TRIAGE` · **Status:** PARTIAL_SOURCE_DATA

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_MISMATCH: filename date and stated review date disagree; artifact excluded from automatic processing
- PARTIAL: missing DAILY_ENGINEERING_DETAIL; run continues in analysis-only mode with reduced confidence

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000002` | Low automation-adoption signal for akanksh-rv | PROCESS_PRACTICE | unresolved | 1 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000049` | Low automation-adoption signal for Pj-Vineeth-Kumar | PROCESS_PRACTICE | unresolved | 1 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000003` | Low automation-adoption signal for Amrutha-Beedikar | PROCESS_PRACTICE | unresolved | 1 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000282` | Hand-written `docs(review-logs)` evidence commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | pnpm-lock repair commits after dependency bumps | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Manual `dev`-into-branch merges | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Have Devin build the content-sync preflight matrix as tests (three environments × transportable/untransportable × ambiguous natural key) so the pass he ran by h | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000286` | Delegate the bundle-integrity regression suite covering the signature-check-fails-open class he fixed on 08-27 and the audit-stamp gap he fixed today. | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000287` | Delegate the lockfile/dependency-bump chore lane entirely. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Substance recorded in commits, approval left empty | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | A long-lived branch grows instead of landing | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000290` | Repairing specs the branch's own contract changes falsified | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000291` | Doc/PRD re-sync after each design correction | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000292` | Hand-written review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000293` | Delegate the RBAC/authorisation matrix test suite for "case access outranks AI ownership" — the exact invariant he fixed by hand today, currently pinned by noth | MISSING_TEST | globalcodio-monorepo | 8 | 6 | — | CODE_CHANGE |
| `ISSUE_000294` | Delegate the endpoint-map and Atlas generation so docs stop needing five catch-up commits. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Delegate the decomposition itself: have Devin carve #1260 into contract, API, and web PRs against the current diff. | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000296` | Very large single PR (team-level pattern, flagged 08-27 and 08-28 for #1239) | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000297` | Hand-written review-log commits (`/check`, `/fix`, `/architect-review`, gate results) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | Being the only substantive reviewer | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Fixing the same defect on both API and web layers | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000300` | Delegate a contract test for checklist grouping/ordering (platform vs firm-owned, `sort_order`, always-null fields) so the semantics she verified by reading are | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Delegate the conversion of her review template into a repo checklist plus a PR-size-triggered required-reviewer rule. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Delegate the mock/repository-layer realignment across the remaining API modules that still bypass the repository layer. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Review quality depends on one person's availability | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000304` | Applying a cross-cutting rule surface-by-surface (URL state 08-28, read-only gates today) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000305` | Findings on his PRs closed by the reviewer | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Hand-written review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000307` | Delegate the read-only enforcement matrix tests — every mutating case/document endpoint × closed/archived/active — the only way a central policy stays central. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Delegate answering the three #1258 findings with commits before review. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000309` | Delegate the URL-state utility extraction still outstanding from 08-28. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Devin Review findings on his PRs left for the reviewer | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000311` | Cross-cutting behaviour changed surface-by-surface | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Manual `qa update` cycles on the file-number / govt-notice surfaces | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000313` | RCA written into `docs/audits` by hand | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000314` | Make the e2e matrix a required check on `dev` and delegate the first three journeys to Devin, converting his own QA cycle into a mechanism. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Delegate extraction allow-list fixtures (empty fields, display-only `doc.`, multi-questionnaire paths) — the regression class ADR-0028 describes. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Delegate closing out #1250, open since 08-27 with a finding history. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Devin-authored PR merged without independent human approval | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000318` | A branch left open across windows with an unanswered finding | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000319` | File Number behaviour changed per surface (generation 08-27, search + labels today) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000320` | Terminology/copy corrections after the feature ships | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000321` | #1239 kept alive by merges instead of landing | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Delegate the File Number test suite — generation format, uniqueness/collision (the P2002 path), organisation vs individual lookup — before the third surface is  | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000323` | Delegate the decomposition of #1239 into the reports-hub skeleton plus per-report PRs, and land the skeleton. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Delegate answering #1257's finding. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000325` | #1239 not decomposed | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000326` | Devin Review findings unanswered on his open PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000327` | `dev`→`uat`→`main` promotion PRs with template bodies | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000328` | Approving a promotion with "approved" | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000329` | Closing and re-opening a promotion PR (#1255 → #1262) | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000330` | Delegate a release-note generator that renders the promotion PR body from the `uat..main` range, including unanswered Devin Review findings in the range — this  | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000331` | Delegate a post-deploy smoke suite against the five deployed services. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Delegate the rollback-point documentation for each prod train. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000333` | Promotion approved with a content-free body (team-level, flagged 08-20 onward) | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000334` | Per-client column/header mapping fixes | AUTOMATION_OPPORTUNITY | medicodio-nextgen-integration | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000335` | `Dev_1.0`→`Uat_1.0`→prod promotion PRs on a 448-character template | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000336` | Self-merging his own fix PRs | PROCESS_PRACTICE | medicodio-nextgen-integration | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000337` | Delegate the registration header-mapping fixture suite — one case per source format, asserting the zero-import guard he hit today — the single highest-value del | PROCESS_PRACTICE | medicodio-nextgen-integration | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000338` | Delegate the payer-fallthrough regression cases (blank carrier, orphaned payer, HST claim parsing) he has now fixed by hand three windows running. | PROCESS_PRACTICE | medicodio-nextgen-integration | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000339` | Delegate promotion-body generation so the 448-character template disappears. | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000340` | Production behaviour changed with zero tests | PROCESS_PRACTICE | medicodio-nextgen-integration | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000341` | Self-merge without an independent approver | PROCESS_PRACTICE | medicodio-nextgen-integration | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000342` | Template-only promotion bodies | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000343` | Per-facility QA re-baseline after each merge or model change | MISSING_TEST | unresolved | 6 | 6 | — | CODE_CHANGE |
| `ISSUE_000344` | Closing review findings by hand, one commit per batch | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000345` | Empty-body approvals on other people's PRs | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Delegate the prompt-registry seed/drift test suite (section order per facility, empty rendered prompt, substitution boundary, cached-failure growth) — every one | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000347` | Delegate the QA re-baseline harness so a model bump costs one run, not a day. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000348` | Delegate the remaining mechanical findings on #249 so he can land it. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Approvals with no content | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000350` | A large feature branch that does not land | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000351` | Behaviour changes without automated tests | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000352` | Approving and merging `Dev_1.0`→`Uat_1.0` promotions | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000353` | Reading a large promotion diff with no summary | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000354` | Delegate a promotion summariser that posts "PRs in range / open Devin Review findings / migrations touched / rollback point" as a comment, so his approval can c | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000355` | Delegate an auto-merge-on-green rule for `Dev_1.0`→`Uat_1.0` so his attention moves to `release/prod_1.0` only. | PROCESS_PRACTICE | medicodio-nextgen-integration | 2 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000356` | Approval with no recorded content | MECHANICAL_MIGRATION | medicodio-nextgen-integration | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000357` | Environment/tagging logic corrected right after shipping it | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000358` | The same change authored twice across nodejs and react | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000359` | Manual `Dev_1.0` sync merges | MECHANICAL_MIGRATION | unresolved | 5 | 7 | — | CODE_CHANGE |
| `ISSUE_000360` | Delegate metrics tests: label cardinality, environment tag correctness per env, and the Loki flush-serialization failure path (dropped batch, backpressure) — no | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000361` | Delegate a regression suite for the encounter decrypt/patch path (recommended 08-28, still open). | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000362` | Delegate answering the #591/#592 findings. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000363` | Merging while a Devin Review report is open | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000364` | Production-path changes with no tests | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000365` | "okay" approvals on engine PRs | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000366` | Merging config changes with no fixture evidence | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000367` | Delegate the `guidelines_journey` golden-file suite (recommended 08-28, not started) — it protects the logic he rewrote on three consecutive days. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000368` | Delegate a config-change fixture runner so an ortho/BMI config PR arrives with before/after prediction evidence and the approval has something to cite. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000369` | Land or close draft #405. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000370` | Merge within seconds of a findings report | PROCESS_PRACTICE | nextgen-codio-engine | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000371` | Approvals of ≤ 5 characters | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000372` | BMI/E66-Z68 trigger data edited without a fixture | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000373` | Config/data PRs on a template body | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000374` | Delegate the E66/Z68 gate fixtures (recommended 08-28, not started) — a handful of chart fixtures pinning each trigger. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000375` | Delegate a regression test for the DXEX2 memory-recall filter he removed today, so the block cannot silently return. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000376` | Delegate the body/evidence generation for data-only config PRs. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000377` | Merge over an unanswered findings report, on a template body | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000378` | Model/RAG config toggles shipped without evidence of effect | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000379` | Template-only PR bodies on prediction-affecting changes | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000380` | Delegate the routing-trigger fixture suite (recommended 08-28, not started) — the change he ships most often is the one with no test at all. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000381` | Delegate a config-diff evidence job so a model switch arrives with measured output, not an assertion. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000382` | Delegate the answer to #412's two findings as a follow-up PR. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000383` | Merging (or promoting) while a Devin Review finding is unanswered | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000384` | Prediction-affecting config with no fixture evidence | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000385` | Work accumulating on someone else's draft branch instead of a PR of his own | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000386` | Terse commit subjects ("added more paramters…") on pipeline-affecting code | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000387` | Delegate unit tests for DXEX2 memory dedup — deduplication is exactly the kind of logic that fails silently and is trivially testable. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000388` | Delegate the split of his three commits into a reviewable PR with a body describing the recall contract. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000389` | Delegate a fixture proving DXEX1 and DXEX2 recall behave identically for the shared parameter set. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000390` | No reviewable PR of his own | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000391` | Upstream sync + lockfile refresh + release | MECHANICAL_MIGRATION | paperclip-ai | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000392` | Delegate triage of the Docker/Release failure class so a red sync does not need a person watching it. | MECHANICAL_MIGRATION | paperclip-ai | 4 | 5 | — | CODE_CHANGE |

## Scoring rationale

### `ISSUE_000002` Low automation-adoption signal for akanksh-rv

- Priority: Priority 1/10 from base 3 adjusted by: non-code process item, no software risk (-1); rating-card corroboration only, not defect evidence (-2).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.3

### `ISSUE_000049` Low automation-adoption signal for Pj-Vineeth-Kumar

- Priority: Priority 1/10 from base 3 adjusted by: non-code process item, no software risk (-1); rating-card corroboration only, not defect evidence (-2).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.3

### `ISSUE_000003` Low automation-adoption signal for Amrutha-Beedikar

- Priority: Priority 1/10 from base 3 adjusted by: non-code process item, no software risk (-1); rating-card corroboration only, not defect evidence (-2).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.3

### `ISSUE_000282` Hand-written `docs(review-logs)` evidence commits

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (25) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000283` pnpm-lock repair commits after dependency bumps

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (27) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000284` Manual `dev`-into-branch merges

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (27) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000285` Have Devin build the content-sync preflight matrix as tests (three environments × transportable/untransportable × ambiguous natural key) so the pass he ran by h

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000286` Delegate the bundle-integrity regression suite covering the signature-check-fails-open class he fixed on 08-27 and the audit-stamp gap he fixed today.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000287` Delegate the lockfile/dependency-bump chore lane entirely.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000288` Substance recorded in commits, approval left empty

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000289` A long-lived branch grows instead of landing

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000290` Repairing specs the branch's own contract changes falsified

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (43) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000291` Doc/PRD re-sync after each design correction

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000292` Hand-written review-log commits

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000293` Delegate the RBAC/authorisation matrix test suite for "case access outranks AI ownership" — the exact invariant he fixed by hand today, currently pinned by noth

- Priority: Priority 8/10 from base 3 adjusted by: category MISSING_TEST (+2); security scope AUTHORIZATION (+3).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; no file paths identified (+1); security-sensitive surface AUTHORIZATION (+2).
- Confidence: 0.5

### `ISSUE_000294` Delegate the endpoint-map and Atlas generation so docs stop needing five catch-up commits.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000295` Delegate the decomposition itself: have Devin carve #1260 into contract, API, and web PRs against the current diff.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000296` Very large single PR (team-level pattern, flagged 08-27 and 08-28 for #1239)

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000297` Hand-written review-log commits (`/check`, `/fix`, `/architect-review`, gate results)

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (25) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000298` Being the only substantive reviewer

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (29) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000299` Fixing the same defect on both API and web layers

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000300` Delegate a contract test for checklist grouping/ordering (platform vs firm-owned, `sort_order`, always-null fields) so the semantics she verified by reading are

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000301` Delegate the conversion of her review template into a repo checklist plus a PR-size-triggered required-reviewer rule.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000302` Delegate the mock/repository-layer realignment across the remaining API modules that still bypass the repository layer.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000303` Review quality depends on one person's availability

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000304` Applying a cross-cutting rule surface-by-surface (URL state 08-28, read-only gates today)

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000305` Findings on his PRs closed by the reviewer

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1256) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000306` Hand-written review-log commits

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (28) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000307` Delegate the read-only enforcement matrix tests — every mutating case/document endpoint × closed/archived/active — the only way a central policy stays central.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000308` Delegate answering the three #1258 findings with commits before review.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000309` Delegate the URL-state utility extraction still outstanding from 08-28.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000310` Devin Review findings on his PRs left for the reviewer

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000311` Cross-cutting behaviour changed surface-by-surface

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000312` Manual `qa update` cycles on the file-number / govt-notice surfaces

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (1250) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000313` RCA written into `docs/audits` by hand

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (27) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000314` Make the e2e matrix a required check on `dev` and delegate the first three journeys to Devin, converting his own QA cycle into a mechanism.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000315` Delegate extraction allow-list fixtures (empty fields, display-only `doc.`, multi-questionnaire paths) — the regression class ADR-0028 describes.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000316` Delegate closing out #1250, open since 08-27 with a finding history.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000317` Devin-authored PR merged without independent human approval

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000318` A branch left open across windows with an unanswered finding

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000319` File Number behaviour changed per surface (generation 08-27, search + labels today)

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000320` Terminology/copy corrections after the feature ships

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (26) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000321` #1239 kept alive by merges instead of landing

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (29) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000322` Delegate the File Number test suite — generation format, uniqueness/collision (the P2002 path), organisation vs individual lookup — before the third surface is 

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000323` Delegate the decomposition of #1239 into the reports-hub skeleton plus per-report PRs, and land the skeleton.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000324` Delegate answering #1257's finding.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000325` #1239 not decomposed

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000326` Devin Review findings unanswered on his open PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000327` `dev`→`uat`→`main` promotion PRs with template bodies

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (20) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000328` Approving a promotion with "approved"

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000329` Closing and re-opening a promotion PR (#1255 → #1262)

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000330` Delegate a release-note generator that renders the promotion PR body from the `uat..main` range, including unanswered Devin Review findings in the range — this 

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000331` Delegate a post-deploy smoke suite against the five deployed services.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000332` Delegate the rollback-point documentation for each prod train.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000333` Promotion approved with a content-free body (team-level, flagged 08-20 onward)

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000334` Per-client column/header mapping fixes

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000335` `Dev_1.0`→`Uat_1.0`→prod promotion PRs on a 448-character template

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (20) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000336` Self-merging his own fix PRs

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (266) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000337` Delegate the registration header-mapping fixture suite — one case per source format, asserting the zero-import guard he hit today — the single highest-value del

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000338` Delegate the payer-fallthrough regression cases (blank carrier, orphaned payer, HST claim parsing) he has now fixed by hand three windows running.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000339` Delegate promotion-body generation so the 448-character template disappears.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000340` Production behaviour changed with zero tests

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000341` Self-merge without an independent approver

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000342` Template-only promotion bodies

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000343` Per-facility QA re-baseline after each merge or model change

- Priority: Priority 6/10 from base 3 adjusted by: category MISSING_TEST (+2); high reported frequency (27) (+1).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000344` Closing review findings by hand, one commit per batch

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (15) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000345` Empty-body approvals on other people's PRs

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (28) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000346` Delegate the prompt-registry seed/drift test suite (section order per facility, empty rendered prompt, substitution boundary, cached-failure growth) — every one

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000347` Delegate the QA re-baseline harness so a model bump costs one run, not a day.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000348` Delegate the remaining mechanical findings on #249 so he can land it.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000349` Approvals with no content

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000350` A large feature branch that does not land

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000351` Behaviour changes without automated tests

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000352` Approving and merging `Dev_1.0`→`Uat_1.0` promotions

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (28) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000353` Reading a large promotion diff with no summary

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000354` Delegate a promotion summariser that posts "PRs in range / open Devin Review findings / migrations touched / rollback point" as a comment, so his approval can c

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000355` Delegate an auto-merge-on-green rule for `Dev_1.0`→`Uat_1.0` so his attention moves to `release/prod_1.0` only.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.6

### `ISSUE_000356` Approval with no recorded content

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000357` Environment/tagging logic corrected right after shipping it

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (592) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000358` The same change authored twice across nodejs and react

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (28) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000359` Manual `Dev_1.0` sync merges

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (28) (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000360` Delegate metrics tests: label cardinality, environment tag correctness per env, and the Loki flush-serialization failure path (dropped batch, backpressure) — no

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000361` Delegate a regression suite for the encounter decrypt/patch path (recommended 08-28, still open).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000362` Delegate answering the #591/#592 findings.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000363` Merging while a Devin Review report is open

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000364` Production-path changes with no tests

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000365` "okay" approvals on engine PRs

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (28) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000366` Merging config changes with no fixture evidence

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (413) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000367` Delegate the `guidelines_journey` golden-file suite (recommended 08-28, not started) — it protects the logic he rewrote on three consecutive days.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000368` Delegate a config-change fixture runner so an ortho/BMI config PR arrives with before/after prediction evidence and the approval has something to cite.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000369` Land or close draft #405.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000370` Merge within seconds of a findings report

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000371` Approvals of ≤ 5 characters

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000372` BMI/E66-Z68 trigger data edited without a fixture

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (413) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000373` Config/data PRs on a template body

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (401) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000374` Delegate the E66/Z68 gate fixtures (recommended 08-28, not started) — a handful of chart fixtures pinning each trigger.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000375` Delegate a regression test for the DXEX2 memory-recall filter he removed today, so the block cannot silently return.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000376` Delegate the body/evidence generation for data-only config PRs.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000377` Merge over an unanswered findings report, on a template body

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000378` Model/RAG config toggles shipped without evidence of effect

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (28) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000379` Template-only PR bodies on prediction-affecting changes

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000380` Delegate the routing-trigger fixture suite (recommended 08-28, not started) — the change he ships most often is the one with no test at all.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000381` Delegate a config-diff evidence job so a model switch arrives with measured output, not an assertion.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000382` Delegate the answer to #412's two findings as a follow-up PR.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000383` Merging (or promoting) while a Devin Review finding is unanswered

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000384` Prediction-affecting config with no fixture evidence

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000385` Work accumulating on someone else's draft branch instead of a PR of his own

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (25) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000386` Terse commit subjects ("added more paramters…") on pipeline-affecting code

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000387` Delegate unit tests for DXEX2 memory dedup — deduplication is exactly the kind of logic that fails silently and is trivially testable.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000388` Delegate the split of his three commits into a reviewable PR with a body describing the recall contract.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000389` Delegate a fixture proving DXEX1 and DXEX2 recall behave identically for the shared parameter set.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000390` No reviewable PR of his own

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000391` Upstream sync + lockfile refresh + release

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000392` Delegate triage of the Docker/Release failure class so a red sync does not need a person watching it.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

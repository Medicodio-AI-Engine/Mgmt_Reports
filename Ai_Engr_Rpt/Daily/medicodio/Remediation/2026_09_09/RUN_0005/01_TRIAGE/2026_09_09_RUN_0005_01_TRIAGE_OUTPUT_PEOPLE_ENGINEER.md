# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-09 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Dev→UAT / UAT→prod promotion PRs with badge-only bodies | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000283` | CI-probe no-op PR to exercise the unit-test stage | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Same-morning "address Devin review" follow-up commits | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Use Devin to write regression tests for `resolveFacilityFeature` covering scope guards, inactive facilities and union rows — the exact classes Devin Review foun | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000286` | Replace `#549`-style probe PRs with a `workflow_dispatch` trigger (small, bounded, Good Devin Candidate). | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Ask Devin for a one-paragraph open-findings digest on each promotion PR before approving. | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000288` | Empty approvals on prod-path PRs | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | CI-probe PRs | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Prod promotions with badge-only body | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000291` | Manual verification of add-on state edge cases | MISSING_TEST | unresolved | 6 | 6 | — | CODE_CHANGE |
| `ISSUE_000292` | Delegate unit tests for the prolonged add-on state (orphan, unit drift, reopen) to Devin — the three bugs it found today are the test cases. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000293` | Coder-performance dedupe golden fixtures (scope filter on/off). | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Empty approvals on prod promotions | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000295` | Port a prompt clause between Dev/UAT/prod by hand (`#295`, `#296`) | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Two prod promotions per day | MECHANICAL_MIGRATION | unresolved | 5 | 7 | — | CODE_CHANGE |
| `ISSUE_000297` | Generate regression fixtures for every prompt rule fixed this week (bare-X, laterality, option-grid, hospitalization heading) — each fix added one test by hand. | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000298` | A Devin task to reconcile the M0xx error-code registry and add a uniqueness test (today's collision was found by Devin Review, not tests). | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Prod promotion with unanswered Devin findings | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000300` | Selector / dialog timing fixes discovered by running the robot | MISSING_TEST | unresolved | 6 | 6 | — | CODE_CHANGE |
| `ISSUE_000301` | Self-merge of feature branch to `main` | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000302` | Install Devin Review on `medicodio-nextgen-rf-rpa-automation` and open PRs with bodies — bounded, immediate. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Unit tests for `libraries/.py` (coding-note formatter, filtered-vs-failed counters) — pure Python, Good Devin Candidate. | MISSING_TEST | unresolved | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000304` | Add `robocop`/dry-run lint as a GitHub Action. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Empty approvals on integration prod path | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000306` | Self-merge, no review (new) | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000307` | One-word approvals ("okay") | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000308` | Manual `client_configs` list edits that silently regress (`04d7512c`) | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000309` | Config-bundle invariant tests (every specialty declares the required keys) — would have caught the vital_gastro regression before Devin Review did. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Ask Devin for an open-findings digest before merging others' PRs. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000311` | One-word approvals | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Ordering/routing logic verified by reading, not golden tests | MISSING_TEST | unresolved | 6 | 6 | — | CODE_CHANGE |
| `ISSUE_000313` | Golden tests for `build_chart_text_from_row` ordering across specialty ∪ client field lists. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000314` | Golden tests for routing/assembly absent | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000129` | — | PROCESS_PRACTICE | unresolved | 3 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Sweep the remaining `sys.path.insert` / raw-string comparison seams across legacy guidelines — the same class of defect, bounded. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000316` | Re-opening the same sequencing work as new PRs (`#382` 08-21, `#415` 09-01 by avinash, `#434`/`#435` today) | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000317` | Ask Devin to answer the 13 findings with reasoned dispositions, then write sequencing golden tests (2nd recommendation). | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000318` | Unanswered Devin findings | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000319` | One-word approvals on PRs with open findings | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000320` | Open a draft PR for `feat/checkpoint` so Devin Review inspects a 3,000-line change. | PROCESS_PRACTICE | unresolved | 2 | 7 | — | NON_CODE_PROCESS |
| `ISSUE_000321` | Checkpoint round-trip tests (write → resume → identical output). | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000322` | Approves / merges with open findings | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000323` | Template/badge-only bodies | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000324` | Gate-by-gate fixes discovered by running charts | AUTOMATION_OPPORTUNITY | unresolved | 5 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000325` | Open a draft PR so Devin Review runs on ≈ 20 commits of engine gate logic (3rd recommendation). | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000326` | Fixture generation for the principal-drop regression. | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000327` | Long-running branch without PR | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000328` | Large schema/field moves across 65 files by hand | AUTOMATION_OPPORTUNITY | unresolved | 4 | 7 | — | TOOLING_AUTOMATION |
| `ISSUE_000329` | Contract tests for `asserted_at` / `author_role` stamping. | MISSING_TEST | unresolved | 5 | 6 | — | CODE_CHANGE |
| `ISSUE_000330` | Work on shared branch without PR | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000331` | Finishing other people's large PRs to get them merged | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000332` | Green-gate matrix documented by hand in `docs/review` | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 3 | — | TOOLING_AUTOMATION |
| `ISSUE_000333` | Route the 4 "needs decision" threads on `#1284` to a Devin follow-up PR with the decisions as acceptance criteria (as `#1321` did for `#1320`). | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000334` | Have Devin generate the gate-matrix summary from CI artefacts instead of hand-written review logs. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000335` | Large PR finished and merged by the reviewer | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000336` | Hand-written `docs(review-logs)` and atlas regeneration | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000337` | 40-commit single-day PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000338` | Disposition the 5 `#1336` findings via Devin with reasons before requesting review. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000339` | Split `#1336` with Devin's help into db-migration / api / web PRs. | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000340` | Very large PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000341` | `/check` audit logs written by hand into `docs/review` | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 3 | — | TOOLING_AUTOMATION |
| `ISSUE_000342` | Fixes for QA findings landing on a branch that also carries unrelated scope ("three independent fixes landed on one branch at the user's direction") | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000343` | Delegate the 21 open findings to Devin with reasons (accept/reject) — bounded, high value. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000344` | One regression test per QA finding in `#1334` (2 findings → verify 2 tests). | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000345` | >50-file PRs open concurrently | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000346` | Devin findings unanswered | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000347` | Large UI feature commits (60–99 files) on a personal branch without PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000348` | Open `feat/mobbin-trails` as a PR and let Devin Review run on +6,700 lines. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000349` | Repeat the `#1333` pattern (PRD → decisions → implement) for the appearance-preferences feature. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000350` | Work without PR (`feat/mobbin-trails`) | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000351` | Ownership-guard exemptions added case by case | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000352` | Regression tests for the ownership guard (guidance-only vs rule writes). | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000353` | Draft PR for the branch. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000354` | — (branch without PR is new for her) | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000355` | Re-syncing long-lived feature branch with `dev` | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000356` | Regression test for the remediation-card case (from 09-08). | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000357` | — | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |

## Scoring rationale

### `ISSUE_000282` Dev→UAT / UAT→prod promotion PRs with badge-only bodies

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000283` CI-probe no-op PR to exercise the unit-test stage

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (549) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000284` Same-morning "address Devin review" follow-up commits

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000285` Use Devin to write regression tests for `resolveFacilityFeature` covering scope guards, inactive facilities and union rows — the exact classes Devin Review foun

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000286` Replace `#549`-style probe PRs with a `workflow_dispatch` trigger (small, bounded, Good Devin Candidate).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000287` Ask Devin for a one-paragraph open-findings digest on each promotion PR before approving.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000288` Empty approvals on prod-path PRs

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000289` CI-probe PRs

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000290` Prod promotions with badge-only body

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000291` Manual verification of add-on state edge cases

- Priority: Priority 6/10 from base 3 adjusted by: category MISSING_TEST (+2); high reported frequency (555) (+1).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000292` Delegate unit tests for the prolonged add-on state (orphan, unit drift, reopen) to Devin — the three bugs it found today are the test cases.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000293` Coder-performance dedupe golden fixtures (scope filter on/off).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000294` Empty approvals on prod promotions

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000295` Port a prompt clause between Dev/UAT/prod by hand (`#295`, `#296`)

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000296` Two prod promotions per day

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (300) (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000297` Generate regression fixtures for every prompt rule fixed this week (bare-X, laterality, option-grid, hospitalization heading) — each fix added one test by hand.

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000298` A Devin task to reconcile the M0xx error-code registry and add a uniqueness test (today's collision was found by Devin Review, not tests).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000299` Prod promotion with unanswered Devin findings

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000300` Selector / dialog timing fixes discovered by running the robot

- Priority: Priority 6/10 from base 3 adjusted by: category MISSING_TEST (+2); high reported frequency (13) (+1).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000301` Self-merge of feature branch to `main`

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (18) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000302` Install Devin Review on `medicodio-nextgen-rf-rpa-automation` and open PRs with bodies — bounded, immediate.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000303` Unit tests for `libraries/.py` (coding-note formatter, filtered-vs-failed counters) — pure Python, Good Devin Candidate.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 5/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2).
- Confidence: 0.6

### `ISSUE_000304` Add `robocop`/dry-run lint as a GitHub Action.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000305` Empty approvals on integration prod path

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000306` Self-merge, no review (new)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000307` One-word approvals ("okay")

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (19) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000308` Manual `client_configs` list edits that silently regress (`04d7512c`)

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (7716) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000309` Config-bundle invariant tests (every specialty declares the required keys) — would have caught the vital_gastro regression before Devin Review did.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000310` Ask Devin for an open-findings digest before merging others' PRs.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000311` One-word approvals

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000312` Ordering/routing logic verified by reading, not golden tests

- Priority: Priority 6/10 from base 3 adjusted by: category MISSING_TEST (+2); high reported frequency (436) (+1).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000313` Golden tests for `build_chart_text_from_row` ordering across specialty ∪ client field lists.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000314` Golden tests for routing/assembly absent

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000129` —

- Priority: Priority 3/10 from base 3 adjusted by: reported twice across sources (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000315` Sweep the remaining `sys.path.insert` / raw-string comparison seams across legacy guidelines — the same class of defect, bounded.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000316` Re-opening the same sequencing work as new PRs (`#382` 08-21, `#415` 09-01 by avinash, `#434`/`#435` today)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000317` Ask Devin to answer the 13 findings with reasoned dispositions, then write sequencing golden tests (2nd recommendation).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000318` Unanswered Devin findings

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000319` One-word approvals on PRs with open findings

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000320` Open a draft PR for `feat/checkpoint` so Devin Review inspects a 3,000-line change.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 7/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2).
- Confidence: 0.6

### `ISSUE_000321` Checkpoint round-trip tests (write → resume → identical output).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000322` Approves / merges with open findings

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000323` Template/badge-only bodies

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000324` Gate-by-gate fixes discovered by running charts

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (12) (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000325` Open a draft PR so Devin Review runs on ≈ 20 commits of engine gate logic (3rd recommendation).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000326` Fixture generation for the principal-drop regression.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000327` Long-running branch without PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000328` Large schema/field moves across 65 files by hand

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 7/10 from: category AUTOMATION_OPPORTUNITY base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000329` Contract tests for `asserted_at` / `author_role` stamping.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 6/10 from: category MISSING_TEST base 3; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000330` Work on shared branch without PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000331` Finishing other people's large PRs to get them merged

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1314) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000332` Green-gate matrix documented by hand in `docs/review`

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 3/10 from: category AUTOMATION_OPPORTUNITY base 4; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000333` Route the 4 "needs decision" threads on `#1284` to a Devin follow-up PR with the decisions as acceptance criteria (as `#1321` did for `#1320`).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000334` Have Devin generate the gate-matrix summary from CI artefacts instead of hand-written review logs.

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000335` Large PR finished and merged by the reviewer

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000336` Hand-written `docs(review-logs)` and atlas regeneration

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000337` 40-commit single-day PRs

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (1336) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000338` Disposition the 5 `#1336` findings via Devin with reasons before requesting review.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000339` Split `#1336` with Devin's help into db-migration / api / web PRs.

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000340` Very large PRs

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000341` `/check` audit logs written by hand into `docs/review`

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 3/10 from: category AUTOMATION_OPPORTUNITY base 4; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000342` Fixes for QA findings landing on a branch that also carries unrelated scope ("three independent fixes landed on one branch at the user's direction")

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1334) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000343` Delegate the 21 open findings to Devin with reasons (accept/reject) — bounded, high value.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000344` One regression test per QA finding in `#1334` (2 findings → verify 2 tests).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000345` >50-file PRs open concurrently

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000346` Devin findings unanswered

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000347` Large UI feature commits (60–99 files) on a personal branch without PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000348` Open `feat/mobbin-trails` as a PR and let Devin Review run on +6,700 lines.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.6

### `ISSUE_000349` Repeat the `#1333` pattern (PRD → decisions → implement) for the appearance-preferences feature.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000350` Work without PR (`feat/mobbin-trails`)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000351` Ownership-guard exemptions added case by case

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000352` Regression tests for the ownership guard (guidance-only vs rule writes).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000353` Draft PR for the branch.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000354` — (branch without PR is new for her)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000355` Re-syncing long-lived feature branch with `dev`

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000356` Regression test for the remediation-card case (from 09-08).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000357` —

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

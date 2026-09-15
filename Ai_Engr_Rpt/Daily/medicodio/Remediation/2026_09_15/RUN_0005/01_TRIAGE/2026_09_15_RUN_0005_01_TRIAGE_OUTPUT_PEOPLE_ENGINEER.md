# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-15 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-written `docs(review-logs)` commits (standards audit, architect review, PR review, gate results) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | "regenerate atlas (module_map, screen_index)" commit | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Remediating a peer's PR before approving it | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000285` | Use Devin to write the non-mocked integration suite for the email-triage recovery legs (`StuckEmailTriageRecovery` 4 legs, BullMQ jobId dedupe) — the 09-13/09-1 | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Delegate the two open `email_triage_readings` index decisions on `#1367` as a measured task: Devin runs `EXPLAIN` on `findTriagePage` `all`/`needs-you` buckets  | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Pre-merge QA on `#1373`: trigger the Devin QA gate on the branch before approval so the NOT READY pattern (4 in a row) does not repeat on a 95-file PR. Good Dev | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Reviewer remediates, then approves, then merges the same PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Merge with own "needs your decision" items open | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Post-merge Devin QA NOT READY | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Hand-written review-log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Atlas regeneration / function-header sync / debt-ledger sync commits | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000293` | `/review-all` ledger written into `docs/review-logs/` by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 3 | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Review-pass commits on a peer's branch | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Use Devin to implement the Entity Status Phase 1 PRD as a spike PR against `dev` with the PRD's acceptance criteria as the prompt — the PRD is written, the surf | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Use Devin to convert the 7 NEEDS-DECISION items on `#1373` into issues with options and evidence, so the decision owner (Saijyoti) can answer in writing before  | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Devin QA gate pre-merge on `#1373` (shared with Saijyoti). | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000298` | Review-pass as 20+ direct commits on a peer's PR instead of a review | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Work on a branch without a PR | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Sync/regeneration chores as human commits | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000301` | Hand-fixing Devin PRs after Devin Review findings | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000302` | Ask Devin to add a regression test for the orphan-checklist audit count on `#1360` and answer the `scripts/` approval-gate finding — Good Devin Candidate. | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000303` | Get `#1360` and `#1364` merged by requesting a named reviewer; both are small and green. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000304` | Small PRs left open without requesting review | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000305` | Large PR opened without a named reviewer | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000306` | Have Devin produce the reviewer's map of `#1363` (per-area summary, risk list, test evidence) so a peer can review 110 files in bounded time — Good Devin Candid | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000307` | Devin QA gate on `#1363` before merge — the PR touches performance/security paths. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000308` | >60-file PR without reviewer | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000309` | Branch with large checkpoint, no PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000310` | Open `feat/hr-portal-revamp` as a draft PR and let Devin Review run — the branch has been invisible to review for 5 reports. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000311` | `feat/hr-portal-revamp` no PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000312` | Placeholder `Co-Authored-By` Devin e-mails | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000313` | Findings/promotions carried without disposition | MECHANICAL_MIGRATION | unresolved | 4 | 7 | — | CODE_CHANGE |
| `ISSUE_000314` | `feat/inpatient-engine` no PR | PROCESS_PRACTICE | unresolved | 2 | 7 | — | NON_CODE_PROCESS |
| `ISSUE_000315` | Reviews ≤10 chars on production-bound PRs | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |

## Scoring rationale

### `ISSUE_000282` Hand-written `docs(review-logs)` commits (standards audit, architect review, PR review, gate results)

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (21) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000283` "regenerate atlas (module_map, screen_index)" commit

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000284` Remediating a peer's PR before approving it

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1367) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000285` Use Devin to write the non-mocked integration suite for the email-triage recovery legs (`StuckEmailTriageRecovery` 4 legs, BullMQ jobId dedupe) — the 09-13/09-1

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000286` Delegate the two open `email_triage_readings` index decisions on `#1367` as a measured task: Devin runs `EXPLAIN` on `findTriagePage` `all`/`needs-you` buckets 

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000287` Pre-merge QA on `#1373`: trigger the Devin QA gate on the branch before approval so the NOT READY pattern (4 in a row) does not repeat on a 95-file PR. Good Dev

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000288` Reviewer remediates, then approves, then merges the same PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000289` Merge with own "needs your decision" items open

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000290` Post-merge Devin QA NOT READY

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000291` Hand-written review-log commits

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000292` Atlas regeneration / function-header sync / debt-ledger sync commits

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (13) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000293` `/review-all` ledger written into `docs/review-logs/` by hand

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (21) (+1).
- Complexity: Complexity 3/10 from: category AUTOMATION_OPPORTUNITY base 4; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000294` Review-pass commits on a peer's branch

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1373) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000295` Use Devin to implement the Entity Status Phase 1 PRD as a spike PR against `dev` with the PRD's acceptance criteria as the prompt — the PRD is written, the surf

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000296` Use Devin to convert the 7 NEEDS-DECISION items on `#1373` into issues with options and evidence, so the decision owner (Saijyoti) can answer in writing before 

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000297` Devin QA gate pre-merge on `#1373` (shared with Saijyoti).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000298` Review-pass as 20+ direct commits on a peer's PR instead of a review

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000299` Work on a branch without a PR

- Priority: Priority 3/10 from base 3 adjusted by: reported twice across sources (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.8

### `ISSUE_000300` Sync/regeneration chores as human commits

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000301` Hand-fixing Devin PRs after Devin Review findings

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (1360) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000302` Ask Devin to add a regression test for the orphan-checklist audit count on `#1360` and answer the `scripts/` approval-gate finding — Good Devin Candidate.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000303` Get `#1360` and `#1364` merged by requesting a named reviewer; both are small and green.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000304` Small PRs left open without requesting review

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000305` Large PR opened without a named reviewer

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (1363) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000306` Have Devin produce the reviewer's map of `#1363` (per-area summary, risk list, test evidence) so a peer can review 110 files in bounded time — Good Devin Candid

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000307` Devin QA gate on `#1363` before merge — the PR touches performance/security paths.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000308` >60-file PR without reviewer

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000309` Branch with large checkpoint, no PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000310` Open `feat/hr-portal-revamp` as a draft PR and let Devin Review run — the branch has been invisible to review for 5 reports.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.6

### `ISSUE_000311` `feat/hr-portal-revamp` no PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000312` Placeholder `Co-Authored-By` Devin e-mails

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000313` Findings/promotions carried without disposition

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 7/10 from: category MECHANICAL_MIGRATION base 4; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000314` `feat/inpatient-engine` no PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 7/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2).
- Confidence: 0.65

### `ISSUE_000315` Reviews ≤10 chars on production-bound PRs

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.55

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

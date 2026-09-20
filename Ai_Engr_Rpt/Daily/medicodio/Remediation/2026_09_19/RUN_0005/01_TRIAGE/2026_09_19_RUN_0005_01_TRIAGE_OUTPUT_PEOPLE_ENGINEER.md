# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-19 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_19_Employee_Rating_Cards.md, 2026_09_19_Mgmt_Activity_Report.md; dated by filename only, no stated review date

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Review-log / standards-log / atlas refresh commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000283` | "Repair what the pre-push gate surfaced" (type errors, imports, JSX) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Function-header relocation/restoration | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Reviewer pushes 20–44 fix commits to a peer's PR then merges it | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Hand Devin the 11 "Remaining items — author/user decision" from her own log as bounded PRs (R16 enforcement on two CREATE paths; single owner for the three regi | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Devin-generated review-log/atlas commit from gate output, replacing 7 hand commits per PR. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000288` | Run the Devin QA gate against the PR's preview before approval; paste the verdict into the approval body. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Reviewer remediates, then approves and merges (no independent approver) | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Merge with own open pre-merge list | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000291` | QA verdict consumed after merge | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Header relocation / review-log commits by hand | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Gate-surfaced repair commits after push | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Oversized single PR (>200 files) | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000295` | Devin drafts the §12.4/§12.5 measurement PR (read-only queries, p50/p95 harness) — well-defined, bounded. | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000296` | Devin opens one PR per "major" (#5–#11 in the review) with the acceptance test stated in the log. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Devin regression tests for the demotion-rejection and inheritance/PII-exclusion paths the QA gate could not exercise (7f items). | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000298` | Oversized single PR | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000299` | Author's own findings dispositioned by reviewer | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |

## Scoring rationale

### `ISSUE_000282` Review-log / standards-log / atlas refresh commits

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (17) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000283` "Repair what the pre-push gate surfaced" (type errors, imports, JSX)

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (1390) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000284` Function-header relocation/restoration

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (25) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000285` Reviewer pushes 20–44 fix commits to a peer's PR then merges it

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1391) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000286` Hand Devin the 11 "Remaining items — author/user decision" from her own log as bounded PRs (R16 enforcement on two CREATE paths; single owner for the three regi

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000287` Devin-generated review-log/atlas commit from gate output, replacing 7 hand commits per PR.

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000288` Run the Devin QA gate against the PR's preview before approval; paste the verdict into the approval body.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000289` Reviewer remediates, then approves and merges (no independent approver)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000290` Merge with own open pre-merge list

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000291` QA verdict consumed after merge

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000292` Header relocation / review-log commits by hand

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000293` Gate-surfaced repair commits after push

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (17) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000294` Oversized single PR (>200 files)

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (1391) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000295` Devin drafts the §12.4/§12.5 measurement PR (read-only queries, p50/p95 harness) — well-defined, bounded.

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000296` Devin opens one PR per "major" (#5–#11 in the review) with the acceptance test stated in the log.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000297` Devin regression tests for the demotion-rejection and inheritance/PII-exclusion paths the QA gate could not exercise (7f items).

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000298` Oversized single PR

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000299` Author's own findings dispositioned by reviewer

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

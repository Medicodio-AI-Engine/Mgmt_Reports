# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-13 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Hand-fixing another member's findings, then approving and merging | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000283` | `docs(review-logs)` commits written by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Re-running the 37-gate matrix and transcribing results into prose | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`,  | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000286` | Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is ne | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Reviewer remediates, approves, then merges | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Merged over the approver's own written blocker | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Post-merge QA-gate verdict unactioned in-window | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Ad-hoc per-component timestamp formatting | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000292` | Branch carried without a PR | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC se | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000294` | Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real). | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work. | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 3 | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Work carried on a branch with no PR | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Large single PR (73 files) awaiting a human reviewer | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000298` | Author absent while another member remediates and merges his PR | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000299` | Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migra | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Decision items on his PRs resolved without him | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000302` | PR-description accuracy | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |

## Scoring rationale

### `ISSUE_000282` Hand-fixing another member's findings, then approving and merging

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (11) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000283` `docs(review-logs)` commits written by hand

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (11) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000284` Re-running the 37-gate matrix and transcribing results into prose

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000285` Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`, 

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000286` Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is ne

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000287` Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000288` Reviewer remediates, approves, then merges

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000289` Merged over the approver's own written blocker

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000290` Post-merge QA-gate verdict unactioned in-window

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000291` Ad-hoc per-component timestamp formatting

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (45) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000292` Branch carried without a PR

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (16) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000293` Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC se

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000294` Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real).

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000295` Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work.

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 3/10 from: category AUTOMATION_OPPORTUNITY base 4; repository and paths both known (-1).
- Confidence: 0.6

### `ISSUE_000296` Work carried on a branch with no PR

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000297` Large single PR (73 files) awaiting a human reviewer

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000298` Author absent while another member remediates and merges his PR

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1366) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000299` Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000300` Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migra

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000301` Decision items on his PRs resolved without him

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000302` PR-description accuracy

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-06 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Fixing another author's PR to merge-readiness, then approving it | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000283` | Backfilling "mandatory function headers" and `docs(headers)` commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Repairing specs broken by fix commits (`realign five specs`, `repair three specs the gate run surfaced`) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000285` | `docs(review-logs): record …` commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000286` | Merging `dev` into a 100+-file feature branch and repairing the merge | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Good Devin Candidate — "Convert the 20-blocker list from the `#1305` review into an automated DVR pre-review checklist (tenancy predicate on every firm-scoped q | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000288` | Good Devin Candidate — "Write a regression test that fails when a `dev` merge into a feature branch reduces the `onRowClick`/fix count on files touched by both  | MISSING_TEST | globalcodio-monorepo | 5 | 4 | — | CODE_CHANGE |
| `ISSUE_000289` | Possible Devin Candidate — "Propose a ≤ 60-file split plan for the next letter-groups/support-letter feature along the shared-types → db → api → web seam" — hum | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000290` | > 100-file feature PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000291` | Remediate-then-approve (non-independent review) | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Approve with own open blockers/decisions | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000293` | Repairing test mocks/fixtures after interface changes (`repair stale test mocks`, `repair 3 pre-existing test-fixture bugs`, `repair gate-failing test/registry drift`) | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000294` | Fixing the blocker in a PR she is reviewing | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Standards-audit log commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000296` | Good Devin Candidate — "Re-run the 39/42 quality gates on the `#1305`/`#1318` merge commits and post the raw table to the PR; open issues for any gate that is n | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so t | PROCESS_PRACTICE | globalcodio-monorepo | 5 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000298` | Possible Devin Candidate — "Implement the four open decisions on `#1305` (owned-rule guidance columns, canonical tier precedence, N+1 in the interactive tx, `Do | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000299` | 100+-file PRs | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000300` | Reviewer fixes the blocker, then approves | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000301` | PR-body claims not matching verification | SECURITY_TENANCY | globalcodio-monorepo | 10 | 10 | — | CODE_CHANGE |

## Scoring rationale

### `ISSUE_000282` Fixing another author's PR to merge-readiness, then approving it

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1318) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000283` Backfilling "mandatory function headers" and `docs(headers)` commits

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000284` Repairing specs broken by fix commits (`realign five specs`, `repair three specs the gate run surfaced`)

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000285` `docs(review-logs): record …` commits

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000286` Merging `dev` into a 100+-file feature branch and repairing the merge

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (816270755) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000287` Good Devin Candidate — "Convert the 20-blocker list from the `#1305` review into an automated DVR pre-review checklist (tenancy predicate on every firm-scoped q

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000288` Good Devin Candidate — "Write a regression test that fails when a `dev` merge into a feature branch reduces the `onRowClick`/fix count on files touched by both 

- Priority: Priority 5/10 from base 3 adjusted by: category MISSING_TEST (+2).
- Complexity: Complexity 4/10 from: category MISSING_TEST base 3; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000289` Possible Devin Candidate — "Propose a ≤ 60-file split plan for the next letter-groups/support-letter feature along the shared-types → db → api → web seam" — hum

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000290` > 100-file feature PRs

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000291` Remediate-then-approve (non-independent review)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000292` Approve with own open blockers/decisions

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000293` Repairing test mocks/fixtures after interface changes (`repair stale test mocks`, `repair 3 pre-existing test-fixture bugs`, `repair gate-failing test/registry drift`)

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000294` Fixing the blocker in a PR she is reviewing

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1317) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000295` Standards-audit log commits

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000296` Good Devin Candidate — "Re-run the 39/42 quality gates on the `#1305`/`#1318` merge commits and post the raw table to the PR; open issues for any gate that is n

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000297` Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so t

- Priority: Priority 5/10 from base 3 adjusted by: security scope BILLING (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1); security-sensitive surface BILLING (+2).
- Confidence: 0.6

### `ISSUE_000298` Possible Devin Candidate — "Implement the four open decisions on `#1305` (owned-rule guidance columns, canonical tier precedence, N+1 in the interactive tx, `Do

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000299` 100+-file PRs

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000300` Reviewer fixes the blocker, then approves

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000301` PR-body claims not matching verification

- Priority: Priority 10/10 from base 3 adjusted by: category SECURITY_TENANCY (+4); security scope TENANT_ISOLATION (+4).
- Complexity: Complexity 10/10 from: category SECURITY_TENANCY base 9; no file paths identified (+1); security-sensitive surface TENANT_ISOLATION (+2).
- Confidence: 0.65

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

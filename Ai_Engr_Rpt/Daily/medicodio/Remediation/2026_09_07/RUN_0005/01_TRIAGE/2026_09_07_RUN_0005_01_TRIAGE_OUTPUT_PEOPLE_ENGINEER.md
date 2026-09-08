# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-07 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge) | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000283` | Recording review passes as `docs(review-logs)` commits | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift) | MECHANICAL_MIGRATION | globalcodio-monorepo | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000285` | Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind) | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number f | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inher | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000288` | Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the co | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Approves and merges a branch he remediated | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Own "needs decision" items left open at merge | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000291` | `#1278` `importSession` SEV-High finding without fix or waiver | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Large unreviewed branches | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 3 | — | CODE_CHANGE |
| `ISSUE_000293` | Insufficient data — one commit in the week | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000294` | Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000296` | Devin findings on own PR unanswered | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Open PR not progressed by its author | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |

## Scoring rationale

### `ISSUE_000282` Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge)

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (1304) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000283` Recording review passes as `docs(review-logs)` commits

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (76306) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000284` Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift)

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (183664306) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000285` Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000286` Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number f

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000287` Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inher

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000288` Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the co

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000289` Approves and merges a branch he remediated

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000290` Own "needs decision" items left open at merge

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000291` `#1278` `importSession` SEV-High finding without fix or waiver

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000292` Large unreviewed branches

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 3/10 from: category MECHANICAL_MIGRATION base 4; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000293` Insufficient data — one commit in the week

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000294` Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000295` Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000296` Devin findings on own PR unanswered

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000297` Open PR not progressed by its author

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-21 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_21_Employee_Rating_Cards.md, 2026_09_21_Mgmt_Activity_Report.md; dated by filename only, no stated review date

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Workflow/infra change merged without a dry run of its own verification path | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 4 | — | NON_CODE_PROCESS |
| `ISSUE_000283` | Findings left undispositioned on open PRs | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 5 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000284` | Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable a | PROCESS_PRACTICE | globalcodio-monorepo | 5 | 8 | — | NON_CODE_PROCESS |
| `ISSUE_000285` | (Carried) Devin triage of the 15 `#1394` findings into fix / accept / out-of-scope drafts. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000286` | Findings undispositioned | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000287` | Infra change lands without exercising its own verification path | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000288` | 0-char approvals followed by immediate merge | PROCESS_PRACTICE | globalcodio-monorepo | 3 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000289` | Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off a | PROCESS_PRACTICE | globalcodio-monorepo | 5 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000290` | Empty approvals | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000291` | Branch protection not enabled (as EM) | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000292` | Carried: review-log / atlas / header-relocation commits by hand | AUTOMATION_OPPORTUNITY | globalcodio-monorepo | 4 | 5 | — | TOOLING_AUTOMATION |
| `ISSUE_000293` | (Carried) 11 NEEDS-DECISION items from `#1391` as bounded Devin PRs with her written acceptance tests. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000294` | (Carried) Run the QA gate on the PR head before approval. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000295` | Reviewer remediates, approves, merges | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000296` | QA verdict consumed after merge | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000297` | Carried: oversized single PR (`#1310`, `#1322`, `#1391`) | MECHANICAL_MIGRATION | globalcodio-monorepo | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000298` | (Carried) Devin drafts §12.4/§12.5 measurement PR. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000299` | (Carried) One Devin PR per major #5–#11. | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000300` | Author's findings dispositioned by the reviewer | PROCESS_PRACTICE | globalcodio-monorepo | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000301` | Manual upstream fork sync (`paperclip-ai`) | MECHANICAL_MIGRATION | paperclip-ai | 5 | 5 | — | CODE_CHANGE |
| `ISSUE_000302` | (Carried) Fit assessment of `paperclip-ai` against the existing Devin/Claude workflow instead of a hand-maintained fork. | PROCESS_PRACTICE | paperclip-ai | 2 | 6 | — | NON_CODE_PROCESS |
| `ISSUE_000303` | Large invoicing PRs with badge-only bodies (`#652`/`#578`) | PROCESS_PRACTICE | unresolved | 2 | 8 | — | NON_CODE_PROCESS |

## Scoring rationale

### `ISSUE_000282` Workflow/infra change merged without a dry run of its own verification path

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (1384) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 4/10 from: category PROCESS_PRACTICE base 5; repository and paths both known (-1).
- Confidence: 0.75

### `ISSUE_000283` Findings left undispositioned on open PRs

- Priority: Priority 5/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1); high reported frequency (1394) (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000284` Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable a

- Priority: Priority 5/10 from base 3 adjusted by: security scope SECRETS (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1); security-sensitive surface SECRETS (+2).
- Confidence: 0.5

### `ISSUE_000285` (Carried) Devin triage of the 15 `#1394` findings into fix / accept / out-of-scope drafts.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000286` Findings undispositioned

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000287` Infra change lands without exercising its own verification path

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000288` 0-char approvals followed by immediate merge

- Priority: Priority 3/10 from base 3 adjusted by: high reported frequency (71) (+1); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000289` Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off a

- Priority: Priority 5/10 from base 3 adjusted by: security scope SECRETS (+3); non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; security-sensitive surface SECRETS (+2); repository and paths both known (-1).
- Confidence: 0.6

### `ISSUE_000290` Empty approvals

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000291` Branch protection not enabled (as EM)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000292` Carried: review-log / atlas / header-relocation commits by hand

- Priority: Priority 4/10 from base 3 adjusted by: category AUTOMATION_OPPORTUNITY (+1).
- Complexity: Complexity 5/10 from: category AUTOMATION_OPPORTUNITY base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000293` (Carried) 11 NEEDS-DECISION items from `#1391` as bounded Devin PRs with her written acceptance tests.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000294` (Carried) Run the QA gate on the PR head before approval.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000295` Reviewer remediates, approves, merges

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000296` QA verdict consumed after merge

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000297` Carried: oversized single PR (`#1310`, `#1322`, `#1391`)

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.65

### `ISSUE_000298` (Carried) Devin drafts §12.4/§12.5 measurement PR.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000299` (Carried) One Devin PR per major #5–#11.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.6

### `ISSUE_000300` Author's findings dispositioned by the reviewer

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000301` Manual upstream fork sync (`paperclip-ai`)

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (19) (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.55

### `ISSUE_000302` (Carried) Fit assessment of `paperclip-ai` against the existing Devin/Claude workflow instead of a hand-maintained fork.

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000303` Large invoicing PRs with badge-only bodies (`#652`/`#578`)

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 8/10 from: category PROCESS_PRACTICE base 5; target repository not determined from the report (+2); no file paths identified (+1).
- Confidence: 0.65

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

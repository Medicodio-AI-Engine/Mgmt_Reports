# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-09-21

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **1** — 0 bug(s), 1 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ISSUE_000303` | Large invoicing PRs with badge-only bodies (`#652`/`#578`) | Work carried out: unresolved repository: repository history was not read (no local checkout with history) / Code now: target repository unresolved, so no code was inspected / Reported: Recurring pattern flagged for karthikmed: Large invoicing PRs with badge-only bodies (`#652`/`#578`). / Recommended: Test-evidence body before review | karthikmed | Process change | ENHANCEMENT | ENHANCEMENT | yes | 8 | 04:00 | 00:15 | 02:15 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |

## Out of pilot scope (21)

- `ISSUE_000282` Workflow/infra change merged without a dry run of its own verification path — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000283` Findings left undispositioned on open PRs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000284` Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable a — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000285` (Carried) Devin triage of the 15 `#1394` findings into fix / accept / out-of-scope drafts. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000286` Findings undispositioned — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000287` Infra change lands without exercising its own verification path — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000288` 0-char approvals followed by immediate merge — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000289` Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off a — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000290` Empty approvals — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000291` Branch protection not enabled (as EM) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000292` Carried: review-log / atlas / header-relocation commits by hand — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000293` (Carried) 11 NEEDS-DECISION items from `#1391` as bounded Devin PRs with her written acceptance tests. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000294` (Carried) Run the QA gate on the PR head before approval. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000295` Reviewer remediates, approves, merges — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000296` QA verdict consumed after merge — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000297` Carried: oversized single PR (`#1310`, `#1322`, `#1391`) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000298` (Carried) Devin drafts §12.4/§12.5 measurement PR. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000299` (Carried) One Devin PR per major #5–#11. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000300` Author's findings dispositioned by the reviewer — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000301` Manual upstream fork sync (`paperclip-ai`) — paperclip-ai is outside the medicodio pilot scope
- `ISSUE_000302` (Carried) Fit assessment of `paperclip-ai` against the existing Devin/Claude workflow instead of a hand-maintained fork. — paperclip-ai is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-09-19

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **0** — 0 bug(s), 0 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Out of pilot scope (18)

- `ISSUE_000282` Review-log / standards-log / atlas refresh commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000283` "Repair what the pre-push gate surfaced" (type errors, imports, JSX) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000284` Function-header relocation/restoration — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000285` Reviewer pushes 20–44 fix commits to a peer's PR then merges it — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000286` Hand Devin the 11 "Remaining items — author/user decision" from her own log as bounded PRs (R16 enforcement on two CREATE paths; single owner for the three regi — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000287` Devin-generated review-log/atlas commit from gate output, replacing 7 hand commits per PR. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000288` Run the Devin QA gate against the PR's preview before approval; paste the verdict into the approval body. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000289` Reviewer remediates, then approves and merges (no independent approver) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000290` Merge with own open pre-merge list — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000291` QA verdict consumed after merge — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000292` Header relocation / review-log commits by hand — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000293` Gate-surfaced repair commits after push — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000294` Oversized single PR (>200 files) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000295` Devin drafts the §12.4/§12.5 measurement PR (read-only queries, p50/p95 harness) — well-defined, bounded. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000296` Devin opens one PR per "major" (#5–#11 in the review) with the acceptance test stated in the log. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000297` Devin regression tests for the demotion-rejection and inheritance/PII-exclusion paths the QA gate could not exercise (7f items). — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000298` Oversized single PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000299` Author's own findings dispositioned by reviewer — globalcodio-monorepo is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

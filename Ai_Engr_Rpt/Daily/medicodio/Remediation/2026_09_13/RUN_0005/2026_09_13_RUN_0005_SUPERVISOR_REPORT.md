# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-09-13

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **0** — 0 bug(s), 0 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Out of pilot scope (21)

- `ISSUE_000282` Hand-fixing another member's findings, then approving and merging — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000283` `docs(review-logs)` commits written by hand — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000284` Re-running the 37-gate matrix and transcribing results into prose — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000285` Delegate the checklist-table chip-map change (`ITEM_SATISFACTION_CHIP`: `missing→Requested`, `pending_review→Received — under review`, `rejected→Needs fixing`,  — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000286` Delegate the `findDueForSweep` / worker cross-process signal reproduction (`CLEANUP-153`): have Devin write the failing test that proves an ESCALATED goal is ne — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000287` Delegate the 16 `findMany` without `take` audit (`CLEANUP-152`) as a per-site behaviour-change report, not a blanket patch. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000288` Reviewer remediates, approves, then merges — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000289` Merged over the approver's own written blocker — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000290` Post-merge QA-gate verdict unactioned in-window — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000291` Ad-hoc per-component timestamp formatting — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000292` Branch carried without a PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000293` Regression suite for the timezone migration — one Devin task to generate rendering tests for the 45 migrated sites (DST boundary, legacy timezone string, UTC se — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000294` Lint rule + codemod to prevent new private formatters re-appearing (the five deleted today prove drift is real). — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000295` Open `feat/hr-portal-revamp` as a draft PR via Devin with a body generated from the branch diff, so it stops accumulating unreviewed work. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000296` Work carried on a branch with no PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000297` Large single PR (73 files) awaiting a human reviewer — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000298` Author absent while another member remediates and merges his PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000299` Delegate the PRD Screen-Contract A2/A3 chip-map change on the checklist table plus both-portal snapshot tests — the top open item on his merged PR. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000300` Delegate the `outcome_statement` backfill question (frozen at open; existing goals keep wording the branch calls wrong) as a data-impact report before any migra — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000301` Decision items on his PRs resolved without him — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000302` PR-description accuracy — globalcodio-monorepo is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

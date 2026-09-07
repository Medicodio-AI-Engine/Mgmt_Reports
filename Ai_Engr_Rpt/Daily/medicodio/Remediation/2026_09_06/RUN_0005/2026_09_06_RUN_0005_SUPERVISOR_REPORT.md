# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-09-06

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **0** — 0 bug(s), 0 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Out of pilot scope (20)

- `ISSUE_000282` Fixing another author's PR to merge-readiness, then approving it — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000283` Backfilling "mandatory function headers" and `docs(headers)` commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000284` Repairing specs broken by fix commits (`realign five specs`, `repair three specs the gate run surfaced`) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000285` `docs(review-logs): record …` commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000286` Merging `dev` into a 100+-file feature branch and repairing the merge — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000287` Good Devin Candidate — "Convert the 20-blocker list from the `#1305` review into an automated DVR pre-review checklist (tenancy predicate on every firm-scoped q — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000288` Good Devin Candidate — "Write a regression test that fails when a `dev` merge into a feature branch reduces the `onRowClick`/fix count on files touched by both  — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000289` Possible Devin Candidate — "Propose a ≤ 60-file split plan for the next letter-groups/support-letter feature along the shared-types → db → api → web seam" — hum — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000290` > 100-file feature PRs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000291` Remediate-then-approve (non-independent review) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000292` Approve with own open blockers/decisions — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000293` Repairing test mocks/fixtures after interface changes (`repair stale test mocks`, `repair 3 pre-existing test-fixture bugs`, `repair gate-failing test/registry drift`) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000294` Fixing the blocker in a PR she is reviewing — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000295` Standards-audit log commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000296` Good Devin Candidate — "Re-run the 39/42 quality gates on the `#1305`/`#1318` merge commits and post the raw table to the PR; open issues for any gate that is n — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000297` Good Devin Candidate — "Add a `getStates` batching parity test for every `TrackableProvider` (document-checklist, checklist-group, payment, support_letter) so t — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000298` Possible Devin Candidate — "Implement the four open decisions on `#1305` (owned-rule guidance columns, canonical tier precedence, N+1 in the interactive tx, `Do — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000299` 100+-file PRs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000300` Reviewer fixes the blocker, then approves — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000301` PR-body claims not matching verification — globalcodio-monorepo is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

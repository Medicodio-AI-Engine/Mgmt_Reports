# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-08-30

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **0** — 0 bug(s), 0 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Corroborating signals (1)

1 support record(s) from the rating cards helped prioritise the tasks above. They are not tasks, and no individual rating is reproduced here.

## Out of pilot scope (33)

- `ISSUE_000282` Hand-writing the `/check` → `/fix` remediation commits after each gate run — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000283` Authoring the review-log markdown for each gate pass — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000284` Re-deriving whether a Devin finding is real — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000285` Delegate a permission/scope matrix suite for `MyAiWorkService` — one case per (caller permission × instance filter) combination. Two of this window's bugs and o — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000286` Delegate the `data_flows.md` AI Case Manager entity section, the one gap her own review left open and recommended as a fast follow-up. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000287` Delegate the `/fix` remediation pass on her next feature close-out and keep the review for herself, so verification and remediation are not done by the same han — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000288` Approve-and-merge within seconds of the last automated report — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000289` Reviewer and remediator are the same person — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000290` Hand-fixing blockers found by his own audit pass on a Devin-authored branch — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000291` Re-running and re-recording gate results across three review logs — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000292` Discovering that a spec suite mocks the data layer and therefore cannot fail — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000293` Delegate a non-mocked content-sync integration suite (export → bundle → import → rollback against a real schema). This is the highest-value delegable suite in G — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000294` Delegate the export/import round-trip fixtures for every registry table, including the JSON-expression natural key case that failed. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000295` Delegate the six `[needs decision]` items as one scoped follow-up PR with his decisions written as acceptance criteria — they are currently merged and unresolve — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000296` Reviewer-of-own-work — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000297` Very large PR instead of a reviewable series — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000298` Merge with `[needs decision]` items open — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000299` Implementing near-identical subscriber + notification + repository-hook trios per AI skill — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000300` Accumulating many phases on one branch before opening a PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000301` Hand-writing per-phase tests unevenly (3 of 8 commits) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000302` Delegate the subscriber/notification test matrix for the draft-letter skill (fired / not fired / duplicate / permission-denied), covering the paths the AI Revie — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000303` Delegate the AI-skill registry contract test so any new skill provider must satisfy the same interface the `DraftStepStartedSubscriber` rewire assumes. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000304` Delegate phase-by-phase PR preparation: each numbered phase becomes its own small PR with the acceptance criteria you already write in the commit subject. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000305` One very large PR instead of a reviewable series — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000306` Tests that encode current behaviour rather than intended behaviour — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000307` No observable Devin leverage — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000308` Signing off large merges with a one-word body — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000309` Manually judging whether a large PR is safe to merge — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000310` Assembling the release/promotion summary — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000311` Delegate a pre-merge gate check — a small CI job (Devin can write it in one scoped session) that blocks merge while any Devin Review finding or `[needs decision — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000312` Delegate generation of the merge/promotion summary from the commit range so the approval body is substantive by construction. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000313` Approval without content on a very large PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000314` Merge over an unresolved findings/decision set — globalcodio-monorepo is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-09-07

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **0** — 0 bug(s), 0 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Out of pilot scope (16)

- `ISSUE_000282` Finishing another author's PR to merge it (sync `dev`, fix, document, review, approve, merge) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000283` Recording review passes as `docs(review-logs)` commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000284` Clearing inherited `dev` gate failures on a feature branch (`content-table-registry`, migration drift) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000285` Repeating the same rigor checks by hand (recompute incident value, grep for consumers, verify DI import kind) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000286` Good Devin Candidate: write the three `merge-data-builder.spec.ts` tests the review specified (assert `resolveScheme(ctx.firmId, 'individual')`; stored-number f — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000287` Good Devin Candidate: a scheduled `dev` gate-health run that opens one fix PR when `dev` fails its own registry/migration checks, so feature branches stop inher — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000288` Possible Devin Candidate: draft ADR-0045's option table (A server adopts party-first / B web reads `primaryPersonId` / C scheme-wins-only-when-NULL) with the co — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000289` Approves and merges a branch he remediated — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000290` Own "needs decision" items left open at merge — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000291` `#1278` `importSession` SEV-High finding without fix or waiver — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000292` Large unreviewed branches — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000293` Insufficient data — one commit in the week — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000294` Good Devin Candidate: the three `merge-data-builder.spec.ts` tests the review specified (recipe given) — as her follow-up PR to `#1288`. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000295` Good Devin Candidate: close the four remaining `{{file_number}}` read sites the retracted PRD now lists as open (persons search, global search, client-portfolio — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000296` Devin findings on own PR unanswered — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000297` Open PR not progressed by its author — globalcodio-monorepo is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

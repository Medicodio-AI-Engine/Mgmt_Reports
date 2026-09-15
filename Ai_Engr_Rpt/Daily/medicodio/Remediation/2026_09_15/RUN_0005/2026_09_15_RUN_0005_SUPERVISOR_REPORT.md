# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-09-15

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **3** — 0 bug(s), 3 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ISSUE_000313` | Findings/promotions carried without disposition | Work carried out: unresolved repository: repository history was not read (no local checkout with history) / Code now: target repository unresolved, so no code was inspected / Reported: Recurring pattern flagged for Medicodio members: Findings/promotions carried without disposition. / Recommended: Tuesday-first triage with a named owner each | Medicodio members | Code fix | ENHANCEMENT | ENHANCEMENT | yes | 7 | 07:00 | 00:30 | 04:00 | category MECHANICAL_MIGRATION confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000314` | `feat/inpatient-engine` no PR | Work carried out: unresolved repository: repository history was not read (no local checkout with history) / Code now: target repository unresolved, so no code was inspected / Reported: Recurring pattern flagged for Medicodio members: `feat/inpatient-engine` no PR. / Recommended: Draft PR | Medicodio members | Process change | ENHANCEMENT | ENHANCEMENT | yes | 7 | 03:30 | 00:15 | 02:00 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |
| `ISSUE_000315` | Reviews ≤10 chars on production-bound PRs | Work carried out: unresolved repository: repository history was not read (no local checkout with history) / Code now: target repository unresolved, so no code was inspected / Reported: Recurring pattern flagged for Medicodio members: Reviews ≤10 chars on production-bound PRs. / Recommended: Approval template naming what was checked | Medicodio members | Process change | ENHANCEMENT | ENHANCEMENT | yes | 8 | 04:00 | 00:15 | 02:15 | category PROCESS_PRACTICE confirms the reported enhancement. state DEV_REVIEW, review PENDING. nothing changed (dry run). |

## Out of pilot scope (31)

- `ISSUE_000282` Hand-written `docs(review-logs)` commits (standards audit, architect review, PR review, gate results) — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000283` "regenerate atlas (module_map, screen_index)" commit — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000284` Remediating a peer's PR before approving it — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000285` Use Devin to write the non-mocked integration suite for the email-triage recovery legs (`StuckEmailTriageRecovery` 4 legs, BullMQ jobId dedupe) — the 09-13/09-1 — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000286` Delegate the two open `email_triage_readings` index decisions on `#1367` as a measured task: Devin runs `EXPLAIN` on `findTriagePage` `all`/`needs-you` buckets  — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000287` Pre-merge QA on `#1373`: trigger the Devin QA gate on the branch before approval so the NOT READY pattern (4 in a row) does not repeat on a 95-file PR. Good Dev — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000288` Reviewer remediates, then approves, then merges the same PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000289` Merge with own "needs your decision" items open — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000290` Post-merge Devin QA NOT READY — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000291` Hand-written review-log commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000292` Atlas regeneration / function-header sync / debt-ledger sync commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000293` `/review-all` ledger written into `docs/review-logs/` by hand — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000294` Review-pass commits on a peer's branch — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000295` Use Devin to implement the Entity Status Phase 1 PRD as a spike PR against `dev` with the PRD's acceptance criteria as the prompt — the PRD is written, the surf — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000296` Use Devin to convert the 7 NEEDS-DECISION items on `#1373` into issues with options and evidence, so the decision owner (Saijyoti) can answer in writing before  — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000297` Devin QA gate pre-merge on `#1373` (shared with Saijyoti). — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000298` Review-pass as 20+ direct commits on a peer's PR instead of a review — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000299` Work on a branch without a PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000300` Sync/regeneration chores as human commits — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000301` Hand-fixing Devin PRs after Devin Review findings — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000302` Ask Devin to add a regression test for the orphan-checklist audit count on `#1360` and answer the `scripts/` approval-gate finding — Good Devin Candidate. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000303` Get `#1360` and `#1364` merged by requesting a named reviewer; both are small and green. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000304` Small PRs left open without requesting review — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000305` Large PR opened without a named reviewer — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000306` Have Devin produce the reviewer's map of `#1363` (per-area summary, risk list, test evidence) so a peer can review 110 files in bounded time — Good Devin Candid — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000307` Devin QA gate on `#1363` before merge — the PR touches performance/security paths. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000308` >60-file PR without reviewer — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000309` Branch with large checkpoint, no PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000310` Open `feat/hr-portal-revamp` as a draft PR and let Devin Review run — the branch has been invisible to review for 5 reports. — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000311` `feat/hr-portal-revamp` no PR — globalcodio-monorepo is outside the medicodio pilot scope
- `ISSUE_000312` Placeholder `Co-Authored-By` Devin e-mails — globalcodio-monorepo is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

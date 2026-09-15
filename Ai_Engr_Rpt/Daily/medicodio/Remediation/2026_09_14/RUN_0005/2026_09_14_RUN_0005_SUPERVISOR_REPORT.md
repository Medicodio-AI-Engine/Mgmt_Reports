# Supervisor report — remediation tasks

**Run:** `RUN_0005` · **Report date:** 2026-09-14

> **Dry run.** Nothing was fixed: no repository was modified, no commit or pull request was created. Every row is a task awaiting a human decision.

- Tasks in scope: **0** — 0 bug(s), 0 enhancement(s)
- Reported category revised after analysis: **0**

| Task_ID | Task_Name | Task_Description | Task_Owner | Task_Type | Category | Revised_Category | Category_Match | Complexity | Time_Human | Time_AI | Time_Human_AI | Comments |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Out of pilot scope (3)

- `ISSUE_000282` Manual "Sync fork" of `paperclip-ai` from `paperclipai/paperclip` — paperclip-ai is outside the medicodio pilot scope
- `ISSUE_000283` None meaningful; the only observed activity is a mechanical sync (Recommendation: script it, do not delegate it). — paperclip-ai is outside the medicodio pilot scope
- `ISSUE_000284` None confirmable — paperclip-ai is outside the medicodio pilot scope

---

Time columns are planning estimates derived from the analysed complexity, remediability and autonomy tier — not measurements. `Time_Human` is how long the task takes a person working alone; `Time_AI` is how long it takes Devin working alone — writing the change is the part it does fastest, so it is a small fraction of the human figure, and for a tier C or D task it covers investigation and a written proposal only, because policy forbids the AI from making that change. `Time_Human_AI` is the elapsed time when the two collaborate — Devin drafts and a person directs and reviews — so it is not the sum of the other two and is shorter than `Time_Human`. `Task_Description` states the work the repository history shows was carried out, what a read-only look at the code shows now, and what the report claimed and recommended.

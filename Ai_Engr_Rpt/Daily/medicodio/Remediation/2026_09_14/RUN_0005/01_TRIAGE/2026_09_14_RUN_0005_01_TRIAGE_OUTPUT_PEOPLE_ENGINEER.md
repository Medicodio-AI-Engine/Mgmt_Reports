# Triage — priority and complexity

**Run:** `RUN_0005` · **Report date:** 2026-09-14 · **Stage:** `01_TRIAGE` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

| Issue | Title | Category | Repository | Priority | Complexity | Tier | Remediability |
| ----- | ----- | -------- | ---------- | -------- | ---------- | ---- | ------------- |
| `ISSUE_000282` | Manual "Sync fork" of `paperclip-ai` from `paperclipai/paperclip` | MECHANICAL_MIGRATION | paperclip-ai | 5 | 3 | — | CODE_CHANGE |
| `ISSUE_000283` | None meaningful; the only observed activity is a mechanical sync (Recommendation: script it, do not delegate it). | MECHANICAL_MIGRATION | paperclip-ai | 4 | 5 | — | CODE_CHANGE |
| `ISSUE_000284` | None confirmable | PROCESS_PRACTICE | paperclip-ai | 2 | 6 | — | NON_CODE_PROCESS |

## Scoring rationale

### `ISSUE_000282` Manual "Sync fork" of `paperclip-ai` from `paperclipai/paperclip`

- Priority: Priority 5/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1); high reported frequency (31) (+1).
- Complexity: Complexity 3/10 from: category MECHANICAL_MIGRATION base 4; repository and paths both known (-1).
- Confidence: 0.65

### `ISSUE_000283` None meaningful; the only observed activity is a mechanical sync (Recommendation: script it, do not delegate it).

- Priority: Priority 4/10 from base 3 adjusted by: category MECHANICAL_MIGRATION (+1).
- Complexity: Complexity 5/10 from: category MECHANICAL_MIGRATION base 4; no file paths identified (+1).
- Confidence: 0.5

### `ISSUE_000284` None confirmable

- Priority: Priority 2/10 from base 3 adjusted by: non-code process item, no software risk (-1).
- Complexity: Complexity 6/10 from: category PROCESS_PRACTICE base 5; no file paths identified (+1).
- Confidence: 0.55

Ordering confers no permission: what may actually be done is decided by the autonomy tier and the guardrail engine.

# Employee Rating Cards — 2026-09-21

**Review window:** 2026-09-20 03:00 → 2026-09-21 03:00 UTC (Sunday). **Comparison windows:** previous working day 09-18, week 09-13 → 09-20, month 08-21 → 09-20. Companion to `2026_09_21_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`org.sessions.view`) for the 19th consecutive run. "Observable Devin Leverage" can only be scored from GitHub artefacts (Devin Review / CI-diagnosis comments and their disposition, Devin QA gate verdicts, `devin-ai-integration[bot]` PRs, Claude/Devin trailers). Prompt quality, ACU effort, tests requested and correction loops are unobservable.
- **No Jira, no Sentry.** Coordination, support and incident work are invisible; a silent GitHub day is not evidence of no work.
- **A zero-human-event day (second in a row).** No commits, PRs, reviews or comments in any product repository of either product. The only event was automated: the first scheduled run of the `ACR purge` workflow (GC `#1362`, merged 09-15) failed on a never-created repository variable, and Devin posted the diagnosis. That failure is evidence about a 09-15 merge, not about anyone's Sunday; it is recorded as carried context for ragha82 (author) and anirudh-medicodio (0-char approver) and **is not scored today** — a passive consequence on a non-working day is not a reasonable opportunity to act. **Every member is NR on every dimension.**
- **Volume is not productivity.** Commit, PR, file and review counts are cited only as context.
- A dimension without in-window evidence is **NR** and excluded from the weighted average; fewer than three rated dimensions → overall **NR**. Bands: Strong ≥ 8, Solid ≥ 7, Mixed ≥ 5, Needs Support < 5.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; carried items closed | Work merged or materially advanced; minor loose ends | Progress without closure; carried items untouched | Stalled, abandoned without record, or merged without follow-through |
| Engineering Rigor | 25 | Tests + accurate PR body + findings addressed before merge; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge into prod paths |
| Code Review Contribution | 15 | Substantive, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings or >100 files |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reason/test | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin PRs closed without note |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ragha82 | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; **new carried item:** `#1362` ACR purge failed first run — `ACR_NAME` never created, `dry_run` never dispatched; `#1394` ×15 day 4, `#1382` day 6) |
| anirudh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: 0-char approval on `#1362` whose first run failed; branch-protection recommendation day 6) |
| SaijyotiMeti | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; latest rated card 09-19: 5.4 Mixed; `#1398` verdict unacknowledged day 3) |
| SaahilVishwakarma | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; latest rated card 09-19: 5.4 Mixed, low confidence) |
| Pj-Vineeth-Kumar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: branch without PR, day 4) |
| akanksh-rv, Amrutha-Beedikar, svh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; akanksh `#1373` items day 7) |
| karthikmed | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no events) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, Medicodio-Amit, avinash-codio, vishnu-saikarthik, NandanDate-Medicodio, ashwinsk-medicodio, Sumedh Kaulgud, Murali-Shetty19, sameer-s-mansur, shaheen-khan11, Hitesh Shanthakumar, afifashaikh007, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (zero events in all Medicodio repos, 3rd consecutive day; Sunday is a regular non-working day for this team) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — (1 event: CI-diagnosis comment on `#1362`, 82 s after failure; correct root cause, scope restraint, safe re-run path) |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions). No member has a rated dimension today, so no average is computed.

## Cards

### All members — NR (no in-window evidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | NR | **Observed Fact:** 0 commits on any branch, 0 PRs opened/merged/closed in all seven product repositories. Carried open items did not move; a Sunday is not a reasonable opportunity to move them, so their age is recorded and not scored. |
| Engineering Rigor | NR | No code, tests, PR bodies or finding dispositions in window. **Observed Fact (carried, not scored):** the `#1362` workflow merged 09-15 failed its first scheduled run because a prerequisite documented in its own header (`vars.ACR_NAME`) was never created and the `dry_run` dispatch path was never exercised. This becomes a Rigor input for ragha82 and anirudh-medicodio on the next working day depending on how it is handled. |
| Code Review Contribution | NR | 0 human review submissions, 0 human comments. |
| Observable Devin Leverage | NR | 1 Devin event (CI diagnosis on `#1362`), no human consumption yet (Sunday — judge Monday). 8 Devin PRs (`#1392`–`#1398`) still open with no human response (day 4) — carried, not scored today. |
| Automation of Repetitive Work | NR | No repetitive human action observed. The failed job is itself an automation of a previously manual purge — credit will depend on it working. |
| Consistency Across Windows | NR | Rated only when there is a day to compare; none today. |

**Carried context per owner (Observed Fact, verified still open at collection; for Monday, not for scoring):**

- **ragha82** — `#1362` ACR purge: create `ACR_NAME`, dispatch `dry_run=true`, link run on the PR; `#1394` ×15 findings undispositioned (day 4); `#1382` red spec (day 6).
- **anirudh-medicodio** — branch protection on `dev` not enabled (recommended 09-16 → 09-20); 0-char approval on `#1362`.
- **SaijyotiMeti** — `#1398` BLOCK RELEASE / NOT READY 52 verdict on `#1391` unacknowledged (day 3).
- **SaahilVishwakarma** — `#1391` follow-ups (7 majors, 11 decision items, §12.4/§12.5) not opened.
- **Pj-Vineeth-Kumar** — `feat/support-letter-word-fidelity` (11 commits) without a PR (day 4).
- **akanksh-rv** — `#1373` decision items (day 7).
- **vishnu-saikarthik / NandanDate-Medicodio** — `#460` "fix remains inactive" finding in `prod` (day 5).
- **avinash-codio** — `#464` ×6, `#458` ×4 undispositioned; `#465` no reviewer.
- **jatinkushwaha-medicodio** — `#657` ×26, `#584` ×6 open findings.
- **amit-pandey-medicodio** — `#651` closed-unmerged / prod `23505` status; carried findings on `#6`/`#652`/`#578`.
- **Murali-Shetty19** — `#581` security finding; `#435` open 13 days without activity.
- **Medicodio-Amit** — `#462` no human reviewer.
- **karthikmed** — `#652`/`#578` badge-only PR bodies; `paperclip-ai` fork synced by hand.
- **Hitesh Shanthakumar, ashwinsk-medicodio, sameer-s-mansur, shaheen-khan11** — branches without PR.
- **Amrutha-Beedikar, svh-medicodio, Sumedh Kaulgud, afifashaikh007, Shashvi1** — no carried items.

**Latest rated view for each member:** 09-19 cards (Saijyoti 5.4, Saahil 5.4); 09-18 cards for Global Codio members active that day; 09-17/09-18 cards for the Medicodio team. Today adds no score movement in either direction.

## How to read the spread

- **Observed Fact:** there is no spread. Zero human engineering events in both products for the second consecutive day; every member is NR on every dimension. The one automated event — a first-run failure of a weekly infra job merged on a 0-char approval — is the only new information and it concerns a past merge, not today's work.
- **Inference:** the weekend silence is normal for both teams (every Sunday in the 30-day history has 0 Medicodio commits; GC Sundays have ranged 0–16). The week total (582 commits, lowest on record) is calendar-shaped. The `#1362` failure is small and safe (the script's guard aborted before any deletion) but it is the clearest concrete example this month of what an empty approval costs: the missing prerequisite was written in the PR's own file header.
- **Recommendation:** do not read the all-NR grid as a bad day; read it as no day. Monday's scores will move most on: (1) branch protection on `globalcodio-monorepo` `dev` (owner anirudh, 6th day); (2) whether the `#1362` diagnosis is acted on within one working day — a clean test of Devin-output consumption; (3) a disposition pass on the carried findings above, including Devin fix PRs `#1393`/`#1396`.

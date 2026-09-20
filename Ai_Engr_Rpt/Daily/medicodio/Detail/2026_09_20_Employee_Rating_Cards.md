# Employee Rating Cards — 2026-09-20

**Review window:** 2026-09-19 03:00 → 2026-09-20 03:00 UTC (Saturday). **Comparison windows:** previous working day 09-18, week 09-12 → 09-19, month 08-20 → 09-19. Companion to `2026_09_20_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`org.sessions.view`) for the 18th consecutive run. "Observable Devin Leverage" can only ever be scored from GitHub artefacts (Devin Review findings and their disposition, Devin QA gate verdicts, `devin-ai-integration[bot]` PRs, Claude/Devin trailers). Prompt quality, ACU effort, tests requested and correction loops are unobservable.
- **No Jira, no Sentry.** Coordination, support and incident work are invisible; a silent GitHub day is not evidence of no work.
- **A zero-event day.** There were no commits, PRs, reviews or comments in any product repository of either product. The only human action in the org was an administrative "Sync fork" on an external open-source fork. **No dimension has in-window evidence for any member, so every member is NR today.** Week/month context is noted per member but not scored — a weekend day off must not read as a low score, and a rating cannot be manufactured from carried items alone.
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
| SaijyotiMeti | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; latest rated card 09-19: 5.4 Mixed) |
| SaahilVishwakarma | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; latest rated card 09-19: 5.4 Mixed, low confidence) |
| anirudh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: branch-protection recommendation, day 5) |
| ragha82 | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: `#1394` ×15 day 3, `#1382` day 5) |
| Pj-Vineeth-Kumar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: branch without PR, day 3) |
| akanksh-rv, Amrutha-Beedikar, svh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events) |
| karthikmed | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (one administrative fork-sync click on an external fork; not product work, not scored) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, Medicodio-Amit, avinash-codio, vishnu-saikarthik, NandanDate-Medicodio, ashwinsk-medicodio, Sumedh Kaulgud, Murali-Shetty19, sameer-s-mansur, shaheen-khan11, Hitesh Shanthakumar, afifashaikh007, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (zero events in all Medicodio repos, 2nd consecutive day; Saturday is a regular non-working day for this team) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — (0 events) |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions). No member has a rated dimension today, so no average is computed.

## Cards

### All members — NR (no in-window evidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | NR | **Observed Fact:** 0 commits on any branch, 0 PRs opened/merged/closed in all seven product repositories. Carried open items (listed per owner below) did not move, but a Saturday is not a reasonable opportunity to move them, so their age is recorded and not scored. |
| Engineering Rigor | NR | No code, tests, PR bodies or finding dispositions in window. |
| Code Review Contribution | NR | 0 review submissions, 0 PR/review comments by any human. |
| Observable Devin Leverage | NR | 0 Devin Review / QA events; 8 Devin PRs (`#1392`–`#1398`) remain open in `globalcodio-monorepo` with no human response — carried, not scored today. |
| Automation of Repetitive Work | NR | Only repetitive action observed: `karthikmed`'s manual "Sync fork" on the external `paperclip-ai` fork (a scheduled sync would remove it). Insufficient to rate. |
| Consistency Across Windows | NR | Consistency is rated only when there is a day to compare; none today. |

**Carried context per owner (Observed Fact, verified still open at collection; for Monday, not for scoring):**

- **SaijyotiMeti** — `#1398` BLOCK RELEASE / NOT READY 52 verdict on `#1391` unacknowledged (day 2); 09-19 recommendation stands (next review: REQUEST CHANGES, no own commits, second approver).
- **SaahilVishwakarma** — `#1391` follow-ups (7 majors, 11 decision items, §12.4/§12.5 measurements) not yet opened.
- **anirudh-medicodio** — branch protection on `dev` not enabled (recommended 09-16 → 09-19).
- **ragha82** — `#1394` ×15 findings undispositioned (day 3); `#1382` red spec (day 5).
- **Pj-Vineeth-Kumar** — `feat/support-letter-word-fidelity` (11 commits) still without a PR (day 3).
- **akanksh-rv** — `#1373` decision items (day 6).
- **vishnu-saikarthik / NandanDate-Medicodio** — `#460` "fix remains inactive" finding in `prod` (day 4).
- **avinash-codio** — `#464` ×6, `#458` ×4 undispositioned; `#465` no reviewer.
- **jatinkushwaha-medicodio** — `#657` ×26, `#584` ×6 open findings.
- **amit-pandey-medicodio** — `#651`/prod `23505` status; carried findings on `#6`/`#652`/`#578`.
- **Murali-Shetty19** — `#581` security finding; `#435` open 12 days without activity.
- **Medicodio-Amit** — `#462` (26 files) no human reviewer.
- **karthikmed** — `#652`/`#578` badge-only PR bodies (09-17); `paperclip-ai` fork synced by hand.
- **Hitesh Shanthakumar, ashwinsk-medicodio, sameer-s-mansur, shaheen-khan11** — branches without PR.
- **Amrutha-Beedikar, svh-medicodio, Sumedh Kaulgud, afifashaikh007, Shashvi1** — no carried items.

**Latest rated view for each member:** 09-19 cards (Saijyoti 5.4, Saahil 5.4); 09-18 cards for the Global Codio members active that day; 09-17/09-18 cards for the Medicodio team. Read those alongside this file; today adds no score movement in either direction.

## How to read the spread

- **Observed Fact:** there is no spread. Zero engineering events in both products; every member is NR on every dimension. This is the first Saturday in the 30-day history with zero commits organisation-wide (previous Saturdays 19–93 commits, all Global Codio), and it follows a Friday with a single active author.
- **Inference:** the most likely explanation is planned time off across both teams — Medicodio has been silent on every Saturday but one this month, and Global Codio's weekend contributors (Saijyoti, akanksh, anirudh, Vineeth) all took this one off. It cannot be verified without Jira or calendar access, and a single quiet weekend is not a trend. The week's total (601 commits, lowest on record) is calendar-shaped, not a per-person decline.
- **Recommendation:** do not read the all-NR grid as a bad day; read it as no day. The scores that matter next are Monday's, and the two things that would move them most are the same as on 09-19: branch protection on `globalcodio-monorepo` `dev` (approver ≠ committer; owner anirudh) and a Monday-morning disposition pass on the carried findings listed above, including the two unreviewed Devin fix PRs `#1393`/`#1396`.

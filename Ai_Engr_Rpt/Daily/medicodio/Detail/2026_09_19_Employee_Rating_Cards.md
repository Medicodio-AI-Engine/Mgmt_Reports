# Employee Rating Cards — 2026-09-19

**Review window:** 2026-09-18 03:00 → 2026-09-19 03:00 UTC. **Comparison windows:** previous working day 09-17, week 09-11 → 09-18, month 08-19 → 09-18. Companion to `2026_09_19_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`org.sessions.view`) for the 17th consecutive run. "Observable Devin Leverage" is scored only from GitHub artefacts (Devin Review findings and their disposition, Devin QA gate verdicts, `devin-ai-integration[bot]` PRs, Claude trailers). Prompt quality, ACU effort, tests requested and correction loops are unobservable.
- **No Jira, no Sentry.** Coordination, support and incident work are invisible; a silent GitHub day is not evidence of no work.
- **A single-author day.** 44 of 48 commits were by one person; every Medicodio repository had zero events (non-working day inferred). Only two members have in-window evidence. Everyone else is **NR** today; their week/month context is noted but not scored, so that a day off does not read as a low score.
- **Volume is not productivity.** Commit, PR, file and review counts are cited as evidence of *what* happened, never as the score.
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
| SaijyotiMeti | Global Codio | **5.4** | Mixed | 6 | 6 | 4 | 6 | 4 | 5 | Medium (GitHub only; 6 dims; single-PR day) |
| SaahilVishwakarma | Global Codio | **5.4** | Mixed | 6 | 5 | NR | 4 | NR | 7 | Low (4 dims; no events by him in window — scored on the PR that merged) |
| anirudh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: branch-protection recommendation 3 days) |
| ragha82 | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: `#1394` ×15, `#1382`) |
| Pj-Vineeth-Kumar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; carried: branch without PR) |
| akanksh-rv, Amrutha-Beedikar, svh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, Medicodio-Amit, avinash-codio, vishnu-saikarthik, NandanDate-Medicodio, ashwinsk-medicodio, Sumedh Kaulgud, karthikmed, Murali-Shetty19, sameer-s-mansur, shaheen-khan11, Hitesh Shanthakumar, afifashaikh007, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (zero events in all Medicodio repos; non-working day inferred; carried items listed in the activity report) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions). Saijyoti: (6·25 + 6·25 + 4·15 + 6·15 + 4·10 + 5·10) / 100 = 5.4. Saahil: (6·25 + 5·25 + 4·15 + 7·10) / 75 = 5.4.

## Cards

### SaijyotiMeti — Global Codio · Overall 5.4 · Mixed

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1391` (284 files, 62 commits) merged into `dev` after her 44 commits; her own closeout log listed 4 "still open — author-side, before merge" items at merge; Devin QA BLOCK RELEASE / NOT READY 52 posted 74 min later; three of six central behaviours unexercised. **Inference:** the feature landed, the follow-through did not. |
| Engineering Rigor | 6 | **Observed Fact:** tests added for three 0%-coverage helpers; nine suites repaired; HLD/ADR-0051 and deployment runbook written; migrations verified additive. Against: 28,133-line change merged without the §5.2 size justification; §12.4/§12.5 pre-merge gates converted to "accepted risk"; 6 "repair what the gate surfaced" commits imply gate run after push. |
| Code Review Contribution | 4 | **Observed Fact:** 9,954-char architect/EM review — specific, SHA-linked, verifies schema/indexes/RLS (would score 9 on content). Then `approved` (8 chars) 9 min later on a branch carrying 44 of her own commits, merge 11 s after that — the 7th reviewer-remediates-approves-merges instance since 09-06, and the one yesterday's report named in advance. **Inference:** review changed the code; approval was not independent. Rubric 1–4 band: approval on a >100-file PR with open majors. |
| Observable Devin Leverage | 6 | **Observed Fact:** Devin Review findings adjudicated in her log (2 VERIFIED → fixed/NEEDS-DECISION; stale "empty template" comment correctly dismissed); `/architect-review`, `/check`, `/fix`, 19 `/review-*` skills run. Devin QA gate consumed after merge (5th of her merges to get a sub-READY verdict post-merge). |
| Automation of Repetitive Work | 4 | **Observed Fact:** 7 review-log/atlas commits, 2 header-relocation commits and 6 gate-repair commits by hand; header lint rule recommended 09-17, not proposed. |
| Consistency Across Windows | 5 | **Observed Fact:** cards 09-16 6.4 → 09-17 6.1 → 09-18 6.4 → today 5.4. Review prose consistently strong; merge governance consistently the same shape (`#1322`, `#1367`, `#1380`, `#1390`, `#1391`). |

**Recommendation:** next PR she reviews — REQUEST CHANGES, zero own commits, second approver, QA verdict pasted before approval. If that holds once, Review and Delivery both move to 7+.

### SaahilVishwakarma — Global Codio · Overall 5.4 · Mixed (Low confidence)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1391` merged; his 24 commits (09-17) delivered the party model, PRD walkthrough, standards audit and 5 suite repairs. No commit, comment or reply from him in window while 44 fixes landed on his branch. **Inference:** delivered, but closure was done by someone else. |
| Engineering Rigor | 5 | **Observed Fact:** PR body 115 lines, judged "GOOD" by the reviewer; PRD 2,075 lines. Against: 284 files / 28k lines in one PR (rule ceiling 800); his own PRD pre-merge gates §12.4/§12.5 left `*(to fill)*`; 4 gate-surfaced repair commits after push. |
| Code Review Contribution | NR | No reviews on others' PRs. |
| Observable Devin Leverage | 4 | **Observed Fact:** 16 Devin findings on his PR; 3 auto-resolved by his 09-17 pushes; 0 answered by him in-thread; the rest dispositioned in the reviewer's log. All commits Claude-trailed. |
| Automation of Repetitive Work | NR | No in-window evidence. |
| Consistency Across Windows | 7 | **Observed Fact:** 09-18 card 6.2; 112 commits in the month in bursts; same oversized-PR shape as `#1310` (09-09) and `#1322` (09-11), both also merged by Saijyoti after her commits. |

**Recommendation:** own the follow-ups — seven majors, §12.4/§12.5 measurements, the three QA-untested behaviours — as PRs under his name this week; answer findings in-thread the day they land.

### Members with no in-window evidence (NR)

anirudh-medicodio, ragha82, Pj-Vineeth-Kumar, akanksh-rv, Amrutha-Beedikar, svh-medicodio (Global Codio); amit-pandey-medicodio, jatinkushwaha-medicodio, Medicodio-Amit, avinash-codio, vishnu-saikarthik, NandanDate-Medicodio, ashwinsk-medicodio, Sumedh Kaulgud, karthikmed, Murali-Shetty19, sameer-s-mansur, shaheen-khan11, Hitesh Shanthakumar, afifashaikh007, Shashvi1 (Medicodio).

**Observed Fact:** zero commits, PRs, reviews or comments in the window; the six Medicodio repositories had no events at all. **Inference:** a non-working day for Medicodio (third zero-activity weekday after 08-31 and 09-14); Global Codio members other than Saijyoti simply had no GitHub-visible work. Not scored. Yesterday's cards (09-18) remain the latest rated view for these members; carried open items are listed per owner in the activity report's Management Attention section.

## How to read the spread

- **Observed Fact:** two rateable members, both Global Codio, both 5.4 — one for merging her own remediation of a 284-file PR without an independent approver and before the QA verdict, the other for leaving his PR's findings and closure to the reviewer. Everyone else NR.
- **Inference:** the low spread today is not a team-wide signal; it is one merge event seen from two sides. The scores are lower than the same people's 09-18 cards (6.4 / 6.2) because the exact governance step recommended for this PR 24 h earlier was not taken, not because less work was done — 44 substantive commits, tests and a runbook landed.
- **Recommendation:** read today alongside the 09-18 cards. The one structural change that would have changed both scores is branch protection (approver ≠ committer, QA verdict before approval) on `globalcodio-monorepo` `dev` — owned by the EM, recommended three days running.

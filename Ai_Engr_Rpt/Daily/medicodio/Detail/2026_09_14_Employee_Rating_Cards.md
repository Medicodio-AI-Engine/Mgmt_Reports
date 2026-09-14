# Employee Rating Cards — 2026-09-14

**Review window:** 2026-09-13 03:00 UTC → 2026-09-14 03:00 UTC (Sunday). Comparison windows: previous working day 09-11, week 09-06 → 09-13, month 08-14 → 09-13. Companion to `2026_09_14_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`Missing required permission 'org.sessions.view'`) for the **12th consecutive run**; no MCP servers (Jira, Sentry) were callable. Prompt quality, ACU/effort, tests-requested and correction burden are unobservable. "Observable Devin Leverage" can only ever be scored from GitHub-visible artefacts (Devin-authored PRs, `Co-Authored-By: Devin` trailers, Devin Review/QA findings and their dispositions). Claude markers are not counted as Devin usage.
- **Zero product-repository activity in the window.** No commits, PRs, reviews or comments in any of the six product repositories between 09-13 03:00 and 09-14 03:00 UTC. The only human commit in the organization was a fork-sync merge in the third-party fork `paperclip-ai`. There is therefore **no in-window evidence for any dimension for any member**.
- **NR rules.** A dimension with no in-window evidence is NR and excluded from the weighted average; fewer than three rated dimensions → overall **NR**. Consequently **every member is NR today**. NR is "no evidence", not a low score, and must not be trended.
- **Volume is never scored.** Commit, PR, file and line counts appear only as context.
- **Product boundaries.** Medicodio and Global Codio members are scored against the same rubric but never compared to each other's conventions.
- **Identity note.** `Karthik R Khatavkar` (karthik.r@medicodio.ai) appears for the first time; his only observed activity in 31 days is fork syncing of `paperclip-ai`, which is administrative and not rated.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure | Stalled, abandoned without record, or merged without controls |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin bypassed on reviewable work |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

Bands: **Strong** ≥ 8 · **Solid** ≥ 7 · **Mixed** ≥ 5 · **Needs Support** < 5.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| akanksh-rv | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, Sunday) |
| Pj-Vineeth-Kumar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, Sunday) |
| SaijyotiMeti | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, Sunday) |
| anirudh-medicodio, ragha82, Amrutha-Beedikar, svh-medicodio, SaahilVishwakarma | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, 2nd day) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, Hitesh Shanthakumar, Vishnu Sai Karthik, ashwinsk-medicodio, avinash-codio, sumedh-codio, Murali-Shetty19, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, 2nd day) |
| Karthik R Khatavkar | Shared (fork) | NR | — | NR | NR | NR | NR | NR (1 mechanical fork sync; not rated) | NR | — (administrative only) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Change vs 2026-09-13 cards: Pj-Vineeth-Kumar 7.7 → **NR**; akanksh-rv 6.7 → **NR**; all others remain NR. None of these are score changes — they are absence of evidence on a Sunday.

**Last rated values for reference (do not trend from today):** 09-13 — Pj-Vineeth-Kumar 7.7 Solid, akanksh-rv 6.7 Mixed. 09-12 (last working-day cards) — Medicodio-Amit 7.8, Pj-Vineeth-Kumar 7.3, anirudh-medicodio 7.1, Amrutha-Beedikar 7.1, ashwinsk-medicodio 4.3, avinash-codio 3.4; svh, Saahil, Murali, sumedh NR. Next working-day cards (09-15 report for 09-14 → 09-15) should compare against 09-12 and 09-11, not against this card set.

## Cards

## Karthik R Khatavkar — Shared (fork `paperclip-ai`) — Overall NR — Confidence: Low (0 dimensions rated)

- **Observed Fact:** one merge commit (`6fe0832`, 03:22 UTC) syncing upstream `paperclipai:master` into the org fork; 11 identical syncs since 08-13; no product-repo activity in any window.
- **Inference:** operating/evaluating a third-party tool, not shipping product code; nothing here is scorable engineering work.
- **Recommendation:** replace the manual sync with a scheduled workflow; state the fork's purpose in the repo README.

## Members not rated this window

**Global Codio:** akanksh-rv, Pj-Vineeth-Kumar, SaijyotiMeti, anirudh-medicodio, ragha82, Amrutha-Beedikar, svh-medicodio, SaahilVishwakarma — no commits, PR events, reviews or comments in `globalcodio-monorepo`. All 14 open PRs untouched since 09-12 05:04 UTC.

**Medicodio:** amit-pandey-medicodio, jatinkushwaha-medicodio, sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, Hitesh Shanthakumar, Vishnu Sai Karthik, ashwinsk-medicodio, avinash-codio, sumedh-codio, Murali-Shetty19, Shashvi1 — zero activity across all five Medicodio repositories, second consecutive day.

Open items carried unchanged into Monday (for the next rated cards): `#1371`/`#1369`/`#1358` fix PRs (Global Codio); `#1366` decision items (akanksh-rv); `#1363`/`#1365`/`#1367` unreviewed; `#308` findings, `#314`, engine `#435` (Medicodio); `feat/inpatient-engine` and `feat/hr-portal-revamp` without PRs.

## How to read the spread

- **Observed Fact:** the organization produced no product-repository events in the 24-hour window; the only human commit was an administrative fork sync. Week and month facts are unchanged from 09-13 (week: 1,286 commits / 153 opened / 122 merged / 161 human reviews, 147 ≤10 chars; month: 4,436 / 458 / 381 / 411, 388 ≤10 chars).
- **Inference:** a fully quiet Sunday following a near-quiet Saturday is consistent with the three prior weekend windows and indicates nothing about individual performance. The material signal is what did *not* happen: three Devin QA fix PRs, one security finding and nine Medicodio findings entered the weekend unowned and left it unowned.
- **Recommendation:** treat the 09-15 report (Monday's activity) as the next comparable card set; measure it against 09-11/09-12. Managers should use Monday morning to clear the carried items listed above before new work starts, and grant `org.sessions.view` so Devin leverage can finally be scored from session data rather than GitHub artefacts.

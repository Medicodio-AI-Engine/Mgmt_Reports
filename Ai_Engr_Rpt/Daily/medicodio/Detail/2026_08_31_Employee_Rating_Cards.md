# Employee Rating Cards — 2026-08-31

**Review window:** 2026-08-30 03:00 → 2026-08-31 03:00 UTC (Sunday). Companion report: `2026_08_31_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

1. **The review window contains zero engineering activity.** Across all five product repositories there were 0 commits (default *and* non-default branches), 0 PRs opened/merged/closed, 0 review events, 0 comments and 0 CI runs. This was verified through five independent GitHub endpoints. **Therefore every dimension for every member is NR (no in-window evidence), and every overall score is NR.** This is a rest day, not a performance result; a low score would be a fabrication.
2. **No volume is ever scored.** Commit, PR, ticket, line and session counts are used only to describe the *kind* of work.
3. **Devin session telemetry is unavailable for the twelfth consecutive run** — `devin_session_search` returns HTTP 403 `Missing required permission 'org.sessions.view'`. "Observable Devin Leverage" can only ever be assessed here from commit trailers, `devin-ai-integration[bot]` PR authorship and Devin Review events. Sessions that produced no commit are invisible.
4. **Jira, Sentry and Microsoft Teams data are unavailable** (no callable tool / no token), so ticket hygiene, incident response and coordination work are unobservable.
5. **Attribution is imperfect.** Commits under `amit.p@medicodio.ai`, `hitesh.ms@medicodio.ai` and the branch identity `claude` are not linked to their GitHub logins, so those members' real contribution and Devin leverage are split across identities.
6. **Weekend/rest-day cards must not be trended against weekday cards.** Comparing an NR day to a scored weekday is meaningless.

## Rubric

| Dimension | Weight | 1–4 (Needs Support) | 5–6 (Mixed) | 7–8 (Solid) | 9–10 (Strong) |
| --------- | -----: | ------------------- | ----------- | ----------- | ------------- |
| Delivery & Follow-Through | 25 | Work started and abandoned; PRs left open without owner | Work lands but with stalls | Work lands within its window; open items are tracked | Work lands with follow-ups explicitly named and closed |
| Engineering Rigor | 25 | No tests; unverified assumptions | Tests present but shallow or mocked away | Tests cover the changed behaviour; failure modes named | Root causes named and fixed; wrong tests corrected |
| Code Review Contribution | 15 | No reviews, or content-free approvals | Reviews with little substance | Reviews that find real issues | Architect-level reviews with verdicts and verified findings |
| Observable Devin Leverage | 15 | No delegation where it clearly applied | Occasional, unscoped use | Bounded delegation with review of output | Delegation plus adversarial verification of Devin findings |
| Automation of Repetitive Work | 10 | Repeats manual work identified previously | Aware but manual | Automates part of own repetitive work | Builds automation others use |
| Consistency Across Windows | 10 | Erratic | Uneven | Steady across day/week/month | Steady and improving |

**Bands:** Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5 · **NR** = fewer than three rated dimensions (a dimension with no in-window evidence is NR and excluded from the weighted average).

## Summary grid — 2026-08-31

All dimensions are NR because the window has no in-window evidence for anyone. "Last observed activity" is Observed Fact and is provided so the reader can see who was recently active; it is **not** a score.

| Member | Product | Overall | Band | Delivery | Rigor | Review | Devin | Automation | Consistency | Confidence | Last observed activity (UTC) |
| ------ | ------- | ------- | ---- | -------- | ----- | ------ | ----- | ---------- | ----------- | ---------- | ---------------------------- |
| SaijyotiMeti | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-29 06:56 |
| anirudh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-29 16:01 |
| Amrutha-Beedikar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-29 16:09 |
| akanksh-rv | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-29 06:52 (branch) |
| svh-medicodio | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-28 13:46 |
| ragha82 | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-27 18:22 |
| Pj-Vineeth-Kumar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-27 13:36 |
| sameer-s-mansur | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-28 12:59 |
| jatinkushwaha-medicodio | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-28 10:21 |
| amit-pandey-medicodio | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-28 11:11 |
| NandanDate-Medicodio | Medicodio / Global Codio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-28 11:18 |
| avinash-codio | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-28 09:36 |
| vishnu-saikarthik | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-28 11:13 |
| hitesh (`hitesh.ms@medicodio.ai`) | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-26 14:41 |
| Medicodio-Amit | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-27 11:41 |
| sumedh-codio | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-27 13:15 |
| Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-27 05:14 |
| shaheen-khan11 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-24 06:11 |
| ANANYANG8055 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-25 12:34 |
| Murali-Shetty19 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | None in-window | 2026-08-14 09:53 (commit); PR #382 open since 08-21 |

**Dimension means:** not computable — every dimension is NR for every member.

## Cards

Cards are written only for the members who carried open work into the window, because that is the only member-linked fact the window contains. Every score below is NR; the text records state, not judgement.

### ragha82 — Global Codio — Overall **NR**

- **Observed Fact:** no in-window activity. #1250 (open since 08-27) and #1259 (open since 08-28) sat unattended; both have a Devin Review bot review and no human verdict.
- **Observed Fact (context, not scored):** 6 commits in the week window, 24 in the month, 4 of them Devin-trailered; the 08-21 report credits him with the CI gates and auto-merge-on-green automation.
- **Recommendation:** extend his own CI automation with a scheduled unreviewed/stale-PR report.

### svh-medicodio — Global Codio — Overall **NR**

- **Observed Fact:** no in-window activity. #1258 (closed/archived case read-only) open since 08-28 with bot review only.
- **Observed Fact (context):** 44 commits in the week, 141 in the month, 0 Devin-trailered.
- **Recommendation:** delegate the state-guard test matrix to Devin as a first bounded session.

### Pj-Vineeth-Kumar — Global Codio — Overall **NR**

- **Observed Fact:** no in-window activity. #1257 (file-number findability) open since 08-28 with bot review only.
- **Observed Fact (context):** 36 commits in the week, 10 of them Devin-trailered — third-highest Devin share in the week.
- **Recommendation:** delegate generated search-parity tests for every displayed identifier.

### akanksh-rv — Global Codio — Overall **NR**

- **Observed Fact:** no in-window activity. `feat/ai-cm-draft-support-letter-skill` stands at ~12 numbered phases, last commit 08-29 06:52, **no PR** and therefore no review surface; its commits are attributed to the unlinked identity `claude`.
- **Observed Fact (context):** 115 commits in the week, 416 in the month, 0 Devin-trailered; his #1260 merged on 08-29 as a 161-file PR.
- **Recommendation:** open the branch as a draft PR now so gates and Devin Review run per phase.

### Medicodio-Amit — Medicodio — Overall **NR**

- **Observed Fact:** no in-window activity. Engine #411 open since 08-27 (bot review only); #393 in **draft** since 08-25 with no reviews at all.
- **Observed Fact (context):** 7 commits in the week, 65 in the month, 1 Devin-trailered.
- **Recommendation:** mark #393 ready or close it; delegate per-row KB fixtures for #411.

### amit-pandey-medicodio — Medicodio — Overall **NR**

- **Observed Fact:** no in-window activity. Integration #249 open since 08-27 with **six** Devin Review bot passes and no human verdict; #248 open since 08-26.
- **Observed Fact (context):** the org's highest Devin-trailer share — 19 of 19 week commits and 38 of 40 month commits under `amit.p@medicodio.ai` carry `Co-Authored-By: Devin AI`, plus 37 week / 200 month commits under his login.
- **Recommendation:** link the email to his GitHub account, and require a human verdict before a third bot pass.

### Murali-Shetty19 — Medicodio — Overall **NR**

- **Observed Fact:** no in-window activity. Engine #382 "Testing ortho" open since 08-21 (10 days), last updated 08-25, three bot passes, no human review.
- **Observed Fact (context):** 1 commit in the month window (08-14), 0 Devin trailers.
- **Recommendation:** close #382 or restate it with a purpose and acceptance criteria.

## How to read the spread

- **Observed Fact.** There is no spread to read for 2026-08-31. Every member is NR because the 24-hour window contains no commits, PRs, reviews, comments or CI runs in any product repository — the last push to any product repo was 2026-08-29T17:00:32Z. The only in-window commits anywhere in the organization came from this reporting automation and its companion remediation automation in `Mgmt_Reports`.
- **Inference.** A Sunday of no activity, following a Saturday on which four people finished two features and a Friday of normal throughput, reads as rest. It is not evidence of disengagement for any individual, and no negative pattern is attributed to a person from this window. The only member-linked signal available is *state left open*: eleven product PRs, all of which have automated review coverage and none of which has a human verdict.
- **Recommendation.** Do not average this date into any per-person trend — the correct arithmetic treatment of an NR day is exclusion, not zero. Use the day for the three items that need no engineer's keyboard: make `Mgmt_Reports` private, assign named reviewers to the eleven open PRs, and grant `org.sessions.view` so that the next set of cards can score Devin leverage from session telemetry instead of commit trailers.

---

*Companion to `2026_08_31_Mgmt_Activity_Report.md`. Scores are NR for this review date by rule, not by judgement.*

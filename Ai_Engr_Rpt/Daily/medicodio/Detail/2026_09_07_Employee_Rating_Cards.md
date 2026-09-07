# Employee Rating Cards — 2026-09-07

**Review window:** Sunday 2026-09-06 03:00 UTC → Monday 2026-09-07 03:00 UTC. Comparison windows: previous day (09-05 → 09-06, Saturday), previous working day (09-04 → 09-05), week (08-30 → 09-06), month (08-07 → 09-06). Companion to `2026_09_07_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

- **Devin session telemetry is unavailable.** `devin_session_search` returned HTTP 403 (`org.sessions.view` missing) for the 15th consecutive run. "Observable Devin Leverage" is scored only from GitHub artefacts: Devin Review findings and how they were dispositioned, `devin-ai-integration[bot]` QA-gate comments and PRs, and commit trailers. Prompt quality, scoping, ACU effort and correction loops cannot be assessed.
- **Weekend window.** One person (Global Codio) had observed activity; one further Global Codio member is rated only on the disposition of her own PR by others. Every Medicodio member and six Global Codio members are **NR** on all dimensions. Do not compare today's cards with weekday cards.
- **Attribution.** All 13 human commits are authored under `anirudh-medicodio`; `Claude-Session:` metadata on 12 of them is tool use, not an attribution gap (contrast 09-06).
- **Jira and Sentry** were not available; ticket flow and incident load are unscored.
- **Volume is not productivity.** Commit, file, PR and finding counts appear only as context. The 1,043-file `dev` sync merge is branch synchronisation and earns nothing.
- A dimension with no in-window evidence is **NR** and excluded from the weighted average; fewer than three rated dimensions → overall **NR**.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure; loose ends accumulate | Stalled or abandoned work; commitments not met |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR too large to review | Template body, no tests, inaccurate claims, findings ignored |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence, or substantive but non-independent | Empty/one-word approvals; rubber-stamping |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed | Findings ignored; Devin used where manual is faster |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

Bands: **Strong** ≥ 8 · **Solid** ≥ 7 · **Mixed** ≥ 5 · **Needs Support** < 5.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anirudh-medicodio | Global Codio | **6.6** | Mixed | 6.5 | 7.5 | 6.0 | 6.5 | 4.5 | 7.0 | Medium |
| Amrutha-Beedikar | Global Codio | **NR** | — | 3.0 | NR | NR | 3.5 | NR | NR | Low (2 dimensions rated) |
| ragha82, svh-medicodio, SaahilVishwakarma, akanksh-rv, SaijyotiMeti, Pj-Vineeth-Kumar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, weekend) |
| amit-pandey-medicodio, jatinkushwaha-medicodio, ashwinsk-medicodio, vishnu-saikarthik, afifashaikh007, Medicodio-Amit, sameer-s-mansur, avinash-codio, nandanchouhan-medicodio, sumedh-medicodio, Karthik Khatavkar, hitesh-medicodio, shaheen-medicodio | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity, weekend) |

Weighted overall = Σ(score × weight) / Σ(weights of rated dimensions). anirudh-medicodio: (6.5×25 + 7.5×25 + 6.0×15 + 6.5×15 + 4.5×10 + 7.0×10) / 100 = 6.6.

## anirudh-medicodio — Global Codio — Overall 6.6 (Mixed) — Confidence: Medium

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | `#1288` (open since 09-02) completed and merged to `dev`; deploy green; PRD/data-flow debt retired in the same PR. Against: merged with his own "one blocker survives" and six "need your decision" items unresolved and unwaived in writing; `#1278` `importSession` finding still without fix or waiver (5th report); `feat/document-catalog-samples` checkpointed at 84 files with no PR. |
| Engineering Rigor | 7.5 | Fail-open fix with named blast radius (~62 tokens), pool-pressure fix, gating on `templateMergeFields`, ADR-0045 raised, incident value recomputed by hand, full api + web gate run (13,771 + 2,801 tests) with two inherited failures separated and one fixed; honest disclosure that `ci.yml` is manual and that three tests were deliberately not written blind. Against: those three tests are still missing on a merged PR; Devin's new raw-token-in-reminders bug — in the gate he added — shipped unanswered. |
| Code Review Contribution | 6.0 | 12,151-char Architect/EM review with 5 inline threads and a 12-row Stop-and-Check table — the most thorough review artefact in the org this week, and it changed the code. Capped at 6 because it was not independent (he authored 11 of the PR's 12 commits), his approval was 0 characters, and he approved over his own written blocker 41 minutes later. |
| Observable Devin Leverage | 6.5 | Written adjudication of the six 09-02 Devin findings ("all six verified as real, zero false positives"); Devin credited for `a263b4223`; QA gate on his merge produced READY WITH KNOWN RISKS with `FN1288-4`. Against: three new Devin findings (19:46) unanswered at merge; no Devin delegation observable for the three specified tests. |
| Automation of Repetitive Work | 4.5 | Hand-finished a fourth colleague's PR this week; review-log commit (`76306d350`, 249 lines) repeated from 09-04; inherited-`dev`-failure fixes done on a feature branch again. Repetition is visible in his own commit messages ("stops the next cleanup pass…" 09-04) but no automation attempted. |
| Consistency Across Windows | 7.0 | Day Stable vs previous working day (same strengths, same weakness); week Stable (92 commits, 12 `test(`, 2 substantive reviews, 0 independent approvals received); month Consistent (659 commits, 76 `test(`, review depth improving, independence not). |

Inference: the review reads as a hand-off to the author; with the author absent on a Sunday he chose to ship. That may have been the right call, but no written decision exists on the PR, so the score reflects what is observable. Confidence Medium because session telemetry is missing and the decision rationale is not recorded.

## Amrutha-Beedikar — Global Codio — Overall NR — Confidence: Low

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 3.0 | Her `#1288` merged today — but 11 of its 12 commits, the review, the approval and the merge were another person's. No commit, comment or reply from her since 09-02 (4 days, 2 of them working days). Rated because the outcome of her own open PR is in-window evidence about follow-through. |
| Engineering Rigor | NR | No in-window work of hers to assess. (Her 09-02 PR body was called "exemplary" by the reviewer — noted as a Positive Pattern in the report; not scored today.) |
| Code Review Contribution | NR | No reviews in-window. |
| Observable Devin Leverage | 3.5 | Six Devin findings on her PR (09-02) were never answered by her and were closed by the reviewer's commits; the regression tests named for her on 09-03/09-04 were not delegated or written. |
| Automation of Repetitive Work | NR | No in-window evidence. |
| Consistency Across Windows | NR | Week: 1 commit, PR idle until finished by someone else; month: 31 commits, 2 `test(`. Not scored on a weekend with two rated dimensions. |

Overall **NR** — only two dimensions have in-window evidence (fewer than three). The two rated scores are recorded so the Repeat Pattern (findings unanswered on own PR, 09-03 → 09-07) is visible; they are not an overall judgement of a weekend.

## Members with no in-window evidence — NR on all dimensions

**Global Codio:** ragha82, svh-medicodio, SaahilVishwakarma, akanksh-rv, SaijyotiMeti, Pj-Vineeth-Kumar — Sunday; open PRs `#1314` (80 files), `#1316` (58), `#1312` (57), `#1295` (56), `#1284` (145) unchanged and unreviewed for a third day. See the 09-05 and 09-06 cards for their most recent weekday ratings.

**Medicodio:** amit-pandey-medicodio, jatinkushwaha-medicodio, ashwinsk-medicodio, vishnu-saikarthik, afifashaikh007, Medicodio-Amit, sameer-s-mansur, avinash-codio, nandanchouhan-medicodio, sumedh-medicodio, Karthik Khatavkar, hitesh-medicodio, shaheen-medicodio — no activity in any of the four repositories; `#429` prod promotion (4 unanswered Devin findings) unchanged. See the 09-05 cards for their most recent weekday ratings.

Tool identities (`devin-ai-integration[bot]`, `Devin AI`, `Claude`, `github-actions`) are not rated.

## How to read the spread

- **Observed Fact:** one rated card today. anirudh-medicodio's 6.6 combines the org's most rigorous review artefact (Rigor 7.5) with the org's least independent approval (Review 6.0) and a merge over his own written blocker (Delivery 6.5). Amrutha-Beedikar is NR overall: her only in-window evidence is that others completed her PR (Delivery 3.0, Devin 3.5). Everyone else is NR because it was a Sunday.
- **Observed Fact:** the Devin QA gate produced its first verdict in five days (READY WITH KNOWN RISKS) while `E2E_SUPERADMIN` still returned 401; the server send path it was meant to verify remains unverified.
- **Inference:** the same person is, for the fifth report running, the reviewer, the remediator and the approver on the day's merges. The quality of the review is not in question; the absence of a second reader is. Today's scores would rise by roughly a point on Review and Delivery if a second approver had signed off and the blocker decision had been written on the PR — neither requires more work, only a different sequence.
- **Inference:** Amrutha-Beedikar's low rated dimensions reflect a four-day silence on an open PR with Devin findings, not weekend inactivity; on 09-02 she wrote the best PR body the reviewer has seen. The gap is follow-through, not capability.
- **Recommendation:** for `dev` merges on Global Codio, require an approver who has not committed to the branch (> 25 % authorship disqualifies); when a reviewer declares a blocker, the PR carries a one-line written decision before approval. For Amrutha-Beedikar: open the `#1288` follow-up PR with the three specified tests delegated to Devin and answer the three 19:46 findings in-thread on Monday. For the org admin: grant `org.sessions.view`, reset `E2E_SUPERADMIN`, and make `Mgmt_Reports` private — all three are Repeat items and all three cap the confidence of every card in this file.

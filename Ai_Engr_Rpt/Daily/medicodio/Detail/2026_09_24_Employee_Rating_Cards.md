# Employee Rating Cards — 2026-09-24

**Review window:** 2026-09-23 03:00 UTC → 2026-09-24 03:00 UTC. Comparison windows: previous working day 09-22, week 09-16 → 09-23, month 08-24 → 09-23.
**Companion report:** `2026_09_24_Mgmt_Activity_Report.md` (evidence for every score below).

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable (22nd consecutive run).** `devin_session_search` returned HTTP 403 (`org.sessions.view` missing). Nobody's prompts, session count, tests requested, ACU effort or correction cycles were visible. **Observable Devin Leverage** is therefore scored only on how a member *consumed* GitHub-visible Devin artefacts (Devin Review threads resolved with linked commits or reasoned replies, Devin-authored PRs reviewed/merged/closed with reason). A low score means "no observable consumption", not "did not use Devin".
- **Jira and incident data:** not available. Coordination, support and investigation work that leaves no GitHub trace is unscored, not zero.
- **Volume is not productivity.** Commit, PR, line and review counts are never scored directly. Delivery is scored on closure and follow-through of scoped work; Rigor on tests, accurate PR bodies, dispositioned findings and reviewable size.
- **Review independence** is scored from the observed sequence (commits on branch → review → approval → merge). Whether the author asked for that remediation is not observable.
- **NR** = no in-window evidence for that dimension; excluded from the weighted average. Fewer than three rated dimensions → overall **NR**.
- Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**. Scores are for one working day against the week/month context; a single day never settles a trend.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; carried items closed | Work merged or materially advanced; minor loose ends | Progress without closure; carried items untouched | Stalled, abandoned without record, or merged with known verdicts ignored |
| Engineering Rigor | 25 | Tests + accurate PR body + findings addressed before merge; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, or unreviewable size |
| Code Review Contribution | 15 | Substantive, **independent** review that changes outcomes | Specific comments; approvals name what was checked | Substantive review but not independent, or approvals with minimal evidence | Empty/one-word approvals on PRs with open findings or >100 files |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reason/test | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin PRs closed without reason |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| amit-pandey-medicodio (Amit Prakhar Pandey) | Medicodio | **7.1** | Solid | 8 | 8 | 3 | 9 | 5 | 8 | Medium |
| akanksh-rv | Global Codio | **6.8** | Mixed | 7 | 7 | 6 | 8 | 5 | 7 | Medium |
| SaijyotiMeti | Global Codio | **6.3** | Mixed | 7 | 8 | 5 | 5 | 4 | 6 | Medium |
| Pj-Vineeth-Kumar | Global Codio | **6.3** | Mixed | 8 | 6 | NR | 5 | 4 | 7 | Medium |
| ashwinsk-medicodio | Medicodio | **6.2** | Mixed | 7 | 6 | NR | 6 | NR | 5 | Medium-Low |
| sameer-s-mansur | Medicodio | **6.1** | Mixed | 6 | 6 | NR | 8 | 4 | 6 | Medium |
| svh-medicodio | Global Codio | **6.1** | Mixed | 7 | 6 | NR | 5 | 5 | 7 | Medium |
| jatinkushwaha-medicodio | Medicodio | **5.5** | Mixed | 7 | 6 | 2 | NR | 4 | 7 | Medium |
| SaahilVishwakarma | Global Codio | **5.3** | Mixed | 6 | 6 | NR | 3 | NR | 5 | Medium-Low |
| anirudh-medicodio | Global Codio | **5.1** | Mixed | 7 | 6 | 3 | 3 | 4 | 5 | Medium |
| ragha82 | Global Codio | **4.5** | Needs Support | 5 | 6 | 2 | 3 | 5 | 5 | Medium |
| sumedh-codio (Sumedh Kaulgud) | Medicodio | **3.6** | Needs Support | 6 | 2 | 2 | NR | NR | 4 | Medium |
| avinash-codio | Medicodio | **3.3** | Needs Support | 5 | 3 | 2 | 2 | 3 | 4 | Medium |
| NandanDate-Medicodio | Medicodio | **2.9** | Needs Support | NR | NR | 2 | 3 | NR | 4 | Medium-Low |
| Amrutha-Beedikar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; `#1406` open day 2) |
| Medicodio-Amit | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; `#470` open day 2, 19 findings) |
| afifashaikh007, Vishnu Sai Karthik, Hitesh Shanthakumar, Karthik Khatavkar, Murali-Shetty19, shaheen-khan11, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; `#435` day 16) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | 20 PRs reviewed (~140 threads); 0 PRs opened; 4 closed unmerged by a member; no review on `#1420`/`#1421` |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions).

---

## amit-pandey-medicodio (Amit Prakhar Pandey) — Medicodio — **7.1 Solid** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** impersonation crash → PHI-key reset → auth-epoch guards → refresh-promise race, each merged to `Dev_1.0` and `release/prod_1.0` the same day; manual-chart EMR sections merged; App 2.0 UAT deploy workflow added. Deduction: `Dev_1.0` trigger failed on his `#664` merge and was not followed up. |
| Engineering Rigor | 8 | **Observed Fact:** "add overlapping key-load race case" test; bodies 1.1–1.5k on the fix PRs. Deduction: `#17`/`#18` sync PRs blank. |
| Code Review Contribution | 3 | **Observed Fact:** 0-char approvals on `#13` and `#16` — the only human reader on `application-2.0`. |
| Observable Devin Leverage | 9 | **Observed Fact:** Devin threads resolved before merge: `#589` 5/5, `#590` 4/4, `#588` 1/1, `#664` 2/2, `#665` 2/4. Best consumption in the org today. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 3 duplicate ladder pairs and 2 manual sync PRs (8th/9th this month); Crucible tooling perf work is automation of *his* AI loop, not of the team's repetition. |
| Consistency Across Windows | 8 | Day Improved; week Improving; month Improving. |

**Inference:** he is the reference for how Medicodio should consume Devin Review. **Recommendation:** hand the ladder/sync PRs to Devin and put text in the two `application-2.0` approvals.

## akanksh-rv — Global Codio — **6.8 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1414` closed and re-scoped as `#1420` (298 → 164 commits, `main` commits removed) and merged; `#1419` inbox-triage QA fixes opened. Deduction: still 281 files. |
| Engineering Rigor | 7 | **Observed Fact:** 8.8k body; specs updated for own contract changes; review-log gate table. Deduction: PR size; no Devin Review on it. |
| Code Review Contribution | 6 | **Observed Fact:** 9,580-char review on `#1415` with "[was: blocker — fixed in `<sha>`]" per finding — the most verifiable review of the week — but he had 12 commits on the branch and then approved and merged it. Not independent. |
| Observable Devin Leverage | 8 | **Observed Fact:** "Caught by verifying a Devin comment rather than taking it at face value" — finding used as a lead, verified, fixed, linked. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 4 hand-written review-log commits; gate table recorded manually. |
| Consistency Across Windows | 7 | Day Improved; week Improving; month Consistent. |

**Recommendation:** keep the review convention; give the approve button to someone with no commits on the branch.

## SaijyotiMeti — Global Codio — **6.3 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** closed real security gaps on three branches (firm predicate, CSS scoper, platform-tier authz, DELETE hole, API keys in logs) and both PRs merged. Deduction: yesterday's "post the 8 decision items on `#1403`" — no comment observed. |
| Engineering Rigor | 8 | **Observed Fact:** tests written for each fix class; ADRs; error codes catalogued; "repair two regressions my own tenancy and retry fixes introduced" and a retracted finding after reading `rbac.mdc` — she checks her own work. |
| Code Review Contribution | 5 | **Observed Fact:** two 10.9k/11.7k reviews — the largest in the org — followed by approval and merge of branches she had ~30 and ~25 commits on. Content 9, independence 2; scored in the middle. |
| Observable Devin Leverage | 5 | **Observed Fact:** 6/16 threads on `#1418`; `#1420` merged with **no Devin Review**. |
| Automation of Repetitive Work | 4 | **Observed Fact:** the same tenancy fix classes hand-applied on 4 branches in 2 days; 19-pass review run manually. |
| Consistency Across Windows | 6 | Day Stable; week Needs Attention (independence); month Consistent. |

**Recommendation:** turn the recurring findings into a Devin-generated CI spec pack; stop being the approver of branches you fixed.

## Pj-Vineeth-Kumar — Global Codio — **6.3 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#1418` (Paste & Generate, edit-access expiry, table styling, fonts, comment anchors) merged same day; 28 commits. |
| Engineering Rigor | 6 | **Observed Fact:** 14.5k body; tests for PDF capture. Deduction: 138 files / 96 commits; a `feat!` breaking change inside; six tenancy/security fixes supplied by the reviewer. |
| Code Review Contribution | NR | No reviews given. |
| Observable Devin Leverage | 5 | **Observed Fact:** 6/16 threads resolved; the Devin fix PR for his `#1405` QA (`#1411`) closed unmerged by a colleague, not re-applied visibly. |
| Automation of Repetitive Work | 4 | Second consecutive mega-PR needing external tenancy remediation. |
| Consistency Across Windows | 7 | Day Stable; week Stable; month Consistent. |

**Recommendation:** run the tenancy checks before opening; split the `!` change out.

## ashwinsk-medicodio — Medicodio — **6.2 Mixed** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#471` injury 7th-character fix merged to `uat`; `#472` uat→prod opened and merged 14 min later. |
| Engineering Rigor | 6 | **Observed Fact:** 2.5k body; `devin_fix:` follow-up commit. Deduction: 4/6 threads open at merge; prod promotion same minute. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 6 | **Observed Fact:** 2/6 threads resolved with a linked commit. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5 | Day Improved (0 → 2); week/month sporadic. |

## sameer-s-mansur — Medicodio — **6.1 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#318` Elaris El Paso onboarding open with two review-response rounds; not merged (appropriately). |
| Engineering Rigor | 6 | **Observed Fact:** 431-char body (thin for 18 files / +2,266); fixes are specific and named. Deduction: targets `release/prod_1.0` directly. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 8 | **Observed Fact:** 8/12 Devin threads resolved pre-merge with "Address review" commits. |
| Automation of Repetitive Work | 4 | Onboarding still hand-built; direct-to-prod for the 2nd day. |
| Consistency Across Windows | 6 | Day Improved; week Stable; month Consistent. |

## svh-medicodio — Global Codio — **6.1 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1415` merged (relevance gate, service-type catalog codes, a11y). Deduction: `#1403` NOT READY 48 still without disposition; its fix PR closed by a peer. |
| Engineering Rigor | 6 | **Observed Fact:** 16.2k body; tests for untested branches and a masking mock. Deduction: four concerns in one PR; the reviewer had to fix three blind spots in the gate. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 5 | **Observed Fact:** 8/21 threads resolved. |
| Automation of Repetitive Work | 5 | — |
| Consistency Across Windows | 7 | Day Stable; week Improving; month Consistent. |

## jatinkushwaha-medicodio — Medicodio — **5.5 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** payer-provenance refactor, debounce fix, Chatwoot revert merged; Performance Dashboard `#19` opened. |
| Engineering Rigor | 6 | **Observed Fact:** `#16` body 607 chars; `#15`, `#19` blank; no Devin Review on the repo. |
| Code Review Contribution | 2 | **Observed Fact:** six 0-char approvals incl. two prod hotfixes; two `Dev_1.0` trigger failures on his merges unaddressed. |
| Observable Devin Leverage | NR | No Devin artefacts on `application-2.0`; on `app-react` the threads were already closed by the author. |
| Automation of Repetitive Work | 4 | — |
| Consistency Across Windows | 7 | Day Stable; week/month Improving. |

## SaahilVishwakarma — Global Codio — **5.3 Mixed** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1416` party-attribution completion opened (62 files). Deduction: `#1391` verdicts day 6 unacknowledged. |
| Engineering Rigor | 6 | **Observed Fact:** fixture updated with route change; body is the unfilled template (8,950 chars). |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 3 | **Observed Fact:** 0/10 threads resolved. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5 | Day Improved from zero; week Stable. |

## anirudh-medicodio — Global Codio — **5.1 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1394` observability closed out (day 6) with HLD and 33 green gates; migration review process added. Deduction: `#1404` day 2 untouched; four Devin PRs discarded. |
| Engineering Rigor | 6 | **Observed Fact:** LLM cost-estimator tests, refusal-code tests, detector for the catalog. Deduction: `#1421` promotion body is the template. |
| Code Review Contribution | 3 | **Observed Fact:** 0-char approval + merge of `#1417` with 0/11 Devin threads resolved. |
| Observable Devin Leverage | 3 | **Observed Fact:** 14/35 threads on `#1394` resolved (good) — but `#1410`–`#1413` (two NOT READY QA reports and two fix PRs) closed at 08:46 with no comment, against yesterday's explicit action items. |
| Automation of Repetitive Work | 4 | Third promotion this week with a template body. |
| Consistency Across Windows | 5 | Day Regressed; week Needs Attention; month Consistent. |

## ragha82 — Global Codio — **4.5 Needs Support** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#1417` and `#1394` merged (the latter after a colleague's 23-commit fix pass); `#1362` `ACR_NAME` unactioned day 3 (unverifiable — Actions variables 403). |
| Engineering Rigor | 6 | **Observed Fact:** raw-SQL rule + detector shipped together; `assertCaseAccess` fix. Deduction: 0/11 Devin threads at merge. |
| Code Review Contribution | 2 | **Observed Fact:** approved and merged `#1421` (453 files, template body) 2 minutes after open with 0 characters. |
| Observable Devin Leverage | 3 | **Observed Fact:** `#1417` findings untouched. |
| Automation of Repetitive Work | 5 | Detector is automation; promotion approval is not. |
| Consistency Across Windows | 5 | Day Regressed; week Needs Attention; month Consistent. |

## sumedh-codio (Sumedh Kaulgud) — Medicodio — **3.6 Needs Support** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** four Trinity/export fixes and docs landed on `main`; retry-once feature on a branch. |
| Engineering Rigor | 2 | **Observed Fact:** `#26`–`#29` bodies 0/0/0/11 chars, self-merged within 60 s, no reviewer, no Devin Review. Commit messages themselves are excellent. |
| Code Review Contribution | 2 | **Observed Fact:** 0-char approvals on `#664`, `#665` (prod), `#17`. |
| Observable Devin Leverage | NR | Repo has no Devin Review. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4 | Day Regressed (1 → 4 self-merges); week Needs Attention; month Needs Improvement. |

## avinash-codio — Medicodio — **3.3 Needs Support** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#473` merged to `uat` and `#474` to `release/prod_3.0` — shipped, but with three open findings and no QA step. |
| Engineering Rigor | 3 | **Observed Fact:** one commit, 19 files, +5,588 mixing config, routing and a new skill; 890-char body. |
| Code Review Contribution | 2 | **Observed Fact:** merged `#472` uat→prod with 0 characters. |
| Observable Devin Leverage | 2 | **Observed Fact:** 0/3 threads resolved; second consecutive day of unanswered findings. |
| Automation of Repetitive Work | 3 | — |
| Consistency Across Windows | 4 | Day Regressed; week Needs Attention; month Needs Improvement. |

## NandanDate-Medicodio — Medicodio — **2.9 Needs Support** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | NR | No own PRs. |
| Engineering Rigor | NR | — |
| Code Review Contribution | 2 | **Observed Fact:** `#471` (4 chars), `#473` (5 chars), `#474` uat→prod (5 chars) — three merges, one to production one minute after the feature reached `uat`. |
| Observable Devin Leverage | 3 | **Observed Fact:** merged `#473` with 3 open Devin findings. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4 | One-word approvals every working day since 09-15. |

## Amrutha-Beedikar — Global Codio — **NR**
No events in the window. `#1406` open day 2 awaiting a reviewer. Yesterday's 7.0 stands as the last rated day.

## Medicodio-Amit — Medicodio — **NR**
No events in the window. `#470` open day 2 with 19 Devin findings still to split into fix/won't-fix.

## afifashaikh007, Vishnu Sai Karthik, Hitesh Shanthakumar, Karthik Khatavkar, Murali-Shetty19, shaheen-khan11, Shashvi1 — Medicodio — **NR**
No events in the window. `feat/inpatient-engine` had no commits today (15th report without a PR); `#435` open day 16 without a reviewer.

---

## How to read the spread

**Observed Fact.** Fourteen members rated; one Solid, nine Mixed, four Needs Support, nine NR for absence of events. The spread is driven by two dimensions: **Code Review Contribution** (every rated score ≤ 6; 23 of 26 human approvals were ≤ 10 characters and the three substantive reviews were by people who had committed to the branch) and **Observable Devin Leverage** (bimodal: 8–9 for amit-pandey, akanksh-rv and sameer; 2–3 where findings were merged unread or Devin PRs were closed without reason). Delivery scores are 5–8 across the board — the org ships.

**Inference.** The top of the grid is not the people who wrote the most (SaijyotiMeti wrote 60 commits and sits at 6.3; amit-pandey wrote 43 and leads at 7.1). It is the people who closed the loop with an independent reader — human or Devin — before merging. Where the band is Needs Support, the cause in every case is a *gate* behaviour (self-merge, one-word prod approval, findings unread), not the quality of the code itself; sumedh's commit messages are among the best in the org.

**Recommendation.** Two mechanical changes would move most Mixed scores to Solid without anyone writing more code: (1) branch protection that rejects an approval from anyone with commits on the branch, on Global Codio `dev` and Medicodio `uat`/`release/*`; (2) Devin Review installed on `rf-rpa-automation` and `application-2.0`, with a manual request on any PR over 250 files. Devin session telemetry (`org.sessions.view`) would let the Leverage column be scored on what was *asked* of Devin, not only on what was done with its answers.

# Employee Rating Cards — 2026-09-28

**Review window:** 2026-09-28 03:00 UTC → 2026-09-29 03:00 UTC (Monday). Comparison windows: previous working day Friday 09-25, week 09-21 → 09-28, month 08-29 → 09-28.
**Companion report:** `2026_09_28_Mgmt_Activity_Report.md` (evidence for every score below). Latest stored prior cards: 2026-09-24 (none stored for 09-25 → 09-27).

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable.** `devin_session_search` returned HTTP 403 (`org.sessions.view` missing), as on every prior recorded run. Nobody's prompts, session count, tests requested, ACU effort or correction cycles were visible. **Observable Devin Leverage** is scored only on how a member *consumed* GitHub-visible Devin artefacts (Devin Review threads resolved, or dispositioned with reasons in a review; Devin PRs handled). A low score means "no observable consumption", not "did not use Devin". Most AI-assisted authoring today is Claude-co-authored (188/245 commits), which is not scored as Devin leverage.
- **Jira and incident data:** not available. Coordination, support and investigation work without a GitHub trace is unscored, not zero.
- **Volume is not productivity.** Commit, PR, line and review counts are never scored directly.
- **Review independence** is scored from the observed sequence (reviewer commits → review → approval → merge). Decisions given outside GitHub are not observable.
- **NR** = no in-window evidence; excluded from the weighted average. Fewer than three rated dimensions → overall **NR**.
- Bands: **Strong ≥ 8**, **Solid ≥ 7**, **Mixed ≥ 5**, **Needs Support < 5**. One working day against week/month context; a single day never settles a trend.

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
| akanksh-rv | Global Codio | **6.7** | Mixed | 7 | 7 | 5 | 8 | 5 | 7 | Medium |
| svh-medicodio | Global Codio | **6.6** | Mixed | 8 | 6 | NR | 5 | NR | 7 | Medium |
| Medicodio-Amit | Medicodio | **6.4** | Mixed | 6 | 7 | NR | 6 | NR | NR | Low |
| SaahilVishwakarma | Global Codio | **6.3** | Mixed | 7 | 7 | NR | 4 | NR | 6 | Medium-Low |
| Pj-Vineeth-Kumar | Global Codio | **6.1** | Mixed | 7 | 6 | NR | 5 | NR | 6 | Medium-Low |
| sameer-s-mansur | Medicodio | **6.1** | Mixed | 7 | 6 | NR | 7 | 3 | 6 | Medium |
| SaijyotiMeti | Global Codio | **6.0** | Mixed | 7 | 7 | 4 | 6 | 4 | 6 | Medium |
| ANANYANG8055 | Medicodio | **5.9** | Mixed | 7 | 6 | NR | 4 | NR | NR | Low |
| amit-pandey-medicodio (Amit Prakhar Pandey) | Medicodio | **5.8** | Mixed | 7 | 5 | 3 | 8 | 5 | 6 | Medium |
| jatinkushwaha-medicodio | Medicodio | **5.4** | Mixed | 7 | 6 | 2 | NR | 4 | 6 | Medium |
| anirudh-medicodio | Global Codio | **5.3** | Mixed | 6 | 6 | NR | 4 | 4 | 5 | Medium |
| Amrutha-Beedikar | Global Codio | **5.3** | Mixed | 7 | 5 | NR | 4 | 4 | NR | Medium-Low |
| Vishnu Sai Karthik | Medicodio | **5.3** | Mixed | 7 | 5 | NR | 3 | NR | NR | Low |
| avinash-codio | Medicodio | **4.6** | Needs Support | 6 | 4 | NR | 5 | 3 | 4 | Medium |
| afifashaikh007 | Medicodio | **3.6** | Needs Support | 4 | 3 | NR | NR | NR | 4 | Medium-Low |
| sumedh-codio (Sumedh Kaulgud) | Medicodio | **3.5** | Needs Support | 6 | 2 | 2 | NR | NR | 3 | Medium |
| NandanDate-Medicodio | Medicodio | **2.3** | Needs Support | NR | NR | 2 | 2 | NR | 3 | Medium-Low |
| ragha82 | Global Codio | NR | — | NR | NR | 2 | NR | NR | 4 | — (2 rated dimensions: approvals only) |
| Hitesh Shanthakumar | Medicodio | NR | — | 5 | 6 | NR | NR | NR | NR | — (2 rated; `#27` open, no Devin Review on repo) |
| ashwinsk-medicodio | Medicodio | NR | — | 5 | 6 | NR | NR | NR | NR | — (2 rated; POC branch, no PR) |
| Karthik Khatavkar, Murali-Shetty19, shaheen-khan11, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no events; `#435` day 20) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | Reviewed 31 of 47 touched PRs (154 threads); 0 Devin-authored PRs today; no review on `#1428`, `#1431`, `application-2.0`, `rf-rpa-automation` |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions).

---

## akanksh-rv — Global Codio — **6.7 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1406`, `#1416`, `#1432` reviewed, remediated and merged. Deduction: `#1406` merged with operator decision D1 open. |
| Engineering Rigor | 7 | **Observed Fact:** fixes pinned with specs ("controller spec pinning the split"); SHAs cited per fix. |
| Code Review Contribution | 5 | **Observed Fact:** 13.1k / 8.0k / 5.1k reviews that changed outcomes — but 39 own commits on those branches, then approve + merge. Not independent. |
| Observable Devin Leverage | 8 | **Observed Fact:** "adversarially verified all 10 Devin comments" on `#1432`; 3 false positives documented with reasons. Deduction: threads left unresolved (7/19). |
| Automation of Repetitive Work | 5 | **Observed Fact:** dispositions copied by hand into review bodies. |
| Consistency Across Windows | 7 | Day Improved; week Stable; month Consistent. |

**Inference:** the org's best Devin consumer on Global Codio. **Recommendation:** have a zero-commit colleague approve, and resolve threads with the dispositions already written.

## svh-medicodio — Global Codio — **6.6 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#1429` (SP-1.2) and `#1432` (personal email send) merged. |
| Engineering Rigor | 6 | **Observed Fact:** 229-file PR; reviewer called the `#1429` body stale/false at head; retroactive PRD on `#1432`. |
| Code Review Contribution | NR | No reviews in window. |
| Observable Devin Leverage | 5 | **Observed Fact:** 3/16 and 7/19 threads resolved; dispositions done by reviewers. |
| Automation of Repetitive Work | NR | No repetitive work attributable. |
| Consistency Across Windows | 7 | Day Improved; week Improving; month Consistent. |

## Medicodio-Amit — Medicodio — **6.4 Mixed** — Confidence: Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#475` merged to `uat`; `#470` open day 6 with no events. |
| Engineering Rigor | 7 | **Observed Fact:** 3k body, 8 files. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 6 | **Observed Fact:** 4/6 threads resolved. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | NR | Insufficient history. |

## SaahilVishwakarma — Global Codio — **6.3 Mixed** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1416` merged after 5 days; R16 decision still open. |
| Engineering Rigor | 7 | **Observed Fact:** reviewer: "description is thorough… reuse-before-creation evidence checks out". 127 files. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4 | **Observed Fact:** 4/18 resolved; Devin 🔴/🟥 items fixed by the reviewer, not the author. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 6 | Day Improved; week Stable; month Consistent. |

## Pj-Vineeth-Kumar — Global Codio — **6.1 Mixed** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1426` merged (by SaijyotiMeti) with OD2/OD5 open. |
| Engineering Rigor | 6 | **Observed Fact:** 19.5k body; security defects (origin check, unaudited logo writers) found and fixed by reviewer. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 5 | **Observed Fact:** 5/15 resolved. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 6 | Day Regressed; week Stable; month Consistent. |

## sameer-s-mansur — Medicodio — **6.1 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** Gilbert/Ohio/pairing fixes shipped to prod. Deduction: UAT port `#332` still open. |
| Engineering Rigor | 6 | **Observed Fact:** bodies 430–660 chars; prod before UAT. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 7 | **Observed Fact:** 9/9 on `#326`, 2/2 on `#331`; 0/3, 0/2 on dev ports. |
| Automation of Repetitive Work | 3 | **Observed Fact:** 10 hand-made port PRs. |
| Consistency Across Windows | 6 | Day Improved; week Stable; month Consistent. |

## SaijyotiMeti — Global Codio — **6.0 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1426`, `#1429` merged; own `#1427` advanced. |
| Engineering Rigor | 7 | **Observed Fact:** parity spec, `stepId` PII pin, ADR-0066, SHAs cited. |
| Code Review Contribution | 4 | **Observed Fact:** 10.4k / 8.1k reviews marked REQUEST CHANGES, then "approved" 8 and 4 min later with owner decisions open; 51 own commits on those branches. |
| Observable Devin Leverage | 6 | **Observed Fact:** Devin #2/#3 verified and fixed; threads 5/15, 3/16, 7/23. |
| Automation of Repetitive Work | 4 | **Observed Fact:** same tenancy/auth classes hand-fixed again. |
| Consistency Across Windows | 6 | Day Stable; week Stable; month Consistent. |

**Inference:** the quality of her reviews is the highest in the org; the score is held down by the gate sequence, not the content.

## ANANYANG8055 — Medicodio — **5.9 Mixed** — Confidence: Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#476` otolaryngology onboarding merged to `uat`. |
| Engineering Rigor | 6 | **Observed Fact:** 1.8k body, 18 files. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4 | **Observed Fact:** 2/6 resolved. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | NR | First observed contribution. |

## amit-pandey-medicodio (Amit Prakhar Pandey) — Medicodio — **5.8 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#327` prompt registry, `#25`, `#23`; App 2.0 first prod build succeeded. |
| Engineering Rigor | 5 | **Observed Fact:** `#327` self-merged with template body; `#23` 71 files, blank body; no PR observed into `release/prod_2.0`. |
| Code Review Contribution | 3 | **Observed Fact:** five 0-char approvals, two on prod (`#330`, `#331`). |
| Observable Devin Leverage | 8 | **Observed Fact:** 12/16 threads resolved on `#327` before merge. |
| Automation of Repetitive Work | 5 | **Observed Fact:** promotion bodies still manual/blank. |
| Consistency Across Windows | 6 | Day Stable; week Stable; month Improving. |

## jatinkushwaha-medicodio — Medicodio — **5.4 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#26`, `#28` merged. |
| Engineering Rigor | 6 | **Observed Fact:** bodies 1.4–3k; no tests visible in titles. |
| Code Review Contribution | 2 | **Observed Fact:** 0-char approvals on `#326` (prod), `#23` (71 files, blank body), `#25`. |
| Observable Devin Leverage | NR | No Devin Review on `application-2.0`. |
| Automation of Repetitive Work | 4 | **Observed Fact:** manual promotions. |
| Consistency Across Windows | 6 | Stable / Stable / Consistent. |

## anirudh-medicodio — Global Codio — **5.3 Mixed** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1430` advanced (open); `#1404` day 7; `#1431` opened and merged. |
| Engineering Rigor | 6 | **Observed Fact:** 12.7k body; 124-file PR; `#1431` 668 files with template body. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4 | **Observed Fact:** 1/9, 0/4 (day 7); no disposition for `#1410`–`#1413`. |
| Automation of Repetitive Work | 4 | **Observed Fact:** template promotion body again. |
| Consistency Across Windows | 5 | Stable / Stable / Consistent. |

## Amrutha-Beedikar — Global Codio — **5.3 Mixed** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1406` merged; `#1428` production promotion merged and deployed. |
| Engineering Rigor | 5 | **Observed Fact:** reviewer asked for a `#1406` description rewrite; `#1428` template body. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4 | **Observed Fact:** 1/6 on `#1406`. |
| Automation of Repetitive Work | 4 | **Observed Fact:** promotion body manual/template. |
| Consistency Across Windows | NR | Insufficient history. |

## Vishnu Sai Karthik — Medicodio — **5.3 Mixed** — Confidence: Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#479` merged. |
| Engineering Rigor | 5 | **Observed Fact:** small focused PR; findings unanswered. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 3 | **Observed Fact:** 0/6 resolved. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | NR | Insufficient history. |

## avinash-codio — Medicodio — **4.6 Needs Support** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** time-based prediction and two config changes shipped to prod. |
| Engineering Rigor | 4 | **Observed Fact:** three prod promotions 1–3 min after `uat`; 422-char template bodies. Credit: `#477` 2.1k body. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 5 | **Observed Fact:** 3/3 on `#477` and `#481`; 0/8 on `#478`, 0/5, 0/2. |
| Automation of Repetitive Work | 3 | **Observed Fact:** manual promotions. |
| Consistency Across Windows | 4 | Improved / Needs Attention / Needs Improvement. |

## afifashaikh007 — Medicodio — **3.6 Needs Support** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4 | **Observed Fact:** 13 commits; `feat/inpatient-engine` still has no PR (16th report). |
| Engineering Rigor | 3 | **Observed Fact:** 1,172 unreviewed commits on the branch. Credit: explanatory commit messages. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4 | Stable, but the carried item is untouched. |

## sumedh-codio (Sumedh Kaulgud) — Medicodio — **3.5 Needs Support** — Confidence: Medium

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** 7 RPA fixes merged. |
| Engineering Rigor | 2 | **Observed Fact:** bodies 0–12 chars; merged 0–2 min after open; no review. |
| Code Review Contribution | 2 | **Observed Fact:** 0-char approvals on integration `#325`, `#328`. |
| Observable Devin Leverage | NR | No Devin Review on repo. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 3 | Stable / Needs Attention / Needs Improvement. |

**Inference:** a gate problem, not a code-quality problem — his commit messages are among the clearest in the org.

## NandanDate-Medicodio — Medicodio — **2.3 Needs Support** — Confidence: Medium-Low

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | NR | No authored work. |
| Engineering Rigor | NR | — |
| Code Review Contribution | 2 | **Observed Fact:** 9 approvals of 4–5 chars, 3 to prod. |
| Observable Devin Leverage | 2 | **Observed Fact:** merged with 0/8, 0/6, 0/5 threads open. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 3 | Stable / Needs Attention / Needs Improvement. |

## ragha82 — Global Codio — **NR**

Only two dimensions have evidence: Code Review Contribution **2** (0-char approvals on `#1428` — 453 files to production — and `#1431`, 668 files) and Consistency **4**. No authored work in window (4 commits Friday). Overall NR by rule; the observed gate behaviour is carried in the management report.

## Hitesh Shanthakumar — Medicodio — **NR**

Delivery 5 (`#27` ICD versioning open; inpatient branch without PR), Rigor 6 (self-audit and revert before review). Devin, Review, Automation, Consistency have no evidence. Overall NR.

## ashwinsk-medicodio — Medicodio — **NR**

Delivery 5 (POC `icd_index_agent` iterations, no PR), Rigor 6 (49-chart results documented). Other dimensions no evidence. Overall NR.

## Karthik Khatavkar, Murali-Shetty19, shaheen-khan11, Shashvi1 — Medicodio — **NR**

No in-window events. Engine `#435` (Murali-Shetty19) open day 20 without reviewer.

---

## How to read the spread

**Observed Fact.** Seventeen members rated: none Strong or Solid, thirteen Mixed, four Needs Support; five individually NR plus four with no events. The top score (6.7) is lower than 09-24's (7.1). Two dimensions drive the spread: **Code Review Contribution** (every rated score ≤ 5; 26 of 31 human approvals ≤ 10 characters; the five substantive reviews were all by reviewers who had committed to the branch and then merged it, three of them over their own "REQUEST CHANGES") and **Observable Devin Leverage** (8 for akanksh-rv and amit-pandey, 7 for sameer; 2–4 where findings were merged unanswered). Delivery is 6–8 for everyone with authored work.

**Inference.** Global Codio's reviews have never been more thorough — dispositions, verified Devin false positives, PRD conformance tables — yet no Global Codio feature merged today had an independent approver, and the production promotion had none at all. Medicodio's weakest scores are again gate behaviours (self-merge, one-word prod approvals, minute-long UAT), not code quality. The drop at the top reflects gate behaviour on production paths (`#1428`, `#330`/`#331`, `#478`), not less delivery.

**Recommendation.** (1) Branch protection that rejects an approval from anyone with commits on the branch (Global Codio `dev`/`main`; Medicodio `uat`/`release/*`), and a required "decision recorded" checkbox when a review says REQUEST CHANGES. (2) Devin Review on `rf-rpa-automation`, `application-2.0` and every promotion PR, with a Devin readiness report cited in the promotion approval. (3) Grant `org.sessions.view` so the Devin column can reflect what was *asked* of Devin, not only how its review output was consumed.

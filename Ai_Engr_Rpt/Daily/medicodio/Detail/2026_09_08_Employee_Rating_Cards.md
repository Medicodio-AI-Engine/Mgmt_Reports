# Employee Rating Cards — 2026-09-08

**Review window:** 2026-09-07 03:00 UTC → 2026-09-08 03:00 UTC (Monday). Companion to `2026_09_08_Mgmt_Activity_Report.md`.

## Scoring limitations (read before the numbers)

- **Devin session telemetry is missing.** `devin_session_search` returned `403 Missing required permission 'org.sessions.view'`. "Observable Devin Leverage" is scored only from GitHub artefacts (Devin co-author trailers, Devin-opened PRs, Devin Review finding dispositions, QA-gate comments). Prompt quality, ACU effort, delegation breadth and correction burden are **not observable** and are not scored.
- **Jira and Sentry are unavailable.** Coordination, support and incident work leave no trace here unless mentioned in a PR.
- **Volume is not productivity.** Commit, PR, file and line counts appear only as context for what was reviewed. A member with 2 commits and a written finding disposition can outscore one with 30 commits and none.
- **Branch-only work** (no PR) is scored on what commits show, with Rigor capped because nothing has been reviewed.
- **NR** = no in-window evidence for that dimension; NR dimensions are excluded from the weighted average. Fewer than three rated dimensions → overall **NR**.
- Bands: Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5.
- Identity mapping: `NandanDate-Medicodio` = prior reports' `nandanchouhan-medicodio`; `sumedh-codio` = `sumedh-medicodio`; `anirudh.hanchinamani` commits = `anirudh-medicodio`; `vineeth.kumar` = `Pj-Vineeth-Kumar`.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure; loose ends accumulate | Stalled or abandoned work; commitments not met |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR too large to review | Template body, no tests, inaccurate claims, findings ignored |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence, or substantive but non-independent | Empty/one-word approvals; rubber-stamping |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed | Findings ignored; Devin used where manual is faster |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Medicodio-Amit | Medicodio | **7.3** | Solid | 7.5 | 7.5 | NR | 8.5 | 5.0 | 7.0 | High |
| anirudh-medicodio | Global Codio | **7.1** | Solid | 8.0 | 7.5 | 4.5 | 8.5 | 5.0 | 7.5 | High |
| Amrutha-Beedikar | Global Codio | **7.0** | Solid | 6.5 | 7.0 | NR | 8.0 | NR | 6.5 | Medium |
| amit-pandey-medicodio | Medicodio | **6.4** | Mixed | 8.0 | 7.0 | 3.0 | 7.0 | 5.0 | 6.5 | High |
| jatinkushwaha-medicodio | Medicodio | **6.2** | Mixed | 7.5 | 7.0 | 3.0 | 7.0 | 4.5 | 6.5 | High |
| sameer-s-mansur | Medicodio | **6.2** | Mixed | 7.5 | 6.5 | NR | 5.0 | 4.5 | 6.0 | High |
| afifashaikh007 | Medicodio | **6.2** | Mixed | 6.0 | 6.5 | NR | NR | 5.5 | 6.5 | Medium |
| svh-medicodio | Global Codio | **6.0** | Mixed | 5.5 | 7.0 | NR | 5.0 | 5.5 | 6.5 | High |
| ragha82 | Global Codio | **6.0** | Mixed | 5.0 | 7.0 | NR | NR | 6.0 | 6.0 | Medium |
| sumedh-codio | Medicodio | **5.5** | Mixed | 6.5 | 6.0 | 2.5 | NR | 6.0 | NR | Medium |
| SaahilVishwakarma | Global Codio | **5.3** | Mixed | 6.0 | 6.5 | 2.5 | 5.0 | 5.0 | NR | Medium |
| Pj-Vineeth-Kumar | Global Codio | **5.2** | Mixed | 5.0 | 5.5 | NR | NR | 5.0 | 5.0 | Medium |
| vishnu-saikarthik | Medicodio | **5.1** | Mixed | 6.0 | 5.0 | NR | 3.5 | NR | 5.5 | Medium |
| avinash-codio | Medicodio | **3.9** | Needs Support | 5.5 | 3.0 | NR | 2.5 | NR | 4.0 | Medium |
| NandanDate-Medicodio | Medicodio | **2.9** | Needs Support | NR | NR | 2.5 | 3.0 | NR | 3.5 | High |
| Murali-Shetty19 | Medicodio | NR | — | 5.5 | 5.0 | NR | NR | NR | NR | Low (2 dimensions) |
| ashwinsk-medicodio | Medicodio | NR | — | NR | NR | 2.5 | 3.5 | NR | NR | Low (2 dimensions) |
| SaijyotiMeti, akanksh-rv, hiteshjrxmedicodio, shaheen-khan11, Karthik Khatavkar | — | NR | — | NR | NR | NR | NR | NR | NR | — (no in-window activity) |

Overall = Σ(score × weight) / Σ(weights of rated dimensions), rounded to one decimal.

---

## Medicodio-Amit — Medicodio — 7.3 Solid

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#425` (open since 09-03, 54 files) merged to `uat` 13:03 and promoted to prod (`#433`) 14:05; spec, invariants and config sync included. Against: `#393` (agentic memory) open since 08-25. |
| Engineering Rigor | 7.5 | Canonical Stage-0 `spec.md` + INVARIANTS; line-level conservation invariant; guard fixes with RCA in messages; 19 written dispositions. Against: PR is 5k lines; no new test commit visible today. |
| Code Review Contribution | NR | Reviewed no one else's PR. (His replies on his own PR are counted under Devin.) |
| Observable Devin Leverage | 8.5 | 19 inline dispositions on Devin findings — fix SHA, "by design" with reason, "acknowledged, not changed here" with convention cited; 9 auto-resolved. Against: 6 new findings on the prod PR `#433` unanswered before merge. |
| Automation of Repetitive Work | 5.0 | Manual `client_configs`/prompt seed sync (`7716da7b`); repetition acknowledged in the commit, not automated. |
| Consistency Across Windows | 7.0 | Day Improved (from 4 unanswered findings on 09-04); week Improving; month Consistent. |

## anirudh-medicodio — Global Codio — 7.1 Solid

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | `#1314` completed and merged; `#1284` advanced 32 commits; `#1329`/`#1330` promoted and prod deploy 5/5 green; `#1321` regression PR raised and iterated. Against: `#1320` is a draft of someone else's uncommitted work. |
| Engineering Rigor | 7.5 | Gate failures closed at root, RBAC log updated, ADR raised, tests repaired and added (6 `test(` commits), retest evidence on `#1321`. Against: 776-file promotion merged 10 min after open; self-approval of a 12k-line PR he rewrote. |
| Code Review Contribution | 4.5 | Only approval was 0-char on his own rewrite of `#1314`; no independent review given. Inference: rigor was delivered as authorship, not review. |
| Observable Devin Leverage | 8.5 | `#1321`: Devin-opened PR, 13 commits with trailers, every finding answered with SHA or reasoned rejection, browser retest posted. 18 trailers today. Against: the same technique not used on `#1314`/`#1284`. |
| Automation of Repetitive Work | 5.0 | 5th colleague PR hand-finished this fortnight; 6 `docs(review)` ledger commits by hand; promotion bodies pasted. Repetition evident, `#1321` shows the automated alternative exists. |
| Consistency Across Windows | 7.5 | Day Improved (Devin delegation); week Improving; month Improving on Devin, Consistent on hand-finishing. |

## Amrutha-Beedikar — Global Codio — 7.0 Solid

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | `#1323` opened 17:36 and fixed 18:02; not merged; 4 new findings pending. Removes 1,834 lines of duplicated UI. |
| Engineering Rigor | 7.0 | 10k-char body with Why/UX rationale; regression she introduced found and fixed same hour. Against: no test commit. |
| Code Review Contribution | NR | None given. |
| Observable Devin Leverage | 8.0 | Written 6-row disposition table naming each finding's outcome — the practice recommended to her on 09-04/09-07, now done. 4 later findings not yet answered. |
| Automation of Repetitive Work | NR | No evidence. |
| Consistency Across Windows | 6.5 | Day Improved sharply; week Improving from a 4-day silence; month Consistent. Inference: one good day — hold judgement. |

## amit-pandey-medicodio — Medicodio — 6.4 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 8.0 | 5 PRs opened, 4 merged same day (`#548`, `#550`, `#552`, `#619`, `#621`); dev→uat promotions done; all findings closed by commits. |
| Engineering Rigor | 7.0 | RCA-grade bodies on `#619`/`#621`; guard added for malformed IDs. Against: no tests added; `#550` needed a revert/redo cycle; promotion PRs template-only. |
| Code Review Contribution | 3.0 | 5 approvals, all 0 chars, incl. `#289` (UAT) with 1 open finding. 5th consecutive report. |
| Observable Devin Leverage | 7.0 | 2 Devin trailers; every finding followed by a fix commit within ~1 h and auto-resolved. Against: no written disposition. |
| Automation of Repetitive Work | 5.0 | Template promotions repeated (2 today); no automation. |
| Consistency Across Windows | 6.5 | Day Improved (bodies); week Stable; month Consistent. |

## jatinkushwaha-medicodio — Medicodio — 6.2 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | `#547`, `#618`, `#546` merged; `#551`/`#620` prod promotions opened and **held** with findings visible. Against: `#549` CI-probe PR open. |
| Engineering Rigor | 7.0 | Clear bodies on `#547`/`#618`; SEC finding fixed with commit citing "(Devin review)". Against: no tests; `#551` is 180 files. |
| Code Review Contribution | 3.0 | "lgtm" ×2, "okok", 0-char ×2. 6th report. |
| Observable Devin Leverage | 7.0 | 4 trailers; raised `#547` specifically to fix Devin findings from `#546`; iterated until Resolved. |
| Automation of Repetitive Work | 4.5 | CI-probe PR repeated (`#545` → `#549`, 3 no-op commits) after a 09-05 recommendation to automate. |
| Consistency Across Windows | 6.5 | Day Improved (held promotions); week Stable; month Consistent. |

## sameer-s-mansur — Medicodio — 6.2 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 7.5 | 8 PRs opened, 8 merged: Trinity hardening and `others` fix through Dev/UAT/prod same day; prod deploys green. |
| Engineering Rigor | 6.5 | Best narrative bodies on Medicodio ("four faults observed in prod today"); rule tests updated per fix. Against: prod PR `#291` template body; 4 findings unanswered at prod merge. |
| Code Review Contribution | NR | None given. |
| Observable Devin Leverage | 5.0 | Applied 2 Devin suggestions on `#289`; left 4 findings on `#291` and 1 on `#294` unanswered. |
| Automation of Repetitive Work | 4.5 | Same change opened as paired Dev/UAT PRs twice today and on 09-04; manual promotion within minutes. |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent — same strengths, same promotion habit (4th report). |

## svh-medicodio — Global Codio — 6.0 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 5.5 | 22 commits on `#1316` (97 files, open since 09-04); `#1284` (175 files) being finished by someone else; `#1295` idle since 09-02. Progress without closure. |
| Engineering Rigor | 7.0 | 2 test commits, refactor along read/write seam, DB doc, standards-audit review log, accessibility. Against: 6 new findings unanswered; PR still growing. |
| Code Review Contribution | NR | None given — including on the 32 commits made to his own `#1284`. |
| Observable Devin Leverage | 5.0 | 0 trailers; findings on `#1316` went 9→5→1→6 through commits, no written disposition. |
| Automation of Repetitive Work | 5.5 | "humanize key" fix repeated 3× across consumers; acknowledged in messages, not centralised. |
| Consistency Across Windows | 6.5 | Day Improved (tests/docs); week Stable; month Consistent. |

## afifashaikh007 — Medicodio — 6.2 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | 12 commits on `feat/inpatient-engine` (Phase 2b POA, G2.2, SDK fix). No PR; 09-05 "open a draft PR" not done. |
| Engineering Rigor | 6.5 | Golden Chart Profile fixtures + chain test + audit runner; commit messages state observed defects. Capped: nothing reviewed. |
| Code Review Contribution | NR | None. |
| Observable Devin Leverage | NR | No Devin artefacts; branch invisible to Devin Review. |
| Automation of Repetitive Work | 5.5 | "Phase N silently dropped X" fixed three times by hand; fixtures now exist (progress). |
| Consistency Across Windows | 6.5 | Day Improved (first tests); week Improving; month Insufficient History. |

## ragha82 — Global Codio — 6.0 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | Her `#1314` merged — but the final 30 commits, the approval and the merge were another person's; no comment from her on it in window. E2E suites accumulate on `feat/qa-automation` with no PR. |
| Engineering Rigor | 7.0 | 5 E2E suites each naming IDOR/RLS/tenancy scope; QA skill docs. |
| Code Review Contribution | NR | None. |
| Observable Devin Leverage | NR | No artefacts by her today (QA gate `#1319` is Devin's). |
| Automation of Repetitive Work | 6.0 | E2E automation is her job and is progressing; overlap with Devin QA gate not reconciled. |
| Consistency Across Windows | 6.0 | Day Stable; week Stable; month Consistent. |

## SaahilVishwakarma — Global Codio — 5.3 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | `#1322` opened (68 files) and iterated 17 commits; `#1312` (57 files) idle since 09-03. |
| Engineering Rigor | 6.5 | 2 test commits, pre-push typecheck fixes, decisions recorded as decisions, secrets kept out of logs. Against: 11.5k-line PR; 15 findings without written disposition. |
| Code Review Contribution | 2.5 | Two 0-char approvals within 2 minutes on `#1329` and `#1330` — 776 files each, the latter to prod. |
| Observable Devin Leverage | 5.0 | Several findings addressed by commits; none dispositioned in writing. |
| Automation of Repetitive Work | 5.0 | 7 hand-written docs/gate-record commits. |
| Consistency Across Windows | NR | No 09-04 activity; insufficient window history. |

## sumedh-codio — Medicodio — 5.5 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 6.5 | 18 commits: PCP export end-to-end incl. Jenkins pipeline and telemetry. No PR yet. |
| Engineering Rigor | 6.0 | Well-explained commits and 3 docs commits; never-fail telemetry contract respected. Against: no tests (repo has none), 0 reviews of any kind on this repo in 30 days. |
| Code Review Contribution | 2.5 | 5 approvals, all 0 chars, ≤ 5 min after open, incl. two prod promotions. 3rd report. |
| Observable Devin Leverage | NR | No Devin artefacts; Devin Review not enabled on the repo. |
| Automation of Repetitive Work | 6.0 | Automating repetitive claim export is the work itself — progressing. |
| Consistency Across Windows | NR | Repo newly covered; approval pattern only. |

## Pj-Vineeth-Kumar — Global Codio — 5.2 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 5.0 | 24 commits on two branches; no PR (09-05 "open the draft PR" not done). |
| Engineering Rigor | 5.5 | Precise security-relevant fixes (recipient resolution, HR RBAC basis) and backfill script; no tests; nothing reviewed. |
| Code Review Contribution | NR | None. |
| Observable Devin Leverage | NR | None. |
| Automation of Repetitive Work | 5.0 | 6 manual component promotions; pattern acknowledged by naming, not tooled. |
| Consistency Across Windows | 5.0 | Day Stable; week Needs Attention (93 commits, 0 reviewed). |

## vishnu-saikarthik — Medicodio — 5.1 Mixed

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 6.0 | `#430` merged to uat and prod (by others); 2 inpatient commits on the shared branch. |
| Engineering Rigor | 5.0 | Quantified defects ("32 %"); no tests; `#430` findings never answered. |
| Code Review Contribution | NR | None. |
| Observable Devin Leverage | 3.5 | 6 findings on `#430` (2 BUG) unanswered; carried to prod. |
| Automation of Repetitive Work | NR | No evidence. |
| Consistency Across Windows | 5.5 | Day Stable; week Stable. |

## avinash-codio — Medicodio — 3.9 Needs Support

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 5.5 | `#431` merged and promoted via `#432` same morning. |
| Engineering Rigor | 3.0 | Template-only bodies on both; prod promotion 3 min after open; 3 findings ignored incl. BUG on `extractor.py`. |
| Code Review Contribution | NR | None. |
| Observable Devin Leverage | 2.5 | Findings ignored on both PRs. |
| Automation of Repetitive Work | NR | `vcr` migration recommendation (09-05) — no evidence either way. |
| Consistency Across Windows | 4.0 | Day Regressed; week Needs Attention. |

## NandanDate-Medicodio — Medicodio — 2.9 Needs Support

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | NR | No authored work in window. |
| Engineering Rigor | NR | — |
| Code Review Contribution | 2.5 | 6 review events, all "okay" (one dismissed); merged 7 PRs incl. prod `#429` (4 findings open) and `#433` (6 open, 5k lines). |
| Observable Devin Leverage | 3.0 | Approves over open Devin findings on every PR reviewed. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 3.5 | Identical pattern 08-29 → today (5th report). |

## Murali-Shetty19 — Medicodio — NR

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Delivery & Follow-Through | 5.5 | 2 commits advancing `#415` (open since 09-01). |
| Engineering Rigor | 5.0 | Provenance tiers documented; 8 new findings (5 BUG) unanswered. |
| Others | NR | Two rated dimensions → overall NR. |

## ashwinsk-medicodio — Medicodio — NR

| Dimension | Score | Evidence (Observed Fact unless marked) |
| --- | --- | --- |
| Code Review Contribution | 2.5 | 0-char approval on prod `#432`. |
| Observable Devin Leverage | 3.5 | 4 findings on his `#429` unanswered at prod merge. |
| Others | NR | Two rated dimensions → overall NR. |

---

## How to read the spread

- **Observed Fact:** the three Solid scores today (Medicodio-Amit 7.3, anirudh 7.1, Amrutha 7.0) share one feature — written dispositions of Devin findings. The three Needs Support / near-NR scores (avinash, Nandan, ashwinsk) share the opposite: approvals or promotions with findings open and no text. Every one of the 45 human review bodies today was ≤ 5 characters.
- **Observed Fact:** 17 Devin findings entered Medicodio prod today across five promotions, and a 776-file Global Codio promotion reached `main` on two 0-char approvals. These lower Review and Rigor scores for the approvers, not the authors' Delivery.
- **Inference:** Global Codio's rigor is concentrated in one person's authorship (anirudh) rather than in review; his Review score (4.5) reflects that the independence check is missing even though the work quality is high. svh and ragha82 score lower on Delivery because their PRs were completed by him.
- **Inference:** branch-only members (afifa, Vineeth, Sumedh, ragha82's QA suite) sit in the Mixed band mostly because nothing they wrote has been reviewed — opening draft PRs would move Rigor and Devin from capped/NR to rated.
- **Recommendation:** the single highest-leverage change remains the same as 09-05: one sentence of verification evidence per approval and a written disposition per Devin finding before any `uat`/prod/`main` merge. Today shows the practice is achievable — three people did it.
- **Caveat:** without session telemetry, "Observable Devin Leverage" under-counts anyone who uses Devin without trailers or PR-visible artefacts, and cannot see prompt quality or corrections at all. Confidence column reflects artefact density, not certainty about the person.

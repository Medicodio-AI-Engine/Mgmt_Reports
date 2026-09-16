# Employee Rating Cards — 2026-09-16

**Review window:** 2026-09-15 03:00 UTC → 2026-09-16 03:00 UTC. Comparison: previous working day 09-14, week 09-08 → 09-15, month 08-16 → 09-15. Companion report: `2026_09_16_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`org.sessions.view` missing). *Observable Devin Leverage* is scored only on what is visible in GitHub: Devin Review findings and how they were dispositioned, Devin QA-gate verdicts and follow-up, Devin-authored PRs and how humans consumed them. Prompt quality, ACU effort, correction burden and delegation that never reached GitHub are invisible — this dimension carries **Low–Medium confidence** for everyone.
- **No Jira, no Sentry.** Coordination, support and incident work are unscored unless they left a GitHub trace.
- **Volume is not productivity.** Commit, PR and line counts appear only as context. A member with 29 commits and a member with 2 can score identically; scores follow scoping, controls, evidence and follow-through.
- **NR rules.** A dimension with no in-window evidence is **NR** and excluded from the weighted average. Fewer than three rated dimensions → overall **NR**. Members with zero in-window events are listed once and not scored.
- **Product contexts are separate.** Global Codio and Medicodio members are scored against the same rubric but not against each other's conventions.
- Bands: **Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5.**

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 1–4 |
| --- | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work merged with follow-up handled; open items progressed | Work merged or materially advanced; minor loose ends | Progress on open PRs/branches without closure | Stalled, abandoned without record, or merged without controls |
| Engineering Rigor | 25 | Tests + RCA + accurate PR body + findings addressed; PR sized for review | Clear body or tests; most findings addressed | Body or tests thin; findings partly addressed; PR oversized | Empty body, no tests, findings ignored, self-merge |
| Code Review Contribution | 15 | Substantive, specific, independent review that changes outcomes | Specific comments; approvals name what was checked | Approvals with minimal evidence | Empty/one-word approvals on PRs with open findings |
| Observable Devin Leverage | 15 | Devin used where it gives leverage; every finding dispositioned with reasons/tests | Findings closed with linked commits or reasoned rejection | Findings partially addressed; passive use | Findings ignored at merge; Devin bypassed on reviewable work |
| Automation of Repetitive Work | 10 | Repetitive work removed/automated | Automation in progress | Repetition acknowledged, not addressed | Manual repetition without plan |
| Consistency Across Windows | 10 | Day/week/month all improving or strong | Stable with improvements | Mixed | Regressed vs week and month |

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pj-Vineeth-Kumar | Global Codio | **6.4** | Mixed | 7 | 6 | NR | 6 | 5 | 8 | Medium (GitHub only; 5 dims) |
| jatinkushwaha-medicodio | Medicodio | **6.6** | Mixed | 7 | 6 | NR | 8 | 5 | 7 | Medium (GitHub only; 5 dims) |
| SaijyotiMeti | Global Codio | **6.4** | Mixed | 6 | 7 | NR | 6 | 6 | 7 | Medium (7 commits, no PR; 5 dims) |
| anirudh-medicodio | Global Codio | **5.8** | Mixed | 6 | 7 | 5 | 5 | 4 | 6 | Medium (GitHub only; large evidence base) |
| akanksh-rv | Global Codio | **5.7** | Mixed | 4 | 8 | 5 | 6 | 5 | 5 | Medium (GitHub only; one PR, dense evidence) |
| ragha82 | Global Codio | **5.0** | Mixed | 6 | 5 | 3 | 5 | 6 | 5 | Medium (GitHub only) |
| Vishnu Sai Karthik | Medicodio | **5.5** | Mixed | 5 | 6 | NR | 5 | NR | 6 | Low (1 PR; 4 dims) |
| Hitesh Shanthakumar | Medicodio | **5.4** | Mixed | 5 | 6 | NR | NR | 4 | 6 | Low (4 commits, no PR; 4 dims) |
| amit-pandey-medicodio | Medicodio | **3.6** | Needs Support | NR | NR | 3 | 4 | NR | 4 | Low (reviewer-only role; exactly 3 dims rated) |
| Amrutha-Beedikar | Global Codio | **NR** | — | NR | NR | NR | NR | NR | 6 | — (no own events in window) |
| svh-medicodio, SaahilVishwakarma | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity in window) |
| sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, ashwinsk-medicodio, avinash-codio, sumedh-codio, Murali-Shetty19, Shashvi1 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity in window) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions), rounded to one decimal.

---

## Pj-Vineeth-Kumar — Global Codio — 6.4 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** opened `#1380` (385 files, 90 commits, PRD + decisions log + review guide) after 5 reports of a PR-less branch; 5 further commits on intake badge / bulk-initiation batches. `#1365` (Devin PR on his branch) 5th day with no reviewer. **Inference:** materially advanced with one loose end. |
| Engineering Rigor | 6 | **Observed Fact:** breaking changes marked `!`; body states exactly what was moved verbatim and why; but 385 files in one PR, a `feat(db)` column drop + migration inside it, no test commits among today's 29. **Inference:** the body is strong; the size and embedded schema change cost the top band. |
| Code Review Contribution | NR | No review events in window. |
| Observable Devin Leverage | 6 | **Observed Fact:** Claude trailers on 24/29 commits; Devin Review on `#1380` not yet visible; `#1365` unconsumed. **Inference:** passive; the split-and-test of `#1380` is the unused opportunity. |
| Automation of Repetitive Work | 5 | **Observed Fact:** deep-link/agent repointing done by hand (2 commits); dark-mode token edits recurring. |
| Consistency Across Windows | 8 | **Observed Fact:** week 1st and month 1st by volume; today resolved his named Repeat Pattern. **Inference:** Improving on process, consistent on output. 09-12 card 6.6 → 6.4 (Delivery up, Rigor down on PR size). |

**Recommendation:** split the column drop into its own PR; stack `#1380`.

## jatinkushwaha-medicodio — Medicodio — 6.6 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** 4 PRs merged into `Dev_1.0` (`react#573`, `nodejs#642`, `#643`, `#644`); `#642` reverted by him 20 min after merge and re-done in `#643`. **Inference:** closure on all items, one self-corrected misstep. |
| Engineering Rigor | 6 | **Observed Fact:** migration `20260915_001_batch_runs_retry_of.sql`; fixes for null/zero coercion and import-reuse bypass landed only after Devin flagged them; no test files in the 4 PRs; the reverted refactor implies no test caught it. **Inference:** correct but reactive. |
| Code Review Contribution | NR | No review events in window. |
| Observable Devin Leverage | 8 | **Observed Fact:** 8 Devin Review findings, all resolved with commits within 5–15 min and confirmed `✅ Resolved` by Devin. No delegation. **Inference:** the best finding-consumption in the org today; delegation of tests is the next step. |
| Automation of Repetitive Work | 5 | **Observed Fact:** same coercion/validator class fixed twice today by hand. |
| Consistency Across Windows | 7 | **Observed Fact:** steady daily PR flow on `feat/dashboards-documentation` all week; Medicodio silent Monday not attributable to him. 09-12 card 6.4 → 6.6. |

**Recommendation:** batch-run service tests via Devin as a required check.

## SaijyotiMeti — Global Codio — 6.4 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** 7 commits on a new branch (feature + race fix + PRD + test fix), no PR yet (<3 h old); the 09-15 open items (`#1367` index decision, `#1372` C-1..C-4) not progressed; `#1372` closed by anirudh. **Inference:** progress without closure. |
| Engineering Rigor | 7 | **Observed Fact:** race condition fixed in its own commit with rationale; fixture-type test fix included; PRD reconciled in the same push. No new test coverage for the picker. |
| Code Review Contribution | NR | No review events in window. |
| Observable Devin Leverage | 6 | **Observed Fact:** Claude Sonnet trailers on 7/7; no Devin PRs; her NOT READY QA report closed without her disposition. **Inference:** passive. |
| Automation of Repetitive Work | 6 | **Observed Fact:** PRD-per-branch discipline maintained (this is the right manual work); fixture fixes recurring. |
| Consistency Across Windows | 7 | **Observed Fact:** week 2nd by volume; 3 of the week's NOT READY merges were hers but none today. 09-15 card 6.5 → 6.4. |

**Recommendation:** open the draft PR now; post the `#1367` index decision.

## anirudh-medicodio — Global Codio — 5.8 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1363` (205 files) merged; `#1364` finished and merged; release train `#1375`/`#1377`/`#1378` + hotfix promotion `#1383`/`#1384` all landed; `#1378` broke the prod API build; QA F-6/F-1 on `#1363` undispositioned; 3 fix PRs closed unmerged without record. **Inference:** everything shipped; the controls around shipping were thin. |
| Engineering Rigor | 7 | **Observed Fact:** 10k review verified React behaviour against installed source and corrected the PR narrative; spec rewritten to discriminate the fix; `act()` warnings cleaned. Promotion PR bodies `uat update`/`main update`. **Inference:** high on code, low on release artefacts. |
| Code Review Contribution | 5 | **Observed Fact:** one substantive review (`#1364`) on a PR he had committed 12 times to, then empty self-approve + merge 8 min later with 2 new Devin findings open; empty approvals on `#1362`, `#1382`. **Inference:** substance high, independence nil. |
| Observable Devin Leverage | 5 | **Observed Fact:** consumed Devin Review, two QA gates and CI diagnosis; but merged over 2 fresh findings, left `#1363` F-6/F-1 open, and closed `#1360`/`#1369`/`#1371` (fixes for confirmed PRODUCT_FAILUREs) with no disposition. |
| Automation of Repetitive Work | 4 | **Observed Fact:** 5 hand-made promotion PRs with placeholder bodies; 12 manual PR closures; jest housekeeping by hand. |
| Consistency Across Windows | 6 | **Observed Fact:** month 2nd by volume; release-train pattern unchanged all month; first time he shows the remediate-then-self-merge sequence. 09-12 card 6.8 → 5.8. |

**Recommendation:** disposition `#1363` F-6/F-1 and the three closed fix PRs in writing.

## akanksh-rv — Global Codio — 5.7 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4 | **Observed Fact:** approved (`approved`) and merged `#1373` 2 min after his own review said "REQUEST-DECISION on release readiness … Write and approve the §4.4 script, settle item 2, and this is good to go"; QA gate NOT READY 55/100 66 min later; `#1373` promoted to `main` at 19:15. **Inference:** the rubric's "merged without controls" language applies literally. |
| Engineering Rigor | 8 | **Observed Fact:** two regression-guard test commits; fixed a tenancy gap, a prod-breaking env fallback, and two tests that could not pass; 42/42 gate recorded; his own broken test corrected and strengthened. **Inference:** the code-level rigour is the highest in the org today. |
| Code Review Contribution | 5 | **Observed Fact:** 11,839-char review with an 11-row decision table, 2 refuted rows — then the approving reviewer was the same person, on a PR he had 27+ commits on. **Inference:** substance 9, independence 1 (same split as SaijyotiMeti's 09-15 card). |
| Observable Devin Leverage | 6 | **Observed Fact:** Devin Review findings dispositioned earlier (09-15); post-merge NOT READY gate not acted on in window; Devin's report PR `#1374` closed by anirudh. No delegation of the §4.4 script he asked for. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 2 `docs(review-logs)` commits; gate-run table hand-written; recurring all month. |
| Consistency Across Windows | 5 | **Observed Fact:** 09-11 merged `#1366` over own blocker; 09-15 stopped at the decision items; today merged over them again. Week 3rd, month 2nd by volume. **Inference:** Regressed vs the one-day improvement; mixed vs month. 09-15 card 7.3 → 5.7. |

**Recommendation:** decision items answered in-PR before any approve; a different person presses merge.

## ragha82 — Global Codio — 5.0 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** prod hotfix `#1382` + prevention hook merged and promoted within ~30 min of Devin's diagnosis; `#1362` merged. QA on `#1382`: merged spec red on `dev` — unanswered. |
| Engineering Rigor | 5 | **Observed Fact:** fix paired with a guard hook (good); the same PR merged a failing jest spec (`Sep` vs `Sept`); Devin Review found 3–4 issues in the hook on `#1383`/`#1384`, unanswered. |
| Code Review Contribution | 3 | **Observed Fact:** 6 approvals, all empty: `#1363` (205 files), `#1375` (531 files, 12 min), `#1377`, `#1378` (542 files — broke prod), `#1383`, `#1384` (≤1 min, with open Devin findings on the diff). **Inference:** merge authority without evidence, on the org's highest-risk PRs. |
| Observable Devin Leverage | 5 | **Observed Fact:** Devin diagnosed the break before her fix; her PR superseded Devin's `#1381` (reasonable); Devin's two follow-up outputs on her own change ignored in window. |
| Automation of Repetitive Work | 6 | **Observed Fact:** added an undeclared-dependency hook — automation of a repeat failure class. |
| Consistency Across Windows | 5 | **Observed Fact:** empty promotion approvals every promotion this month; hotfix-after-promotion recurs. 09-12 card 6.2 → 5.0. |

**Recommendation:** approval comments must list the QA verdicts of the PRs being promoted.

## Vishnu Sai Karthik — Medicodio — 5.5 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `engine#452` opened to `uat`, 2 commits, open at window end with no reviewer requested; `#435` also open, no reviewer. |
| Engineering Rigor | 6 | **Observed Fact:** malformed-scope rules now rejected instead of applied everywhere (fails closed); no tests in the PR; 1 Devin finding unanswered. |
| Code Review Contribution | NR | No review events in window. |
| Observable Devin Leverage | 5 | **Observed Fact:** 5 findings → 1 resolved by commit; 1 new at 13:08 unanswered. |
| Automation of Repetitive Work | NR | No repetitive-work evidence in window. |
| Consistency Across Windows | 6 | **Observed Fact:** low steady volume; same "PR to `uat` without reviewer" shape as `#435`. |

**Recommendation:** reviewer on open; validator tests.

## Hitesh Shanthakumar — Medicodio — 5.4 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** 4 commits on `feat/inpatient-engine`; no PR — 10th consecutive report. |
| Engineering Rigor | 6 | **Observed Fact:** commits describe clinical behaviour (disputed body part → PCS, DRG grouping, empty-text fetch); no tests visible in the 4 commits. |
| Code Review Contribution | NR | No review events in window. |
| Observable Devin Leverage | NR | No Devin touchpoint possible without a PR; not penalised, not credited. |
| Automation of Repetitive Work | 4 | **Observed Fact:** the branch-without-PR pattern is acknowledged in 9 prior reports and unaddressed. |
| Consistency Across Windows | 6 | **Observed Fact:** consistent output, consistent absence of PR. |

**Recommendation:** draft PR today.

## amit-pandey-medicodio — Medicodio — 3.6 (Needs Support)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | NR | No authored work in window. |
| Engineering Rigor | NR | No authored work in window. |
| Code Review Contribution | 3 | **Observed Fact:** 4 approvals, all empty, each 1–2 min after Devin Review finished; `#642` reverted 20 min after his approval. |
| Observable Devin Leverage | 4 | **Observed Fact:** waited for Devin Review to complete before approving (positive); no evidence of reading its findings independently. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4 | **Observed Fact:** empty approvals every reviewing day since the 08-2x reports. |

Exactly three dimensions rated, so the overall is computed (3.6). **Inference:** all three are review-side; this is a score for how he reviewed today, not for engineering output he did not produce in window — read with Low confidence. **Recommendation:** one sentence per approval naming the check.

## Amrutha-Beedikar — Global Codio — NR

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | NR | No own events; `#1364` merged after anirudh's 12 commits; `#1360` closed unmerged by anirudh. |
| Engineering Rigor | NR | — |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 6 | **Observed Fact:** 09-15 1 commit, today 0; week 27, month 45. |

**Recommendation:** disposition comment on `#1360`.

---

## How to read the spread

- **Observed Fact:** the spread is 5.0 → 6.6 across eight author-rated members, all in *Mixed*; the one reviewer-only member (amit) is 3.6. No one is *Strong* or *Solid* today. The two highest scores (Vineeth, Jatin) are earned on follow-through and finding-disposition, not volume; the two members with the most code-level rigour (akanksh 8, anirudh 7) sit lower because Delivery and Review are scored on *controls*, and both approved and merged PRs they had remediated, one of them over an explicit written blocker that reached production the same day.
- **Observed Fact:** review evidence is the weakest dimension org-wide — 14 of 16 human review objects were empty or one word, and the two substantive reviews were self-approved. Medicodio's only human reviewer today (amit) is NR for that reason.
- **Inference:** the day's scores moved most for akanksh (7.3 → 5.7) and anirudh (6.8 → 5.8), and that movement is about one decision each, not a change in skill. If the same decisions are not repeated tomorrow, both return to *Solid* on the same evidence base. Vineeth's Delivery rise is real (branch became a PR) but is offset by Rigor on the same PR, which is now the largest open review burden in Global Codio.
- **Inference:** Devin leverage is bounded above by the missing telemetry — Jatin's 8 is the ceiling visible from GitHub; delegation that happened in sessions we cannot see is not credited to anyone.
- **Recommendation:** treat the two *Immediate Attention* items in the companion report (`#1373` decisions and `#1363` F-6/F-1, both in production) as the next-day test of whether these scores were a single unusual day; and grant the automation `org.sessions.view` so Devin leverage can be scored on evidence rather than absence.

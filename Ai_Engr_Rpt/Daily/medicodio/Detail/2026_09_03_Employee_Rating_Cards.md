# Employee Rating Cards — 2026-09-03

**Review window:** 2026-09-02 03:00 UTC → 2026-09-03 03:00 UTC. Comparison windows: previous working day (09-01 03:00 → 09-02 03:00), week (08-26 → 09-03), month (08-03 → 09-03).
**Companion report:** `2026_09_03_Mgmt_Activity_Report.md` (same directory) holds the evidence each score cites.

## Scoring limitations — read before the numbers

1. **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (missing `org.sessions.view`). Nothing here reflects who started a Devin session, how it was prompted, how much effort it consumed, or how much correction it needed. "Observable Devin Leverage" is scored **only** from GitHub artefacts: `devin-ai-integration[bot]` PRs, reviews and comments, `Co-Authored-By: Devin` trailers, Devin-signed QA-gate and CI-diagnosis comments, and whether humans answered them. A member who used Devin through channels that leave no GitHub trace is under-observed, not under-performing.
2. **No Jira, no Sentry.** Ticket hygiene, incident work and coordination are invisible; members whose day was meetings, support or investigation have fewer rated dimensions, which is why NR exists.
3. **Hosted-dev QA could not authenticate.** Four of six Devin gates and the Claude QA routine produced no verdict, so "Engineering Rigor" cannot credit or debit anyone for authenticated UI behaviour today.
4. **Volume is not scored.** Commit, PR, review, line and comment counts appear only as context for a qualitative judgement. A 145-file PR does not raise Delivery; an empty approval on a 601-file promotion lowers Review.
5. **NR rules.** A dimension with no in-window evidence is NR and excluded from the weighted average; a member with fewer than three rated dimensions receives an overall of NR. NR is never a low score.
6. **Single-day caution.** Scores describe this window with week/month context; they are not a performance rating and must not be read as one without the trend columns.

## Rubric

| Dimension | Weight | 1–3 | 4–6 | 7–8 | 9–10 |
| --------- | ------ | --- | --- | --- | ---- |
| **Delivery & Follow-Through** | 25 | Work stalls; nothing reaches a reviewable state; carried items untouched | Work lands but leaves loose ends, or accumulates without a PR | Work lands complete, with follow-through on what it breaks | Lands complete, closes carried items, and leaves the next person nothing to clean up |
| **Engineering Rigor** | 25 | No verification; risky changes shipped blind | Some verification; tests or documentation missing where they mattered | Tests or documented verification accompany behaviour changes | Reproduction tests, design docs and honest failure notes are routine |
| **Code Review Contribution** | 15 | No review, or content-free approvals on substantial diffs | Reviews given but thin relative to diff size | Written verdicts naming what was checked | Architect-level reviews verified against the schema/spec, independent of the author |
| **Observable Devin Leverage** | 15 | Devin output ignored or findings left unanswered | Devin runs but its output is not consumed | Devin findings answered and acted on before merge | Devin used to remove the team's repetitive work, not just to write code |
| **Automation of Repetitive Work** | 10 | Repetitive work repeated by hand with no attempt to remove it | Repetition recognised but unchanged | Some repetition removed or scripted | Builds the tooling that removes repetition for others |
| **Consistency Across Windows** | 10 | Erratic; long gaps with no explanation | Present but uneven across the week | Steady across day, week and month | Steady and improving across all three windows |

**Bands:** Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5. Overall = Σ(score × weight) / Σ(weights of rated dimensions).

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| ------ | ------- | ------- | ---- | ------------- | ---------- | ----------- | ---------- | --------------- | ---------------- | ---------- |
| SaijyotiMeti | Global Codio | **7.6** | Solid | 8 | 8 | 8 | 7 | 4 | 9 | High |
| SaahilVishwakarma | Global Codio | **7.4** | Solid | 7 | 8 | NR | 8 | NR | 6 | Medium |
| ragha82 | Global Codio | **6.4** | Mixed | 7 | 7 | 3 | 7 | 7 | 7 | High |
| sameer-s-mansur | Medicodio | **6.2** | Mixed | 7 | 5 | NR | 6 | 6 | 8 | High |
| akanksh-rv | Global Codio | **5.9** | Mixed | 6 | 6 | 6 | 5 | 6 | 6 | Medium |
| anirudh-medicodio | Global Codio | **5.8** | Mixed | 7 | 5 | 3 | 6 | 5 | 9 | High |
| jatinkushwaha-medicodio | Medicodio | **5.8** | Mixed | 7 | 6 | 3 | 5 | 5 | 8 | High |
| Shashvi1 | Medicodio | **5.7** | Mixed | 6 | 6 | NR | 5 | NR | 5 | Low |
| Pj-Vineeth-Kumar | Global Codio | **5.5** | Mixed | 6 | 5 | NR | 5 | 5 | 7 | Medium |
| Amrutha-Beedikar | Global Codio | **5.5** | Mixed | 7 | 6 | 3 | 5 | NR | 5 | Medium |
| amit-pandey-medicodio | Medicodio | **5.2** | Mixed | 6 | 5 | 2 | 4 | NR | 8 | High |
| avinash-codio | Medicodio | **4.7** | Needs Support | 6 | 4 | NR | 3 | NR | 6 | Medium |
| svh-medicodio | Global Codio | **4.4** | Needs Support | 5 | 4 | 2 | 4 | NR | 6 | Medium |
| NandanDate-Medicodio | Medicodio | **4.4** | Needs Support | 5 | 4 | 2 | 3 | NR | 7 | Medium |
| Medicodio-Amit | Medicodio | **NR** | NR | 5 | NR | NR | NR | NR | 5 | Low |
| shaheen-khan11 | Medicodio | **NR** | NR | NR | NR | NR | NR | NR | 6 | Low |
| sumedh-codio | Medicodio | **NR** | NR | NR | NR | NR | NR | NR | NR | Low |
| hitesh (`hiteshjrxmedicodio`) | Medicodio | **NR** | NR | NR | NR | NR | NR | NR | NR | Low |

Bot and alias identities (`devin-ai-integration[bot]`, `claude`, `Azhao15`, `saijyoti.m`, `anirudhdmedicodio`, `karthikmed`) are not rated.

---

## SaijyotiMeti — Global Codio — **7.6 Solid** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** drove `#1285` (167 files) from open to merge with 30 remediation commits covering security (ReDoS), data integrity (three `parseDateValue` iterations, two west-of-UTC off-by-ones) and UX; opened `#1305` DVR engine the same night. **Inference:** the loose end is that `#1305` is a 105-file single PR |
| Engineering Rigor | 8 | **Observed Fact:** 3 `test(` commits tied to the fixes; a disclosed own-fix reversal verified against write paths and the repository's own `::date` truncation; gates green across six packages before merge. Held below 9 because the Claude QA High (country codes not backend-enforced) was not caught by the review |
| Code Review Contribution | 8 | **Observed Fact:** the organisation's only substantive review today — 4,508 chars, 13 inline verdicts each mapped to a SHA. Not 9 because it was not independent: 30 of the day's commits on the branch are hers, and her 8-char `approved` preceded her own merge by 60 s (same shape as 09-01) |
| Observable Devin Leverage | 7 | **Observed Fact:** 7 Devin re-scan rounds consumed adversarially, one of which caught her own fix; 0 Devin-authored commits; 8 findings on `#1305` not yet answered (3 h old) |
| Automation of Repetitive Work | 4 | **Observed Fact:** 5 hand-written `docs(review)` commits (4 on 09-01, 6 on 08-31) and six per-view date fixes where one codemod would do — repetition recognised, unchanged |
| Consistency Across Windows | 9 | **Observed Fact:** 168 commits in the week, 13 `test(`; substantive review on every active day since coverage began |

**Trend:** Stable vs yesterday (7.7 → 7.6; Automation down one for the growing review-log habit).

---

## SaahilVishwakarma — Global Codio — **7.4 Solid** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1283` merged; `#1304` opened 2.5 h later resolving all 10 QA findings. Held at 7 because the landing depended on ~25 remediation commits by ragha82 |
| Engineering Rigor | 8 | **Observed Fact:** each QA finding re-verified against code; three rejected with reasoning; the High (retry verdict "nothing could read") explained mechanically in the body. No `test(` commit by him in-window |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 8 | **Observed Fact:** 46 Devin Review comments on `#1283` and the QA verdicts consumed and answered with commits, not acknowledgements |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 6 | **Observed Fact:** two consecutive substantive days after a quiet week; 119 commits in the month |

**Trend:** Stable (7.3 → 7.4).

---

## ragha82 — Global Codio — **6.4 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1278` merged; ~25 remediation commits carried `#1283` to merge; `#1299/#1300/#1301` opened and landed; 6 gates executed |
| Engineering Rigor | 7 | **Observed Fact:** `test(ci)` enabling `packages/*` suites, `fix(ci)` for the Nx legs, an ADR for the advisory lock, "four failures — all mine". Not higher because he merged and promoted `#1278` within 3 h of his own gate's NOT READY |
| Code Review Contribution | 3 | **Observed Fact:** 5 approvals, 5 empty — `#1278` (60 files) and three production-path promotions |
| Observable Devin Leverage | 7 | **Observed Fact:** the gate produced one real verdict and four honest no-verdicts; the doctrine is his. Down from 9 because four runs validated nothing and the verdict is not enforced on promotion |
| Automation of Repetitive Work | 7 | **Observed Fact:** gate/CI wiring reduces manual QA; no pre-flight for the credential failure that recurred |
| Consistency Across Windows | 7 | **Observed Fact:** 39 commits week, present most days |

**Trend:** Regressed (6.8 → 6.4; Devin and Rigor down for the promoted NOT READY).

---

## sameer-s-mansur — Medicodio — **6.2 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** Trinity laterality/addendum, PPV continuation + TCM, `others` catch-all and table convention landed through `Dev_1.0 → Uat_1.0 → release/prod_1.0` in 27 min |
| Engineering Rigor | 5 | **Observed Fact:** 0 `test(` commits; prompt/parsing changes to prod same day; both PR bodies template-only. Commit messages are descriptive |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 6 | **Observed Fact:** "Address review" commit 17 min after Devin Review's 5 findings on `#280`, before the UAT merge |
| Automation of Repetitive Work | 6 | **Observed Fact:** `others` defined by absence of mapping and a table-formatting convention replace per-section one-offs; 09-01's `/onboard-facility` skill still the high-water mark |
| Consistency Across Windows | 8 | **Observed Fact:** 63 commits week, 228 month, every weekday |

**Trend:** Regressed slightly (6.9 → 6.2; smaller day, Automation lower than the skill day).

---

## akanksh-rv — Global Codio — **5.9 Mixed** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** two QA routine passes published; `#1296` merged; `#1306` opened at 145 files after multi-day accumulation (4th report with this shape) |
| Engineering Rigor | 6 | **Observed Fact:** QA comments are scored, cite files/lines, disclose "no live persona login was possible" and SQL-only checks; found the High in `#1283`. `#1306` ships with 7 unanswered findings and no split |
| Code Review Contribution | 6 | **Observed Fact:** no formal review events, but two 3,700-char QA verdicts on others' features acted on by the authors — scored as review because that is what they are |
| Observable Devin Leverage | 5 | **Observed Fact:** runs the Claude routine in parallel to the Devin gate on the same features; no Devin authoring; 7 findings on `#1306` not yet answered (1 h old) |
| Automation of Repetitive Work | 6 | **Observed Fact:** the QA routine is automation; duplicated with the Devin gate rather than unified |
| Consistency Across Windows | 6 | **Observed Fact:** 106 commits week / 441 month, still concentrated in single long branches |

**Trend:** Stable (5.9 → 5.9).

---

## anirudh-medicodio — Global Codio — **5.8 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1278`, `#1290`, `#1294`, `#1257` merged; prod OOM repaired through the train; 16 remediation commits landed `#1257` |
| Engineering Rigor | 5 | **Observed Fact:** 2 `test(` commits (first in four reports) and excellent root-cause bodies; but the NOT READY SEV-High on `#1278` was promoted to `main` unaddressed and the content-sync corpus named 08-30 is still absent |
| Code Review Contribution | 3 | **Observed Fact:** 4 approvals, 4 empty, incl. `#1283` (98 files, +11,637) 1 min before his own merge and two `main` promotions |
| Observable Devin Leverage | 6 | **Observed Fact:** consumed Devin's CI diagnosis and chose the train over Devin's `main` hotfix; answered 12 findings on `#1257`; did not consume the gate verdict on `#1278` |
| Automation of Repetitive Work | 5 | **Observed Fact:** 5 hand-made promotion PRs with template bodies; 2 hand-written review logs |
| Consistency Across Windows | 9 | **Observed Fact:** 212 commits week, 811+ month, present every day |

**Trend:** Stable (5.9 → 5.8; Rigor up for tests, Review down for the empty `#1283` approval).

---

## jatinkushwaha-medicodio — Medicodio — **5.8 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#601`/`#526` analytics fixes merged; `#528` test PR opened; two superseded PRs closed and branch deleted |
| Engineering Rigor | 6 | **Observed Fact:** `#528` (23 files) is the first test-focused PR seen in Medicodio coverage and answers a five-report pattern; `#526` self-merged |
| Code Review Contribution | 3 | **Observed Fact:** `lgtm` ×2 on `#603`/`#529` (145 files combined), merged by him within a minute |
| Observable Devin Leverage | 5 | **Observed Fact:** Devin finding on `#528` addressed (re-scan 0 new); no Devin authoring |
| Automation of Repetitive Work | 5 | **Observed Fact:** analytics BE↔FE mirror still hand-kept; `#528` refactors tests to a shared `ToastProvider` context (some removal) |
| Consistency Across Windows | 8 | **Observed Fact:** 75 commits week, 176+ month, steady |

**Trend:** Improved (5.2 → 5.8; Rigor up for `#528`).

---

## Shashvi1 — Medicodio — **5.7 Mixed** (Low confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#421` opened — one scoped commit, 6 files; not yet merged |
| Engineering Rigor | 6 | **Observed Fact:** body states the defect in CMS terms with expected thresholds; no test visible in the commit list |
| Code Review Contribution | NR | No reviews in-window (3 one-word reviews in the week) |
| Observable Devin Leverage | 5 | **Observed Fact:** 1 Devin finding unanswered after 15 h |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 5 | **Observed Fact:** 3 commits week, 7 month — present but light |

**Trend:** Insufficient Data (first card).

---

## Pj-Vineeth-Kumar — Global Codio — **5.5 Mixed** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1285` and `#1257` both merged today. **Inference:** landing depended on 30 and 16 remediation commits by others |
| Engineering Rigor | 5 | **Observed Fact:** 4 own commits, 0 tests; Claude QA rated `#1285` READY WITH KNOWN RISKS with a High (ISO-3166 rule not backend-enforced) that is now in production |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 5 | **Observed Fact:** `#1280` Devin PR still open with 29 more bot comments and no human review; no delegation of the remediation |
| Automation of Repetitive Work | 5 | **Observed Fact:** the field-rules editor is configuration-over-code (removes per-country hand edits); nothing else |
| Consistency Across Windows | 7 | **Observed Fact:** 39 commits week, 173 month, 24 Devin-trailer — steady Devin author |

**Trend:** Stable (5.1 → 5.5).

---

## Amrutha-Beedikar — Global Codio — **5.5 Mixed** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1288` root-causes a customer-visible `{{file_number}}` leak to the exact path `#1243` missed; scoped to 6 files |
| Engineering Rigor | 6 | **Observed Fact:** 10.8k-char body with history; no test commit; 6 Devin findings unanswered after 13 h |
| Code Review Contribution | 3 | **Observed Fact:** `approved` (8 chars) on `#1286`, a 601-file `dev → uat` promotion, 90 s before merge |
| Observable Devin Leverage | 5 | **Observed Fact:** findings received, not yet consumed |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 5 | **Observed Fact:** 4 commits week, 59 month — sporadic |

**Trend:** Insufficient Data (first full card).

---

## amit-pandey-medicodio — Medicodio — **5.2 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** workspace-module refactor landed in both repos; audit and provider-code fixes; four promotions incl. one to `release/prod_1.0` |
| Engineering Rigor | 5 | **Observed Fact:** both refactor PRs template-only bodies (one is 124 files); 0 tests; opened-to-merged in ≤ 22 min |
| Code Review Contribution | 2 | **Observed Fact:** 7 approvals, 7 empty — `#602` (182 files, −437k lines), `#527` (337 files), `#281` production 23 s after opening (5th consecutive report) |
| Observable Devin Leverage | 4 | **Observed Fact:** 8 Devin findings on `#602` unanswered before the UAT merge; Devin Review on his own PRs not answered in-window |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 8 | **Observed Fact:** 93 commits week, present every day |

**Trend:** Improved from NR to rated (yesterday's card lacked authored work); review dimension unchanged at 2.

---

## avinash-codio — Medicodio — **4.7 Needs Support** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#420` per-chart gate-threshold fix merged; `#415` still open |
| Engineering Rigor | 4 | **Observed Fact:** template-only body on a 22-file behaviour change; no tests; merged 9 min after opening |
| Code Review Contribution | NR | No reviews given in-window |
| Observable Devin Leverage | 3 | **Observed Fact:** 5 findings on `#420` (merged 6 min later) and 2 on `#415` unanswered |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 6 | **Observed Fact:** 11 commits week, 71 month, promotion-shaped |

**Trend:** Insufficient Data (was NR).

---

## svh-medicodio — Global Codio — **4.4 Needs Support** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#1258` closed unmerged after 5 days; `#1284` (113 files) and `#1295` (43 files) opened. **Inference:** `#1284` supersedes `#1258` — the work exists but has not reached a reviewable state in six days |
| Engineering Rigor | 4 | **Observed Fact:** both bodies template-only; 0 tests; TipTap replacing `execCommand` is sound |
| Code Review Contribution | 2 | **Observed Fact:** 0-char approvals on `#1297` (191 files → uat) and `#1298` (→ `main`), 13 s before the author merged |
| Observable Devin Leverage | 4 | **Observed Fact:** 17 findings unanswered (17 h / 8 h) |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 6 | **Observed Fact:** 18 commits week, 135 month |

**Trend:** Insufficient Data (was unrated for inactivity).

---

## NandanDate-Medicodio — Medicodio — **4.4 Needs Support** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 5 | **Observed Fact:** 2 merges (`#419` → prod, `#420` → uat); no authored change |
| Engineering Rigor | 4 | **Observed Fact:** `#419` merged to `release/prod_3.0` with no review recorded; `#420` merged 6 min after 5 Devin findings |
| Code Review Contribution | 2 | **Observed Fact:** `okay` on `#420` (22 files), merge 6 s later — third report with the same word |
| Observable Devin Leverage | 3 | **Observed Fact:** findings unanswered; one flagged a file outside the diff |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 7 | **Observed Fact:** 37 commits week (24 merges), 158 month |

**Trend:** Regressed (4.7 → 4.4).

---

## Medicodio-Amit — Medicodio — **NR** (Low confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 5 | **Observed Fact:** `#419` (uat → prod_3.0) merged by another member; no commits or reviews by him |
| Engineering Rigor | NR | No authored change in-window |
| Code Review Contribution | NR | No reviews |
| Observable Devin Leverage | NR | No evidence (the `#411` findings unanswered pattern is historical, not in-window) |
| Automation of Repetitive Work | NR | No evidence |
| Consistency Across Windows | 5 | **Observed Fact:** 8 commits week, 68 month |

Two rated dimensions → overall NR.

---

## shaheen-khan11 — Medicodio — **NR** (Low confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | NR | **Observed Fact:** `#521` closed unmerged; no other event — insufficient to rate |
| Engineering Rigor | NR | — |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | — |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 6 | **Observed Fact:** 15 commits week, 67 month |

---

## sumedh-codio — Medicodio — **NR** (Low confidence)

No in-window activity. Week: 22 merges with 22 empty approvals (previously noted). All dimensions NR.

---

## hitesh (`hiteshjrxmedicodio`) — Medicodio — **NR** (Low confidence)

No in-window activity attributable to him. Week: 3 commits. All dimensions NR.

---

## How to read the spread

**Observed Fact.** The spread is 7.6 to 4.4 among rated members, with two Solid, nine Mixed, three Needs Support and four NR. The top two are separated from the rest almost entirely by Engineering Rigor and Review — the two members who wrote down what they verified, answered bot findings with commits, and disclosed their own errors. The bottom three share one behaviour: substantial or production merges approved with nothing written (including one production merge with no review at all) and Devin findings left unread. Nobody scored above 7 on Automation; the day's repetitive work — promotion PRs, review logs, template bodies, per-facility prompt edits — was done by hand by everyone who did it.

**Inference.** The scores separate along the review-culture axis more than along product lines: Global Codio's verification improved (7 `test(` commits, `packages/*` suites in CI, a gate that produced a real verdict) while its release control regressed (that verdict was promoted to production, 13 of 14 approvals empty). Medicodio's cadence is steady and its review quality is unchanged at 11 of 11 low-information approvals, with `#528` the first sign of a test culture. Confidence is High only where a member left enough written trace to judge; Low confidence and NR are consequences of missing Devin/Jira telemetry and light days, not judgements about the person.

**Recommendation.** Read the trend line on each card before the number. Use the cards to pick tomorrow's conversations — anirudh and ragha82 on the promoted NOT READY, Nandan on the no-review production merge, svh on the template bodies — not to rank people. Do not compare Needs Support and NR: the former has evidence, the latter does not. Restore Devin session access and Jira before treating "Observable Devin Leverage" as a measure of Devin adoption.

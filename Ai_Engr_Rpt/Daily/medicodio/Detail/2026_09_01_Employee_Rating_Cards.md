# Employee Rating Cards — 2026-09-01

**Review window:** 2026-08-31 03:00 → 2026-09-01 03:00 UTC (Monday). Comparison windows: previous day 2026-08-30 (Sunday, zero activity), previous working day 2026-08-28 (Friday), week 2026-08-25 → 09-01, month 2026-08-02 → 09-01.
**Products are separate contexts.** Medicodio and Global Codio are scored against their own repositories, release trains and review conventions. No score is transferred across the boundary.

## Scoring limitations — read before the numbers

1. **Devin session telemetry is unavailable.** `devin_session_search` returns `HTTP 403 — Missing required permission 'org.sessions.view'`. There is no session count, prompt text, scoping quality, acceptance-criteria evidence, ACU-ish effort signal, tests-requested flag or correction-burden data for anyone. **Observable Devin Leverage is therefore scored only from GitHub artefacts** — `Co-Authored-By: Devin AI` trailers, PRs authored by `devin-ai-integration[bot]`, Devin Review comments, and whether those findings were answered. Where a member shows none of those signals, the dimension is **NR**, not a low score: absence of evidence here is a measurement gap, not evidence of absence.
2. **Volume is not productivity.** Commits, PR counts, lines changed and review counts are not scored. A 34-commit day and a 2-commit day can both score well or badly; what is scored is whether the work landed safely, was verified, was reviewed with recorded reasoning, and used automation where automation was the right tool.
3. **One day is not a verdict.** Consistency Across Windows is the only dimension that reaches beyond the review day. The previous day was an empty Sunday, so day-over-day movement is not scorable for anyone; the previous *working* day (Friday 08-28) is used where a comparison is meaningful.
4. **Jira is unavailable** (installed, no callable tool) and **Sentry is unauthenticated**, so planning follow-through and production error impact are outside the evidence base.
5. **NR rules.** A dimension with no in-window evidence is **NR** and is excluded from the weighted average. A member with fewer than three rated dimensions receives an overall of **NR** rather than a low score.
6. Members with no in-window activity are not scored and do not appear below. That is an observation about the window, not about them.

## Rubric

| Dimension | Weight | 1–3 | 4–6 | 7–8 | 9–10 |
| --------- | ------ | --- | --- | --- | ---- |
| **Delivery & Follow-Through** | 25 | Work stalls; nothing reaches a reviewable state; carried items untouched | Work lands but leaves loose ends, or accumulates without a PR | Work lands complete, with follow-through on what it breaks | Lands complete, closes carried items, and leaves the tree better than found |
| **Engineering Rigor** | 25 | No verification; risky changes shipped blind | Some verification; tests or documentation missing where they mattered | Tests or documented verification accompany behaviour changes | Reproduction tests, design docs and honest failure reporting are routine |
| **Code Review Contribution** | 15 | No review, or content-free approvals on substantial diffs | Reviews given but thin relative to diff size | Written verdicts naming what was checked | Architect-level reviews verified against the schema/spec, with recorded decisions |
| **Observable Devin Leverage** | 15 | Devin output ignored or findings left unanswered | Devin runs but its output is not consumed | Devin findings answered and acted on before merge | Devin used to remove the team's repetitive work, not just to write code |
| **Automation of Repetitive Work** | 10 | Repetitive work repeated by hand with no attempt to remove it | Repetition recognised but unchanged | Some repetition removed or scripted | Builds the tooling that removes repetition for others |
| **Consistency Across Windows** | 10 | Erratic; long gaps with no explanation | Present but uneven across the week | Steady across day, week and month | Steady and improving across all three windows |

**Bands:** Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5 · **NR** = fewer than three rated dimensions.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| ------ | ------- | ------- | ---- | ------------- | ---------- | ----------- | ---------- | --------------- | ---------------- | ---------- |
| SaijyotiMeti | Global Codio | **7.8** | Solid | 8 | 8 | 9 | 7 | 5 | 9 | High |
| hitesh (`hiteshjrxmedicodio`) | Medicodio | **7.6** | Solid | 8 | 8 | NR | 8 | NR | 5 | Medium |
| anirudh-medicodio | Global Codio | **7.2** | Solid | 8 | 7 | NR | 6 | 6 | 9 | High |
| ragha82 | Global Codio | **6.4** | Mixed | 7 | 5 | 3 | 9 | 9 | 7 | Medium |
| shaheen-khan11 | Medicodio | **6.3** | Mixed | 8 | 6 | NR | NR | 3 | 6 | Medium |
| sameer-s-mansur | Medicodio | **6.2** | Mixed | 8 | 5 | NR | NR | 3 | 8 | Medium |
| jatinkushwaha-medicodio | Medicodio | **6.1** | Mixed | 8 | 6 | 3 | NR | 4 | 8 | High |
| amit-pandey-medicodio | Medicodio | **5.9** | Mixed | 8 | 6 | 2 | NR | 4 | 8 | High |
| akanksh-rv | Global Codio | **5.2** | Mixed | 5 | 7 | 3 | NR | 4 | 6 | High |
| Medicodio-Amit | Medicodio | **4.5** | Needs Support | 5 | NR | NR | 4 | NR | 4 | Low |
| svh-medicodio | Global Codio | **NR** | NR | 5 | NR | 4 | NR | NR | NR | Low |

Confidence reflects how much in-window evidence exists for that member, not how good the outcome was. Every "Devin" score in this grid is a GitHub-artefact proxy (see limitation 1).

---

## SaijyotiMeti — 7.8 (Solid) · Global Codio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** landed `#1239` (HR reports hub, 186 files) and shipped the fixes that got `#1269` merged; also repaired three content-sync tests broken by someone else's merge |
| Engineering Rigor | 8 | **Observed Fact:** 4 test commits including forbidden-path coverage and bound-parameter assertions; fixed a real multi-tenant defect (`scope all 8 report views to the switched-to org`); documented PRD drift. **Inference:** rigor is high but the feature merged before its QA gate returned |
| Code Review Contribution | 9 | **Observed Fact:** two ~6,000-character architect/EM reviews verified against `schema.prisma`, with committed review logs. 10 of the org's 11 human comments today |
| Observable Devin Leverage | 7 | **Observed Fact:** corrected 4 verified Devin findings on `#1239` and documented 2 as needing a product decision. **Inference:** consumption of Devin output is strong; no delegation of new work observed |
| Automation of Repetitive Work | 5 | **Observed Fact:** 6 hand-written review-log commits for data the gate runner already produces |
| Consistency Across Windows | 9 | **Observed Fact:** 118 commits in the week, 459 in the month, and substantive reviews on both of the last two active days |

**Strength:** she is the only person in either product supplying written review reasoning, and she acts on automated findings rather than clicking past them.
**Watch:** `#1239` was approved by her at 01:52:52 and merged by her 18 seconds later; its QA gate returned "feature untested" 22 minutes after the merge.
**Recommendation:** delegate the HR-report persona/permission matrix as code-level tests — that is the gap the QA automation structurally cannot close.

---

## hitesh (`hiteshjrxmedicodio`) — 7.6 (Solid) · Medicodio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#518` reverted the Prediction Trail stage rail cleanly and merged the same day |
| Engineering Rigor | 8 | **Observed Fact:** the revert names the restored SHA (`4e574cb9`) and the superseded PR (`#500`) and asserts the file is byte-identical; 3,287-character body |
| Code Review Contribution | NR | No review events in-window |
| Observable Devin Leverage | 8 | **Observed Fact:** `fix(prediction-trail): address Devin review on the restored stage rail` — findings answered with code before merge |
| Automation of Repetitive Work | NR | No evidence either way in-window |
| Consistency Across Windows | 5 | **Observed Fact:** 11 commits in the week, 85 in the month, concentrated in bursts |

**Strength:** the cleanest single change in the Medicodio repos today, and one of only two observed cases of Devin Review findings being consumed.
**Watch:** commits land under the unlinked email `hitesh.ms@medicodio.ai`, flagged since 08-23, so his contribution is invisible to account-based attribution.
**Recommendation:** link the email, then delegate visual-regression snapshots for the stage rail so the next UI direction change is caught in review rather than by revert.

---

## anirudh-medicodio — 7.2 (Solid) · Global Codio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** four content-sync PRs opened and merged the same day, including a fix titled as having "made every bundle unimportable" |
| Engineering Rigor | 7 | **Observed Fact:** round-trip test against a live database plus an HLD for the async import design. **Observed Fact against:** four defects of the same class escaped in one day, and one commit landed with the message "Implement feature X to enhance user experience and optimize performance" |
| Code Review Contribution | NR | No review events in-window |
| Observable Devin Leverage | 6 | **Observed Fact:** Devin QA gates ran on all four PRs; `#1267` reported "NOT READY: central behaviour untested + red spec on dev" and two further merges followed it. **Inference:** the output was produced and not consumed |
| Automation of Repetitive Work | 6 | **Observed Fact:** the write-batching change (`#1270`) removes real per-row cost; no automation of his own repeated defect-hunting |
| Consistency Across Windows | 9 | **Observed Fact:** 169 commits in the week, 811 in the month, steady across every active window |

**Strength:** he shipped the regression test that would have caught his own defect and said so in the PR title — exactly the behaviour the 08-27 and 08-28 reports asked for.
**Watch:** every one of his four merges followed a content-free approval by 0.1–0.8 minutes.
**Recommendation:** delegate a content-sync type-coverage corpus with today's four defects as acceptance criteria; it converts one-at-a-time firefighting into a permanent gate.

---

## ragha82 — 6.4 (Mixed) · Global Codio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** merged five Global Codio PRs, each with a green `dev` deployment; `#1250` remains open since 08-27 |
| Engineering Rigor | 5 | **Observed Fact:** merges 0.1–0.8 minutes after his own empty approvals; `#1266` merged before its own QA gate reported NOT READY |
| Code Review Contribution | 3 | **Observed Fact:** 3 approvals, all empty bodies |
| Observable Devin Leverage | 9 | **Observed Fact:** the `feat/qa-automation` branch he pushed produced six Devin QA/documentation PRs today — post-merge gates for `#1266`, `#1270`, `#1271`, `#1269`, `#1239` plus two as-built docs PRs. This is the largest observable Devin footprint in the org |
| Automation of Repetitive Work | 9 | **Observed Fact:** he is the only member using AI to remove the team's own repetitive work (QA execution and as-built documentation) rather than to write features |
| Consistency Across Windows | 7 | **Observed Fact:** 8 commits in the week, 27 in the month; contribution is the automation, not the commit count |

**Strength:** the QA automation is the highest-leverage AI work in either product, and its gates report their own limitations honestly instead of passing silently.
**Watch:** four of six gates reached no verdict for lack of hosted-dev personas, and the one gate that said NOT READY did not stop anything.
**Recommendation:** delegate a seeded QA persona script for hosted-dev and promote the gate verdict to a required status check — one fix turns the whole automation from advisory into authoritative.

---

## shaheen-khan11 — 6.3 (Mixed) · Medicodio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** the CPT-MOD-ICD Final Summary shipped end-to-end — backend field, frontend column, toggles and Excel export — in one day |
| Engineering Rigor | 6 | **Observed Fact for:** he extracted the shared code-linking logic and added regression tests, the only Medicodio regression tests observed in the window. **Observed Fact against:** the same change went to `release/prod_1.0` as "Prod fix issue" with a badge-only body |
| Code Review Contribution | NR | No review events in-window |
| Observable Devin Leverage | NR | No Devin trailer, no recorded response to Devin Review |
| Automation of Repetitive Work | 3 | **Observed Fact:** the dev→prod duplication was done by hand, and two column-visibility edge cases were fixed individually rather than covered by a matrix |
| Consistency Across Windows | 6 | **Observed Fact:** 6 commits in the week, 39 in the month; first observed activity since Friday |

**Strength:** he landed the first Medicodio regression tests of the collected week, directly against a finding that has been open since 08-27.
**Watch:** the production promotion carrying that work has no title, no description and no independent reviewer; it deployed to production at 08:02.
**Recommendation:** carry the dev PR's title and body into the promotion so a production change is reconstructable from the repository alone.

---

## sameer-s-mansur — 6.2 (Mixed) · Medicodio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** two client onboardings (Capital Orthopedic, Wilkes-Barre) plus the Elaris primary-payer header and provider-scoped KB mappings, all landed |
| Engineering Rigor | 5 | **Observed Fact:** no tests; both PRs carry the 448-character badge-only template body; a wrong KB mapping is a silent data-quality defect |
| Code Review Contribution | NR | No review events in-window |
| Observable Devin Leverage | NR | No Devin signal in-window |
| Automation of Repetitive Work | 3 | **Observed Fact:** the same five-step onboarding sequence was executed by hand for the third and fourth clients this month |
| Consistency Across Windows | 8 | **Observed Fact:** 58 commits in the week, 206 in the month, steady onboarding throughput |

**Strength:** clear, plain commit subjects make the onboarding history readable without opening diffs.
**Watch:** `#268` (15 files) and `#269` (11 files) were both self-merged with zero review events of any kind.
**Recommendation:** delegate a client-onboarding scaffold generator using today's two clients as acceptance fixtures — the highest-value repetitive-work removal in the integration repo.

---

## jatinkushwaha-medicodio — 6.1 (Mixed) · Medicodio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** break-glass approver routing delivered across backend and frontend, four PRs merged into `Dev_1.0` |
| Engineering Rigor | 6 | **Observed Fact for:** PR bodies (701–826 chars) state the rule and its rationale, above the Medicodio norm. **Observed Fact against:** an access-control rule was changed three times in one day with no test commit |
| Code Review Contribution | 3 | **Observed Fact:** one approval, body "lgtm", merged 5 seconds later |
| Observable Devin Leverage | NR | No Devin signal in-window |
| Automation of Repetitive Work | 4 | **Observed Fact:** six PRs opened for three logical changes through manual dev/prod fan-out |
| Consistency Across Windows | 8 | **Observed Fact:** 43 commits in the week, 148 in the month |

**Strength:** his PR bodies are the most informative in the Medicodio repos, in a codebase where template-only bodies are normal.
**Watch:** this is security-relevant routing (who can approve a break-glass request) shipping with no test pinning the routing table, and two production PRs (`#594`, `#514`) are queued behind it.
**Recommendation:** delegate an approver-routing decision-table test suite before those two PRs are promoted.

---

## amit-pandey-medicodio — 5.9 (Mixed) · Medicodio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** `#598` fixed a PE-integration constraint violation that silently stranded charts, and shipped a self-heal for already-affected rows |
| Engineering Rigor | 6 | **Observed Fact for:** the best defect write-up in the Medicodio repos today — constraint named, failure mode explained, invisibility of the symptom called out. **Observed Fact against:** no test accompanies the state-machine fix |
| Code Review Contribution | 2 | **Observed Fact:** 9 review events, all with empty bodies, including the two production promotions he merged 8 seconds after approving |
| Observable Devin Leverage | NR | No Devin signal in-window; 19 Devin-trailer commits in the month sit under the unlinked email `amit.p@medicodio.ai` |
| Automation of Repetitive Work | 4 | **Observed Fact:** approvals batched by hand across every open PR; no automation of the promotion flow he administers |
| Consistency Across Windows | 8 | **Observed Fact:** 30 commits in the week (plus 19 under the unlinked email), 203 in the month |

**Strength:** when he writes a defect PR, it is the clearest artefact in the repo.
**Watch:** he is effectively the sole review control for Medicodio, and that control produced nine empty approvals today — two of them gating production. This is the org's largest single control gap and it has been named in seven prior reports.
**Recommendation:** stop being the sole approver on `release/prod_1.0`; nominate a second reviewer and record a one-line verdict on production promotions.

---

## akanksh-rv — 5.2 (Mixed) · Global Codio

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 5 | **Observed Fact:** 34 authored commits on `feat/ai-cm-draft-support-letter-skill`, third consecutive day with no PR; nothing of his own authorship reached `dev` this week |
| Engineering Rigor | 7 | **Observed Fact:** added branch coverage tests, corrected three stale specs, and recorded "the seven test failures they caught" plus an explicit out-of-scope note |
| Code Review Contribution | 3 | **Observed Fact:** approved `#1269` (80 files, +6,318/−632) with the 8-character body "approved" and merged it one minute later |
| Observable Devin Leverage | NR | No Devin signal; 43 of the branch's 50 commits carry a Claude trailer, and with no PR, Devin Review never runs on this work |
| Automation of Repetitive Work | 4 | **Observed Fact:** standards-audit and remediation logs hand-written each phase, for data the gate runner already emits |
| Consistency Across Windows | 6 | **Observed Fact:** 67 commits in the week, 402 in the month, all on one un-PR'd branch |

**Strength:** the branch discipline inside the branch is good — he runs his own gates and reports his own failures honestly.
**Watch:** without a PR there is no CI, no Devin Review and no human reviewer on three days of substantial work; this is the third report to say so.
**Recommendation:** open a draft PR today so the remaining phases are gated continuously rather than in one batch at the end.

---

## Medicodio-Amit — 4.5 (Needs Support) · Medicodio (NextGen Codio Engine)

**Confidence: Low.** Three rated dimensions, all from a small evidence base. This score reflects the review-and-landing loop around his work, not the difficulty or quality of the engine changes themselves, which the data does not let us assess.

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 5 | **Observed Fact:** one feature commit on `feat/amit/combination-code-redesign`; `#411` open since 08-27 and `#393` a draft since 08-25 |
| Engineering Rigor | NR | No test, documentation or verification evidence either way in-window |
| Code Review Contribution | NR | No review events in-window |
| Observable Devin Leverage | 4 | **Observed Fact:** Devin Review posted 4 inline comments plus a summary at 05:13 and 4 more plus a summary at 09:53 on `#411`; none are answered. **Observed Fact (not his fault):** the repo's `Claude PR Review Fix` workflow fired 10 times against those events and every run was skipped or cancelled |
| Automation of Repetitive Work | NR | No evidence either way in-window |
| Consistency Across Windows | 4 | **Observed Fact:** 3 commits in the week, 62 in the month |

**Strength:** the branch is kept merged up from `uat`, so the eventual PR will not carry a stale base.
**Watch:** two open items at 5 and 7 days with eight unanswered automated findings, in a repo whose automated remediation workflow is itself broken.
**Recommendation:** answer or dismiss the eight Devin Review comments on `#411` with reasons and request a named human reviewer; separately, someone should fix why `Claude PR Review Fix` skips every run.

---

## svh-medicodio — NR · Global Codio

Two rated dimensions, below the three-dimension threshold, so **no overall score is assigned**. This is a measurement outcome, not a judgement.

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 5 | **Observed Fact:** no commits in-window; `#1258` open since 08-28, updated today with a written summary of the fixes made in response to review |
| Engineering Rigor | NR | No in-window code changes to assess |
| Code Review Contribution | 4 | **Observed Fact:** one approval with an empty body on `#1263` (27 files), 30 seconds before merge |
| Observable Devin Leverage | NR | No Devin signal in-window |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | NR | 31 commits in the week and 135 in the month exist, but with two in-window events there is no basis to rate steadiness for this date |

**Strength:** he answers review feedback in writing on his own PR and states what changed — a habit most of the org does not have.
**Watch:** `#1258` is in its fourth day awaiting a human verdict.
**Recommendation:** get `#1258` a named reviewer and a date; the code has been ready since 08-28.

---

# How to read the spread

**Observed Fact.** The scores cluster between 5.2 and 7.8 with one NR and one Needs Support. Delivery scores are uniformly high (5–8, mostly 8): almost everyone landed real work. The spread is created almost entirely by two dimensions — **Code Review Contribution** (2, 3, 3, 3, 4, 9 where rated) and **Automation of Repetitive Work** (3, 3, 4, 4, 5, 6, 9). Engineering Rigor is mid-to-high across the board. In other words, the team's *output* is healthy and its *controls* are not.

**Observed Fact.** Two members sit outside that pattern in opposite directions. SaijyotiMeti scores 9 on review because she writes verdicts nobody else writes; ragha82 scores 9 on Devin leverage and automation because he is building the tooling that removes other people's repetitive work. Both are single points of dependency: remove either and the corresponding control disappears from the organisation entirely.

**Inference.** The low review scores are not a competence signal. Nine empty approvals from one person in one day, and 17 content-free events out of 19 org-wide, describe a *process* in which approval is a merge mechanic rather than a review — an arrangement that would produce these numbers regardless of who held the button. Scoring the individuals without saying that would be unfair to them.

**Inference.** Every "Devin" score in this grid is a proxy built from GitHub artefacts, because session telemetry is inaccessible. Members who used Devin in ways that leave no GitHub trace are systematically under-credited here, and the four NRs in that column should be read as "not measurable", not "did not use".

**Inference.** The Medicodio scores cluster slightly lower than Global Codio's, and the mechanism is visible in the dimension detail: Global Codio has test-bearing commits, written reviews and QA gates in its workflow; Medicodio has almost none of those, so its members lose points on Rigor and Review for working the way their repository's conventions permit. This is a product-level difference, not eleven individual ones.

**Recommendation.** Three changes would move most of this grid, and none of them are about working harder:
1. **A one-line written verdict required on every approval, and a non-author approver required on `release/prod_1.0`.** This addresses the dimension where six of nine rated members score 4 or below.
2. **Seeded QA personas in hosted-dev.** Four of six Devin QA gates reached no verdict today purely for lack of credentials; fixing it makes the automation authoritative and raises the observable-leverage evidence base for everyone.
3. **Restore `org.sessions.view` for this automation.** Until then, one of the six dimensions is measured through a keyhole, and the fairest reading of every Devin score in this document is "provisional".

---

*Scores describe one review window against six weighted dimensions. Volume is not scored as productivity. Observed Fact = present in the gathered data; Inference = a reading of that data; Recommendation = a proposed action. MediCodio AI © 2026. All Rights Reserved · www.medicodio.ai*

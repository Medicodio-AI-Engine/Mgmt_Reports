# Employee Rating Cards — 2026-09-02

**Review window:** 2026-09-01 03:00 → 2026-09-02 03:00 UTC (Tuesday). Comparison windows: previous working day Mon 08-31, week 08-26 → 09-02, month 08-03 → 09-02.
**Companion report:** `2026_09_02_Mgmt_Activity_Report.md` (same directory) holds the evidence each card cites.

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable.** `devin_session_search` returned `403 Missing required permission 'org.sessions.view'` for the 12th consecutive run. Nothing about prompts, scoping, acceptance criteria, tests requested, correction burden or ACU is observable. **Observable Devin Leverage** is therefore scored only from GitHub artefacts: `Co-Authored-By: Devin AI` trailers, `devin-ai-integration[bot]` PRs, Devin Review findings and whether they were answered before merge. A member who used Devin in sessions that left no GitHub trace is under-scored on this dimension, and the card says so where it is likely.
- **Jira is not callable and Sentry has no token**, so Support, Meetings/Coordination and incident work are invisible. Members whose day was spent there will look quiet here.
- **Volume is not productivity.** Commit, PR and review counts appear only as evidence of *shape* (e.g. "0 tests on 21 commits"), never as the basis for a score.
- **NR (Not Rated)** marks a dimension with no in-window evidence either way; it is excluded from the weighted average. A member with fewer than three rated dimensions receives an overall **NR**, not a low score.
- **Members with no in-window activity are not carded** (hitesh `hiteshjrxmedicodio`, svh-medicodio, Amrutha-Beedikar, vishnu-saikarthik, Shashvi1) — one quiet day is not evidence.
- Product contexts are separate: Global Codio cards are not compared against Medicodio cards, whose review culture, CI and release trains differ.

## Rubric

| Dimension | Weight | 1–3 | 4–6 | 7–8 | 9–10 |
| --------- | ------ | --- | --- | --- | ---- |
| **Delivery & Follow-Through** | 25 | Work stalls; nothing reaches a reviewable state; carried items untouched | Work lands but leaves loose ends, or accumulates without a PR | Work lands complete, with follow-through on what it breaks | Lands complete, closes carried items, and leaves the next person nothing to clean up |
| **Engineering Rigor** | 25 | No verification; risky changes shipped blind | Some verification; tests or documentation missing where they mattered | Tests or documented verification accompany behaviour changes | Reproduction tests, design docs and honest failure notes are routine |
| **Code Review Contribution** | 15 | No review, or content-free approvals on substantial diffs | Reviews given but thin relative to diff size | Written verdicts naming what was checked | Architect-level reviews verified against the schema/spec, with record |
| **Observable Devin Leverage** | 15 | Devin output ignored or findings left unanswered | Devin runs but its output is not consumed | Devin findings answered and acted on before merge | Devin used to remove the team's repetitive work, not just to write code |
| **Automation of Repetitive Work** | 10 | Repetitive work repeated by hand with no attempt to remove it | Repetition recognised but unchanged | Some repetition removed or scripted | Builds the tooling that removes repetition for others |
| **Consistency Across Windows** | 10 | Erratic; long gaps with no explanation | Present but uneven across the week | Steady across day, week and month | Steady and improving across all three windows |

**Bands:** Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5. **Confidence** reflects how much in-window evidence exists, not how good it is.

## Summary grid

| Member | Product | Overall | Band | Delivery (25) | Rigor (25) | Review (15) | Devin (15) | Automation (10) | Consistency (10) | Confidence |
| ------ | ------- | ------- | ---- | ------------- | ---------- | ----------- | ---------- | --------------- | ---------------- | ---------- |
| SaijyotiMeti | Global Codio | **7.7** | Solid | 8 | 8 | 8 | 7 | 5 | 9 | High |
| SaahilVishwakarma | Global Codio | **7.3** | Solid | 7 | 8 | NR | 8 | 5 | NR | Medium |
| sameer-s-mansur | Medicodio | **6.9** | Mixed | 8 | 6 | NR | 5 | 8 | 8 | High |
| ragha82 | Global Codio | **6.8** | Mixed | 7 | 7 | 3 | 9 | 8 | 7 | Medium |
| akanksh-rv | Global Codio | **5.9** | Mixed | 7 | 6 | NR | 4 | NR | 6 | Medium |
| anirudh-medicodio | Global Codio | **5.9** | Mixed | 6 | 5 | NR | 6 | 5 | 9 | High |
| jatinkushwaha-medicodio | Medicodio | **5.2** | Mixed | 7 | 4 | NR | 3 | 4 | 8 | High |
| Pj-Vineeth-Kumar | Global Codio | **5.1** | Mixed | 4 | 5 | NR | 5 | 6 | 7 | Medium |
| shaheen-khan11 | Medicodio | **4.9** | Needs Support | 7 | 6 | 2 | 3 | 3 | 6 | Medium |
| NandanDate-Medicodio | Medicodio | **4.7** | Needs Support | 6 | 5 | 2 | 3 | NR | 7 | Medium |
| Medicodio-Amit | Medicodio | **4.5** | Needs Support | 6 | 5 | NR | 2 | 3 | 5 | Medium |
| amit-pandey-medicodio | Medicodio | **NR** | NR | NR | NR | 2 | NR | NR | 8 | Low |
| sumedh-codio | Medicodio | **NR** | NR | NR | NR | 2 | NR | NR | NR | Low |
| avinash-codio | Medicodio | **NR** | NR | NR | 3 | 2 | NR | NR | NR | Low |

Dimension means over rated members (Global Codio / Medicodio kept separate): Delivery 6.5 / 6.8 · Rigor 6.5 / 5.0 · Review 5.5 / 2.0 · Devin 6.5 / 3.3 · Automation 6.0 / 4.5 · Consistency 7.6 / 6.8. Previous-day means (09-01 cards, all rated members): Delivery 7.4, Rigor 6.4, Review 4.0, Devin 6.9, Automation 4.8, Consistency 7.1.

---

## SaijyotiMeti — Global Codio — **7.7 Solid** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** drove `#1282` (89 files, 10k lines) from open to merge in 2 h with 19 remediation commits — Inbox undercount, row-click routing, missing `entity_type`/`entity_id`, bounded reads — and closed a three-report Repeat Pattern. **Inference:** the loose end is that two `[needs your decision]` items were merged unresolved |
| Engineering Rigor | 8 | **Observed Fact:** 3 `test(` commits incl. a live-DB integration spec for the ownership JOIN; gate confirmed 36/36 before merge; a false atomicity claim corrected in docs |
| Code Review Contribution | 8 | **Observed Fact:** the organisation's only substantive review today — 6,889 chars, 7 inline verdicts each mapped to a fixing SHA or a decision. Scored 8 not 9 because it was not independent: 19 of the PR's day commits are hers and her own 8-char `approved` preceded her own merge by 12 s |
| Observable Devin Leverage | 7 | **Observed Fact:** 15 Devin Review findings on `#1282` consumed and mapped; 0 Devin-trailer commits. **Inference:** consumption strong, delegation absent |
| Automation of Repetitive Work | 5 | **Observed Fact:** 4 hand-written `docs(review)` log commits (6 yesterday); no attempt to script them |
| Consistency Across Windows | 9 | **Observed Fact:** 138 commits in the week, 478 in the month, substantive review on every active day since coverage began |

**Recommendation:** hand remediation back to the PR author (or a Devin task the author owns) and keep your role to the verdict.

## SaahilVishwakarma — Global Codio — **7.3 Solid** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1283` (57 files, 21 commits) brings AI-extraction values through to case data and is gate-green ("all 13 green"); still open, bot-review only. **Inference:** complete but not yet landed, and too broad to review quickly |
| Engineering Rigor | 8 | **Observed Fact:** privilege-escalation and tenancy fixes with a `test(extraction)` commit asserting the accept path commits; autosave row lock; seven API test failures repaired rather than skipped; deploy runbook for the unique index; "stop the superseded FAIL from reading as the current verdict" |
| Code Review Contribution | NR | No review events given in-window |
| Observable Devin Leverage | 8 | **Observed Fact:** 13 Devin Review findings answered with commits and a per-finding remediation log |
| Automation of Repetitive Work | 5 | **Observed Fact:** 5 hand-written review-log/runbook commits |
| Consistency Across Windows | NR | **Observed Fact:** 0 default-branch commits in the prior week, 98 in the month — insufficient in-window pattern to rate steadiness fairly |

**Recommendation:** split the privilege-escalation fix into its own PR and request a human reviewer today.

## sameer-s-mansur — Medicodio — **6.9 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 8 | **Observed Fact:** Graph redaction (`#270`/`#272`), canonical identifier across three Elaris modules and the loader boundary (`#275`/`#276`), `sheet_identifier_text` import (`#278`), Wilkes-Barre onboarding — all through `Dev_1.0` → `Uat_1.0` → `release/prod_1.0` in one day, with `#274` withdrawn and replaced cleanly |
| Engineering Rigor | 6 | **Observed Fact:** "test through a real workbook" and "test the real loaders" accompany the identifier work; UAT-round PHI-in-logs findings fixed. Held at 6 because "Log LLM prompt and response bodies by default" — a PHI logging decision — was made inside a feature PR with an empty approval, and 4 of 10 PR bodies are template-only |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 5 | **Observed Fact:** Devin Review's 19 inline comments on `#271` were addressed in follow-up commits at UAT stage; the three `Dev_1.0` PRs were self-merged before any finding could be read (13 s, 7 s, 10 min) |
| Automation of Repetitive Work | 8 | **Observed Fact:** `/onboard-facility` skill (`#273`) encodes the Capital/Wilkes-Barre steps "so the next one does not re-derive" — the exact delegation recommended yesterday, delivered next day |
| Consistency Across Windows | 8 | **Observed Fact:** 56 commits in the week, 219 in the month, active every weekday |

**Recommendation:** take the LLM-payload logging default to a named security owner as its own PR/ADR.

## ragha82 — Global Codio — **6.8 Mixed** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1281` merged; 4 stale QA PRs closed; `#1275`/`#1276` still open |
| Engineering Rigor | 7 | **Observed Fact:** root-caused why five QA runs "cost 122.5 ACU and validated nothing" (wrong persona names, no provisioning doctrine) and fixed both in the skill; recorded the setup-project trap and tightened the IDOR assertion |
| Code Review Contribution | 3 | **Observed Fact:** merged `#1250` (1,224 files) into `feat/qa-automation` as author with 0 approvals; no reviews given |
| Observable Devin Leverage | 9 | **Observed Fact:** Devin authored the doctrine change (4 trailer commits), 3 review rounds answered; the change makes every future Devin QA gate cheaper. **Inference:** highest-leverage Devin use in the window |
| Automation of Repetitive Work | 8 | **Observed Fact:** diff-scoped tiers replace the generic smoke every gate re-ran |
| Consistency Across Windows | 7 | **Observed Fact:** 8 commits week, 27 month, present most days |

**Recommendation:** make the QA verdict a required status check on `dev`.

## akanksh-rv — Global Codio — **5.9 Mixed** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1282` opened and merged the same day, closing a three-report pattern. Held at 7 because the landing depended on the reviewer remediating 19 commits' worth of findings |
| Engineering Rigor | 6 | **Observed Fact:** the branch carried tests and a standards audit from prior days (08-31 report); today's only commit is a `dev` merge; the PR body is a full design narrative |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 4 | **Observed Fact:** Devin Review raised 15 findings on his PR; all were fixed by someone else |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 6 | **Observed Fact:** 106 commits week / 439 month, all on one branch with one PR |

**Recommendation:** open the next skill as a draft PR on day one and answer your own Devin findings.

## anirudh-medicodio — Global Codio — **5.9 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1278` grew to 17 commits (async import, live progress, mirror mode with safety-export undo, email-delivery scope) and is still open with bot-only review. Yesterday four scoped PRs merged |
| Engineering Rigor | 5 | **Observed Fact:** 10 fix commits in one day on the same PR — "the third bundle-breaking decode bug", "a seventh ref was missed", "two breaks that never compiled" — and no `test(` commit. **Inference:** the mocked-Prisma root cause named on 08-30 is unaddressed |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 6 | **Observed Fact:** 28 Devin Review inline comments across 9 rounds, each followed by a fix commit. **Inference:** Devin is being used as the missing test suite — consumed, but expensive |
| Automation of Repetitive Work | 5 | **Observed Fact:** the recommended corpus fixture has not appeared (third report) |
| Consistency Across Windows | 9 | **Observed Fact:** 169 commits week, 811 month, daily |

**Recommendation:** land the non-mocked content-sync integration suite before further content-sync features.

## jatinkushwaha-medicodio — Medicodio — **5.2 Mixed** (High confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** 7 PRs, 6 merged (`tracked_roles` default BE+FE, Other-bucket leak BE+FE, `ColumnKey` import, prediction-trail rail); 6 green react deploys |
| Engineering Rigor | 4 | **Observed Fact:** 0 tests on 21 commits; `#525` fixed a compile break his own commit introduced 3 minutes earlier; `#519` (22 files) has a template-only body |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 3 | **Observed Fact:** Devin Review findings on `#524`/`#526`/`#599`/`#600` unanswered; `#524`/`#525` self-merged 97–178 s after approval |
| Automation of Repetitive Work | 4 | **Observed Fact:** BE → FE config mirror hand-kept twice today |
| Consistency Across Windows | 8 | **Observed Fact:** 67 week / 176 month, steady |

**Recommendation:** a Devin-authored contract test for BE ↔ FE analytics defaults, then stop hand-mirroring.

## Pj-Vineeth-Kumar — Global Codio — **5.1 Mixed** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 4 | **Observed Fact:** 32 Devin-trailer commits across two docs PRs; `#1279` closed unmerged by him (superseding `#1277`, also closed), `#1280` open after 15 review rounds. Nothing landed |
| Engineering Rigor | 5 | **Observed Fact:** as-built annotations correct stale PRD claims against code; PRD rounds converge on contradictions ("resolve ccq/failure/token contradictions"). **Inference:** rigour is being outsourced to Devin Review rather than applied once |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 5 | **Observed Fact:** heaviest Devin author today; but `#1280` = 98 bot review events / 159 inline comments / 23 Devin commits with no human read. **Inference:** Devin-reviews-Devin loop; ACU unobservable |
| Automation of Repetitive Work | 6 | **Observed Fact:** documentation drift correction delegated to Devin — a Good Devin Candidate |
| Consistency Across Windows | 7 | **Observed Fact:** 23 week (16 Devin-trailer) / 157 month (30) — steadiest Devin author in the org |

**Recommendation:** cap automated review rounds at 3 and put a human owner on `#1280`.

## shaheen-khan11 — Medicodio — **4.9 Needs Support** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#520`/`#522`/`#523` merged (Final Summary opt-in, SLA stripe, de-migration ratchet); `#521` prod promotion open |
| Engineering Rigor | 6 | **Observed Fact:** `#523` body explains the ratchet clearly; but it was a 45-minute follow-up to `#522`'s incomplete fix, with no test; `#521` body is `---` |
| Code Review Contribution | 2 | **Observed Fact:** one empty approval (`#525`) |
| Observable Devin Leverage | 3 | **Observed Fact:** Devin Review findings on `#520`/`#522`/`#523` unanswered |
| Automation of Repetitive Work | 3 | **Observed Fact:** second "Prod fix issue" template promotion in two days; column edge cases fixed serially |
| Consistency Across Windows | 6 | **Observed Fact:** 10 week / 43 month |

**Recommendation:** delegate a regression matrix for column visibility so the next migration ships once.

## NandanDate-Medicodio — Medicodio — **4.7 Needs Support** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#416` add-on phrase enrichment merged; merged `#411`/`#414`/`#417`/`#418` for others |
| Engineering Rigor | 5 | **Observed Fact:** concise PR summary; no tests; Devin Review finding on `#416` unanswered |
| Code Review Contribution | 2 | **Observed Fact:** 5 of 5 approvals `okay`, two on production promotions (`#414` 33 files/+4,480 merged 14 s later; `#417` 10 s) |
| Observable Devin Leverage | 3 | **Observed Fact:** 0 Devin-trailer commits today (9 in month); findings unanswered on merged PRs |
| Automation of Repetitive Work | NR | No evidence either way |
| Consistency Across Windows | 7 | **Observed Fact:** 28 week / 123 month; 0 yesterday, 6 today |

**Recommendation:** approvals on `release/prod_3.0` list the PRs included and the UAT evidence.

## Medicodio-Amit — Medicodio — **4.5 Needs Support** (Medium confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#411` merged after 4.7 days (flagged in three reports); `#418` opened and merged in 93 min; `#419` prod promotion open |
| Engineering Rigor | 5 | **Observed Fact:** `#418` body documents the deploy order; then prod config was seeded ahead of the code, inverting it, with a candid 1,200-char disclosure of the interim risk. **Inference:** honesty high, controls low |
| Code Review Contribution | NR | No reviews given |
| Observable Devin Leverage | 2 | **Observed Fact:** 8 Devin Review findings on `#411` never answered; merged anyway |
| Automation of Repetitive Work | 3 | **Observed Fact:** prod config seeded by hand at "the requester's direction" |
| Consistency Across Windows | 5 | **Observed Fact:** 8 week / 67 month, bursty |

**Recommendation:** a config-key drift check that fails when prod config references a key the deployed code does not read.

## amit-pandey-medicodio — Medicodio — **NR** (Low confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Delivery & Follow-Through | NR | No authored work in-window (6 default-branch commits are merges); `#248`/`#249` untouched |
| Engineering Rigor | NR | No authored change to assess |
| Code Review Contribution | 2 | **Observed Fact:** 7 of 7 approvals empty, incl. `#519` (22 files, template body) 6 s before merge — fourth report with this pattern |
| Observable Devin Leverage | NR | None in-window (19 Devin-trailer commits earlier in the week) |
| Automation of Repetitive Work | NR | No evidence |
| Consistency Across Windows | 8 | **Observed Fact:** 54 week / 249 month, present daily |

Two rated dimensions → overall **NR**. **Recommendation:** two-line approval template; the review score alone would be the lowest on the grid and should not stand in for an overall.

## sumedh-codio — Medicodio — **NR** (Low confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Code Review Contribution | 2 | **Observed Fact:** 6 of 6 approvals empty; `#277` (+3,161 → prod) and `#279` merged 7–8 s after approval; `#279` open-to-merge 27 s |
| All other dimensions | NR | Release-gate role only; nothing else observable |

**Recommendation:** three-line promotion approval (UAT build verified, PRs included, rollback path).

## avinash-codio — Medicodio — **NR** (Low confidence)

| Dimension | Score | Basis |
| --------- | ----- | ----- |
| Engineering Rigor | 3 | **Observed Fact:** three promotion PRs (`#414`, `#415`, `#417`) with `---` bodies, one carrying +4,480/−2,051 to production |
| Code Review Contribution | 2 | **Observed Fact:** one `ok` approval |
| All other dimensions | NR | No authored code, Devin or automation evidence |

**Recommendation:** generated promotion body for `release/prod_3.0`.

---

## How to read the spread

**Observed Fact.** Fourteen members were active; eleven have enough evidence to rate. Global Codio's rated members span 5.1–7.7; Medicodio's span 4.5–6.9, with three release-gate roles at NR. The Medicodio Review mean is 2.0 because every one of the 19 Medicodio approvals today was empty or one word; the Global Codio Review mean rests on one person. Devin dimension means are 6.5 (GC) vs 3.3 (Medicodio): Global Codio consumes Devin Review output and has Devin-authored work on branches; Medicodio's Devin findings were unanswered on every merged PR today. Versus the 09-01 cards, Review moved 4.0 → (blended) 4.0 and Devin 6.9 → 5.2 — the latter because today's Devin activity is concentrated in documentation loops and unanswered findings rather than consumed fixes.

**Inference.** The top of the grid is defined by *consuming* review output and writing verification down (Saijyoti, Saahil, ragha82, sameer), not by volume — anirudh and akanksh have the highest commit counts in the org and sit mid-grid because their work landed serially or via someone else's remediation. The bottom of the grid is defined by the merge path, not by the code: template bodies, one-word approvals and seconds-long approval-to-merge on production branches. Pj-Vineeth's 5.1 is the one score most likely to be wrong in either direction, because the value of a 15-round Devin PRD loop cannot be judged without session telemetry.

**Recommendation.** Treat the Medicodio Review mean as the single number to move tomorrow — a two-line approval template applied by Nandan, sumedh and amit-pandey would lift five cards without any change to the code they ship. Grant the reporting automation `org.sessions.view` so the Devin dimension can be scored on sessions rather than on trailers, and make `Mgmt_Reports` private before circulating these cards further.

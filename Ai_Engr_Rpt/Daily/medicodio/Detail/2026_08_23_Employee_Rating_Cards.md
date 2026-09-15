# Employee Rating Cards — 2026-08-23

**Review date:** 2026-08-23 (Sunday, UTC) · **Run date:** 2026-08-24 UTC
**Scope:** the 6 contributors with observable activity on the review date (of ~24 seen across the month)
**Companion report:** `2026_08_23_Mgmt_Activity_Report.md`

> **Weekend caveat — read before comparing.** 2026-08-23 was a Sunday. These cards score the *quality* of what was done on a low-staffing day, not the day's throughput, and they are **not** a like-for-like baseline for weekday cards. Where a dimension has no evidence on the day it is marked **NR** and excluded from the weighted average.
>
> **CI caveat.** `globalcodio-monorepo` had **zero successful CI runs** on the review date (52 failed, 14 cancelled — GitHub Actions billing/spending-limit block, third consecutive day). Rigor scores below credit *locally run* gates and published gate logs, because automated verification was unavailable to everyone in Global Codio through no fault of theirs.

## Scoring model

| Dimension | Weight | What it measures |
| --------- | ------ | ---------------- |
| Delivery | 25% | Did complete, usable units of work land — reviewed and merged, not just committed |
| Rigor | 25% | Tests, gate cycles, real verification, disclosed limits, change sizing |
| Review | 15% | Quality of review given and review sought — written verdicts, not bare approvals |
| Devin | 15% | Whether Devin was used where it gave real leverage, and whether its output was landed and reviewed |
| Automation | 10% | Whether repetitive work was automated away rather than repeated by hand |
| Consistency | 10% | Sustained, predictable contribution across the week/month windows |

Scale 1–10. **NR** = not rated (no evidence); NR dimensions are excluded from the weighted average, and fewer than three rated dimensions yields an overall of **NR**.
Bands: **Strong** ≥ 8 · **Solid** ≥ 7 · **Mixed** ≥ 5 · **Needs Support** < 5.

## Summary grid

| Member | Product | Delivery | Rigor | Review | Devin | Automation | Consistency | Overall | Band |
| ------ | ------- | -------- | ----- | ------ | ----- | ---------- | ----------- | ------- | ---- |
| SaijyotiMeti | Global Codio | 8 | 8 | 9 | 5 | 4 | 8 | **7.3** | Solid |
| akanksh-rv | Global Codio | 8 | 7 | 8 | 6 | 4 | 8 | **7.1** | Solid |
| Amrutha-Beedikar | Global Codio | 7 | 8 | 6 | 4 | 4 | 5 | **6.2** | Mixed |
| sameer-s-mansur | Medicodio (integration) | 7 | 7 | 3 | 4 | 4 | 7 | **5.7** | Mixed |
| anirudh-medicodio | Global Codio | 6 | 6 | 3 | 5 | 4 | 8 | **5.4** | Mixed |
| hitesh | Medicodio (app) | 4 | 5 | 3 | 3 | 4 | 5 | **4.1** | Needs Support |

**Team observations (Observed Fact).** All 5 human review events on the day were substantive Architect+EM write-ups with explicit verdicts — a clear improvement on the week baseline of 124/153 low-information approvals — but they came from only two people. Meanwhile 4 of the day's 8 merges had no independent human review at all, **0** commits carried `Co-Authored-By: Devin AI` (second consecutive zero day), and 93 of 119 commits carried Claude trailers.

---

## SaijyotiMeti — 7.3 · Solid

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 8 | PR #1212 (Document Checklist Goal Agent, 140 files) reviewed by a colleague and merged; PR #1215 opened and merged early 08-24. 59 commits. |
| Rigor | 8 | 6 `test` commits; ran the pre-review `/check`+`/fix` cycle; explicitly held #1213's approval "pending green gates" rather than passing a red/absent CI by default. |
| Review | 9 | Three full Architect+EM reviews with explicit verdicts on #1210/#1211/#1213, each followed by a formal approval, then merged — no bare-approval merges. |
| Devin | 5 | No Devin-authored work; Devin Review findings answered in-thread. AI leverage ran through Claude Code (`claude/document-checklist-goal-agent-*`). |
| Automation | 4 | 21 `docs` commits, largely hand-transcribed review/gate logs; 8 manual `dev` sync merges. |
| Consistency | 8 | 99 commits in the week window, 121 in the month, with review participation rising. |

**Strength (Observed Fact).** She is the reason the day's review record looks different from the week's: every merge she performed was preceded by her own written verdict.
**Watch (Inference).** Review time is being spent on transcription (the review logs) and on 140-file diffs that no reviewer can fully audit — both fixable without touching her judgment.
**Next improvement (Recommendation).** Generate `docs/review-logs/*` from the `/check`+`/fix` output instead of writing them by hand.

---

## akanksh-rv — 7.1 · Solid

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 8 | #1211 (cross-document validation, 91 files) approved and merged; #1210 (Critical compliance fix — reviewed draft was being discarded on send) merged; #1209 remediation landed into the Devin branch. |
| Rigor | 7 | 2 `test` commits and acted on Devin Review findings; disclosed on #1214 that live authenticated API validation was **not** run. Offset: #1214 self-merged at 315 files. |
| Review | 8 | Full Architect+EM review on #1212 with an escalated product decision, then approval and merge. Offset: no reviewer on his own #1214. |
| Devin | 6 | Highest Devin engagement on the team — authored and landed #1209, the remediation for Devin's PR #1208 — but #1208 itself is still unlanded since 08-21. |
| Automation | 4 | The `dev → feat/qa-automation` promotion and its QA audit are still done by hand, as a 315-file PR. |
| Consistency | 8 | 124 commits in the week, 170 in the month. |

**Strength (Observed Fact).** He separates remediation into its own PR rather than force-pushing over a reviewed diff, and he names what he did not verify.
**Watch (Observed Fact).** The promotion/sync PR self-merge with an unfilled template body is now a repeat of the 08-22 pattern.
**Next improvement (Recommendation).** Automate the `dev → feat/qa-automation` sync and move its QA audit pre-merge.

---

## Amrutha-Beedikar — 6.2 · Mixed

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | PR #1213 (email header / case_number, 35 files) reviewed, approved and merged the same day. |
| Rigor | 8 | Published the pre-merge gate verdict *including* the FAIL and its 5 blockers, with the full standards log, before requesting review; 1 `test` commit. |
| Review | 6 | Sought and waited for an independent approval rather than self-merging; gave no reviews on the day. |
| Devin | 4 | No Devin usage; the `/check`+`/fix` blocker pass she ran by hand is exactly the bounded work Devin handles well. |
| Automation | 4 | Hand-written standards log; manual `dev` sync. |
| Consistency | 5 | Low sustained volume — activity arrives in single-PR bursts (1 commit on 08-22, none observed 08-21). |

**Strength (Observed Fact).** She publishes a failing gate result and its resolution instead of presenting a clean-looking branch — the most honest verification record on the team.
**Watch (Inference).** Her contribution is concentrated in occasional bursts, which makes trend assessment weak rather than negative.
**Next improvement (Recommendation).** One bounded Devin task: regression tests for the email/case_number contract, a surface that broke three times in three days.

---

## sameer-s-mansur — 5.7 · Mixed

**Product:** Medicodio (`medicodio-nextgen-integration`)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | Two PRs landed: #228 (Elaris filename pairing, 63 files) and #229 (lock-key attach form, 1 file). |
| Rigor | 7 | Verified against a real dev run and recorded it ("Test the step-11 guard where it actually runs", "Record the real dev run"); small, targeted fix diff on #229. |
| Review | 3 | Both PRs self-merged — #228 eleven minutes after opening, #229 **eight seconds** after opening, i.e. before Devin Review's pass completed. No human reviewer in the loop on either. |
| Devin | 4 | No Devin usage; Devin Review's 3 findings on #228 arrived after the merge. |
| Automation | 4 | The manual dev-run verification he repeats each time is a harness waiting to be built. |
| Consistency | 7 | 47 commits in the week, 162 in the month — steady solo ownership of the integration repo. |

**Strength (Observed Fact).** He tests where the code actually runs and records the run, rather than asserting behavior.
**Watch (Observed Fact).** `medicodio-nextgen-integration` is currently the only product surface with no second pair of eyes on any change.
**Next improvement (Recommendation).** Hold integration merges until the automated review pass reports, and get a standing reviewer assigned.

---

## anirudh-medicodio — 5.4 · Mixed

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 6 | 7 commits (2 `fix`, 2 `test`, 2 `docs`, 1 sync) on `feat/portal-access-control` — another member's PR #1183 — with nothing of his own landing inside the window. |
| Rigor | 6 | Paired fixes with tests in the same session; the access-control surface he worked is security-sensitive and appropriately human-owned. |
| Review | 3 | Merged #1209 into the open Devin branch with **no human review on record** (only a Devin Review bot comment) — recurrence of the pattern flagged on 08-21, when 3/3 of his review events were low-information. |
| Devin | 5 | No Devin authoring; he did move Devin's #1208 forward by landing its remediation — the right instinct, executed without a verdict. |
| Automation | 4 | Late-night manual test/doc top-ups on a long-lived shared branch. |
| Consistency | 8 | 211 commits in the week (highest on the team) and 326 in the month. |

**Strength (Observed Fact).** He spends his effort unblocking other people's branches, not only his own.
**Watch (Observed Fact).** Throughput is not the concern — scrutiny is. His merges continue to land without a written verdict.
**Next improvement (Recommendation).** Record a one-line verdict naming what you verified on every merge you perform; this single habit closes the team's most-repeated pattern.

---

## hitesh — 4.1 · Needs Support

**Product:** Medicodio (`medicodio-nextgen-app-nodejs`, `medicodio-nextgen-app-react`)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 4 | 10 commits (18:30–21:04) across backend and UI, but nothing landed in the window: PRs #562 (130 files, +9,806/−436,982) and #488 (226 files) sat open from 08-21, were closed **unmerged** on 08-24 and replaced by #569/#493. |
| Rigor | 5 | No test commits observed; the day mixes `feat(kb)!` (breaking removal of guideline versioning) with two `revert(ask-ai)` commits and three `version_number` plumbing fixes — scope settled inside the branch rather than before it. |
| Review | 3 | No human review or approval on record for the day's work, and no automated review pass reached it inside the window. |
| Devin | 3 | No Devin usage; the paired backend/UI propagation and the wizard regression suite are textbook bounded delegations left undone. |
| Automation | 4 | Every KB contract change was mirrored across nodejs and react by hand. |
| Consistency | 5 | Commits appear in short late-day bursts and under an email identity (`hitesh.ms@medicodio.ai`) not linked to a GitHub account, which also limits what can be measured about his work. |

**Strength (Observed Fact).** His commit messages are conventionally typed, scoped, and carry `!` breaking-change markers — the intent of every change is legible, including the reverts.
**Watch (Observed Fact).** Six-figure line deltas on branches that were abandoned and re-opened as fresh PRs; a breaking KB data-model decision made without a review record.
**Next improvement (Recommendation).** Split the KB versioning work into daily flag-guarded slices, and link the work email to the GitHub account so authorship and review data become joinable.

---

## How to read the spread

**Observed Fact.** The spread on this day is driven almost entirely by the **Review** dimension, not by output. Delivery scores sit in a narrow 4–8 band, but Review runs 3–9: two members wrote full verdict-bearing reviews on every PR they touched, while four merges on the same day went in with no independent human review at all. Automation is flat at 4 for everyone — nobody removed a repetitive task; the same review-log transcription, promotion syncs and by-hand branch merges recurred.

**Inference.** The Devin column is low across the board (3–6) not because Devin failed, but because the work best suited to it — tests, log generation, sync PRs, paired backend/UI propagation — was routed to hand or to Claude Code (93 of 119 commits carry Claude trailers; 0 carry Devin trailers, for the second day running). The two Devin-authored PRs in flight are unlanded at 3 and 4 days, which is why measured Devin leverage looks near zero even though Devin Review ran on every PR opened and its findings were acted on.

**Recommendation.** Two changes would move most of these cards on the next weekday: (1) require a one-line written verdict on every merge — this alone raises the four low Review scores and closes the team's most-repeated pattern; (2) assign one bounded Devin task per member from the opportunity lists in the companion report, prioritising the email/send-path regression suite and the QA sync automation. Neither depends on people working more; both depend on routing work differently.

**Caveat (Observed Fact).** Organization-wide Devin session data was unavailable this run (`devin_session_search` → HTTP 403, missing `org.sessions.view`, fourth consecutive run), so the Devin dimension is scored from Git artifacts only — trailers, `devin/*` branches, Devin-authored PRs and Devin Review events. Sessions that produced no committed artifact are invisible to these scores. Jira was likewise unavailable, so no ticket-level context informs any card.

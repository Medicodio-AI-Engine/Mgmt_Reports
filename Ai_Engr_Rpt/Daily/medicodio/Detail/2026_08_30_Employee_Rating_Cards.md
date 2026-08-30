# Employee Rating Cards — 2026-08-30

**Review window:** 2026-08-29 03:00 → 2026-08-30 03:00 UTC (Saturday) · **Comparison windows:** previous working day 2026-08-28 (Friday) · week 2026-08-23 → 2026-08-30 · month 2026-07-31 → 2026-08-30.

## Read this before the numbers

**These are not performance ratings.** They score the *observable evidence of engineering practice* in one 24-hour window, from one source, and they are intended to direct management attention — not to rank people.

**Scoring limitations for this date, in order of severity:**

1. **No Devin session telemetry.** `devin_session_search` returns `HTTP 403 — Missing required permission 'org.sessions.view'`. Prompt quality, acceptance criteria, whether tests were requested, correction burden, parallelisation, and any session that produced no PR are all invisible. **Observable Devin Leverage is therefore scored only on GitHub-visible artefacts** — Devin-authored PRs, `Co-Authored-By: Devin AI` trailers, and how a member engaged with Devin Review findings. A member could be using Devin well and score low here.
2. **The review day is a Saturday.** Four people produced observable activity; ten members active earlier in the week produced none. **Those ten are not scored and their absence is not a finding.** Nothing here should be read as a comparison between the four who worked a weekend and the ten who did not.
3. **A four-person population.** Dimension means below are not comparable to the 08-29 cards, which scored sixteen members. Trends per member are used instead.
4. **No Jira and no Sentry data.** Ticket scoping, estimation, and production-incident context are absent.
5. **One window is a small sample.** Where a member has only one observable action, confidence is marked Low or Medium and the score is deliberately conservative.

**Volume is never scored.** Commit counts, PR counts, lines changed and Devin session counts appear as context only. A member who wrote four commits and one careful review can score above a member who wrote forty.

## Rubric

| Dimension | Weight | 1–4 (Needs Support) | 5–6 (Mixed) | 7–8 (Solid) | 9–10 (Strong) |
| --------- | ------ | ------------------- | ----------- | ----------- | ------------- |
| **Delivery & Follow-Through** | 25 | Work stalls, is abandoned mid-stream, or lands broken | Lands, but with loose ends left for others | Lands complete, with open items named | Lands complete and verified end-to-end, including the unglamorous close-out |
| **Engineering Rigor** | 25 | Ships production paths untested; ignores failures | Some tests, thin on the risky paths | Tests the paths that can fail; fixes root causes | Finds and closes the failure classes others miss, and explains why they were missed |
| **Code Review Contribution** | 15 | Approves without content, or does not review | Reviews occasionally, shallow | Substantive reviews that change the outcome | Substantive, independent reviews that raise decisions and are auditable |
| **Observable Devin Leverage** | 15 | No engagement; findings ignored | Passive benefit only | Uses Devin (authoring or review) where it adds value and acts on the output | Delegates or verifies deliberately, with the reasoning recorded |
| **Automation of Repetitive Work** | 10 | Repeats manual work flagged previously | Aware, no action | Removes or reduces one recurring manual step | Systematically eliminates repetition for the team, not just themselves |
| **Consistency Across Windows** | 10 | Erratic or unexplained gaps | Uneven | Steady across day/week | Steady and improving across day/week/month |

**Bands:** Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5.
**NR** = no in-window evidence for that dimension; excluded from the weighted average. A member with fewer than three rated dimensions receives an overall of **NR**, never a low score.

## Summary grid

| Member | Product | Overall | Band | Delivery | Rigor | Review | Devin | Automation | Consistency | Confidence |
| ------ | ------- | ------- | ---- | -------- | ----- | ------ | ----- | ---------- | ----------- | ---------- |
| SaijyotiMeti | Global Codio | **8.5** | Strong | 9.0 | 9.0 | 8.5 | 8.0 | 6.0 | 9.0 | High |
| anirudh-medicodio | Global Codio | **8.1** | Strong | 8.5 | 9.0 | 7.5 | 7.0 | 6.5 | 9.0 | High |
| akanksh-rv | Global Codio | **6.5** | Mixed | 7.5 | 7.0 | NR | 4.0 | 5.5 | 7.5 | Medium |
| Amrutha-Beedikar | Global Codio | **4.1** | Needs Support | 6.0 | 3.0 | 2.0 | NR | NR | 5.0 | Medium |

Dimension means across the four scored members: **Delivery 7.8** (4 rated), **Rigor 7.0** (4), **Review 6.0** (3), **Devin 6.3** (3), **Automation 6.0** (3), **Consistency 7.6** (4).
**Do not compare these means to the 08-29 cards** (Delivery 7.0, Rigor 6.0, Review 3.4, Devin 4.0, Automation 6.3, Consistency 6.4): that population was sixteen members across both products, this one is four Global Codio engineers on a weekend. The comparison that *is* supported is per member, and it appears in each card.

## Cards

### SaijyotiMeti — Global Codio — Overall 8.5 (Strong) — Confidence High

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery & Follow-Through | 9.0 | Took #1260 (161 files, 80 commits) from a `/check` audit through remediation, review, green gates and merge inside one window, ending in a green `dev` deploy at 06:57:03. Carried three items forward explicitly as "needs your decision" rather than dropping them |
| Engineering Rigor | 9.0 | Fixed two real defects Devin Review raised after verifying each independently; added a regression test for the overdue predicate; **corrected an existing test that had been written to assert the instance-filter bug as correct behaviour**; fixed two test-mock gaps caught by the gate hand-off. 6 of 16 commits touch tests |
| Code Review Contribution | 8.5 | A 6,425-character architect review with four inline comments, each naming the finding it answers and the commit that resolved it, plus a seven-row Stop-and-Check guide with per-row verification commands. Deducted from 10 for approving 20 s after her own review with one Devin finding still unanswered |
| Observable Devin Leverage | 8.0 | The strongest review-side adoption in the collected history: four Devin Review passes triaged, two findings fixed, two documented as dormant with explanatory comments, all recorded in-thread. No authoring delegation observed (0 Devin-trailer commits), which caps this dimension |
| Automation of Repetitive Work | 6.0 | Her de-duplication of status/count logic and consolidation of the mutation-error-toast helper remove repetition in the codebase; the repetitive *process* work (13 hand-written remediation commits, 5 hand-written review logs) was not automated or delegated |
| Consistency Across Windows | 9.0 | Content-bearing review in three consecutive windows; 142 commits and 3 PRs merged across the week; 439 commits and 17 PRs across the month |

**vs previous day:** Improved — on 08-28 she produced the org's only substantive review; this window she added verified bug fixes, a corrected test and a completed close-out.
**Week:** Improving. **Month:** Improving.
**Watch:** approve-and-merge inside the same minute as an unanswered finding; and being both remediator and reviewer of the same branch.

### anirudh-medicodio — Global Codio — Overall 8.1 (Strong) — Confidence High

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery & Follow-Through | 8.5 | Closed out the three-day Devin-authored #1244 with 9 commits, fixed the five gates his own run failed ("all five were mine"), and corrected previously recorded gate results to the real ones. The PR reached a green `dev` deploy at 16:09:18 |
| Engineering Rigor | 9.0 | Found and fixed **seven blockers that were paths which could not work** — an export that always 400'd, a signing secret absent from both Key Vaults, a natural key that could not round-trip, a lane-blind tenancy leak in both directions, a rollback that destroyed the version it overwrote, bindings exporting as `null`, and an expiry sweep racing live imports — and identified the root cause of why the suite missed them: every content-sync spec mocks Prisma, so six tests could not fail |
| Code Review Contribution | 7.5 | A 12,326-character architect review with six inline `[needs decision]` items, two of them Devin-raised and independently verified, spanning schema, memory, scale and tenancy. Reduced from 9 because he is the PR's principal contributor — the review is excellent but not independent, and no second substantive reviewer existed |
| Observable Devin Leverage | 7.0 | Worked inside a Devin-authored PR, credited two Devin Review findings and confirmed them as real; Devin Review replied extending both. No Devin-trailer commits of his own, and the delegated feature arrived as a 125-file PR needing seven human-found blocker fixes |
| Automation of Repetitive Work | 6.5 | Introduced alert-groupable error codes and humanised ids (removes manual triage effort downstream), but hand-fixed the audit findings and hand-wrote three review logs, one of which needed a correction commit |
| Consistency Across Windows | 9.0 | 265 commits across the week and 797 across the month, sustained on one feature; the audit-then-fix practice is unbroken since 08-26 |

**vs previous day:** Stable — same work stream, deeper review.
**Week:** Stable. **Month:** Improving.
**Watch:** merging with six `[needs decision]` items unfiled; being the only substantive reviewer of a PR he principally authored.

### akanksh-rv — Global Codio — Overall 6.5 (Mixed) — Confidence Medium

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery & Follow-Through | 7.5 | #1260 landed and deployed green; eight commits the same day advancing the successor skill through phases 2–12, each commit naming the PRD phase it closes. Deducted because the successor branch has no PR and is accumulating the same way #1260 did |
| Engineering Rigor | 7.0 | 3 of 8 branch commits touch tests, and the phase work is PRD-traceable — but the two real defects in #1260 were found by Devin Review and the reviewer, not by his suite, and one of his tests asserted the buggy behaviour as expected |
| Code Review Contribution | NR | No review events by him in-window. Not penalised |
| Observable Devin Leverage | 4.0 | No Devin-trailer commits, no delegated sub-PRs, no Devin-authored PRs in his name. His benefit from Devin this window was passive — findings raised on his PR and fixed by someone else. This repeats the 08-29 observation unchanged |
| Automation of Repetitive Work | 5.5 | The numbered-phase structure makes his repetitive subscriber/notification/repository-hook work explicitly delegable, but nothing was delegated or scripted |
| Consistency Across Windows | 7.5 | 115 commits and 11 PRs merged across the week; 416 commits and 34 merges across the month. Steady output on one work stream |

**vs previous day:** Stable. **Week:** Stable. **Month:** Insufficient Data — the collected report history contains no individual assessment of him before 2026-08-29, so a monthly *quality* trend is not supported.
**Watch:** branch size before first review; test expectations derived from current behaviour rather than the acceptance criterion.

### Amrutha-Beedikar — Global Codio — Overall 4.1 (Needs Support) — Confidence Medium

Four dimensions are rated, so an overall is reported — but this is a **narrow single-action sample** and should be read as a finding about the *release gate she operates*, not about her capability. Her observable footprint this window is one approval and one merge.

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery & Follow-Through | 6.0 | Unblocked a three-day-old feature branch on a Saturday and the resulting `dev` deploy was green at 16:09:18. That is real delivery value; it is not scored higher because no verification of the merge is visible |
| Engineering Rigor | 3.0 | Merged #1244 (125 files, +25,798) **6 m 22 s after** a review raising six `[needs decision]` items, two of which Devin Review had confirmed as real five minutes earlier, with no intervening commit. No evidence any item was assessed before the merge |
| Code Review Contribution | 2.0 | The deciding approval body was the 8-character string `approved`. This is the fourth consecutive window in which her review artefacts carry no content |
| Observable Devin Leverage | NR | No Devin-attributable activity; her role in the evidence is the release gate. Excluded rather than scored low |
| Automation of Repetitive Work | NR | No in-window evidence either way. The promotion-summary automation recommended on 08-29 has not started, but no promotion PR occurred this window to demonstrate it |
| Consistency Across Windows | 5.0 | Present and reliable across windows (4 PRs opened / 3 merged this week; 23 / 20 this month) with a consistent gate quality problem: no content-bearing review appears anywhere in the collected history |

**vs previous day:** Regressed — the 08-28 release train ran clean but was already flagged for an 8-character approval on a 331-file prod PR; this window the same practice decided a merge over six open items.
**Week:** Needs Attention. **Month:** Needs Attention.
**Note:** the two fixes that would move this score are both process, not skill — a three-line approval template and a CI check that blocks merge on unresolved findings. Both are recommended as tomorrow's actions and neither is her fault alone; she is operating the gate the org gave her.

## How to read the spread

**Observed Fact.** Two engineers wrote the two most substantive reviews in the collected history this window, and both of the merges that shipped were gated by an 8-character approval. Zero `Co-Authored-By: Devin AI` commits were produced for the second consecutive window, while 24 of 26 default-branch commits carried a Claude trailer. Devin Review found two real bugs and confirmed two human findings, and every one of those four was verified by a human before being acted on. Medicodio produced no activity at all.

**Inference.** The spread in this grid is not a spread in effort — it is a spread between *authoring practice*, which is strong and improving in Global Codio, and *gate independence*, which is weak everywhere. The 8.5 and the 4.1 in this table are two halves of the same system: the review work is excellent precisely because the people doing it are the people who wrote the code, and the formal approval is empty precisely because nobody else can absorb a 125-file diff. Scoring the approver low without fixing the size and gate problems would move the number and not the outcome. Separately, the disappearance of Devin authoring alongside heavy Claude-trailer usage suggests a deliberate tool split rather than disengagement — but that cannot be confirmed without session telemetry, and until it is, "Observable Devin Leverage" measures GitHub artefacts, not adoption.

**Recommendation.** Fix the system before the scores. In priority order: (1) block merges while a Devin Review finding or a `[needs decision]` comment is unresolved; (2) require a non-empty approval body and a non-contributor approver on `dev`/`uat`/`main`; (3) enforce a PR size threshold that forces either a split or a named independent architect reviewer; (4) delegate the two non-mocked integration suites (content-sync, `MyAiWorkService` permission matrix) to Devin; (5) grant `org.sessions.view` so the next run can assess Devin adoption on evidence rather than on trailers. Re-score after these land — three of the four cards above would be expected to move without anyone changing how hard they work.

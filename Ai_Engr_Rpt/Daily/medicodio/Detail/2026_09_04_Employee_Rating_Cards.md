# Employee Rating Cards — 2026-09-04

**Review window:** 2026-09-03 03:00 UTC → 2026-09-04 03:00 UTC. Comparison windows: previous working day (09-02 03:00 → 09-03 03:00), week (08-27 → 09-03), month (08-04 → 09-03).
**Companion report:** `2026_09_04_Mgmt_Activity_Report.md` (same directory) — every score below cites evidence that is spelled out there.

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable (HTTP 403, `org.sessions.view`, 12th consecutive run).** *Observable Devin Leverage* is scored only from GitHub artefacts: Devin-trailer commits, `devin-ai-integration[bot]` PRs, QA-gate comments, and whether Devin Review findings were answered, resolved or merged past. Prompt quality, ACU effort, correction rate and tests-requested are unobservable. Where a member has no Devin artefact at all the dimension is **NR**, not a low score.
- **Jira and Sentry are unavailable.** Coordination, support and incident work is invisible; a member who spent the day in meetings or on a live issue may look inactive. *Delivery & Follow-Through* is therefore scored on what reached a branch or a PR, and marked with lower confidence where that is the only evidence.
- **Volume is not scored.** Commit, PR, line, review and finding counts appear in the companion report as context. A score moves only on observable quality signals: was the change described, tested, reviewed by an independent reader, promoted through the train, and were findings answered.
- **NR handling.** A dimension with no in-window evidence is NR and excluded from the weighted average (weights renormalised over rated dimensions). Fewer than three rated dimensions → overall **NR**.
- **Bands:** Strong ≥ 8.0 · Solid ≥ 7.0 · Mixed ≥ 5.0 · Needs Support < 5.0.
- **Confidence:** High = multiple independent artefact types in all windows; Medium = one artefact type or thin history; Low = ≤ 2 in-window events or first appearance.
- Tool identities (`Claude`, `Devin AI`, `devin-ai-integration[bot]`, `github-actions`) and alias identities (`saijyoti`, `saijyoti.m`, `Avinash`, `amit.p`, `vineeth.kumar`, `svhmedicodio`, `anirudhdmedicodio`) are folded into the human account they belong to on e-mail/branch evidence and are not rated separately.

## Rubric

| Dimension | Weight | 9–10 | 7–8 | 5–6 | 3–4 | 1–2 |
| --- | ---: | --- | --- | --- | --- | --- |
| Delivery & Follow-Through | 25 | Scoped work reaches the intended branch through the train with the loop closed (findings, gates, follow-ups) | Work lands; minor loose ends | Work lands but loose ends persist (unanswered findings, open promotions) | Work stalls or lands unverified | Work regresses or breaks something left unrepaired |
| Engineering Rigor | 25 | Root cause quantified, tests with the change, scope disclosed, small reviewable diff | Well-described, mostly tested | Described or tested, not both; large diffs | Template/badge body, no tests, mixed-concern commits | Untested change to production with no description |
| Code Review Contribution | 15 | Independent, evidence-based review that changes the outcome | Substantive comments on peers' PRs | Occasional real comment; mostly short approvals | Empty/one-word approvals only | Empty approvals on production merges |
| Observable Devin Leverage | 15 | Devin used on well-scoped tasks, output reviewed, findings driven to zero | Findings answered with reasons; Devin used where it fits | Findings partly answered | Findings merged past unanswered | Devin output shipped unreviewed |
| Automation of Repetitive Work | 10 | Recurring manual step removed this window | Progress on removing one | Recurring step acknowledged | Recurring step repeated without change | — |
| Consistency Across Windows | 10 | Same quality signals day/week/month | Minor variance | Uneven | One-window spike or lapse | — |

## Summary grid

| Member | Product | Overall | Band | Delivery 25 | Rigor 25 | Review 15 | Devin 15 | Automation 10 | Consistency 10 | Confidence |
| --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| SaijyotiMeti | Global Codio | 7.7 | Solid | 8 | 8 | 9 | 7 | 4 | 9 | High |
| SaahilVishwakarma | Global Codio | 7.9 | Solid | 8 | 8 | NR | 8 | NR | 7 | Medium |
| anirudh-medicodio | Global Codio | 6.7 | Mixed | 8 | 6 | 6 | 6 | 5 | 9 | High |
| Pj-Vineeth-Kumar | Global Codio | 6.5 | Mixed | 7 | 6 | NR | 7 | 5 | 7 | Medium |
| akanksh-rv | Global Codio | 6.4 | Mixed | 7 | 7 | NR | 5 | 6 | 6 | Medium |
| ragha82 | Global Codio | 6.1 | Mixed | 7 | 7 | 2 | 6 | 7 | 7 | High |
| svh-medicodio | Global Codio | 5.8 | Mixed | 6 | 6 | 5 | 6 | NR | 6 | Medium |
| Amrutha-Beedikar | Global Codio | NR | NR | NR | NR | NR | NR | NR | 5 | Low |
| Medicodio-Amit | Medicodio | 6.4 | Mixed | 6 | 7 | NR | 7 | NR | 5 | Medium |
| Shashvi1 | Medicodio | 6.2 | Mixed | 6 | 7 | NR | 6 | NR | 5 | Low |
| ashwinsk-medicodio | Medicodio | 5.9 | Mixed | 7 | 6 | NR | 4 | NR | NR | Low |
| hiteshjrxmedicodio | Medicodio | 5.7 | Mixed | 7 | 6 | NR | 4 | NR | 4 | Low |
| jatinkushwaha-medicodio | Medicodio | 5.1 | Mixed | 6 | 5 | 3 | 4 | 5 | 8 | High |
| sameer-s-mansur | Medicodio | 5.1 | Mixed | 6 | 4 | NR | 3 | 6 | 8 | Medium |
| amit-pandey-medicodio | Medicodio | 4.7 | Needs Support | 6 | 4 | 2 | 4 | NR | 8 | High |
| NandanDate-Medicodio | Medicodio | 4.1 | Needs Support | 5 | 4 | 2 | 3 | NR | 7 | High |
| avinash-codio | Medicodio | 4.1 | Needs Support | 5 | 3 | NR | 3 | NR | 6 | Medium |
| sumedh-codio | Medicodio | NR | NR | NR | NR | 2 | NR | NR | 5 | Low |
| shaheen-khan11 | Medicodio | NR | NR | NR | NR | NR | NR | NR | 5 | Low |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions). Example: SaahilVishwakarma = (8×25 + 8×25 + 8×15 + 7×10) / 75 = 7.9.

## Cards

### SaijyotiMeti — Global Codio — 7.7 Solid (High)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 8 | Three PRs she reviewed reached `dev` (`#1280`, `#1311`, `#1306`); `#1305` (109 files) still open and grew by 8 commits |
| Engineering Rigor | 8 | 1 `test(` + several `fix(test)` commits; verified bugs cited by SHA; product decisions left explicitly open |
| Code Review Contribution | 9 | 3 long-form Architect/EM reviews (7.5k–9.4k chars, 11 inline), one REQUEST CHANGES that changed the outcome; the organisation's only sustained reviewer (39 of 45 human inline comments this week). Held from 10 because all three merges she approved contain 14–20 of her own commits |
| Observable Devin Leverage | 7 | Drove Devin-authored `#1280` to merge after verification; consumed findings on all three PRs; no delegation of the mechanical remediation she did by hand |
| Automation of Repetitive Work | 4 | ≈ 20 mechanical remediation commits + 6 review-log commits done manually again |
| Consistency Across Windows | 9 | Same review depth day/week/month (31 COMMENTED reviews in the month) |

*Change vs 09-03 card:* Review 8 → 9; Delivery 7 → 8. *Next:* hand the `/fix` pass to Devin so the approval is independent of the diff.

### SaahilVishwakarma — Global Codio — 7.9 Solid (Medium)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 8 | `#1304` merged (ten QA findings resolved); `#1312` opened with zero outstanding findings |
| Engineering Rigor | 8 | 6.4k-char body; BCC disclosure fix; atomic terminal outcomes; documented deferred debt and "the gate that lied" |
| Code Review Contribution | NR | No reviews given in-window |
| Observable Devin Leverage | 8 | Devin Review driven 4→5→1→4→0 before requesting human review |
| Automation of Repetitive Work | NR | No recurring step evidenced |
| Consistency Across Windows | 7 | 9 PRs in the month; review contribution thin all month (1 approval) |

*Change vs 09-03:* Delivery 7 → 8. *Next:* one substantive peer review this week.

### anirudh-medicodio — Global Codio — 6.7 Mixed (High)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 8 | Prod hotfix `#1307` through `dev → uat → main` in 3 h 17 min with green deploys; `#1259` finally merged after a 526-commit sync. Held from 9: `#1278` NOT READY still has no fix or waiver |
| Engineering Rigor | 6 | 5 `test(` commits and a 13.8k body with prod numbers; but the sync deleted three shipped capabilities (restored same day) and 25 commits landed inside another person's PR |
| Code Review Contribution | 6 | First substantive review of the week (11.9k, 5 inline) — on a PR where 15 of 19 commits are his; empty approval on his own prod promotion |
| Observable Devin Leverage | 6 | Findings resolved on `#1307`/`#1259`; QA gates on his merges gave no verdict and he did not act on the credential blocker |
| Automation of Repetitive Work | 5 | Branch-drift and post-sync audit remain manual; deleted 148 stale review logs by hand |
| Consistency Across Windows | 9 | Highest, steadiest cadence in the org across all windows |

*Change vs 09-03:* Review 3 → 6; Rigor 7 → 6. *Next:* close `#1278` in writing.

### Pj-Vineeth-Kumar — Global Codio — 6.5 Mixed (Medium)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 7 | `#1311` opened and merged same day; Devin-driven `#1280` merged |
| Engineering Rigor | 6 | 26.8k-char body used as the spec; but 16 of 22 final commits were the reviewer's, and a 57-file single commit sits on a side branch |
| Code Review Contribution | NR | None given |
| Observable Devin Leverage | 7 | The only Devin-authored product code merged this week; 9 findings resolved on `#1311` |
| Automation of Repetitive Work | 5 | Style-only 10-file commit done by hand |
| Consistency Across Windows | 7 | 3 merges this week; 13 PRs in the month |

*Change vs 09-03:* Delivery 6 → 7; Devin 6 → 7. *Next:* run the standards pass before opening the PR.

### akanksh-rv — Global Codio — 6.4 Mixed (Medium)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 7 | `#1306` merged; gate could not verify it |
| Engineering Rigor | 7 | 23.4k body praised by the reviewer as the repo's bar; 163 files, 20 reviewer commits to finish |
| Code Review Contribution | NR | None given |
| Observable Devin Leverage | 5 | Findings resolved (13 marks), no delegation; no Claude QA routine run this window |
| Automation of Repetitive Work | 6 | PRD decision log maintained; PR-size problem unchanged |
| Consistency Across Windows | 6 | Three > 89-file merges this month |

*Change vs 09-03:* unchanged overall. *Next:* ≤ 60-file stacked PRs.

### ragha82 — Global Codio — 6.1 Mixed (High)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 7 | Email attachments feature (8 commits) and `#1314` opened; five merges executed incl. the prod hotfix |
| Engineering Rigor | 7 | 2 `test(` commits with the feature; PRD deviations logged in commits. Held down by the template-only body on a 69-file PR |
| Code Review Contribution | 2 | Four approvals, all 0 characters, one on `uat → main`; merged his own 256-file QA sync with no review |
| Observable Devin Leverage | 6 | Owns the QA-gate doctrine that produced 5 no-verdict runs; closed 5 stale QA PRs; 17 findings on `#1314` unanswered |
| Automation of Repetitive Work | 7 | The QA gate exists because of him — but its blocker is now three days old |
| Consistency Across Windows | 7 | 48 `test(` in the month (highest); 17 empty approvals in the month |

*Change vs 09-03:* Rigor 8 → 7; Review 3 → 2. *Next:* persona secrets reset; gate verdict required on `dev → uat`.

### svh-medicodio — Global Codio — 5.8 Mixed (Medium)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 6 | 52 commits; neither `#1284` (145 files) nor `#1295` merged; 2 days open |
| Engineering Rigor | 6 | 3 `test(` commits; authorisation gap closed; spec repairs after sync; PR size unaddressed |
| Code Review Contribution | 5 | 14 inline replies on his own PR (excellent hygiene) — no review of a peer's PR |
| Observable Devin Leverage | 6 | 13 Devin Review rounds consumed to 0/0/0 on `#1295` |
| Automation of Repetitive Work | NR | No recurring step evidenced |
| Consistency Across Windows | 6 | 10 PRs in the month, 1 closed unmerged, 2 large open |

*Change vs 09-03:* Devin 3 → 6; Review 3 → 5. *Next:* split `#1284` per entity.

### Amrutha-Beedikar — Global Codio — NR (Low)

No commits, PRs, reviews or comments in the window. Consistency 5 (week: 3 PRs, 4 one-word approvals). Fewer than three rated dimensions → overall NR. *Next:* answer the 6 findings on `#1288`.

### Medicodio-Amit — Medicodio — 6.4 Mixed (Medium)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 6 | `#425` (40 files) opened with a full body; not merged |
| Engineering Rigor | 7 | 5.5k body explains the failure mode; conservation guard fixed on a finding; no test added |
| Code Review Contribution | NR | None given |
| Observable Devin Leverage | 7 | 3 findings answered with reasons — one accepted, two declined with rationale (best in Medicodio today) |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5 | Template bodies on prior promotions (`#419`); improved today |

*Change vs 09-03:* Rigor 4 → 7; Devin NR → 7. *Next:* conservation-guard property test.

### Shashvi1 — Medicodio — 6.2 Mixed (Low)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 6 | `#421` merged to `uat` and promoted; `#422` promotion had a badge-only body |
| Engineering Rigor | 7 | 4.8k body with CMS thresholds; implementation guide corrected; minutes-table test still absent |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 6 | 1 finding answered and fixed in-session |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5 | 9 commits in the month |

*Next:* ship the 99205/99215 minutes-table test.

### ashwinsk-medicodio — Medicodio — 5.9 Mixed (Low)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 7 | Guideline inheritance fix merged and promoted to prod within the day |
| Engineering Rigor | 6 | 947-char body quantifies 821 affected parents with a worked example; no test; reached prod 4 minutes after review opened |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4 | 2 findings, 1 resolved by re-scan, none answered |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | NR | First in-window appearance this week; insufficient history |

Three rated dimensions — overall computed. *Next:* inheritance regression test.

### hiteshjrxmedicodio — Medicodio — 5.7 Mixed (Low)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 7 | ASC payment indicators API + KB page both merged to `Dev_1.0` (API not deployed — pipeline red) |
| Engineering Rigor | 6 | 5k / 3.9k bodies with the client question; 0 tests; 1,110 lines merged in 6 minutes |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 4 | 10 findings merged past unanswered |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 4 | No commits earlier in the week; 133 commits in the month with 1 `test(` |

*Next:* loader golden-file test.

### jatinkushwaha-medicodio — Medicodio — 5.1 Mixed (High)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 6 | Test-coverage PR, rename and taxonomy merged; two 180/337-file prod promotions opened with no body |
| Engineering Rigor | 5 | `#528` adds tests (positive); `#608`/`#536` badge-only; 12 findings unanswered |
| Code Review Contribution | 3 | `lgtm` ×2, empty ×2, all within minutes |
| Observable Devin Leverage | 4 | 12 findings on `#608` unanswered |
| Automation of Repetitive Work | 5 | CI skip-path exercised (`#533`); promotion body still manual/absent |
| Consistency Across Windows | 8 | Steady daily cadence in both repos |

*Change vs 09-03:* Rigor 4 → 5 (tests). *Next:* answer `#608` findings and write the promotion body before prod.

### sameer-s-mansur — Medicodio — 5.1 Mixed (Medium)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 6 | `others` parser through `Uat_1.0` to `release/prod_1.0` same day |
| Engineering Rigor | 4 | Badge-only bodies on both PRs incl. prod; no tests; merged a 57-file PR with no review |
| Code Review Contribution | NR | No review given (merge without review is scored under Rigor) |
| Observable Devin Leverage | 3 | 8 findings merged past unanswered (answered 5 yesterday) |
| Automation of Repetitive Work | 6 | Consistent train use; promotion body not automated |
| Consistency Across Windows | 8 | 238 commits in the month, daily presence |

*Change vs 09-03:* Devin 6 → 3; Rigor 5 → 4. *Next:* parser golden-file tests.

### amit-pandey-medicodio — Medicodio — 4.7 Needs Support (High)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 6 | Coder-perf dedupe fix and secrets move shipped; but the BE `Dev_1.0` deploy has failed twice since 12:02 with no repair, so `#606`/`#607` are not live |
| Engineering Rigor | 4 | Badge-only bodies on `#606`, `#534`, `#249` (57 files, merged with no review); no tests |
| Code Review Contribution | 2 | 5 approvals, all 0 characters, ≤ 8 minutes |
| Observable Devin Leverage | 4 | 13 findings across three PRs unanswered; 38 Devin-trailer commits earlier in the week show capability |
| Automation of Repetitive Work | NR | Secrets move is hygiene, not automation of a recurring step |
| Consistency Across Windows | 8 | Highest steady cadence in Medicodio |

*Change vs 09-03:* Delivery 7 → 6; Rigor 5 → 4. *Next:* repair the nodejs deploy; deploy-failure check on merge.

### NandanDate-Medicodio — Medicodio — 4.1 Needs Support (High)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 5 | Six merges executed on the `uat`/`prod_3.0` path — the path is right, the verification is absent |
| Engineering Rigor | 4 | Three production merges within 1–16 minutes of opening, 20 findings unanswered, no tests in any |
| Code Review Contribution | 2 | Six `okay` approvals, three on production |
| Observable Devin Leverage | 3 | Findings on every merged PR ignored |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 7 | Same role every day of the month (147 merges) |

*Change vs 09-03:* Review 3 → 2. *Next:* written prod checklist quoted in the approval.

### avinash-codio — Medicodio — 4.1 Needs Support (Medium)

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Delivery & Follow-Through | 5 | Feature promoted to prod same day; 14 findings unanswered |
| Engineering Rigor | 3 | Badge-only bodies on `uat` and prod PRs; 3 of 5 commits mix concerns ("Antropic failure and devin issue and worksapce id issue"); no tests |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | 3 | 11 + 3 findings ignored; "devin issue" referenced without a link |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 6 | 70 commits and 59 PRs in the month, 0 `test(` |

*Next:* one concern per commit; written body on every promotion.

### sumedh-codio — Medicodio — NR (Low)

Two empty approvals (`#283`, `#284` → production, merged 7 minutes after opening). Review 2, Consistency 5 (17 empty approvals in the prior week). Fewer than three rated dimensions → overall NR. *Next:* name the check in the approval.

### shaheen-khan11 — Medicodio — NR (Low)

No in-window activity. Consistency 5 (19 commits in the week). Overall NR.

## How to read the spread

**Observed Fact.** The grid splits by product: seven Global Codio members average 6.7 on rated dimensions; eleven Medicodio members average 5.2, and the three Needs Support cards are all Medicodio. The gap is carried almost entirely by two dimensions — *Code Review Contribution* (Global Codio produced four substantive reviews today; Medicodio produced zero in the window and all 407 human review events in the month are empty or ≤ 10 characters) and *Engineering Rigor* (0 `test(` commits and 11 of 21 badge-only bodies in Medicodio; 14 `test(` and 7 of 9 full bodies in Global Codio). The two highest cards belong to the person who reviews (SaijyotiMeti) and the person who drove Devin Review to zero before asking for review (SaahilVishwakarma). The lowest belong to members whose in-window artefacts are production merges approved in ≤ 2 minutes with `okay` or nothing.

**Inference.** The Medicodio scores are a process signal more than an individual one: the same people produce 4–5k-char bodies when they choose to (Hitesh, Medicodio-Amit, ashwinsk today), so the badge-only promotion and the `okay` approval are the accepted norm on that train, not a skill gap. Global Codio's higher scores rest on a narrow base — one reviewer writing three long reviews and also authoring 14–20 commits in each PR she approves — so the product's review score would fall sharply if she were absent or if reviewer independence were enforced without a second reviewer being added. Devin Leverage scores are compressed (3–8) because only the artefact layer is visible; a member who ran an excellent session that produced no PR scores the same as one who ran none.

**Recommendation.** Treat the spread as three actions rather than nineteen conversations: (1) make an approval on any `release/prod_*` or `main` promotion quote a checklist item or a QA-gate verdict — this alone moves six Medicodio cards; (2) require a second reader on Global Codio merges where the reviewer wrote > 25 % of commits, and route the mechanical remediation to Devin so the reviewer's time goes to judgement; (3) restore Devin session telemetry (`org.sessions.view`) so *Observable Devin Leverage* can be scored on how Devin was used, not only on whether its comments were answered. Re-score consistency, not the daily number, when judging whether these have taken effect.

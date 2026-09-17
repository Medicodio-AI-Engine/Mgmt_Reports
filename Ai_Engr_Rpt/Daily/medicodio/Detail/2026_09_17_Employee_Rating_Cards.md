# Employee Rating Cards — 2026-09-17

**Review window:** 2026-09-16 03:00 UTC → 2026-09-17 03:00 UTC. Comparison: previous working day 09-15, week 09-09 → 09-16, month 08-17 → 09-16. Companion report: `2026_09_17_Mgmt_Activity_Report.md`.

## Scoring limitations — read before the numbers

- **No Devin session telemetry.** `devin_session_search` returned HTTP 403 (`org.sessions.view` missing) for the 15th consecutive run. *Observable Devin Leverage* is scored only on GitHub evidence: Devin Review findings and how they were dispositioned, Devin QA-gate verdicts and follow-up, Devin-authored PRs and how humans consumed them. Prompt quality, ACU effort, correction burden and delegation that never reached GitHub are invisible and are not scored for or against anyone.
- **No Jira, no Sentry, no CI status.** Coordination, support and incident work are unscored unless they left a GitHub trace.
- **Two repositories are new to this review** (`medicodio-nextgen-application-2.0`, `medicodio-nextgen-rf-rpa-automation`). Members seen only there have no history; their Consistency is NR or low-confidence.
- **Volume is not productivity.** Commit, PR and line counts appear only as context. Scores follow scoping, controls, evidence and follow-through.
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
| anirudh-medicodio | Global Codio | **6.5** | Mixed | 6 | 7 | NR | 7 | 5 | 7 | Medium (GitHub only; 5 dims) |
| karthikmed (Karthik Khatavkar) | Medicodio | **6.5** | Mixed | 6 | 6 | NR | 8 | NR | NR | Low (first window; 3 dims) |
| jatinkushwaha-medicodio | Medicodio | **6.3** | Mixed | 8 | 6 | 3 | 8 | 5 | 7 | Medium (GitHub only; 6 dims) |
| SaijyotiMeti | Global Codio | **6.1** | Mixed | 7 | 7 | 4 | 6 | 5 | 6 | Medium (GitHub only; 6 dims) |
| Pj-Vineeth-Kumar | Global Codio | **5.9** | Mixed | 7 | 6 | NR | 4 | 5 | 7 | Medium (GitHub only; 5 dims) |
| amit-pandey-medicodio | Medicodio | **5.7** | Mixed | 6 | 6 | 2 | 7 | 8 | 5 | Medium (GitHub only; 6 dims) |
| vishnu-saikarthik | Medicodio | **4.4** | Needs Support | 4 | 5 | 3 | 5 | NR | 5 | Medium (GitHub only; 5 dims) |
| Hitesh Shanthakumar | Medicodio | **5.4** | Mixed | 5 | 6 | NR | NR | 4 | 6 | Low (6 commits, no PR; 4 dims) |
| avinash-codio | Medicodio | **4.2** | Needs Support | 5 | 4 | 3 | NR | 4 | 5 | Low (prod-path operator; 5 dims) |
| sumedh-codio | Medicodio | **NR** | — | 6 | 4 | NR | NR | NR | NR | — (2 dims; repo newly visible) |
| akanksh-rv | Global Codio | **NR** | — | 4 | NR | NR | NR | 4 | NR | — (2 dims; 1 commit) |
| ragha82, Amrutha-Beedikar | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no events in window; carried items open) |
| svh-medicodio, SaahilVishwakarma | Global Codio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity in window) |
| sameer-s-mansur, Medicodio-Amit, NandanDate-Medicodio, afifashaikh007, ashwinsk-medicodio, Murali-Shetty19, Shashvi1, shaheen-khan11 | Medicodio | NR | — | NR | NR | NR | NR | NR | NR | — (no activity in window) |
| devin-ai-integration[bot] | — | not rated | tool | — | — | — | — | — | — | — |

Weighted average = Σ(score × weight) / Σ(weights of rated dimensions), rounded to one decimal.

---

## jatinkushwaha-medicodio — Medicodio — 6.3 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 8 | **Observed Fact:** 10 PRs opened, 8 merged into `Dev_1.0`/`Uat_1.0` — entitlement fixes, personal-inbox RLS fix + migration, announcements filter, client-config UI; every PR closed the same day. **Inference:** clean follow-through; one loose end (RLS-migration finding open at promotion). |
| Engineering Rigor | 6 | **Observed Fact:** feature PR bodies descriptive; no test files in any of the 6 feature diffs; 4 promotion PRs with badge-only bodies; `#648` merged 7 min after a BUG finding with no response. |
| Code Review Contribution | 3 | **Observed Fact:** 6 approvals, all empty, 3 of them on `application-2.0#1/#2/#3` within 90 s of open. |
| Observable Devin Leverage | 8 | **Observed Fact:** 6 of 7 Devin Review findings on his feature PRs ✅ Resolved with commits in 3–8 min; `#646` promotion 8 → 4 resolved. **Inference:** the strongest consumer loop in Medicodio; ceiling limited by the two unanswered RLS findings. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 4 hand-made `dev -> uat` PRs today, as on 09-11/09-12. |
| Consistency Across Windows | 7 | **Observed Fact:** 18 PRs/week, 105/month; finding disposition has improved since 08-2x; review bodies never substantive. 09-16 card 6.6 → 6.3 (Review rated today). |

**Recommendation:** answer the personal-inbox RLS migration finding before `uat -> prod`; write one sentence per approval.

## anirudh-medicodio — Global Codio — 6.5 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `#1386` opened (234 files, 27 commits) — substantial advance, not merged; `#1358` (fix for 5 confirmed failures) closed unmerged with no note; `#1363` F-6/F-1 still undispositioned. **Inference:** progress without closure on carried items. |
| Engineering Rigor | 7 | **Observed Fact:** ADR-0050 + `LifecycleWriteGuard` spec added; IDOR/PII/tenancy fixes named; body states "migration never applied, Jest not run". PR size 234 files. **Inference:** honest and test-bearing, oversized. |
| Code Review Contribution | NR | No review events in window. |
| Observable Devin Leverage | 7 | **Observed Fact:** 15 Devin findings on `#1386`; 9 ✅ Resolved via `6ad60a5` "close the three verified Devin findings still outstanding"; 4 latest (incl. SEC) open <9 h. |
| Automation of Repetitive Work | 5 | **Observed Fact:** `chore(atlas)` + 2 review-log commits by hand again. |
| Consistency Across Windows | 7 | **Observed Fact:** no self-approve/merge today (09-15: `#1364`); 112 commits/week, 719/month. **Inference:** Improved vs yesterday on controls. 09-16 card 5.8 → 6.5. |

**Recommendation:** delegate the hosted migrate + Jest run on `#1386` to Devin before requesting review.

## karthikmed (Karthik Khatavkar) — Medicodio — 6.5 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** `nodejs#652` (163 files) and `react#578` (150 files) opened; both open, no reviewer requested. |
| Engineering Rigor | 6 | **Observed Fact:** tests on billing money paths; three race fixes with clear commit messages; badge-only PR bodies; title/branch carry `hitesh/…`. |
| Code Review Contribution | NR | No review events. |
| Observable Devin Leverage | 8 | **Observed Fact:** 20 Devin Review findings across both PRs, 20 ✅ Resolved by follow-up commits within ~40 min per round. |
| Automation of Repetitive Work | NR | No repetitive-work evidence in one window. |
| Consistency Across Windows | NR | First appearance; no history. |

**Recommendation:** write the PR bodies and assign a human reviewer before any merge.

## SaijyotiMeti — Global Codio — 6.1 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1389` opened with full body + tests (65 files); `#1380` merged. **Inference:** advanced and closed work; the merge is scored under Review, not here. |
| Engineering Rigor | 7 | **Observed Fact:** 35 component tests added, 5 specs repaired, PRD + review logs; her own `[needs decision]` on a migration-safety bypass left open at merge. |
| Code Review Contribution | 4 | **Observed Fact:** the only substantive human review in the org today (1,200 chars, two inline notes) — on a PR she had 32 commits on, followed by her own `approved` and merge 6 min later. **Inference:** valuable remediation, not independent review; 7th report of the pattern. |
| Observable Devin Leverage | 6 | **Observed Fact:** QA gate NOT READY on `#1380` unanswered; 9 findings on `#1389` <3 h old. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 4 review-log/PRD-sync commits and 2 spec-repair passes by hand. |
| Consistency Across Windows | 6 | **Observed Fact:** 202 commits/week; pattern recurs. 09-16 card 6.4 → 6.1 (Review rated for the first time this week, low). |

**Recommendation:** record the `DROP COLUMN` decision on `#1380`; hand `#1389` to a reviewer who has not committed to it.

## Pj-Vineeth-Kumar — Global Codio — 5.9 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 7 | **Observed Fact:** `#1380` merged (490 files, 143 commits) — the 5-report branch-without-PR item is closed; timezone work now sits as one commit with no PR. |
| Engineering Rigor | 6 | **Observed Fact:** PRD + migration justification before the table drop; schema drop still inside the feature PR (09-16 advice not taken); 2 spec repairs; no reply to Devin inline findings. |
| Code Review Contribution | NR | No review events. |
| Observable Devin Leverage | 4 | **Observed Fact:** `#1365` (Devin, 530 files, 5 days unreviewed) closed unmerged; 30 min later a single untrailered commit with the same feature title on the same branch; QA items C1/C2 unanswered. **Inference:** Devin output absorbed without trail or review. |
| Automation of Repetitive Work | 5 | **Observed Fact:** 4 doc-sync commits by hand. |
| Consistency Across Windows | 7 | **Observed Fact:** 101 commits/week, month-leading delivery; process signals mixed. 09-16 card 6.4 → 5.9. |

**Recommendation:** open the timezone PR from `1e36c3b` with a body linking `#1365`'s findings.

## amit-pandey-medicodio — Medicodio — 5.7 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** prod `23505` incident fixed on `Dev_1.0`/`Uat_1.0` in 100 min (`#647`, `#650`, `#653`); `#651` to `release/prod_1.0` closed unmerged, prod branch unchanged since 09-11; `application-2.0` bootstrapped. **Inference:** fast fix, prod closure unproven. |
| Engineering Rigor | 6 | **Observed Fact:** three iterations to converge on the race with no test in the diffs; untracked a committed TOTP seed on day one of the new repo. |
| Code Review Contribution | 2 | **Observed Fact:** 12 approvals, 12 empty, several 1 min after open, on prod-bound promotions. |
| Observable Devin Leverage | 7 | **Observed Fact:** 6 Devin findings on the hotfix chain, all ✅ Resolved with commits; Devin trailers on 6 commits. |
| Automation of Repetitive Work | 8 | **Observed Fact:** `repo-structure.md` now regenerated by a Claude Code Stop hook — repetitive doc work eliminated. |
| Consistency Across Windows | 5 | **Observed Fact:** empty approvals every active day since 08-27; authored output up vs 09-15. 09-16 card 3.6 → 5.7 (author dims rated today). |

**Recommendation:** land the `23505` fix in `release/prod_1.0` with a concurrency test.

## vishnu-saikarthik — Medicodio — 4.4 (Needs Support)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4 | **Observed Fact:** change reached prod (`#453`), reverted (`#454`), re-landed (`#458`) within 11 h — three prod merges for one change. |
| Engineering Rigor | 5 | **Observed Fact:** `#455` fix names the cause and restores the legacy loader; no test for the nested-prefix `TypeError`; promotion bodies template-only. |
| Code Review Contribution | 3 | **Observed Fact:** 2 approvals (`approve`, empty) on prod PRs with 4 open Devin findings. |
| Observable Devin Leverage | 5 | **Observed Fact:** `#455` 2 findings ✅ Resolved with reasons; `#453`/`#458` 4 findings each unanswered at prod merge. |
| Automation of Repetitive Work | NR | — |
| Consistency Across Windows | 5 | **Observed Fact:** small targeted fixes all month; promotion review absent (`#435`, `#452`, today). 09-16 card 5.5 → 4.4. |

**Recommendation:** add a nested CPT/HCPCS prefix test and link it from `#458`.

## Hitesh Shanthakumar — Medicodio — 5.4 (Mixed)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** inpatient model ported into `application-2.0` (6 commits); no PR — 11th consecutive report. |
| Engineering Rigor | 6 | **Observed Fact:** commit bodies explain the routing bug and the schema/seed split; monorepo checks surfaced bugs he fixed. No tests visible. |
| Code Review Contribution | NR | — |
| Observable Devin Leverage | NR | No Devin artefacts (no PR → no Devin Review). |
| Automation of Repetitive Work | 4 | **Observed Fact:** manual port across repos; branch discipline unchanged. |
| Consistency Across Windows | 6 | **Observed Fact:** 143 commits/month, 16 PRs in react/nodejs; the inpatient stream has never had a PR. 09-16 card 5.4 → 5.4. |

**Recommendation:** open a draft PR on `Dev_2.0`.

## avinash-codio — Medicodio — 4.2 (Needs Support)

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 5 | **Observed Fact:** reverted the broken prod change within 2.5 h (positive); revert body template-only; `#457` 0-file PR opened and closed. |
| Engineering Rigor | 4 | **Observed Fact:** merged `#453` 28 s after open; `#454`/`#458` bodies carry no reason or evidence. |
| Code Review Contribution | 3 | **Observed Fact:** approvals `ok`, `okay`, `okay`, empty on prod promotions. |
| Observable Devin Leverage | NR | No disposition of any Devin finding (bot findings on PRs he merged are attributed to authors). |
| Automation of Repetitive Work | 4 | **Observed Fact:** manual revert / revert-of-revert ×3. |
| Consistency Across Windows | 5 | **Observed Fact:** one-word approvals 08-27, 09-06, today. First active day since 09-11. |

**Recommendation:** write the revert reason on `#454` and the re-land evidence on `#458`.

## sumedh-codio — Medicodio — NR

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 6 | **Observed Fact:** 2 PRs merged (`rf-rpa-automation#21`, `#22`). |
| Engineering Rigor | 4 | **Observed Fact:** empty bodies, self-merged 2–3 min after open, no reviewer, no Devin Review on the repo. |
| Others | NR | Repo newly visible; no history, no review or Devin evidence. |

**Recommendation:** enable Devin Review on the repo and add a second approver.

## akanksh-rv — Global Codio — NR

| Dimension | Score | Evidence |
| --- | --- | --- |
| Delivery & Follow-Through | 4 | **Observed Fact:** 1 atlas commit; `#1373` decision items 1–3 (in prod) unanswered for a 2nd day. |
| Automation of Repetitive Work | 4 | **Observed Fact:** manual atlas regeneration again. |
| Others | NR | No PR, review or Devin evidence in window. Yesterday's 5.7 stands as the last rated card. |

**Recommendation:** resolve `#1373` items 1–3 in the PR thread.

---

## How to read the spread

- **Observed Fact:** nine members are rated, 5.4 → 6.5 in *Mixed* plus two in *Needs Support* (Vishnu 4.4, avinash 4.2), both from the same event — a `nextgen-codio-engine` change that reached production, was reverted and re-landed inside 11 hours with 8 Devin findings unanswered. No one is *Solid* or *Strong*. The top three (Jatin, anirudh, Karthik) are there because they close Devin findings with linked commits inside minutes and their PR bodies say what is and is not verified — not because of volume; Saijyoti and anirudh authored the most code and sit mid-table.
- **Observed Fact:** Code Review is the weakest dimension org-wide for the 14th report — 25 of 26 human review objects were empty or one word, and the one substantive review approved and merged a PR its author had 32 commits on. Every Medicodio reviewer rated today (amit 2, Jatin 3, Vishnu 3, avinash 3) is in the bottom band on that dimension alone.
- **Inference:** two moves are about one decision each, not skill — Vineeth's Devin score (6 → 4) is the closure of `#1365` with the work re-pushed untraced; Saijyoti's Review score (NR → 4) is the `#1380` merge sequence. amit's rise (3.6 → 5.7) reflects authored dimensions being rated for the first time this week plus one real automation; his Review score did not move.
- **Inference:** Devin leverage remains bounded above by missing telemetry — Karthik's and Jatin's 8 are the ceiling visible from GitHub; the Medicodio consumption loop is now the healthiest Devin signal in the org, while Global Codio's QA gate still runs after merge and has returned NOT READY six times in a row.
- **Recommendation:** treat three items as tomorrow's test of whether today's low scores were a single unusual day — the `23505` fix reaching `release/prod_1.0`, `#458`'s findings answered with a test, and the `#1380` decision recorded; and grant the automation `org.sessions.view` so Devin leverage can be scored on evidence rather than absence.

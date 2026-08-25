# Employee Rating Cards — 2026-08-24 (Monday, UTC)

**Scope:** members with observable activity on 2026-08-24 across `globalcodio-monorepo` (Global Codio) and `nextgen-codio-engine` / `medicodio-nextgen-app-nodejs` / `medicodio-nextgen-app-react` / `medicodio-nextgen-integration` (Medicodio).

## Scoring limitations — read before the numbers

- **Devin session telemetry is unavailable** (API permission `org.sessions.view` denied, 6th consecutive run). "Observable Devin Leverage" is scored only from Git evidence: `Co-Authored-By: Devin AI` trailers, Devin-authored PRs, and recorded interaction with Devin Review findings. Members who use Devin without Git-visible output are undercounted.
- **Jira is not queryable**, so coordination, ticket hygiene, and non-code work are invisible.
- Scores rate the **quality of observable engineering behavior**, never raw volume: commit/PR counts appear only as consistency evidence, not as productivity.
- A dimension with no in-window evidence is **NR** and is excluded from the weighted average. A member with fewer than three rated dimensions gets an overall of **NR**.
- One-day windows are noisy; the day/week/month comparisons in the companion report temper single-day readings.

## Rubric

| Dimension | Weight | 8–10 (Strong) | 5–7 (Solid/Mixed) | 1–4 (Needs Support) |
| --------- | ------ | ------------- | ----------------- | ------------------- |
| Delivery & Follow-Through | 25 | Scoped work merged through full review; follow-ups closed | Work lands but with size/latency friction | Stalled, duplicated, or unreviewable delivery |
| Engineering Rigor | 25 | Tests/gates evidenced; findings resolved pre-merge | Partial gate discipline | Merges over unresolved findings; empty release records |
| Code Review Contribution | 15 | Substantive written verdicts that change outcomes | Occasional real reviews among thin approvals | Rubber-stamp approvals only |
| Observable Devin Leverage | 15 | Effective delegation with reviewed output | Some interaction with Devin output | None despite suitable tasks |
| Automation of Repetitive Work | 10 | Repetitive work automated or being automated | Aware, partial automation | Manual repetition persists |
| Consistency Across Windows | 10 | Steady day/week/month contribution | Uneven but present | Sporadic or opaque |

**Bands:** Strong ≥ 8 · Solid ≥ 7 · Mixed ≥ 5 · Needs Support < 5.

## Summary Grid

| Member | Product | Delivery | Rigor | Review | Devin | Automation | Consistency | Overall | Band | Confidence |
| ------ | ------- | -------- | ----- | ------ | ----- | ---------- | ----------- | ------- | ---- | ---------- |
| akanksh-rv | Global Codio | 8 | 8 | 9 | 7 | 7 | 8 | **7.9** | Solid | High |
| Medicodio-Amit | Medicodio (engine) | 8 | 7 | NR | 6 | 5 | 6 | **6.8** | Mixed | Medium |
| SaijyotiMeti | Global Codio | 7 | 7 | 8 | 5 | 4 | 8 | **6.7** | Mixed | High |
| Pj-Vineeth-Kumar | Global Codio | 8 | 7 | NR | 5 | 4 | 7 | **6.6** | Mixed | Medium |
| svh-medicodio | Global Codio | 7 | 7 | NR | 5 | NR | 7 | **6.6** | Mixed | Medium |
| SaahilVishwakarma | Global Codio | 7 | 7 | NR | 4 | NR | 6 | **6.3** | Mixed | Medium |
| anirudh-medicodio | Global Codio | 7 | 6 | 6 | 4 | 5 | 8 | **6.1** | Mixed | High |
| sameer-s-mansur | Medicodio (integration) | 7 | 5 | NR | 5 | 6 | 7 | **5.9** | Mixed | Medium |
| amit-pandey-medicodio | Medicodio (app) | 7 | 5 | 4 | 6 | 5 | 7 | **5.7** | Mixed | High |
| jatinkushwaha-medicodio | Medicodio (app) | 7 | 6 | 4 | 4 | 4 | 7 | **5.6** | Mixed | Medium |
| hitesh | Medicodio (app) | 6 | 5 | NR | 4 | 4 | 6 | **5.1** | Mixed | Medium |
| NandanDate-Medicodio | Medicodio (engine) | 6 | 4 | 3 | 4 | 4 | 7 | **4.7** | Needs Support | High |
| shaheen-khan11 | Medicodio (app) | 6 | 5 | NR | 3 | 3 | 5 | **4.7** | Needs Support | Medium |
| ragha82 | Global Codio | 6 | 4 | 4 | 4 | 4 | 5 | **4.6** | Needs Support | Medium |
| avinash-codio | Medicodio (engine) | 5 | 4 | 3 | NR | NR | 5 | **4.3** | Needs Support | Low |
| Amrutha-Beedikar | Global Codio | 5 | 4 | 4 | 3 | 4 | 5 | **4.2** | Needs Support | Medium |
| vishnu-saikarthik | Medicodio (engine) | NR | NR | NR | NR | NR | NR | **NR** | NR | Low |

**Team observations (Observed Fact).** 8 substantive human reviews came from 3 people (akanksh 5, anirudh 2, Saijyoti 1) against 44 empty/one-word approvals. A 1,068-file production PR (#1232) merged in 2 minutes with an unfilled template body. Org-wide Devin trailers fell from 17 (08-21) to 1 (today, sameer). Global Codio CI recovered fully (74 green runs).

---

## akanksh-rv — 7.9 · Solid

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 8 | #1233 (Graph-mail MIME fix) authored, reviewed, merged same day; 4 stacked remediation PRs landed. |
| Rigor | 8 | #1233 called "one of the best-documented fix PRs" by its reviewer; remediation PRs gated through github-actions merges. |
| Review | 9 | 5 substantive Architect+EM reviews (#1215/#1222/#1223/#1227/#1231) with explicit verdicts — highest of the day. |
| Devin | 7 | Ran the /check+/fix audit cycle on Devin PR #1227 and engaged Devin's re-verification in-thread. |
| Automation | 7 | Stacked `claude/review-fixes/*` remediation workflow is systematic; auto-merged by gates. |
| Consistency | 8 | 145 commits week / 340 month with rising review share. |

**Strength (Observed Fact).** He is carrying the review culture: 5 of the day's 8 substantive reviews, each with verdict and findings list.
**Watch (Inference).** Single-reviewer concentration — if he is out, the substantive-review rate collapses.
**Next improvement (Recommendation).** Delegate remediation-PR preparation to Devin from his own findings lists.

---

## Medicodio-Amit — 6.8 · Mixed

**Product:** Medicodio (engine)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 8 | Co-Pilot escalation feature (#387) + ENM schema (#384) merged and promoted to prod the same day. |
| Rigor | 7 | #389 explicitly patched "three review findings" before promotion — the engine's only findings-driven remediation; docked for prod promotion 1 min after uat merge (#388), before Devin Review finished. |
| Review | NR | No reviews given in window. |
| Devin | 6 | Responded to Devin Review findings via a dedicated patch PR; 1 trailer commit in month window. |
| Automation | 5 | Feature itself automates escalation (Teams cards), but his UAT→prod pairs remain manual. |
| Consistency | 6 | 16 commits week / 71 month; day was a spike. |

**Strength (Observed Fact).** Findings → dedicated patch PR → promote, all in one morning: the correct loop.
**Watch (Observed Fact).** Every merge in his chain was gated by a one-word 'okay'.
**Next improvement (Recommendation).** Hold prod promotion until Devin Review completes on the uat PR.

---

## SaijyotiMeti — 6.7 · Mixed

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | #1231 (system-actor fix) and #1215 merged through substantive review. |
| Rigor | 7 | #1231 replaced a reviewer-impersonation hack with a system actor — a security-correctness fix; 4 reviewer decision-items left open (Inference: edge cases untested). |
| Review | 8 | Full Architect+EM review of #1233; merges paired with verdicts; one 'approved'-only on small #1235. |
| Devin | 5 | 3 Devin-trailer commits in week window (alias); pushed to Devin PR #1208's branch but no verdict issued yet. |
| Automation | 4 | Manual sync/merge chores persist. |
| Consistency | 8 | 158 commits week / 433 month, steady review participation. |

**Strength (Observed Fact).** Verdict-then-merge discipline held again today.
**Watch (Observed Fact).** Devin PR #1208 has API- and browser-level verification posted and awaits only her decision — day 4.
**Next improvement (Recommendation).** Issue the #1208 verdict; it sets the org's Devin-delegation template.

---

## Pj-Vineeth-Kumar — 6.6 · Mixed

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 8 | 3 PRs merged: #1183 (150-file feature after 5-day cycle), #1221, #1222 — all through review. |
| Rigor | 7 | Remediated the QA DEV-FIX-LIST and new Devin Review findings same-day before approval. |
| Review | NR | No reviews given in window. |
| Devin | 5 | Devin Review findings on #1221 addressed between posts (Inference from update timing). |
| Automation | 4 | QA fix-lists worked manually. |
| Consistency | 7 | 32 commits week / 127 month; improving trajectory. |

**Strength (Observed Fact).** Fastest findings→fix turnaround of the day.
**Watch (Observed Fact).** #1183 merged at 150 files — beyond reliable human audit.
**Next improvement (Recommendation).** Delegate the next QA DEV-FIX-LIST to Devin as itemized acceptance criteria.

---

## svh-medicodio — 6.6 · Mixed

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | #1223 merged after full REQUEST CHANGES → remediate → approve cycle; #1238 opened. |
| Rigor | 7 | Took the day's only REQUEST CHANGES and closed it within the evening. |
| Review | NR | No reviews given in window. |
| Devin | 5 | Devin Review engaged on both PRs; 4 findings pending on #1238 at day end. |
| Automation | NR | No evidence either way. |
| Consistency | 7 | 33 commits week / 221 month. |

**Strength (Observed Fact).** Zero-friction response to a hard review verdict.
**Watch (Observed Fact).** #1238 opened at 112 files with 4 immediate automated findings.
**Next improvement (Recommendation).** Pre-clear Devin Review findings before requesting human review.

---

## SaahilVishwakarma — 6.3 · Mixed

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | Both long-running PRs (#1178, 99 files; #1179, 77 files) merged after full review. |
| Rigor | 7 | #1178 merged with "all 14 gates green" per the review record. |
| Review | NR | No reviews given in window. |
| Devin | 4 | Devin Review findings accumulated to 8+ over 5 days before merge; no visible engagement. |
| Automation | NR | No evidence either way. |
| Consistency | 6 | 64 commits week / 113 month, cyclical around big PRs. |

**Strength (Observed Fact).** Finished both review cycles properly — no shortcut merges.
**Watch (Inference).** PR size drives 5–6 day review latency; that is the real throughput limiter.
**Next improvement (Recommendation).** Slice the next feature into ≤30-file increments targeted at 48-hour merges.

---

## anirudh-medicodio — 6.1 · Mixed

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | #1220 (deploy Actions + QA gate) merged; ran the full release train; 8 merges performed. |
| Rigor | 6 | Proper REQUEST CHANGES loop on #1223; but self-merged 903-file sync #1217 in 4 min and merged 1,068-file prod PR #1232 in 2 min. |
| Review | 6 | 2 substantive reviews (#1178, #1223) against 7 empty-body approvals. |
| Devin | 4 | No delegation; he is Devin's named decision-maker on #1227 policy items (engagement, not leverage). |
| Automation | 5 | Built deploy/QA-gate Actions (#1220) — real automation; promotion PRs still hand-made. |
| Consistency | 8 | 218 commits week / 679 month, the org's highest. |

**Strength (Observed Fact).** The #1223 loop — REQUEST CHANGES at 21:23, fixes verified, approval at 21:30 — is the model for the team.
**Watch (Observed Fact).** The same evening he approved a 1,068-file production release in 2 minutes with an empty body: the two behaviors cannot both be the standard.
**Next improvement (Recommendation).** Auto-generated release-diff summaries required on promotion PRs before approval.

---

## sameer-s-mansur — 5.9 · Mixed

**Product:** Medicodio (integration)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | #230 event-driven batch runs (68 files) merged; the repo's feature track advanced. |
| Rigor | 5 | Self-merged 14 min after a fresh Devin Review finding, with only an empty peer approval in between. |
| Review | NR | No reviews given in window. |
| Devin | 5 | The day's only org-wide Devin-trailer commit (migration-doc update). |
| Automation | 6 | The feature itself automates batch-run fan-out for event-driven facilities. |
| Consistency | 7 | 53 commits week / 159 month, steady sole-contributor cadence. |

**Strength (Observed Fact).** First integration-repo Devin trailer in this report series — the workflow has started.
**Watch (Observed Fact).** As the repo's only contributor, Devin Review is effectively his only reviewer, and today it was merged over.
**Next improvement (Recommendation).** Respond to every Devin Review finding before merge in the integration repo.

---

## amit-pandey-medicodio — 5.7 · Mixed

**Product:** Medicodio (app)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | #573 (payer resolve-or-create, 3 files) and #487 (workspace refactor) merged; keeps the app pipeline moving. |
| Rigor | 5 | Own PRs small and clean; but merged 130- and 226-file PRs with no recorded checks. |
| Review | 4 | 17–18 approvals, all empty-body — sole human gate for the app team. |
| Devin | 6 | 17 Devin-trailer commits on 08-21 under the `amit.p` alias (Inference: same person); zero today. |
| Automation | 5 | Batched endpoint reduces integration round-trips; merge servicing fully manual. |
| Consistency | 7 | 47 commits week / 210 month. |

**Strength (Observed Fact).** His own changes are the best-scoped in the app repos.
**Watch (Observed Fact).** Third consecutive report citing the empty-approval merge gate.
**Next improvement (Recommendation).** Auto-merge small green-gate PRs; write one-line evidence-based verdicts on large ones.

---

## jatinkushwaha-medicodio — 5.6 · Mixed

**Product:** Medicodio (app)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 7 | Impersonation management (#564) + banner (#490), audit columns (#571) merged. |
| Rigor | 6 | Proactive dead-code removal (#565, −383 lines; #568); impersonation shipped without visible tests. |
| Review | 4 | Two 'lgtm' approvals. |
| Devin | 4 | No observable usage. |
| Automation | 4 | 3 manual dev→uat sync PRs. |
| Consistency | 7 | 45 commits week / 102 month. |

**Strength (Observed Fact).** Only app-repo member doing deliberate cleanup alongside features.
**Watch (Observed Fact).** Impersonation/session management is the app's most security-sensitive surface and merged untested.
**Next improvement (Recommendation).** Devin-generated regression tests for the impersonation flow.

---

## hitesh — 5.1 · Mixed

**Product:** Medicodio (app)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 6 | The KB/MCP/Ask-AI wave finally merged (nodejs #569/#575; react #493/#496/#497) — but via duplicate/re-opened PRs (#574→#575; #569/#493 re-open the 08-21 closures). |
| Rigor | 5 | Small #497 was clean; 130/226-file PRs merged with Devin Review findings unresolved. |
| Review | NR | No reviews given in window. |
| Devin | 4 | Devin Review findings on 5 of his PRs, none visibly resolved pre-merge. |
| Automation | 4 | Manual PR churn (close/re-open) adds work rather than removing it. |
| Consistency | 6 | 40 commits week / 53 month; delivery arrived in a burst. |

**Strength (Observed Fact).** Up from 4.1 on 08-23 — the stuck work landed.
**Watch (Observed Fact).** Close-and-reopen destroyed the findings history on the largest diffs of the day.
**Next improvement (Recommendation).** Update PRs in place; make a green-or-answered Devin Review the pre-merge bar.

---

## NandanDate-Medicodio — 4.7 · Needs Support

**Product:** Medicodio (engine)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 6 | HCPCS ophthalmology changes (#392) shipped. |
| Rigor | 4 | Self-merged #392 on a bare peer approval, 49 seconds before Devin Review posted a finding. |
| Review | 3 | 7 merges performed, every approval the single word 'okay' — including prod-branch merges. |
| Devin | 4 | 6 Devin-trailer commits in week window (only engine member with any). |
| Automation | 4 | Manual promotion merges continue. |
| Consistency | 7 | 41 commits week / 116 month; reliable gate-keeper cadence. |

**Strength (Observed Fact).** He already uses Devin trailers — the adoption seed exists.
**Watch (Observed Fact).** He controls 7 of 8 engine merge events; his 'okay' standard *is* the engine's review standard.
**Next improvement (Recommendation).** Wait for Devin Review + write one-line evidence-based verdicts on the merges he performs.

---

## shaheen-khan11 — 4.7 · Needs Support

**Product:** Medicodio (app)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 6 | Prod fix and bulk-upload change landed in both repos. |
| Rigor | 5 | Fixes small and targeted; duplicated by hand across 4 PRs with divergence risk. |
| Review | NR | No reviews given in window. |
| Devin | 3 | None observable, on the org's most Devin-suited workload. |
| Automation | 3 | 2 logical changes → 4 hand-made PRs; pattern recurs across the month. |
| Consistency | 5 | 10 commits week / 31 month. |

**Strength (Observed Fact).** Minimal, targeted diffs.
**Watch (Inference).** Manual porting will eventually ship inconsistent fixes across branches.
**Next improvement (Recommendation).** One Devin session per fix to open the dev+prod ports across both repos.

---

## ragha82 — 4.6 · Needs Support

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 6 | #1235 (DOB optional) merged cleanly through review. |
| Rigor | 4 | #1234 (454 files) opened with the raw template as its body; promotion merges within a minute of opening. |
| Review | 4 | 2 empty-body approvals on 91-file main/uat promotions. |
| Devin | 4 | No observable usage. |
| Automation | 4 | The recurring "qa update-DD-MM" sync remains manual. |
| Consistency | 5 | 11 commits week / 23 month; steady but low-volume release-support role. |

**Strength (Observed Fact).** Small fixes done right (#1235).
**Watch (Observed Fact).** The nightly QA sync is his biggest time sink and produces the emptiest records.
**Next improvement (Recommendation).** Automate the qa-update sync with a generated summary body.

---

## avinash-codio — 4.3 · Needs Support

**Product:** Medicodio (engine)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 5 | Config changes (#386) shipped to the prod branch. |
| Rigor | 4 | Merged 2 minutes after opening; Devin Review found 2 issues post-merge. |
| Review | 3 | One empty approval (#392) given seconds after the PR opened. |
| Devin | NR | No evidence either way. |
| Automation | NR | No evidence either way. |
| Consistency | 5 | 25 commits week / 70 month, mostly configuration. |

**Strength (Observed Fact).** Config changes are PR-based, not direct pushes.
**Watch (Observed Fact).** Production configuration is changing faster than any review can occur.
**Next improvement (Recommendation).** 15-minute cooling period on prod-branch PRs so automated review lands pre-merge.

---

## Amrutha-Beedikar — 4.2 · Needs Support

**Product:** Global Codio

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | 5 | The production release (#1232) shipped on schedule — but as a single 1,068-file PR. |
| Rigor | 4 | #1232 body is the unfilled template; merged 2 minutes after opening. |
| Review | 4 | Three one-word approvals ('approved', 'approvedd') on 38–993-file promotions. |
| Devin | 3 | No observable usage. |
| Automation | 4 | Release assembly fully manual. |
| Consistency | 5 | 21 commits week / 48 month. |

**Strength (Observed Fact).** Release cadence is dependable.
**Watch (Observed Fact).** Third consecutive report citing promotion-record quality; today's production release has no reviewable record at all.
**Next improvement (Recommendation).** Auto-generated release notes as the mandatory body of every production PR.

---

## vishnu-saikarthik — NR

**Product:** Medicodio (engine)

| Dimension | Score | Evidence |
| --------- | ----- | -------- |
| Delivery | NR | Branch pushes to `phrase-semantical-matching` only; content not measurable. |
| Rigor | NR | No PRs or reviews in window. |
| Review | NR | — |
| Devin | NR | — |
| Automation | NR | — |
| Consistency | NR | 6 commits week / 13 month, all off default branches. |

Fewer than three rated dimensions → **Overall NR** (not a low score — the data simply does not show the work).
**Next improvement (Recommendation).** Open the branch as a draft PR so the work becomes visible to review.

---

## How to read the spread

- **Observed Fact** — directly present in the collected Git data: PR/review/commit records, timestamps, file counts, approval bodies, CI conclusions. Every score's Evidence column is built from these.
- **Inference** — a conclusion the facts support but do not prove (e.g. that `amit.p@medicodio.ai` and `amit-pandey-medicodio` are the same person; that update timing between Devin Review posts means findings were addressed). Inferences are labeled and never the sole basis for a low score.
- **Recommendation** — the action we believe follows; each card carries exactly one, chosen for highest leverage rather than completeness.

The band compresses a weighted average; read the dimension row, not the headline. Today's spread says: Global Codio's review culture is consolidating around three people while its release records thin out, and Medicodio's delivery is steady but gated almost entirely by one-word approvals. The absent dimension — Observable Devin Leverage — is also the noisiest: without session telemetry, a member could be using Devin heavily with nothing visible in Git. Treat Devin scores as a floor, not a measurement.

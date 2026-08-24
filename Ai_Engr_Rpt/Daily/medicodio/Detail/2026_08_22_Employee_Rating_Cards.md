# Employee Rating Cards — 2026-08-22 (Saturday, UTC)

Scored from GitHub-observable evidence for the review day only. Weights: Delivery 25 / Rigor 25 / Review 15 / Devin 15 / Automation 10 / Consistency 10. Dimensions with no in-window evidence are **NR** and are excluded from the weighted average; a member with fewer than three rated dimensions gets no overall rating (**NR**). Bands: Strong >= 8, Solid >= 7, Mixed >= 5, Needs Support < 5.

**Weekend caveat.** 2026-08-22 was a Saturday: 8 of ~24 active members worked, 2 PRs were opened and 2 merged. These cards therefore rate a thin, self-selected slice of the team and must not be read as a standing performance ranking — members absent on a weekend are not scored at all, and a single Saturday is not a trend. Compare only against other single-day cards, never against the weekly picture.

**Context that limits every card.** GitHub Actions executed no runs after 2026-08-21 22:38 UTC (billing / spending-limit failure), so no gate or deployment ran on the review day. Devin session data is unavailable (`org.sessions.view` 403), so the Devin dimension scores only GitHub-observable leverage: Devin-authored PRs, `Co-Authored-By: Devin AI` trailers, Devin Review usage, and whether clearly-scoped candidate work was delegated.

## Summary grid

| Member | Product | Delivery | Rigor | Review | Devin | Automation | Consistency | Weighted | Band |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| akanksh-rv | Global Codio | 9 | 9 | NR | 5 | 4 | 9 | 7.7 | Solid |
| sameer-s-mansur | Medicodio | 8 | 8 | NR | 4 | 5 | 8 | 6.9 | Mixed |
| jatinkushwaha-medicodio | Medicodio | 7 | 6 | NR | 5 | 4 | 7 | 6.0 | Mixed |
| anirudh-medicodio | Global Codio | 7 | 5 | NR | 5 | 5 | 8 | 5.9 | Mixed |
| SaijyotiMeti | Global Codio | 6 | NR | NR | 4 | 5 | 8 | 5.7 | Mixed |
| amit-pandey-medicodio | Medicodio | 5 | 4 | 3 | 5 | 4 | 6 | 4.5 | Needs Support |
| Amrutha-Beedikar | Global Codio | 5 | 4 | 3 | NR | NR | NR | 4.2 | Needs Support |
| karthikmed | Shared / tooling | NR | NR | NR | NR | 3 | NR | NR | NR |

**Dimension means (rated members only):** Delivery 6.7, Rigor 6.0, Review 3.0, Devin 4.7, Automation 4.3, Consistency 7.7

## Cards

### akanksh-rv — Global Codio

**Weighted: 7.7 (Solid)** · Delivery 9 · Rigor 9 · Review NR · Devin 5 · Automation 4 · Consistency 9

**Evidence (Observed Fact)**

- 39 commits on two branches; PR #1210 fixes a Critical QA defect (reviewed draft discarded on send) plus a cancellation-audit race, a missing ACTION_SENT emission and a read-purity defect that could bill the payment provider.
- PR body cites six grepped surfaces, states the reuse decision and proves cleanup with a zero-hit grep; includes an honest note that his own first cut was wrong and `/check` caught it.
- Devin Review returned No Issues Found; no Devin session delegated for the two clearly-scoped slices (regression tests, CLEANUP debt queue).
- Review dimension NR — gave no reviews on the review day (he reviewed others' PRs on 08-21).

**Do:** Keep PR bodies at #1210's standard, including the 'what my first cut got wrong' line.

**Don't:** Don't leave a Critical-fix PR red and unattended — #1210 untouched since 07:18.

**Next improvement:** Delegate the reviewed-draft-to-send regression suite to Devin using #1210's QA fix-list as acceptance criteria.

### sameer-s-mansur — Medicodio

**Weighted: 6.9 (Mixed)** · Delivery 8 · Rigor 8 · Review NR · Devin 4 · Automation 5 · Consistency 8

**Evidence (Observed Fact)**

- 7 commits across two integration branches: app-team handoff docs, then Elaris filename-MRN chart pairing across all three facilities with OCR-first retired in the same change.
- Tests placed on the path production runs ('Test the step-11 guard where it actually runs'); F22 verification case added for the new pairing.
- No PR opened — both branches carried work past end of day, so no review and (once Actions returns) no gate saw it.
- Review dimension NR — gave no reviews on the review day.

**Do:** Keep retiring the mechanism you replace in the same change.

**Don't:** Don't run a hardening branch for days with no PR.

**Next improvement:** Open a draft PR for the pairing branch and let Devin generate the per-facility verification cases.

### anirudh-medicodio — Global Codio

**Weighted: 5.9 (Mixed)** · Delivery 7 · Rigor 5 · Review NR · Devin 5 · Automation 5 · Consistency 8

**Evidence (Observed Fact)**

- Landed GC #1202 (PERM case-manager parity, +6487/-2711 across 82 files) after four Devin Review passes and an architect review — the most complete pre-merge loop in the org.
- The PR body was merged as the unfilled repository template: every section still a placeholder, so the rationale for a 9,200-line change is not in the record.
- Merged while GitHub Actions had not executed a single run since 08-21 22:38 UTC; the post-merge deployment trigger failed to start.
- Review dimension NR — no review events on the review day.

**Do:** Keep the bot-review → architect-review → remediation → merge sequence.

**Don't:** Don't merge with the PR template unfilled.

**Next improvement:** Have Devin draft the PR body from the branch's commits so a complete description is the default.

### jatinkushwaha-medicodio — Medicodio

**Weighted: 6.0 (Mixed)** · Delivery 7 · Rigor 6 · Review NR · Devin 5 · Automation 4 · Consistency 7

**Evidence (Observed Fact)**

- PR #563 (+63/-38, 3 files): import batch sweep timezone safety (24h minimum protection for abandoned batches) and batch-number resolution split for event-driven vs RPA facilities.
- Body explains the reasoning in three bullets — above this repo's median — but the change re-tunes a previously shipped threshold and adds no test pinning it.
- Opened 16:12, bot review clean 16:16, empty human approval 16:17, merged 16:17 — 5 minutes open-to-merge on a production-bound branch; the deployment trigger then failed to start.
- Review dimension NR — gave no reviews on the review day (16 of his 30 weekly review events were low-information).

**Do:** Keep PRs at this size — 3 files with a stated rationale is cheap to review.

**Don't:** Don't treat 'Devin Review: No Issues Found' as the review.

**Next improvement:** Ask Devin for a DST/timezone boundary test matrix around the sweep threshold before touching it again.

### SaijyotiMeti — Global Codio

**Weighted: 5.7 (Mixed)** · Delivery 6 · Rigor NR · Review NR · Devin 4 · Automation 5 · Consistency 8

**Evidence (Observed Fact)**

- Inside the window: two branches created (00:08, 01:04) and two commits, including the Claude-authored 'Document Checklist Goal Agent (3rd CodioOps object type)'.
- The substantive continuation (2-state upload model, checklist audit events, summarizer registry replacing an objectType ternary, docs/atlas sync) landed 08-23 — credited to the next review day.
- Rigor / Review NR — insufficient in-window evidence, not a negative finding.
- Third instance of an existing object-type pattern with no Devin delegation of the mechanical half.

**Do:** Keep the feature-branch / claude-remediation-branch split.

**Don't:** Don't open a named feature branch with a generic 'Refactor code structure' subject.

**Next improvement:** Hand the next CodioOps object type's pattern-replication half to a Devin session.

### amit-pandey-medicodio — Medicodio

**Weighted: 4.5 (Needs Support)** · Delivery 5 · Rigor 4 · Review 3 · Devin 5 · Automation 4 · Consistency 6

**Evidence (Observed Fact)**

- Review-day activity is one approval (empty body) and the merge of #563 to Dev_1.0, 74 seconds after the bot review.
- The post-merge deployment trigger failed to start (Actions billing) and was not visibly noticed.
- Weekly context: 32 PRs authored and 34 review events given — all 34 low-information. Third consecutive review day this pattern is flagged.
- Owns the org's clearest Devin success (RPA Job Scheduler, nodejs #555 + react #484, merged 08-21) — capability proven, unused on the review day.
- Commit identity amit.p@medicodio.ai is still unlinked, so part of his Devin-assisted output attributes to a phantom account.

**Do:** Keep the fast turnaround — 5 minutes on a Saturday is genuinely valuable.

**Don't:** Don't approve with an empty body on a production-bound branch.

**Next improvement:** Add one sentence per approval naming what you verified — at 34 review events a week this moves the org number more than anyone else's change.

### Amrutha-Beedikar — Global Codio

**Weighted: 4.2 (Needs Support)** · Delivery 5 · Rigor 4 · Review 3 · Devin NR · Automation NR · Consistency NR

**Evidence (Observed Fact)**

- Approved GC #1202 — 82 files, +6487/-2711 — with the one-word body 'approved', then merged it.
- Prior scrutiny did exist (architect review plus four Devin Review passes); relying on it is legitimate, but the record does not say so.
- Devin / Automation / Consistency NR — no in-window evidence.
- The post-merge deployment trigger for dev failed to start.

**Do:** Keep sequencing merges after independent scrutiny.

**Don't:** Don't let 'approved' be the whole record for 82 files.

**Next improvement:** On the next >20-file review, write two lines: what you verified and whose review you are relying on.

### karthikmed — Shared / tooling

**Weighted: NR (NR)** · Delivery NR · Rigor NR · Review NR · Devin NR · Automation 3 · Consistency NR

**Evidence (Observed Fact)**

- Single review-day action: merged upstream paperclipai:master into the org's paperclip-ai fork at 03:19.
- Manual fork sync against an upstream that produced 10+ commits in the preceding 8 hours — script-automatable work being done by hand.
- All other dimensions NR — no in-window evidence. No overall rating is issued.

**Do:** Keep the fork current.

**Don't:** Don't do it by hand on a Saturday morning.

**Next improvement:** Replace the manual sync with a scheduled workflow once Actions billing is restored.

## How to read the spread

**Observed Fact.** The rated members split cleanly by role on this day: the four who wrote code (akanksh-rv, sameer-s-mansur, jatinkushwaha-medicodio, anirudh-medicodio) score 5.9-7.7, while the two whose only review-day action was approving and merging someone else's change (amit-pandey-medicodio, Amrutha-Beedikar) score below 5. Every human review event on the review day (2 of 2) was empty or one-word, and no dimension mean reaches 8.

**Inference.** The low Review and Automation means are not about individual diligence; they are what a process that has no enforced review-record standard and no working CI produces. On a day when no gate executed, an empty approval is the *only* remaining evidence that anything was checked — which is why the two reviewer-only cards land where they do. Equally, the code-writing scores are inflated by the absence of any gate that could have contradicted them.

**Recommendation.** Do not act on the reviewer-only cards as performance signals from this day alone; act on the two things that would change them structurally: restore Actions (so gates, not approvals, carry the evidence) and require one line per approval naming what was verified. Re-score after a full working day with CI running before drawing any conclusion about individuals.

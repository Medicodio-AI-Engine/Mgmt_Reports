# Dev review — decisions required

**Run:** `RUN_0005` · **Report date:** 2026-09-21 · **Stage:** `05_DEV_REVIEW` · **Status:** OK

> **Dry run.** No repository was modified, no commit or pull request was created, nothing was deployed, and no external system was changed. Everything below is analysis and proposal.

**Warnings**

- DATE_UNVERIFIED: 2026_09_21_Employee_Rating_Cards.md, 2026_09_21_Mgmt_Activity_Report.md; dated by filename only, no stated review date

Record each decision in the block under the issue: set `DECISION:` to exactly one of `APPROVE`, `REVIEW` (with at least one question), or `REJECT`, then commit this file. The next run reads it back.

Version 1 stops here. Approval does not promote anything to QA, UAT, or production.

## `ISSUE_000282` Workflow/infra change merged without a dry run of its own verification path

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 4 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:58` — Workflow/infra change merged without a dry run of its own verification path
- [RECOMMENDATION] `SOURCE_065:58` — Improve documentation/process — PR body for `.github/` changes must link a successful `workflow_dispatch` run (dry-run) before approval

### DECISION: ISSUE_000282_ATTEMPT_01
<!-- Workflow/infra change merged without a dry run of its own verification path -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000283` Findings left undispositioned on open PRs

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:59` — Findings left undispositioned on open PRs
- [RECOMMENDATION] `SOURCE_065:59` — Automate with Devin — triage drafts; owner confirms

### DECISION: ISSUE_000283_ATTEMPT_01
<!-- Findings left undispositioned on open PRs -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000284` Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable a

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: SECRETS
- Priority: 5 · Complexity: 8 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:62` — Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable across the six `deploy-prod-.yml` workflows.

### DECISION: ISSUE_000284_ATTEMPT_01
<!-- Ask Devin for a one-file PR adding a `Preflight: required vars` step to `acr-purge.yml` that fails fast with the list of missing `vars.`/`secrets.` — reusable a -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000285` (Carried) Devin triage of the 15 `#1394` findings into fix / accept / out-of-scope drafts.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:63` — (Carried) Devin triage of the 15 `#1394` findings into fix / accept / out-of-scope drafts.

### DECISION: ISSUE_000285_ATTEMPT_01
<!-- (Carried) Devin triage of the 15 `#1394` findings into fix / accept / out-of-scope drafts. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000286` Findings undispositioned

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:82` — Findings undispositioned — unchanged, +1 day (weekend)
- [RECOMMENDATION] `SOURCE_065:82` — Owner + date per finding Monday
- [REPORT_OBSERVATION] `SOURCE_065:82` — previous evidence: `#1382`/`#1384` 09-16 → 09-20; `#1394` 09-18 → 09-20

### DECISION: ISSUE_000286_ATTEMPT_01
<!-- Findings undispositioned -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000287` Infra change lands without exercising its own verification path

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:83` — Infra change lands without exercising its own verification path — `#1362` first scheduled run fails on missing `ACR_NAME`; `dry_run` never dispatched
- [RECOMMENDATION] `SOURCE_065:83` — Not yet a confirmed Repeat Pattern (two instances, different mechanisms); flagged for monitoring
- [REPORT_OBSERVATION] `SOURCE_065:83` — previous evidence: `#1382`/`#1384` hook (QA gate 09-16 found the merged spec red)

### DECISION: ISSUE_000287_ATTEMPT_01
<!-- Infra change lands without exercising its own verification path -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000288` 0-char approvals followed by immediate merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 3 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:106` — 0-char approvals followed by immediate merge
- [RECOMMENDATION] `SOURCE_065:106` — Improve documentation/process — approval text names what was checked (for infra PRs: "dry run link verified")

### DECISION: ISSUE_000288_ATTEMPT_01
<!-- 0-char approvals followed by immediate merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000289` Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off a

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: SECRETS
- Priority: 5 · Complexity: 6 · Tier: C
- Playbook: none matched
- Proposed action: PROPOSE: no approved playbook matched; request human direction.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:109` — Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off audit that would have caught `ACR_NAME` and may catch others.

### DECISION: ISSUE_000289_ATTEMPT_01
<!-- Ask Devin to enumerate every `vars.`/`secrets.` referenced across `.github/workflows/.yml` and diff against what is configured (read-only via API) — a one-off a -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000290` Empty approvals

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:123` — Empty approvals — `#1362` 0-char approval is the merge whose first run failed today
- [RECOMMENDATION] `SOURCE_065:123` — Approval names the check
- [REPORT_OBSERVATION] `SOURCE_065:123` — previous evidence: every report since 08-21

### DECISION: ISSUE_000290_ATTEMPT_01
<!-- Empty approvals -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000291` Branch protection not enabled (as EM)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:124` — Branch protection not enabled (as EM) — still not enabled (6th day; weekend)
- [RECOMMENDATION] `SOURCE_065:124` — Enable Monday
- [REPORT_OBSERVATION] `SOURCE_065:124` — previous evidence: recommended 09-16 → 09-20

### DECISION: ISSUE_000291_ATTEMPT_01
<!-- Branch protection not enabled (as EM) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000292` Carried: review-log / atlas / header-relocation commits by hand

- Category: AUTOMATION_OPPORTUNITY · Remediability: TOOLING_AUTOMATION · Security scope: NONE
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_QA_VALIDATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:145` — Carried: review-log / atlas / header-relocation commits by hand
- [RECOMMENDATION] `SOURCE_065:145` — Automate with Devin — bot commit from gate output; header lint rule

### DECISION: ISSUE_000292_ATTEMPT_01
<!-- Carried: review-log / atlas / header-relocation commits by hand -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000293` (Carried) 11 NEEDS-DECISION items from `#1391` as bounded Devin PRs with her written acceptance tests.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:148` — (Carried) 11 NEEDS-DECISION items from `#1391` as bounded Devin PRs with her written acceptance tests.

### DECISION: ISSUE_000293_ATTEMPT_01
<!-- (Carried) 11 NEEDS-DECISION items from `#1391` as bounded Devin PRs with her written acceptance tests. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000294` (Carried) Run the QA gate on the PR head before approval.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:149` — (Carried) Run the QA gate on the PR head before approval.

### DECISION: ISSUE_000294_ATTEMPT_01
<!-- (Carried) Run the QA gate on the PR head before approval. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000295` Reviewer remediates, approves, merges

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:162` — Reviewer remediates, approves, merges — no new instance; no control landed
- [RECOMMENDATION] `SOURCE_065:162` — Branch protection — owner anirudh
- [REPORT_OBSERVATION] `SOURCE_065:162` — previous evidence: `#1288` → `#1391` (09-06 → 09-18)

### DECISION: ISSUE_000295_ATTEMPT_01
<!-- Reviewer remediates, approves, merges -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000296` QA verdict consumed after merge

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:163` — QA verdict consumed after merge — `#1398` unacknowledged, day 3
- [RECOMMENDATION] `SOURCE_065:163` — Acknowledge in `#1391` Monday
- [REPORT_OBSERVATION] `SOURCE_065:163` — previous evidence: 8 consecutive large merges

### DECISION: ISSUE_000296_ATTEMPT_01
<!-- QA verdict consumed after merge -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000297` Carried: oversized single PR (`#1310`, `#1322`, `#1391`)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 4 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:184` — Carried: oversized single PR (`#1310`, `#1322`, `#1391`)
- [RECOMMENDATION] `SOURCE_065:184` — Improve documentation/process — split by runtime

### DECISION: ISSUE_000297_ATTEMPT_01
<!-- Carried: oversized single PR (`#1310`, `#1322`, `#1391`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000298` (Carried) Devin drafts §12.4/§12.5 measurement PR.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:187` — (Carried) Devin drafts §12.4/§12.5 measurement PR.

### DECISION: ISSUE_000298_ATTEMPT_01
<!-- (Carried) Devin drafts §12.4/§12.5 measurement PR. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000299` (Carried) One Devin PR per major #5–#11.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:188` — (Carried) One Devin PR per major #5–#11.

### DECISION: ISSUE_000299_ATTEMPT_01
<!-- (Carried) One Devin PR per major #5–#11. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000300` Author's findings dispositioned by the reviewer

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:201` — Author's findings dispositioned by the reviewer — follow-ups still unowned
- [RECOMMENDATION] `SOURCE_065:201` — Open follow-up PRs Monday
- [REPORT_OBSERVATION] `SOURCE_065:201` — previous evidence: `#1322` 09-11, `#1391` 09-18

### DECISION: ISSUE_000300_ATTEMPT_01
<!-- Author's findings dispositioned by the reviewer -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000301` Manual upstream fork sync (`paperclip-ai`)

- Category: MECHANICAL_MIGRATION · Remediability: CODE_CHANGE · Security scope: UNKNOWN
- Priority: 5 · Complexity: 5 · Tier: D
- Playbook: ORG_PB_MECHANICAL_MIGRATION
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:251` — Manual upstream fork sync (`paperclip-ai`)
- [RECOMMENDATION] `SOURCE_065:251` — Automate through scripts/tooling — scheduled sync, or archive

### DECISION: ISSUE_000301_ATTEMPT_01
<!-- Manual upstream fork sync (`paperclip-ai`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000302` (Carried) Fit assessment of `paperclip-ai` against the existing Devin/Claude workflow instead of a hand-maintained fork.

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 6 · Tier: D
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: DOCUMENT ONLY: human-owned surface; produce findings and a proposal.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:254` — (Carried) Fit assessment of `paperclip-ai` against the existing Devin/Claude workflow instead of a hand-maintained fork.

### DECISION: ISSUE_000302_ATTEMPT_01
<!-- (Carried) Fit assessment of `paperclip-ai` against the existing Devin/Claude workflow instead of a hand-maintained fork. -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


## `ISSUE_000303` Large invoicing PRs with badge-only bodies (`#652`/`#578`)

- Category: PROCESS_PRACTICE · Remediability: NON_CODE_PROCESS · Security scope: NONE
- Priority: 2 · Complexity: 8 · Tier: C
- Playbook: GEN_PB_PROCESS_IMPROVEMENT_PROPOSAL
- Proposed action: INVESTIGATE AND PROPOSE: no implementation until a human approves.

**Evidence**

- [REPORT_OBSERVATION] `SOURCE_065:267` — Large invoicing PRs with badge-only bodies (`#652`/`#578`) — untouched
- [RECOMMENDATION] `SOURCE_065:267` — Test-evidence body before review
- [REPORT_OBSERVATION] `SOURCE_065:267` — previous evidence: 09-17

### DECISION: ISSUE_000303_ATTEMPT_01
<!-- Large invoicing PRs with badge-only bodies (`#652`/`#578`) -->
<!-- Set DECISION to exactly one of APPROVE | REVIEW | REJECT, then commit. -->
DECISION: PENDING
REVIEWER:
COMMENTS:
QUESTIONS:


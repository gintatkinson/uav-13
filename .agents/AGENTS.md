# Project-Scoped Rules

## 1. Coordinator Role: Fast-Path Dispatch vs. Planned Edits
Thought blocks must focus directly on technical reasoning -- never emit startup checklists, initialization receipt tables, or "Ready for instructions" prompts.

- **Coordinator Mutation Lock**: The Coordinator NEVER edits, copies, moves, or deletes repository files directly (nor via `cp`, `mv`, `rm`, `tee`, `sed -i`, `>`, `>>`). All repository writes are delegated to single-item subagents.
- **Fast-Path 1 -- Pure Issue Dispatch (NO `implementation_plan.md` Required)**:
  - When the user commands dispatching issue(s) to `debug-protocol` or `adversarial-code-auditor`, the Coordinator acts strictly as a dumb router.
  - Do NOT read source code, do NOT read issue bodies to diagnose bugs, and do NOT write `implementation_plan.md`.
  - If given an issue range, run `gh issue list` to get open issue numbers, then immediately invoke one context-isolated subagent per issue with `PROCEED` and instructions to `view_file` the target `SKILL.md` first.
- **Fast-Path 2 -- Planned Modifications (`implementation_plan.md` Required)**:
  - When the Coordinator is designing a code/spec edit or running a specification/feature workflow, write an atomic (max 1 item) plan to `<appDataDir>/brain/<conversation-id>/implementation_plan.md` (or `.pipeline/plans/<slug>.md`) and wait for `PROCEED` before dispatching edit subagents. Never clobber root `./implementation_plan.md` or create `walkthrough.md` before completion.
- **Continuous Execution**: Once `PROCEED` is active, run dispatches, verification gates, and git pushes continuously to completion. Stop ONLY on: (1) non-zero tool/test exit codes, (2) unresolvable ambiguity, or (3) unapproved initial plans.

## 2. Subagent Isolation & Lazy Governance
- **Lazy Context Load**: Only once per session before a spec or feature workflow, silently check `test -d .pipeline/upstream`, `git status --short --branch`, `.pipeline/constitution.md`, and `.pipeline/ACTIVE_RULES_BUNDLE.md`. Skip on diagnostic turns, surgical edits, and inside subagents receiving `---GOVERNANCE-END---`. Read only the active `SKILL.md` (and `.pipeline/profiles/<target_platform>.md` only during downstream implementation).
- **Subagent Rules**:
  1. **Fresh Context & Atomic Scope**: 1 item max per subagent (1 issue, 1 Epic/Feature/Story/Use Case, or 1 `part def` component in Step 1.5 `Component Failure Mode Researcher` swarms). Reclaim/terminate subagents immediately on completion.
  2. **Skill vs. Surgical Edit**: For skill workflows, subagents `view_file` the active `SKILL.md` first and reject steered/summarized prompts. For bounded surgical edits with approved `Target`/`Replacement` blocks in `implementation_plan.md`, subagents skip `SKILL.md` and run `edit_file` directly.
  3. **Strict Target Boundary**: Subagents only read/write assigned target files and never redundantly run `verify-baseline`, `cargo test`, `git commit`, or `git push` (verification and commits run once at the Coordinator level).
  4. **3-Layer Definition of Done**: Every spec item and micro-task must close all 3 layers: (1) Domain State & Data Model, (2) Logic & State Management, (3) Presentation & Actuator Interface Binding (`N/A` is forbidden).

## 3. Repository Role, Clean Landing Zones & Black-Box Firewall
- **Role Detection**:
  - **`.pipeline/upstream/` present (`UPSTREAM_SPEC_CORE_COMPILER`)**: `DEAP01-spec-core` compiler repo. Landing zones (`schema/`, `docs/epics/`, `docs/features/`, `docs/user-stories/`, `docs/use-cases/`) must contain ONLY `.gitkeep`. Never commit domain/customer specs or hardcode domain concepts; all specs derive deterministically from `schema/` AST nodes.
  - **`.pipeline/upstream/` absent (`DOWNSTREAM_CUSTOMER_PROJECT`)**: Downstream workspace (`schema/` and `.pipeline/schema.sysml` are 100% SSOT). Requires root `.gitignore`, zero `.DS_Store`, and zero duplicate master blueprints.
- **Downstream Binary-Only Firewall**: Tier-0 compiler source (`crates/*`, `Cargo.toml`, `Cargo.lock`), `.pipeline/upstream/`, and `docs/architecture/blueprints/` reside exclusively in `DEAP01-spec-core`. Never copy Tier-0 `crates/*` or run `cargo build` downstream, and never read `../DEAP01-spec-core/crates/*` from a downstream session.
- **Upstream Defect Reporting**: Report compiler/tooling bugs via `skills/adversarial-code-auditor/SKILL.md` to produce a 7-section dossier in `.pipeline/defects/<NAME>.md` and validate/publish via `./target/release/verify-baseline check-defect .pipeline/defects/<NAME>.md` (or `./target/release/verify-baseline audit-code --path <PATH>`). Never apply silent local patches.

## 4. Native Rust TDD & 3-Tier Verification Gates
- **Checks 32, 33 & 34 (Pure Rust)**: Shell scripts (`*.sh`), regex crates, and Python/pytest files (`*.py`, `pytest`, `python3`) are strictly prohibited across the workspace. Retired scripts (`verify_downstream_baseline.py`, `sysmlv2_ingest.py`, `e2e_acceptance_harness.py`, `reconcile_backlog.py`, `parity_auditor`, `setup_git_hooks.sh`) are permanently retired and forbidden.
- **Mandatory Rust RED-GREEN-REFACTOR TDD**: All executable code changes in `crates/` require native Rust `#[test]` unit/mutation tests demonstrated RED before implementation and GREEN after. Use auto-cleaned temp directories for test fixtures (never create mock test dirs in the workspace, and never write `fs::read_to_string` tests asserting Markdown prompt prose).
- **3-Tier Pre-Commit Gate (Coordinator Level Only)**:
  - **Tier 1 (Markdown/Governance only)**: Zero `cargo` runs; run `./target/release/verify-baseline . --no-domain` before commit.
  - **Tier 2 (Single-crate internal change)**: `cargo test -p <crate> <filter>` during TDD; `cargo test -p <crate>` before commit (rebuild `--release` binary only if CLI runtime code changed).
  - **Tier 3 (Cross-crate `pub` API or `Cargo.toml` change)**: `cargo test -p <crate>` + `cargo check --workspace --all-targets` during iteration; `cargo test --workspace` before commit.
- **Native Binaries & Step 4 Builds**: Use `./target/release/{verify-baseline,reconcile-backlog,compile-sysml,ingest-sysml,assemble-conops}`. Run full app compilation (`flutter build` / `npm run build`) during Step 4 verification.

## 5. Git Hygiene, Formatting & Workspace Invariants
- **Parallel-Safe Scoped Git & Remote Sync**: Stage and commit only explicit paths (`git add -- <files>` and `git commit --only -- <files>`). Unscoped `git add .`, `git add -A`, `git commit -a`, `git checkout .`, `git restore .`, and `git stash` are forbidden. Verify `git diff origin/<branch>` is empty before final reporting. Update `README.md` when rules/directories change; never wholesale-replace docs without user approval.
- **Commit Non-Closure & Issue Transition**: Auto-closing keywords (`fix #`, `fixes #`, `close #`, `resolve #`) are forbidden; use `(#<id>)` or `(refs #<id>)`. Transition fixed issues to `status:fixed-resolved` (or `status::fixed-resolved` on GitLab) with verification evidence before walkthrough completion.
- **Paths & Formatting**:
  - **Zero Em Dash**: Unicode em dashes (`\u2014`) are forbidden everywhere; use `--` or `-`.
  - **Relative Paths**: Use only workspace-relative (`./...`) or env-derived paths. Root source writes are forbidden (`app_flutter/` for Flutter, `web_react/` for React). Commit durable artifacts in `docs/`, `schema/`, or `.pipeline/defects/`.
  - **Mermaid & KaTeX (Checks 13 & 13B)**: Mermaid blocks require valid diagram headers, newline closing fences, double-quoted labels for special characters, zero inline backticks, zero unquoted angle brackets, and zero curly braces or colons in class members. KaTeX display math must use isolated delimiter lines with `aligned` blocks and never wrap requirement/hazard IDs in math delimiters.
  - **Empirical State & `exebox` TLS**: Verify state via `git status`, `ls`, and `gh issue view`/`gh api` (using `<ADDITIONAL_METADATA>` for date). If `gh` hits `x509`/`401` on macOS `exebox`, run `security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain-db /tmp/antigravity-ca.crt` and `gh auth token | gh auth login --with-token --insecure-storage`.
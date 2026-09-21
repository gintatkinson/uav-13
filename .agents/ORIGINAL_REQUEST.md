# Original User Request

## 2026-09-21T11:20:52Z

Fix the two-tier installation and propagation architecture in DEAP01-spec-core so that domain repositories scaffold self-contained install instructions pointing to themselves, enabling customer project repositories to install cleanly in isolation without references to spec-core or broken local paths.

Working directory: /Users/perkunas/jail/DEAP01-spec-core
Integrity mode: development

## Requirements

### R1. Two-Tier Architecture Alignment
- Distinguish Tier 1 (Upstream Compiler DEAP01-spec-core -> Domain Distribution Template DEAP-*) from Tier 2 (Domain Distribution Template DEAP-* -> Customer Application Workspace uav-*).
- Update DEAP01-spec-core/README.md to document this two-tier boundary cleanly, preventing maintainers and users from conflating compiler tooling propagation with end-user customer onboarding.

### R2. Parameterized Domain Installer & Scaffolding
- Update scripts/install_pipeline.sh so that when it scaffolds or updates a downstream domain repository's README.md, the installation section automatically embeds the domain repository's own git remote URL rather than defaulting to DEAP01-spec-core.
- In downstream domain repositories, the documented onboarding command for end-user customer projects must be a single self-contained command operating strictly inside the customer project directory with zero sibling path dependencies (../...):
  git clone <domain-repo-remote-url> ./.tmp-pipeline && bash ./.tmp-pipeline/scripts/install_pipeline.sh . && rm -rf ./.tmp-pipeline

### R3. Robust Model & Schema Copying
- Ensure scripts/install_pipeline.sh copies domain models and schemas from the domain repo into the target customer project directory even if an empty schema/ directory already exists.

## Acceptance Criteria

### Verification & Conformance
- [ ] python3 scripts/verify_downstream_baseline.py --no-domain passes all checks cleanly in DEAP01-spec-core.
- [ ] Code blocks in all updated markdown files contain pure, valid shell syntax with zero unescaped parentheses in comments and zero unquoted angle-bracket placeholders.
- [ ] Downstream README generation logic in scripts/install_pipeline.sh produces verified, self-contained onboarding instructions using the target domain's remote URL.

PROCEED

## 2026-09-21T11:40:40Z

Implement Level 0 OEM prose/markdown ingestion support in sysmlv2_ingest.py and update the Operator Prompt Catalog / Pipeline 0 sequence in DEAP01-spec-core so that downstream customer projects starting with unstructured/prose manuals (markdown, PDF, BOM tables) have a sanctioned, deterministic path to generate schema/model.sysml and satisfy the compilation gate without deadlocking.

Working directory: /Users/perkunas/jail/DEAP01-spec-core
Integrity mode: development

## Requirements

### R1. Level 0 Markdown / BOM Schema Ingestion in sysmlv2_ingest.py
- Extend skills/spec-orchestrator/scripts/sysmlv2_ingest.py to support --format markdown (or --format auto detection of markdown tables / BOM specifications in schema/ and schema/extracted/).
- Parse structured Markdown tables (e.g. components, BOMs, signal/port interfaces, parametric ranges) and translate them into a valid, canonical SysML v2 textual model (schema/model.sysml / .pipeline/schema.sysml) with complete package, part def, port definitions, and constraint blocks.

### R2. Operator Prompt Catalog & Pipeline 0 Sequence Remediation
- Update the Operator Prompt Catalog (in scripts/install_pipeline.sh, skills/spec-orchestrator/SKILL.md, and downstream README templates) to formalize Step 0.0: Level 0 OEM Ground Truth Ingestion:
  - Explicitly document the entrypoint for customer projects starting with prose/PDF documentation.
  - Clarify that extracting BOM and physical parameters into schema/extracted/ and synthesizing schema/model.sysml is authorized under Check 23 and is the required precursor to running compile_sysml.py --compile.
  - Provide a dedicated subagent prompt for Level 0 OEM Ground Truth extraction and SysML v2 model authoring.

### R3. Pipeline 0 Compilation Gate Fallback & Helpful Error Messages
- Update scripts/compile_sysml.py so that when no .sysml file is found in schema/, the error message does not just raise an unhelpful FileNotFoundError, but provides clear remediation instructions directing the user/agent to run Step 0.0 / sysmlv2_ingest.py.

## Acceptance Criteria

### Verification & Conformance
- [ ] Unit tests added in tests/ verifying markdown table / BOM ingestion into SysML v2 AST.
- [ ] python3 skills/spec-orchestrator/scripts/sysmlv2_ingest.py --schema <sample_markdown> --format markdown --out .pipeline/schema.sysml successfully produces a valid SysML v2 AST parseable by compile_sysml.py.
- [ ] python3 scripts/verify_downstream_baseline.py --no-domain passes all checks cleanly in DEAP01-spec-core.
- [ ] All updated markdown code blocks contain valid shell syntax with zero unescaped parentheses in comments.

PROCEED


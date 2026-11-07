# Procedural Blueprint: Deterministic Specification Synthesis & Enhancement (Tooling-Anchored, Agent-Elaborated)

## Executive Summary

This blueprint establishes the standard operating procedure for synthesizing rich, mathematically grounded, and regulatory-compliant engineering specifications (SysML v2, ConOps, Mission Intent, STPA, and C-ABI contracts) from raw manuals and problem briefs for the uav-13 platform.

It resolves the dual failure modes of:

1. **Raw Compiler Scaffolding Only**: Emitting hollow, generic skeletons (`Loss of safe function of SensorModality`, `as_str`, `{{PLACEHOLDERS}}`).
2. **Uncontrolled Agent Swarms**: Unleashing unmonitored background agents that make invisible, commingled changes across the repository and break determinism.

---

## The 3-Tier Operating Principle

```
+-----------------------------------------------------------------------------------+
| Tier 1: Compiler Scaffolding & Verification Gate (100% Rust Tooling)             |
|   - Generates AST digests, tables, schemas, and structural boundaries             |
|   - Runs cryptographic hashing, syntax checks, and mathematical constraint gates   |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Tier 2: Single-Item Controlled Elaboration (Single-Unit Agent Scope)             |
|   - Takes 1 unit / 1 topic at a time (Max 1 file per turn)                        |
|   - Grounded strictly in schema/SSOT AST nodes and normative standards           |
|   - Emits rich domain prose, KaTeX physics equations, and operational doctrine    |
|   - Zero background swarms; exact diff presented in the conversation turn         |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
| Tier 3: Closed-Loop Tooling Acceptance (100% Rust Tooling)                       |
|   - Tooling verifies unit immediately (assemble-conops --verify, verify-baseline) |
|   - Rejects ungrounded parameters, broken syntax, or placeholder tokens           |
+-----------------------------------------------------------------------------------+
```

---

## End-to-End Procedural Lifecycle

### Phase -1: Provenance Reset & Input Allowlist (100% Tooling + Coordinator)

*Objective: Quarantine unverifiable derived artifacts before any ingestion so that no circular, self-generated, or provenance-free content enters the canonical model.*

1. **Quarantine Unverifiable Derived Artifacts**:
   - Move prior generated or unverifiable derived artifacts into `.pipeline/legacy/pre-rebuild/` with a `MANIFEST.md` recording relative path, byte size, SHA-256, and quarantine reason (`legacy-derived`, `unverifiable-provenance`, or `reference`).
   - The uav-13 legacy snapshot MUST quarantine the prior single-file ingestion dump `schema/avenger_v2_5_sysml_v2_ingestion.md`, stale `schema/extracted/*` snapshots, and the prior `.pipeline/schema-digest.json` output.
   - Never add `.pipeline/legacy/` to any ingest, compile, or verify input path.
2. **Curated Input Allowlist**:
   - Ingest ONLY explicitly allowlisted OEM source files (for example `schema/extracted/oem_bom.md`, `schema/extracted/interface_table.md`, `schema/extracted/parametric_limits.md`, and the raw OEM manuals they derive from).
   - Recursive ingestion of the whole `schema/` tree is forbidden; pass explicit file paths or a curated allowlist directory.
3. **Numeric Provenance Citations**:
   - Every extracted physical parameter, component count, and interface in `the three schema/extracted tables` MUST cite its OEM source as `file:line`.
   - Any parameter without a `file:line` citation is a Check 23 violation and must be quarantined, not elaborated.

#### uav-13 Canonical Terminology & Scope Decisions (binding for all downstream phases)

These decisions are authoritative for this repository and MUST be applied consistently across every specification unit, safety artifact, and generated contract:

1. **`Ruddervator` is the canonical term**. The synonym `tail stabiliser` may appear only as a parenthetical clarification. The token `Fins` is forbidden anywhere in the specification tree.
2. **ESAD is a Critical (DAL-A) arming device**. The Electronic Safe and Arm Device MUST be modelled and analysed at the highest criticality tier (DAL-A), and its contributing failures must be treated as catastrophic under the safety loss taxonomy.
3. **Parachute is a non-mission variant**. The parachute recovery variant is excluded from the baseline losses, hazards, STPA/FMECA matrices, and ConOps operational scope. It must not introduce baseline mission losses or hazards.
4. **User manual authority for flight limits**. All flight-limit values (airspeed, altitude, load factor, operating envelope) derive from the user manual and MUST carry `file:line` provenance; no flight limit may be invented or synthesized without that citation.

---

### Phase 0: Unstructured / Prose Ingestion & Canonical SysML v2 Synthesis (Step 0.0)

*Objective: Ingest raw OEM technical documentation, flight/operating manuals, ICD tables, and BOM markdown tables located in `schema/` and `schema/extracted/`, extract physical parameters, component hierarchies, mass/power budgets, port/pin interfaces, and operational envelopes, and synthesize the canonical SysML v2 textual model per Check 23.*

#### 1. Worker 00: OEM Prose / BOM Ingestion & Model Synthesis Prompt (Step 0.0)

Dispatch a context-isolated subagent with the canonical Worker 00 prompt defined in README.md Section 4.2.0:

```text
Execute `view_file` on `skills/spec-orchestrator/SKILL.md` as your very first step before taking any action.

Repository Classification: DOWNSTREAM_CUSTOMER_PROJECT

Role: Worker 00 -- OEM Prose / BOM Ingestion & Model Synthesizer (Step 0.0)

Primary Commercial Toolchain Integration Context:
This project explicitly declares MATLAB / Simulink / Stateflow / Embedded Coder as the Primary Tier-1 Commercial Toolchain Integration Context (Model-Based Design, Control Law Synthesis, DO-178C C/SPARK Ada code generation).

Directive:
Execute Level 0 OEM Ground Truth Ingestion and initial SysML v2 textual model synthesis for customer projects starting from unstructured OEM prose manuals, PDF documentation, markdown tables, or Bill of Materials (BOM) specifications:

1. Unstructured & Semi-Structured Ingestion Scope:
   - Ingest raw OEM technical documentation, flight/operating manuals, ICD tables, and BOM markdown tables located in `schema/` and `schema/extracted/`.
   - Authorized Under Check 23: Extract physical parameters, component hierarchies, mass/power budgets, port/pin interfaces, and operational envelopes into machine-readable Markdown tables in `schema/extracted/` (e.g., `schema/extracted/oem_bom.md`, `schema/extracted/interface_table.md`, `schema/extracted/parametric_limits.md`).

2. Canonical SysML v2 Model Synthesis:
   - Execute the Level 0 ingestion translator:
     ./target/release/ingest-sysml -s "schema/extracted/" -f markdown -o "schema/model.sysml" -d ".pipeline/schema-digest.json"
   - Alternatively, synthesize a formal SysML v2 textual model `schema/model.sysml` directly, defining:
     * Root `package` matching the uav-13 platform.
     * All component definitions as canonical `part def` elements with typed attributes (mass, power, dimensions, channel count, part numbers), using `Ruddervator` (never `Fins`).
     * Directional communication and electrical interface boundaries as `port def` elements (`in`, `out`, `inout`).
     * Physical, environmental, and operational constraints as `constraint def` / `assert constraint` blocks.
     * State machine structures and operational lifecycle phases as `state def` elements.

3. Compilation Gate Precursor Verification:
   - Verify that the generated `schema/model.sysml` passes the Step 0 SysML Compilation Gate:
     ./target/release/compile-sysml --compile --schema .pipeline/schema.sysml --out .pipeline/schema.sysml --digest .pipeline/schema-digest.json
   - Ensure `.pipeline/schema.sysml` and `.pipeline/schema-digest.json` are successfully generated without compilation errors.
   - Verify Check 23 compliance (Factual Grounding & Numeric Provenance Gate): all physical parameters and component counts in `schema/model.sysml` strictly match the Level 0 OEM ground truth in `schema/extracted/`.

Defect Filing Directive:
If any compiler fault, schema inconsistency, or invariant violation is discovered, you are strictly forbidden from filing raw issues directly. You MUST dispatch a fresh context-isolated subagent with `skills/adversarial-code-auditor/SKILL.md` to perform the 5-pillar audit and produce a verified 7-section defect dossier under `.pipeline/defects/<NAME>.md`. Validate and publish it with:
```zsh
./target/release/verify-baseline check-defect .pipeline/defects/<NAME>.md
```
This atomically validates all checks, persists the dossier, and publishes or updates the upstream issue (add `--dry-run` to validate only). Issue auto-closing keywords or issue close commands are strictly forbidden.

PROCEED
```

#### 2. The 3 Mandatory Extraction Tables (Check 23 Standard)

The extraction process under Check 23 synthesizes the following three tables under `schema/extracted/`:

- **`schema/extracted/oem_bom.md`** (Physical Hardware & Subsystem Hierarchy):
  ```markdown
  # OEM Bill of Materials (BOM)

  | Subsystem | Component Name | Part Number | Mass (kg) | Power (W) | Interface |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  ```

- **`schema/extracted/parametric_limits.md`** (Physical Limits & Performance Bounds):
  ```markdown
  # Parametric Limits & Performance Bounds

  | Parameter ID | Parameter Name | Min | Max | Units | Verification Source |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  ```

- **`schema/extracted/interface_table.md`** (Input/Output Ports & Protocols):
  ```markdown
  # Interface & Signal Dictionary

  | Port Name | Direction | Protocol | Data Type | Refresh Rate | Associated Subsystem |
  | :--- | :--- | :--- | :--- | :--- | :--- |
  ```

#### 3. Compilation & AST Digest Gate (100% Tooling)

Once the extraction files exist in `schema/extracted/` or `schema/model.sysml` is synthesized, run the compilation and verification gates:

Step 1: Ingest extracted markdown tables into SysML v2:
```zsh
./target/release/ingest-sysml -s schema/extracted/ -f markdown -o .pipeline/schema.sysml -d .pipeline/schema-digest.json
```

Step 2: Compile AST and lock SHA-256 digest:
```zsh
./target/release/compile-sysml --compile --schema .pipeline/schema.sysml --out .pipeline/schema.sysml --digest .pipeline/schema-digest.json
```
*Gate: Exit code `0`; `.pipeline/schema.sysml` and `.pipeline/schema-digest.json` successfully generated.*

---

### Phase 1: Structural Scaffolding Generation (100% Tooling)

*Objective: Use compiler binaries to generate the structural skeletons, tables, and contract bindings.*

1. **Scaffold Safety & STPA Suite (Tooling)**:
   ```zsh
   ./target/release/compile-sysml --schema .pipeline/schema.sysml --stpa-transpile --out-dir docs/safety/
   ```
   *Result: Emits the 10-pillar STPA scaffolding, table schemas, and initial RPN calculations. Elaboration must satisfy the repo's enforced Check 17 schema; do not reduce the pillar count.*
2. **Scaffold Modular ConOps Units (Tooling)**:
   - Ensure unit skeleton templates exist under `docs/conops/units/conops/` (`01` through `12`) and `docs/conops/units/mission_intent/` (`01` through `10`).
3. **Scaffold Platform Contracts (Tooling)**:
   ```zsh
   ./target/release/compile-sysml --schema .pipeline/schema.sysml --emit-flutter-contracts app_flutter/ --force
   ```
   *Result: Emits typed DTOs, domain seeds, and FFI shims.*

---

## Phase 2: Serialized, Single-Unit Domain Elaboration (Controlled Agents)

*Objective: Systematically replace hollow compiler scaffolding (`Loss of safe function of SensorModality`, `as_str`, `{{PLACEHOLDERS}}`) with rich, defense-grade engineering specifications, KaTeX physics equations, and regulatory compliance. Every unit is elaborated independently (Max 1 file per turn) and immediately verified by compiler gates.*

#### Strict Execution Guardrails:

- **Rule of One**: Exactly **1 unit file** opened, elaborated, and committed per turn. Never touch multiple files in a single pass.
- **Contract Boundary**: The agent must ingest ONLY `.pipeline/schema.sysml`, `the three schema/extracted tables`, and the active unit file. Reading outside this boundary is forbidden.
- **Zero Placeholder Invariant**: All `{{...}}`, `PENDING`, `PENDING_PARAMETER`, `TODO`, `TBD`, and generic method identifiers (`as_str`, `fmt`) must be permanently eradicated.
- **Compiler Immediate Gate**: Every single file must pass its per-file gate (`verify-baseline . --spec-only --only "<file>"` or `assemble-conops --verify`) immediately upon writing. If a check fails, the turn halts and fixes it before moving forward.
- **Git Hygiene & Explicit-Path Staging**: At the start of every turn run `git status --short --branch` and confirm the working tree is clean against `origin/<branch>`. If the tree is dirty, stop and resolve or quarantine the unrelated changes before elaborating. Never use `git add .`, `git add -A`, `git commit -a`, `git checkout .`, `git restore .`, or `git stash`; stage and commit only the active unit with `git add -- <target-file>` and `git commit --only -- <target-file>`.

---

### 2.1 ConOps & Mission Intent Modular Elaboration

The compiler scaffolding creates 22 modular unit files under `docs/conops/units/`. These files must be processed one at a time across two sequential catalogs.

#### 1. The 22 Canonical Unit Catalogs (uav-13)

**Catalog A: 12 ConOps Units (`docs/conops/units/conops/`)**:

1. `01_METADATA_AND_OVERVIEW.md` - Scope, system identification, normative baseline, physical/legal boundaries, stakeholder roster, and user classes (`UCL-xx`).
2. `02_DEFICIENCIES_AND_MOTIVATION.md` - Predecessor baseline, technical, operational, and human deficiencies motivating the platform.
3. `03_PROPOSED_CAPABILITIES.md` - Mission drivers, value propositions, and engineering trade-off evaluations.
4. `04_SYSTEM_ARCHITECTURE.md` - Super-system architecture across Platform, Ground Segment, and Launch Segment; subsystem architecture subsections covering 100% of declared AST `part def` nodes; port taxonomy and SSOT model binding.
5. `05_OPERATIONAL_STATE_SPACE_AND_RISK.md` - 4D volume formulation, boundary containment margin ($R_{\mathrm{containment}} \ge R_{\mathrm{min}}$), and boundary containment / risk parameters table.
6. `06_UAF_OPERATIONAL_ACTIVITIES.md` - Open-ended UAF activity roster (`OA-XX`) with mandatory Gate 24 allocation tags.
7. `07_OPTX_EXCHANGES.md` - Operational information exchange roster (`OpTx-XX`) with source, destination, data rates, latency limits, and criticality.
8. `08_ENVIRONMENTAL_OPERATING_LIMITS.md` - Ambient temperature, ingress protection (IP), electromagnetic/RF environment, and spatial clearance envelopes.
9. `09_SCENARIOS_AND_TIMELINES.md` - Nominal, degraded, and contingency scenario threads (`SCN-XX`) with an `OV-6c` Mermaid sequence diagram per scenario.
10. `10_MAINTENANCE_AND_GSE_SUPPORT.md` - Three-tier Organizational (O-Level), Intermediate (I-Level), Depot (D-Level) maintenance and GSE support model.
11. `11_IMPACTS_AND_TRADE_STUDIES.md` - Operational impacts, system limitations, and documented trade studies.
12. `12_EMERGENCY_DECISION_MATRIX.md` - Minimum 7 canonical emergency triggers (seven `EMG-XX` triggers) with deterministic recovery actions.

**Catalog B: 10 Mission Intent Units (`docs/conops/units/mission_intent/`)**:

1. `01_COMMANDERS_INTENT.md` - Operational purpose, key mission tasks, and desired end state.
2. `02_MISSION_ESSENTIAL_TASK_LIST.md` - Doctrinal Mission Essential Task List (`MET-XX`) with conditions, quantitative metrics, verification methods, and Gate 24 allocation tags.
3. `03_INCOSE_MOE_MOP_MATH.md` - INCOSE SEH v5.0 Measures of Effectiveness (MoE) and Measures of Performance (MoP) with KaTeX formulas, Threshold/Objective values, and engineering units.
4. `04_MULTI_DOMAIN_THREAT_MATRIX.md` - Open multi-domain threat matrix across all canonical operational domains (Kinetic, Mechanical, Power/Thermal, Environmental, EW/Cyber, Optical, Signature/Acoustic, Human Factors, CBRN) with public clause citations.
5. `05_PACE_C2_PLAN.md` - 4-tier PACE communications plan (Primary, Alternate, Contingency, Emergency) with schema-derived frequency bands, bandwidth, and parameterized heartbeat timeouts.
6. `06_SAFETY_INTERLOCKS.md` - Safety constraints, interlock predicates, and subsystem state interlocks (`INT-XX`) derived from AST constraint and state definitions, including the ESAD Critical (DAL-A) arming interlock.
7. `07_AIRSPACE_GEOZONES.md` - Primary boundary perimeter, dynamic exclusion/keep-out zones, and horizontal/vertical separation minima.
8. `08_GO_NO_GO_MATRIX.md` - Operational phase checks (`GNG-XX`), threshold conditions, sensors/mechanisms, and deterministic Go/No-Go actions.
9. `09_BINGO_ENERGY_MATH.md` - Critical energy dynamics formulation ($E_{\mathrm{critical}}(t)$ or $R_{\mathrm{threshold}}(t)$), statutory reserve ratio constraint ($\ge 20\%$), and energy parameter table.
10. `10_OPERATIONAL_ALLOCATION_TAGS.md` - Comprehensive listing of Gate 24 allocation tags (`/// OperationalAllocation: [MET-XX]`) for cross-model traceability.

#### 2. The Coordinator-Dispatched Per-Unit Loop

The coordinator never elaborates units itself. It dispatches exactly one fresh, context-isolated subagent per unit, never runs two unit subagents concurrently, and advances to the next unit only after both gates in the prompt below pass. Every dispatch uses this normative per-unit elaboration prompt, with placeholders resolved from the unit catalog and the unit input matrix.

```text
Role: Single-Unit <ConOps|Safety> Elaborator -- <UNIT_ID> (one file only).

Step 1: read skills/<ACTIVE_SKILL>/SKILL.md.
Step 2: read the canonical template <TEMPLATE_PATH>.

Target file: <UNIT_FILE>.

Allowed inputs: the target file, .pipeline/schema.sysml,
schema/extracted/oem_bom.md, interface_table.md, parametric_limits.md,
<UNIT_ADDITIONAL_INPUTS>. No other files.

Required content (unit mandatory):
<UNIT_MANDATORY_CONTENT>.

Grounding rules:
- Every numeric value cites schema/extracted/parametric_limits.md or an OEM file:line.
- OEM silence -> "Not stated in OEM sources." Never invent.
- Ruddervator canonical (Fins/tail stabiliser only as parenthetical synonyms).
- ESAD Critical (DAL-A); parachute non-mission variant excluded from baseline.
- No ungrounded protocols (Check 23); no literal OA-/MET- numeric IDs (Check 25).
- KaTeX display math only; no math inside tables; ASCII only; no placeholders.

Gates, in order:
1. ./target/release/verify-baseline . --spec-only --only "<UNIT_FILE>"
2. ./target/release/assemble-conops --input-dir docs/conops/units/ --output-dir docs/conops/ --verify
Fix until both exit 0. Do not touch other files. No git.

Report: exit codes, what changed, OEM-silent fields.
---GOVERNANCE-END---
PROCEED
```

**Unit input matrix**:

- Every unit requires `.pipeline/schema.sysml` and the three tables `schema/extracted/oem_bom.md`, `schema/extracted/interface_table.md`, and `schema/extracted/parametric_limits.md`; `<UNIT_ADDITIONAL_INPUTS>` carries only unit-specific additions.
- `01_METADATA_AND_OVERVIEW` additionally requires `docs/research/RESEARCH_INVENTORY.md`; for every other unit `<UNIT_ADDITIONAL_INPUTS>` is `none` unless its catalog entry states otherwise.
- `<UNIT_MANDATORY_CONTENT>` is resolved from the catalog description for that unit in Catalog A or Catalog B above.
- `<TEMPLATE_PATH>` is `skills/spec-conops-engineering/resources/units/conops/01_METADATA_AND_OVERVIEW.md` for unit 01 and the matching resource `skills/spec-conops-engineering/resources/units/<conops|mission_intent>/<UNIT_ID>.md` for each other unit.
- `<ACTIVE_SKILL>` is `spec-conops-engineering`; `<UNIT_FILE>` is `docs/conops/units/<conops|mission_intent>/<UNIT_ID>.md`.

**Unit-01 worked example (reference instance)**:

```text
Role: Single-Unit ConOps Elaborator -- 01_METADATA_AND_OVERVIEW (one file only).

Step 1: read skills/spec-conops-engineering/SKILL.md.
Step 2: read the canonical template skills/spec-conops-engineering/resources/units/conops/01_METADATA_AND_OVERVIEW.md.

Target file: docs/conops/units/conops/01_METADATA_AND_OVERVIEW.md.

Allowed inputs: the target file, .pipeline/schema.sysml,
schema/extracted/oem_bom.md, interface_table.md, parametric_limits.md,
docs/research/RESEARCH_INVENTORY.md. No other files.

Required content (unit mandatory):
Scope, system identification, normative baseline, physical/legal boundaries,
stakeholder roster, and user classes (UCL-xx).

Grounding rules:
- Every numeric value cites schema/extracted/parametric_limits.md or an OEM file:line.
- OEM silence -> "Not stated in OEM sources." Never invent.
- Ruddervator canonical (Fins/tail stabiliser only as parenthetical synonyms).
- ESAD Critical (DAL-A); parachute non-mission variant excluded from baseline.
- No ungrounded protocols (Check 23); no literal OA-/MET- numeric IDs (Check 25).
- KaTeX display math only; no math inside tables; ASCII only; no placeholders.

Gates, in order:
1. ./target/release/verify-baseline . --spec-only --only "docs/conops/units/conops/01_METADATA_AND_OVERVIEW.md"
2. ./target/release/assemble-conops --input-dir docs/conops/units/ --output-dir docs/conops/ --verify
Fix until both exit 0. Do not touch other files. No git.

Report: exit codes, what changed, OEM-silent fields.
---GOVERNANCE-END---
PROCEED
```

#### 3. Verification Gate (Run Immediately After Each Unit)

Run the per-file specification gate for the active unit:
```zsh
./target/release/verify-baseline . --spec-only --only "docs/conops/units/conops/01_METADATA_AND_OVERVIEW.md"
```
*Gate: Exit code 0. If `verify-baseline` reports any syntax error, broken table, or missing header, halt and fix that unit before touching any other file.*

Once all 22 units are elaborated and pass per-file verification, compile the master documents and run the full baseline exactly once:
```zsh
./target/release/assemble-conops --input-dir docs/conops/units/ --output-dir docs/conops/ --verify
./target/release/verify-baseline . --no-domain
```

---

### 2.2 STPA Hazard Analysis & FMECA Safety Elaboration

The compiler transpiles initial structural safety matrices into `docs/safety/`. These raw files are hollow code-level scaffolds (for example, listing Rust methods like `as_str` or `fmt` as failure modes). They must be elaborated one by one into real cyber-physical safety analyses.

#### 1. The 9 Canonical Safety Files

1. `01_LOSSES_HAZARDS_TOPOLOGY.md` - System mission losses (L-XX), system-level hazards (H-XX), and hierarchical control structure topology.
2. `02_UCA_COMBINATORIAL_MATRIX.md` - Unsafe Control Actions (UCA-XX) evaluated across the 4 universal failure modes.
3. `03_LOSS_SCENARIOS.md` - Causal scenarios ($LS-1..N$) detailing how UCAs occur through controller, sensor, actuator, or environmental degradation.
4. `04_SAFETY_CONSTRAINTS.md` - Formally traceable safety constraints (SC-XX) enforcing hazard mitigation and invariant boundaries.
5. `05_FMECA_MATRIX.md` - Component Failure Mode, Effects, and Criticality Analysis (FM-XX) with mathematically verified RPN values.
6. `06_REGULATORY_OBJECTIVES_ASSESSMENT.md` - Domain airworthiness and regulatory compliance mapping (for example SORA OSO-01..24, DO-178C, DO-254).
7. `07_RTA_ARCHITECTURE.md` - Run-Time Assurance (RTA) monitors, safety net switching, simplex control architecture, and contingency envelopes.
8. `HAZARD_LOG.md` - Master hazard tracking register maintaining lifecycle tracking, verification evidence, and disposition status.
9. `STPA_MATRIX.md` - The master closed-loop traceability matrix linking Losses, Hazards, UCAs, Loss Scenarios, Safety Constraints, and SysML requirements.

#### 2. The Coordinator-Dispatched Per-Unit Safety Loop

The coordinator never elaborates safety documents itself. It dispatches exactly one fresh, context-isolated subagent per document, never runs two safety subagents concurrently, and advances to the next document only after both gates in the prompt below pass. Every dispatch uses the same normative per-unit elaboration template as Phase 2.1, specialized for safety.

```text
Role: Single-Unit Safety Elaborator -- <UNIT_ID> (one file only).

Step 1: read skills/<ACTIVE_SKILL>/SKILL.md.
Step 2: read the canonical template <TEMPLATE_PATH>.

Target file: <UNIT_FILE>.

Allowed inputs: the target file, .pipeline/schema.sysml,
schema/extracted/oem_bom.md, interface_table.md, parametric_limits.md,
<UNIT_ADDITIONAL_INPUTS>. No other files.

Required content (unit mandatory):
<UNIT_MANDATORY_CONTENT>.

Grounding rules:
- Every numeric value cites schema/extracted/parametric_limits.md or an OEM file:line.
- OEM silence -> "Not stated in OEM sources." Never invent.
- Ruddervator canonical (Fins/tail stabiliser only as parenthetical synonyms).
- ESAD Critical (DAL-A); parachute non-mission variant excluded from baseline.
- No ungrounded protocols (Check 23); no literal OA-/MET- numeric IDs (Check 25).
- KaTeX display math only; no math inside tables; ASCII only; no placeholders.

Gates, in order:
1. ./target/release/verify-baseline . --spec-only --only "<UNIT_FILE>"
2. ./target/release/verify-baseline . --no-domain
Fix until both exit 0. Do not touch other files. No git.

Report: exit codes, what changed, OEM-silent fields.
---GOVERNANCE-END---
PROCEED
```

**Safety input matrix**:

- Every safety document requires `.pipeline/schema.sysml`, the three tables `schema/extracted/oem_bom.md`, `schema/extracted/interface_table.md`, and `schema/extracted/parametric_limits.md`, plus `docs/conops/CONOPS.md`; `<UNIT_ADDITIONAL_INPUTS>` is `docs/conops/CONOPS.md`.
- `<ACTIVE_SKILL>` is `spec-orchestrator`, which defines the Worker 0B STPA Hazard Analysis, FMECA & Domain Safety Assurer procedure.
- `<UNIT_FILE>` is `docs/safety/<UNIT_ID>.md`; `<TEMPLATE_PATH>` is the compiler scaffold emitted by `compile-sysml --stpa-transpile` at that same path.
- `<UNIT_MANDATORY_CONTENT>` is resolved from the 9-file safety catalog above and always includes: purging generic scaffold text ("Loss of safe function of SensorModality", "as_str", "fmt"); analysis across the 4 Universal Failure Dimensions (Timing/Latency, Value/Integrity, Commission/Spurious Actuation, Omission/Loss of Function); the repo's enforced Check 17 10-pillar STPA schema emitted by `--stpa-transpile`; verified `RPN = S x O x D`; and HITL consent before any ESAD arming.

#### 3. Verification Gate (Run Immediately After Each Safety File)

Verify the active safety artifact with the per-file gate:
```zsh
./target/release/verify-baseline . --spec-only --only "docs/safety/01_LOSSES_HAZARDS_TOPOLOGY.md"
```
*Gate: Exit code 0. If any check fails, halt and fix before moving to the next file.*

After the final safety document passes, run the full baseline exactly once:
```zsh
./target/release/verify-baseline . --no-domain
```

---

### Phase 3: Deterministic Master Document Assembly (100% Tooling)

*Objective: Compile the modular, elaborated units into master delivery artifacts.*

1. **Compile Master ConOps & Mission Intent**:
   ```zsh
   ./target/release/assemble-conops --input-dir docs/conops/units/ --output-dir docs/conops/ --verify
   ```
   *Produces `docs/conops/CONOPS.md` and `docs/conops/MISSION_INTENT.md`. Acceptance is structural, not line-count based: every catalog unit is present, every mandatory cardinality is satisfied (seven `EMG-XX` triggers, all 4 PACE tiers, all 9 threat domains), and every numeric value is grounded in `schema/extracted/parametric_limits.md`.*
2. **Audit Zero-Placeholder Invariant**:
   Verify zero unresolved placeholders:
   ```zsh
   grep -rnE "PENDING|PENDING_PARAMETER|TODO|TBD|\{\{.*\}\}" docs/conops/ docs/safety/
   ```
   *Requirement: Exactly 0 matches.*

---

### Phase 4: Downstream Backlog & Contract Projection (100% Tooling)

*Objective: Project the grounded specifications into executable backlog and application contracts.*

1. **Project Agile Backlog**:
   ```zsh
   ./target/release/reconcile-backlog --dry-run
   ```
   *Synchronizes Epics, Features, User Stories, and Use Cases with 100% traceability to SysML requirements.*
2. **Re-Emit Application Contracts**:
   ```zsh
   ./target/release/compile-sysml --schema .pipeline/schema.sysml --emit-flutter-contracts app_flutter/ --force
   ```
3. **Final Semantic Acceptance Baseline**:
   ```zsh
   ./target/release/verify-baseline . --no-domain
   ```
   *Requirement: Exit code `0` across all structural, safety, and traceability gates.*

---

## Tooling-Bug Escalation Path

If any compiler fault, schema inconsistency, or invariant violation is discovered during any phase, do not file a raw issue and do not apply a silent local-only patch. Dispatch a fresh context-isolated subagent with `skills/adversarial-code-auditor/SKILL.md` to produce a verified 7-section defect dossier under `.pipeline/defects/<NAME>.md`, then validate and publish it with:

```zsh
./target/release/verify-baseline check-defect .pipeline/defects/<NAME>.md
```

This atomically validates all checks, persists the dossier, and publishes or updates the upstream issue (add `--dry-run` to validate only). Issue auto-closing keywords and issue close commands are strictly forbidden.

---

## Comparative Matrix: Why This Procedure Works

| Attribute | Uncontrolled Agent Swarm | Raw Tooling Only | Procedural Blueprint (Tool + Serial Agent) |
| :--- | :--- | :--- | :--- |
| **Domain Depth & Prose** | High, but ungrounded | Low (hollow scaffolds) | **High (grounded in SSOT & defense standards)** |
| **Mathematical Precision** | Hallucination-prone | Rigidly constrained | **Verified KaTeX formulas matching SysML** |
| **Operator Visibility** | Zero (invisible changes) | High (CLI stdout) | **Total (CLI stdout + 1 visible diff at a time)** |
| **Tooling Compliance** | Often breaks baseline checks | Passes baseline checks | **100% validated at every step by Rust tooling** |
| **Execution Stability** | High risk of divergence | Stable but incomplete | **Fully deterministic, repeatable, and robust** |

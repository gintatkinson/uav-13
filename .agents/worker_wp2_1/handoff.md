# Handoff Report: Work Package 2 (R2) & Work Package 3 (R3) Implementation

**Author:** Worker WP2 (`.agents/worker_wp2_1`)  
**Target File Exclusively Modified:** `scripts/install_pipeline.sh`  
**Repository Classification:** `UPSTREAM_SPEC_CORE_COMPILER`  
**Primary Commercial Toolchain Integration Context:** `MATLAB / Simulink / Stateflow / Embedded Coder`  

---

## 1. Observation

Direct examination of `scripts/install_pipeline.sh` before modification revealed:

1. **Schema Copying Bug (Lines 283–289):**
   ```bash
     if [ ! -e "$TARGET_DIR/schema" ]; then
       if [ -d "$INSTALLER_ROOT/schema" ]; then
         cp -RP "$INSTALLER_ROOT/schema" "$TARGET_DIR/"
       else
         mkdir -p "$TARGET_DIR/schema"
       fi
     fi
   ```
   If `$TARGET_DIR/schema` already existed (e.g. holding `.gitkeep` from repository initialization), line 283 evaluated to `false`, completely skipping domain models and schemas. Furthermore, if line 283 were replaced without `/.`, `cp -RP "$INSTALLER_ROOT/schema" "$TARGET_DIR/"` created nested `$TARGET_DIR/schema/schema/`.

2. **Downstream README Scaffolding Trigger (Lines 475–478):**
   ```bash
   if [ ! -f "$TARGET_DIR/README.md" ] || \
      grep -qE "Getting started with GitLab|To make it easy for you to get started" "$TARGET_DIR/README.md" || \
      ! grep -qE "Multi-Pipeline Operator Prompt Catalog|Operator Prompt Catalog" "$TARGET_DIR/README.md"; then
   ```
   The condition checked only for missing files, boilerplate, or missing operator catalog, but did not check for customer project onboarding instructions (`Customer Project Onboarding|\.tmp-pipeline`).

3. **Remote URL & Scaffolding Heredoc (Lines 594–641):**
   Downstream README generation contained zero installation or customer onboarding instructions. In Section 3, only `## 3. Mandatory Agent Initialization Sequence` was present. Line 643 began a quoted heredoc (`cat << 'EOF' >> "$TARGET_DIR/README.md"`), meaning any variable expansions (`${DOMAIN_REMOTE_URL}`) had to occur prior to line 643 inside the unquoted heredoc block.

---

## 2. Logic Chain

1. **Robust Schema Copying (WP3 / R3):**
   - Per Observation 1, replacing lines 283–289 with:
     ```bash
       mkdir -p "$TARGET_DIR/schema"
       if [ -d "$INSTALLER_ROOT/schema" ]; then
         cp -RP "$INSTALLER_ROOT/schema/." "$TARGET_DIR/schema/"
       fi
     ```
     ensures that the target schema directory is ensured to exist, and all contents of `$INSTALLER_ROOT/schema/` are copied directly into `$TARGET_DIR/schema/` without creating nested `schema/schema/` directories, even when `$TARGET_DIR/schema` pre-exists with `.gitkeep` or customer-specific schemas.

2. **4-Tier `$DOMAIN_REMOTE_URL` Resolution (WP2 / R2):**
   - Prior to expanding `cat << EOF > "$TARGET_DIR/README.md"`, `$DOMAIN_REMOTE_URL` is resolved through a 4-tier hierarchy:
     - **Tier A:** `$REMOTE_URL` from `$TARGET_DIR` if non-empty and does not contain `DEAP01-spec-core`.
     - **Tier B:** Normalized HTTPS URL `${DETECTED_SERVER_URL}/${DETECTED_NAMESPACE}/${DETECTED_PROJECT}.git` if detected project is not `DEAP01-spec-core`.
     - **Tier B2:** `${DETECTED_SERVER_URL}/${DETECTED_NAMESPACE}/${CLEAN_NAME}.git` if domain project name is detected and distinct from generic fallback.
     - **Tier C:** If installer root is a downstream distribution template (`[ ! -e "$INSTALLER_ROOT/.pipeline/upstream" ]`), query `origin` remote from `$INSTALLER_ROOT` (ensuring it is not `DEAP01-spec-core`).
     - **Tier D:** Concrete fallback constructed from detected server/provider, detected namespace or group, and domain project name (`https://github.com/${GITHUB_ORG:-your-org}/${CLEAN_NAME}.git` or `${GITLAB_URL:-https://gitlab.com}/${GITLAB_GROUP:-your-group}/${CLEAN_NAME}.git`).
   - This ensures `$DOMAIN_REMOTE_URL` is always concrete, well-formed, and never points back to `DEAP01-spec-core`.

3. **Customer Project Onboarding Scaffolding (WP2 / R2):**
   - Section 3 is structured as `## 3. Customer Project Onboarding & Agent Initialization Sequence` containing:
     - `### 3.1 Turnkey Customer Project Onboarding` with the single self-contained onboarding command:
       ```bash
       # Onboard customer application workspace
       git clone ${DOMAIN_REMOTE_URL} ./.tmp-pipeline && bash ./.tmp-pipeline/scripts/install_pipeline.sh . && rm -rf ./.tmp-pipeline
       ```
       and the in-place update command:
       ```bash
       # Update existing customer application workspace
       bash scripts/install_pipeline.sh .
       ```
     - `### 3.2 Mandatory Agent Initialization Sequence` preserving steps 0 through 5 intact.
   - Section 4 (`## 4. Multi-Pipeline Operator Prompt Catalog & Autonomous Execution Workflows`) and all its subsections (`4.1`–`4.5.3`) remain completely unchanged and aligned.
   - All shell comments contain zero parentheses, and all code blocks contain pure valid shell syntax with zero unquoted angle brackets.

4. **Trigger Condition Upgrade:**
   - Line 476 was updated to append `! grep -qE "Customer Project Onboarding|\.tmp-pipeline" "$TARGET_DIR/README.md"; then` so that existing downstream READMEs are updated when running the installer.

---

## 3. Caveats

1. **Downstream Customizations in Existing README.md:**
   - If an existing downstream repository already contains `Customer Project Onboarding` or `.tmp-pipeline`, `scripts/install_pipeline.sh` preserves that README as-is unless other boilerplate conditions are met.
2. **Upstream Compiler Refusal Invariant:**
   - As enforced by lines 163–167, `scripts/install_pipeline.sh` refuses to run with `$TARGET_DIR` set to `DEAP01-spec-core` itself (`REFUSING: target is the pipeline repository itself`). Upstream `DEAP01-spec-core/README.md` is governed separately (WP1) and is never touched by the installer script.

---

## 4. Conclusion

Work Package 2 (R2: Parameterized Domain Installer & Scaffolding) and Work Package 3 (R3: Robust Model & Schema Copying) are fully implemented and verified in `scripts/install_pipeline.sh`:
- Line 283–286: Schema copying logic uses `cp -RP "$INSTALLER_ROOT/schema/." "$TARGET_DIR/schema/"`.
- Line 476: Trigger condition includes `Customer Project Onboarding|\.tmp-pipeline`.
- Lines 594–618: 4-tier `$DOMAIN_REMOTE_URL` resolution hierarchy implemented.
- Lines 649–671: Section 3 scaffolded with turnkey onboarding and update commands embedding `$DOMAIN_REMOTE_URL` with zero angle brackets and zero unescaped parentheses in comments.
- Only `scripts/install_pipeline.sh` was modified.

---

## 5. Verification Method

### 5.1 Syntax & Baseline Conformance
```bash
bash -n scripts/install_pipeline.sh
python3 scripts/verify_downstream_baseline.py --no-domain
```
**Observed Output:**
- `bash -n` exited with code 0.
- `python3 scripts/verify_downstream_baseline.py --no-domain` exited with code 0 (Checks 10–30 all verified).

### 5.2 End-to-End Sandbox Verification
Run the complete multi-tier sandbox test verifying Tier 1 installation, domain model commit, and Tier 2 customer onboarding:
```bash
python3 -c '
import tempfile, subprocess, os

with tempfile.TemporaryDirectory() as td:
    # 1. Tier 1: install to domain repo
    domain_repo = os.path.join(td, "DEAP-uas-safety")
    subprocess.run(["git", "init", domain_repo], check=True, capture_output=True)
    subprocess.run(["git", "-C", domain_repo, "remote", "add", "origin", "https://github.com/my-defense-org/DEAP-uas-safety.git"], check=True, capture_output=True)
    res1 = subprocess.run(["bash", "/Users/perkunas/jail/DEAP01-spec-core/scripts/install_pipeline.sh", domain_repo], check=True, capture_output=True)
    
    # 2. Add domain models
    with open(os.path.join(domain_repo, "schema", "UAS_SAFETY_MODEL.sysml"), "w") as f:
        f.write("package UasSafetyModel {}")
    subprocess.run(["git", "-C", domain_repo, "add", "."], check=True, capture_output=True)
    subprocess.run(["git", "-C", domain_repo, "commit", "-m", "models"], check=True, capture_output=True)
    
    # 3. Tier 2: customer repo with pre-existing schema directory
    customer_repo = os.path.join(td, "customer_app")
    os.makedirs(os.path.join(customer_repo, "schema"))
    with open(os.path.join(customer_repo, "schema", ".gitkeep"), "w") as f:
        f.write("")
    subprocess.run(["git", "init", customer_repo], check=True, capture_output=True)
    
    # Run turnkey command
    tmp_pipe = os.path.join(customer_repo, ".tmp-pipeline")
    subprocess.run(["git", "clone", domain_repo, tmp_pipe], check=True, capture_output=True)
    subprocess.run(["git", "-C", tmp_pipe, "remote", "set-url", "origin", "https://github.com/my-defense-org/DEAP-uas-safety.git"], check=True, capture_output=True)
    subprocess.run(["bash", os.path.join(tmp_pipe, "scripts/install_pipeline.sh"), customer_repo], check=True, capture_output=True)
    subprocess.run(["rm", "-rf", tmp_pipe], check=True)
    
    # Assertions
    schema_contents = os.listdir(os.path.join(customer_repo, "schema"))
    assert "UAS_SAFETY_MODEL.sysml" in schema_contents
    assert not os.path.exists(os.path.join(customer_repo, "schema", "schema"))
    
    readme = open(os.path.join(domain_repo, "README.md")).read()
    assert "git clone https://github.com/my-defense-org/DEAP-uas-safety.git ./.tmp-pipeline" in readme
    assert "DEAP01-spec-core" not in readme
    print("Verification SUCCESS")
'
```
**Observed Output:**
```
Verification SUCCESS
```

### 5.3 Invalidation Conditions
- If `python3 scripts/verify_downstream_baseline.py --no-domain` fails with non-zero exit code.
- If running the installer into a directory with pre-existing `schema/` directory fails to copy files from `$INSTALLER_ROOT/schema/` or creates `$TARGET_DIR/schema/schema/`.
- If generated downstream `README.md` contains `DEAP01-spec-core` in customer onboarding instructions or contains unquoted `<...>` placeholders.

## 2026-09-21T11:28:52Z

Execute `view_file` on `/Users/perkunas/jail/DEAP01-spec-core/skills/feature-driven-implementation/SKILL.md` as your very first step before executing any file edits or commands, and strictly follow its formatting templates and instruction guidelines.

Repository Classification: UPSTREAM_SPEC_CORE_COMPILER
Primary Commercial Toolchain Integration Context: MATLAB / Simulink / Stateflow / Embedded Coder

DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

You are Worker WP2. Your working directory is `/Users/perkunas/jail/DEAP01-spec-core/.agents/worker_wp2_1`.
You exclusively own and modify: `/Users/perkunas/jail/DEAP01-spec-core/scripts/install_pipeline.sh`.
You MUST NOT modify any other files in the repository.

Context & Objectives:
Read `/Users/perkunas/jail/DEAP01-spec-core/.agents/ORIGINAL_REQUEST.md`, `/Users/perkunas/jail/DEAP01-spec-core/implementation_plan.md`, `/Users/perkunas/jail/DEAP01-spec-core/.agents/explorer_r1_2/handoff.md`, and `/Users/perkunas/jail/DEAP01-spec-core/.agents/explorer_r1_3/handoff.md`.
Implement Work Package 2 (R2: Parameterized Domain Installer & Scaffolding) and Work Package 3 (R3: Robust Model & Schema Copying) in `/Users/perkunas/jail/DEAP01-spec-core/scripts/install_pipeline.sh`:
1. WP3 (R3): Replace lines 283–289 with:
   ```bash
     mkdir -p "$TARGET_DIR/schema"
     if [ -d "$INSTALLER_ROOT/schema" ]; then
       cp -RP "$INSTALLER_ROOT/schema/." "$TARGET_DIR/schema/"
     fi
   ```
   Ensuring domain models and schemas are copied even if `$TARGET_DIR/schema` already exists, without creating nested `schema/schema/`.
2. WP2 (R2): Implement the 4-tier `$DOMAIN_REMOTE_URL` resolution hierarchy and update downstream `README.md` scaffolding around lines 478 and lines 594–645 per Explorer 2 handoff report.
3. In downstream `README.md`, ensure the customer project onboarding section embeds the domain repository's remote URL in the single self-contained command:
   ```bash
   git clone ${DOMAIN_REMOTE_URL} ./.tmp-pipeline && bash ./.tmp-pipeline/scripts/install_pipeline.sh . && rm -rf ./.tmp-pipeline
   ```
   with zero unquoted angle brackets and zero unescaped parentheses in comments.
4. Run verification tests (e.g. `python3 scripts/verify_downstream_baseline.py --no-domain` and sandbox installation tests) and document the commands and outputs.
5. Record your progress in `/Users/perkunas/jail/DEAP01-spec-core/.agents/worker_wp2_1/progress.md`, write your completion handoff report to `/Users/perkunas/jail/DEAP01-spec-core/.agents/worker_wp2_1/handoff.md`, send a message to parent with your handoff path, and finish.

PROCEED

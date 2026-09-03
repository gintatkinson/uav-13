#!/usr/bin/env python3
"""
ConOps & Mission Intent Completeness Validator CLI Wrapper (Gate 26).
"""
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
parity_src = os.path.join(repo_root, "skills", "spec-orchestrator", "parity_auditor", "src")
if parity_src not in sys.path:
    sys.path.insert(0, parity_src)

from parity_auditor.core.workspace import WorkspaceRepository
from parity_auditor.validators.conops_completeness_validator import (
    ConopsCompletenessValidator,
    MissionIntentCompletenessValidator,
)


def main():
    target_dir = sys.argv[1] if len(sys.argv) > 1 else repo_root
    repo = WorkspaceRepository(workspace_dir=target_dir)
    v1 = ConopsCompletenessValidator()
    v2 = MissionIntentCompletenessValidator()
    errs1 = v1.validate(repo)
    errs2 = v2.validate(repo)
    all_errs = errs1 + errs2
    if all_errs:
        for err in all_errs:
            print(f"[{getattr(err, 'rule_id', 'ERROR')}] {err}")
        sys.exit(1)
    else:
        print("[OK] Gate 26 (ConOps & Mission Intent Completeness): All checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()

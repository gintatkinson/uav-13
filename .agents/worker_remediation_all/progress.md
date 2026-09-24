# Progress - worker_remediation_all

Last visited: 2026-09-25T00:26:00Z

## Status
Starting investigation and execution of remediation tasks.

## Checklist
- [ ] 1. Inspect `scripts/install_pipeline.sh` lines 500-800
- [ ] 2. Inspect `tests/test_readme_scaffolding.py`
- [ ] 3. Implement changes in `scripts/install_pipeline.sh`:
  - [ ] a) In-place README upgrade detection for DOMAIN_DISTRIBUTION_TEMPLATE and DOWNSTREAM_CUSTOMER_PROJECT
  - [ ] b) Domain README generator Section 2, Section 4.5.1, Section 4.5.2
  - [ ] c) Customer README generator title deduplication
- [ ] 4. Update / add unit tests in `tests/test_readme_scaffolding.py`
- [ ] 5. Run test suites in `DEAP01-spec-core`:
  - [ ] `python3 -m unittest tests/test_readme_scaffolding.py`
  - [ ] `python3 scripts/verify_downstream_baseline.py --no-domain`
- [ ] 6. Commit and push in `DEAP01-spec-core`
- [ ] 7. Re-propagate to `DEAP-uas-infrastructure-safety` in scratch dir, verify, commit, push, cleanup
- [ ] 8. Re-propagate to `uav-011`, verify, commit, push
- [ ] 9. Write handoff report and notify parent

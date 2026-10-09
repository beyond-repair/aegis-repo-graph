# Claim Status — aegis-repo-graph

**Tool claim:** ≤1 (deterministic validator of a dated catalog).
**Lifecycle:** RESEARCH — not a live GitHub crawler and not a production AEGIS host-integrity product.
**Catalog row:** `repo:aegis-repo-graph` still stores integer `claim: 3` from the 2026-09-04 lock. That integer is snapshot data. It does not raise this tool's claim.
**Snapshot:** 2026-09-04 — 72 repository artifacts + 1 queue artifact (`artifacts=73`) and 21 relationships. Not a live completeness proof of any later search count.
**Version:** 0.1.3

## Allowed claims

- The in-repo catalog can be validated for identity keys, allowed kinds, allowed clusters and lifecycles, referential integrity, integer claim 0–5, ARCHIVED/SUPERSEDED claim caps, and non-empty function lists (`graph.engine.validate` / `python -m graph`).
- Tests in `tests/test_graph.py` encode that contract.
- `graph.drift.name_drift` reports name-set drift against a frozen 2026-10-06 search of 83 names. It does not add or delete catalog rows.

## Forbidden / uncapped claims

- Live completeness of any later GitHub search set (the catalog is a 2026-09-04 snapshot).
- FLS production conformance of every beyond-repair repository, or an FLS compiler.
- Host integrity, firmware measurement, or Watchman/Restoration pillars (those were sketched in forge-aegis / AEGIS-Project-Nehemiah-; this repo does not copy them).
- SUPERSEDES of ADL-Portfolio-Census or forge-aegis.
- Census compatible-build status `built`. ADL-Portfolio-Census still locks this name as `not_built`. Existence and a green validator are not that contract.

## Evidence precedence

1. Deterministic `python -m graph.engine` and `python -m pytest -q` on a clean clone of the merged default branch.
2. The locked catalog in `graph/catalog.py` (rows not rewritten by Sweep-239).
3. Pre-change head evidence: CI run 37402540834 completed success on `98bac63122d060a51a21f023bcf3328a82eb6cc2`. That run is not evidence for 0.1.3.
4. Historical CI run 37069800025 succeeded on `96ca55789c3e8656d9b4052392d9000c69bc4c17`. It is not evidence for `98bac631` or for 0.1.3.
5. Sweep-239 local pytest: 11 passed after the drift witness. Commits `50e85433`, `3bb7c49c`, `d9a2e29e` are the implementation sequence. New CI on the final docs commit is pending at this write.

## Notes

- Sweep-125 classified the repo RESEARCH and did not mutate the catalog.
- v0.1.1 makes the package installable and rejects bool claims, bare-string function fields, and unknown cluster/lifecycle values. Catalog rows are unchanged.
- Sweep-228 records older head CI only.
- Sweep-239 records the 83-name search as a frozen observation and a non-mutating drift report. Claim remains ≤1. Catalog claim integer 3 is still snapshot data. No tag. No archive. Census `not_built` freeze unchanged.
- Observation-only names (18) and catalog-only names (7) are listed by `name_drift`. Expanding the lock is operator-only.

- Sweep-292 records a second frozen search (2026-10-09, total_count 83, incomplete_results false, 83 items). `observation_reconfirm` reports the name set equal to the 2026-10-06 freeze. Claim remains ≤1. Catalog rows unchanged. Catalog claim integer 3 remains snapshot data. Census `not_built` freeze unchanged. No tag. No archive. Actions are pinned to commit SHAs. A later green CI run is an Actions conclusion only.

- Sweep-292 CI: run 37934144237 conclusion success on b8a5c7f431ad8624503c92a47efad57af056a581. Actions conclusion only. Not evidence for catalog expansion, FLS conformance, or census built status.

# Claim Status — aegis-repo-graph

**Tool claim:** ≤1 (deterministic validator of a dated catalog).
**Lifecycle:** RESEARCH — not a live GitHub crawler and not a production AEGIS host-integrity product.
**Catalog row:** `repo:aegis-repo-graph` still stores integer `claim: 3` from the 2026-09-04 lock. That integer is snapshot data. It does not raise this tool's claim.
**Snapshot:** 2026-09-04 — 72 repository artifacts + 1 queue artifact (`artifacts=73`) and 21 relationships. Not a live completeness proof of any later search count.
**Version:** 0.1.1

## Allowed claims

- The in-repo catalog can be validated for identity keys, allowed kinds, allowed clusters and lifecycles, referential integrity, integer claim 0–5, ARCHIVED/SUPERSEDED claim caps, and non-empty function lists (`graph.engine.validate` / `python -m graph`).
- Tests in `tests/test_graph.py` encode that contract.

## Forbidden / uncapped claims

- Live completeness of any later GitHub search set (the catalog is a 2026-09-04 snapshot).
- FLS production conformance of every beyond-repair repository, or an FLS compiler.
- Host integrity, firmware measurement, or Watchman/Restoration pillars (those were sketched in forge-aegis / AEGIS-Project-Nehemiah-; this repo does not copy them).
- SUPERSEDES of ADL-Portfolio-Census or forge-aegis.
- Census compatible-build status `built`. ADL-Portfolio-Census still locks this name as `not_built`. Existence and a green validator are not that contract.

## Evidence precedence

1. Deterministic `python -m graph.engine` and `python -m pytest -q` on a clean clone of the merged default branch.
2. The locked catalog in `graph/catalog.py` (rows not rewritten by the installability repair).
3. Current head evidence: CI run 37069800025 completed success on `96ca55789c3e8656d9b4052392d9000c69bc4c17`. Job `test` 111046279932 success (`python -m graph.engine`, `python -m pytest -q`). Local re-run on that SHA: engine printed `artifacts=73 relationships=21` and `OK`; pytest 10 passed.
4. Historical CI run 34072230795 succeeded on older head `1a5a2fde`. That run is not evidence for `96ca557`.

## Notes

- Sweep-125 classified the repo RESEARCH and did not mutate the catalog.
- v0.1.1 makes the package installable (`pip install -e ".[dev]"`), aligns the README claim line with the ≤1 badge, and rejects bool claims, bare-string function fields, and unknown cluster/lifecycle values. Catalog rows are unchanged.
- Sweep-228 records head CI only. No catalog edit. No version bump. No tag. No archive.

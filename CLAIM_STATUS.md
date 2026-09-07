# Claim Status — aegis-repo-graph

**Claim level:** 3 (structured inventory / graph validity of a *locked snapshot*).
**Lifecycle (this sweep):** RESEARCH — deterministic validator of a dated catalog, not a live GitHub crawler and not a production AEGIS host-integrity product.
**Snapshot date recorded in README:** 2026-09-04.
**Head at discover:** `e1dc3940332e047133098401dbce7bcad00d962f`

## Allowed claims

- The in-repo catalog can be validated for identity uniqueness, allowed kinds, referential integrity, and ARCHIVED/SUPERSEDED claim caps (`graph.engine.validate`).
- CI workflow `.github/workflows/ci.yml` exists and last completed product run **33928255440** concluded **success** on that head.
- Tests in `tests/test_graph.py` encode the contract above.

## Forbidden / uncapped claims

- Live completeness of the 75-item GitHub search set (catalog is a snapshot).
- FLS production conformance of every beyond-repair repository.
- Host integrity, firmware measurement, or Watchman/Restoration pillars (those live in forge-aegis / AEGIS-Project-Nehemiah-).
- SUPERSEDES of ADL-Portfolio-Census or forge-aegis.

## Evidence precedence

1. Deterministic `python -m graph.engine` + pytest (CI run 33928255440).
2. Tree listing at `e1dc394`.
3. Repository security advisories: empty list observed 2026-09-07.
4. Releases/tags: none observed (operator).

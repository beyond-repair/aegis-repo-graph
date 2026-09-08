# Claim Status — aegis-repo-graph

**Claim level:** 3 (structured inventory / graph validity of a *locked snapshot*).
**Lifecycle (this sweep):** RESEARCH — deterministic validator of a dated catalog, not a live GitHub crawler and not a production AEGIS host-integrity product.
**Snapshot date recorded in README:** 2026-09-04 (catalog locked; live census now 75).
**Head at Sweep-125:** `1a5a2fde5eb95f664beb41cd82ec48ce0e5e1005`

## Allowed claims

- The in-repo catalog can be validated for identity uniqueness, allowed kinds, referential integrity, and ARCHIVED/SUPERSEDED claim caps (`graph.engine.validate`).
- CI workflow `.github/workflows/ci.yml` exists and last completed product run **34072230795** concluded **success** on head `1a5a2fde`.
- Tests in `tests/test_graph.py` encode the contract above (5 tests).

## Forbidden / uncapped claims

- Live completeness of the 75-item GitHub search set (catalog is a 2026-09-04 snapshot).
- FLS production conformance of every beyond-repair repository.
- Host integrity, firmware measurement, or Watchman/Restoration pillars (those live in forge-aegis / AEGIS-Project-Nehemiah-).
- SUPERSEDES of ADL-Portfolio-Census or forge-aegis.

## Evidence precedence

1. Deterministic `python -m graph.engine` + pytest (CI run 34072230795).
2. Tree listing at `1a5a2fde`.
3. Repository security advisories: empty list observed prior cycles.
4. Releases/tags: none observed (operator).

## Sweep-125 notes

- Classification aligned to ADL-Governance PORTFOLIO_STATUS_REPORT (RESEARCH).
- Catalog internal lifecycle for self remains claim-capped; no expansion of allowed claims.
- No code mutation; docs only.

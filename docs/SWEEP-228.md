# Sweep-228 — 2026-10-05

Subject: `aegis-repo-graph`.
Classification: **RESEARCH**. Tool claim remains ≤1.
Head at observation: `96ca55789c3e8656d9b4052392d9000c69bc4c17`.

## Discover

- ADL-Portfolio-Census `COMPATIBLE_BUILDS` still marks this name `not_built`. That freeze was locked in Sweep-227 and is not rewritten here.
- This repository exists and validates a 2026-09-04 catalog (`artifacts=73`, `relationships=21`).
- `CLAIM_STATUS.md` previously cited only CI run 34072230795 on `1a5a2fde` as non-evidence for later commits.

## Verified

- Actions run 37069800025 success on `96ca557`. Job 111046279932 success.
- Local clone of that SHA: `python -m graph.engine` OK; `pytest -q` 10 passed.

## Not done

- Catalog rows unchanged.
- Census status unchanged.
- No tag. No archive. No claim elevation.

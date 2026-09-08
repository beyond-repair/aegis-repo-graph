# aegis-repo-graph

Claim level **3**. Deterministic Artifact Graph of the beyond-repair portfolio.

This repository exists because [forge-aegis](https://github.com/beyond-repair/forge-aegis)
models host/policy artifacts, and [ADL-Portfolio-Census](https://github.com/beyond-repair/ADL-Portfolio-Census)
locks a tabular inventory, but **repositories themselves were not yet FLS artifacts**.

## Contract

- Every repository is an Artifact with a stable Identity (`repo:<name>`).
- Cluster and lifecycle are Properties, not Relationships.
- Typed Relationships: `GOVERNED_BY`, `SUPERSEDES`, `COMPATIBLE_WITH`, `IMPLEMENTS`.
- Validity = unique identities + referential integrity + claim caps on ARCHIVED/SUPERSEDED.

Not a live GitHub crawler. Snapshot dated 2026-09-04 (live census 75 as of 2026-09-08).
See [CLAIM_STATUS.md](CLAIM_STATUS.md).

```bash
pip install -r requirements.txt
python -m graph.engine
python -m pytest -q
```

## Sweep-125

Classification: **RESEARCH**. Last product CI: run 34072230795 success on `1a5a2fde`.
No code mutation this cycle (docs + claim alignment only).

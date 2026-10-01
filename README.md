<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy
```

</div>

---

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

Not a live GitHub crawler. Snapshot dated 2026-09-04 (live census 81 as of 2026-09-08).
See [CLAIM_STATUS.md](CLAIM_STATUS.md).

```bash
pip install -r requirements.txt
python -m graph.engine
python -m pytest -q
```

## Sweep-125

Classification: **RESEARCH**. Last product CI: run 34072230795 success on `1a5a2fde`.
No code mutation this cycle (docs + claim alignment only).


---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>

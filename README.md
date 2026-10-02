<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy · live crawl · FLS compiler · Nehemiah host
```

</div>

---

# aegis-repo-graph

Claim level **≤1**. Deterministic Artifact Graph of a locked beyond-repair snapshot.

This repository exists because [forge-aegis](https://github.com/beyond-repair/forge-aegis)
models host/policy artifacts, and [ADL-Portfolio-Census](https://github.com/beyond-repair/ADL-Portfolio-Census)
locks a tabular inventory, but **repositories themselves were not yet FLS artifacts**.

The banner and this line agree. A green run does not raise the claim. The catalog row `repo:aegis-repo-graph` still stores the locked integer `claim: 3`. That integer is snapshot data. It is not a license to claim live FLS conformance, a compiler, or a Nehemiah host.

## Contract

- Every repository is an Artifact with a stable Identity (`repo:<name>`).
- Cluster and lifecycle are Properties, not Relationships.
- Typed Relationships: `GOVERNED_BY`, `SUPERSEDES`, `COMPATIBLE_WITH`, `IMPLEMENTS`, `CLUSTER_PEER`.
- Validity = unique identities + referential integrity + claim caps on ARCHIVED/SUPERSEDED + allowed cluster/lifecycle + a non-empty function list (a bare string does not count) + integer claim 0–5 (`True`/`False` do not count).

Not a live GitHub crawler. Not an FLS compiler. Not a copy of forge-aegis and not a Nehemiah host. The catalog is the locked 2026-09-04 snapshot: **72** repository artifacts, **1** queue artifact, **21** relationships (`artifacts=73`). It does not prove a later 81-row portfolio search is complete.
See [CLAIM_STATUS.md](CLAIM_STATUS.md).

Nothing to configure. The checker does not read the network, the environment, or a token.

## Quick start

Python 3.11 or newer. From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
python -m graph.engine
python -m graph
python -m pytest -q
```

Both commands print `artifacts=73 relationships=21` and `OK`, and both exit 0, when the locked graph passes. They exit 1 and list `ERRORS` when a graph breaks the contract. `python -m graph` is the same report as `python -m graph.engine`. After the editable install, those commands work from any working directory.

`requirements.txt` pins the same pytest for a root-directory run without installing the package. That path only works when the current directory is the repository root, because Python then imports the local `graph` package:

```bash
python -m pip install -r requirements.txt
python -m graph.engine
python -m pytest -q
```

## Sweep-125

Classification: **RESEARCH**. The catalog was not expanded in that sweep. This repair does not expand it either.

---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>

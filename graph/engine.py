"""Validity checker per FLS-003: identity uniqueness + referential integrity + claim caps."""

from __future__ import annotations

from dataclasses import dataclass

from .catalog import build_graph
from .model import ALLOWED_KINDS, ALLOWED_REL_KINDS, ArtifactGraph


@dataclass(frozen=True)
class GraphReport:
    artifact_count: int
    relationship_count: int
    errors: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.errors


def validate(graph: ArtifactGraph | None = None) -> GraphReport:
    g = build_graph() if graph is None else graph
    errors: list[str] = []

    for ident, art in g.artifacts.items():
        if ident != art.identity:
            errors.append(f"key/identity mismatch: {ident} vs {art.identity}")
        if art.kind not in ALLOWED_KINDS:
            errors.append(f"{ident}: unknown kind {art.kind}")
        if art.kind == "RepositoryArtifact":
            claim = art.properties.get("claim", -1)
            life = art.properties.get("lifecycle")
            if not isinstance(claim, int) or claim < 0 or claim > 5:
                errors.append(f"{ident}: claim must be 0-5")
            if life in {"ARCHIVED", "SUPERSEDED"} and isinstance(claim, int) and claim > 1:
                errors.append(f"{ident}: archived/superseded claim must be ≤1")
            if not art.properties.get("functions"):
                errors.append(f"{ident}: functions required")

    ids = g.identities()
    for rel in g.relationships:
        if rel.kind not in ALLOWED_REL_KINDS:
            errors.append(f"unknown relationship kind {rel.kind}")
        if rel.source not in ids:
            errors.append(f"dangling source {rel.source} ({rel.kind})")
        if rel.target not in ids:
            errors.append(f"dangling target {rel.target} ({rel.kind})")

    return GraphReport(
        artifact_count=len(g.artifacts),
        relationship_count=len(g.relationships),
        errors=tuple(errors),
    )


def main() -> int:
    report = validate()
    print(f"artifacts={report.artifact_count} relationships={report.relationship_count}")
    if report.errors:
        print("ERRORS:")
        for e in report.errors:
            print(" -", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

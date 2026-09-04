"""Minimal FLS-002 / FLS-003 types. No new ontology primitives."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


ALLOWED_KINDS = frozenset({"RepositoryArtifact", "GovernanceArtifact", "QueueArtifact"})
ALLOWED_REL_KINDS = frozenset(
    {"GOVERNED_BY", "SUPERSEDES", "COMPATIBLE_WITH", "IMPLEMENTS", "CLUSTER_PEER"}
)


@dataclass(frozen=True)
class Artifact:
    identity: str
    kind: str
    properties: dict[str, Any] = field(default_factory=dict)
    revision: str = "r1"


@dataclass(frozen=True)
class Relationship:
    kind: str
    source: str
    target: str


@dataclass
class ArtifactGraph:
    artifacts: dict[str, Artifact]
    relationships: list[Relationship]

    def identities(self) -> set[str]:
        return set(self.artifacts)

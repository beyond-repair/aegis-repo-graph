from graph.catalog import build_graph
from graph.engine import validate
from graph.model import Artifact, ArtifactGraph, Relationship


def test_locked_graph_is_valid():
    report = validate()
    assert report.ok, report.errors
    assert report.artifact_count >= 70
    assert report.relationship_count >= 15


def test_identities_unique():
    g = build_graph()
    assert len(g.artifacts) == len({a.identity for a in g.artifacts.values()})


def test_governance_anchor_present():
    g = build_graph()
    assert "repo:ADL-Governance" in g.artifacts
    assert "repo:aegis-repo-graph" in g.artifacts
    gov = [r for r in g.relationships if r.kind == "GOVERNED_BY"]
    assert any(r.target == "repo:ADL-Governance" for r in gov)


def test_dangling_relationship_fails():
    g = build_graph()
    broken = ArtifactGraph(
        artifacts=g.artifacts,
        relationships=g.relationships + [Relationship("COMPATIBLE_WITH", "repo:sunder", "repo:does-not-exist")],
    )
    report = validate(broken)
    assert not report.ok
    assert any("dangling target" in e for e in report.errors)


def test_claim_cap_on_archived():
    bad = ArtifactGraph(
        artifacts={
            "repo:x": Artifact(
                identity="repo:x",
                kind="RepositoryArtifact",
                properties={"name": "x", "cluster": "legacy", "lifecycle": "ARCHIVED", "claim": 4, "functions": ("f",)},
            )
        },
        relationships=[],
    )
    report = validate(bad)
    assert not report.ok

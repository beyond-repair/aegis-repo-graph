import subprocess
import sys
from pathlib import Path

from graph import __version__
from graph.catalog import build_graph
from graph.engine import validate
from graph.model import Artifact, ArtifactGraph, Relationship

ROOT = Path(__file__).resolve().parents[1]
LOCKED_ARTIFACTS = 73
LOCKED_RELATIONSHIPS = 21


def test_locked_graph_is_valid():
    report = validate()
    assert report.ok, report.errors
    assert report.artifact_count == LOCKED_ARTIFACTS
    assert report.relationship_count == LOCKED_RELATIONSHIPS


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
    assert any("archived/superseded claim must be" in e for e in report.errors)


def test_bool_claim_is_rejected():
    bad = ArtifactGraph(
        artifacts={
            "repo:x": Artifact(
                identity="repo:x",
                kind="RepositoryArtifact",
                properties={"name": "x", "cluster": "legacy", "lifecycle": "ACTIVE", "claim": True, "functions": ("f",)},
            )
        },
        relationships=[],
    )
    report = validate(bad)
    assert not report.ok
    assert any("claim must be 0-5" in e for e in report.errors)


def test_string_functions_are_rejected():
    bad = ArtifactGraph(
        artifacts={
            "repo:x": Artifact(
                identity="repo:x",
                kind="RepositoryArtifact",
                properties={"name": "x", "cluster": "legacy", "lifecycle": "ACTIVE", "claim": 1, "functions": "not-a-list"},
            )
        },
        relationships=[],
    )
    report = validate(bad)
    assert not report.ok
    assert any("functions required" in e for e in report.errors)


def test_unknown_lifecycle_and_cluster_are_rejected():
    bad = ArtifactGraph(
        artifacts={
            "repo:x": Artifact(
                identity="repo:x",
                kind="RepositoryArtifact",
                properties={"name": "x", "cluster": "not-a-cluster", "lifecycle": "SHIPPED", "claim": 1, "functions": ("f",)},
            )
        },
        relationships=[],
    )
    report = validate(bad)
    assert not report.ok
    assert any("unknown lifecycle" in e for e in report.errors)
    assert any("unknown cluster" in e for e in report.errors)


def test_public_version():
    assert __version__ == "0.1.2"


def test_module_entrypoint_matches_engine():
    proc = subprocess.run(
        [sys.executable, "-m", "graph"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert f"artifacts={LOCKED_ARTIFACTS} relationships={LOCKED_RELATIONSHIPS}" in proc.stdout
    assert "OK" in proc.stdout
    assert proc.stderr == ""


def test_observed_drift_does_not_mutate_lock():
    from graph.drift import name_drift

    before = validate()
    drift = name_drift()
    after = validate()
    assert before.ok and after.ok
    assert after.artifact_count == LOCKED_ARTIFACTS
    assert after.relationship_count == LOCKED_RELATIONSHIPS
    assert drift["catalog_repository_count"] == 72
    assert drift["observed_count"] == 83
    assert drift["observed_only"] == (
        "ADL-Nexus",
        "CFTv3.3-IQG-Unified-Framework",
        "Open-Energy-Fusion",
        "RealityOS",
        "Sovereign-Epistemic-Reality-Engine",
        "adl-capability-matrix",
        "adl-function-census",
        "atomicdreamlabs",
        "bloch-coherence-factor2",
        "finite-gasket-spectral-derivatives",
        "informational-flux-identity",
        "mend",
        "mendthegame",
        "os-family-constitution-map",
        "scale-functional-I",
        "seem-identity-unifier",
        "seem-sunder-bridge",
        "sunder-cleanroom-vsa-adapter",
    )
    assert drift["catalog_only"] == (
        "CFT-v3.3-IQG-Unified-Framework",
        "MyCore",
        "SuperAGI",
        "bolt.new",
        "clean-room-skill-export",
        "docs",
        "sunder-aegis-bridge",
    )

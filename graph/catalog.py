"""Locked 2026-09-04 snapshot of beyond-repair repositories as Artifacts."""

from __future__ import annotations

from .model import Artifact, ArtifactGraph, Relationship


def _repo(name: str, cluster: str, lifecycle: str, claim: int, functions: list[str]) -> Artifact:
    return Artifact(
        identity=f"repo:{name}",
        kind="RepositoryArtifact",
        properties={
            "name": name,
            "cluster": cluster,
            "lifecycle": lifecycle,
            "claim": claim,
            "functions": tuple(functions),
        },
    )


def build_graph() -> ArtifactGraph:
    artifacts: dict[str, Artifact] = {}

    rows = [
        ("ADL-Governance", "governance", "ACTIVE", 4, ["constitution", "lifecycle", "claim 0-5"]),
        ("ADL-SEEM", "governance", "ACTIVE", 4, ["SEEM v3.0 contract"]),
        ("ADL-Portfolio-Census", "governance", "ACTIVE", 3, ["locked inventory", "claim-cap validator"]),
        ("aegis-repo-graph", "integrity", "ACTIVE", 3, ["repo Artifact Graph", "referential integrity"]),
        ("forge-aegis", "integrity", "ACTIVE", 3, ["FLS ontology", "result_hash pipeline"]),
        ("sovereign-clean-room", "cognitive-substrate", "ACTIVE", 3, ["FHRR VSA", "skill gates"]),
        ("sunder", "agent-runtime", "EXPERIMENTAL", 1, ["local coding agent", "VSA memory"]),
        ("Sovereign-OS", "governance", "RESEARCH", 1, ["constitutional OS concept"]),
        ("SovereignOS", "governance", "SUPERSEDED", 0, ["prior naming"]),
        ("SEEM-2.0-Self-Evolving-Emergent-Mind", "cognitive-substrate", "SUPERSEDED", 1, ["symbolic AGI-seed"]),
        ("SEEM-Cognitive-Microservice", "cognitive-substrate", "SUPERSEDED", 1, ["microservice kernel"]),
        ("SEEM-Cognitive_Microservice", "cognitive-substrate", "SUPERSEDED", 1, ["duplicate kernel"]),
        ("coherence-drive", "physics-cft", "RESEARCH", 2, ["vacuum-coherent engine integration"]),
        ("stress-tensor-modification", "physics-cft", "RESEARCH", 2, ["modified Maxwell stress tensor"]),
        ("momentum-closure", "physics-cft", "RESEARCH", 2, ["surface + Poynting closure"]),
        ("ware-constant-phenomenology", "physics-cft", "RESEARCH", 2, ["W≈0.08 phenomenology"]),
        ("sierpinski-geometry-045", "physics-cft", "RESEARCH", 2, ["0.45 Sierpinski geometry"]),
        ("CFT-v3.1", "physics-cft", "RESEARCH", 2, ["CFT white paper"]),
        ("CFT-v3.0", "physics-cft", "SUPERSEDED", 1, ["volumetric metric draft"]),
        ("CFT-v3.3-IQG-Unified-Framework", "physics-cft", "RESEARCH", 2, ["IQG unified draft"]),
        ("-ware-constant-derivation", "physics-cft", "RESEARCH", 2, ["Ware derivation notes"]),
        ("m2-renormalization-law", "physics-cft", "RESEARCH", 2, ["m2 renormalization"]),
        ("topological-pinch", "physics-cft", "RESEARCH", 2, ["topological pinch"]),
        ("thrust-target-30", "physics-cft", "RESEARCH", 2, ["thrust target study"]),
        ("optimization-limit-conjecture", "physics-cft", "RESEARCH", 2, ["obstruction floors"]),
        ("The-Origin-Point-Hypothesis.", "physics-cft", "RESEARCH", 1, ["origin-point paper"]),
        ("-Entanglement-and-Emergence", "physics-cft", "RESEARCH", 1, ["entanglement gravity sketch"]),
        ("-text-informational-fork-protocol-", "physics-cft", "RESEARCH", 1, ["informational fork protocol"]),
        ("Project-Cold-Boot", "simulation-games", "ACTIVE", 2, ["DLRSE sim", "SCAN SNAP SUNDER play"]),
        ("blacksite", "simulation-games", "EXPERIMENTAL", 2, ["PvE roguelite"]),
        ("ExoAxis-1", "health", "RESEARCH", 1, ["network pharmacology sketch"]),
        ("VigilE.S.A.-Enhanced-Security", "security-ops", "RESEARCH", 1, ["zero-trust sketch"]),
        ("acoustic-token-modem", "security-ops", "EXPERIMENTAL", 1, ["acoustic token channel"]),
        ("LegionOS", "agent-runtime", "RESEARCH", 1, ["legion OS sketch"]),
        ("Auto_Legion", "agent-runtime", "ARCHIVED", 0, ["early legion"]),
        ("Agent-Snake", "agent-runtime", "ARCHIVED", 0, ["snake agent"]),
        ("AtomicNexusAI", "agent-runtime", "ARCHIVED", 0, ["nexus AI"]),
        ("Gia---General-Intelligence-Assistant", "agent-runtime", "ARCHIVED", 1, ["local models + tools"]),
        ("Digital_Double_virtual_workforce", "agent-runtime", "RESEARCH", 1, ["virtual workforce"]),
        ("DigitalDoubleVirtualWorkforce3.5", "agent-runtime", "ARCHIVED", 0, ["workforce 3.5"]),
        ("Digital_Double_Virtual_Workforce_4.", "agent-runtime", "ARCHIVED", 0, ["workforce 4"]),
        ("Digital_Double_Virtual_Workforce_4.2", "agent-runtime", "ARCHIVED", 0, ["workforce 4.2"]),
        ("Digital-Double_Mobile", "agent-runtime", "ARCHIVED", 0, ["mobile double"]),
        ("digital-double-mobile", "agent-runtime", "ARCHIVED", 0, ["mobile double alias"]),
        ("BlockSwarm", "markets", "EXPERIMENTAL", 0, ["on-chain swarm"]),
        ("FortiTrade_Multi-Strategy", "markets", "ARCHIVED", 0, ["multi-strategy trade"]),
        ("btc-trading", "markets", "ARCHIVED", 0, ["btc scripts"]),
        ("fantom-smart-contracts-first-bot", "markets", "ARCHIVED", 0, ["FTM bot"]),
        ("fantom_trading_bot_2", "markets", "ARCHIVED", 0, ["FTM bot 2"]),
        ("ftmA.I.bot", "markets", "ARCHIVED", 0, ["FTM AI bot"]),
        ("seem-block-system", "cognitive-substrate", "RESEARCH", 1, ["SEEM block system"]),
        ("AEGIS-Project-Nehemiah-", "integrity", "RESEARCH", 2, ["Nehemiah source dump"]),
        ("My-mind-A.I.", "legacy", "ARCHIVED", 0, ["early personal AI"]),
        ("MyCore", "legacy", "ARCHIVED", 0, ["core sketch"]),
        ("new-program-1.01", "legacy", "ARCHIVED", 0, ["successor name"]),
        ("Code_Generation_AI_Program", "legacy", "ARCHIVED", 0, ["codegen sketch"]),
        ("automate_passive_income", "legacy", "ARCHIVED", 0, ["income automation"]),
        ("quantum_A.I._optimization.py", "legacy", "ARCHIVED", 0, ["filename-as-repo"]),
        ("Quantumclustering", "legacy", "ARCHIVED", 0, ["placeholder"]),
        ("-Py2APK-main", "legacy", "ARCHIVED", 0, ["apk packager"]),
        ("bolt.new", "legacy", "ARCHIVED", 0, ["fork"]),
        ("SuperAGI", "legacy", "ARCHIVED", 0, ["fork"]),
        ("DevelopTool-Unified-Dev-Environment", "legacy", "ARCHIVED", 0, ["dev env"]),
        ("RepoRover-", "legacy", "ARCHIVED", 0, ["repo rover"]),
        ("docs", "legacy", "ARCHIVED", 0, ["docs dump"]),
        ("beyond-repair", "legacy", "ARCHIVED", 0, ["profile repo"]),
        ("genieGPT", "legacy", "ARCHIVED", 0, ["gpt wrapper"]),
        ("smart_home_BCI", "health", "ARCHIVED", 0, ["BCI sketch"]),
        ("potential-garbanzo", "legacy", "ARCHIVED", 0, ["default name"]),
        ("test", "legacy", "ARCHIVED", 0, ["sandbox"]),
        ("sunder-aegis-bridge", "integrity", "EXPERIMENTAL", 0, ["planned merge-gate"]),
        ("clean-room-skill-export", "integrity", "EXPERIMENTAL", 0, ["planned skill export"]),
    ]

    for name, cluster, life, claim, fns in rows:
        art = _repo(name, cluster, life, claim, fns)
        artifacts[art.identity] = art

    artifacts["queue:compatible"] = Artifact(
        identity="queue:compatible",
        kind="QueueArtifact",
        properties={"items": ("sunder-aegis-bridge", "clean-room-skill-export")},
    )

    rels = [
        Relationship("GOVERNED_BY", "repo:ADL-Portfolio-Census", "repo:ADL-Governance"),
        Relationship("GOVERNED_BY", "repo:aegis-repo-graph", "repo:ADL-Governance"),
        Relationship("GOVERNED_BY", "repo:forge-aegis", "repo:ADL-Governance"),
        Relationship("GOVERNED_BY", "repo:sunder", "repo:ADL-Governance"),
        Relationship("GOVERNED_BY", "repo:sovereign-clean-room", "repo:ADL-Governance"),
        Relationship("GOVERNED_BY", "repo:ADL-SEEM", "repo:ADL-Governance"),
        Relationship("IMPLEMENTS", "repo:ADL-Portfolio-Census", "repo:ADL-Governance"),
        Relationship("IMPLEMENTS", "repo:aegis-repo-graph", "repo:forge-aegis"),
        Relationship("COMPATIBLE_WITH", "repo:aegis-repo-graph", "repo:ADL-Portfolio-Census"),
        Relationship("COMPATIBLE_WITH", "repo:aegis-repo-graph", "repo:forge-aegis"),
        Relationship("COMPATIBLE_WITH", "repo:sunder-aegis-bridge", "repo:sunder"),
        Relationship("COMPATIBLE_WITH", "repo:sunder-aegis-bridge", "repo:forge-aegis"),
        Relationship("COMPATIBLE_WITH", "repo:clean-room-skill-export", "repo:sovereign-clean-room"),
        Relationship("COMPATIBLE_WITH", "repo:clean-room-skill-export", "repo:forge-aegis"),
        Relationship("SUPERSEDES", "repo:Sovereign-OS", "repo:SovereignOS"),
        Relationship("SUPERSEDES", "repo:CFT-v3.1", "repo:CFT-v3.0"),
        Relationship("SUPERSEDES", "repo:sovereign-clean-room", "repo:SEEM-2.0-Self-Evolving-Emergent-Mind"),
        Relationship("SUPERSEDES", "repo:sunder", "repo:Gia---General-Intelligence-Assistant"),
        Relationship("CLUSTER_PEER", "repo:coherence-drive", "repo:stress-tensor-modification"),
        Relationship("CLUSTER_PEER", "repo:coherence-drive", "repo:momentum-closure"),
        Relationship("CLUSTER_PEER", "repo:coherence-drive", "repo:ware-constant-phenomenology"),
    ]
    return ArtifactGraph(artifacts=artifacts, relationships=rels)

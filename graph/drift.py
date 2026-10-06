"""Compare the locked catalog to a dated observed name set.

Does not mutate catalog rows. A name present only in the observation is not an artifact.
A name present only in the catalog is not deleted.
"""

from __future__ import annotations

from .catalog import build_graph
from .observed_2026_10_06 import OBSERVED_NAMES, OBSERVED_ON, SEARCH_TOTAL_COUNT


def catalog_repository_names() -> tuple[str, ...]:
    graph = build_graph()
    names = [
        art.properties["name"]
        for art in graph.artifacts.values()
        if art.kind == "RepositoryArtifact"
    ]
    return tuple(sorted(names))


def name_drift() -> dict[str, object]:
    catalog = set(catalog_repository_names())
    observed = set(OBSERVED_NAMES)
    return {
        "observed_on": OBSERVED_ON,
        "search_total_count": SEARCH_TOTAL_COUNT,
        "catalog_repository_count": len(catalog),
        "observed_count": len(observed),
        "observed_only": tuple(sorted(observed - catalog)),
        "catalog_only": tuple(sorted(catalog - observed)),
    }

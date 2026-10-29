"""Compare the locked catalog to a dated observed name set.

Does not mutate catalog rows. A name present only in the observation is not an artifact.
A name present only in the catalog is not deleted.
"""

from __future__ import annotations

from .catalog import build_graph
from .observed_2026_10_06 import OBSERVED_NAMES, OBSERVED_ON, SEARCH_TOTAL_COUNT
from .observed_2026_10_09 import OBSERVED_NAMES as OBSERVED_NAMES_2026_10_09
from .observed_2026_10_09 import OBSERVED_ON as OBSERVED_ON_2026_10_09
from .observed_2026_10_09 import SEARCH_TOTAL_COUNT as SEARCH_TOTAL_COUNT_2026_10_09
from .observed_2026_10_28 import OBSERVED_NAMES as OBSERVED_NAMES_2026_10_28
from .observed_2026_10_28 import OBSERVED_ON as OBSERVED_ON_2026_10_28
from .observed_2026_10_28 import SEARCH_TOTAL_COUNT as SEARCH_TOTAL_COUNT_2026_10_28
from .observed_2026_10_29 import OBSERVED_NAMES as OBSERVED_NAMES_2026_10_29
from .observed_2026_10_29 import OBSERVED_ON as OBSERVED_ON_2026_10_29
from .observed_2026_10_29 import SEARCH_TOTAL_COUNT as SEARCH_TOTAL_COUNT_2026_10_29


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


def observation_reconfirm() -> dict[str, object]:
    """Compare two frozen searches (06 to 09). Does not mutate the catalog."""
    earlier = set(OBSERVED_NAMES)
    later = set(OBSERVED_NAMES_2026_10_09)
    return {
        "earlier_on": OBSERVED_ON,
        "later_on": OBSERVED_ON_2026_10_09,
        "earlier_total_count": SEARCH_TOTAL_COUNT,
        "later_total_count": SEARCH_TOTAL_COUNT_2026_10_09,
        "later_only": tuple(sorted(later - earlier)),
        "earlier_only": tuple(sorted(earlier - later)),
        "name_set_equal": earlier == later,
    }


def observation_reconfirm_2026_10_28() -> dict[str, object]:
    """Compare 2026-10-09 frozen search to 2026-10-28. Does not mutate the catalog."""
    earlier = set(OBSERVED_NAMES_2026_10_09)
    later = set(OBSERVED_NAMES_2026_10_28)
    return {
        "earlier_on": OBSERVED_ON_2026_10_09,
        "later_on": OBSERVED_ON_2026_10_28,
        "earlier_total_count": SEARCH_TOTAL_COUNT_2026_10_09,
        "later_total_count": SEARCH_TOTAL_COUNT_2026_10_28,
        "later_only": tuple(sorted(later - earlier)),
        "earlier_only": tuple(sorted(earlier - later)),
        "name_set_equal": earlier == later,
    }


def observation_reconfirm_2026_10_29() -> dict[str, object]:
    """Compare 2026-10-28 frozen search to 2026-10-29. Does not mutate the catalog."""
    earlier = set(OBSERVED_NAMES_2026_10_28)
    later = set(OBSERVED_NAMES_2026_10_29)
    return {
        "earlier_on": OBSERVED_ON_2026_10_28,
        "later_on": OBSERVED_ON_2026_10_29,
        "earlier_total_count": SEARCH_TOTAL_COUNT_2026_10_28,
        "later_total_count": SEARCH_TOTAL_COUNT_2026_10_29,
        "later_only": tuple(sorted(later - earlier)),
        "earlier_only": tuple(sorted(earlier - later)),
        "name_set_equal": earlier == later,
    }

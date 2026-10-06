"""FLS-aligned repository Artifact Graph (locked-snapshot validator).

Do not import ``graph.engine`` here. ``python -m graph.engine`` must load that
module as ``__main__``; importing it during package init emits a RuntimeWarning.
"""

__version__ = "0.1.2"

__all__ = ["__version__"]

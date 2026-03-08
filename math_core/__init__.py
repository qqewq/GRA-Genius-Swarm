"""
GRA Math Core: Реализация многоуровневой архитектуры GRA Мета-обнулёнка.
"""
from .foam_functional import FoamFunctional
from .multiverse_state import MultiverseState, ProjectorHierarchy
from .beauty_score import beauty_score, embed_structure

__version__ = "1.0.0-multiverse"
__all__ = [
    "FoamFunctional",
    "MultiverseState",
    "ProjectorHierarchy",
    "beauty_score",
    "embed_structure"
]
"""
datapackpy.internal
===================
Internal utilities for datapack building.

This package is **not intended for direct use** by end-users.  
It supports the higher-level public APIs.

This package exposes only the public-facing APIs:
- `GameVersion`: encapsulates a specific Minecraft version.
- `utils`: general utility functions for datapack processing.
- `Component`: contains ABC class for all components, like `Advancement`
- `PackRegistry`: contains registry for holding components of a pack
"""

from .game_version import GameVersion
from . import utils  # keep utils as a submodule
from .component import Component
from .pack_registry import PackRegistry

__all__ = ["GameVersion", "utils", "Component", "PackRegistry"]

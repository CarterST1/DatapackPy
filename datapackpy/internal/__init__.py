"""
datapackpy.internal
===================
Internal utilities for datapack building.

This package is **not intended for direct use** by end-users.  
It supports the higher-level public APIs.

This package exposes only the public-facing APIs:
- `GameVersion`: encapsulates a specific Minecraft version.
- `PackMeta`: stores the metadata of a `DataPack`.
- `utils`: general utility functions for datapack processing.
"""

from .game_version import GameVersion
from .pack_meta import PackMeta
from . import utils  # keep utils as a submodule

__all__ = ["GameVersion", "PackMeta", "utils"]

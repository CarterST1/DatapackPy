"""
datapackpy.internal
===================
Internal utilities for datapack building.

This package is **not intended for direct use** by end-users.  
It supports the higher-level public APIs.

This package exposes only the public-facing APIs:
- `GameVersion`: encapsulates a specific Minecraft version.
- `utils`: general utility functions for datapack processing.
"""

from .game_version import GameVersion
from .export import Export
from . import utils  # keep utils as a submodule

__all__ = ["GameVersion", "Export", "utils"]

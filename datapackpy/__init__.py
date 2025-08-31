"""
datapackpy
===========
Main package for building and exporting Minecraft datapacks.

This package exposes only the public-facing APIs:
- `DataPack`: create and manage datapacks
- `components`: contains the classes to replicate Minecraft objects, such as `Advancement`
- `Export`: allows for building packs
"""

from .datapack import DataPack
from . import components
from .internal.export import Export

__all__ = ["DataPack", "components", "Export"]

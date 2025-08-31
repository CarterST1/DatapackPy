"""
datapackpy
===========
Main package for building and exporting Minecraft datapacks.

This package exposes only the public-facing APIs:
- `DataPack`: create and manage datapacks
- `core`: contains the classes to replicate Minecraft objects, such as `Advancement`
- `export`: allows for building packs
"""

from .datapack import DataPack
from . import core
from .internal.export import Export

__all__ = ["DataPack", "core", "Export"]

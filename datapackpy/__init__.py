"""
datapackpy
===========
Main package for building and exporting Minecraft datapacks.

This package exposes only the public-facing APIs:
- `DataPack`: create and manage datapacks
- `components`: contains the classes to replicate Minecraft objects, such as `Advancement`
"""

from .datapack import DataPack
from . import components

__all__ = ["DataPack", "components"]

"""
datapackpy.core
===============
Core package containing the primary building blocks of Minecraft datapacks.

This package exposes only the public-facing APIs:
- `Function`: represents a Minecraft function (a sequence of commands).
- (Future classes may include `Advancement`, `LootTable`, etc.)
"""

from .function import *

__all__ = ['Function']
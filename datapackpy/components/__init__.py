"""
datapackpy.components
===============
Core package containing the primary building blocks of Minecraft datapacks.

This package exposes only the public-facing APIs:
- `Function`: represents a Minecraft function (a sequence of commands).
- `PackMeta`: contains metadata for teh datapack
- (Future classes may include `Advancement`, `LootTable`, etc.)
"""

from .function import *
from .pack_meta import *

__all__ = ['Function', 'PackMeta']
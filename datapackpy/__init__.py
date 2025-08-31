"""Library that makes Minecraft datapack creation easier"""

from .datapack import DataPack
from . import internal
from . import core

__all__ = ["DataPack", "internal", "core"]  # only show top-level things

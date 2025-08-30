# Public modules
from . import datapack

# Internal modules
from .internal import game_version, pack_meta, utils

# Re-export public classes
DataPack = datapack.DataPack
GameVersion = game_version.GameVersion

__all__ = [
    "DataPack",
    "GameVersion",
]

# Clean up namespace (like pygame does)
del datapack
del game_version
del pack_meta
del utils

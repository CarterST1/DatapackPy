from typing import Optional, TypeAlias, Union
from modules.game_version import GameVersion
from modules import utils

Version: TypeAlias = GameVersion | tuple[int, int, int] | tuple[int, int]

class DataPack:
    """A collection of data used to configure a number of features of Minecraft"""
    def __init__(self, version: Version, namespace: str) -> None:
        if isinstance(version, tuple):
            version = GameVersion.fromTuple(version)
        self.game_version = version
        self.pack_format = utils.getPackFormatId(self.game_version)
        self.namespace = namespace

    def __str__(self) -> str:
        return f"DataPack[{self.namespace} | {self.game_version} | format={self.pack_format}]"

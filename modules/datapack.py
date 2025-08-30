from pathlib import Path
import shutil
from typing import final
from modules.game_version import GameVersion
from modules import utils
from modules.pack_meta import PackMeta

class DataPack:
    """A collection of data used to configure a number of features of Minecraft"""
    def __init__(self, version: utils.Version, name: str, namespace: str) -> None:
        self.name = name.lower()
        self.namespace = namespace
        if isinstance(version, tuple):
            version = GameVersion.fromTuple(version)
        self.game_version = version

        self.meta = PackMeta(self)

    def __str__(self) -> str:
        return f"DataPack[{self.namespace} | {self.game_version} | format={self.meta.pack_format}]"
    
    @final
    def save(self, path: str = 'dist'):
        dist_dir = Path(path)
        if dist_dir.exists() and dist_dir.is_dir():
            shutil.rmtree(dist_dir, ignore_errors=True)
        dist_dir.mkdir()

        pack_dir = Path(dist_dir / self.name)
        pack_dir.mkdir()

        mcMeta = Path(pack_dir / 'pack.mcmeta')
        mcMeta.write_text(self.meta.toJson())

        # Do other stuff

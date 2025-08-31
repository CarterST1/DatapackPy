from pathlib import Path
import shutil
from typing import final

from deprecated import deprecated
from datapackpy.internal.game_version import GameVersion
from datapackpy.internal import utils
from datapackpy.components.pack_meta import PackMeta

__all__ = ['DataPack']

class DataPack:
    """A collection of data used to configure a number of features of Minecraft"""
    def __init__(self, version: utils.Version, name: str, namespace: str) -> None:
        self.name = utils.slugify(name)
        self.namespace = utils.slugify(namespace)
        if isinstance(version, tuple):
            version = GameVersion.fromTuple(version)
        self.game_version = version

        self.components: list[utils.Component] = []

        self.meta = PackMeta(self)

    def __repr__(self) -> str:
        header = f"<DataPack '{self.namespace}' | {self.game_version}@format={self.meta.pack_format}"
    
        if not self.components:
            return f"{header} | 0 components>"
        
        # preview first 5 components
        preview_count = 5
        component_preview = ', '.join(
            f"<{c.__class__.__name__} '{c.name}'>" for c in self.components[:preview_count]
        )
        if len(self.components) > preview_count:
            component_preview += f", ... (+{len(self.components) - preview_count} more)"
        
        return f"{header} | {len(self.components)} components: {component_preview}>"
    
    @final
    @deprecated(reason='Use `export.py` functions instead')
    def save(self, path: str = 'dist'):
        """Deprecated: use `export.py` functions instead"""
        dist_dir = Path(path)
        if dist_dir.exists() and dist_dir.is_dir():
            shutil.rmtree(dist_dir, ignore_errors=True)
        dist_dir.mkdir()

        pack_dir = Path(dist_dir / self.name)
        pack_dir.mkdir()

        self.meta.createMetaFile(pack_dir)

        # Do other stuff

        return pack_dir
    
    def set_meta(self, meta: PackMeta):
        self.meta = meta
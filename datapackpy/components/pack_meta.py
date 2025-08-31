from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING

from datapackpy.internal.component import Component

__all__ = ['PackMeta']

if TYPE_CHECKING:
    from datapackpy.datapack import DataPack

import json
from datapackpy.internal import utils


class PackMeta(Component):
    def __init__(
            self,
            pack: DataPack,
            description: str = 'My First DataPack'
        ):
        super().__init__(pack, pack.namespace)

        self.pack = pack
        self.description = description
        packFormat = utils.getPackFormatId(self.pack.game_version)
        if packFormat:
            self.pack_format = packFormat
        else:
            raise ValueError(f"Invalid game version: {self.pack.game_version}")

    def toJson(self):
        rawDict = {
            'pack': {
                'description': self.description,
                'pack_format': int(self.pack_format)
            }
        }
        jsonDict = json.dumps(rawDict, indent=2)
        return jsonDict
    
    def export(self, base_dir: Path):
        """Writes this meta to a .mcmeta file."""
        meta_path = base_dir / 'pack.mcmeta'
        meta_path.parent.mkdir(parents=True, exist_ok=True)

        with meta_path.open("w", encoding="utf-8") as f:
            f.write(self.toJson())

    def is_empty(self) -> bool:
        return len(self.description) < 5
    
    def __repr__(self) -> str:
        string = f'<PackMeta \'{self.description}\' format={self.pack_format}>'
        return string

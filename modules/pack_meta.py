from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modules.datapack import DataPack

import json
from modules import utils
from modules.game_version import GameVersion


class PackMeta:
    def __init__(
            self,
            pack: DataPack,
            description: str = 'My First DataPack'
        ) -> None:

        self.pack = pack
        self.description = description
        packFormat = utils.getPackFormatId(self.pack.game_version)
        if packFormat:
            self.pack_format = packFormat
        else:
            raise NotImplemented

    def toJson(self):
        rawDict = {
            'pack': {
                'description': self.description,
                'pack_format': int(self.pack_format)
            }
        }
        jsonDict = json.dumps(rawDict, indent=2)
        return jsonDict
    
    def createMetaFile(self, pack_dir: Path):
        mcMeta = Path(pack_dir / 'pack.mcmeta')
        mcMeta.write_text(self.toJson())
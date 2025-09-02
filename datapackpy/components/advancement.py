from enum import Enum
from typing import Optional

from datapackpy.datapack import DataPack
from datapackpy.internal.component import Component


class AdvancementFrame(Enum):
    challenge = 0
    goal = 1
    task = 2

class Advancement(Component):
    def __init__(self, datapack: DataPack, name: str, parent: Optional['Advancement'], icon_id: str, title: str, description: str):
        super().__init__(datapack, name, 'advancement')
        self.parent = parent
        self.icon_id = icon_id
        self.title = title
        self.description = description
        self.frame = AdvancementFrame.task

        self.show_toast = True
        self.announce_to_chat = True
        self.hidden = False

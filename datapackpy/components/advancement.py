from enum import Enum
import json
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
    
    def __repr__(self) -> str:
        return f'<Advancement \'{self.resource_location}\'>'
    
    def is_empty(self) -> bool:
        return False
    
    def to_json(self):
        raw_json = {
            'display': {
                'icon': {'id': self.icon_id},
                'title': self.title,
                'description': self.description,
                'frame': self.frame.name,
                'show_toast': self.show_toast,
                'announce_to_chat': self.announce_to_chat,
                'hidden': self.hidden
            },
            'criteria': {
                'requirement': 'minecraft:impossible'
            }
        }
        
        return json.dumps(raw_json, indent=2)
    
    def export(self):
        """Writes this advancement to a .json file."""
        adv_path = self.export_path.with_suffix('.json')
        adv_path.parent.mkdir(parents=True, exist_ok=True)

        with adv_path.open("w", encoding="utf-8") as f:
            f.write(self.to_json())
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datapackpy.datapack import DataPack

from datapackpy.internal.component import Component

__all__ = ['Function']

class Function(Component):
    def __init__(self, name: str, datapack: 'DataPack'):
        super().__init__(datapack, name, 'function')
        self.commands: list[str] = []

    def add_command(self, command: str):
        """Add a Minecraft command to this function."""
        self.commands.append(command)

    def add_commands(self, *commands: str):
        """Add multiple commands at once."""
        self.commands.extend(commands)
    
    def __repr__(self) -> str:
        if not self.commands:
            return f"<Function '{self.resource_location}' | 0 commands>"

        # preview first 3 commands
        preview_count = 3
        preview_commands = [
            (c if len(c) <= 7 else c[:7] + "...")
            for c in self.commands[:preview_count]
        ]
        preview = ', '.join(preview_commands)
        
        if len(self.commands) > preview_count:
            preview += f", ... (+{len(self.commands) - preview_count} more)"
        
        return f"<Function '{self.resource_location}' | {len(self.commands)} commands: {preview}>"

    def export(self, base_dir: Path):
        """Writes this function to a .mcfunction file."""
        func_path = self.export_path.with_suffix('.mcfunction')
        func_path.parent.mkdir(parents=True, exist_ok=True)

        with func_path.open("w", encoding="utf-8") as f:
            f.write("\n".join(self.commands))

    def is_empty(self) -> bool:
        return not self.commands
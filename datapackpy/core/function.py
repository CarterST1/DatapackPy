from pathlib import Path
from datapackpy.internal.utils import slugify

__all__ = ['Function']

class Function:
    def __init__(self, name: str):
        self.name = slugify(name)
        self.commands: list[str] = []

    def add_command(self, command: str):
        """Add a Minecraft command to this function."""
        self.commands.append(command)

    def add_commands(self, *commands: str):
        """Add multiple commands at once."""
        self.commands.extend(commands)

    def __str__(self) -> str:
        """Return the function as a string ready to write to a .mcfunction file."""
        return "\n".join(self.commands)
    
    def create_function_file(self, path_dir: Path):
        function_file = Path(path_dir / f'{self.name}.mcfunction')
        function_file.write_text(str(self))

        return function_file
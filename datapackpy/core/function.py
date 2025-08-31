from pathlib import Path

__all__ = ['Function']

class Function:
    def __init__(self, name: str):
        from datapackpy.internal.utils import slugify
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
    
    def __repr__(self) -> str:
        string = f'<Function \'{self.name}\' | '
        string += f'{len(self.commands)} commands: '
        for i, command in enumerate(self.commands[:3]):
            if len(command) > 50:
                command = command[:50] + '...'
            string += f'\'{command}\''
            if i < len(self.commands[:3]) - 1:  # add comma except after the last command
                string += ', '
        if len(self.commands) > 3:
            string += f', ... (+{len(self.commands) - 3} more)'
        string += '>'
        return string

    def create_function_file(self, path_dir: Path):
        function_file = Path(path_dir / f'{self.name}.mcfunction')
        function_file.write_text(str(self))

        return function_file
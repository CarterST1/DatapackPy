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
        if not self.commands:
            return f"<Function '{self.name}' | 0 commands>"

        # preview first 3 commands
        preview_count = 3
        preview_commands = [
            (c if len(c) <= 7 else c[:7] + "...")
            for c in self.commands[:preview_count]
        ]
        preview = ', '.join(preview_commands)
        
        if len(self.commands) > preview_count:
            preview += f", ... (+{len(self.commands) - preview_count} more)"
        
        return f"<Function '{self.name}' | {len(self.commands)} commands: {preview}>"

    def create_function_file(self, path_dir: Path):
        function_file = Path(path_dir / f'{self.name}.mcfunction')
        function_file.write_text(str(self))

        return function_file
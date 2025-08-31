from pathlib import Path
import shutil
from typing import TYPE_CHECKING
from datapackpy.core.function import Function
from datapackpy.internal.utils import Component

if TYPE_CHECKING:
    from datapackpy.datapack import DataPack

class Export:
    def __init__(self, datapack: 'DataPack'):
        self.datapack = datapack
        self.export_location = 'dist'
        self.items: list[Component] = []

    def add_item(self, item: Component):
        if not isinstance(item, Component):
            raise ValueError(f'Item of type {str(type(item))} is not a Component')
        if item in self.items:
            print(f'{type(item).__name__} already exists')
            return
        self.items.append(item)

    def remove_item(self, item: Component):
        if not isinstance(item, Component):
            raise ValueError(f'Item of type {str(type(item))} is not a Component')
        if not item in self.items:
            print(f'{type(item)} isn\'t in cache')
            return
        self.items.remove(item)

    def build(self, path: Path | str = 'dist'):
        dist_path = Path(path)
        if dist_path.exists() and dist_path.is_dir():
            shutil.rmtree(dist_path, ignore_errors=True)
        dist_path.mkdir()
        
        datapack_dir = dist_path / self.datapack.name
        data_dir = datapack_dir / "data"
        namespace_dir = data_dir / self.datapack.namespace
        function_dir = namespace_dir / "function"

        self.datapack.meta.createMetaFile(datapack_dir)

        for component in self.items:
            if isinstance(component, Function):
                if len(component.commands) == 0:
                    print('Skipped Function with no commands')
                    continue
                component.create_function_file(function_dir)
from typing import TYPE_CHECKING
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
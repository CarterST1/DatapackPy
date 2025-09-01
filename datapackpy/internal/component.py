from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING

from datapackpy.internal import utils

__all__ = ['Component']

if TYPE_CHECKING:
    from datapackpy.datapack import DataPack

class Component(ABC):
    """Basic component used to make other components."""
    def __init__(self, datapack: 'DataPack', name: str, subpath: str = ''):
        self.name = utils.slugify(name)
        self.subpath = utils.slugify(subpath)
        self.datapack = datapack

        datapack.registry.add(self)

    @property
    def resource_location(self):
        success, namespace_path = utils.formatWithNamespace(
            self.datapack.namespace, (self.subpath + '/' if self.subpath else '') + self.name
        )
        if not success:
            raise ValueError(f"Invalid resource location: {self.name}")
        return namespace_path
    
    @property
    def export_path(self):
        """Return the filesystem path for this component inside the datapack."""
        path_parts = ((self.subpath + '/' if self.subpath else '') + self.name).split('/')
        return Path(self.datapack.get_pack_path()) / 'data' / path_parts[0] / Path(*path_parts[1:])
    
    @abstractmethod
    def export(self):
        """Export this component to disk."""
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """Return True if this component has no content and can be skipped."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
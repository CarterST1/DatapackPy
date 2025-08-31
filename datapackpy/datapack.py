from pathlib import Path
import shutil
from typing import final

from deprecated import deprecated
from datapackpy.internal.component import Component
from datapackpy.internal.game_version import GameVersion
from datapackpy.internal import utils
from datapackpy.internal.pack_registry import PackRegistry

__all__ = ['DataPack']

class DataPack:
    """A collection of data used to configure a number of features of Minecraft"""
    def __init__(self, version: utils.Version, name: str, namespace: str) -> None:
        self.name = utils.slugify(name)
        self.namespace = utils.slugify(namespace)
        if isinstance(version, tuple):
            version = GameVersion.fromTuple(version)
        self.game_version = version
        self.export_dir = 'dist'
        self.registry = PackRegistry()

        from datapackpy.components.pack_meta import PackMeta
        self.meta = PackMeta(self)

    def add_component(self, component: Component):
        """Manually add a component (optional, usually auto-registered)."""
        self.registry.add(component)

    def build(self):
        """Export all components to disk."""
        dist_path = Path(self.export_dir)
        if dist_path.exists():
            import shutil
            shutil.rmtree(dist_path, ignore_errors=True)
        dist_path.mkdir(parents=True, exist_ok=True)

        pack_path = self.get_pack_path()

        # Export all components
        for component in self.registry.all_components():
            if not component.is_empty():
                component.export(pack_path)
            else:
                print(f"Skipping empty component: {component}")

    def __repr__(self) -> str:
        comps = self.registry.all_components()
        comp_preview = ", ".join(f"<{c.__class__.__name__} '{c.name}'>" for c in comps[:5])
        if len(comps) > 5:
            comp_preview += f", ... (+{len(comps)-5} more)"
        return f"<DataPack '{self.namespace}' | {len(comps)} components: {comp_preview}>"
    
    def get_namespace_path(self):
        dist_path = Path(self.export_dir)
        return dist_path / self.name / 'data' / self.namespace
    
    def get_pack_path(self):
        dist_path = Path(self.export_dir)
        return dist_path / self.name
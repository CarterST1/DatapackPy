from datapackpy.internal.component import Component


class PackRegistry:
    def __init__(self) -> None:
        self._components: dict[str, Component] = {}
    
    def add(self, component: Component):
        loc = component.resource_location
        if loc in self._components:
            raise ValueError(f"Duplicate resource location: {loc}")
        self._components[loc] = component

    def get(self, resource_location: str):
        return self._components.get(resource_location)
    
    def all_components(self):
        return list(self._components.values())
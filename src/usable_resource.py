from src.resource import Resource, ResourceType

class UsableResource(Resource):
    def __init__(self, name:str, capacity:int):
        super().__init__(name, ResourceType.USABLE)
        if capacity <= 0:
            raise ValueError(f"Capacity for '{name}' must be positive.")
        self._capacity = capacity

    def is_available_for_use(self) -> bool:
        return self._is_available

    def allocate(self) -> None:
        if not self._is_available:
            print(f"Warning: Resource '{self.name}' is not available for use.")
        self._is_available = False

    def release(self) -> None:
        if self._is_available:
            print(f"Warning: Resource '{self.name}' is available for use.")
        self._is_available = True

    def use(self) -> None:
        print(f"Using resource '{self.name}' (Capacity: '{self._capacity}' GHz).")
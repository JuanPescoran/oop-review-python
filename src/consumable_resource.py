from src.resource import Resource, ResourceType

class ConsumableResource(Resource):
    def __init__(self, name:str, capacity: int):
        super().__init__(name, Resource.CONSUMABLE, capacity)
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self._total_capacity = capacity
        self._remaining_capacity = capacity

    def is_available_for_use(self) -> bool:
        return self._remaining_capacity > 0

    def allocate(self) -> None:
        if self._remaining_capacity <= 0:
            raise RuntimeError(f"Resource '{self}' has no capacity.")
        self._remaining_capacity -= 1
        self._is_available = self._remaining_capacity > 0

    def release(self) -> None:
        if self._remaining_capacity == 0 and not self._is_available:
            print(f"Warning: Consumable resource '{self.name}' is depleted and cannot be used without replenishment.")
        self._is_available = self._is_available > 0

    def use(self) -> None:
        print(f"Using consumable resource '{self.name}' (remaining: '{self._remaining_capacity}'/'{self._total_capacity}').")

    @property
    def remaining_capacity(self) -> int:
        return self._remaining_capacity
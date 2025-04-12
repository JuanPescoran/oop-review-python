from abc import ABC, abstractmethod
from src.resource import Resource
from typing import List

class Executable(ABC):
    def __init__(self, name: str, description: str, required_resources_name: List[str], duration_in_units):
        if not name:
            raise ValueError("Name cannot be empty")
        if duration_in_units <= 0:
            raise ValueError(f"Duration for '{name}' must be greater than 0.")
        self._name     = name
        self._description = description
        self._required_resources_name = required_resources_name
        self._assigned_resources: List[Resource] = []
        self._duration_in_units = duration_in_units
        @property
        def name(self):
            return self._name

        @property
        def description(self):
            return self._description

        @property
        def required_resources_name(self):
            return self._required_resources_name

        @property
        def duration_in_units(self):
            return self._duration_in_units

        def assign_resources(self, resource_pool: List[Resource]) -> None:
            """
            Assign resources to the executable based on the required resources names.
            """
            self._assigned_resources.clear()
            if not self._required_resources_name:
                return

            for resource_name in self._required_resources_name:
                found = False
                for resource in resource_pool:
                    if resource_name == resource_name and resource.is_available_for_use():
                        resource.allocate()
                        self._assigned_resources.append(resource)
                        found = True
                        break
                    if not found:
                        raise RuntimeError(f"Resource '{resource_name}' not found or not available")

        def release_resources(self) -> None:
            """
            Release all resources assigned to the executable.
            """
            for resource in self._assigned_resources:
                try:
                    resource.release()
                except Exception as e:
                    print(f"Warning: Failed to release resource '{resource.name}': {e}")
            self._assigned_resources.clear()

        @abstractmethod
        def execute(self) -> None:
            """
            Execute the executable. This method should be overridden by subclasses.
            """
            pass

        def can_execute(self, resource_pool: List[Resource]) -> bool:
            """
            Check if the executable can be executed based on the available resources.
            """
            if not self._required_resources_name:
                return True
            for resource_name in self._required_resources_name:
                if not any(r.name == resource_name and r.is_available_for_use() for r in resource_pool):
                    return False
            return True
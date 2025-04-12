from src.executable import Executable

class Task(Executable):
    def __init__(self, name: str, description: str, required_resources_name: list[str], duration_in_units: int):
        super().__init__(name, description, required_resources_name, duration_in_units)

    def execute(self) -> None:
        if len(self._assigned_resources) != len(self._required_resources_name):
            raise RuntimeError(f"Resources not assigned correctly for task '{self._name}'.")
        print(f"Executing task '{self._name}': '{self._description}' (Duration: '{self._duration_in_units}' units).")
        for resource in self._assigned_resources:
            resource.use()
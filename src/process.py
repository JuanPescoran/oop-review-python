from src.executable import Executable
from src.resource import Resource
from typing import List

class Process(Executable):
    def __init__(self,
                 name: str,
                 description: str,
                 required_resources_names: List[str],
                 duration_in_units: int):
        super().__init__(name, description, required_resources_names, duration_in_units)
        self._resource_pool: List[Resource] = []
        self._tasks: List[Executable] = []

    def add_resource(self, resource: Resource):
        self._resource_pool.append(resource)

    def add_task(self, task: Executable):
        self._tasks.append(task)

    def execute(self):
        if self._required_resources_names and len(self._required_resources_names) != len(self._assigned_resources):
            raise RuntimeError(f"Resources not properly assigned for {self.name} process.")
        print(f"Executing process {self._name}: {self._description} (Duration: {self.duration_in_units} units)")
        if self._assigned_resources:
            for resource in self._assigned_resources:
                resource.use()
        for task in self._tasks:
            try:
                if task.can_execute(self._resource_pool):
                    task.assign_resources(self._resource_pool)
                    print("  ", end="")
                    task.execute()
                    task.release_resources()
                else:
                    print(f"  Task {task.name} skipped: not enough resources.")
            except Exception as e:
                print(f"  Error executing task {task.name}: {e}")

    def run(self)-> None:
        try:
            if not self._required_resources_names or self.can_execute(self._resource_pool):
                if self._required_resources_names:
                    self.assign_resources(self._resource_pool)
                self.execute()
                self.release_resources()
                print(f"Process {self._name} completed successfully.")
            else:
                raise RuntimeError(f"Process {self._name} skipped: not enough resources in Pool to start.")
        except Exception as e:
            print(f"Error running process {self._name}: {e}")
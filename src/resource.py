from abc import ABC, abstractmethod
from enum import Enum

class ResourceType(Enum):
    """
    Enum for resource types.
    """

    CONSUMABLE = "Consumable"
    USABLE = "Usable"


class Resource(ABC):
    """ Abstract base class for all resources. """

    def __init__(self, name: str, resource_type: ResourceType):
        self._name = name
        self._is_available = True
        self._resource_type = resource_type

    @property
    def name(self) -> str:
        """ Returns the name of the resource. """
        return self._name

    @property
    def resource_type(self) -> ResourceType:
        """ Returns the type of the resource. """
        return self._resource_type

    @abstractmethod
    def is_available_for_use(self) -> bool:
        """ Returns True if the resource is available, False otherwise. """
        pass

    @abstractmethod
    def allocate(self) -> None:
        """ Allocates the resource. """
        pass

    @abstractmethod
    def use(self) -> None:
        """ Uses the resource. """
        pass

    @abstractmethod
    def release(self) -> None:
        """ Releases the resource. """
        pass
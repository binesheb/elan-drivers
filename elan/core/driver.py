from abc import ABC, abstractmethod
from collections.abc import Sequence

from .capabilities import Capability
from .device import Device


class Driver(ABC):
    """Base contract implemented by every vendor driver."""

    manufacturer: str

    @abstractmethod
    async def discover(self) -> Sequence[Device]:
        """Discover compatible devices on the local network."""

    @abstractmethod
    async def connect(self, device: Device) -> None:
        """Connect and authenticate to a device."""

    @abstractmethod
    async def disconnect(self, device: Device) -> None:
        """Close the device connection."""

    @abstractmethod
    async def get_capabilities(self, device: Device) -> set[Capability]:
        """Return capabilities supported by the specific device."""

    async def get_status(self, device: Device) -> object:
        raise NotImplementedError

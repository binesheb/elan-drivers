from dataclasses import dataclass, field
from enum import StrEnum

from .capabilities import Capability


class DeviceStatus(StrEnum):
    UNKNOWN = "unknown"
    ONLINE = "online"
    OFFLINE = "offline"
    ERROR = "error"


@dataclass(slots=True)
class Device:
    id: str
    manufacturer: str
    model: str | None = None
    name: str | None = None
    host: str | None = None
    port: int | None = None
    status: DeviceStatus = DeviceStatus.UNKNOWN
    capabilities: set[Capability] = field(default_factory=set)
    metadata: dict[str, object] = field(default_factory=dict)

    def supports(self, capability: Capability) -> bool:
        return capability in self.capabilities

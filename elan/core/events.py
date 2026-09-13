from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum


class EventType(StrEnum):
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    MOTION = "motion"
    ALARM = "alarm"
    ERROR = "error"
    STATUS_CHANGED = "status_changed"


@dataclass(frozen=True, slots=True)
class DeviceEvent:
    device_id: str
    event_type: EventType
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    data: dict[str, object] = field(default_factory=dict)

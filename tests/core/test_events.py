from datetime import timezone

from elan.core.events import DeviceEvent, EventType


def test_event_defaults_to_utc_timestamp() -> None:
    event = DeviceEvent(device_id="cam-1", event_type=EventType.MOTION)
    assert event.timestamp.tzinfo == timezone.utc
    assert event.event_type == EventType.MOTION

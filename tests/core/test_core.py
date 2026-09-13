import pytest

from elan.core.capabilities import Capability
from elan.core.device import Device, DeviceStatus
from elan.core.registry import DriverRegistry


def test_device_capability_detection() -> None:
    device = Device(
        id="cam-1",
        manufacturer="Hikvision",
        capabilities={Capability.STREAM, Capability.SNAPSHOT},
    )

    assert device.supports(Capability.STREAM)
    assert not device.supports(Capability.PTZ)
    assert device.status == DeviceStatus.UNKNOWN


def test_registry_is_case_insensitive() -> None:
    class StubDriver:
        manufacturer = "Hikvision"

    registry = DriverRegistry([StubDriver()])
    assert registry.get("hikVISION") is not None
    assert registry.manufacturers() == ("hikvision",)


def test_registry_rejects_duplicate_manufacturer() -> None:
    class StubDriver:
        manufacturer = "Tapo"

    registry = DriverRegistry([StubDriver()])
    with pytest.raises(ValueError):
        registry.register(StubDriver())

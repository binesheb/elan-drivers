import pytest

from elan.core.config import DeviceCredentials
from elan.core.device import Device, DeviceStatus
from elan.drivers.hikvision import HikvisionDriver


@pytest.mark.asyncio
async def test_hikvision_connect_lifecycle() -> None:
    driver = HikvisionDriver(DeviceCredentials("admin", "secret"))
    device = Device(id="cam-1", manufacturer="Hikvision", host="192.168.1.10")

    await driver.connect(device)
    assert device.status == DeviceStatus.ONLINE
    assert "cam-1" in driver._clients

    await driver.disconnect(device)
    assert device.status == DeviceStatus.OFFLINE
    assert "cam-1" not in driver._clients


def test_hikvision_rtsp_builder() -> None:
    driver = HikvisionDriver(DeviceCredentials("admin", "p@ss"))
    device = Device(id="cam-1", manufacturer="Hikvision", host="192.168.1.10")
    endpoint = driver.rtsp(device, channel=2, stream=1)
    assert endpoint.url("admin", "p@ss") == "rtsp://admin:p%40ss@192.168.1.10:554/Streaming/Channels/21"


def test_hikvision_isapi_endpoint() -> None:
    driver = HikvisionDriver(DeviceCredentials("admin", "secret"))
    device = Device(id="cam-1", manufacturer="Hikvision", host="192.168.1.10")
    assert driver.isapi(device).endpoint("ISAPI/System/deviceInfo") == "http://192.168.1.10/ISAPI/System/deviceInfo"

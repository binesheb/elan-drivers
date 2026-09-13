import pytest

from elan.core.config import DeviceCredentials
from elan.drivers.hikvision.isapi import IsapiClient


@pytest.mark.asyncio
async def test_isapi_get_uses_injected_transport() -> None:
    calls = []

    async def request(method, url, credentials, timeout, body=None):
        calls.append((method, url, credentials.username, timeout, body))
        return {"ok": True}

    client = IsapiClient(
        "192.168.1.10",
        DeviceCredentials("admin", "secret"),
        request=request,
    )
    result = await client.device_info()

    assert result == {"ok": True}
    assert calls[0][0] == "GET"
    assert calls[0][1] == "http://192.168.1.10/ISAPI/System/deviceInfo"
    assert calls[0][2] == "admin"


@pytest.mark.asyncio
async def test_isapi_put_and_post_preserve_body() -> None:
    calls = []

    async def request(method, url, credentials, timeout, body=None):
        calls.append((method, url, body))
        return True

    client = IsapiClient("camera", DeviceCredentials("admin", "secret"), request=request)
    await client.put("ISAPI/test", "<xml/>")
    await client.post("ISAPI/test", b"payload")

    assert calls == [
        ("PUT", "http://camera/ISAPI/test", "<xml/>"),
        ("POST", "http://camera/ISAPI/test", b"payload"),
    ]

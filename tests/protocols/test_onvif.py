import pytest

from elan.core.config import DeviceCredentials
from elan.core.exceptions import DriverAuthenticationError, DriverConnectionError
from elan.protocols.onvif.client import OnvifClient


@pytest.mark.asyncio
async def test_onvif_client_requires_endpoint() -> None:
    client = OnvifClient("", DeviceCredentials("admin", "secret"))
    with pytest.raises(DriverConnectionError):
        await client.connect()


@pytest.mark.asyncio
async def test_onvif_client_requires_username() -> None:
    client = OnvifClient("http://camera/onvif/device_service", DeviceCredentials("", "secret"))
    with pytest.raises(DriverAuthenticationError):
        await client.connect()


@pytest.mark.asyncio
async def test_onvif_client_connection_lifecycle() -> None:
    client = OnvifClient("http://camera/onvif/device_service", DeviceCredentials("admin", "secret"))
    await client.connect()
    assert (await client.get_device_information()).endpoint == client.endpoint
    await client.close()
    assert client.connected is False

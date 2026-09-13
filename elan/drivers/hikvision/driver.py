from collections.abc import Sequence

from ...core.capabilities import Capability
from ...core.config import DeviceCredentials, DriverConfig
from ...core.device import Device, DeviceStatus
from ...core.driver import Driver
from ...protocols.onvif.client import OnvifClient
from .isapi import IsapiClient
from .rtsp import RtspEndpoint


class HikvisionDriver(Driver):
    """Hikvision camera/NVR driver facade."""

    manufacturer = "Hikvision"

    def __init__(self, credentials: DeviceCredentials, config: DriverConfig | None = None) -> None:
        self.credentials = credentials
        self.config = config or DriverConfig()
        self._clients: dict[str, OnvifClient] = {}

    async def discover(self) -> Sequence[Device]:
        # Discovery transport is implemented separately so this driver can
        # support ONVIF discovery without coupling to vendor HTTP APIs.
        return ()

    async def connect(self, device: Device) -> None:
        if not device.host:
            raise ValueError("Hikvision device requires a host")
        client = OnvifClient(
            f"http://{device.host}/onvif/device_service",
            self.credentials,
            self.config,
        )
        await client.connect()
        self._clients[device.id] = client
        device.status = DeviceStatus.ONLINE

    async def disconnect(self, device: Device) -> None:
        client = self._clients.pop(device.id, None)
        if client is not None:
            await client.close()
        device.status = DeviceStatus.OFFLINE

    async def get_capabilities(self, device: Device) -> set[Capability]:
        capabilities = {
            Capability.DEVICE_INFO,
            Capability.STATUS,
            Capability.STREAM,
            Capability.SNAPSHOT,
            Capability.EVENTS,
        }
        if device.metadata.get("ptz"):
            capabilities.add(Capability.PTZ)
        return capabilities

    def isapi(self, device: Device) -> IsapiClient:
        if not device.host:
            raise ValueError("Hikvision device requires a host")
        return IsapiClient(device.host, self.credentials, self.config)

    def rtsp(self, device: Device, channel: int = 1, stream: int = 1) -> RtspEndpoint:
        if not device.host:
            raise ValueError("Hikvision device requires a host")
        return RtspEndpoint(device.host, channel=channel, stream=stream)

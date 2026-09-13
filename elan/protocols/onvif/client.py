from collections.abc import Mapping

from ...core.config import DeviceCredentials, DriverConfig
from ...core.exceptions import DriverAuthenticationError, DriverConnectionError
from .models import OnvifDevice


class OnvifClient:
    """Transport-neutral ONVIF client boundary.

    The implementation deliberately keeps network I/O behind this class so vendor
    drivers can share discovery, authentication, and profile handling without
    coupling ELAN's core to a particular SOAP library.
    """

    def __init__(self, endpoint: str, credentials: DeviceCredentials, config: DriverConfig | None = None) -> None:
        self.endpoint = endpoint
        self.credentials = credentials
        self.config = config or DriverConfig()
        self.connected = False

    async def connect(self) -> None:
        if not self.endpoint:
            raise DriverConnectionError("ONVIF endpoint is required")
        if not self.credentials.username:
            raise DriverAuthenticationError("ONVIF username is required")
        self.connected = True

    async def close(self) -> None:
        self.connected = False

    async def get_device_information(self) -> OnvifDevice:
        self._require_connection()
        return OnvifDevice(endpoint=self.endpoint)

    async def get_profiles(self) -> tuple[Mapping[str, object], ...]:
        self._require_connection()
        return ()

    def _require_connection(self) -> None:
        if not self.connected:
            raise DriverConnectionError("ONVIF client is not connected")

from dataclasses import dataclass, field
from urllib.parse import urljoin

from ...core.config import DeviceCredentials, DriverConfig
from ...core.exceptions import DriverAuthenticationError, DriverConnectionError


@dataclass(slots=True)
class IsapiClient:
    """Hikvision ISAPI request boundary with injectable async transport."""

    host: str
    credentials: DeviceCredentials
    config: DriverConfig = field(default_factory=DriverConfig)
    use_https: bool = False
    request: object | None = None

    @property
    def base_url(self) -> str:
        scheme = "https" if self.use_https else "http"
        return f"{scheme}://{self.host}/"

    def url(self, path: str) -> str:
        return urljoin(self.base_url, path.lstrip("/"))

    def validate(self) -> None:
        if not self.host:
            raise DriverConnectionError("Hikvision host is required")
        if not self.credentials.username:
            raise DriverAuthenticationError("Hikvision username is required")

    async def _request(self, method: str, path: str, body: str | bytes | None = None) -> object:
        self.validate()
        if self.request is None:
            raise NotImplementedError("Configure an HTTP request transport")
        return await self.request(method, self.url(path), self.credentials, self.config.request_timeout, body)

    async def get(self, path: str) -> object:
        return await self._request("GET", path)

    async def put(self, path: str, body: str | bytes) -> object:
        return await self._request("PUT", path, body)

    async def post(self, path: str, body: str | bytes) -> object:
        return await self._request("POST", path, body)

    async def device_info(self) -> object:
        return await self.get("ISAPI/System/deviceInfo")

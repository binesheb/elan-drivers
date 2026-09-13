from dataclasses import dataclass
from urllib.parse import urljoin

from ...core.config import DeviceCredentials, DriverConfig
from ...core.exceptions import DriverAuthenticationError, DriverConnectionError


@dataclass(slots=True)
class IsapiClient:
    """Small ISAPI transport boundary.

    Concrete HTTP I/O is intentionally kept behind this boundary so the driver
    can later use an async HTTP implementation without changing its public API.
    """

    host: str
    credentials: DeviceCredentials
    config: DriverConfig = DriverConfig()
    use_https: bool = False

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

    def endpoint(self, path: str) -> str:
        self.validate()
        return self.url(path)

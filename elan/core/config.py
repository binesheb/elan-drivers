from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DeviceCredentials:
    """Runtime-only credentials; never serialize this object to source control."""

    username: str
    password: str


@dataclass(frozen=True, slots=True)
class DriverConfig:
    connect_timeout: float = 5.0
    request_timeout: float = 10.0
    reconnect_attempts: int = 3

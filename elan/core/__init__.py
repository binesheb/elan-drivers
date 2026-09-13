"""Vendor-independent ELAN driver core."""

from .capabilities import Capability
from .config import DeviceCredentials, DriverConfig
from .device import Device, DeviceStatus
from .driver import Driver
from .exceptions import (
    DriverAuthenticationError,
    DriverConnectionError,
    DriverError,
    UnsupportedCapabilityError,
)
from .registry import DriverRegistry

__all__ = [
    "Capability", "Device", "DeviceStatus", "DeviceCredentials", "Driver",
    "DriverConfig", "DriverError", "DriverAuthenticationError",
    "DriverConnectionError", "UnsupportedCapabilityError", "DriverRegistry",
]

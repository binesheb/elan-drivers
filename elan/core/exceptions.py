class DriverError(Exception):
    """Base exception for ELAN driver failures."""


class DriverConnectionError(DriverError):
    """Raised when a device cannot be reached or connected."""


class DriverAuthenticationError(DriverError):
    """Raised when device authentication fails."""


class UnsupportedCapabilityError(DriverError):
    """Raised when an operation is not supported by a device."""

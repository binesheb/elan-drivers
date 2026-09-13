from collections.abc import Iterable

from .driver import Driver


class DriverRegistry:
    """Registry for vendor drivers."""

    def __init__(self, drivers: Iterable[Driver] = ()) -> None:
        self._drivers: dict[str, Driver] = {}
        for driver in drivers:
            self.register(driver)

    def register(self, driver: Driver) -> None:
        key = driver.manufacturer.casefold()
        if key in self._drivers:
            raise ValueError(f"Driver already registered: {driver.manufacturer}")
        self._drivers[key] = driver

    def get(self, manufacturer: str) -> Driver:
        try:
            return self._drivers[manufacturer.casefold()]
        except KeyError as exc:
            raise KeyError(f"No driver registered for: {manufacturer}") from exc

    def manufacturers(self) -> tuple[str, ...]:
        return tuple(self._drivers)

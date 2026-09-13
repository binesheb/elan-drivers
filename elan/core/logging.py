import logging


LOGGER_NAME = "elan.drivers"


def get_logger(component: str | None = None) -> logging.Logger:
    """Return the shared ELAN logger without configuring global handlers."""
    name = LOGGER_NAME if component is None else f"{LOGGER_NAME}.{component}"
    return logging.getLogger(name)

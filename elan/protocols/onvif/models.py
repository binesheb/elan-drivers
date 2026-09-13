from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class OnvifProfile:
    token: str
    name: str | None = None
    video_source_token: str | None = None
    video_encoder_token: str | None = None
    ptz_configuration_token: str | None = None
    stream_uri: str | None = None


@dataclass(frozen=True, slots=True)
class OnvifDevice:
    endpoint: str
    manufacturer: str | None = None
    model: str | None = None
    firmware: str | None = None
    serial_number: str | None = None
    hardware_id: str | None = None
    profiles: tuple[OnvifProfile, ...] = field(default_factory=tuple)

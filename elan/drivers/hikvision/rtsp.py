from dataclasses import dataclass
from urllib.parse import quote


@dataclass(frozen=True, slots=True)
class RtspEndpoint:
    host: str
    channel: int = 1
    stream: int = 1
    port: int = 554

    def url(self, username: str | None = None, password: str | None = None) -> str:
        auth = ""
        if username is not None:
            auth = quote(username, safe="")
            if password is not None:
                auth += f":{quote(password, safe='')}"
            auth += "@"
        return f"rtsp://{auth}{self.host}:{self.port}/Streaming/Channels/{self.channel}{self.stream}"

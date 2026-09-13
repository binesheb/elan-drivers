from enum import StrEnum


class Capability(StrEnum):
    DISCOVERY = "discovery"
    DEVICE_INFO = "device_info"
    STATUS = "status"
    STREAM = "stream"
    SNAPSHOT = "snapshot"
    EVENTS = "events"
    PTZ = "ptz"
    PRESETS = "presets"
    AUDIO = "audio"
    TWO_WAY_AUDIO = "two_way_audio"
    MOTION = "motion"
    PERSON_DETECTION = "person_detection"
    PRIVACY = "privacy"
    ALARM = "alarm"
    STORAGE = "storage"

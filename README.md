# ELAN Drivers

A modular device-driver framework for ELAN integration.

## Project status

🚧 Early development

The project starts with support for:

- Hikvision IP cameras / NVRs
- TP-Link Tapo cameras

The architecture is designed to support additional manufacturers and protocols without changing the ELAN-facing interface.

## Goals

- Unified device abstraction
- Capability-based driver model
- ONVIF support
- RTSP stream handling
- Hikvision ISAPI integration
- Tapo camera integration
- Device discovery
- Events and alarms
- PTZ and presets
- Audio and two-way audio where supported
- Connection monitoring and automatic recovery
- Diagnostics and structured logging
- Automated driver tests

## Architecture

```text
ELAN
  │
  ▼
ELAN Driver API
  │
  ▼
Driver Core
  ├── Hikvision
  ├── Tapo
  └── Future Drivers
       ├── Dahua
       ├── Uniview
       ├── Reolink
       └── ...
```

Drivers expose capabilities rather than assuming that every device supports every function.

## Development roadmap

### Phase 0 — Driver Core

- [ ] Driver interface
- [ ] Device model
- [ ] Capability model
- [ ] Driver registry
- [ ] Exceptions
- [ ] Logging
- [ ] Configuration
- [ ] Test framework

### Phase 1 — Hikvision

- [ ] Device discovery
- [ ] Authentication
- [ ] Device information
- [ ] Channel enumeration
- [ ] ISAPI client
- [ ] ONVIF integration
- [ ] RTSP streams
- [ ] Snapshots
- [ ] Events
- [ ] PTZ
- [ ] Presets
- [ ] Storage status

### Phase 2 — Tapo

- [ ] Device discovery
- [ ] Authentication
- [ ] Capability detection
- [ ] Camera status
- [ ] Live stream
- [ ] Snapshots
- [ ] Motion events
- [ ] Person detection where supported
- [ ] PTZ where supported
- [ ] Privacy mode
- [ ] Audio
- [ ] Alarm/siren

### Phase 3 — Unified API

- [ ] REST API
- [ ] WebSocket events
- [ ] Device management
- [ ] Unified camera controls

### Phase 4 — ELAN Integration

- [ ] ELAN driver packaging
- [ ] ELAN-facing commands
- [ ] Event mapping
- [ ] Connection/status feedback
- [ ] Integration testing

## Repository structure

```text
elan-drivers/
├── elan/
│   ├── core/
│   ├── protocols/
│   ├── drivers/
│   │   ├── hikvision/
│   │   └── tapo/
│   ├── discovery/
│   ├── events/
│   ├── streaming/
│   └── api/
├── tests/
├── examples/
├── docs/
└── tools/
```

## Design principles

1. Keep the ELAN-facing API manufacturer-independent.
2. Detect capabilities at runtime.
3. Prefer standards such as ONVIF where appropriate.
4. Keep vendor-specific protocol logic inside its driver.
5. Never store device credentials in source code.
6. Make failures observable through structured errors and logs.
7. Test against real hardware as well as mocks.
8. Add new manufacturers without breaking existing drivers.

## Security

Credentials, tokens, certificates, and private device information must never be committed to the repository. Use environment variables or a secure configuration mechanism during development.

## License

License to be decided during the initial development phase.

# PPS Wire Protocol v0.1 — Candidate

Status: Candidate / not production-frozen
Date: 2026-10-06

## Discovery frame

PPS v0.1 uses a 17-byte candidate BLE discovery payload. It is T0 discovery, not authenticated identity.

| Offset | Bytes | Field |
|---|---:|---|
| 0 | 1 | wire_version = 0x01 |
| 1 | 1 | frame_type = 0x01 mobile person |
| 2 | 1 | policy_version = 0x01 |
| 3 | 2 | policy_flags |
| 5 | 8 | ephemeral identifier (EID) |
| 13 | 2 | epoch_hint |
| 15 | 1 | capabilities |
| 16 | 1 | reserved = 0 |

Multibyte integers use network byte order.

## Policy flags

Set means DENIED/RESTRICTED: 0x0001 capture; 0x0002 identification; 0x0004 profiling; 0x0008 emotion inference; 0x0010 retention; 0x0020 cloud upload; 0x0040 training; 0x0080 commercial use. Higher bits are reserved. An unset bit is not affirmative consent.

## Capabilities

bit 0 authenticated-session upgrade; bit 1 Nearby-compatible local transport; bit 2 UWB binding candidate; bit 3 QR semantic policy. A capability bit is not proof that the mechanism has run.

## Privacy and rotation

The EID MUST NOT be a stable account/device/person identifier and MUST rotate. Adjacent values MUST NOT be publicly predictable. Candidate interoperability tests use a maximum 15-minute EID lifetime; production value remains subject to field/security review. epoch_hint is not authentication.

## Trust upgrade

T0: syntactically valid discovery -> DISCOVERED_UNVERIFIED.

T1: authenticated local session + canonical policy digest + fresh session evidence -> AUTHENTICATED_UNBOUND. Android Mobile Binding v0.2 is the current T1-oriented experiment.

T2: T1 plus a documented subject-binding profile/evidence -> BOUND state. BLE alone never establishes T2.

## Authentication decision

v0.1 does not place a truncated MAC/signature in the open discovery frame. Shared broadcast MACs create key-distribution/impersonation problems; public-key broadcast authentication needs a larger privacy/key architecture. Broadcast-verifiable authentication is deferred to a later cryptographic profile.

## Parsing

Receivers MUST reject wrong length, unsupported wire version/frame type and nonzero reserved byte. Parsing MUST be bounded before trust upgrade. Duplicate T0 frames MAY be coalesced. T1 freshness comes from authenticated session evidence, not epoch_hint alone.

## Extensions and production blockers

New policy semantics require a policy-version change; incompatible layout requires a wire-version/frame-type change. Production freeze still requires independent crypto review, final EID construction and timing, second implementation, fuzzing, negative vectors, measured resource limits and binding validation.

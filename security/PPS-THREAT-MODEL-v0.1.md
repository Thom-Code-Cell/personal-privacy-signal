# PPS / PPS+ Threat Model v0.1

Status: Draft for manufacturer integration
Date: 2026-10-06
Project: PPS / PPS+ — TH Analytica Physical AI Governance
Scope: Security and privacy requirements that MUST be resolved before freezing a production wire protocol.

## 1. Purpose

PPS is a vendor-neutral policy-enforcement protocol concept for Physical AI. It separates PPS Protocol (discovery/transport), PPS+ Policy (machine-readable rules), PPS Binding (association with a physical subject/place), PPS Enforcement (receiver behaviour), and PPS Conformance (reproducible implementation evidence).

This threat model intentionally precedes a normative BLE byte layout. Packet size, identifiers, authenticators, rotation intervals and extension fields MUST be derived from security requirements rather than fixed first.

## 2. Security goals

1. Authenticity: distinguish authentic protocol messages from arbitrary injected data at the claimed trust level.
2. Integrity: policy data cannot be modified undetected in transit.
3. Freshness: stale observations cannot be replayed as current consent or restriction.
4. Unlinkability: passive observers cannot use PPS as a durable person-tracking identifier.
5. Data minimisation: discovery does not require name, account, advertising ID, GPS history, face template or persistent identity.
6. Binding confidence: radio proximity is not silently equated with visual subject identity.
7. Availability: malformed or high-volume PPS traffic cannot trivially disable a receiver.
8. Deterministic enforcement: resolved policy produces defined receiver behaviour.
9. Safe degradation: uncertainty MUST NOT silently become permission for privacy-invasive processing.
10. Auditable exceptions: safety/emergency exceptions are narrow and reviewable without creating a general surveillance bypass.

## 3. Non-goals and current limitations

PPS v0.1 does not claim that an open BLE advertisement proves who sent it; that RSSI identifies a person in a camera frame; that Android Mobile Binding solves camera-to-person attribution; that commercial smart glasses currently enforce PPS; that UWB ranging has been validated on the current field devices; that a safety exception may be activated solely by an unverified radio assertion; or that PPS implementation alone establishes legal compliance.

Existing Mobile Binding v0.2 demonstrates authenticated nearby policy transport, session/policy-bound acknowledgement and explicit user confirmation. It is a transport/binding building block, not proof of spatial subject attribution.

## 4. Assets to protect

- A1 Personal policy integrity: DENY/ALLOW and other semantics cannot be changed undetected.
- A2 Subject privacy: PPS must not create a durable identifier, movement history or identity graph.
- A3 Binding correctness: one person's policy must not be enforced against another because of weak proximity inference.
- A4 Receiver availability: malformed, duplicated or high-volume signals must not exhaust the receiver.
- A5 Enforcement integrity: restrictions must survive capture, inference, retention, upload and training stages.
- A6 Safety exception integrity: emergency processing must not become a generic override channel.
- A7 Protocol agility: obsolete/downgraded versions and cryptographic mechanisms can be rejected/migrated.

## 5. Trust boundaries

PPS sender -> untrusted/shared radio environment -> discovery parser -> authenticity/freshness boundary -> policy resolver -> subject-binding confidence boundary -> OS/firmware enforcement point -> local inference / identity / profiling / retention / cloud / training -> user feedback and audit/exception path.

All radio input MUST be treated as attacker-controlled until validated to the trust level required by the requested action.

## 6. Adversaries

- Passive observer: records broadcasts to track people.
- Spoofer: transmits forged PPS messages or copies another subject's policy.
- Replay attacker: rebroadcasts previously valid messages.
- Relay attacker: forwards a live signal from another location.
- Flooder: emits many fake senders/messages to exhaust resources.
- Downgrade attacker: forces an older/weaker protocol or interpretation.
- Malicious receiver: claims PPS support but ignores or selectively enforces policies.
- Compromised sender: malware changes policy or abuses credentials.
- Curious infrastructure operator: aggregates ephemeral observations into a tracking graph.
- Binding manipulator: causes a valid policy to be associated with the wrong visible subject.
- Exception abuser: falsely triggers safety/emergency processing.

## 7. Threat catalogue and requirements

### T01 Static identifier tracking
Threat: stable BLE/device/policy identifiers enable passive tracking.
Requirements: no stable public person identifier; ephemeral identifiers MUST rotate without a deterministic public sequence; receivers SHOULD minimise raw discovery retention; conformance MUST test rotation and prohibited identifiers.

### T02 Replay
Threat: a captured valid packet is rebroadcast later.
Requirements: production authentication MUST include freshness; replay windows MUST be bounded; session transports MUST bind ACKs to active session and policy; duplicate/stale messages MUST NOT extend expired presence. Mobile Binding v0.2 nonce + policy hash + echoed ACK is useful session protection but does not authenticate the separate open BLE advertisement.

### T03 Signal spoofing / policy impersonation
Threat: an attacker advertises another person's restrictive or permissive policy.
Requirements: trust levels MUST distinguish unauthenticated presence from authenticated policy; privileged effects MUST NOT rely on unauthenticated advertisement alone; production design MUST support cryptographic proof appropriate to trust level; key material MUST NOT create a stable tracking identifier.

### T04 Relay / wormhole
Threat: a valid live signal is forwarded into another physical space.
Requirements: proximity MUST NOT follow solely from message validity; binding MAY combine independent local evidence such as authenticated connection, ranging/direction or other device-local context; high-impact enforcement requiring attribution MUST expose binding confidence.

### T05 False subject binding
Threat: a nearby sender is mapped to the wrong person/object in sensor data.
Requirements: radio presence alone MUST NOT equal camera identity; Subject Binding MUST be modular with explicit confidence/state; UNBOUND and AMBIGUOUS states MUST exist; uncertain binding MUST NOT authorize otherwise prohibited identity matching/profiling; implementations MUST document binding evidence. RSSI, AoA, ToF/UWB, depth and visual geometry are candidate signals, not mandatory proof.

### T06 Signal flooding / Sybil DoS
Threat: many fake PPS presences overload discovery or cause blanket disablement.
Requirements: bounded CPU/memory/queues; rate limits for repeated/invalid sources; unauthenticated broadcasts MUST NOT trigger unlimited expensive crypto/UI work; duplicate coalescing and expiry MUST be defined; PPS MUST NOT become an anonymous kill switch.

### T07 Malformed payload / parser exploitation
Threat: crafted packets cause crashes, overflows or inconsistent parsing.
Requirements: explicit version/length rules; deterministic unknown/reserved handling; reject invalid encodings before policy evaluation; conformance corpus includes malformed, truncated, oversized and reserved vectors; reference parsers SHOULD be fuzz tested.

### T08 Downgrade / version confusion
Threat: attacker forces weaker semantics or crypto.
Requirements: version MUST be authenticated where authentication exists; unsupported versions fail explicitly; security semantics MUST NOT silently fall back; crypto agility/deprecation rules MUST precede production freeze.

### T09 Policy tampering / semantic confusion
Threat: transport flags and resolved semantic policy disagree.
Requirements: canonical mapping MUST be versioned; authenticated transports bind authentication to exact policy representation or canonical digest; contradictory/unknown rules resolve deterministically; binary flags and JSON/JSON-LD require testable equivalence.

### T10 Receiver non-compliance
Threat: vendor claims compatibility while enforcement is partial/deceptive.
Requirements: PPS Conformance tests observable receiver behaviour; capabilities are declared by level rather than a vague compatible claim; tests cover capture, identification, profiling, embedding generation, retention, cloud upload, training/secondary use and feedback where applicable; unsupported controls are reported.

### T11 Downstream enforcement bypass
Threat: capture is restricted while embeddings, logs, cloud copies or training continue.
Requirements: enforcement covers the processing lifecycle, not cosmetic pixelation; resolution occurs before protected downstream processing; derived data inherits applicable restrictions unless normative policy says otherwise; OS/firmware enforcement points SHOULD constrain app bypass.

### T12 Safety/emergency override abuse
Threat: normal processing is labelled safety to bypass PPS.
Requirements: exceptions MUST be narrow and separately specified; an unverified PPS packet MUST NOT trigger override; activation SHOULD require appropriate device-local or trusted evidence; scope/duration MUST be minimal; normal policy resumes automatically; audit SHOULD capture reason/scope/time without unnecessary identity/location retention.

### T13 Compromised sender / key theft
Threat: malware or extracted keys publish unauthorized policies.
Requirements: production key material SHOULD use platform-backed secure storage; rotation/revocation MUST be defined; compromise recovery MUST NOT require permanent public identity; reference implementations avoid long-lived secrets in logs/backups.

### T14 Correlation across transports
Threat: BLE, QR, Nearby, UWB or web representations expose a common stable identifier.
Requirements: cross-transport correlation MUST be minimised; semantic policy identity and radio presence identity MUST be separable; public documents MUST NOT require stable personal ID; tests inspect whether transport combination defeats unlinkability.

### T15 Privacy-invasive telemetry
Threat: compliance logging becomes surveillance.
Requirements: telemetry MUST be minimised; raw nearby-person histories SHOULD NOT be retained by default; audit evidence SHOULD prefer aggregate/event-scoped records; logs MUST NOT silently add names, account IDs, precise location or biometrics.

## 8. Binding state model

A manufacturer profile SHOULD expose at least: UNSEEN; DISCOVERED_UNVERIFIED; AUTHENTICATED_UNBOUND; BOUND_LOW_CONFIDENCE; BOUND_HIGH_CONFIDENCE; AMBIGUOUS; EXPIRED/DISCONNECTED.

The normative Manufacturer Integration Profile MUST define permitted enforcement actions at each state. A permissive action MUST NOT be inferred merely because binding is uncertain.

## 9. Preliminary trust levels

- T0 Advisory Presence: syntactically valid but unauthenticated discovery.
- T1 Session Authenticated: authenticated local session/policy integrity; no visual subject-attribution claim.
- T2 Bound Policy: authenticated policy plus binding evidence meeting a defined confidence profile.

A future higher level may cover hardware-backed attestation. v0.1 MUST NOT claim it until requirements and interoperable evidence exist.

## 10. Security decisions required before Wire Protocol v0.1

1. Trust level required for each policy action.
2. Identifier lifetime and unlinkability target.
3. Freshness/replay window.
4. Authenticator construction and truncation strength.
5. Key establishment, rotation and compromise recovery.
6. Broadcast-verifiable, session-established or hybrid authentication.
7. Maximum parser work per unauthenticated sender.
8. Version/downgrade behaviour.
9. Policy canonicalisation and flag-to-semantic mapping.
10. Extension mechanism.
11. Binding-state semantics and confidence requirements.
12. Exception authorization and audit requirements.

Only after these are resolved should PPS commit to a BLE payload byte count.

## 11. Conformance test families

- C-PRIV: rotation, unlinkability, prohibited identifiers.
- C-REPLAY: stale, duplicate, reordered messages.
- C-AUTH: forged, modified, wrong-key policies.
- C-DOS: flood, duplicate, resource-bound tests.
- C-PARSE: malformed/truncated/reserved-value corpus.
- C-VERSION: downgrade and unsupported-version tests.
- C-BIND: unbound, ambiguous, low/high-confidence and multi-person scenarios.
- C-POLICY: binary/semantic equivalence and conflict resolution.
- C-ENFORCE: lifecycle controls across inference, identity, profiling, retention, upload and training.
- C-SAFETY: exception authorization, duration, recovery and audit.
- C-XPORT: cross-transport correlation/privacy tests.

## 12. Manufacturer integration consequence

A manufacturer is not asked to trust a radio packet and blur a person. The intended sequence is: PPS discovery -> authenticity/freshness -> subject-binding state -> policy resolution -> OS/firmware enforcement point -> local processing controls -> user feedback -> narrowly scoped auditable safety exception.

Each transition has a defined trust boundary and must be independently testable.

## 13. Open decisions for v0.2

Before PPS Wire Protocol v0.1 is frozen: choose cryptographic authentication; quantify replay/freshness windows; define ephemeral rotation; define T0/T1/T2 enforcement permissions; define binding confidence inputs without mandating vendor sensors; define hostile-radio resource limits; freeze canonical PPS+ semantics; define safety-exception authorization; produce positive and negative conformance vectors.

## 14. Provenance and project position

This document is part of the PPS / PPS+ work by TH Analytica. It records a candidate security architecture for open technical review. It is not a claim of adoption by any smart-glasses manufacturer, standards body or platform vendor.

The design deliberately preserves the distinction between what has been demonstrated in the Android lab and what remains a production security requirement.
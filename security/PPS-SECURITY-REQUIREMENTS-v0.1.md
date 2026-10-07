# PPS Security Requirements v0.1

Status: Candidate requirements for manufacturer integration
Date: 2026-10-06
Project: PPS / PPS+ — TH Analytica Physical AI Governance
Source: `security/PPS-THREAT-MODEL-v0.1.md`

## 1. Normative language

The key words MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT and MAY indicate requirement strength for this candidate specification. This document does not claim adoption by a standards body or manufacturer.

## 2. Architecture invariants

- **SR-ARCH-001** PPS MUST separate policy semantics from discovery transport.
- **SR-ARCH-002** A receiver MUST treat radio/discovery input as untrusted until the applicable trust checks complete.
- **SR-ARCH-003** A receiver MUST represent subject-binding state separately from policy authenticity.
- **SR-ARCH-004** Failure to establish subject binding MUST NOT be interpreted as positive permission for otherwise restricted identity, profiling, retention, upload or training operations.
- **SR-ARCH-005** Manufacturer enforcement MUST address downstream processing, not only display-time redaction.

## 3. Privacy and unlinkability

- **SR-PRIV-001** Mobile-person discovery MUST NOT expose name, e-mail, account ID, advertising ID, phone number, biometric template or GPS history.
- **SR-PRIV-002** Mobile-person radio discovery MUST NOT require a stable public PPS identifier.
- **SR-PRIV-003** Ephemeral discovery identifiers MUST rotate.
- **SR-PRIV-004** Identifier rotation MUST NOT use a publicly predictable sequence that enables trivial linkage.
- **SR-PRIV-005** Receivers SHOULD discard raw ephemeral identifiers when no longer required for the active protocol purpose.
- **SR-PRIV-006** Cross-transport representations MUST NOT require a common stable personal identifier.
- **SR-PRIV-007** Compliance telemetry MUST be data-minimised and MUST NOT silently create a nearby-person movement history.

## 4. Authenticity, integrity and freshness

- **SR-AUTH-001** The protocol MUST distinguish unauthenticated discovery from authenticated policy state.
- **SR-AUTH-002** A T0 observation MUST NOT be represented as cryptographically authenticated.
- **SR-AUTH-003** T1 or higher MUST provide integrity protection for the policy representation or its canonical digest.
- **SR-AUTH-004** T1 or higher MUST provide freshness protection sufficient to reject stale session/policy reuse.
- **SR-AUTH-005** Session acknowledgements MUST be bound to the active session and applicable policy.
- **SR-AUTH-006** Production authentication MUST define key establishment or verification, rotation and compromise recovery.
- **SR-AUTH-007** Long-lived secret key material SHOULD use platform-backed secure storage when available.
- **SR-AUTH-008** Authentication material MUST NOT intentionally create a stable public tracking identifier.

## 5. Replay and relay resistance

- **SR-FRESH-001** The production protocol MUST define an explicit freshness mechanism.
- **SR-FRESH-002** The production protocol MUST define a bounded acceptance/replay window or equivalent freshness rule.
- **SR-FRESH-003** Duplicate or stale observations MUST NOT extend an expired policy presence.
- **SR-RELAY-001** Cryptographic validity alone MUST NOT be treated as proof of physical proximity.
- **SR-RELAY-002** A T2 bound-policy claim MUST include binding evidence meeting the defined binding profile.

## 6. Subject binding

- **SR-BIND-001** Radio presence alone MUST NOT establish camera-to-person attribution.
- **SR-BIND-002** Implementations MUST support at least UNSEEN, DISCOVERED_UNVERIFIED, AUTHENTICATED_UNBOUND, AMBIGUOUS and EXPIRED/DISCONNECTED states.
- **SR-BIND-003** Implementations claiming T2 MUST additionally expose a bound state and its confidence/profile.
- **SR-BIND-004** Binding evidence MUST be documented by the implementation.
- **SR-BIND-005** RSSI, AoA, ToF/UWB, depth, visual geometry or other signals MAY contribute to binding but no individual candidate signal is normative in v0.1.
- **SR-BIND-006** Multiple plausible subjects/senders MUST resolve to AMBIGUOUS rather than silently selecting one.
- **SR-BIND-007** The Manufacturer Integration Profile MUST define allowed enforcement behaviour for every binding state.

## 7. Parser and availability security

- **SR-PARSE-001** Every wire representation MUST have explicit version and length/structure validation.
- **SR-PARSE-002** Invalid, truncated, oversized or unsupported messages MUST be rejected before policy enforcement.
- **SR-PARSE-003** Unknown and reserved values MUST have deterministic handling.
- **SR-PARSE-004** Reference parsers SHOULD be fuzz-tested before production designation.
- **SR-DOS-001** Receiver CPU, memory and queue work attributable to unauthenticated senders MUST be bounded.
- **SR-DOS-002** Receivers MUST implement duplicate suppression, expiry or equivalent controls.
- **SR-DOS-003** Receivers MUST rate-limit or otherwise bound repeated invalid traffic.
- **SR-DOS-004** An unauthenticated sender MUST NOT be able to create unlimited expensive cryptographic operations or UI prompts.
- **SR-DOS-005** Anonymous PPS traffic MUST NOT function as an unconditional safety/security kill switch.

## 8. Versioning and downgrade resistance

- **SR-VERS-001** Every normative wire message MUST identify its protocol version.
- **SR-VERS-002** Unsupported versions MUST fail explicitly rather than silently reinterpret security-critical fields.
- **SR-VERS-003** Where message authentication exists, security-relevant version information MUST be covered by authentication.
- **SR-VERS-004** The production specification MUST define algorithm agility and deprecation behaviour.

## 9. Policy semantics

- **SR-POL-001** PPS+ policy semantics MUST be versioned independently from transport.
- **SR-POL-002** Compact transport flags MUST have a deterministic mapping to canonical semantic policy.
- **SR-POL-003** Authenticated policy transport MUST protect either the exact canonical representation or a canonical digest.
- **SR-POL-004** Unknown, contradictory and reserved policy values MUST resolve deterministically.
- **SR-POL-005** A permissive personal rule MUST NOT override a stricter applicable place rule under the current candidate conflict model.
- **SR-POL-006** Binary and JSON/JSON-LD representations MUST have conformance vectors demonstrating semantic equivalence.

## 10. Enforcement requirements

- **SR-ENF-001** Enforcement capabilities MUST be declared explicitly; a generic 'PPS compatible' claim is insufficient.
- **SR-ENF-002** A receiver MUST NOT report a control as enforced when it is unsupported or advisory only.
- **SR-ENF-003** Where applicable, enforcement profiles MUST distinguish capture, identification, profiling, embedding generation, retention, cloud upload, training/secondary use and user feedback.
- **SR-ENF-004** Derived data MUST inherit applicable restrictions unless the normative policy explicitly defines otherwise.
- **SR-ENF-005** Policy resolution required for protected processing MUST occur before the protected downstream operation.
- **SR-ENF-006** OS/firmware integrations SHOULD place enforcement at a trust boundary that constrains application bypass.

## 11. Safety and emergency exceptions

- **SR-SAFE-001** Safety/emergency exceptions MUST be separately specified from normal policy resolution.
- **SR-SAFE-002** An unverified PPS message MUST NOT itself authorize an emergency override.
- **SR-SAFE-003** Override activation MUST require evidence appropriate to the safety use case and trust model.
- **SR-SAFE-004** Override scope and duration MUST be limited to the safety purpose.
- **SR-SAFE-005** Normal policy enforcement MUST resume automatically when the exception ends.
- **SR-SAFE-006** Exception audit SHOULD record reason, scope and time while minimising identity and location data.

## 12. Trust levels

- **T0 — Advisory Presence:** syntactically valid discovery; no cryptographic authenticity claim.
- **T1 — Session Authenticated:** policy/session integrity and freshness established; no visual subject-attribution claim.
- **T2 — Bound Policy:** T1 plus subject-binding evidence satisfying a defined binding profile.

- **SR-TRUST-001** Implementations MUST NOT claim a higher trust level than the evidence actually established.
- **SR-TRUST-002** A future hardware-attested trust level MUST NOT be claimed until its requirements and interoperability tests are separately specified.

## 13. Conformance requirements

- **SR-CONF-001** Each MUST/MUST NOT requirement intended for implementation MUST map to at least one positive or negative conformance test before production designation.
- **SR-CONF-002** Conformance MUST include malformed input, replay, spoofing, downgrade, binding ambiguity, flood/resource and safety-exception cases.
- **SR-CONF-003** A conformance report MUST identify protocol version, policy version, trust level and enforcement capabilities tested.
- **SR-CONF-004** Partial conformance MUST be reported as partial; unsupported enforcement domains MUST remain visible.

## 14. Decisions required before PPS Wire Protocol v0.1

The wire protocol MUST NOT be frozen until the following have explicit values or algorithms: identifier lifetime; freshness/replay rule; authentication construction; authenticator strength/truncation; key establishment/rotation/recovery; version authentication; maximum unauthenticated receiver work; extension mechanism; canonical policy mapping; and trust-level requirements for each enforcement action.

Consequently, this document intentionally does not prescribe a 4-byte, 8-byte or other fixed BLE payload size.

## 15. Traceability to Threat Model

- T01 -> SR-PRIV-*
- T02 -> SR-AUTH-004/005, SR-FRESH-*
- T03 -> SR-AUTH-* and SR-TRUST-*
- T04 -> SR-RELAY-* and SR-BIND-*
- T05 -> SR-BIND-*
- T06 -> SR-DOS-*
- T07 -> SR-PARSE-*
- T08 -> SR-VERS-*
- T09 -> SR-POL-*
- T10/T11 -> SR-ENF-* and SR-CONF-*
- T12 -> SR-SAFE-*
- T13 -> SR-AUTH-006/007
- T14/T15 -> SR-PRIV-006/007

## 16. Project position

This is a candidate engineering specification derived from the PPS Threat Model. It is not a claim that any manufacturer or standards body has adopted PPS. Existing Android Mobile Binding evidence remains T1-oriented transport evidence and does not by itself establish T2 visual subject binding.
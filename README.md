# PPS / PPS+ — Personal Privacy Signal for Physical AI

**Person-centric privacy preferences for smart glasses, AI cameras, wearables, robots and other Physical-AI systems.**

> **PPS means Personal Privacy Signal.** It is an experimental interoperability proposal and candidate engineering specification v0.1 for expressing a person's privacy preferences to nearby third-party Physical-AI systems.

## What PPS does

PPS explores a simple question: **How can a person communicate machine-readable privacy preferences to an AI-enabled device that is observing them?**

A compatible receiver can discover a local PPS preference, verify authenticity/freshness, determine the subject-binding state, resolve the applicable PPS+ policy and enforce that policy at the operating-system or firmware layer.

Examples of policy-relevant operations include identification, profiling, retention/upload and use for AI training.

PPS separates:

`preference expression → local discovery → authenticity/freshness → subject binding → policy resolution → trusted enforcement → user feedback/auditability`

## What PPS is NOT

PPS / PPS+ is **not**:

- a camera or microphone activity/status light;
- a red/green busy-light or workplace presence indicator;
- a Teams, Zoom or Google Meet status monitor;
- an ESP32, Arduino or Raspberry Pi signalling-light project;
- a Home Assistant, MQTT or smart-home presence protocol;
- a mechanism that reports whether the PPS user's own camera or microphone is active.

The signal expresses **the observed person's privacy preference toward third-party Physical-AI systems**. It does not merely display the operating state of the person's own devices.

## PPS and PPS+

**PPS** provides the local privacy-preference signalling and receiver architecture.

**PPS+** represents richer policy semantics so a compatible Physical-AI system can distinguish between operations and constraints instead of treating privacy as a single on/off state.

## Status and non-claims

This repository is the public external-review baseline for **PPS/PPS+ v0.1**.

It is **not a W3C standard**, is not endorsed by W3C, and does not claim adoption or enforcement by any commercial smart-glasses manufacturer.

A received Bluetooth/radio signal is **not proof of a person's visual identity**. Reliable camera-to-person subject binding remains an explicit research problem. The specification therefore keeps authenticity and subject-binding state separate and defines explicit UNBOUND and AMBIGUOUS states.

## Start here

- [v0.1 Freeze Manifest](docs/PPS-V0.1-FREEZE-MANIFEST.md)
- [Wire Protocol](spec/PPS-WIRE-PROTOCOL-v0.1.md)
- [Policy Mapping](spec/PPS-POLICY-MAPPING-v0.1.md)
- [Security Requirements](security/PPS-SECURITY-REQUIREMENTS-v0.1.md)
- [Threat Model](security/PPS-THREAT-MODEL-v0.1.md)
- [Manufacturer Integration Profile](docs/PPS-MANUFACTURER-INTEGRATION-PROFILE-v0.1.md)
- [Conformance Specification](conformance/PPS-CONFORMANCE-v0.1.md)
- [Test Vectors](conformance/PPS-TEST-VECTORS-v0.1.md)
- [Independent Validation Protocol](docs/review/PPS-INDEPENDENT-VALIDATION-PROTOCOL-v0.1.md)
- [Python Reference Receiver](receiver-kit/pps_reference_receiver.py)
- [Reference Receiver Tests](conformance/test_pps_reference_receiver.py)

## Core safety invariants

1. Radio presence alone MUST NOT be treated as camera-to-person identity.
2. Authenticity and subject-binding state MUST remain separate.
3. UNBOUND and AMBIGUOUS states MUST be explicit.
4. Uncertain binding MUST NOT be interpreted as permission for otherwise restricted identification, profiling, retention, upload or training.
5. Safety exceptions MUST be narrow, purpose-limited and auditable.
6. A receiver MUST NOT infer persistent identity merely from receipt of PPS.
7. Preference receipt, policy resolution and actual downstream enforcement are distinct claims.

## Independent review

Independent implementation, security review and measured T2 camera-to-person subject-binding validation are invited. Please use GitHub Issues for technical findings and interoperability questions.

## Project identity

**Protocol name:** PPS — Personal Privacy Signal  
**Policy layer:** PPS+  
**Domain:** Physical AI privacy preferences and policy enforcement  
**Developer:** TH Analytica / Thomas Hullin, Switzerland  
**Public project page:** https://th-analytica.com/pps-privacy-signal

## Licensing

See [LICENSE.md](LICENSE.md). Licensing does not imply W3C affiliation, endorsement or standards status.

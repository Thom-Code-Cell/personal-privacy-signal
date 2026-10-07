# PPS / PPS+ v0.1 Freeze Manifest

Status: Candidate engineering baseline  
Freeze date: 2026-10-07  
Project: TH Analytica PPS / PPS+

## Purpose

This manifest defines the PPS/PPS+ v0.1 review baseline. It is a candidate research and interoperability proposal for machine-readable privacy preferences and policy enforcement in Physical-AI environments. It is not a claim of adoption by any manufacturer, standards body, regulator or commercial smart-glasses platform.

## Normative review set

- `security/PPS-THREAT-MODEL-v0.1.md`
- `security/PPS-SECURITY-REQUIREMENTS-v0.1.md`
- `spec/PPS-WIRE-PROTOCOL-v0.1.md`
- `spec/PPS-POLICY-MAPPING-v0.1.md`
- `docs/PPS-MANUFACTURER-INTEGRATION-PROFILE-v0.1.md`
- `conformance/PPS-CONFORMANCE-v0.1.md`
- `conformance/PPS-TEST-VECTORS-v0.1.md`
- `receiver-kit/pps_reference_receiver.py`
- `conformance/test_pps_reference_receiver.py`

## Supporting evidence and handoff

- `docs/PPS-MANUFACTURER-HANDOFF-v0.1.md`
- `docs/PPS-RESEARCH-VALIDATION-BRIEF-v1.md`
- `docs/PPS-PHYSICAL-AI-STANDARDISATION-GAP-v1.md`
- `docs/PPS-LAB-MOBILE-BINDING.md`
- `docs/review/PPS-EXTERNAL-REVIEW-PACK.md`
- `docs/review/STANDARDISATION-VENUE-MATRIX.md`

## Architecture under review

Preference expression -> local discovery -> authenticity/freshness -> subject-binding state -> policy resolution -> trusted OS/firmware enforcement -> local processing controls -> user feedback/auditability.

## v0.1 safety invariants

1. Radio presence alone MUST NOT be treated as camera-to-person identity.
2. Authenticity and subject-binding state MUST remain separate.
3. UNBOUND and AMBIGUOUS states MUST be explicit.
4. Uncertain binding MUST NOT be interpreted as permission for otherwise restricted identification, profiling, retention, upload or training.
5. Safety exceptions MUST be narrow, purpose-limited and auditable.
6. A receiver MUST NOT infer persistent identity merely from receipt of PPS.
7. Enforcement claims MUST distinguish preference receipt, policy resolution and actual downstream enforcement.
8. PPS/PPS+ preference expression and legal enforceability are separate questions.

## Explicitly not proven at freeze

- universal third-party enforcement
- reliable camera-to-person subject binding
- UWB ranging in the current field setup
- resistance to all spoofing, relay and Sybil attacks
- legal effect of the signal
- adoption by a manufacturer or standards body

## External validation gate

The baseline MUST NOT be described as production-ready until at least:

- one independent security/architecture review is completed;
- a second implementation reproduces the normative test vectors;
- hostile-radio/resource-abuse testing is measured and documented;
- T2 camera-to-person subject binding is experimentally validated at defined confidence/error thresholds;
- an integration reviewer can implement the receiver/enforcement sequence without project-author clarification.

## Change control

Changes to normative v0.1 artifacts after this freeze should be made through reviewable pull requests and should identify whether they are editorial, compatible clarification, or protocol/policy breaking changes.

## Immediate review questions

1. Are the binding states sufficient for safe enforcement?
2. Can a manufacturer expose the proposed enforcement hooks before capture, identity inference, profiling, retention/upload and training?
3. Are authenticity/freshness and anti-replay requirements implementable on constrained wearable hardware?
4. Which additional abuse cases must be added before a public interoperability pilot?
5. Can an independent implementation reproduce the expected conformance results?

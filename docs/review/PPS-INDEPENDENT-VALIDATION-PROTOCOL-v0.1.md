# PPS / PPS+ Independent Validation Protocol v0.1

Status: External validation protocol  
Date: 2026-10-07

## Objective

Determine whether an independent implementer can reproduce the PPS/PPS+ v0.1 receiver and enforcement model from repository documentation without project-author clarification.

## Reviewer inputs

Use only the frozen v0.1 artifacts listed in `docs/PPS-V0.1-FREEZE-MANIFEST.md`.

## Required validation tracks

### V1 — Specification comprehension
Reviewer documents the interpreted sequence from discovery through authenticity/freshness, binding, policy resolution and enforcement. Any ambiguity is recorded before implementation.

### V2 — Independent receiver
Implement a receiver independently of `receiver-kit/pps_reference_receiver.py`. Run the published conformance test vectors and record pass/fail plus deviations.

### V3 — Security review
Review replay, spoofing, relay, Sybil/flooding, parser/resource exhaustion, downgrade, policy-conflict and safety-exception behavior. Confirm that authenticity is not conflated with subject binding.

### V4 — T2 subject-binding experiment
Test camera-to-person binding separately from BLE policy transport. At minimum record:
- number of people and simultaneous PPS senders;
- distance and movement;
- occlusion and crossing subjects;
- false-bind, missed-bind and ambiguous rates;
- confidence threshold and evidence used;
- behavior when evidence is insufficient.

BLE/RSSI alone MUST NOT be reported as proof of visual identity.

### V5 — Enforcement integration
Demonstrate at least one restricted operation being denied after a HIGH-confidence binding and policy resolution. Candidate operations: identification, profiling, retention/upload or training. Also demonstrate safe behavior for UNBOUND and AMBIGUOUS states.

### V6 — Abuse/resource testing
Measure receiver behavior under duplicate advertisements, rapid rotation, malformed frames and many simultaneous senders. Record CPU/memory impact, dropped inputs and fail-safe behavior.

## Pass criteria for external-review milestone

The milestone passes only if:
1. an independent receiver reproduces the normative vectors;
2. no critical architecture ambiguity prevents implementation;
3. security findings are documented and triaged;
4. T2 binding results include measured error/ambiguity rates, not anecdotal success;
5. enforcement behavior is demonstrated for HIGH-confidence, UNBOUND and AMBIGUOUS states;
6. no claim exceeds the evidence collected.

Passing this milestone does not establish legal effect, universal interoperability, standards adoption or production readiness.

## Reviewer report template

- Reviewer / organization:
- Date:
- Implementation language/platform:
- Documents used:
- Clarification requested from project author: YES/NO
- Conformance vector result:
- Security findings:
- T2 binding setup:
- False-bind rate:
- Missed-bind rate:
- Ambiguous rate:
- Enforcement demonstration:
- Abuse/resource results:
- Blocking issues:
- Recommendation: PASS / PASS WITH FINDINGS / FAIL

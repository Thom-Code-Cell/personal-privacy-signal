# PPS Manufacturer Integration Profile v0.1

Status: Candidate integration profile
Date: 2026-10-06

Reference sequence: PPS discovery -> authenticity/freshness -> subject-binding state -> policy resolution -> OS/firmware enforcement -> local processing controls -> user feedback -> auditable safety exception.

Required states are UNSEEN, DISCOVERED_UNVERIFIED, AUTHENTICATED_UNBOUND, BOUND_LOW_CONFIDENCE, BOUND_HIGH_CONFIDENCE, AMBIGUOUS and EXPIRED/DISCONNECTED.

T0 is advisory discovery. T1 is authenticated policy/session with freshness but no visual attribution. T2 is T1 plus binding evidence satisfying a documented binding profile. Radio proximity alone MUST NOT turn AUTHENTICATED_UNBOUND into BOUND.

A manufacturer MAY combine RSSI trajectory, AoA, UWB/ToF, depth, visual geometry or other privacy-preserving local evidence. No individual sensor is mandatory in v0.1. Multiple plausible mappings resolve to AMBIGUOUS.

Each enforcement domain is declared ENFORCED, ADVISORY or UNSUPPORTED: capture, identification, profiling, emotion inference, embedding/persistent tracking representation, retention, cloud upload, training/secondary learning, commercial secondary use and user feedback. A generic PPS-compatible claim is insufficient without this declaration.

Before protected processing: resolve applicable policies -> resolve binding -> calculate effective restrictions -> gate protected downstream operations. Derived data inherits restrictions unless a future normative policy says otherwise.

Safety handling is separate from normal policy. Reason, scope and duration are bounded; normal policy resumes automatically; audit is data-minimised.

Conceptual adapter operations: observe discovery; upgrade trust; resolve subject binding; resolve policy; enforce; show status; begin/end safety exception; emit conformance evidence. These are conceptual integration points, not claims about proprietary vendor APIs.

This profile is ready for engineering review and prototype integration. It is not a claim of manufacturer adoption or standards certification.

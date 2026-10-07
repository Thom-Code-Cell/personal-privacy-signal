# PPS+ Policy Mapping v0.1 — Candidate

Status: Candidate
Date: 2026-10-06

Transport flags are a compact projection of richer PPS+ semantics and are versioned independently.

0x0001 capture DENY
0x0002 identification DENY
0x0004 profiling DENY
0x0008 emotion inference DENY
0x0010 retention DENY
0x0020 cloud upload DENY
0x0040 training DENY
0x0080 commercial use DENY

User alerts, safety processing, emergency escalation and emergency-only disclosure remain in the richer semantic document; they are not compressed into discovery bits because exception semantics require explicit resolution and audit.

For T1, semantic policy MUST be serialized deterministically before hashing. The Android experiment uses canonical policy JSON plus SHA-256. Exact cross-language canonicalization remains a production-freeze item.

An unset DENY bit is not affirmative consent. A stricter applicable place policy may further restrict a personal policy under the current candidate conflict model.

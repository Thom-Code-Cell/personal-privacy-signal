# PPS Test Vectors v0.1

Status: Candidate
Date: 2026-10-06

These vectors test only the T0 discovery parser.

| ID | Input (hex) | Expected |
|---|---|---|
| V001 | 01010100e7a1a2a3a4a5a6a7a812340b00 | accept T0; flags 0x00e7 |
| V002 | 01010100e7a1a2a3a4a5a6a7a812340b | reject invalid length |
| V003 | 02010100e7a1a2a3a4a5a6a7a812340b00 | reject unsupported wire version |
| V004 | 01020100e7a1a2a3a4a5a6a7a812340b00 | reject unsupported frame type |
| V005 | 01010100e7a1a2a3a4a5a6a7a812340b01 | reject nonzero reserved byte |
| V006 | 0101010000b1b2b3b4b5b6b7b812350100 | accept T0; zero DENY flags MUST NOT be described as affirmative consent |

Future T1 vectors must include session nonce mismatch, policy digest mismatch, stale session and rejected authentication. Future T2 vectors must include unbound, ambiguous, low-confidence and high-confidence binding cases.

## Additive semantic regression vectors (2026-10-21)

[Eight literal single-bit vectors](policy-meaning-vectors.json) transcribe the
existing wire/policy mapping into separate expected restriction names, without
importing parser constants. The [tests](test_policy_meanings.py) check exact
meanings, all combinations and structured fields; the
[mutation check](../tools/check_policy_mutations.py) must detect all 28 pairwise
meaning swaps. No wire semantics, protocol version or trust level is changed.
These are spec-derived AI-assisted vectors, not an independent implementation.

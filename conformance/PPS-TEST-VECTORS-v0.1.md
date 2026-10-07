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

# PPS+ Purpose Guard – Candidate extension proposal

**Revision:** 0.2-draft (19 November 2026)  
**Status:** PROPOSED / NON-NORMATIVE / NOT IMPLEMENTED  
**Reference:** PPS+ candidate policy mapping v0.1, SR-ENF-*, SR-SAFE-*, SR-BIND-*  
**Change control:** This proposal DOES NOT modify the frozen v0.1 wire format, flag mapping, trust levels, existing tests or manufacturer conformance claims.

## Problem statement

An inference initially performed for immediate physical safety can create person-presence events, location/time metadata or derived embeddings. If the receiving application can silently relay those events to identification, profiling, targeting, remote action or cloud/training pipelines, a narrow safety allowance becomes an uncontrolled purpose bypass. Model refusals and prompt framing alone are not an enforcement boundary. No PPS beacon is required to benefit from applicable baseline protections.

## Proposed requirements for independent review

- **PG-001** – A cooperating integrator MUST apply its own baseline legal/safety restrictions irrespective of PPS discovery; absence of PPS MUST NOT be affirmative consent.
- **PG-002** – A `safety_inference` allowance, where independently applicable, SHALL be bound to a specific purpose, limited data schema, local processing scope and expiry. It MUST NOT confer permission to identify, profile, upload, retain, train on or act harmfully on a person.
- **PG-003** – Each downstream sink (derived metadata, embeddings, persistent storage, cloud API, notification, actuator) requires a fresh authorization decision tied to the specific data and purpose; downstream data inherits restrictions.
- **PG-004** – User/prompt/application text such as “simulation,” “game,” “research,” or role play MUST NOT reduce an independently established protection level or create a safety exception.
- **PG-005** – A safety/emergency exception, where authorized, MUST remain bounded by trusted trigger evidence, permitted operations, minimized data, expiration, audit and automatic restoration. An unauthenticated radio advertisement MUST NOT be an override token.
- **PG-006** – A system MUST distinguish `ADVISORY`, `POLICY_RESOLVED`, `ENFORCED_AT_SINK`, and `INDEPENDENTLY_VALIDATED` claims, reporting unsupported domains separately. Policy evaluation itself is not enforcement.
- **PG-007** – Binding state remains separate from authentication; no automatic attribution from BLE proximity or one person's preferences to another subject. Ambiguity MUST NOT cause permissive upgrades.
- **PG-008** – The protection design SHOULD support people with no emitting device and SHOULD NOT make a publicly observable beacon a prerequisite for baseline protections.
- **PG-009** – Implementations MUST avoid unauthenticated arbitrary device shutdowns; safe mechanical operation and privacy-restrictive processing need separately defined failure modes and tests.
- **PG-010** – This proposed profile concerns defensive governance and safety. It MUST NOT add tooling for recognizing, locating, prioritizing or engaging humans as targets for harm.

`MUST` here expresses proposed strength for design review only. These clauses are **not** adopted normative PPS v0.1 requirements.

## Decision matrix, illustrative only

| Condition | Privacy interpretation | System / action boundary |
|---|---|---|
| No PPS | Not consent | Baseline rules apply; safe operation independent of signal |
| Valid `DENY_ID` applied to a bound subject | Identification prohibited in applicable policy | Block at actual sink, not simply warn in UI |
| `UNBOUND` or `AMBIGUOUS` | No positive release | No guessed person match; report uncertainty |
| `safety_inference` limited allowance | Only named minimum safety output in scope | No general reuse of event or derived data |
| “Game” / “Simulation” request | Not a permission grant | Same independent authorization boundary |
| Unverified emergency claim | Not an override | Ignore claim for escalation privilege |
| Trusted bounded emergency with separate approval | Minimized exception | Deadline, audit, independent constraints, automatic restoration |
| Unsupported or hostile third-party device | Protection not verifiable | Advisory/not protected; never promise enforcement |

## Compatibility and review tasks

1. No new BLE bits or reserved values. Discuss richer PPS+ semantic versioning independently.
2. Produce formal state × purpose × operation × trust × exception decision tables before any executable resolver.
3. Specify trusted enforcement points in OS/firmware, plugin and cloud; independently test secondary data paths and exceptions.
4. Run `P7` synthetic tests first; real hardware and people only after explicit safety, privacy and ethics authorization.
5. Confirm source provenance, applicability across jurisdictions, accessibility, denial-of-service behavior and non-emitting-user baseline.

## External evidence (not a PPS performance result)

- Vals AI (2026-11-17): https://www.vals.ai/blogs/autonomous-warfare
- ICRC (2026-10-08): https://www.icrc.org/en/article/faq-autonomous-weapon-systems

No manufacturer endorsement, T1/T2 implementation, autonomous-harm prevention or legal guarantee is claimed.

# Physical Place website integration: PPS+ research template

**Status: INFORMATIVE / NOT A LIVE VENUE RULE / NOT ENFORCEMENT.** 2026-11-19.

This guide is for **TH Analytica website-optimisation commissions** covering
physical locations. Venue-specific files are created, validated with and approved
by the operator, then integrated into that operator's website only after
explicit publication approval. This generic template does not authorize changes
on any existing customer website.

## Goal and separation of layers

| Layer | Can TH Analytica prepare as website work? | What it proves |
|---|---|---|
| Public editorial notice, accessible human-readable venue rules | Yes, with operator confirmation | Public statement of venue preference |
| Machine-readable venue page, JSON-LD and link to a versioned local rule file | Yes, with operator confirmation | Discoverable claim, not its authenticity or spatial scope |
| Operator authority, signed rule, expiry/revocation and verifiable boundary | Candidate design only; requires operator and independent validation | Cannot be inferred from HTTPS or JSON alone |
| Camera/AI headset enforcement, nearby-person attribution | No, independent supported system required | Must be measured on specific receiver and firmware |

## Proposed website deliverables (per engagement, never blanket-published)

1. Human-readable accessible policies including language, scope, exceptions,
   site rules and last-review date.
2. A generic **informative** JSON file derived from
   [`conformance/fixtures/p8-venue-policy-template.json`](../conformance/fixtures/p8-venue-policy-template.json),
   with operator-reviewed text and **no claim of verified signature or enforcement**.
3. Optional `schema.org/Place`-type structured data for the place's public facts,
   using established schema fields only. PPS-specific semantics remain in a
   separately labelled proposed document, not falsely represented as standardized
   Schema.org properties.
4. Accessible entry signage and alternative for visitors without phones.
5. Owner approval and maintenance procedure; accurate archival revision history
   where appropriate; review after zone or rules change.

## Threats and boundaries

- Website publication is not a geofence. GPS, BLE and DNS/HTTPS cannot prove
  physical applicability to an observed person. Walls and adjacent rooms create
  ambiguity. An unknown rule must never be reported as verified local authority.
- A phone's biometric unlock proves local authentication, not legal identity,
  spatial attribution or consent to capture by third parties.
- The prototype venue JSON is intentionally unsigned and uses `example.invalid`.
  Do not publish it as a functioning protection zone; obtain operator authority,
  expiry and revocation design before real implementation.
- No static individual identifier, face template, person-specific location feed,
  unrestricted safety override or continuous monitoring is needed for the example.
- Connected devices may ignore website metadata completely. Published material
  must not promise that AI glasses, cameras or drones will discover or obey it.

## Suggested acceptance checklist for a customer website

- [ ] Operator verifies location identity, boundaries and all statements.
- [ ] Human-readable rules are current, accessible and multilingual if needed.
- [ ] Privacy/legal review identifies responsible parties and data flows.
- [ ] No personal biometric or precise location stream is included.
- [ ] Machine-readable example explicitly states ADVISORY/NOT_VERIFIED.
- [ ] Search/structured-data validation is not passed off as device compliance.
- [ ] Owner explicitly approves deployment and maintenance responsibility.

Research questions and real-device enforcement belong to independent volunteer
and manufacturer work, not to the website deliverable.

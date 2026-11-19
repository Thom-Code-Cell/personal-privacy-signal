# PPS/PPS+ Community Research Scope — 2026-11-19

**Status: INFORMATIVE / COMMUNITY RESEARCH / NOT VALIDATED.** This is a workflow
clarification, not a change to frozen v0.1 specifications or to the existing license.

## Roles and responsibility

- **TH Analytica:** initiates PPS/PPS+ research concepts, threat models, candidate
  specifications, machine-readable examples and documentation. Maintains the
  public discussion, provenance and evidence boundaries. May run bounded static
  and synthetic checks on contributed source to avoid publishing broken examples;
  these checks are **not** field validation.
- **Independent volunteers, universities, integrators and manufacturers:** may
  implement, reproduce, falsify and benchmark candidate ideas under applicable
  law and their own safety/ethics approvals. No outside organisation is assumed
  to have agreed to test or adopt the proposals.
- **Physical-location website work:** when separately commissioned, TH Analytica
  can create site-specific digital-detox/venue policy files and site metadata for
  a physical location. The venue operator must approve its contents, zone scope,
  authority, maintenance and publication. Any on-device enforcement requires
  independent compatible receiver and OS/firmware integration.

## Non-goals for TH Analytica's PPS research workflow

No mandatory in-house Android app, biometric registry, device manufacturing,
Vuzix/other hardware tests, human-subject experiment, surveillance, persistent
location tracking or autonomous targeting capability. No claims of camera blocking,
legal immunity, real-world protection, standards recognition or manufacturer
adoption from website files, BLE messages, parsing, simulations or proposed
rules alone.

## Evidence and safety requirements for contributors

1. Preserve the v0.1 freeze; propose changes in versioned informative documents.
2. Keep personal biometrics, precise location traces, participant data, private
   contact details, credentials and proprietary SDKs out of public Git history.
3. Separate syntactic parsing, simulated policy resolution, cryptographic
   verification, person binding, spatial applicability and actual enforcement.
4. Unregistered people and those without smartphones retain all legal and
   fundamental protection; lack of signal/identity must never imply consent or
   permission to harm.
5. Report limitations and failures, with hardware-specific claims backed by an
   independent reproducible protocol, explicit scope and suitable ethical review.
6. Submit reproducible examples and security findings through GitHub contribution
   and private vulnerability disclosure routes already established.

## Review flow

Issue/Discussion -> scoped non-normative proposal -> synthetic fixtures where
appropriate -> independent review/measurement by willing third parties ->
explicit maintainer decision for any merge/spec revision. Draft PR publication
alone is neither merge nor validation. No automatic outreach, release or deployment.

## Proposals covered

- [P7 Purpose Guard](../../SPECIFICATIONS/PROPOSAL-PPS-PLUS-PURPOSE-GUARD-v0.2.md)
- [P8 Identity & Location](../../SPECIFICATIONS/PROPOSAL-PPS-PLUS-IDENTITY-LOCATION-v0.2.md)
- [P8 Venue/mobile adapter interface](../../SPECIFICATIONS/P8-MOBILE-AND-VENUE-ADAPTER-CONTRACT.md)
- [Website integration templates](../PPS-PHYSICAL-PLACE-WEBSITE-INTEGRATION-GUIDE.md)

These are optional research proposals for review, not extensions that devices
must implement under v0.1.

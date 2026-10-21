# Discussion guide, FAQ and sources

**Can I independently research PPS?** Yes, study and reuse the published baseline
under its existing license conditions. TH Analytica remains the initiator, not an
exclusive research gatekeeper. Future license choices do not silently replace those rights.

**Does PPS stop cameras?** No. A preference packet cannot stop an uncooperative
camera. A hypothetical cooperating OS/firmware integration needs separate evidence.
No signal, zero flags, failed binding or missing phone means no consent inference.

**Is it a standard or a manufacturer product?** No. v0.1 is a candidate baseline;
research-package v1.0 is documentation, not protocol v1.0 or a release certification.

**What is reproducible now?** Local parser tests and negative vectors. T0 does not
authenticate identity/freshness. Real Android/Vuzix/other-wearable validation is
not established by this repository's tests. See Issue #1 for scoped user reports;
these are separate evidence classes, not laboratory certification.

**How do PPS and PPS+ differ?** PPS is the signalling/receiver architecture;
PPS+ describes richer policy semantics. Radio reception does not bind a visible
person or establish a venue operator's authority. Cryptography alone cannot prove
physical location. See the security requirements and research protocols.

**Where should I post?** Discussions for questions and design alternatives;
Issues for actionable research/bugs; PRs for reviewable changes. If Discussions
are unavailable, use a research-question issue. Security: private channel in SECURITY.
Keep personal or confidential information out of every public channel.

**Can I call an NC variant open source?** No, a commercial-use restriction conflicts
with OSI's field-of-endeavour rule. The license decision brief distinguishes options.

Primary project sources:
- [Wire protocol](../../spec/PPS-WIRE-PROTOCOL-v0.1.md)
- [Policy mapping](../../spec/PPS-POLICY-MAPPING-v0.1.md)
- [Security requirements](../../security/PPS-SECURITY-REQUIREMENTS-v0.1.md)
- [Threat model](../../security/PPS-THREAT-MODEL-v0.1.md)
- [Freeze manifest](../PPS-V0.1-FREEZE-MANIFEST.md) (six referenced supporting files absent)
- [Research agenda and source references](../research-v1/02-agenda.md)
- [License sources and decision](LICENSE-DECISION.md)

Vendor feasibility sources are recorded in the [Vuzix plan](../research-v1/04-vuzix.md)
and Issue #1. Recheck current SDK terms before use. Referencing these sources is
not an endorsement or permission to copy vendor materials.

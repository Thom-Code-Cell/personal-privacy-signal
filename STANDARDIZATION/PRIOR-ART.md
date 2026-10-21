# Prior-art research ledger

Status: OPEN RESEARCH TASK, not novelty, patent clearance or worldwide priority.
Search dated primary papers, specifications, code and patent publications for
privacy preferences, bystander privacy, consent/opt-out, BLE discovery, visual/QR
notices and subject binding. Record queries, databases, access dates and exclusions.

| Reference/revision/date | Problem/transport | Overlap/difference | Rights/evidence | Open questions/reviewer |
|---|---|---|---|---|
| Repository v0.1; see ORIGIN.md | local preference discovery | comparison baseline, not novelty proof | LICENSE.md | wider comparison pending |
| [DNT, W3C Note 2019-01-17](https://www.w3.org/TR/2019/NOTE-tracking-dnt-20190117/), editors Roy T. Fielding and David Singer | HTTP tracking preference and receiver status | shared preference-versus-compliance distinction; not camera-to-person binding or BLE discovery | primary Note read; no specification text/code imported | do not transfer HTTP semantics or claim a W3C Recommendation |
| [Global Privacy Control draft](https://w3c.github.io/gpc/), accessed 2026-10-21; [source snapshot](https://github.com/w3c/gpc/tree/09013acfed7820dc967489514a156e2ced827289) | HTTP/DOM do-not-sell-or-share preference | shared machine-readable restriction; web scope rather than physical subject binding | primary draft read; no implementation imported | no automatic legal effect for PPS inferred; detailed semantic mapping pending |
| [BLINDSPOT v1](https://arxiv.org/abs/2512.14746v1), Jad Al Aaraj and Athina Markopoulou, 2025-12-12 | bystander privacy signals for camera devices | authors describe gesture, visible-light and UWB modalities plus geometric origin checks; directly relevant to PPS discovery/binding questions | abstract/version history read; preprint results are authors' reports, not reproduced here | full technical comparison, assumptions, limitations and independent replication pending |

Add verified primary references before comparative claims. Distinguish publication,
patent priority claims, grants and present legal scope. Link rather than copying
restricted standards/SDKs. Patent counsel and freedom-to-operate are separate.
A no-hit search proves no absence of prior art. Cite competing work and criticism.

## Bounded first search — 2026-10-21

Web-search queries: `site.w3.org TR tracking dnt tracking preference expression`;
`site.globalprivacycontrol.github.io gpc specification`;
`site.usenix.org bystander privacy wearable cameras privacy beacon`;
`site.rfc-editor.org RFC 6973 privacy considerations unlinkability`.
Selection: directly relevant primary protocol pages and the authors' versioned
preprint; excluded secondary summaries and social posts from comparison evidence.
The search was English-language, web-index bounded and not exhaustive; no patent
database search or citation-chain review was completed. RFC 6973 full-text retrieval
returned HTTP 429, so no detailed claim is based on that unavailable text.

This comparison does not establish novelty, precedence of every underlying idea,
patent scope, freedom to operate or interchangeability. In particular, BLINDSPOT's
earlier publication requires substantive comparison before broad originality claims.
Thomas Hullin remains the documented initiator of this PPS project; independent
earlier authors retain their own credit. Source licensing was not used as permission
to import any paper, standard text or code.

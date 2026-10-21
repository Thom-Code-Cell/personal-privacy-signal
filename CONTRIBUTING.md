# Contributing to PPS / PPS+

Developers, universities, hardware makers and interested individuals can propose
independent implementations, replications, translations, accessibility reviews
and negative findings. No affiliation, purchase or TH Analytica approval is
required to study the published material under its existing terms.

1. Read [README](README.md), [rights inventory](docs/community/RIGHTS-REVIEW.md)
   and [governance](GOVERNANCE.md). Check existing issues and Draft PR #2.
2. Open a research question or bug report with a small, bounded proposal.
   Use [SECURITY.md](SECURITY.md) for vulnerabilities, never public exploit data.
3. Fork/branch; keep changes focused. Describe normative compatibility and cite
   the exact specification revision. Preserve copyright and third-party notices.
4. Run the README checks and the documentation validator. Provide commands,
   versions, result and limitations; failures and NOT_MEASURED are useful results.
5. Submit a PR with the checklist. Use synthetic fixtures and aggregate results
   only. No private correspondence, participant records, faces, voices, addresses,
   persistent radio identifiers, device serials, secrets or unpublished SDK code.

Existing LICENSE.md remains applicable; this guide adds no CLA, assignment,
patent promise or future relicensing consent. Confirm authority to contribute
(including employer/university rights) and list origin/license for imported work.
If rights are unclear, propose the idea without uploading restricted material.
Substantive contributions need provenance review before merge; a PR is not a
certification. No mandatory real-name sign-off; GitHub noreply is recommended.

Python 3.11 or later is the proposed test baseline. CI runs 3.11 and 3.12.
Hardware claims require the [replication record](docs/community/REPLICATION.md)
and existing P1–P6 protocols. A mock or parser test cannot pass a device gate.

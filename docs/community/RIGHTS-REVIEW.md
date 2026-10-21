# Rights, privacy and repository inspection — 2026-10-21

Scope: main 17c278d48e6cf74ee81e0a23f80c3fa28c25b5f8 and Draft #2
2db356552e62581f46cacb9d770760f4de76d782 before this addition. Only open PR: #2;
Issue #1 and its five comments inspected. Previous inventory is historical.

| Area | Observed | Limit/action |
|---|---|---|
| License | LICENSE.md names W3C Software and Document License 2023; TH Analytica/Thomas Hullin copyright | preserve unchanged; see decision brief |
| Ownership/IP | no separate patent grant, patent inventory, CLA, NOTICE or third-party ledger found | authorship statements are not chain-of-title proof; verify before relicensing |
| Runtime | Python dataclasses, no external runtime import | no manufacturer SDK or private website source copied |
| Development tools | Ruff 0.14.1 and Bandit 1.8.6 pinned | independently distributed tools, not relicensed here; future dependencies require license review |
| Protocol | candidate 17-byte T0 parser, separate policy/security specs | no signatures, replay defence, person binding or hardware enforcement implemented |
| Privacy | P1–P6, consent template and threat requirements already exist | raw data and signed consent must stay outside Git; templates are not ethics approval |
| Policies | community/contribution/security/governance absent before this addition | this PR adds these processes without assigning rights |
| Evidence | Android lab references lack runnable evidence here; six supporting freeze-manifest documents absent | cannot re-certify external claims; preserve historical manifest |
| GitHub | admin/push/maintain permission; Actions enabled; secret scanning and push protection enabled | scan results are snapshots, not exhaustive assurance |

No copied SDK, vendor logo, research participant dataset or private correspondence
was identified in the inspected tree. External links and named prospective contacts
are references, not licensed third-party code or partnerships. This is a bounded
repository review, not legal clearance, a trademark search or a patent opinion.

New files in this PR are project documentation/templates and CI configuration;
no license file, normative wire layout, receiver implementation or dependency
version is changed. Existing repository terms remain; no additional rights grant.
Future imports must record source, exact revision, author, license, notices,
modifications and compatibility before acceptance. Do not copy restricted SDK
examples, external standards text or private implementations merely because linked.

## Repository settings checked/changed within this task

Discussions and private vulnerability reporting were disabled; both were enabled
using verified admin permission. Secret scanning and push protection were already
enabled and retained; open secret alerts and repository advisories each returned
zero at inspection. No code-scanning clearance is claimed. Main branch protection
API returned 404 (branch not protected); no protection or permissions were changed.
New read-only GitHub Actions checks cover Python 3.11/3.12 and checksum-verified
Gitleaks history scanning; final-head run results are recorded in the handoff.

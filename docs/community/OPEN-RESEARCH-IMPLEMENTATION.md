# International open research infrastructure — 2026-10-21

Extends existing Draft PR #2 on research/pps-validation-v1; no competing PR.
The earlier chat "PPS/PPS+ Forschungsinitiative öffnen" was completed, not running,
at inspection. Its community files and CI are preserved. Only PR #2 was open.
Main inspected at 17c278d48e6cf74ee81e0a23f80c3fa28c25b5f8; draft baseline at
e716ccf2f38fe5c5048f895860114bedee5403b4. Historical inspection records retain
their original scope; this file records the additional scope.

Adds origin evidence, CFF metadata, AI guidance, funding possibilities, specification
proposals/conformance review, experiment templates and standardization/publication
infrastructure. Reuses existing normative specifications, P1–P6 and replication
records. Adds hardware/standards issue forms and direct private security routing.
No separate public vulnerability form invites sensitive disclosures.

## Rights and publication review

LICENSE.md is unchanged. Its existing W3C 2023 notice covers the public v0.1
materials and refers to terms permitting use for any purpose subject to conditions.
These additions introduce no alternate license, assignment or patent commitment.
The prior rights inventory remains bounded: complete ownership, patent clearance
and absent external evidence are not established. No SDK, participant data or
third-party standards text was imported. Standards/process descriptions are
original summaries with primary links, checked 2026-10-21. Git-based origin is
explicitly distinguished from independently certified priority.

Public visibility alone is not open-source licensing. Existing terms remain the
basis for permitted reuse; any future license migration requires explicit approval
and rights review. No commercial/noncommercial decision is made here.

Discussions, private vulnerability reporting, secret scanning and push protection
were already enabled and retained. Private reporting returned enabled; open
secret alerts returned zero at inspection. No new setting or moderation category
was required. No release, DOI deposit, outreach, paid service or merge is performed.

## Local validation before publication

- 10 existing unit tests: PASS.
- Ruff lint and format; Bandit; Python compilation: PASS.
- Expanded documentation checks: headings, encoding, final newlines, fences,
  whitespace, local links and original license preservation: PASS.
- CITATION.cff: cffconvert 2.0.0 validates against CFF 1.2.0 schema: PASS.
- All six issue/config YAML files parse successfully: PASS.
- git diff --check; Gitleaks 8.24.3 working tree and history: PASS, no secret findings.

CI runs the existing Python 3.11/3.12 and Gitleaks checks on the pushed head;
actual final-head remote results must be read from the PR, not inferred here.
CFF schema validation and YAML parsing above are local checks, not new CI jobs.
No physical-device, authenticated profile, subject-binding or enforcement
validation is established by these documentation changes. Independent review and
the evidence-gated roadmap remain open.

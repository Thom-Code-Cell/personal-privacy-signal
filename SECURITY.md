# Security and responsible disclosure

PPS/PPS+ v0.1 is experimental. No supported production release or security SLA
exists. The reference receiver parses T0 discovery bytes only; it authenticates
neither sender nor freshness and cannot bind a person or prevent recording.

Private vulnerability reporting is enabled (checked 2026-10-21). Use the
repository Security tab → **Report a vulnerability**:
https://github.com/Thom-Code-Cell/personal-privacy-signal/security/advisories/new
Do not put vulnerabilities, working exploits, secrets or participant data in a
public issue. If the private form is inaccessible, keep details private and
open only a detail-free request for a safe reporting route. No private project
email or monitored emergency hotline is currently designated.

A report should contain the affected commit, threat boundary, minimal synthetic
reproduction, expected/observed behaviour, impact and suggested mitigation.
Do not test other people's devices, networks or services, or record bystanders.
No bounty, legal safe harbour, deadline or permission to access systems is granted.
Maintainer target: acknowledge within 7 days and provide an initial assessment
within 30 days, best effort only. Agree coordinated disclosure timing case by
case; offer attribution only with the reporter's consent.

If a secret or personal record is accidentally published: stop dissemination,
revoke affected credentials, notify the owner privately and assess Git history,
CI artifacts and forks. Deleting a file alone does not erase public copies.
Security fixes require regression evidence; never equate a clean scanner with
secure radio, cryptography, hardware or privacy compliance.

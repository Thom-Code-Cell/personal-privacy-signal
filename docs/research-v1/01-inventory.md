# Bestandsaufnahme · 21.10.2026

## Repository und laufende Arbeiten

Geprüfte Basis: `Thom-Code-Cell/personal-privacy-signal`, öffentlich,
`main` bei `17c278d48e6cf74ee81e0a23f80c3fa28c25b5f8`.
GitHub-Branchliste: nur main; PR-Liste aller Zustände: leer; Issue-Liste: ein offenes
[Issue #1](https://github.com/Thom-Code-Cell/personal-privacy-signal/issues/1)
zur echten Wearable-Hinweisintegration. Frischer isolierter Clone, vor Änderung sauber.
Andere lokale Checkouts wurden nicht verändert; kein vollständiges Inventar fremder
lokaler Stashes behauptet. Neuer Branch: `research/pps-validation-v1`.

## Architektur und Lücken

Die README trennt Präferenz → Discovery → Authentizität/Frische → Subject Binding →
Policy → OS/Firmware-Enforcement → Rückmeldung. Implementiert ist hier allein ein
17-Byte-Python-T0-Parser mit vier ursprünglichen Unit-Tests. Kein Bluetooth-Stack,
keine Authentifizierung, keine Frischeprüfung, keine Kamera-/Policy-Enforcement-Pipeline,
keine App, keine Runtime-Fremdabhängigkeiten, kein CI-/Lint-/Buildsystem vorhanden.

Gelesen: README, Wire Protocol, Policy Mapping, Security Requirements, Threat Model,
Manufacturer Integration Profile, Freeze Manifest, Conformance, Test Vectors und
Independent Validation Protocol. Die dort genannten Android-Mobile-Binding-Ergebnisse
liegen hier nicht als ausführbare APK/Logs vor und werden nicht nachzertifiziert.

Das Freeze Manifest nennt sechs ergänzende Dokumente, die in diesem Repository fehlen:
Manufacturer Handoff, Research Validation Brief, Standardisation Gap, Lab Mobile Binding,
External Review Pack und Standardisation Venue Matrix. Dieses Paket schliesst die
Forschungsplanungslücke, behauptet aber keine Rekonstruktion jener Originale.

## Separater TH-Analytica-Stand

[PR #103](https://github.com/Thom-Code-Cell/th-analytica-2025/pull/103) ist offen,
geprüfter Head `fedb87ff436ff1e0442ef27048bfad44ea7f2d48`.
Bauminventar belegt PPS+-Policy-Reader, Session-/Discovery-Module und Tests sowie
`research/pps-multimodal`. Dessen README beschreibt kurzlebige unsignierte Marker,
synthetisches PCM und QR-Rastertests ausdrücklich ohne Geräte-Enforcement.
Diese Quelltexte wurden nicht in dieses Repository kopiert und deren Tests hier nicht
erneut ausgeführt. [PR #104](https://github.com/Thom-Code-Cell/th-analytica-2025/pull/104)
ist die separate offene Dependency-Sicherheitsarbeit. Keine Änderungen an beiden PRs.
Weitere offene Website-PRs (54, 62, 70, 94, 95, 98, 99, 105, 106) bleiben unberührt.

## Sicherheitsbefunde

| Befund | Evidenz/Behandlung | Restgrenze |
|---|---|---|
| Unbekannte policy_version akzeptiert | Parserkontrolle ergänzt | absichtlich strengere Annahme |
| Reservierte Policy-/Capability-Bits akzeptiert | explizite Ablehnung ergänzt | künftige Version braucht neue Regeln |
| T0 enthält keine Signatur/Replayprüfung | by design, kein T1 behaupten | Produktblocker |
| BLE/RSSI beweist weder Person noch Raum | bestehende Invarianten, neue Protokolle | T2 offen |
| Code-Scanning API 404 „no analysis found“ | keine Analyse verfügbar | kein Clean-Befund |
| Dependabot API 403, Alerts disabled | nicht aktiviert/verändert | nicht vollständig prüfbar |
| Secret-Scanning API liefert [] | keine gemeldeten Alerts im Abruf | kein vollständiger Secret-Scan-Beweis |

Vorhandene Threat-Model-Risiken umfassen Tracking, Replay, Spoofing, Relay,
Fehlbindung, DoS, Downgrade, Policy-Konflikte, Bypass und Schlüsselkompromittierung.
Lokales Bandit prüft nur Python-Muster; es ersetzt weder Kryptoreview noch Funkmessung.

# PPS+ Identity & Location: Community-Forschungsroadmap

**19.11.2026** · Offener Implementierungs- und Forschungsvorschlag für unabhängige Interessierte. TH Analytica entwickelt keine eigene Android- oder Hardwareproduktlinie und führt keine P8-Geräteversuche als Projektpflicht aus. Keine Freigabe für Ausgaben, Partnerkontakte oder Liveschaltung.

| Prio | Paket | Erledigungsgrad | Nächste Evidenz |
|---|---|---|---|
| P0 | Research, Grundrechte, Datenminimierung und Architektur | DOKUMENTIERT | Sicherheits-/Datenschutzreview extern |
| P0 | Reine Policy-Entscheidungsfunktion | SYNTHETISCH IMPLEMENTIERT | unabhängige Reimplementierung + widerlegende Tests |
| P0 | 28 synthetische Szenarien, Unit-Tests | AUTOMATISIERT GETESTET | weitere Mutation-/Property-Tests, adversariale Fälle |
| P1 | Optionale persönliche PPS-App mit OS-Biometrie und nur lokalem Schlüsselzugang | NICHT IMPLEMENTIERT | Vorschlag für unabhängige Entwickler: iOS/Android-Pilot, sichere Kryptographie |
| P1 | Nachweis ohne statische Tracking-Kennung | NICHT IMPLEMENTIERT | Unabhängige Prüfung von Challenge, TTL, Rotation, Replay und Privacy |
| P1 | Gebäude-Zonenregel mit Betreiberbefugnis | NICHT IMPLEMENTIERT | TH Analytica: Website-/Integrationsdateien je Auftrag; Dritte: räumliche und technische Validierung |
| P2 | Verifiziertes Binding ohne Gesichtsdatenbank | OFFENE FORSCHUNGSFRAGE | Externe Forschung zu Ground Truth und Fehlerquoten; keine Erfolgsbehauptung |
| P2 | OS-/Firmware-Purpose-Guard, kontrollierte Datensenken | NICHT IMPLEMENTIERT | Integrations- und Bypass-Nachweis ausschliesslich durch unabhängige Entwickler/Hersteller |
| P3 | Physische Orte (z. B. Simmenfälle) | WEBSITE-DATEIEN NUR NACH AUFTRAG | Betreiberfreigabe und Website-Integration getrennt von externem Hardwarepilot |
| P3 | Unabhängige fachliche Validierung | AUSSTEHEND | tatsächlich eingegangene Rückmeldungen und Review |

**Nicht vorziehen:** globale biometrische Identität, Echtzeit-Tracking, zivile Zielklassifikation, automatische Geräte-/Waffensperre. Diese Ziele gehören nicht zum PPS-Forschungsprototyp.

## Entscheidung

GO: reviewbare Community-Forschung, synthetische Negativszenarien und klar als nicht normativ gekennzeichnete Vorschläge. Eine öffentliche Draft-PR darf als Diskussionsgrundlage dienen; weder das Projekt noch ein Beitrag ist dadurch validiert.  
NO-GO: eigener Android-/Hardwarepilot, automatische Website-Deployments, Merges, Geräte-/Herstellerfreigaben, Käufe und Kontaktaufnahmen ohne separate Entscheidung.  
Ausstehende Rückmeldungen werden beobachtet und nach Eingang fachlich eingeordnet, ohne Entwicklungs- oder Testpflicht für TH Analytica.

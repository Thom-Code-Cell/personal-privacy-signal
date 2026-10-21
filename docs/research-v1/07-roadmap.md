# Priorisierte Roadmap und Go/No-Go

Aufwände sind Planungsschätzungen in Personentagen, keine Angebote. CHF 0 bedeutet
keine zusätzlichen externen Ausgaben in diesem Auftrag, nicht kostenlose Arbeitszeit.
Rollen sind Vorschläge; unbesetzte Rollen dürfen kein Gate selbst attestieren.

| Prio / Schritt | Verantwortung | Aufwand / Zusatzkosten | Risiko / Abhängigkeit | Go / No-Go |
|---|---|---|---|---|
| P0 Paket und Parserprüfung | TH Analytica Engineering | 2–4 PT / CHF 0 | überinterpretierte Tests | Softwarechecks grün, Evidenzgrenzen sichtbar; sonst Nacharbeit |
| P0 Review und PR | Thomas Hullin Freigabe; unabhängiger Reviewer noch offen | 0,5–1 PT / CHF 0 | öffentliches Repository, eingefrorene Basis | konkrete Änderungen reviewbar; Push/öffentliche PR erst nach Klärung Veröffentlichungsfreigabe |
| P1 Methodik-/Datenschutzfreigabe | Studienleitung und Datenschutzreview noch zu benennen | 2–3 PT / CHF 0 vorgesehen | Einwilligung, Accessibility, Akustik | Protokolle, Stop, Löschung, Verantwortliche bestätigt; sonst keine Personenversuche |
| P1 Synthetische Zustands-/Angriffsmatrix | TH Analytica Engineering | 2–4 PT / CHF 0 | Parser ist keine Policy Engine | unabhängige negative Vektoren, keine Trust-Upgrades; kein Feldclaim |
| P2 Eigener Android-BLE-Lauf | Android Engineer + Geräteverantwortliche, noch offen | 3–5 PT / nur vorhandene Geräte | API/Permissions, Energie, BLE-Transportkennung | V0–V4 und P1/P4 reproduziert; sonst nur S-Evidenz |
| P2 Raum-/Mehrpersonenversuche | Studienleitung + unabhängige Beobachtung | 3–6 PT / vorhandener Testraum | Ground Truth, Cluster, Relay | Agenda-Gates je Bedingung erfüllt; sonst UNBOUND/AMBIGUOUS beibehalten |
| P3 Vuzix-Leihgerätversuch | Geräteverantwortliche + Android Engineer | 2–5 PT / keine Beschaffung freigegeben | Firmware/Patchstand, Verfügbarkeit | autorisiertes vorhandenes Gerät und V0–V5; sonst BLOCKED |
| P3 Partnerreview | Thomas Hullin; mögliche Partner nicht beauftragt | 1–2 PT intern / externe Kosten unbekannt | Kapazität, Interessenkonflikte | gesonderte Kontakt-/Kostenfreigabe; keine Zusage voraussetzen |
| P4 Zweitimplementation/Krypto-/Bypassreview | unabhängiges Labor noch offen | offen / kein Budget freigegeben | Schlüssel, Anti-Relay, Ressourcen | reproduzierte Vektoren und gemessene Grenzen; sonst kein T1/T2-Produktclaim |
| P5 Herstellerintegration/Realpilot | Hersteller + Datenschutz + Betreiber, alle offen | offen / separate Freigabe erforderlich | OS-Hooks, Rechtswirkung, echte Fremdgeräte | alle nachfolgenden Release-Gates erfüllt; aktuell NO-GO |

## Release-Gates (nicht durch diesen Auftrag freigegeben)

1. Unabhängiges Security-/Kryptoreview, zweite Implementierung, Ressourcen-/Flood-
   Tests und vollständige Traceability der normativen Anforderungen.
2. T1-Frische/Rotation/Recovery definiert; T2 nur nach messbar belastbarem Binding-
   Profil, separat bewerteten Fehlbindungen und unabhängiger Reproduktion.
3. Offline-Revokationsgrenze, räumliche Autorität, Smartphonefreiheit,
   Accessibility, Datenminimierung und zugängliche analoge Schutzprozesse belegt.
4. Tatsächliches OS-/Firmware-Enforcement aller behaupteten Verarbeitungsschritte
   an unterstützten Fremdgeräten belegt; keine App-Anzeige als Ersatz.
5. Explizite Freigabe für Kosten, Pilot, Veröffentlichung oder Produktion jeweils
   separat. Merge/Deployment/E-Mail/Hardwarekauf gehören nicht zum aktuellen Umfang.

## Entscheidung jetzt

GO für Forschungs-/Reviewpaket, reversible Parserhärtung und nach ausdrücklicher
Freigabe die öffentliche Draft-PR als Research & Validation – Experimental.
NO-GO für Produktionsreife, universelle Kamerasperre, Herstelleradoption,
bestätigte T2-Bindung und reale Fremdgerätewirkung. Keine Zeitplanung setzt
ungeklärte Partner-/Geräteverfügbarkeit als gegeben voraus.

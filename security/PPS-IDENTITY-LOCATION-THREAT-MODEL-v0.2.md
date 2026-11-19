# PPS+ Identity & Location: Bedrohungsmodell (P8)

**Entwurf, 19.11.2026.** Ergänzt die vorhandenen T01–T15 und P7-T16–T22 ohne bereits ausgerollte Abwehrleistung.

## Schutzgüter

A. Grundrechte und physischer Schutz **aller** Personen, auch ohne Geräte.  
B. Keine Entstehung eines weltweiten Personen-Tracking- oder Gesichtsdatenregisters.  
C. Integrität der freiwilligen Datenschutzpräferenz.  
D. Korrekte zeitliche/räumliche Anwendbarkeit lokaler Hausregeln.  
E. Zweckbindung über Rohdaten, abgeleitete Merkmale, Logs und jede Datensenke.  
F. Verlässliche Anzeige, wenn Durchsetzung **nicht** möglich oder nicht nachgewiesen ist.

## Vertrauensgrenzen

1. User → OS-Biometrie-Dialog → hardwaregeschützter Schlüssel **(Konzept, nicht implementiert)**
2. Gerät → unzuverlässiges Nahfunksignal → Sitzungsechtheit und Frische **(nicht implementiert)**
3. Sender/Receiver → beobachtete Person **(nicht gelöst)**
4. Website/Betreiber → signierte Hausregel → unabhängige Autoritätsprüfung **(nicht implementiert)**
5. Lokales Zonensignal → tatsächlich betroffener Raum **(nicht gelöst)**
6. Policy Resolver → OS-/Firmware-Schnittstelle → Kamera, Speicher, KI-Embedding, Cloud, Training, fremde Apps **(nicht implementiert)**

## Bedrohungskatalog und Gegenmassnahmen

| ID | Angriff / Fehlannahme | Anforderung / Test |
|---|---|---|
| T23 | Weltweites Gesichts-/Standortregister wird selbst zum Überwachungsinstrument | P8-01/02/06: Registerverbot, Datenfluss-/Linkability-Review, keine echten IDs |
| T24 | Telefonentsperrung wird mit echter Identität oder Kamera-Subjekt verwechselt | P8-03/04/05: getrennte Zustände; Negativfall P8-02/03 |
| T25 | Nahfunk oder UWB wird über Wände/Relay als sichere Raum-/Personenlage gedeutet | P8-04/09: getrennte Zone/Binding-Evidenz, P8-12 |
| T26 | Geklonter QR, gefälschte oder abgelaufene Hausregel | P8-07/08/09: Quelle, Zeit, Ort und Autorität unabhängig; P8-07/08/11 |
| T27 | Website-JSON wird als physisch erzwungene No-Camera-Zone ausgegeben | P8-08/15: nur advisory ohne Enforcer; P8-07/22 |
| T28 | Fehlendes PPS oder leeres Handy wird zur Erlaubnis für Erfassung/Zielentscheidung | P8-02/11/13: kein Default-ALLOW; P8-01/14/21 |
| T29 | Bösartige Sender lösen allgemeines Abschalten sicherheitsrelevanter Systeme aus | P8-14: keine anonyme Kill-Switch-Wirkung; P8-23 |
| T30 | Eng erlaubte Sicherheitsinferenz wird in Profiling/Training/Schadenshandlungen umgewidmet | P8-12/13, P7-Zwecksperren; P8-14/15/16/17–20 |
| T31 | Unterschiedliche Hersteller-Apps umgehen die gemeldete Kamera-/Cloud-Sperre | P8-15: OS-/Firmware-Gate, Status UNSUPPORTED sichtbar; P8-22 |
| T32 | Logging von Kurzzeitnachweisen schafft faktisch Bewegungsprofile | P8-01/06: rotierende, empfängergebundene Nachweise, Redaction/Retention Review |
| T33 | Aufdringliche Authentisierungsabfragen oder erzwungene Zustimmung benachteiligen Menschen ohne Gerät | P8-02: gleichwertige analoge Prozesse, Accessibility und No-Phone-Versuche |
| T34 | Frühere, gestohlene oder gerätefremde Nachweise werden abgespielt | unabhängige Krypto-/Replay-/Revocation-Tests vor T1; hier NOT_IMPLEMENTED |
| T35 | Ein signierter Standort-Claim wird als rechtlich gültige Hausrechtsanordnung angesehen | P8-07/09/10: juristischer und technischer Gültigkeitsbeweis getrennt |

## Trennschärfe: «Signal fehlt» ist weder Ja noch Nein

*Fehlendes PPS* gibt keine zusätzlichen Rechte. Es darf aber auch nicht als anonyme Steueranweisung für fremde Sicherheitsanlagen wirken. Der bestehende Rechts-/Einwilligungs-/Schutzrahmen und nachweislich anwendbare Hausregeln bleiben unabhängig erhalten. `DENY` ist im Prototyp ein vorgeschlagener Kontrollentscheid, kein Befehlsoutput einer Kamera, Drohne oder Waffe.

## Datenschutz- und Ethik-Gates

- Privacy Impact Assessment und Rechtsprüfung für Schweizer DSG und ggf. DSGVO vor jeder echten Anwendung.
- Keine Gesichtsbilder, akustischen Aufnahmen, biometrischen Templates, Personenkoordinaten, ungeschützten EIDs oder Bewohnerlisten in öffentliches Git/CI.
- Minderjährige und Menschen ohne Geräte müssen als Fälle im Konzept erhalten bleiben, dürfen aber **nicht** ohne weitere Freigaben real getestet werden.
- Einwilligung, Betreiberrechte, Vorabinformation, Widerruf, Löschung, Datenminimierung und unabhängige Review.
- Kein Experiment an einem militärischen Zielsystem, keine Zielkoordinaten, keine Live-Personenerkennung, keine fremde Funkinterferenz.
- Externe Angreifer, unkooperative Geräte oder tatsächliche Autonomie-Entscheidungen sind in dieser Lieferung **nicht** validiert.

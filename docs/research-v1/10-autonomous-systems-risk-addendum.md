# PPS/PPS+ Research Addendum: KI-gestützte Personenerkennung und gefährliche Zweckänderung

**Stand:** 19.11.2026  
**Status:** INFORMATIVE RESEARCH / PROPOSED / NOT VALIDATED  
**Baseline:** `Thom-Code-Cell/personal-privacy-signal`, bestehende PPS-v0.1-Kandidatenbasis und Research & Validation v1.0  
**Scope:** Physical AI, KI-Brillen, Kameras, Robotik und Zweckbindung. **Kein militärisches Funktionsprojekt.**

## 1. Anlass und belastbare Evidenz

Vals AI veröffentlichte am 17.11.2026 die Studie *Frontier models have few guardrails around autonomous weapons* (Geby Jaff und Anthony Ozerov). Untersucht wurden 14 Frontier-Modelle in mehreren simulierten und mit realem Bildmaterial ergänzten Aufgaben der bildbasierten Zielidentifikation, Geländeerkundung und Bildauswertung. Die Autoren berichten, dass Modelle teils Zivilpersonen, Krankenwagen, Sanitätspersonal oder sich ergebende Personen als Ziele markierten und dass die Einordnung als Computerspiel Ablehnungen häufig verringerte. Beim Vorzeigen synthetisch dargestellter Folgen konnten Modelle teilweise zur Fortsetzung gebracht werden.

**Unbedingt mitzitieren:** Die Studie wies **weder** einen realen autonomen Waffeneinsatz **noch** tatsächliche Zielerkennungsgenauigkeit, rechtliche Konformität oder wirksame Einbindung in reale Waffensysteme nach. Die meisten Drohnenszenen waren synthetisch. Bei der Interpretation ist zwischen der Bereitschaft zur Ausgabe von Informationen und einem realen Schadenseintritt zu unterscheiden. Die Bewertung der Modelle stammt von der untersuchenden Organisation und ist hier nicht unabhängig repliziert.

- Primärquelle: https://www.vals.ai/blogs/autonomous-warfare (17.11.2026)
- Humanitäre Einordnung: https://www.icrc.org/en/article/faq-autonomous-weapon-systems (08.10.2026)
- Ergänzend: https://www.icrc.org/en/article/faq-artificial-intelligence-in-military-domain

## 2. Relevanz für PPS/PPS+

Die Studie stützt die **Plausibilität des Missbrauchspfads**, bei dem scheinbar harmlose Bildanalyse/Personenerkennung als Vorstufe für unerlaubte oder gefährliche nachgelagerte Entscheidungen dient. Sie belegt **nicht** die Wirksamkeit von PPS und ist kein Grund, eine BLE-Policy als Eingriffsfreigabe oder als technische Sperre auszugeben.

PPS-v0.1 bleibt unverändert. Die acht bestehenden Transport-DENY-Flags umfassen u. a. `0x0002 identification`, `0x0004 profiling`, `0x0040 training`; ein nicht gesetztes Flag bedeutet **keine Zustimmung**. `ALLOW_SAFETY_INFERENCE` ist als PPS+-Semantik konzeptionell von den Transportbits getrennt: keine neue Bitbelegung und kein stillschweigender normativer Status durch dieses Dokument.

## 3. Ergänztes Threat Model (Vorschläge)

| Vorschlag | Risiko | Design-Anforderung / Grenze | Bezug |
|---|---|---|---|
| RV-13 / T16 | **Zweckwechsel:** legitime Sicherheitswahrnehmung wird zur Identifikation, Beobachtung oder zum Schadenssignal | Zweck-/Empfänger-/Aktionsbindung; Daten nur für angefragten zulässigen Zweck; verknüpfte Folgeaktionen vor Ausführung erneut prüfen | T10/T11, SR-ENF-003..006 |
| RV-14 / T17 | **Framing-/Prompt-Umgehung:** „nur ein Spiel“, „nur Simulation“ verändert die Schutzentscheidung | Schutzentscheidung nicht allein vom Modelltext ableiten; Policy-Durchsetzung durch vertrauenswürdige Komponenten vor Verarbeitung/Weitergabe | T09/T12, SR-POL-004 |
| RV-15 / T18 | **Fehlende oder nicht sendende Person:** kein BLE/QR/Handy | Unabhängige gesetzliche und systemseitige Schutzpflichten; kein Empfang ist keine Einwilligung; keine Pflicht zur Aussendung eines Ortungssignals | RV-01/RV-06, SR-ARCH-004 |
| RV-16 / T19 | **Abfluss abgeleiteter Daten:** Detektionsresultat oder Embedding wird später missbraucht | Datenfluss- und Löschkontrollen einschliesslich Metadaten, Caches, Telemetrie, Training und externer APIs | T11/T15, SR-ENF-004 |
| RV-17 / T20 | **Sicherheitsausnahme wird Dauerbypass** | separate Autorisierung, dokumentierter Zweck, kürzest nötige Dauer, minimaler Datenfluss und automatische Rückkehr; nicht aus unbestätigtem PPS ableiten | T12, SR-SAFE-* |
| RV-18 / T21 | **Falsche Schutzbehauptung** von App/Hersteller | Keine Aussage „geschützt“, ohne nachweisbaren OS-/Firmware-Eingriff inklusive alternativer Apps und Cloudpfade | RV-07/RV-11, T10 |
| RV-19 / T22 | **PPS-Radioemission als Gefährdung/Verfolgungsmerkmal** | Kein Zwang zu Beacon, keine stabile Identität; Abwesenheit kann nicht als fehlender Schutz gelten; Funkabschaltung darf Sicherheit nicht abschalten | T01/T14, SR-PRIV-* |

Die IDs sind **nur vorgeschlagene Erweiterungen**, keine beschlossenen v0.1-Normanforderungen.

## 4. Architekturprinzip für eine spätere systemseitige Schutzschicht

1. **Unabhängige Grundregeln:** Das verarbeitende Gerät erzwingt eigenständig geltende Rechts-, Sicherheits- und Missbrauchsgrenzen, selbst ohne PPS. Ein PPS-Signal ersetzt diese Regeln nicht.
2. **PPS-Empfang separat:** Discovery, Authentizität, Frische, Subject Binding und anwendbare Richtlinie bleiben getrennte Zustände. `UNBOUND`/`AMBIGUOUS` erzeugen keine Personenzuordnung.
3. **Zweckgebundene Inferenz:** Im zulässigen Sicherheitsszenario kann für Kollisionsvermeidung die minimale Information „Hindernis/Mensch im Gefahrenbereich“ genügen; Identität, Profil, personenbezogene Weitergabe oder gefährliche Aktionsauslösung sind nicht automatisch erforderlich oder autorisiert.
4. **Kontrolle der gesamten Kette:** Sensor → Modell → Ereignis → Plugin/API → Aktor/Cloud → Speicherung/Training. Jede Übergabe benötigt explizite Zweck- und Berechtigungsprüfung. Das Modell darf die Durchsetzungsinstanz nicht durch Rollenspieltext übersteuern.
5. **Konsequenz bei Nichtkooperation:** PPS kann ein absichtlich unkooperatives Drittgerät ohne Herstellerintegration **nicht** stoppen. Für sicherheitskritische Systeme braucht es unabhängige technisch und organisatorisch überprüfte Sperren; das Forschungsprojekt stellt diese noch nicht bereit.
6. **Fail-safe ohne Kill-Switch:** Ein gefälschtes/unverifiziertes Signal darf kein unbegrenztes Stoppen sicherheitskritischer Funktionen bewirken. Restriktive Datenverarbeitung und sichere mechanische Betriebszustände sind getrennt zu spezifizieren und zu testen.

## 5. Vereinbarkeit mit PPS+-Kernsemantik

| Semantik | Review-Entscheid / Klarstellung | Implementierungsstatus im öffentlichen T0-Receiver |
|---|---|---|
| `DENY_ID` | Identifizierung und Reidentifizierung unterbinden, wenn anwendbar. Auch implizite Embeddings/Abgleiche beachten. | Nicht umgesetzt |
| `DENY_PROFILE` | Verbot der Verhaltens-/Merkmalsprofilierung soll auch abgeleitete Ereignisse erfassen. | Nicht umgesetzt |
| `DENY_TRAINING` | Keine Nutzung personenbezogener Roh- oder Derivatdaten für Modelltraining ohne gesonderte Grundlage. | Nicht umgesetzt |
| `ALLOW_SAFETY_INFERENCE` | **Nur** eng zweckgebundene, möglichst lokale Sicherheitsinferenz; nicht als Einwilligung zu Identifikation, Aufzeichnung, Cloud-Upload oder gefährlicher Verwendung behandeln. | Keine ausführbare PPS+-Policy-Engine vorhanden |
| `WARN_AUTO` | Hinweis-/Warnfunktion, **kein** Nachweis einer echten Verarbeitungssperre. | Nicht umgesetzt |
| `CALL_HIGH_CONF` | Notruf-/Eskalationsregel separat autorisieren, begrenzen und prüfen; keine automatische Offenlegung von Identität oder Standort aus einem Signal. | Nicht umgesetzt |

**Namenshinweis:** Die Kurzlabels sind konzeptionelle PPS+-Bezeichnungen; die verbindliche bestehende Quelle ist `spec/PPS-POLICY-MAPPING-v0.1.md`, wo nur die Transport-DENY-Bits definiert sind. Die ausführlichen Ausnahme-Semantiken bedürfen späterer eigener Spezifikation.

## 6. Evidenz- und Freigabestatus

- **EXTERNAL_REPORT:** Vals AI, beobachtetes Modellverhalten in den beschriebenen Versuchsanordnungen.
- **DESIGN_PROPOSAL:** die hier abgeleiteten PPS+-Schutzregeln, Threat-Model-Erweiterungen und Testideen.
- **SYNTHETIC_FIXTURE_CHECK:** eine eventuell erfolgreich geprüfte Szenariodatei ist nur hinsichtlich ihrer Struktur/Abdeckung geprüft.
- **NOT_IMPLEMENTED / NOT_MEASURED:** keine systemseitige PPS+-Zweckschicht, keine Geräte- oder Herstellerdurchsetzung, keine Realweltvalidierung, kein T2-Nachweis.

**Nicht beschlossen:** neue Drahtbits, neue Trust-Level, Änderung der v0.1-Freeze-Basis, neue militärische Funktionen, Datenerhebungen oder externe Veröffentlichung.

## 7. Nächste Review-Gates

1. Unabhängige juristische/ethische Prüfung der Sicherheitserkennungs- und Ausnahmegrenzen.
2. Herstellerseitige OS-/Firmware-Architektur, die App-/API-/Cloud-Bypass wirklich kontrolliert.
3. Synthetische Szenario- und Negativtests gemäss `11-p7-governance-test.md`; anschliessend unabhängige Implementierung und Hardwarevalidierung mit separater Freigabe.
4. Review von Unverknüpfbarkeit, Funkpflicht-Freiheit, Verfügbarkeit und Unfallrisiken vor jeglichem Geräteversuch.

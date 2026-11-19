# PPS+ Identity & Location Research – v0.2 proposal

**Status:** PROPOSED, NOT STANDARD, NOT DEPLOYED · **Datum:** 19.11.2026  
**Kontext:** `Thom-Code-Cell/personal-privacy-signal`, Kandidat v0.1; Research & Validation v1.0; P7 Purpose Guard.  
**Geltung:** getrennte, optionale Forschungserweiterung; keine Änderung am eingefrorenen Wire-Protokoll, an dessen Flags oder an existierenden Nachweisen.

## 1. Zweck und harte Schutzgrenzen

PPS soll ein *Präferenzsignal* und die Möglichkeit der Überprüfung seiner Einhaltung erforschen. Es darf **keine universelle Personenidentifizierungs- oder Echtzeit-Ortungsinfrastruktur** schaffen. Insbesondere:

1. Menschenrechte und Schutz von Zivilpersonen sind **nicht** abhängig von Registrierung, Gerät, Biometrie, Signal, Standortdaten oder Klassifikation.
2. Kein weltweites biometrisches Register; keine Gesichts-Fingerprints, Rohfotos, Face-Embeddings, Fingerabdrücke oder Identitätsnummern in PPS-Protokoll, Backend oder öffentlichen Quellen.
3. Eine lokale Entsperrung beweist nur die Berechtigung zum Zugriff auf eine bestimmte Gerätefunktion, keine amtliche Identität und keine visuelle Zuordnung zu einer Person vor einer Kamera.
4. Position des Handys, physische Raumzuordnung und Zuordnung zur beobachteten Person sind **drei getrennte Tatsachen**. GPS, BLE-Nähe und UWB-Distanz sind keine automatischen Belege für Kamera-Person-Bindung.
5. Kein geheimer Standortkanal, keine laufende Speicherung der Aufenthaltsorte, kein Missbrauch als Zielidentifizierungs- oder Zieldatenbank.
6. Webseiten-Metadaten beschreiben ein Gebäude; sie sind **weder** ein räumlicher Autoritätsbeweis **noch** eine technische Durchsetzung bei fremden KI-Geräten.
7. Reine Parser-, Regel- und UI-Prüfungen sind keine Realwelt-Sicherheitsgarantie. Nicht kooperierende Kameras, Roboter oder Waffen werden durch PPS nicht gestoppt.
8. PPS-Authentisierung darf nie automatisch gefährliche nachgelagerte Verarbeitung autorisieren. Kein `ALLOW` aus fehlendem Signal, erfolgreichen Biometriedialogen oder einem Spiel-/Simulationslabel.

## 2. Drei strikt getrennte Architekturbereiche

### A. PPS Personal Protection (opt-in)

- **App-Wallet auf Gerät:** Person legt Schutzpräferenzen fest. Kein Benutzerkonto zwingend. Alternativen für Menschen ohne Gerät bleiben bestehen.
- **Lokale Freigabe:** Betriebssystem-API (`LocalAuthentication` / `BiometricPrompt` mit Keystore-Schutz), optional Geräte-PIN. Keine Übergabe biometrischer Merkmale an PPS.
- **Kryptografische Bindung:** künftige, separat zu spezifizierende challenge-gebundene Sitzung mit hardwaregeschütztem Schlüssel, kurzlebigem kontext-/empfängerspezifischem Nachweis und Replay-Schutz; im Prototyp **nicht implementiert**.
- **Übertragungsweg:** noch zu entscheiden. BLE kann Präsenz anzeigen; für authentifizierte Aussagen bedarf es einer gesicherten Sitzung und Verifikation. Keine dauerhafte Sende-ID.
- **Kamera-Person-Binding:** separate, bislang nicht nachgewiesene Forschung; `UNBOUND/AMBIGUOUS` nicht zu `BOUND` hochstufen. Biometrische Gesichtsdaten nicht als Lösungsabkürzung einsetzen.

### B. PPS Protected Locations (Ort/Objekt)

- **Öffentlicher Hinweis:** Website, Schild und maschinenlesbare Hausregeln informieren über die Schutzpolitik (beispielsweise Digital Detox).
- **Verifizierbares Regelpaket:** Herausgeber, Versionsnummer, Zone, Gültigkeitsdauer, erlaubte/gesperrte Zwecke, offline nutzbare Signatur und Widerrufsgrenze sind künftige Felder; die öffentliche Website allein genügt nicht.
- **Autorität und räumliche Anwendbarkeit:** getrennte Validierungen. Eine gültige Signatur beweist nicht, dass der Betreiber für den Ort autorisiert ist; ein gültiges Dokument beweist nicht, dass der Receiver im betreffenden Raum ist.
- **Nachbarschaftseffekt:** Funk durch Wände, QR-Kopien, veraltete Offline-Regeln, mehrdeutige Gebäude und mehrere konkurrierende Betreiber können falsche Zuordnungen erzeugen.
- **Fallback:** Bei ungeklärter Anwendbarkeit Status `UNKNOWN` statt vorgetäuschter Durchsetzung. Verbotene/hochriskante Verarbeitung erhält keine automatische Freigabe. Keine anonyme Funksperre von notwendigen Sicherheitsfunktionen.

**Beispiel Simmenfälle:** Die bestehenden Website-/KI-Dateien sind höchstens Informationen. Ein separater, signierter Gebäude-Policy-Pilot mit lokalem Empfänger, Betreiberfreigabe und nachgewiesener Raumzuordnung müsste erst entstehen; hier wird nichts am Liveauftritt verändert.

### C. PPS+ System Protection (vertrauenswürdiger Empfänger)

- **Normativer Kandidat:** Quelle (mit Evidenzklasse) → Echtheit/Frische → Zonenautorität/Anwendbarkeit → getrenntes Subject Binding → PPS+-Zweckpolicy → überprüfbarer OS-/Firmware-Enforcement-Punkt → nachgelagerte Datenflusskontrolle → minimiertes Audit.
- **Zwecksperre:** Ein eng erlaubter Sicherheits-Hinweis erlaubt nicht Identifizierung, Profilbildung, Training, Upload, Weitergabe oder schädliche Wiederverwendung.
- **Jeder Datensenke prüfen:** Rohbild, Embedding, Zwischenrepräsentation, Cache, Log, Cloud, Modelltraining und Aktionsschnittstelle müssen separat geprüft werden.
- **Echte Enforcement-Behauptung nur mit Herstellerintegration und Gerätenachweis.** Das Referenzprogramm liefert ausdrücklich bloss synthetische Richtlinienentscheide.

## 3. Evidenz-/Vertrauenszustände

| Dimension | Werte im Forschungsprototyp | Bedeutungsgrenze |
|---|---|---|
| Geräte-Authentisierung | `ABSENT`, `LOCAL_AUTH_ONLY`, `SESSION_VERIFIED` | Kein Gesicht oder Kamera-Subjekt identifiziert |
| Zuordnung zu Person | `UNBOUND`, `AMBIGUOUS`, `INDEPENDENTLY_VERIFIED` | Letzter Zustand ist **vorgegebene synthetische Annahme**, nicht durch PPS erreicht |
| Gebäudestatus | `ABSENT`, `WEB_METADATA_ONLY`, `SIGNED_ZONE_UNCONFIRMED`, `EXPIRED`, `VERIFIED_APPLICABLE` | Letzter Zustand ist **vorgegebene synthetische Annahme**, nicht über GPS berechnet |
| Sicherheitsfreigabe | `NONE`, `INDEPENDENTLY_AUTHORIZED_NARROW` | Kein allgemeines Verarbeitungsprivileg; vorläufige Simulation |
| Durchsetzung | `SIMULATION`, `UNSUPPORTED` | Beide **ohne** Hardware-Enforcement |

**Wichtig:** Die Fixture-Labels `SESSION_VERIFIED`, `INDEPENDENTLY_VERIFIED` oder `VERIFIED_APPLICABLE` sind nicht die Ausgaben tatsächlicher Authentifizierungs-, Biometrie- oder Ortsmessungen. Sie werden nur zur Prüfung einer hypothetischen Policy-Engine als Eingaben gesetzt.

## 4. Kandidatenanforderungen (P8-01 bis P8-16)

| ID | Anforderung |
|---|---|
| P8-01 | Kein zentraler Biometrie- oder Personenstandortregister-Baustein |
| P8-02 | Opt-in ohne Identitätszwang; keine Benachteiligung bei Geräte-/Signallosigkeit |
| P8-03 | OS-Biometrie nur zur lokalen Schlüssel-/Funktionsfreigabe, keine Templates |
| P8-04 | Authentisierung, Identität, Sichtzuordnung und Lage getrennt ausweisen |
| P8-05 | Unbound/ambiguous nie zum stillen Personen-Freigabezustand hochstufen |
| P8-06 | Kein wiederverwendbarer Personen-/Geräte-Tracking-Identifier in Ausgaben |
| P8-07 | Sender-, Betreiber-, Raum- und Durchsetzungsnachweis getrennt |
| P8-08 | Website-Metadaten nicht als räumlich gültige Hausregel werten |
| P8-09 | Ungültige, abgelaufene oder benachbarte Hausregel nie als verifiziert werten |
| P8-10 | In tatsächlich gültigen Zonen restriktivere Regeln berücksichtigen |
| P8-11 | Keine automatische Erlaubnis aus fehlendem PPS-Signal oder nicht gesetzten Bits |
| P8-12 | Sicherheitsinferenz nur getrennt, eng autorisiert und ohne Zweck-Reuse |
| P8-13 | Schädliche Weiterverwendung unabhängig von Identität und Kontext sperren |
| P8-14 | Keine Sicherheitssperre allein aufgrund unbestätigter anonymer Funksignale |
| P8-15 | `policy_decision` und `actual_enforcement` getrennt; unsupported nie als geschützt melden |
| P8-16 | Vor Personen- oder Kameratests: Ethik, Recht, Einwilligung, sichere Testumgebung und unabhängige Review |

## 5. Grenzen des lauffähigen Demonstrators

Datei `receiver-kit/pps_identity_location_reference.py` implementiert ausschliesslich eine **reine Funktion** über synthetische Zustandswerte; `conformance/test_pps_identity_location.py` prüft Negativfälle. Eine geschlossene Eingabestruktur lehnt zusätzliche Rohkoordinaten-, Biometrie- und Identifier-Felder ab. Es gibt keine native App, Authentisierungs-API, digitalen Ausweis, BLE/UWB-Stack, Geofence-Geometrie, Signaturprüfung, Kamera- oder Firmware-Steuerung. Daraus folgt keinerlei Produktionsreife.

## 6. Migration ohne v0.1-Veränderung

Neue Vorschläge werden in eigener Datei dokumentiert und über Review auf eine mögliche spätere Version geprüft. Keine Änderungen an `spec/PPS-WIRE-PROTOCOL-v0.1.md`, `spec/PPS-POLICY-MAPPING-v0.1.md` oder am bisherigen T0-Parser. Ein späteres Modell muss die fünf Evidenzgrenzen getrennt technisch belegen und unabhängig reproduzierte Tests bestehen.

## 7. Quellen zur technischen Machbarkeit

- Apple: https://developer.apple.com/documentation/localauthentication (API-Zugriff ohne biometrische Rohdaten)
- Android: https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt (lokale Authentisierung / CryptoObject)
- Android UWB: https://developer.android.com/develop/connectivity/uwb (Geräte-Range, kein visueller Personenbeweis)
- Apple Nearby Interaction: https://developer.apple.com/documentation/nearbyinteraction/ (Distanz/Richtung zu Geräten)
- W3C VC 2.0: https://www.w3.org/TR/vc-data-model-2.0/ (Minimierung, Korrelation, selektive Offenlegung; Implementierung hier **nicht** behauptet)
- Bestandsgrundlage: https://github.com/Thom-Code-Cell/personal-privacy-signal

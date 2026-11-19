# PPS+ Identity & Location Research: Forschungsnachtrag

**Stand 19.11.2026 · Status: RESEARCH / NOT MEASURED ON DEVICES**

## Ausgangshypothese

Menschen können freiwillige Präferenzen auf ihrem Gerät verwalten. Für die digitale Durchsetzung können lokale Geräteauthentisierung, verifizierte Sitzungen und unabhängig nachgewiesene Gebäuderegeln *zusammenwirken*, ohne einen zentralen Personen- oder Standortindex aufzubauen. Diese Kopplung benötigt mehrstufige Prüfung und darf Schutz **nicht** von Registrierung abhängig machen.

### Hypothesen und Falsifikationskriterien

| Hypothese | Gegenversuch / Gate | Stand |
|---|---|---|
| H-P8-AUTH | Lokaler Biometriedialog gibt keinen biometrischen Rohwert heraus; Entsperrung darf Camera-Binding nicht aufwerten | synthetischer Fehlerfall geprüft; Plattformexperiment NOT_MEASURED |
| H-P8-NOPHONE | Gleicher Basis-Schutz auch mit leerem oder fehlendem Gerät | synthetische Fälle geprüft; Android/Brille NOT_MEASURED |
| H-P8-BIND | Authentifizierte Sitzung ist nicht räumliches Subject Binding | Negativtest für SESSION_VERIFIED + UNBOUND/AMBIGUOUS; Kameraexperimente NOT_MEASURED |
| H-P8-VENUE | Signierte Regel und räumlich anwendbare Regel sind getrennt | Tests WEBSITE_ONLY, SIGNED_UNBOUND, EXPIRED, VERIFIED_APPLICABLE; Realzone NOT_MEASURED |
| H-P8-PURPOSE | Kurzzeitige Sicherheitsinferenz erzeugt keine allgemeine Weiterverwendungserlaubnis | synthetischer Negativtest + P7; OS-/Cloud-Sinks NOT_MEASURED |
| H-P8-PRIVACY | Kurzlebige, empfängerbezogene Nachweise haben geringeres Tracking-Risiko als statische IDs | Krypto- und Protokollentwurf erforderlich; NOT_MEASURED |
| H-P8-DEVICE | Alle geschützten Datenpfade werden auch in anderen Apps tatsächlich blockiert | Hersteller- und Firmwareintegration erforderlich; NOT_IMPLEMENTED |

## Machbarkeit heute

1. iOS `LocalAuthentication` und Android `BiometricPrompt` können *lokale* Freigabe bestätigen, ohne biometrische Rohdaten an die App auszugeben. Das ist keine zivile Identitätsprüfung.
2. BLE lokalisiert Geräte grob, nicht eindeutig Menschen. UWB kann Gerätedistanzen und teils Richtungen bestimmen, aber für viele Geräte gar nicht eingesetzt werden; keine Person-Bild-Verifikation.
3. Verifiable Credentials können selektive Offenlegung unterstützen; diese Eigenschaften entstehen nicht automatisch durch die Wahl eines Datenformats. Wir implementieren hier **keine** VC-Kryptographie.
4. Webseiten können Regeln *kommunizieren*, aber sie übertragen diese nicht zwingend an Offline-Kameras und erzwingen auch kein Firmwareverhalten.
5. Keine universelle Einigung über Hersteller-Enforcement oder automatische Schutzwirkung von PPS nachgewiesen.

## Minimaler Ablauf für spätere Pilotarchitektur

Person aktiviert optional Datenschutzpräferenz → OS gibt lokalen Zugriff frei → App erhält *keinen* biometrischen Rohwert → kurzlebiger, challengengebundener Policy-Nachweis als Forschungsoption → Empfänger prüft getrennt Sitzung, Zone, Bindung und Zweck → unterstützter, nachweisbarer Enforcement-Punkt beurteilt jeden Verarbeitungsschritt → Feedback zeigt tatsächliche Durchsetzung oder «nicht unterstützt».

Für Gebäude separat: Betreiber verfasst Hausregel → Kompetenz/Autorität wird unabhängig geklärt → signiertes lokales Paket mit eindeutiger Geltungsgrenze → Receiver weist **vor** Policy-Anwendung räumliche Zugehörigkeit nach → setzt verifizierte Regeln nur in unterstützten Anwendungen um.

Für Menschen ohne Gerät: unabhängige allgemeine Regeln, sichtbare Hinweise, betriebliche Verfahren und gesetzliche Schutzpflichten. **Keine Zusatzsicherheit entsteht allein durch Geräteverbreitung.**

## Ergebnis dieser Lieferung

Der Python-Demonstrator ist ein **Policy-Simulator**, kein Teilnehmernachweis und keine sichere Empfangssoftware. Er prüft 28 benannte rein synthetische Fälle und lehnt unzulässige zusätzliche Datenfelder ab. Die simulierte Ausgabe `DENY` hat **keine** Wirkung auf Kamera, Cloud, KI-Modell oder Hardware. Keine Messung an Menschen/Standorten, keine Online-Anwendung und keine gesetzliche Autorisierung.

## Quellen und Aktualität

Dokumentiert am 19.11.2026:

- https://developer.apple.com/documentation/localauthentication
- https://developer.android.com/reference/android/hardware/biometrics/BiometricPrompt
- https://developer.android.com/develop/connectivity/uwb
- https://developer.apple.com/documentation/nearbyinteraction/
- https://www.w3.org/TR/vc-data-model-2.0/
- https://github.com/Thom-Code-Cell/personal-privacy-signal

Keine dieser Quellen belegt einen aktuell implementierten PPS+-Identitäts- oder Standortdienst.

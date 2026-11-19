# P8: Validierungsprotokoll Identity & Location

**Klassifizierung:** S (synthetische Softwareprüfung) · **P8-Feldmessung:** NOT_MEASURED. 

## 1. Wiederholbare lokale Prüfung

Nur Python-Standardbibliothek, kein Internet/Konto/Kamera/Funk nötig:

```bash
python -m unittest discover -s conformance -p 'test_pps_identity_location.py' -v
python -m unittest discover -s conformance -p 'test_pps_identity_location.py' -q
python tools/validate_p7_fixtures.py
```

Die P8-Tests sind bewusst als eigener Dateiname abgelegt, um im Originalrepository bestehende Testpläne oder Module nicht umzudefinieren. Tests kontrollieren **simulierte Entscheidungslogik**, nicht die tatsächliche Verhinderung von Ausführung.

## 2. Szenariomatrix

`conformance/fixtures/p8-identity-location-scenarios.json` enthält 28 synthetische Fälle mit IDs P8-01 bis P8-28. Gruppen:

- **P8-01–06:** Personen ohne Smartphone, Biometrie-/Session-Abgrenzung, unklare Bindung, korrekt gebundene restriktive Präferenz.
- **P8-07–13:** Website-Annotation, nur signierte Regel, bestätigte Zone, Expiry und übergreifende Hausregel.
- **P8-14–16:** schädliche Zweckumwidmung, kein Trick über scheinbares Spielsetting.
- **P8-17–21:** eng überprüfte Sicherheitsanwendung gegenüber unzulässigen Ausnahmen.
- **P8-22–28:** fehlendes Receiver-Enforcement, anonyme Signale, Cloud-Zwecksperre, Session/Ort-Verwechslungsgefahr.

Auch separate Unit-Tests decken unbekannte Felder, überzählige personenbezogene Datenattribute und fehlerhafte Enum-Zustände ab. Die Szenariomatrix ist kein umfassender Proof of Safety.

## 3. Künftige echte Gates, nicht Bestandteil dieses Laufs

| Gate | Prüfung | Freigabevoraussetzungen |
|---|---|---|
| G1 Recht/Datenschutz | Schutzbedürftige Daten, Zweckbindung, Datenminimierung, DPIA, Zuständigkeiten | Fachreview, dokumentierter Zweck, echte Einwilligung (nur soweit erforderlich) |
| G2 Mobile | iOS/Android Authentisierung; Schlüsselbindung; Background-Grenzen; TTL; Recovery | unabhängiger sicherer Gerätebuild und Einwilligung, kein Template-Export |
| G3 Radio | BLE/UWB-Abdeckung, Relay, Cross-Wall, Replay, Geräteausfall | kontrollierte Umgebung, synthetische Tags, keine unbeteiligten Personen |
| G4 Ort | digitale Betreiberautorität, Zonengrenze, Abweichung und Revokation | Betreiberfreigabe, unabhängige Ground Truth, Fehlzuordnungen messen |
| G5 Binding | Mehrpersonen-Pose, Ambiguität, Challenge-/Zuordnungsraten | Vorklärung Ethik/Datenschutz, möglichst ohne reale Gesichter |
| G6 Purpose | Capture/Embedding/Profiling/Retention/Upload/Training/Safety-Sink | Hersteller-Hooks, negatives Bypass-Testing, Messungen an unterstützten Geräten |
| G7 Unkooperative Empfänger | Nicht unterstützte Hardware meldet sich als solche | klar «nicht geschützt», nie falsches GREEN-Statussignal |
| G8 Unabhängiges Audit | Provenienz, Reproduzierbarkeit, Security- und Safety-Evaluation | separate Reviewer und unabhängige Umsetzung |

Eine echte nachweisbare Schutzwirkung verlangt mehr als 0 Fehler in 28 künstlichen Fällen: vorregistrierte Stichproben, Ground Truth, Zeit-/Ressourcenmessungen, Unsicherheitsintervalle, Geräte-/OS-/Firmwarestände, Bypass- und negative Kontrollen. Diese Freigaben liegen **nicht** vor.

## 4. No-Go

Kein Einsatz mit realen Biometrieaufnahmen, Bewegungsprofilen oder Personenüberwachung; keine unkontrollierte Kameraerfassung, keine Militär-/Zielsystemkopplung. Kein Einsatz von `DENY`-Simulationsergebnissen als reale Sicherheitsgarantie. Vor Änderung bestehender v0.1-Spezifikation: formale Versions-/Review-Entscheidung.

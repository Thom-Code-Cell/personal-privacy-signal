# Vuzix-Testplan — dokumentierte Möglichkeiten und Nachweisgrenzen

Quellen am 21.10.2026 geprüft:

- [Vuzix Technical Details](https://support.vuzix.com/docs/m400-m4000-technical-details):
  nennt modifiziertes Android 11, Standard-Bluetooth/BLE und Android-Kamera-APIs.
- [Developer Resources](https://support.vuzix.com/docs/developer-resources):
  mehrere eigenständige Android-Brillen; Z100 dagegen Smartphone-Peripherie.
- [M400 Produktseite](https://www.vuzix.com/products/m400-smart-glasses):
  nennt auch Android-13-Perspektive und Grenzen künftiger OS-Sicherheitsupdates.
- [Android Bluetooth Permissions](https://developer.android.com/develop/connectivity/bluetooth/bt-permissions)
  und [Background BLE](https://developer.android.com/develop/connectivity/bluetooth/ble/background).
- [Vuzix Connectivity SDK](https://github.com/Vuzix/connectivity-sdk): optionaler
  Companion-Weg, keine Voraussetzung für den geplanten Standalone-Versuch.

Dokumente können unterschiedliche Firmwarestände beschreiben. Weder „Vuzix“ noch
„AOSP“ ersetzt Modell-/API-/Patchstandprüfung am realen Gerät. M400/M4000 sind
Kandidaten, keine Kaufempfehlung oder bereits validierte PPS-Empfänger.

## Gestufter Ablauf

| Stufe | Handlung und Nachweis | Gate |
|---|---|---|
| V0 Dokumente | Modell, Firmwarezweig, Patchversorgung, SDK-Lizenz und vorhandenes Leihgerät klären | keine Kosten; sonst warten |
| V1 Inventar | auf autorisiertem Gerät Modell, API, Build-Fingerprint, Patchdatum, BLE-Features und Permissions erfassen | keine Personen-/Accountdaten exportieren |
| V2 eigene App | lokale Debug-App als sichtbarer T0-Receiver, keine Kamera-/Mikrofon-Permission im BLE-Test | Installation/Entfernung reversibel; kein Device-Admin |
| V3 Discovery | bekanntes 17-Byte-Service-Payload, Scanfilter, Fehlframes, Anzeige, Stop/Restart | nur T0 melden, keine Bindung behaupten |
| V4 Lebenszyklus | P1/P2/P4, Screen-off, Permissionentzug, Akku und Hintergrundregeln | Ausfall sichtbar; keine Always-on-Zusage |
| V5 visuell | separate explizite Kamerafreigabe in eigener Forschungs-App, flüchtige Markeranalyse | P3/P5, Kamera danach nachweislich geschlossen |
| V6 unabhängig | unabhängige Implementierung und Geräteeigentümer wiederholen Protokoll | erst dann Fremdgeräte-Evidenz |

Inventar beispielsweise über autorisiertes USB-Debugging und Android-Systeminfos;
keine Seriennummern in öffentliche Logs. Feature `android.hardware.bluetooth_le`,
Bluetooth-Zustand und gegebenenfalls Advertising-Unterstützung tatsächlich abfragen.
BLE-Service-UUID/Herstellerkennung ist im Python-17-Byte-Parser nicht spezifiziert:
für Labortests temporäre, dokumentierte Test-Service-UUID verwenden und nicht als
registrierte PPS-Kennung ausgeben. Kein fremdes Herstellerpräfix beanspruchen.

Android 12+ beim passenden targetSdk: BLUETOOTH_SCAN, ggf. CONNECT/ADVERTISE zur
Laufzeit. Ältere Versionen haben andere Bluetooth-/Standortanforderungen.
`neverForLocation` nur bei zutreffender Aussage einsetzen; Raumforschung kann eine
solche Aussage ausschliessen und die Option kann Beacon-Ergebnisse filtern.
Minimalrechte je Stufe, Denial/Entzug immer testen. Hintergrundstarts sind durch
OS-Version und App-Lebenszyklus begrenzt; sichtbarer manueller Start ist die Baseline.
Keine Google-Play-Services-Abhängigkeit für den AOSP-BLE-Basistest vorsehen.

## Nachweisformular und Nichtbehauptungen

Für jeden Lauf: Klasse A oder F, Eigentümerfreigabe, Modell/Firmware/API/Patch,
APK-Hash/Commit, targetSdk, gewährte Rechte, Startart, Scanparameter, erwarteter und
beobachteter Hinweis, p95/FP/FN, Energie, Offlinezustand und Grenzen dokumentieren.
Screenshots nur mit synthetischem Inhalt. Deinstallation der Test-App und Rücknahme
der eigens gewährten Rechte am Ende; keine vorhandenen Apps/Konten zurücksetzen.

Standard-Android-Kamera-APIs betreffen die eigene autorisierte App. Sie belegen
keine Sperrung anderer Apps, keine Steuerung fremder Brillen und keinen OS-/Firmware-
Enforcement-Hook. Tatsächliche Unterbindung von Capture, Upload oder Modelltraining
braucht separat belegte Hersteller-/OS-Integration und unabhängige Messung.
Aktueller Stand: kein Vuzix-Gerät getestet, keine Android-APK gebaut.

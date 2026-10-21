# Reproduzierbare Testprotokolle

## Gemeinsamer Ablauf

Nur kontrollierter, geschlossener Forschungsraum mit volljährigen freiwilligen
Teilnehmenden; Café und Toiletten werden nachgestellt, niemals unbeteiligte Gäste
oder reale Toilettennutzer aufnehmen. Vorher [Einwilligungsablauf](consent.md),
Betreiberzustimmung, lokale Datenschutzprüfung und Stop-Kriterien abschliessen.
Akustik ist optional und standardmässig aus. Keine Gesichtserkennung oder echten
personenbezogenen Präferenzprofile. Pseudonyme Trials statt dauerhafter Sender-IDs.

1. Commit, Geräte-/OS-/Firmware-/SDK-Version, Konfiguration, Energiezustand und
   App-Hash erfassen. Raumskizze ohne echte Adresse, Wandmaterial, Abstände,
   Ausrichtung, Lichtpegel und Störquellen lokal festhalten.
2. Synthetic-, Android- oder Fremdgeräteklasse vorab markieren. Sender/Receiver und
   Beobachterrollen trennen. Ground Truth aus vorbereiteter Szenarioliste, ohne Video.
3. Baseline mit deaktiviertem Signal und anschliessend einzeln BLE, visuell und
   optional Audio testen; Kombination erst danach. Reihenfolge mit Seed 20261021
   randomisieren, geplante Reihenfolge im lokalen Log bewahren.
4. Uhrenvergleich vor/nach Session, 10-s-Reset ohne aktive Signalreste zwischen
   Trials; je 5 s vor und 10 s nach Ereignis beobachten. Timeout im Loss-Test separat.
5. Mindestens 30 Trials je Bedingung/3 Sessions explorativ; bestätigende Stichprobe
   nach Agenda. Kein Pooling von Räumen, Geräten oder Sichtbedingungen zur Gate-Umgehung.
6. CSV-Vorlage verwenden; fehlende Ergebnisse NOT_MEASURED, Abbruchgrund erfassen.
   Zusammenfassung mit TP/FP/FN/TN, Ambiguität, Latenz, Ressourcen und Intervallen.
7. Bei unerwarteter Aufnahme/Upload, Reidentifikation, Unwohlsein, gefährlicher
   Ablenkung oder unerlaubtem Publikum sofort abbrechen und lokale Daten sichern/löschen.

Protokollparameter sind Vorschläge für geschlossene Versuche, keine Leistungszusagen.
Vor Testbeginn Gerätefähigkeit und begründete Änderungen dokumentieren.

## P1 — Café / Discovery nach Transport (H-BLE, H-VIS, H-AUD)

Aufbau: 6 × 8 m nachgestellte Sitzfläche, 1/4/8 Freiwillige oder zunächst Dummies;
Senderabstände 0,5/2/5 m, frontal/90°/verdeckt, ruhige und belegte Situation.
Für QR 100/300/700 lux und 0°/30°/60° festlegen, Markergrösse und Optik messen.
BLE-Advertising-Intervall, Scanmodus und TX-Leistung protokollieren, keine
universellen Werte voraussetzen. Audio nur nach Freigabe, mit kalibriertem Pegel
und genehmigtem Maximalwert; PCM-Amplitude ist kein Schalldruckmesswert.

Signalstart/Eintritt auslösen, Empfang und sichtbaren Hinweis getrennt messen.
Negativtrials ohne Signal und mit fremden Mustern gleich verteilen. Kriterien aus
Agenda je Zelle prüfen; Fehlalarme/Audio zusätzlich über mindestens 3 Stunden
Hintergrundmaterial ohne Sprache von Teilnehmenden. Grenze: Sichtbarkeit und
Empfang beweisen keine Personenzuordnung oder rechtliche Einwilligung.

## P2 — benachbarte Toilette / Nebenraum (H-ROOM)

Zwei nachgestellte Räume mit dokumentierter Trennwand, Tür offen/geschlossen;
Sender jeweils in Raum A/B, Receiver auf beiden Seiten, 0,5/2/5 m zur Wand.
Türdurchtritt und Verweilen separat. Stärkstes RSSI als explizit unsichere Baseline
mit manuell bestätigtem, lokalem Zonenanker vergleichen. Bodenplan-Ground-Truth
kommt vom Beobachter, nicht aus dem Funkmodell. Echos und Multipath dokumentieren.

Zählen: falscher Raum, falsche Hausregel, unbekannter Raum, Wechselverzögerung.
Gate: keine als sicher ausgegebene Zone ohne unabhängigen Nachweis; empirisches
<1%-Gate erst mit bestätigender Stichprobe. Toilette bleibt ohne Smartphone durch
Beschilderung, Betreiberregel und kontrollierte Betriebsprozesse geschützt.
BLE-Empfang durch die Wand ist ein erwartbarer Fehlerfall, keine lokale Autorität.

## P3 — mehrere Personen / Binding / Konflikte (H-BIND, H-CONFLICT)

2/4/8 Subjekte; nur eine, mehrere oder alle mit widersprüchlichen Präferenzen.
Gekreuzte Laufwege, Sichtverdeckung, Badge-Tausch, zwei Kopien desselben Markers,
naher fremder Sender und entferntes sichtbares Subjekt. Synthetische Binding-
Kandidaten zuerst; kein automatisches BOUND allein aus RSSI/QR-Syntax.
Explizite Challenge ist nur ein Forschungskandidat und kein implementiertes T2.

Für jedes geschützte Objekt Ground Truth und Ausgabe UNBOUND/AMBIGUOUS/BOUND
getrennt notieren. Konflikte: Person unset vs. Hausregel deny; zwei Hausregel-
Herausgeber; signierte, aber nicht räumlich belegte Hausregel; anwendbare strengere
Regel vs. authentische permissive Regel. Unbekannte Anwendbarkeit bleibt unbekannt.
Gate: 0 permissive Upgrades, 0 automatische Auswahl bei mehreren plausiblen Subjekten;
Fehlbindung und Abdeckung wie Agenda. Keine Behauptung, dass Beschilderung allein
eine absichtlich nicht kooperierende Fremdkamera technisch stoppt.

## P4 — Signalverlust / Lebenszyklus (H-LOSS)

Sender aus, Bluetooth aus, Permission entziehen, Display aus, App Hintergrund,
Prozessneustart, Batteriemangel und Netzwerk weg einzeln testen. Forschungskonfiguration:
5-s-Presence-Timeout, 60-s-Marker-Gültigkeit; beides protokolliert, keine Normwerte.
Ereignisse unmittelbar vor/nach Timeout, Systemuhrsprung ±10 min, monotone
Fristen, wiederholte alte Pakete und Wiederkehr eines frischen Senders prüfen.

Gate: alte Frames verlängern keine authentifizierte Gültigkeit; unbekannter Zustand
sichtbar innerhalb 2 s nach Timeout, keine Aufnahmeerlaubnis aus Verlust/Expiry.
App-Neustart darf keinen alten verifizierten Zustand wiederherstellen.
Messen: stale acceptance, Übergangszeit, Hintergrundausfälle. T0-epoch_hint liefert
keine Replay-Sicherheit; dieses Gate ist mit dem aktuellen Parser allein nicht erfüllbar.

## P5 — Manipulation / Ressourcen (H-ATTACK)

Offline: falsche Länge/Version, reservierte Werte, Trunkierung, 10 000 Seed-Frames.
Nach T1-Implementierung: Bitänderung signierter Policy, falscher Schlüssel,
abgelaufen/revoziert, Replay, Relay zwischen Räumen, kopierter QR, Sybil-Sender.
QR-Ziele: falscher Betreiber, Redirect zu fremdem Host, lokale/interne URL,
überlange Antwort und Timeout; nur eigene Testserver, kein fremdes Netz scannen.
Offline-Bundles separat mit falscher Uhr/abgelaufenem Schlüssel prüfen.

Ressourcenlast synthetisch in isoliertem Prozess: 1/10/100/1000 Frames/s je 60 s,
CPU/RAM/Queue und Benutzerhinweise messen. Vor Hardwarelauf konkretes Budget
aus Idle-Baseline festschreiben (Vorschlag RAM-Zuwachs <10 MB, Queue ≤100,
keine unbeschränkten Prompts); bei Überschreitung abbrechen. Keine Funkstörung
oder öffentliches Flooding. Gate: kein Absturz/Trust-Upgrade und alle Budgets erfüllt.
Der aktuelle Korpus ist Parser-Stabilität, kein gemessener Flood-/Relay-Nachweis.

## P6 — Offline-Hausregeln / Schutz ohne Smartphone (H-OFF)

Gedruckte verständliche Regeln und zugängliche Alternative am Eingang; Smartphone
abwesend/aus; Policy lokal vorab geladen und Netzwerk vollständig getrennt.
Person ohne Sender darf nicht als zustimmend gelten. Tests: gültiges lokales Bundle,
unbekannter Betreiber, falsche Zone, abgelaufen, Widerruf nicht aktuell prüfbar,
Uhr unzuverlässig, konkurrierende Regeln, Aus-/Wiedereintritt und Notfallprozess.

Gate: tatsächliche Offline-Anzeige nur mit dokumentierter Herkunft/Frischegrenze;
unklare Regeln nie „verifiziert“ nennen; restriktiver Betriebsfallback ohne
Aufnahmeeinwilligung. Signatur beweist weder Standort noch Hausrechtsbefugnis.
Verständnis mit fünf neutralen Fragen erheben, ≥90% richtige Antworten als
exploratives Ziel; keine personenbezogenen Antworten zentral sammeln.
Grenze: Offline-Revokation kann veraltet sein, universelle Durchsetzung ist unbelegt.

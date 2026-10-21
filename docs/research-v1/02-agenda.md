# Forschungsagenda mit falsifizierbaren Hypothesen

Alle Schwellen vor Messbeginn festschreiben; Änderungen als neue Protokollversion.
Keine Hypothese gilt durch dieses Paket als bestätigt. TH Analytica verantwortet
Methodik und Implementierung; unabhängige Prüfer und Laborleitung sind unbesetzt.

| ID | Hypothese und Vergleich | Messgrösse und vorläufiges Gate | Protokoll |
|---|---|---|---|
| H-BLE | Lokale BLE-Discovery liefert im Café rechtzeitig Hinweise, ohne Personenbindung | je Distanz/Belegung mindestens 95% erkannt binnen 2 s; p50/p95 Latenz, Ausfallquote, Energie | P1 |
| H-ROOM | BLE allein reicht nicht zur zuverlässigen Trennung benachbarter Räume | Gegenhypothese Raumdetektor nur akzeptieren bei oberer 95%-Grenze falscher Raumzuordnung <1%; RSSI-Baseline gegen bestätigte Zonenbindung vergleichen | P2 |
| H-VIS | Sichtbarer Marker ist räumlich gezielter erkennbar als BLE, aber kein Identitätsbeweis | Erkennung ≥95% binnen 2 s je Licht/Winkel; Fehlzuordnung separat <1% obere 95%-Grenze; kopierte Marker dürfen nie BOUND ergeben | P1/P3/P5 |
| H-AUD | Optionales Tonsignal ist unter definierter Störung erkennbar | Sensitivität ≥95%; falsche Events ≤1/Stunde mit Konfidenzintervall; kein Personen-/Raumbeweis | P1/P3/P5 |
| H-BIND | Explizite lokale Challenge plus geometrischer Bezug reduziert Fehlbindung gegenüber stärkstem RSSI | Verwechslungen obere 95%-Grenze <1%, Unbound-/Abbruchquote und Abdeckung separat; 0 freigebende Entscheidungen bei Ambiguität | P3 |
| H-LOSS | Verlust/Expiry hebt Restriktionen nicht automatisch auf | 0 Übergänge zu Aufnahmeerlaubnis; Unsicherheitsanzeige binnen 2 s ab festgelegtem Timeout | P4 |
| H-ATTACK | Malformed/Replay/Relay können keine höhere Vertrauensstufe erzeugen | 0 T1/T2/Permission-Upgrades; CPU, RAM, Queue begrenzt | P5 |
| H-OFF | Hausregeln und Schutz ohne Smartphone bleiben offline verständlich | 100% ungeklärte Herkunft/Expiry als unbekannt anzeigen; ≥90% korrektes Verständnis bei zugänglicher Beschilderung | P6 |
| H-CONFLICT | Restriktionen werden bei Mehrpersonen-/Hausregelkonflikten nicht freigebend aufgelöst | 0 Freigaben durch unset Bits, widersprechende Sender oder permissive Person bei strengerer anwendbarer Hausregel | P3/P6 |

## Auswertung

Ein Trial ist ein vorab geplanter Zustandswechsel mit Ground Truth eines separaten
Beobachters, nicht jedes empfangene BLE-Paket. Sensitivität = TP/(TP+FN), Fehlalarmrate
= FP/negative Beobachtungszeit, Fehlbindung = falsch gebundene Trials/gebundene Trials.
Zusätzlich korrekt gebunden/alle Trials und AMBIGUOUS/alle Trials berichten: ein
System, das alles ablehnt, besteht keine Nutzbarkeitsprüfung durch niedrige Fehlbindung.
Latenz vom geplanten Eintritt/Signalstart bis sichtbarem Hinweis, monotone Uhr;
Synchronisationsfehler dokumentieren. Energie gegen gleich langen Idle-Lauf vergleichen.

Explorativ mindestens 30 randomisierte Trials je Bedingung über drei Sessions.
Für ein <1%-Fehlergate mindestens 300 unabhängige Trials der kritischen Bedingung
mit null Fehlern (einseitige exakte 95%-Obergrenze ca. 0,994%); Cluster nach Person,
Gerät und Session berücksichtigen. Wiederholte Pakete sind nicht unabhängig.
Bei Fehlern exakte Binomialintervalle berechnen und Stichprobe neu planen;
keine günstigen Untergruppen nachträglich wählen. Null akustische Fehlalarme über
3 Stunden ergeben eine Poisson-Obergrenze von ca. 1/Stunde, nur unter passender
Unabhängigkeitsannahme. Feldstörungen und Cluster können mehr Daten verlangen.

## Offene Forschungsentscheidungen

Markerrotation vs. Druckbadge/Barrierefreiheit; explizite Challenge ohne biometrische
Identität; rechtmässige Raumautorität und Revokation offline; EID-/Schlüsselrotation;
Anti-Relay ohne falsche Distanzbehauptung; konkrete Ressourcenbudgets je Hardware;
akustische Zumutbarkeit. Keine dieser Fragen wird mit BLE-RSSI oder einer Signatur allein gelöst.

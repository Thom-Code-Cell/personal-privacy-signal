# Datenschutzanforderungen und Threat-Model-Ergänzung

Ergänzt die bestehenden SR-* Anforderungen und T01–T15, ersetzt sie nicht.
Assets: körperliche Privatsphäre, Präferenzintegrität, Unverknüpfbarkeit,
Verfügbarkeit und korrekte Anzeige der tatsächlichen Durchsetzung.
Angreifer: passiver Tracker, kopierender Sender, Relay/Sybil, kompromittierter
Betreiber/Receiver, absichtlich nicht kooperierender Kameranutzer.
Vertrauensgrenzen: Person/Badge → Radio/Optik/Audio → Parser → Auth/Frische →
Binding/Zone → Policy → eigene App → fremde App/OS/Firmware → Cloud.

| ID | Anforderung | Verifikation / Grenze |
|---|---|---|
| RV-01 | Schutz darf kein Smartphone, Konto oder aktiven Sender voraussetzen | P6 mit Person ohne Gerät; Hausregel und zugängliche analoge Alternative |
| RV-02 | Keine zentrale Sammlung persönlicher Präferenzen, Scan-/Bewegungshistorien oder biometrischen Templates | Datenflussreview, Netzverkehrsmessung und lokale Speicherprüfung vor Personenversuch |
| RV-03 | Keine stabilen transportübergreifenden Personenkennungen; rotierende IDs trotzdem als potenziell verknüpfbar behandeln | Tracking-/Korrelationsreview, keine Identitätsaussage aus Rotation |
| RV-04 | Nur notwendige Rechte, flüchtige Verarbeitung; kein verstecktes Mikrofon und keine Cloud-OCR | Rechte-/Netzwerk-/Dateiprüfung je Gerätebuild |
| RV-05 | Signatur, Frische, Subject Binding, räumliche Autorität und Enforcement getrennt ausweisen | P2/P3/P5/P6, getrennte Zustandsfelder |
| RV-06 | Unbekannt/Mehrdeutig/Verlust/fehlender Sender nie als Zustimmung werten | P3/P4; keine Aufnahmefreigabe aus Null-Flags |
| RV-07 | Umgehung über deaktivierten Receiver, alternative Kamera-App oder Uploadpfad untersuchen | Hersteller-/OS-Gate; reine App kann Bypass nicht verhindern |
| RV-08 | Online-Revokation nicht offline behaupten; begrenzte Gültigkeit, sicherer Uhrzustand und restriktiver Fallback | P6 und P4 mit alter Policy/Uhrfehler |
| RV-09 | Eingabegrösse, Parserarbeit, Queue, Retries und Prompts begrenzen | P5, Budget je Gerät vorab fixieren |
| RV-10 | Notfallausnahme nur separat autorisiert, zweck-/zeitbegrenzt und minimal auditiert | keine anonyme Nachricht als Ausnahmetoken; unabhängige Review |
| RV-11 | Fremdgeräte ohne Integration dürfen nicht als geschützt ausgegeben werden | Kennzeichnung advisory/unsupported; kein grünes „geschützt“ bei blossem Empfang |
| RV-12 | Teilnehmerdaten und Korrespondenz bleiben ausserhalb öffentlicher Git-Historie | Review vor jedem Push; nur synthetische Fixtures/aggregierte Befunde |

## Angriffe und Behandlung

Tracking: rotierende EIDs reduzieren direkte stabile Kennungen, verhindern aber
keine Funkfingerprints, räumliche Korrelation oder kopierte sichtbare Badges.
Replay/Relay: authentische Bytes können ausserhalb der richtigen Zone auftauchen;
Challenge/Expiry allein beweist keine Distanz. Subject Binding darf erst nach
definiertem unabhängig geprüftem Profil T2 heissen.

Confused deputy: eine signierte Hausregel eines unberechtigten Herausgebers oder
aus dem Nebenraum darf keine lokale Autorität erben. Trust-Registry und räumlicher
Nachweis sind getrennt zu prüfen; Registry darf keine persönliche Präferenzdatenbank
werden. QR-URLs zusätzlich auf Host, Redirect, interne Ziele, Grösse und Timeout
begrenzen, bevor ein Netzwerkclient eingesetzt wird.

Downgrade: unbekannte Semantik nicht still als geringere Restriktion lesen.
Diese PR-Vorbereitung lehnt unbekannte Policy-Versionen und reservierte Bits ab.
Keine Behauptung einer vollständigen Policy-Engine.

Bypass: Software ohne Kontrolle über andere Apps kann deren Aufnahmen nicht
unterbinden. Für echte Umgehungssicherheit sind OS-/Firmware-Vertrauensgrenze,
Boot-/Update-Schutz, Schlüsselverwaltung und Prüfung sämtlicher nachgelagerter
Pfade erforderlich. Bis dahin NO-GO für Durchsetzungsversprechen.

Datenschutzprüfung vor Personenversuch: Verantwortlichkeit, Rechtsgrundlage,
Information, Aufbewahrung, Betroffenenrechte, DPIA-Bedarf und Akustik-/Sensorregeln
lokal fachlich klären. Dies sind Review-Anforderungen, keine Rechtsauskunft und
keine Behauptung rechtlicher Wirkung des PPS-Signals.

# P8: Vertrag für künftige Smartphone- und Gebäudeadapter

**Entwurf. Kein vollständiger API-Vertrag. Keine implementierten Plattformadapter.**

## A. Smartphone

Eingaben der zukünftigen lokalen Wallet: Restriktionspolicy, einmalige Challenge des bekannten Empfängers, Ablaufzeit einer nicht nachverfolgbaren Sitzung, gewählte freiwillige Interaktion. Keine Fotos, Face Templates, nationalen IDs, Telefonnummern, MAC-Adressen oder absoluten Aufenthaltsorte.

Ausgaben **nur** bei erfolgreicher freigegebener OS-Aktion und implementierter Signatur: Sitzungsnachweis mit Policy-Digest, Nonce, Empfänger-/Kontextbindung, kurzer Frist, überprüfbarer Herausgeber-/Schlüsselrolle. Verschiedene Empfänger sollen keinen gemeinsam stabilen Identifier sehen. Alle Konzepte für Schlüsselausgabe, Signature-Suite, Revokation, Kollisions-/Relay-Widerstand und Schutz vor Tracking bleiben zur Normierung offen. Ein einfacher Pass/Fail-Rückgabewert darf **nicht** als vollwertiges extern überprüfbares Token verkauft werden.

### Mögliche Plattformfunktionen

- iOS: `LocalAuthentication`; ggf. Keychain/Secure Enclave für autorisierte Schlüsseloperationen.
- Android: `BiometricPrompt` + `CryptoObject` / Android Keystore, vorzugsweise starke Authentisierung, soweit unterstützbar.

**Wichtig:** Lokale Gerätefreigabe ist weder Identität noch Proof-of-Presence vor einem anderen Sensor. Keine behauptete App-Betriebsbereitschaft.

## B. Standort und geschützte Räume

Die Website kann ein einfach lesbares Policy-Dokument veröffentlichen, aber sie liefert nur eine Informationsebene. Für einen gültigen Enforcement-Geltungsbereich braucht ein zukünftiges Gerät getrennte Prüfschritte:

1. Wer beansprucht welche Hausregel (Issuer / Betreiber, Schlüsselherkunft)?
2. Ist die Schlüssel-/Regelfassung gültig, unverändert, aktuell und widerrufbar?
3. Ist dieser Issuer tatsächlich für **diesen Raum** zuständig? Keine Autorität allein durch eine Domain.
4. Ist das Gerät zuverlässig in **diesem Raum**, nicht bloss nebenan oder im Empfangsbereich?
5. Welche Bearbeitungsoperation soll gesteuert werden, und kann die Herstellertechnik sie tatsächlich steuern?

Nur wenn 1–5 nachvollziehbar sind, darf «verifiziert und anwendbar» berichtet werden. Eine geschlossene Tür, ein anderer Raum oder ausgefallene Funktechnik erzeugen niemals automatisch den Status «verifiziert». Das gilt auch für signierte Website-/JSON-Dateien.

## C. Nicht erlaubte Schnittstellen und Artefakte

Kein `/identify-person`, `/upload-face`, `/global-person-location`, `/civilian-classification`, `/targets` und keine Personenstandortabfrage. Kein Zentralserver mit Face-Embeddings, Biometrie-IDs oder GPS-Spuren. Keine API zur Steuerung von Waffen, Drohnen oder militärischer Zielauswahl. Keine «Deny-Aktion» an nicht kooperierende Systeme behaupten.

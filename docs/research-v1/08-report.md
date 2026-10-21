# Abschlussbericht · PPS Research & Validation Package v1.0

Stand: 21.10.2026, TH Analytica. Lokales Reviewpaket fertig; Veröffentlichung,
öffentliche PR, Merge und Produktionsfreigabe nicht erfolgt.

## Lieferumfang und technische Änderung

Alle sechs angeforderten Arbeitsbereiche sind unter [Paketindex](README.md)
versionierbar abgelegt. P1–P6 decken Café, Nebenraum/Toilette, mehrere Personen,
Signalverlust, Manipulation und Offline-Hausregeln ab. CSV und Einwilligungsablauf
stehen für spätere genehmigte Messungen bereit; es wurden keine Messdaten erfunden.

Parserhärtung: unbekannte Policy-Version, reservierte Policy-Bits und reservierte
Capability-Bits führen jetzt zu explizitem ValueError statt teilweiser Interpretation.
Alle bekannten 17-Byte-v0.1-Frames behalten ihre Bedeutung und T0-Stufe.
Wire-Spec ergänzt die strengere Annahmeregel als datierte Klarstellung nach Freeze.
Bestehender Parser und Tests wurden für prüfbares Linting formatiert;
keine Kryptografie, Gerätebefehle oder Netzwerkzugriffe hinzugefügt.
Rollback ist ein Revert des lokalen Implementierungscommits; kein Datenmigrationsbedarf.

## Prüfresultate

Umgebung: Windows, Python 3.12.10, Ruff 0.14.1, Bandit 1.8.6.
Ausführbare Details und Exitcodes: `evidence/local-checks.txt`.

| Prüfung | Ergebnis | Aussagegrenze |
|---|---|---|
| ursprüngliche Baseline | 4/4 PASS vor Änderung | ursprüngliche T0-Tests |
| finale Unit-Tests | 10/10 PASS | 6 zusätzliche Testmethoden mit Teilfällen |
| gültige Flagkombinationen | alle 256 PASS, T0 bleibt erhalten | keine Einwilligung/Bindung |
| unbekannte Versionen | alle 255 verworfen | Policy-Version 1 bleibt unterstützt |
| reservierte Felder | jedes der 8 Policy- und 4 Capability-Bits verworfen | keine vollständige Fuzz-Zustandsraumabdeckung |
| Seed-Korpus | 10 000 Bytestrings, Seed 20261021, Längen 0–64 | synthetischer Parsercheck, keine Funklastmessung |
| Ruff Lint/Format | PASS nach Formatierung | zuerst vorhandene Stilprobleme behoben |
| Bandit Produktionsparser | PASS, 0 gemeldete Befunde | statische Python-Muster, keine Krypto-/Geräteprüfung |
| Python-Kompilation | PASS | kein APK-/Firmware-Buildsystem vorhanden |
| git diff --check | PASS | Format-/Whitespacekontrolle |
| Runtime-Abhängigkeiten | nur Python-Standardbibliothek | QA-Tools separat installiert; kein vollständiger Supply-Chain-Audit |
| GitHub Security | siehe Inventar: Code Scan nicht vorhanden, Dependabot deaktiviert, Secret-Alerts [] | kein pauschales Security-PASS |
| CI/Preview/Deployment | NOT_RUN | kein vorhandener Workflow, keine Veröffentlichung |
| eigene Android-Tests | NOT_MEASURED | kein Gerätetest/APK in diesem Auftrag |
| Vuzix / echte Fremdgeräte | NOT_MEASURED | Herstellerdocs sind keine Hardwarevalidierung |

## Reviewstatus und Nachweise

Basiscommit: `17c278d48e6cf74ee81e0a23f80c3fa28c25b5f8`.
Arbeitsbranch: `research/pps-validation-v1`. Exakte lokale neue Commit-IDs stehen
im ausgelieferten `COMMIT-AND-HANDOFF.md`; sie werden nach Abschluss aus Git gelesen.
Ein PR-Entwurf liegt als `PR-DRAFT.md` bei. Es gibt keinen neuen PR-Link, da weder
Push noch öffentliche PR vorgenommen wurden. Das Zielrepository ist öffentlich;
die im Auftrag gesondert verlangte Zustimmung zur Veröffentlichung liegt nicht vor.
Bestehende Links: [offenes Issue #1](https://github.com/Thom-Code-Cell/personal-privacy-signal/issues/1),
[separater Website-PR #103](https://github.com/Thom-Code-Cell/th-analytica-2025/pull/103),
[Dependency-PR #104](https://github.com/Thom-Code-Cell/th-analytica-2025/pull/104).

Quellen und Einschränkungen: [Vuzix](04-vuzix.md), [Partner](06-partners.md),
[Bestandsaufnahme](01-inventory.md). Private Mailinhalte wurden nicht übernommen;
ein Connector-Suchversuch lieferte keinen auswertbaren Originalmail-Nachweis.

## Offene Punkte und Entscheidungen

- Öffentlichen Branch-Push und Draft-PR gesondert freigeben; kein Merge dadurch.
- Studienleitung, Datenschutzreview, unabhängigen Reviewer und Android-Verantwortung
  verbindlich benennen. Partnerrollen sind unbesetzt, keine Zusagen voraussetzen.
- Fehlende Originalbelege zu Android Mobile Binding und berichteter Korrespondenz
  lokal prüfen, bevor daraus externe Aussagen entstehen.
- Hardware-/Labor-/Audio-/Personenversuche mit realer Einwilligung und festgelegten
  Parametern durchführen; aktuelle Testresultate ausschliesslich Klasse S.
- T1-Key-/Freshness-/Recovery, T2-Binding, Zonenautorität, Offline-Revokation und
  Umgehungsschutz bleiben separate Forschungs- und Releaseblocker.

Produktion, Konten, Nutzerdaten und laufende Websitearbeiten wurden nicht geändert.
Keine kostenpflichtigen Dienste, Käufe, E-Mails, Merges oder Deployments ausgelöst.

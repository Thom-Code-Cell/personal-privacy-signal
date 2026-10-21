# PPS Research & Validation Package v1.0

TH Analytica · 21.10.2026 · Forschungsstand, keine Produktionsfreigabe.

**Research & Validation – Experimental.** Keine einsatzbereite Datenschutzlösung.
Android-, Vuzix- und echte Fremdgerätevalidierung stehen weiterhin aus.

## Inhalt

1. [Bestandsaufnahme und Evidenz](01-inventory.md)
2. [Forschungsagenda](02-agenda.md)
3. [Reproduzierbare Protokolle](03-protocols.md)
4. [Vuzix-Testplan](04-vuzix.md)
5. [Datenschutz und Threat Model](05-privacy-threat-model.md)
6. [Forschungspartner-Dossier](06-partners.md)
7. [Roadmap und Entscheidungen](07-roadmap.md)
8. [Abschlussbericht](08-report.md)
9. [Messvorlage](measurement-template.csv) und [Einwilligungsablauf](consent.md)

Dieses Paket ergänzt die v0.1-Kandidatenbasis. Es ändert keine Vertrauensstufen und
liefert keine T1/T2-, Rechtswirkungs-, Herstelleradoptions- oder Kamera-Sperrbehauptung.
Messziele sind vorläufige Forschungsschwellen, keine bereits gemessenen Resultate.
Die technische Änderung ist eine absichtliche Verschärfung bisher akzeptierter
unbekannter Semantik; bekannte v0.1-Frames bleiben kompatibel.

## Reproduktion ohne Hardware

Python 3.12 verwenden. Vom Repository-Stamm:

```text
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements-dev.txt
.venv/Scripts/python -m unittest discover -s conformance -v
.venv/Scripts/python -m ruff check receiver-kit conformance
.venv/Scripts/python -m ruff format --check receiver-kit conformance
.venv/Scripts/python -m bandit -r receiver-kit
.venv/Scripts/python -m compileall -q receiver-kit conformance
git diff --check
```

Unter Unix `.venv/bin/python` verwenden. Installation benötigt Paketdownload;
danach benötigen diese Prüfungen weder Netzwerk noch Konto, Radio, Kamera oder Mikrofon.
Kein Android-Projekt/Buildsystem liegt hier vor: Bytecode-Kompilation ist der
verfügbare Python-Buildcheck, kein APK- oder Firmware-Build.
Toolversionen sind direkt fixiert; transitive QA-Abhängigkeiten sind nicht vollständig
gelockt. Ein Produktions-Supply-Chain-Nachweis ist damit nicht erbracht.

## Evidenzklassen

| Klasse | Zulässige Aussage | Stand dieses Pakets |
|---|---|---|
| S — lokal/synthetisch | Parser-/Negativvektoren, deterministischer Zufallskorpus | ausgeführt, siehe Bericht |
| A — eigene Android-Tests | Gerät, Firmware, APK-Hash, Messprotokoll erforderlich | nicht durchgeführt |
| F — echte Fremdgeräte | unabhängiger Receiver/Hersteller, tatsächliche Verarbeitung prüfen | nicht durchgeführt |

Dokumentation und Fremdberichte sind keine ausgeführten Gerätetests. Fehlende Evidenz
bleibt NOT_MEASURED/BLOCKED; kein stilles Hochstufen durch grüne Softwaretests.

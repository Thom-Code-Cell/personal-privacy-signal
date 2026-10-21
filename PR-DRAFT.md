# Research & Validation – Experimental: PPS Package v1.0

**Experimental research only. Keine einsatzbereite Datenschutzlösung.**
Android-, Vuzix- und echte Fremdgerätevalidierung stehen aus.
Freigegeben ist ausschliesslich die öffentliche Draft-PR; kein Merge,
Produktionsupdate, E-Mail-Versand oder externe Ankündigung.

Der bisherige T0-Parser akzeptierte unbekannte Policy-Versionen und reservierte
Policy-/Capability-Bits. Solche Frames werden jetzt explizit zurückgewiesen;
gültige v0.1-Frames behalten Layout, Restriktionen und T0-Vertrauensstufe.
Die datierte Spec-Klarstellung macht die strengere Annahme nach dem Freeze sichtbar.

Das Forschungspaket ergänzt messbare BLE-/Visuell-/Audio-Hypothesen, Subject-Binding-
und Raumtests, reproduzierbare P1–P6-Protokolle, einen quellenbelegten Vuzix-Plan,
Datenschutz-/Threat-Model-Anforderungen, ein prospektives Partnerdossier und eine
Roadmap mit Verantwortungsrollen, Kostenrisiken und Go/No-Go-Gates.

Validierung lokal: 10 Python-Tests inklusive 256 gültiger Flagkombinationen und
10 000 deterministischer Fehleingaben; Ruff Lint/Format, Bandit und Bytecode-
Kompilation. Exakte Befehle/Exitcodes in docs/research-v1/evidence/local-checks.txt.
Keine Android-, Vuzix- oder echte Fremdgerätevalidierung. Kein T1/T2- oder
Enforcement-Nachweis; CI wurde nicht ausgeführt. Existierende Website-PRs bleiben
unverändert. Kein Merge oder Deployment angefordert.

Bezug: https://github.com/Thom-Code-Cell/personal-privacy-signal/issues/1
(wird durch Forschungsplanung nicht geschlossen).

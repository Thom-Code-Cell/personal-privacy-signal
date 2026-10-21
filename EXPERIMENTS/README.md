# Reproducible independent experiments

Reuse [P1–P6 protocols](../docs/research-v1/03-protocols.md),
[replication record](../docs/community/REPLICATION.md) and
[measurement CSV](../docs/research-v1/measurement-template.csv). Use the
[validation template](VALIDATION-TEMPLATE.md) for new bounded questions.

Open an issue; predeclare controls, acceptance thresholds and sample rationale.
Document deviations and negative findings. Start with synthetic fixtures. Human
or hardware trials need consent, operator authority, ethics/privacy review, stop
criteria and deletion rules; templates grant none of those approvals.

Only reviewed aggregates and synthetic artifacts enter PRs. Keep raw logs,
consents and reidentification keys outside Git/CI. Include experiment ID, exact
commits, artifact hashes and independent review. Distinguish SYNTHETIC_ONLY,
SIMULATOR, PHYSICAL_DEVICE and NOT_MEASURED. None implies production readiness.

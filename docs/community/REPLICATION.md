# Independent replication record

Use with [P1–P6](../research-v1/03-protocols.md) and the existing
[CSV schema](../research-v1/measurement-template.csv). Copy this template outside
Git for raw work; only publish synthetic inputs and reviewed aggregate results.

- Research question / hypothesis / protocol ID:
- Preregistered acceptance threshold, sample size and analysis method:
- Specification revision / full commit / date / implementation origin:
- Evidence class: SYNTHETIC_ONLY / SIMULATOR / PHYSICAL_DEVICE / NOT_MEASURED:
- Hardware model, firmware, OS, SDK and app hash (no serials or MAC addresses):
- Independent operator/reviewer role; conflicts/funding (optional public affiliation):
- Reproduction commands, tool versions, random seed and synthetic fixture path:
- Baseline/control, conditions, randomisation and clock uncertainty:
- Ground truth method (no video or biometrics), expected vs observed state:
- Trials by condition; TP/FP/FN/TN, ambiguity, wrong binding, missingness:
- Latency distribution/uncertainty; resource use; confidence interval method:
- Result: PASS / FAIL / BLOCKED / NOT_MEASURED and deviations/abort reason:
- Separate claims: receipt / authenticity / binding / policy / actual enforcement:
- Negative findings, limitations, reviewer and exact evidence artifact hashes:
- Privacy/ethics approval status; participant consent/withdrawal checked locally:
- Local retention deadline, access owner, deletion verification; publication review:

Do not prefill PASS. A successful T0 parse never supplies T1/T2 or device evidence.
Do not pool conditions to hide failures or publish small identifiable aggregates.
If independent reproduction is blocked, say what is missing rather than infer success.

## Data handling before any human trial

Name a local data custodian and set a justified retention/deletion date before
collection. Separate signed consent/contact keys from measurements; encrypt local
storage, limit access to the approved team and do not sync it into public or
unapproved cloud folders. Use trial IDs without an identity mapping in published
material. Withdrawals and deletion are handled by the local custodian; record
completion without publishing the participant's identity. Review metadata, small
cells and reidentification risk before releasing aggregates. A .gitignore is only
an accidental-add guard and does not protect previously tracked files or artifacts.

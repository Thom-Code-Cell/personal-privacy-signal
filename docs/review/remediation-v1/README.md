# Review remediation v1 — experimental

Follow-up to the AI preliminary review of PR #2 at
`3225cef446c3b0d1348ffab614ed4be154842ab3`, 2026-10-21. That scope was 56 files,
including a 22-file last addition. The [baseline manifest](baseline-scope.json)
preserves that exact set and hashes. Follow-up files are additional, not retroactive
changes to the reviewed snapshot. PR #2 remains Draft and its branch is preserved.

The same AI assisted implementation and review. This work and its second technical
check are **AI self-review, not independent external review**, certification or
rights-holder confirmation. No hardware experiment, outreach or production release.

- [All eight findings and remaining gates](FINDINGS.md)
- [Second technical check (AI self-review)](SECOND-REVIEW.md)
- [Current claims and security boundaries](CLAIMS.md)
- [Rights inventory and unresolved authority](RIGHTS.md), [file inventory](rights-scope.csv)
- [Preregistration requirements](ANALYSIS-PLAN.md)
- [External review reproduction and questions](REVIEW-PROTOCOL.md)
- [Origin evidence](origin-evidence.json)

## Reproduce without radio, camera, account or network API

Use the README virtual environment and development dependencies. Package installation
requires downloads; the following checks then run locally without provider calls:

```sh
python -m unittest discover -s conformance -p 'test_*.py' -v
python tools/check_policy_mutations.py
python tools/check_review_evidence.py
python tools/check_community_docs.py
python -m ruff check receiver-kit conformance tools
python -m ruff format --check receiver-kit conformance tools
python -m bandit -r receiver-kit -q
git diff --check
```

Expected: 15 tests; 28 pairwise meaning swaps detected; origin/rights/baseline
evidence checks PASS. The structured test has 4,352 byte mutations: 2,837 accepted
as T0 and 1,515 rejected with specified reasons. All 256 policy combinations are
checked against exact spec-derived meanings. The older 10,000-random-frame test
remains a shallow malformed-input check, not measured radio/flood coverage.

The vectors are independent of parser constants, but not an independently authored
implementation or external validation. The mutation tool temporarily changes only
the loaded mapping in its process and restores it; it writes no receiver files.
CI must pass on the follow-up head; parent-PR CI is not evidence for this delta.

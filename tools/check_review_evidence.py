"""Check recorded source content and inventory completeness; never attest IP rights."""

import csv
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs/review/remediation-v1"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def digest(content):
    return hashlib.sha256(content).hexdigest()


def check():
    scope = json.loads((REVIEW / "baseline-scope.json").read_text(encoding="utf-8"))
    names = (
        git("diff", "--name-only", scope["base"], scope["head"]).decode().splitlines()
    )
    last = set(
        git("diff", "--name-only", scope["previous"], scope["head"])
        .decode()
        .splitlines()
    )
    assert len(names) == 56 and len(last) == 22
    assert names == [item["path"] for item in scope["files"]]
    for item in scope["files"]:
        assert (
            digest(git("show", f"{scope['head']}:{item['path']}"))
            == item["sha256_git_blob_content"]
        )
        assert item["last_addition_22"] == (item["path"] in last)

    origin = json.loads((REVIEW / "origin-evidence.json").read_text(encoding="utf-8"))
    for record in origin["records"]:
        raw = git("show", f"{record['revision']}:{record['path']}")
        assert digest(raw) == record["sha256"]
        assert (
            git("show", "-s", "--format=%aI", record["revision"]).decode().strip()
            == (record["recorded_author_date"])
        )
        assert all(needle in raw.decode("utf-8") for needle in record["required_text"])

    tracked = set(git("ls-files", "-z").decode().rstrip("\0").split("\0"))
    with (REVIEW / "rights-scope.csv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == len({row["path"] for row in rows}), "Duplicate rights rows"
    assert {row["path"] for row in rows} == tracked, (
        "Update inventory for tracked files"
    )
    for row in rows:
        assert row["holder_confirmation"] == "PENDING_NOT_ATTESTED"
        assert row["third_party_clearance"] == "NOT_ASSESSED"
        if row["origin_revision"] != "FOLLOWUP_PROPOSED":
            assert row["origin_revision"] == scope["head"]
            assert (
                digest(git("show", f"{scope['head']}:{row['path']}"))
                == row["baseline_sha256"]
            )
        else:
            assert not row["baseline_sha256"]
    print(
        f"PASS: baseline 56/22, {len(origin['records'])} origin sources, "
        f"{len(rows)} inventory rows; legal authority remains pending"
    )


if __name__ == "__main__":
    check()

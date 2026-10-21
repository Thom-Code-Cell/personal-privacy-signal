"""Validate community entry links and preservation of the published license."""

import re
import subprocess
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
BASE = "2db356552e62581f46cacb9d770760f4de76d782"
expected = subprocess.check_output(["git", "show", f"{BASE}:LICENSE.md"], cwd=ROOT)
assert (ROOT / "LICENSE.md").read_bytes().replace(b"\r\n", b"\n") == expected.replace(
    b"\r\n", b"\n"
), "Published license changed: explicit rights decision required"
paths = [
    ROOT / name
    for name in (
        "README.md",
        "CONTRIBUTING.md",
        "GOVERNANCE.md",
        "CODE_OF_CONDUCT.md",
        "SECURITY.md",
    )
] + sorted((ROOT / "docs/community").glob("*.md"))
checked = 0
for path in paths:
    content = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        if "://" in target or target.startswith("#"):
            continue
        local = unquote(target.split("#", 1)[0])
        resolved = (path.parent / local).resolve()
        assert resolved.is_relative_to(ROOT), f"Escaping link: {path}: {target}"
        assert resolved.is_file(), f"Broken link: {path}: {target}"
        checked += 1
print(
    f"PASS: {len(paths)} community documents, {checked} local links, license unchanged"
)

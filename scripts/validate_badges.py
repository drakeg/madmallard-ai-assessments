"""Validate stack-specific and dynamic badges without network calls."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
readme = (root / "README.md").read_text()
start, end = "<!-- madmallard-badges:start -->", "<!-- madmallard-badges:end -->"
assert readme.count(start) == readme.count(end) == 1
assert readme.index(start) < readme.index(end) < readme.index("## Modules")
block = readme.split(start, 1)[1].split(end, 1)[0]
for name in ("Python", "FastAPI", "Docker", "Docker%20Compose"):
    assert f"badge/{name}-" in block, f"Missing badge {name}"
for path in ("actions/workflows/ci.yml/badge.svg", "github/issues/", "github/issues-pr/"):
    assert path in block, f"Missing dynamic badge {path}"
assert "github/license/" not in block or (root / "LICENSE").exists()
assert "github/v/release/" not in block, "No published release verified"
assert "PostgreSQL-" not in block, "PostgreSQL is not yet deployed"
assert "Vercel-" not in block, "Vercel is not configured"
assert "passing-" not in block.lower()
images = re.findall(r"\[!\[[^]]+\]\((https?://[^)]+)\)\]\((https?://[^)]+)\)", block)
assert len(images) >= 7, "All badges must be clickable"
print("Badge validation passed")

"""Atomically initialize or update the claim ledger from a JSON source file."""
import json
from pathlib import Path
import sys

if len(sys.argv) == 2:
    data = json.loads(Path(sys.argv[1]).read_text())
else:
    data = {
        "outcome": "no-progress",
        "summary": "Attempt in progress; no verified claim yet.",
        "claims": [],
        "next_step": "Audit the energetic comparison and certify a rational trial within its justified scope.",
    }
destination = Path("claims.json")
temporary = destination.with_suffix(".json.tmp")
temporary.write_text(json.dumps(data, indent=2) + "\n")
temporary.replace(destination)

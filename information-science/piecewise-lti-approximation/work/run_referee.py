#!/usr/bin/env python3
"""Run the explicitly requested read-only referee; bind its reviewed proof bytes."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
SCRATCH = ROOT.parents[1] / "scratch" / "ai4s-piecewise-lti-approximation"
round_name = "referee2" if sys.argv[1:] == ["2"] else "referee"
prompt_path = ROOT / "evidence" / f"{round_name}-prompt.txt"
proof_path = ROOT / "proof.md"
command = [
    "codex", "exec", "-m", "gpt-6.1-sol", "-c", "model_reasoning_effort=max",
    "--sandbox", "read-only", "--ephemeral", "--skip-git-repo-check",
    "-C", str(ROOT), "-o", str(SCRATCH / f"codex-{round_name}.md"),
    prompt_path.read_text(),
]
receipt = {
    "command": command,
    "cwd": str(ROOT),
    "stdin": "DEVNULL",
    "proof_sha256_before": hashlib.sha256(proof_path.read_bytes()).hexdigest(),
    "readme_sha256_before": hashlib.sha256((ROOT / "README.md").read_bytes()).hexdigest(),
    "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
    "started_unix": time.time(),
    "time_limit_seconds": 2700,
}
with (SCRATCH / f"codex-{round_name}-stdout.log").open("w") as out, (SCRATCH / f"codex-{round_name}-stderr.log").open("w") as err:
    try:
        result = subprocess.run(command, cwd=ROOT, stdin=subprocess.DEVNULL,
                                stdout=out, stderr=err, timeout=2700, check=False)
        receipt["returncode"] = result.returncode
    except subprocess.TimeoutExpired:
        receipt["returncode"] = "TIMEOUT"
receipt["finished_unix"] = time.time()
receipt["proof_sha256_after"] = hashlib.sha256(proof_path.read_bytes()).hexdigest()
(ROOT / "evidence" / f"{round_name}-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))

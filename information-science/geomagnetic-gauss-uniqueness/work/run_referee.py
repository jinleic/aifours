"""Run the explicitly requested read-only referee and bind its input snapshot."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
SCRATCH = ROOT.parents[1] / "scratch" / "ai4s-geomagnetic-gauss-uniqueness"
parser = argparse.ArgumentParser()
parser.add_argument("--round", type=int, choices=(1, 2), default=1)
suffix = "" if parser.parse_args().round == 1 else "-round2"
PROMPT = ROOT / "evidence" / f"referee{suffix}-prompt.txt"
OUTPUT = SCRATCH / f"codex-referee{suffix}.md"
command = [
    "codex", "exec", "-m", "gpt-6.1-sol", "-c", "model_reasoning_effort=max",
    "--sandbox", "read-only", "--ephemeral", "--skip-git-repo-check",
    "-C", str(ROOT), "-o", str(OUTPUT), PROMPT.read_text(),
]
inputs = [ROOT / "README.md", ROOT / "proof.md", PROMPT]
inputs += sorted((ROOT / "sources").glob("*"))
receipt = {
    "command": command, "stdin": "/dev/null", "cwd": str(ROOT),
    "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "input_sha256": {
        str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in inputs if p.is_file()
    },
}
start = time.monotonic()
with (SCRATCH / f"codex-referee{suffix}-stdout.log").open("w") as out:
    try:
        result = subprocess.run(command, cwd=ROOT, stdin=subprocess.DEVNULL,
                                stdout=out, stderr=subprocess.STDOUT, timeout=2400)
        receipt["exit_code"] = result.returncode
    except subprocess.TimeoutExpired:
        receipt["exit_code"] = None
        receipt["timed_out_seconds"] = 2400
receipt["elapsed_seconds"] = time.monotonic() - start
if OUTPUT.exists():
    receipt["output_sha256"] = hashlib.sha256(OUTPUT.read_bytes()).hexdigest()
    receipt["output_path"] = str(OUTPUT)
(ROOT / "evidence" / f"referee{suffix}-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps({k: v for k, v in receipt.items() if k != "input_sha256"}, indent=2))

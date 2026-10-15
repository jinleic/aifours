#!/usr/bin/env python3
"""Run the explicitly requested read-only Codex referee; registry controls model.
Reproduce: python3 work/run_review.py --phase initial|addendum|extended|completion
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import signal
import time

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--phase", choices=("initial","addendum","extended","completion"), default="initial")
args = parser.parse_args()
prefix = {"initial":"review","addendum":"addendum-review","extended":"extended-review","completion":"completion-review"}[args.phase]

root = Path(__file__).resolve().parent.parent
registry = Path('/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json')
settings = json.loads(registry.read_text())["codex"]
prompt_path = root / f"evidence/{prefix}-prompt.txt"
output_path = root / ("evidence/independent-review.md" if args.phase == "initial" else f"evidence/{prefix}.md")
manifest_path = None if args.phase == "addendum" else root / f"evidence/{prefix}-inputs.json"
command = ["codex","exec","-m",settings["model"],"-c",f'model_reasoning_effort={settings["effort"]}',
           "--sandbox","read-only","--ephemeral","--skip-git-repo-check","-C",str(root),
           "-o",str(output_path),prompt_path.read_text()]
started = time.monotonic()
with (root/f"evidence/{prefix}-stdout.log").open("w") as out, (root/f"evidence/{prefix}-stderr.log").open("w") as err:
    process = subprocess.Popen(command,cwd=root,stdin=subprocess.DEVNULL,stdout=out,stderr=err,start_new_session=True)
    try:
        process.wait(timeout=3500)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid,signal.SIGTERM)
        process.wait(timeout=30)
receipt = {"exit_code":process.returncode,"model_requested":settings["model"],"effort_requested":settings["effort"],
           "sandbox":"read-only","ephemeral":True,"seconds":time.monotonic()-started,
           "prompt_sha256":hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
           "input_manifest_sha256":hashlib.sha256(manifest_path.read_bytes()).hexdigest() if manifest_path else None}
(root/f"evidence/{prefix}-receipt.json").write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt,indent=2))
raise SystemExit(process.returncode)

"""Run the authorized read-only Codex referee with a saved prompt and log."""
import json
import os
from pathlib import Path
import subprocess
import time

root = Path(__file__).resolve().parents[1]
workspace = root.parents[1]
settings = json.loads((workspace / "docs/knowledge-system/DELEGATE_MODELS.json").read_text())
prompt = (root / "evidence/codex-referee.prompt.txt").read_text()
args = [
    "codex", "exec", "-m", settings["codex"]["model"],
    "-c", f'model_reasoning_effort="{settings["codex"]["effort"]}"',
    "--sandbox", "read-only", "--ephemeral", "--skip-git-repo-check",
    "-C", str(root), "-o", str(root / "evidence/codex-referee.md"), prompt,
]
started = time.time()
with (root / "evidence/codex-referee.log").open("w") as log:
    result = subprocess.run(args, stdin=subprocess.DEVNULL, stdout=log,
                            stderr=subprocess.STDOUT, timeout=3500,
                            env={**os.environ, "OMP_NUM_THREADS": "1"})
metadata = {
    "command": "python3 work/run_referee.py",
    "argv_without_prompt": args[:-1],
    "prompt_path": "evidence/codex-referee.prompt.txt",
    "seconds": time.time() - started,
    "returncode": result.returncode,
}
(root / "evidence/codex-referee-run.json").write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata, indent=2))
raise SystemExit(result.returncode)

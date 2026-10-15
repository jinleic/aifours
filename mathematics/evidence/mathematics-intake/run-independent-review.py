"""Run the configured independent Claude reviewer on the embedded public evidence."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
models = json.loads((ROOT / "docs/knowledge-system/DELEGATE_MODELS.json").read_text())
config = models["claude"]
name = sys.argv[1] if len(sys.argv) > 1 else "independent-review"
prompt_path = HERE / f"{name}.prompt.txt"
prompt = prompt_path.read_text()
command = [
    "claude", "--model", config["model"], "--effort", config["effort"],
    "--safe-mode", "--no-chrome", "--tools", "",
    "--permission-mode", "dontAsk", "--no-session-persistence",
    "--output-format", "json", "-p", prompt,
]
started = time.time()
result = subprocess.run(
    command, cwd=HERE, stdin=subprocess.DEVNULL,
    capture_output=True, text=True, timeout=1800,
)
(HERE / f"{name}.stdout.json").write_text(result.stdout)
(HERE / f"{name}.stderr.txt").write_text(result.stderr)
if result.returncode:
    raise SystemExit(f"Reviewer exited {result.returncode}; inspect local stderr")
events = json.loads(result.stdout)
if isinstance(events, dict):
    events = [events]
final = [event for event in events if event.get("type") == "result"][-1]
if final.get("subtype") != "success" or final.get("is_error", False):
    raise SystemExit("Reviewer did not return a successful final result")
text = final["result"].strip()
if text.startswith("```"):
    text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
review = json.loads(text)
receipt = {
    "requested_model": config["model"],
    "requested_effort": config["effort"],
    "reported_init_models": [e.get("model") for e in events if e.get("type") == "system"],
    "reported_model_usage": final.get("modelUsage", {}),
    "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
    "duration_seconds": time.time() - started,
    "returncode": result.returncode,
    "review": review,
}
(HERE / f"{name}.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt, indent=2))

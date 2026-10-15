"""Run the explicitly requested independent referees on one pinned snapshot.

This command invokes configured external model CLIs; it is not part of the
scientific replay. It never installs packages or changes the reviewed files.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "review"
CONFIG = ROOT.parents[1] / "docs/knowledge-system/DELEGATE_MODELS.json"


def hashes():
    paths = [ROOT / name for name in ("README.md", "STATUS.md", "RESULTS.md")]
    for directory in ("source", "code", "results"):
        paths.extend(p for p in (ROOT / directory).iterdir() if p.is_file())
    return {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def run_one(name, argv, prompt_file):
    started = datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()
    stdout_path = REVIEW / (name + "-stdout.json" if name == "claude" else name + "-stdout.txt")
    stderr_path = REVIEW / (name + "-stderr.txt")
    with stdout_path.open("w") as stdout, stderr_path.open("w") as stderr:
        result = subprocess.run(argv, cwd=ROOT, stdin=subprocess.DEVNULL, stdout=stdout, stderr=stderr, timeout=3600)
    receipt = {"started_local": started, "returncode": result.returncode, "command_without_prompt": argv[:-1],
               "prompt_sha256": sha256(prompt_file.read_bytes()).hexdigest(),
               "stdout_sha256": sha256(stdout_path.read_bytes()).hexdigest(), "stderr_sha256": sha256(stderr_path.read_bytes()).hexdigest()}
    if name == "claude" and result.returncode == 0:
        data = json.loads(stdout_path.read_text())
        events = data if isinstance(data, list) else [data]
        terminal = next(event for event in reversed(events) if event.get("type") == "result")
        receipt["subtype"] = terminal.get("subtype")
        receipt["is_error"] = terminal.get("is_error")
        receipt["modelUsage"] = terminal.get("modelUsage")
    return name, receipt


def main():
    config = json.loads(CONFIG.read_text())
    before = hashes()
    (REVIEW / "snapshot-before-review.json").write_text(json.dumps(before, indent=2) + "\n")
    claude_prompt = REVIEW / "claude-prompt.md"
    codex_prompt = REVIEW / "codex-prompt.md"
    claude = ["claude", "--model", config["claude"]["model"], "--effort", config["claude"]["effort"],
              "--safe-mode", "--no-chrome", "--tools", "Read,Glob,Grep", "--permission-mode", "dontAsk",
              "--no-session-persistence", "--output-format", "json", "-p", claude_prompt.read_text()]
    codex = ["codex", "exec", "-m", config["codex"]["model"], "-c", "model_reasoning_effort=" + config["codex"]["effort"],
             "--sandbox", "read-only", "--ephemeral", "--skip-git-repo-check", "-C", str(ROOT),
             "-o", str(REVIEW / "codex-review.md"), codex_prompt.read_text()]
    with ThreadPoolExecutor(max_workers=2) as pool:
        jobs = [pool.submit(run_one, "claude", claude, claude_prompt), pool.submit(run_one, "codex", codex, codex_prompt)]
        results = dict(job.result() for job in jobs)
    results["snapshot_unchanged"] = hashes() == before
    (REVIEW / "review-receipt.json").write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps({name: {k: v for k, v in receipt.items() if k in ("returncode", "subtype", "is_error")} for name, receipt in results.items() if isinstance(receipt, dict)}, indent=2))
    print("snapshot_unchanged:", results["snapshot_unchanged"])


if __name__ == "__main__":
    main()

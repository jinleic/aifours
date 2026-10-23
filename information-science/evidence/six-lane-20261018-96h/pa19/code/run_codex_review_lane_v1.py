#!/usr/bin/env python3
"""One scoped read-only Codex review for the PA19 lane (pattern of RUN/control/run_codex_review_v1.py).

Model/effort come ONLY from the workspace registry DELEGATE_MODELS.json (key 'codex').  The snapshot
directory must be inside LANE/review; outputs are exclusive-created inside it.  Self budget with one
owned SIGTERM to the reviewer's own process group and a bounded 60 s wait; no escalation, no tool
timeout.  The reported model identity is parsed from the CLI stderr header, never assumed.
Usage: run_codex_review_lane_v1.py SNAPSHOT_DIR [BUDGET_SECONDS]
"""
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

LANE = Path("/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261018-96h/pa19")
REGISTRY = Path("/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json")


def clock():
    return subprocess.check_output(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], text=True, stdin=subprocess.DEVNULL).strip()


def wx(path, value):
    with path.open("x") as f:
        json.dump(value, f, indent=2, sort_keys=True)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())


def main():
    snap = Path(sys.argv[1]).resolve()
    budget = int(sys.argv[2]) if len(sys.argv) > 2 else 2400
    if not snap.is_relative_to(LANE / "review") or not 60 <= budget <= 3600:
        raise SystemExit("out-of-scope snapshot or budget")
    prompt, schema = snap / "prompt.txt", snap / "schema.json"
    paths = {k: snap / v for k, v in [("stdout", "stdout.txt"), ("stderr", "stderr.txt"), ("launch", "launch.json"),
                                       ("receipt", "receipt.json"), ("result", "result.json")]}
    if any(p.exists() for p in paths.values()):
        raise SystemExit("refusing overwrite")
    cfg = json.loads(REGISTRY.read_text())["codex"]
    cmd = ["codex", "exec", "-m", cfg["model"], "-c", "model_reasoning_effort=" + cfg["effort"], "--sandbox", "read-only",
           "--ephemeral", "--skip-git-repo-check", "-C", str(snap), "--output-schema", str(schema),
           "-o", str(paths["result"]), prompt.read_text()]
    env = dict(os.environ, TMPDIR=str(LANE / "tmp"), TMP=str(LANE / "tmp"), TEMP=str(LANE / "tmp"),
               PYTHONDONTWRITEBYTECODE="1")
    t = time.monotonic()
    r = {"started_at": clock(), "registry": str(REGISTRY), "requested_model": cfg["model"],
         "requested_effort": cfg["effort"], "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest(),
         "schema_sha256": hashlib.sha256(schema.read_bytes()).hexdigest(),
         "manifest_sha256": hashlib.sha256((snap / "MANIFEST.json").read_bytes()).hexdigest(),
         "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), "sandbox": "read-only",
         "status": "NO_VERDICT", "self_budget_seconds": budget}
    with paths["stdout"].open("x") as out, paths["stderr"].open("x") as err:
        p = subprocess.Popen(cmd, cwd=snap, env=env, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                             start_new_session=True)
        wx(paths["launch"], dict(r, pid=p.pid, pgid=p.pid, cwd=str(snap),
                                 argv_sha256=hashlib.sha256(json.dumps(cmd).encode()).hexdigest()))
        print("LAUNCH", paths["launch"], p.pid, flush=True)
        while p.poll() is None and time.monotonic() - t < budget:
            time.sleep(1)
        if p.poll() is None:
            r.update(status="SELF_BUDGET_SIGTERM_NO_VERDICT", stop_requested_at=clock())
            os.killpg(p.pid, signal.SIGTERM)  # own session leader pid == pgid, child unreaped
            end = time.monotonic() + 60
            while p.poll() is None and time.monotonic() < end:
                time.sleep(0.2)
            if p.poll() is None:
                r["unsettled_pid"] = p.pid
                p.wait()
        r["returncode"] = p.poll()
    r["reported_identity"] = dict(re.findall(r"^(model|provider|sandbox|reasoning effort): (.+)$",
                                             paths["stderr"].read_text(errors="replace"), re.M))
    if r["returncode"] == 0 and "stop_requested_at" not in r and paths["result"].exists():
        raw = paths["result"].read_bytes()
        r["result_sha256"] = hashlib.sha256(raw).hexdigest()
        try:
            res = json.loads(raw)
            r["status"] = "REVIEW_RETURNED_UNVERIFIED"
            r["verdict"] = res.get("verdict")
            r["finding_severities"] = [f.get("severity") for f in res.get("findings", [])]
        except Exception as exc:
            r["status"] = "RESULT_UNPARSEABLE"
            r["parse_error"] = repr(exc)
    r.update(finished_at=clock(), duration_seconds=round(time.monotonic() - t, 1))
    wx(paths["receipt"], r)
    print(json.dumps(r, indent=2), flush=True)
    return 0 if r["status"] == "REVIEW_RETURNED_UNVERIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())

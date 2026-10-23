"""Lane ContinueMOQLS8: run ONE read-only Codex review (registry model/effort, subscription CLI auth) on a frozen
snapshot; preserve prompt/stdout/stderr/note/receipt; exclusive-create every output; self-budget then owned SIGTERM
to the review's own process group with a bounded 60 s settle; never SIGKILL, never a subprocess timeout kill.
Usage: /usr/bin/python3 -I -B run_codex_review_v1.py PROMPT_PATH SNAPSHOT_DIR BUDGET_SECONDS"""
import hashlib
import json
import os
import re
import signal
import subprocess
import sys
import time

LANE = "/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8"
REGISTRY = "/Users/jinleic/jinleic-workspace/docs/knowledge-system/DELEGATE_MODELS.json"
SETTLE = 60


def clock():
    return subprocess.check_output(["/bin/date", "+%Y-%m-%dT%H:%M:%S%z"], text=True).strip()


def sha(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    prompt_path, snap = os.path.realpath(sys.argv[1]), os.path.realpath(sys.argv[2])
    budget = int(sys.argv[3])
    if not (prompt_path.startswith(LANE + "/review/") and snap.startswith(LANE + "/review/")
            and os.path.isfile(prompt_path) and os.path.isdir(snap) and 60 <= budget <= 3600):
        raise SystemExit("prompt and snapshot must be inside the lane review/ directory; budget 60..3600 s")
    base = prompt_path[:-len(".prompt.txt")] if prompt_path.endswith(".prompt.txt") else prompt_path
    out = {k: base + s for k, s in (("note", ".note.md"), ("stdout", ".stdout.txt"), ("stderr", ".stderr.txt"),
                                    ("launch", ".launch.json"), ("receipt", ".receipt.json"))}
    if any(os.path.lexists(p) for p in out.values()):
        raise SystemExit("refusing to overwrite review evidence")
    cfg = json.load(open(REGISTRY))["codex"]
    prompt = open(prompt_path).read()
    cmd = ["/opt/homebrew/bin/codex", "exec", "-m", cfg["model"], "-c", "model_reasoning_effort=" + cfg["effort"],
           "--sandbox", "read-only", "--ephemeral", "--skip-git-repo-check", "-C", os.path.dirname(snap),
           "-o", out["note"], prompt]
    tmp = os.path.join(os.path.dirname(snap), "tmp")
    env = dict(os.environ, TMPDIR=tmp + "/", TMP=tmp, TEMP=tmp, PYTHONDONTWRITEBYTECODE="1")
    rec = {"started_at": clock(), "requested_model": cfg["model"], "requested_effort": cfg["effort"],
           "registry_sha256": sha(REGISTRY), "prompt_sha256": sha(prompt_path), "runner_sha256": sha(__file__),
           "snapshot": snap, "sandbox": "read-only", "ephemeral": True, "stdin": "DEVNULL",
           "self_budget_seconds": budget, "stop_policy": "owned SIGTERM to the review process group, 60 s settle, "
           "never SIGKILL", "status": "NO_VERDICT"}
    t0 = time.monotonic()
    with open(out["stdout"], "x") as so, open(out["stderr"], "x") as se:
        p = subprocess.Popen(cmd, cwd=os.path.dirname(snap), env=env, stdin=subprocess.DEVNULL, stdout=so,
                             stderr=se, start_new_session=True)
        pgid = os.getpgid(p.pid)
        with open(out["launch"], "x") as f:
            json.dump(dict(rec, pid=p.pid, pgid=pgid,
                           argv_sha256=hashlib.sha256(json.dumps(cmd).encode()).hexdigest()), f, indent=1)
            f.write("\n")
        while p.poll() is None and time.monotonic() - t0 < budget:
            time.sleep(1)
        if p.poll() is None:
            rec["stop_requested_at"] = clock()
            rec["status"] = "SELF_BUDGET_SIGTERM_NO_VERDICT"
            os.killpg(pgid, signal.SIGTERM)
            end = time.monotonic() + SETTLE
            while p.poll() is None and time.monotonic() < end:
                time.sleep(0.2)
            if p.poll() is None:
                rec["unsettled_pid"] = p.pid
        rec["returncode"] = p.poll()
    if rec["returncode"] == 0 and "stop_requested_at" not in rec and os.path.isfile(out["note"]):
        if open(out["note"], "rb").read().strip():
            rec["status"] = "NOTE_RETURNED_UNVERIFIED"
            rec["note_sha256"] = sha(out["note"])
    err = open(out["stderr"], errors="replace").read()
    rec["reported_identity"] = dict(re.findall(r"^(model|provider|sandbox|reasoning effort|approval): (.+)$", err, re.M))
    rec["stdout_sha256"], rec["stderr_sha256"] = sha(out["stdout"]), sha(out["stderr"])
    rec["finished_at"] = clock()
    rec["duration_seconds"] = round(time.monotonic() - t0, 1)
    with open(out["receipt"], "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps(rec, indent=1))
    return 0 if rec["status"] == "NOTE_RETURNED_UNVERIFIED" else 1


if __name__ == "__main__":
    raise SystemExit(main())

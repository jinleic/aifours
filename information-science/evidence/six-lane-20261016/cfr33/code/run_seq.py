#!/usr/bin/env python3
"""Run a JSON list of jobs sequentially (lane cfr33). Usage: run_seq.py JOBS.json OUTDIR
JOBS.json: [{"name": str, "cmd": [..]}, ...]. OUTDIR created (must not exist); per job OUTDIR/<name>.out (mode x) and
one JSON line appended to OUTDIR/records.jsonl (host start/end, exit code, sha256 of output and of the executable).
SIGTERM: forwarded to the running job, then the driver stops after it exits. No Python-side timeouts.
"""
import hashlib, json, os, signal, subprocess, sys, time


def host_time():
    return subprocess.run(["date", "+%Y-%m-%d %H:%M:%S %Z"], capture_output=True, text=True).stdout.strip()


jobs = json.load(open(sys.argv[1]))
outdir = sys.argv[2]
os.mkdir(outdir)
state = {"child": None, "stop": False}


def fwd(signum, frame):
    state["stop"] = True
    if state["child"] is not None:
        try:
            state["child"].send_signal(signal.SIGTERM)
        except ProcessLookupError:
            pass


signal.signal(signal.SIGTERM, fwd)
signal.signal(signal.SIGINT, fwd)
for job in jobs:
    if state["stop"]:
        break
    path = os.path.join(outdir, job["name"] + ".out")
    exe = job["cmd"][0]
    exe_sha = hashlib.sha256(open(exe, "rb").read()).hexdigest() if os.path.isfile(exe) else None
    t0, h0 = time.time(), host_time()
    with open(path, "x") as fh:
        state["child"] = subprocess.Popen(job["cmd"], stdout=fh, stderr=subprocess.STDOUT)
        rc = state["child"].wait()
        state["child"] = None
    rec = {"name": job["name"], "cmd": job["cmd"], "exe_sha256": exe_sha, "host_time_start": h0, "host_time_end": host_time(),
           "wall_s": round(time.time() - t0, 3), "exit_code": rc,
           "out_sha256": hashlib.sha256(open(path, "rb").read()).hexdigest()}
    with open(os.path.join(outdir, "records.jsonl"), "a") as fh:
        fh.write(json.dumps(rec) + "\n")
print("done")

#!/usr/bin/env python3
"""Run one SAT solver on one CNF with a native time limit; exclusive JSON record; optional DRAT proof.

Usage: python3 -B code/sat_run.py SOLVER CNF SECONDS OUTPREFIX [--proof] [--seed S] [--extra ARG ...]
  SOLVER in {kissat, cadical}.  Writes OUTPREFIX.stdout, OUTPREFIX.json (mode x) and, with --proof,
  OUTPREFIX.drat.zst (binary DRAT, compressed by a zstd child process reading the solver's proof through a FIFO
  OUTPREFIX.fifo created inside the lane; the FIFO node is left in place, never deleted).
Time limits are native (kissat --time=, cadical -t).  Disk guard: free bytes on the volume must be >= 12e9 before a
proof run starts; while running, if free bytes drop below 12e9 the solver gets SIGTERM, the driver waits (bounded
by polling) and the verdict is UNKNOWN.  No SIGKILL, no Popen.kill(), no subprocess.run(timeout=...).
Verdict: exit 10 -> SAT, 20 -> UNSAT, anything else -> UNKNOWN.
"""
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import time

FLOOR = 12_000_000_000


def host_date():
    return subprocess.run(["date"], capture_output=True, text=True, check=True).stdout.strip()


def free_bytes(path):
    return shutil.disk_usage(path).free


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    solver, cnf, secs, outp = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
    rest = sys.argv[5:]
    proof = "--proof" in rest
    seed = None
    extra = []
    i = 0
    while i < len(rest):
        if rest[i] == "--seed":
            seed = int(rest[i + 1])
            i += 2
        elif rest[i] == "--extra":
            extra.append(rest[i + 1])
            i += 2
        else:
            i += 1
    lane_dir = os.path.dirname(os.path.abspath(outp))
    rec = {"solver": solver, "cnf": cnf, "cnf_sha256": sha256_file(cnf), "time_limit_s": secs, "seed": seed,
           "extra": extra, "proof": proof, "free_bytes_at_start": free_bytes(lane_dir)}
    if proof and rec["free_bytes_at_start"] < FLOOR:
        rec.update({"verdict": "NOT-STARTED", "reason": "disk guard"})
        with open(outp + ".json", "x") as f:
            json.dump(rec, f, indent=1)
        print(json.dumps(rec))
        return
    if solver == "kissat":
        cmd = ["kissat", f"--time={secs}"] + ([f"--seed={seed}"] if seed is not None else []) + extra + [cnf]
    elif solver == "cadical":
        cmd = ["cadical", "-t", str(secs)] + ([f"--seed={seed}"] if seed is not None else []) + extra + [cnf]
    else:
        raise ValueError(solver)
    zproc = None
    if proof:
        fifo = outp + ".fifo"
        os.mkfifo(fifo)
        zout = open(outp + ".drat.zst", "xb")
        zproc = subprocess.Popen(["zstd", "-q", "-c", "-T1", fifo], stdout=zout)
        cmd = cmd + [fifo] if solver == "kissat" else cmd + ["--binary=true", fifo]
        if solver == "kissat":
            cmd.insert(1, "--force")
    rec["cmd"] = cmd
    rec["start"] = host_date()
    t0 = time.time()
    with open(outp + ".stdout", "x") as so:
        p = subprocess.Popen(cmd, stdout=so, stderr=subprocess.STDOUT)
        rec["pid"] = p.pid
        guard_tripped = False
        while p.poll() is None:
            time.sleep(1.0)
            if proof and not guard_tripped and free_bytes(lane_dir) < FLOOR:
                guard_tripped = True
                p.send_signal(signal.SIGTERM)
        rc = p.returncode
    rec["end"] = host_date()
    rec["wall_s"] = round(time.time() - t0, 3)
    rec["exit_code"] = rc
    if proof:
        # if the solver never opened the FIFO, zstd is still blocked in open(); give it EOF by opening the write end
        for _ in range(30):
            if zproc.poll() is not None:
                break
            time.sleep(1.0)
        if zproc.poll() is None:
            try:
                fd = os.open(fifo, os.O_WRONLY | os.O_NONBLOCK)
                os.close(fd)
                rec["fifo_unblocked_by_driver"] = True
            except OSError as exc:
                rec["fifo_unblock_error"] = repr(exc)
        zproc.wait()
        zout.close()
        rec["proof_file"] = outp + ".drat.zst"
        rec["proof_zst_bytes"] = os.path.getsize(outp + ".drat.zst")
        rec["proof_zst_sha256"] = sha256_file(outp + ".drat.zst")
        rec["disk_guard_tripped"] = guard_tripped
    rec["verdict"] = {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN")
    if proof and rec.get("disk_guard_tripped"):
        rec["verdict"] = "UNKNOWN"
    with open(outp + ".json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({k: rec[k] for k in ("solver", "cnf", "verdict", "wall_s", "exit_code")}))


if __name__ == "__main__":
    main()

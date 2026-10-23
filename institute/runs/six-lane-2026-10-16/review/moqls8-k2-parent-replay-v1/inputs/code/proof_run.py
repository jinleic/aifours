"""Certificate runs with zstd-compressed DRAT proofs and a size watchdog (README §1). Never deletes anything.

solve: solver writes its (binary) DRAT proof into an anonymous pipe (/dev/fd/N); zstd compresses it to
       <proof>.drat.zst; a watchdog stops the solver (SIGTERM) if the compressed proof exceeds --cap-bytes; the partial
       file is kept. A receipt JSON (mode 'x') records argv, exit codes, times, sizes, SHA-256 of CNF and proof.
check: zstd -dc <proof> is piped into drat-trim (/dev/fd/N); receipt records the drat-trim verdict line.

python -B proof_run.py solve --solver cadical --cnf X.cnf --proof X.drat.zst --cap-bytes 3221225472 --receipt R.json
python -B proof_run.py check --cnf X.cnf --proof X.drat.zst --drat-trim PATH --receipt R.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import signal
import subprocess
import sys
import threading
import time


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def solve(a):
    # named FIFO inside the lane (CaDiCaL refuses /dev/fd/N); the FIFO node is left in place (never deleted)
    fifo = a.proof + ".fifo"
    os.mkfifo(fifo)
    if a.solver == "cadical":
        cmd = ["cadical", "-q", a.cnf, fifo] + (["-t", str(a.time)] if a.time else [])
    else:
        cmd = ["kissat", "-q", a.cnf, fifo] + (["--time=%d" % a.time] if a.time else [])
    with open(a.proof, "xb") as out, open(a.proof + ".zstd.log", "x") as zlog, \
            open(a.receipt + ".solver.log", "x") as slog:
        t0 = time.time()
        s = subprocess.Popen(cmd, stdout=slog, stderr=subprocess.STDOUT)
        rfd = open(fifo, "rb")                 # blocks until the solver opens the FIFO for writing
        z = subprocess.Popen(["zstd", "-q", "-c", "-3"], stdin=rfd, stdout=out, stderr=zlog)
        rfd.close()
        stopped = {"by_watchdog": False}

        def watch():
            while s.poll() is None:
                if os.path.getsize(a.proof) > a.cap_bytes:
                    stopped["by_watchdog"] = True
                    s.send_signal(signal.SIGTERM)
                    return
                time.sleep(5)
        th = threading.Thread(target=watch, daemon=True)
        th.start()
        s.wait()
        z.wait()
        th.join(timeout=10)
    rec = {"mode": "solve", "argv": sys.argv, "solver_argv": cmd, "solver_exit": s.returncode,
           "status": {10: "SAT", 20: "UNSAT"}.get(s.returncode, "OTHER(%d)" % s.returncode),
           "zstd_exit": z.returncode, "secs": round(time.time() - t0, 1), "stopped_by_watchdog": stopped["by_watchdog"],
           "cap_bytes": a.cap_bytes, "cnf_sha256": sha(a.cnf), "proof": a.proof,
           "proof_bytes_compressed": os.path.getsize(a.proof), "proof_sha256": sha(a.proof)}
    with open(a.receipt, "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


def check(a):
    # drat-trim reads the proof from stdin (single file argument), binary mode forced (-i): it peeks and re-opens a
    # named proof file, which a pipe/FIFO cannot support.
    with open(a.receipt + ".drat-trim.log", "x") as dlog:
        t0 = time.time()
        z = subprocess.Popen(["zstd", "-q", "-dc", a.proof], stdout=subprocess.PIPE)
        cmd = [a.drat_trim, a.cnf, "-i", "-t", str(a.time or 50000)]
        d = subprocess.Popen(cmd, stdin=z.stdout, stdout=dlog, stderr=subprocess.STDOUT)
        z.stdout.close()
        d.wait()
        z.wait()
    txt = open(a.receipt + ".drat-trim.log").read()
    rec = {"mode": "check", "argv": sys.argv, "drat_trim_argv": cmd, "drat_trim_exit": d.returncode,
           "zstd_exit": z.returncode, "secs": round(time.time() - t0, 1),
           "verified": "s VERIFIED" in txt and "NOT VERIFIED" not in txt, "cnf_sha256": sha(a.cnf),
           "proof_sha256": sha(a.proof), "drat_trim_sha256": sha(a.drat_trim)}
    with open(a.receipt, "x") as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))
    if not rec["verified"]:
        raise SystemExit("NOT VERIFIED")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["solve", "check"])
    ap.add_argument("--solver", choices=["cadical", "kissat"])
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--proof", required=True)
    ap.add_argument("--cap-bytes", type=int, default=3 << 30)
    ap.add_argument("--time", type=int, default=0)
    ap.add_argument("--drat-trim")
    ap.add_argument("--receipt", required=True)
    a = ap.parse_args()
    solve(a) if a.mode == "solve" else check(a)


if __name__ == "__main__":
    main()

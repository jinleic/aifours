#!/usr/bin/env python3
"""Method M2 for the E0 split: independent encoder encode_q0b.py + CaDiCaL 3.0.1 writing an
ASCII LRAT proof directly, checked by lrat-check (lane-local build).
Usage: run_m2.py GENG_FILE OUTDIR WORKERS TIMEOUT_S ; resumable.
"""
import concurrent.futures as cf
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
CADICAL = "/opt/homebrew/bin/cadical"
LC = os.path.join(LANE, "tools", "drat-trim", "lrat-check")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def one(outdir, i, g6, timeout):
    tag = "g%03d" % i
    cnf = os.path.join(outdir, "cnf", tag + ".cnf")
    lrat = os.path.join(outdir, "proof", tag + ".lrat")
    enc = subprocess.run([sys.executable, os.path.join(HERE, "encode_q0b.py"), g6, cnf],
                         capture_output=True, text=True)
    t0 = time.time()
    try:
        p = subprocess.run([CADICAL, "-q", "--lrat=true", "--binary=false", cnf, lrat],
                           capture_output=True, text=True, timeout=timeout)
        rc = p.returncode
    except subprocess.TimeoutExpired:
        rc = -1
    res = {"tag": tag, "graph6": g6, "encoder": "encode_q0b.py", "solver": "cadical 3.0.1 --lrat",
           "status": {10: "SAT", 20: "UNSAT"}.get(rc, "UNKNOWN"), "seconds": round(time.time() - t0, 2),
           "cnf_sha256": sha(cnf), "encoder_info": json.loads(enc.stdout)}
    if res["status"] == "UNSAT":
        t1 = time.time()
        q = subprocess.run([LC, cnf, lrat], capture_output=True, text=True)
        res.update({"lrat_sha256": sha(lrat), "lrat_bytes": os.path.getsize(lrat),
                    "lrat_check_seconds": round(time.time() - t1, 2), "lrat_check_rc": q.returncode,
                    "lrat_verified": q.returncode == 0 and "c VERIFIED" in q.stdout.splitlines()})
    json.dump(res, open(os.path.join(outdir, "results", tag + ".json"), "w"), indent=1)
    return res


def main():
    gfile, outdir, workers, timeout = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
    for d in ("cnf", "proof", "results"):
        os.makedirs(os.path.join(outdir, d), exist_ok=True)
    gs = [l.strip() for l in open(gfile) if l.strip()]
    todo = [(i, g) for i, g in enumerate(gs)
            if not os.path.exists(os.path.join(outdir, "results", "g%03d.json" % i))]
    print("to run:", len(todo), flush=True)
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        futs = [ex.submit(one, outdir, i, g, timeout) for i, g in todo]
        for fu in cf.as_completed(futs):
            r = fu.result()
            print(time.strftime("%H:%M:%S"), r["tag"], r["status"], r["seconds"], r.get("lrat_verified"),
                  flush=True)


if __name__ == "__main__":
    main()

"""EXPLORATORY kissat timing signal (parent approval 18:1x; NOT a certificate). One kissat 4.0.4 process, proof-free,
native --time=900, on the K5 leaf given by --leaf (literals read from the validated ledger). The leaf CNF (base header
with C + |lits|, base body, one unit per literal) is streamed through a lane FIFO; its SHA-256 is computed from the same
bytes BEFORE launch and written, with the kissat binary path/SHA-256/version, argv and start time, to
OUTDIR/EXPLORE_RECEIPT.json (exclusive create) before kissat starts. Joint lane guard every ≤ 5 s: busy lane
processes (cadical, drat-trim, kissat, zstd whose command line contains the lane path) ≤ 3 and aggregate RSS of all
processes whose command line contains the lane path ≤ 7.5 GiB; on violation SIGTERM ONLY kissat, wait ≤ 30 s, record
UNKNOWN. Never SIGKILL; never signals any other process. Result: OUTDIR/RESULT.json.
python -B kissat_explore.py --ledger ../evidence/k5_split_v1/ledger/LEDGER.v007.json --leaf c016.L2.040.L3.104 \\
       --base ../evidence/gram_dev_v1/GA5L_K5_sb2.cnf --outdir ../evidence/k5_split_v1/explore_kissat
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import signal
import subprocess
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
RSS_CAP = int(7.5 * 2 ** 30)

MARK = re.compile(r"moqls8-problem16|k4_split_v1|k5_split_v1|k4_leafrun|k5_leafrun|chunk_cap\.py|kissat_explore\.py")


def lane_procs():
    out = subprocess.run(["ps", "-axo", "pid=,rss=,pcpu=,command="], capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split(None, 3)
        if len(parts) == 4 and MARK.search(parts[3]) and not parts[3].startswith("ps "):
            rows.append((int(parts[0]), int(parts[1]) * 1024, float(parts[2]), parts[3]))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--leaf", required=True)
    ap.add_argument("--base", required=True)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    spec = importlib.util.spec_from_file_location("k5_cover", os.path.join(HERE, "k5_cover.py"))
    C = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(C)
    L, lsha = C.load_ledger(a.ledger)
    base = C.Base(a.base)
    v = C.validate(L, base, C.Receipts())
    if v["problems"]:
        raise SystemExit("ledger invalid")
    x = next(y for y in L["leaves"] if y["id"] == a.leaf)
    lits = x["lits"]
    head = ("p cnf %d %d\n" % (base.nv, base.nc + len(lits))).encode()
    tail = "".join("%d 0\n" % l for l in lits).encode()
    h = hashlib.sha256(head)
    h.update(base.body)
    h.update(tail)
    cnf_sha = h.hexdigest()
    if cnf_sha != base.leaf_sha(lits):
        raise SystemExit("leaf hash mismatch")
    os.makedirs(a.outdir, exist_ok=False)
    fifo = os.path.join(a.outdir, "leaf.cnf.fifo")
    os.mkfifo(fifo)
    kis = os.path.realpath(shutil.which("kissat"))
    argv = [kis, "--time=900", fifo]
    rec = {"label": "EXPLORATORY timing signal, proof-free, not a certificate", "leaf": a.leaf, "lits": lits,
           "ledger": a.ledger, "ledger_sha256": lsha, "base_cnf_sha256": base.sha, "leaf_cnf_sha256": cnf_sha,
           "kissat_binary": kis, "kissat_sha256": hashlib.sha256(open(kis, "rb").read()).hexdigest(),
           "kissat_version": subprocess.run([kis, "--version"], capture_output=True, text=True).stdout.strip(),
           "argv": argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "guard": {"busy_max": 3, "rss_cap": RSS_CAP, "period_s": 5}, "start": time.ctime(),
           "start_epoch": time.time()}
    with open(os.path.join(a.outdir, "EXPLORE_RECEIPT.json"), "x") as fh:
        json.dump(rec, fh, indent=1)
    log = open(os.path.join(a.outdir, "kissat.log"), "x")
    t0 = time.time()
    p = subprocess.Popen(argv, stdout=log, stderr=subprocess.STDOUT)
    feed_err = []

    def feed():
        try:
            with open(fifo, "wb") as fh:
                fh.write(head)
                fh.write(base.body)
                fh.write(tail)
        except OSError as e:
            feed_err.append(repr(e))

    th = threading.Thread(target=feed)
    th.start()
    tripped, peak_lane, peak_busy, samples = None, 0, 0, 0
    while p.poll() is None:
        rows = lane_procs()
        busy = sum(1 for r in rows if re.search(r"(^|/)(cadical|drat-trim|kissat|zstd)( |$)", r[3]))
        agg = sum(r[1] for r in rows)
        peak_lane, peak_busy, samples = max(peak_lane, agg), max(peak_busy, busy), samples + 1
        if (busy > 3 or agg > RSS_CAP) and tripped is None:
            tripped = {"time": time.ctime(), "busy": busy, "aggregate_rss": agg}
            p.send_signal(signal.SIGTERM)
            t1 = time.time()
            while p.poll() is None and time.time() - t1 < 30:
                time.sleep(1)
            break
        time.sleep(5)
    rc = p.wait() if p.poll() is not None else None
    th.join(timeout=30)
    log.close()
    txt = open(os.path.join(a.outdir, "kissat.log"), errors="replace").read()
    status = "UNSAT" if re.search(r"^s UNSATISFIABLE", txt, re.M) else \
        ("SAT" if re.search(r"^s SATISFIABLE", txt, re.M) else "UNKNOWN")
    if tripped:
        status = "UNKNOWN (guard trip)"
    res = {"leaf": a.leaf, "status": status, "returncode": rc, "secs": round(time.time() - t0, 1),
           "guard_trip": tripped, "peak_lane_rss": peak_lane, "peak_busy": peak_busy, "samples": samples,
           "feed_errors": feed_err, "end": time.ctime(),
           "label": "EXPLORATORY timing signal, proof-free, not a certificate"}
    with open(os.path.join(a.outdir, "RESULT.json"), "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    main()

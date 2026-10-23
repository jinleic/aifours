#!/usr/bin/env python3
"""Proof pass for cases already classified UNSAT without proof (pass 1).
For each such case: check the stored CNF still has the pass-1 SHA-256, re-run kissat 4.0.4
(--seed=1) writing a binary DRAT proof, then verify it with drat-trim while streaming the
emitted LRAT through a named pipe into lrat-check (LRAT is not stored; it is reproducible
from CNF + DRAT with the same drat-trim build).
Usage: run_proofpass.py CASEDIR WORKERS [TAG_PREFIX ...] ; resumable (proofcheck/<tag>.json).
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
KISSAT = "/opt/homebrew/bin/kissat"
DT = os.path.join(LANE, "tools", "drat-trim", "drat-trim")
LC = os.path.join(LANE, "tools", "drat-trim", "lrat-check")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def one(casedir, tag, wid):
    res = json.load(open(os.path.join(casedir, "results", tag + ".json")))
    cnf = os.path.join(LANE, res["cnf"])
    out = {"tag": tag, "pass1_status": res["status"], "cnf": res["cnf"]}
    out["cnf_sha256"] = sha(cnf)
    out["cnf_matches_pass1"] = out["cnf_sha256"] == res["cnf_sha256"]
    drat = os.path.join(casedir, "proof", tag + ".drat")
    t0 = time.time()
    p = subprocess.run([KISSAT, "-q", "--seed=1", cnf, drat], capture_output=True, text=True)
    out["kissat_rc"] = p.returncode
    out["solve_seconds"] = round(time.time() - t0, 2)
    out["drat_sha256"] = sha(drat)
    out["drat_bytes"] = os.path.getsize(drat)
    fifo = os.path.join(casedir, "fifo", "w%d.lrat" % wid)
    if not os.path.exists(fifo):
        os.mkfifo(fifo)
    t0 = time.time()
    lc = subprocess.Popen([LC, cnf, fifo], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    dt = subprocess.run([DT, cnf, drat, "-L", fifo, "-t", "20000"], capture_output=True, text=True)
    lc_out, _ = lc.communicate()
    out["check_seconds"] = round(time.time() - t0, 2)
    out["drat_trim_verified"] = "s VERIFIED" in dt.stdout
    out["drat_trim_tail"] = dt.stdout.strip().splitlines()[-2:]
    out["lrat_check_rc"] = lc.returncode
    out["lrat_verified"] = lc.returncode == 0 and "c VERIFIED" in lc_out.splitlines()
    out["ok"] = (out["cnf_matches_pass1"] and out["kissat_rc"] == 20 and out["drat_trim_verified"]
                 and out["lrat_verified"])
    json.dump(out, open(os.path.join(casedir, "proofcheck", tag + ".json"), "w"), indent=1)
    return out


def worker(args):
    casedir, tags, wid = args
    res = []
    for t in tags:
        o = one(casedir, t, wid)
        print(time.strftime("%H:%M:%S"), t, "ok" if o["ok"] else "FAIL", o["solve_seconds"], o["check_seconds"],
              flush=True)
        res.append(o["ok"])
    return res


def main():
    casedir, workers = sys.argv[1], int(sys.argv[2])
    prefixes = sys.argv[3:]
    for d in ("proof", "proofcheck", "fifo"):
        os.makedirs(os.path.join(casedir, d), exist_ok=True)
    tags = []
    for fn in sorted(os.listdir(os.path.join(casedir, "results"))):
        tag = fn[:-5]
        if prefixes and not any(tag.startswith(p) for p in prefixes):
            continue
        if os.path.exists(os.path.join(casedir, "proofcheck", tag + ".json")):
            continue
        r = json.load(open(os.path.join(casedir, "results", fn)))
        if r["status"] == "UNSAT":
            tags.append(tag)
    print("to prove:", len(tags), flush=True)
    chunks = [(casedir, tags[i::workers], i) for i in range(workers)]
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        allres = [x for r in ex.map(worker, chunks) for x in r]
    print("done", len(allres), "ok", sum(allres), flush=True)


if __name__ == "__main__":
    main()

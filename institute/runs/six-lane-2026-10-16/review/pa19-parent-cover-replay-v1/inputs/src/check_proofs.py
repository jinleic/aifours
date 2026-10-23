#!/usr/bin/env python3
"""Check kissat DRAT proofs of UNSAT cases: drat-trim (backward check, emits LRAT) then
lrat-check on the emitted LRAT. Both binaries are compiled lane-locally from
marijnheule/drat-trim (tools/drat-trim, commit in COMMIT.txt).
Usage: check_proofs.py CASEDIR WORKERS [TAG_PREFIX ...]; resumable (results/<tag>.check.json).
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
DT = os.path.join(LANE, "tools", "drat-trim", "drat-trim")
LC = os.path.join(LANE, "tools", "drat-trim", "lrat-check")


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check(casedir, tag):
    res = json.load(open(os.path.join(casedir, "results", tag + ".json")))
    cnf = os.path.join(LANE, res["cnf"])
    proof = os.path.join(LANE, res["proof"])
    lrat = os.path.join(casedir, "proof", tag + ".lrat")
    out = {"tag": tag, "cnf_sha256_now": sha(cnf), "cnf_sha256_at_solve": res["cnf_sha256"],
           "proof_sha256": sha(proof), "proof_bytes": os.path.getsize(proof)}
    t0 = time.time()
    p = subprocess.run([DT, cnf, proof, "-L", lrat, "-t", "50000"], capture_output=True, text=True)
    out["drat_trim_seconds"] = round(time.time() - t0, 2)
    out["drat_trim_rc"] = p.returncode
    out["drat_trim_verified"] = "s VERIFIED" in p.stdout
    out["drat_trim_tail"] = p.stdout.strip().splitlines()[-3:]
    if out["drat_trim_verified"] and os.path.exists(lrat):
        t0 = time.time()
        q = subprocess.run([LC, cnf, lrat], capture_output=True, text=True)
        out["lrat_check_seconds"] = round(time.time() - t0, 2)
        out["lrat_check_rc"] = q.returncode
        out["lrat_bytes"] = os.path.getsize(lrat)
        out["lrat_sha256"] = sha(lrat)
        out["lrat_check_tail"] = (q.stdout + q.stderr).strip().splitlines()[-3:]
        out["lrat_verified"] = q.returncode == 0 and "c VERIFIED" in q.stdout.splitlines()
    else:
        out["lrat_verified"] = False
    out["ok"] = (out["cnf_sha256_now"] == out["cnf_sha256_at_solve"] and out["drat_trim_verified"]
                 and out["lrat_verified"])
    json.dump(out, open(os.path.join(casedir, "results", tag + ".check.json"), "w"), indent=1)
    return out


def main():
    casedir, workers = sys.argv[1], int(sys.argv[2])
    prefixes = sys.argv[3:]
    tags = []
    for fn in sorted(os.listdir(os.path.join(casedir, "results"))):
        if not fn.endswith(".json") or fn.endswith(".check.json"):
            continue
        tag = fn[:-5]
        if prefixes and not any(tag.startswith(p) for p in prefixes):
            continue
        r = json.load(open(os.path.join(casedir, "results", fn)))
        if r["status"] != "UNSAT" or os.path.exists(os.path.join(casedir, "results", tag + ".check.json")):
            continue
        tags.append(tag)
    print("to check:", len(tags), flush=True)
    with cf.ProcessPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(check, casedir, t): t for t in tags}
        for fu in cf.as_completed(futs):
            o = fu.result()
            print(time.strftime("%H:%M:%S"), o["tag"], "ok" if o["ok"] else "FAIL", o["drat_trim_seconds"],
                  o.get("lrat_check_seconds"), flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env /usr/bin/python3
"""k2_classesB.py: independent K2 stage-2 screen with encoder B (gram_encB.py, stdlib) and kissat.
Lane moqls7-maximum. Exploration pass (no proofs). Sequential: the CNF is generated into one scratch file
(explore/scratch/encB_current.cnf, reused; scratch, not evidence), then solved; at most one busy process at a time.
Records the CNF SHA-256 for every class so the certification pass can check it regenerates identical CNFs.
Usage: /usr/bin/python3 k2_classesB.py CLASSES.txt OUT.jsonl [--start I] [--stop J] [--time SEC]
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
P = 7


def square_from_key(key):
    L = [[0] * P for _ in range(P)]
    for c in range(P):
        L[0][c] = c
    for r in range(P):
        L[r][0] = r
    t = 0
    for r in range(1, P):
        for c in range(1, P):
            L[r][c] = int(key[t])
            t += 1
    return L


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("classes")
    ap.add_argument("out")
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--stop", type=int, default=10 ** 9)
    ap.add_argument("--time", type=int, default=1800)
    a = ap.parse_args()
    scratch = os.path.join(HERE, "..", "explore", "scratch")
    os.makedirs(scratch, exist_ok=True)
    cnf = os.path.join(scratch, "encB_current.cnf")
    ljs = os.path.join(scratch, "encB_current_L.json")
    rows = [l.split() for l in open(a.classes) if l.strip()]
    with open(a.out, "a") as out:
        for idx, (key, red, par) in enumerate(rows):
            if idx < a.start or idx >= a.stop:
                continue
            with open(ljs, "w") as f:
                json.dump(square_from_key(key), f)
            subprocess.run([sys.executable, "-B", os.path.join(HERE, "gram_encB.py"), "--squares", "2", "--net-L", ljs,
                            "--heavy", "--out", cnf], check=True, capture_output=True)
            with open(cnf, "rb") as f:
                h = hashlib.sha256(f.read()).hexdigest()
            t0 = time.time()
            p = subprocess.run(["kissat", "-q", "--time=%d" % a.time, cnf], capture_output=True, text=True)
            res = {10: "SAT", 20: "UNSAT"}.get(p.returncode, "UNKNOWN(rc=%d)" % p.returncode)
            rec = {"idx": idx, "key": key, "encoder": "B", "cnf_sha256": h, "stage2": res,
                   "sec": round(time.time() - t0, 1)}
            out.write(json.dumps(rec) + "\n")
            out.flush()


if __name__ == "__main__":
    main()

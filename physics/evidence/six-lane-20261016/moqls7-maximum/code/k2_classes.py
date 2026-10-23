#!/usr/bin/env python3
"""k2_classes.py: K2 screening over the main classes of Latin squares of order 7 (exploration pass, no proofs).
Lane moqls7-maximum.

K2 is invariant under paratopy of the 3-net (rows, columns, L) (all three classes are ONB lines of both quantum
squares, and the Gram-support conditions are frame-free), so one representative L per main class suffices.
Per class: stage 1 = one heavy ONB-assignment on the 3-net (gram_enc.build(1, L, heavy=True)); UNSAT there excludes
the class for K2. Stage 2 (only if stage 1 is SAT) = two edge-disjoint heavy assignments (nsq=2, heavy).
Every UNSAT used in a claim must later be re-run with a DRAT proof (certification pass).
Usage: k2_classes.py CLASSES.txt OUT.jsonl --t1 SEC --t2 SEC [--start I] [--stop J]
"""
import argparse
import json
import subprocess
import time

import gram_enc

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


def solve(F, tl):
    t0 = time.time()
    p = subprocess.run(["cadical", "-q", "-t", str(tl)], input=F.text(), capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(p.returncode, "UNKNOWN(rc=%d)" % p.returncode), round(time.time() - t0, 1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("classes")
    ap.add_argument("out")
    ap.add_argument("--t1", type=int, default=600)
    ap.add_argument("--t2", type=int, default=1800)
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--stop", type=int, default=10 ** 9)
    a = ap.parse_args()
    rows = [l.split() for l in open(a.classes) if l.strip()]
    with open(a.out, "a") as out:
        for idx, (key, red, par) in enumerate(rows):
            if idx < a.start or idx >= a.stop:
                continue
            L = square_from_key(key)
            rec = {"idx": idx, "key": key, "reduced": int(red), "par": int(par)}
            F, _ = gram_enc.build(1, L, True, False, None)
            rec["stage1"], rec["stage1_sec"] = solve(F, a.t1)
            if rec["stage1"] == "SAT":
                F, _ = gram_enc.build(2, L, True, False, None)
                rec["stage2"], rec["stage2_sec"] = solve(F, a.t2)
            out.write(json.dumps(rec) + "\n")
            out.flush()
            print(json.dumps(rec), flush=True)

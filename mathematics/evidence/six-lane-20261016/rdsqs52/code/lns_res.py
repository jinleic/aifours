#!/usr/bin/env python3
"""LNS resolution engine: PartialCol start, then exact SAT repairs on small colour subsets.

State: a legal partial colouring of the triples of an STS(v) with k=(v-1)/2 colours.
Repair step: pick an uncoloured triple t; choose a colour set J containing, for each point
of t, one colour missing there, padded with random colours to size s; free every triple
coloured in J and re-colour {freed} ∪ {t} with colours J by SAT (each triple exactly one
colour of J, each (point, colour in J) at most once).  SAT => |U| decreases by one.
Usage: lns_res.py FILE.tri SEED MAX_SECONDS [S] [PCOL_ITERS]
Writes FILE.lns.json with status and (if solved) the classes.
"""
import json
import os
import random
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rdsqs_lib import CNF, kissat


def main():
    path, seed, maxsec = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
    s = int(sys.argv[4]) if len(sys.argv) > 4 else 10
    piters = sys.argv[5] if len(sys.argv) > 5 else "5000000"
    rng = random.Random(seed)
    t0 = time.time()
    p = subprocess.run([os.path.join(HERE, "bin", "partialcol"), path, str(seed), piters], capture_output=True, text=True)
    lines = p.stdout.split("\n")
    head = lines[0].split()
    v, m = map(int, open(path).readline().split())
    k = (v - 1) // 2
    T, col = [], []
    for l in lines[1:1 + m]:
        a, b, c, d = map(int, l.split())
        T.append((a, b, c))
        col.append(d)
    inc = [[] for _ in range(v)]
    for i, t in enumerate(T):
        for x in t:
            inc[x].append(i)
    U = {i for i in range(m) if col[i] < 0}
    log = {"start": head, "start_uncoloured": len(U), "steps": 0, "sat": 0, "unsat": 0}
    work = path + f".lns{seed}.cnf"
    while U and time.time() - t0 < maxsec:
        t = rng.choice(sorted(U))
        J = set()
        for x in T[t]:
            used = {col[i] for i in inc[x] if col[i] >= 0}
            miss = [c for c in range(k) if c not in used]
            J.add(rng.choice(miss))
        while len(J) < s:
            J.add(rng.randrange(k))
        J = sorted(J)
        freed = [i for i in range(m) if col[i] in J] + [t]
        cnf = CNF()
        var = {(i, c): cnf.var() for i in freed for c in J}
        for i in freed:
            cnf.exactly_one([var[(i, c)] for c in J])
        for x in range(v):
            fi = [i for i in inc[x] if i in set(freed)]
            if len(fi) > 1:
                for c in J:
                    cnf.amo([var[(i, c)] for i in fi])
        cnf.write(work)
        st, model, dt = kissat(work, 30, seed=rng.randrange(1 << 30))
        log["steps"] += 1
        if st == "SAT":
            log["sat"] += 1
            for i in freed:
                col[i] = next(c for c in J if var[(i, c)] in model)
            U.discard(t)
        else:
            log["unsat"] += 1
    log["seconds"] = round(time.time() - t0, 2)
    log["final_uncoloured"] = len(U)
    out = {"file": path, "seed": seed, "s": s, **log}
    if not U:
        classes = [[] for _ in range(k)]
        for i, c in enumerate(col):
            classes[c].append(T[i])
        ok = all(sorted(x for tr in C for x in tr) == list(range(v)) for C in classes)
        out["verified_partition"] = ok
        out["classes"] = classes
        out["status"] = "SOLVED" if ok else "BROKEN"
    else:
        out["status"] = "FAILED"
    json.dump(out, open(path + f".lns{seed}.json", "w"))
    print(out["status"], out["start_uncoloured"], "->", out["final_uncoloured"], "steps", out["steps"], "sat", out["sat"], "s", out["seconds"])


if __name__ == "__main__":
    main()

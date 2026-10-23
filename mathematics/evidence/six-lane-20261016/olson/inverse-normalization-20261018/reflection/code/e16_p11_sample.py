# E16 (plan-E16.md + plan-E16-addendum.md): p = 11, B = 0, regime III, random run data, exhaustive residue DFS per datum with
# interval + 2- + 3-pattern pruning (search3 of e15c_census.py); leaves tested with killed_by m = 2, 3, 4.  Finite aid only.
import json, random, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e15_two_avoiders import windows
from e15c_census import search3
from e14e_kills import killed_by

def rand_datum(k, R, emax, rng):
    while True:
        bars = sorted(rng.sample(range(R + k - 1), k - 1))
        parts = []; prev = -1
        for b in bars + [R + k - 1]:
            parts.append(b - prev - 1); prev = b
        if sum(1 for x in parts if x % 2 == 0) <= emax:
            return parts

def main():
    p = 11
    cells = [(4, 19), (5, 19), (6, 19), (7, 19), (6, 22), (7, 21), (7, 23)]
    out = {"plan": "plan-E16.md + plan-E16-addendum.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "p": p, "cells": []}
    for (kap, k) in cells:
        R = 2 * p - k + 2 * kap
        rng = random.Random(1600 + 37 * kap + k)
        W = windows(p, kap, R, k)
        S = {"kappa": kap, "k": k, "R": R, "Delta": k - p - kap - 1, "data_done": 0, "nodes": 0, "leaves": 0,
             "minimal_m_hist": {}, "examples_unkilled_m_le_4": [], "stopped_by_budget": False}
        t0 = time.time(); stats = {"nodes": 0}
        for _ in range(40):
            if time.time() - t0 > 400:
                S["stopped_by_budget"] = True; break
            r = rand_datum(k, R, 2 * kap, rng)
            found = search3(p, kap, r, W, stats)
            S["data_done"] += 1; S["leaves"] += len(found)
            for u in found:
                mm = None
                for m in (2, 3, 4):
                    if killed_by(p, kap, r, u, m) is not None:
                        mm = m; break
                key = str(mm) if mm is not None else ">4"
                S["minimal_m_hist"][key] = S["minimal_m_hist"].get(key, 0) + 1
                if mm is None and len(S["examples_unkilled_m_le_4"]) < 3:
                    S["examples_unkilled_m_le_4"].append({"r": r, "u": u})
        S["nodes"] = stats["nodes"]; S["seconds"] = round(time.time() - t0, 1)
        out["cells"].append(S)
        print(json.dumps({kk: S[kk] for kk in S if kk != "examples_unkilled_m_le_4"}), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(sys.argv[1], "x") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()

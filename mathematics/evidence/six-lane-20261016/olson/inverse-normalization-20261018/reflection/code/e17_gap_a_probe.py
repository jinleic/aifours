# E17 (plan-E17.md): J and c on interval-feasible data in gap-(a) all-ones cells; (2HA) per arrangement.  Finite aid only.
import json, random, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e14_cfunc_regime3 import run_datum, cvals

def has_2HA(r, Dl):
    k = len(r); R = sum(r); H = 2 * Dl - 1
    rr = r + r
    pre = [0]
    for x in rr:
        pre.append(pre[-1] + x)
    def mass(a, L):  # interval of L runs starting at a (cyclic)
        return pre[a + L] - pre[a]
    def admissible(a, L):
        # S = [a, a+L-1], O = [a+L, a-1] of length k-L
        LO = k - L
        if LO < 1 or mass(a, L) < H or mass((a + L) % k, LO) < H:
            return False
        if LO == 1:
            return True
        b1 = (a + L) % k
        for j in range(LO - 1):  # x = b1 + j, not the last run of O
            if mass(b1, j + 2) >= H and mass((b1 + j) % k, LO - j) >= H:
                return True
        return False
    cands = [(a, L) for a in range(k) for L in range(1, k) if mass(a, L) >= H and admissible(a, L)]
    for (a1, L1) in cands:
        for (a2, L2) in cands:
            # disjoint: S2 inside O(S1)
            off = (a2 - a1) % k
            if off >= L1 and off + L2 <= k:
                return True
    return False

def main():
    out = {"plan": "plan-E17.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "cells": []}
    for (p, kap, R, ndata) in [(13, 4, 13, 20), (29, 7, 29, 10)]:
        k = 2 * p - R + 2 * kap; ne = k - R; Dl = k - p - kap - 1
        rng = random.Random(1700 + p); rngv = random.Random(1701 + p)
        S = {"p": p, "kappa": kap, "R": R, "k": k, "Delta": Dl, "data": 0, "leaves": 0, "J_values": {}, "cmin": None, "cmax": None,
             "with_2HA": 0, "without_2HA": 0, "J_values_without_2HA": {}, "stopped_by_budget": False}
        t0 = time.time()
        for _ in range(ndata):
            if time.time() - t0 > 300:
                S["stopped_by_budget"] = True; break
            r = [1] * R + [0] * ne
            rng.shuffle(r)
            h2 = has_2HA(r, Dl)
            S["with_2HA" if h2 else "without_2HA"] += 1
            leaves = run_datum(p, kap, r, 200, rngv)
            S["data"] += 1
            for u in leaves:
                J, cs, w = cvals(p, kap, r, u)
                S["leaves"] += 1
                S["J_values"][str(J)] = S["J_values"].get(str(J), 0) + 1
                if not h2:
                    S["J_values_without_2HA"][str(J)] = S["J_values_without_2HA"].get(str(J), 0) + 1
                mn, mx = min(cs.values()), max(cs.values())
                S["cmin"] = mn if S["cmin"] is None else min(S["cmin"], mn)
                S["cmax"] = mx if S["cmax"] is None else max(S["cmax"], mx)
        S["seconds"] = round(time.time() - t0, 1)
        out["cells"].append(S)
        print(json.dumps(S), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(sys.argv[1], "x") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()

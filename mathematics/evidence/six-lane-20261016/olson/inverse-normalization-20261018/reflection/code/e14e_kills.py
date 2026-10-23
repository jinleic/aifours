# E14e (plan-E14e.md): do patterns with m = 2, 3 intervals kill the interval-feasible leaves of E14c/E14d?  Finite aid only.
import json, random, sys, time, os
from itertools import combinations
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e14_cfunc_regime3 import run_datum, cvals
from e14b_cfunc_general_v2 import make_datum

def gm(m, E, p, kap):
    return min(p - m, E + m - kap - 1, E // 2)

def killed_by(p, kap, r, u, m):
    k = len(r); R = sum(r)
    U = [0] * (k + 1); M = [0] * (k + 1)
    for t in range(k):
        U[t + 1] = (U[t] + u[t]) % p; M[t + 1] = M[t] + r[t]
    win = {}
    def inwin(E, x):
        key = E
        if key not in win:
            lo, hi = -gm(m, R - E, p, kap), gm(m, E, p, kap)
            win[key] = set(y % p for y in range(lo, hi + 1)) if hi >= lo else set()
        return x in win[key]
    for cuts in combinations(range(k), 2 * m):
        E = 0; x = 0
        for i in range(m):
            a, b = cuts[2 * i], cuts[2 * i + 1]
            E += M[b] - M[a]; x += U[b] - U[a]
        if inwin(E, x % p):
            return cuts
    return None

def main():
    out = {"plan": "plan-E14e.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "sets": []}
    specs = [("C1", 13, 6, 13, 1416, 1417, 15, 600), ("C3", 13, 6, 14, 1416, 1417, 15, 600),
             ("C4", 11, 5, 11, 1416, 1417, 15, 600), ("D2", 17, 7, 18, 1418, 1419, 12, 500)]
    for (name, p, kap, R, s1, s2, ndata, cap) in specs:
        rng = random.Random(sum(map(ord, name)) * 1000 + s1); rngv = random.Random(s2)
        bad, good = [], []
        for _ in range(ndata):
            r = make_datum(p, kap, R, rng)
            for u in run_datum(p, kap, r, cap, rngv):
                J, cs, w = cvals(p, kap, r, u)
                if J != 0 and len(bad) < 400:
                    bad.append((r, u, J))
                elif J == 0 and len(good) < 100:
                    good.append((r, u, J))
        S = {"name": name, "p": p, "kappa": kap, "R": R, "tested_Jnonzero": len(bad), "tested_J0": len(good),
             "killed_m2": {"Jnonzero": 0, "J0": 0}, "killed_m3": {"Jnonzero": 0, "J0": 0},
             "unkilled_m_le_3": {"Jnonzero": 0, "J0": 0}, "m3_skipped": 0, "unkilled_examples": []}
        m3_budget = 60
        for label, lst in (("Jnonzero", bad), ("J0", good)):
            for (r, u, J) in lst:
                if killed_by(p, kap, r, u, 2) is not None:
                    S["killed_m2"][label] += 1; continue
                if m3_budget <= 0:
                    S["m3_skipped"] += 1; continue
                m3_budget -= 1
                if killed_by(p, kap, r, u, 3) is not None:
                    S["killed_m3"][label] += 1
                else:
                    S["unkilled_m_le_3"][label] += 1
                    if len(S["unkilled_examples"]) < 3:
                        S["unkilled_examples"].append({"r": r, "u": u, "J": J})
        out["sets"].append(S)
        print(json.dumps({kk: S[kk] for kk in S if kk != "unkilled_examples"}), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(sys.argv[1], "x") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()

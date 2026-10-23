# E14c (plan-E14c.md): IIIa cells with theta+ <= 0.  Reuses e14 / e14b_v2 functions unchanged.  Finite aid, not a premise.
import json, random, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e14_cfunc_regime3 import run_datum, cvals
from e14b_cfunc_general_v2 import make_datum

def main():
    out = {"plan": "plan-E14c.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "sets": []}
    configs = [("C1", 13, 6, 13), ("C2", 17, 8, 17), ("C3", 13, 6, 14), ("C4", 11, 5, 11)]
    for (name, p, kap, R) in configs:
        rng = random.Random(sum(map(ord, name)) * 1000 + 1416)
        rngv = random.Random(1417)
        S = {"name": name, "p": p, "kappa": kap, "R": R, "k": 2 * p - R + 2 * kap, "theta_plus": 2 * R - p - 3 * kap + 3,
             "data": 0, "data_with_leaves": 0, "leaves": 0, "cmin": None, "cmax": None, "J_values": {},
             "leaves_with_c_nonzero": 0, "examples": []}
        for _ in range(15):
            r = make_datum(p, kap, R, rng)
            S["data"] += 1
            leaves = run_datum(p, kap, r, 600, rngv)
            if leaves:
                S["data_with_leaves"] += 1
            for u in leaves:
                J, cs, w = cvals(p, kap, r, u)
                S["leaves"] += 1
                S["J_values"][str(J)] = S["J_values"].get(str(J), 0) + 1
                mn, mx = min(cs.values()), max(cs.values())
                S["cmin"] = mn if S["cmin"] is None else min(S["cmin"], mn)
                S["cmax"] = mx if S["cmax"] is None else max(S["cmax"], mx)
                if mn != 0 or mx != 0:
                    S["leaves_with_c_nonzero"] += 1
                    if len(S["examples"]) < 5:
                        bad = [[s, L, c] for (s, L), c in cs.items() if c != 0][:12]
                        S["examples"].append({"r": r, "u": u, "w": w, "J": J, "nonzero_c": bad})
        out["sets"].append(S)
        print(json.dumps({kk: S[kk] for kk in ("name", "p", "kappa", "R", "k", "theta_plus", "data_with_leaves", "leaves", "cmin", "cmax", "J_values", "leaves_with_c_nonzero")}), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(sys.argv[1], "x") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()

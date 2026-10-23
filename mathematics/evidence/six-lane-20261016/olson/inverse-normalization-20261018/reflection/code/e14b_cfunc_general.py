# E14b (plan-E14b.md): c-function structure in regime III with general masses, and R <= 2 kappa.  Finite aid, not a premise.
import json, random, sys, time, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from e14_cfunc_regime3 import run_datum, cvals

def make_datum(p, kap, R, rng):
    k = 2 * p - R + 2 * kap
    ne = rng.randint(max(0, k - R), 2 * kap)
    npos = k - ne
    # random composition of R into npos positive parts
    cuts = sorted(rng.sample(range(1, R), npos - 1)) if npos > 1 else []
    parts = [b - a for a, b in zip([0] + cuts, cuts + [R])]
    r = parts + [0] * ne
    rng.shuffle(r)
    return r

def main():
    out = {"plan": "plan-E14b.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "sets": []}
    configs = [("A1", 11, 5, 13), ("A2", 13, 5, 16), ("A3", 13, 6, 17), ("A4", 11, 4, 12), ("A5", 7, 3, 8), ("B1", 7, 4, 7)]
    for (name, p, kap, R) in configs:
        rng = random.Random(hash(name) % 100000 + 1414)
        rngv = random.Random(1415)
        S = {"name": name, "p": p, "kappa": kap, "R": R, "k": 2 * p - R + 2 * kap, "data": 0, "data_with_leaves": 0,
             "leaves": 0, "cmin": None, "cmax": None, "J_values": {}, "leaves_with_c_nonzero": 0, "examples": []}
        for _ in range(20):
            r = make_datum(p, kap, R, rng)
            S["data"] += 1
            leaves = run_datum(p, kap, r, 1000, rngv)
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
        print(json.dumps({kk: S[kk] for kk in ("name", "p", "kappa", "R", "k", "data_with_leaves", "leaves", "cmin", "cmax", "J_values", "leaves_with_c_nonzero")}), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(sys.argv[1], "x") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()

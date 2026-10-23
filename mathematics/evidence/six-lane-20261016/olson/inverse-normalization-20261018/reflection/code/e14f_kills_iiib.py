# E14f (plan-E14f.md): minimal killing m for interval-feasible leaves in IIIb.  Finite aid, not a premise.
import json, random, sys, time, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from e14_cfunc_regime3 import run_datum, cvals
from e14b_cfunc_general_v2 import make_datum
from e14e_kills import killed_by

def main():
    out = {"plan": "plan-E14f.md", "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "sets": []}
    specs = [("F1", 7, 4, 7, 10, 300), ("F2", 11, 6, 11, 8, 150), ("F3", 13, 7, 14, 8, 150), ("F4", 11, 6, 12, 8, 150)]
    for (name, p, kap, R, ndata, cap) in specs:
        rng = random.Random(sum(map(ord, name)) * 1000 + 1420); rngv = random.Random(1421)
        S = {"name": name, "p": p, "kappa": kap, "R": R, "k": 2 * p - R + 2 * kap, "leaves": 0, "minimal_m": {},
             "J_values": {}, "m4_budget_used": 0, "examples_unkilled_m_le_3": []}
        m4_budget = 30
        for _ in range(ndata):
            r = make_datum(p, kap, R, rng)
            for u in run_datum(p, kap, r, cap, rngv):
                S["leaves"] += 1
                J, cs, w = cvals(p, kap, r, u)
                S["J_values"][str(J)] = S["J_values"].get(str(J), 0) + 1
                found = None
                for m in (2, 3):
                    if killed_by(p, kap, r, u, m) is not None:
                        found = m; break
                if found is None:
                    if len(S["examples_unkilled_m_le_3"]) < 3:
                        S["examples_unkilled_m_le_3"].append({"r": r, "u": u, "J": J})
                    if m4_budget > 0:
                        m4_budget -= 1; S["m4_budget_used"] += 1
                        found = 4 if killed_by(p, kap, r, u, 4) is not None else "none_le_4"
                    else:
                        found = "untested_m4"
                S["minimal_m"][str(found)] = S["minimal_m"].get(str(found), 0) + 1
        out["sets"].append(S)
        print(json.dumps({kk: S[kk] for kk in S if kk != "examples_unkilled_m_le_3"}), flush=True)
    out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(sys.argv[1], "x") as f:
        json.dump(out, f, indent=1)

if __name__ == "__main__":
    main()

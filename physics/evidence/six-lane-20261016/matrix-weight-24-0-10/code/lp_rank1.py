"""LP over the 8-parameter genus-2 family with nonnegativity of all pair counts AND the 84 exact
rank-1-block PSD conditions (each block = c(s) * v v^T, PSD <=> c(s) >= 0). Floating point exploration
(HiGHS) in rescaled variables s = s_ref + w*u; feasibility/infeasibility is then re-derived exactly.
"""
import json
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog

from g2_polytope import load_space


def rows_and_funcs():
    keys, piv, free, c, V = load_space()
    st = json.load(open("../evidence/block_structure.json"))
    funcs = []
    for r in st["rank1"]:
        k0 = Fraction(r["const"])
        kv = [Fraction(q) for q in r["coef"]]
        funcs.append((tuple(r["block"]), k0, kv))
    return keys, piv, free, c, V, funcs


if __name__ == "__main__":
    keys, piv, free, c, V, funcs = rows_and_funcs()
    nf = len(free)
    cf = np.array([float(x) for x in c])
    Vf = np.array([[float(x) for x in row] for row in V])
    rng = json.load(open("../evidence/g2_polytope_ranges.json"))
    lo = np.array([(rng[str(keys[f])][1] or 0.0) for f in free])
    hi = np.array([rng[str(keys[f])][3] for f in free])
    w = np.maximum(hi - lo, 1.0)
    sref = lo
    # constraint rows in u: a_i . u + b_i >= 0 ; normalize each row to unit max-coefficient
    Arows, brows, tags = [], [], []
    for i in range(len(cf)):
        a = Vf[i] * w
        bb = cf[i] + Vf[i] @ sref
        nrm = max(np.abs(a).max(), abs(bb), 1e-300)
        if np.abs(a).max() == 0:
            if bb < 0:
                print("constant negative pair count row", i, bb)
            continue
        Arows.append(a / nrm); brows.append(bb / nrm); tags.append(("count", i))
    for blkid, k0, kv in funcs:
        a = np.array([float(q) for q in kv]) * w
        bb = float(k0) + np.array([float(q) for q in kv]) @ sref
        nrm = max(np.abs(a).max(), abs(bb), 1e-300)
        if np.abs(a).max() == 0:
            if bb < 0:
                print("constant negative block functional", blkid, bb)
            continue
        Arows.append(a / nrm); brows.append(bb / nrm); tags.append(("block", blkid))
    for f in range(nf):  # s_f >= 0  ->  u_f >= -sref_f / w_f
        e = np.zeros(nf); e[f] = 1.0
        Arows.append(e); brows.append(sref[f] / w[f]); tags.append(("s", f))
    A = np.array(Arows); b = np.array(brows)
    # maximize t s.t. A u + b >= t  <=>  -A u + t <= b
    res = linprog(np.r_[np.zeros(nf), -1.0], A_ub=np.hstack([-A, np.ones((len(b), 1))]), b_ub=b,
                  bounds=[(None, None)] * nf + [(None, 1.0)], method="highs")
    print("joint LP:", res.status, res.message, "margin t* =", None if res.status else -res.fun)
    if res.status == 0:
        u = res.x[:nf]
        s = sref + w * u
        slack = A @ u + b
        order = np.argsort(slack)[:12]
        print("tightest rows:", [(tags[k], float(slack[k])) for k in order])
        json.dump({"s": s.tolist(), "margin": float(-res.fun), "w": w.tolist(), "sref": sref.tolist(),
                   "active": [[str(tags[k]), float(slack[k])] for k in order]},
                  open("../evidence/lp_rank1_center.json", "w"))

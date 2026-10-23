"""Nonnegativity polytope of the exact 8-parameter genus-2 solution family (float LP exploration).
x = c + V s, s = counts of the 8 free orbit types; require x >= 0, s >= 0. Reports per-parameter ranges.
"""
import json
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog


def load_space(path="../evidence/g2_solution_space.json"):
    d = json.load(open(path))
    keys = d["keys"]
    piv = d["pivots"]
    free = d["free"]
    nv = len(keys)
    c = [Fraction(0)] * nv
    V = [[Fraction(0)] * len(free) for _ in range(nv)]
    for i, (num, den) in d["particular"].items():
        c[int(i)] = Fraction(num, den)
    for fi, f in enumerate(free):
        V[f][fi] = Fraction(1)
        for i, (num, den) in d["null"][str(f)].items():
            V[int(i)][fi] = Fraction(num, den)
    return keys, piv, free, c, V


if __name__ == "__main__":
    keys, piv, free, c, V = load_space()
    nv, nf = len(keys), len(free)
    cf = np.array([float(x) for x in c])
    Vf = np.array([[float(x) for x in row] for row in V])
    # x = cf + Vf s >= 0  ->  -Vf s <= cf
    A_ub = -Vf
    b_ub = cf
    out = {}
    for fi in range(nf):
        e = np.zeros(nf); e[fi] = 1
        lo = linprog(e, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)] * nf, method="highs")
        hi = linprog(-e, A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)] * nf, method="highs")
        out[str(keys[free[fi]])] = (lo.status, lo.fun if lo.status == 0 else None,
                                    hi.status, -hi.fun if hi.status == 0 else None)
        print(keys[free[fi]], out[str(keys[free[fi]])])
    feas = linprog(np.zeros(nf), A_ub=A_ub, b_ub=b_ub, bounds=[(0, None)] * nf, method="highs")
    print("nonneg polytope feasible:", feas.status == 0, feas.message)
    json.dump(out, open("../evidence/g2_polytope_ranges.json", "w"), indent=1)

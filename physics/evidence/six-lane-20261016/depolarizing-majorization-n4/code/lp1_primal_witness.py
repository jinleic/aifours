"""Obstruction for the level-1 twirled PPT relaxation: exact rational PRIMAL points c (feasible for every LP
constraint of twirl_lp_exact.py) with objective K_k(T_s) + gap, for U_2 at k = 6..10 and U_3 at k = 2..4.
Feasibility and objective are re-checked with Fractions independently of sympy's solver.
"""
import itertools
import json
from fractions import Fraction as Fr
from math import comb

import sympy as sp

import twirl_lp_exact as T

out = {}
for s, ks in ((2, range(6, 11)), (3, range(2, 5))):
    obj = [comb(len(S), s) * 2 ** s * 3 ** (4 - len(S)) for S in T.subsets]
    eig = sorted([comb(z, s) for z in range(5) for _ in range(comb(4, z))], reverse=True)
    for k in ks:
        val, sol = T.lp_value(obj, k)
        c = [Fr(str(sol[sym])) for sym in sp.symbols("c0:16")]
        g = lambda inS, t: (Fr(1, 2) if t == 0 else Fr(-1, 2)) if inS else (Fr(1, 2) if t == 0 else Fr(3, 2))
        checks = {
            "bounds": all(Fr(0) <= x <= Fr(1, 16) for x in c),
            "trace": sum(c[i] * 3 ** (4 - len(S)) for i, S in enumerate(T.subsets)) == k,
            "tr_sigma": sum(c[i] * Fr(1, 2) ** len(S) * Fr(3, 2) ** (4 - len(S)) for i, S in enumerate(T.subsets)) <= 1,
            "ppt": all(Fr(0) <= sum(c[i] * sp.prod([g(l in S, tau[l]) for l in range(4)]) for i, S in
                                    enumerate(T.subsets)) <= Fr(1, 16)
                       for tau in itertools.product((0, 1), repeat=4)),
        }
        objective = sum(obj[i] * c[i] for i in range(16))
        target = sum(eig[:k])
        out[f"U{s}_k{k}"] = {"c": [str(x) for x in c], "checks": checks, "objective": str(objective),
                             "target": target, "excess": str(objective - target)}
        print(f"U{s} k={k}: feasible={all(checks.values())} objective={objective} target={target} "
              f"excess={objective - target}")
json.dump(out, open("../evidence/lp1_primal_witnesses.json", "w"), indent=1)

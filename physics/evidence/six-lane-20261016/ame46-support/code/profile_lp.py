#!/usr/bin/env python3
"""profile_lp.py: profile-level necessary conditions on the classical part T (officers). Lane ame46-support.
Exploration tool. A profile counts as excluded only with an exactly verified certificate.

Setting (LOWER42 r2 §0, LOWER46 Lemma 12): for a profile, V_i is the set of values of coordinate i with positive
deficit, and d_{i,a} is the deficit of a in V_i (normal form: V_i = {6-|p_i|, ..., 5}, d_{i,a} = p_i[k]). Known facts:
 - a hole line contains no officer; every other line contains exactly one officer;
 - every hole line of the pair (i, j) lies in V_i x V_j, and the line (x_i, x_j) = (a, b) with a in V_i is a hole
   line for exactly d_{i,a} values b.
Type of an officer x: tau = (tau_1, ..., tau_4) with tau_i = x_i if x_i is in V_i, else '*'. Let n_tau be the number
of officers of type tau. Valid constraints, all of the form A n = b or A n <= b, with n >= 0:
 (E1) sum over tau of n_tau = t;
 (E2) for i != j and a in V_i: #{officers with x_i = a, x_j not in V_j} = 6 - |V_j|, and
      #{officers with x_i = a, x_j in V_j} = |V_j| - d_{i,a};
 (E3) for i != j and b in V_j: #{officers with x_i not in V_i, x_j = b} = 6 - |V_i|;
 (E4) for i != j: #{officers with x_i not in V_i, x_j not in V_j} = (6 - |V_i|)(6 - |V_j|);
 (U1) for i < j, a in V_i, b in V_j: #{officers with x_i = a, x_j = b} <= 1.
Infeasibility certificate (Farkas, for {A_eq n = b_eq, A_ub n <= b_ub, n >= 0}): vectors y (free) and z >= 0 with
A_eq^T y + A_ub^T z >= 0 componentwise and b_eq.y + b_ub.z < 0. Verified exactly in rationals.
"""
import itertools
import json
import sys
from fractions import Fraction as Fr

import numpy as np
from scipy.optimize import linprog


def build(prof, t):
    h = sum(prof[0])
    V = [list(range(6 - len(p), 6)) for p in prof]
    d = [{a: p[k] for k, a in enumerate(V[i])} for i, p in enumerate(prof)]
    types = list(itertools.product(*[V[i] + ["*"] for i in range(4)]))
    col = {tau: k for k, tau in enumerate(types)}
    Aeq, beq, Aub, bub, names_eq, names_ub = [], [], [], [], [], []

    def row(pred):
        return [1 if pred(tau) else 0 for tau in types]
    Aeq.append([1] * len(types)); beq.append(t); names_eq.append("E1")
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            for a in V[i]:
                Aeq.append(row(lambda tau: tau[i] == a and tau[j] == "*")); beq.append(6 - len(V[j]))
                names_eq.append("E2out i%d a%d j%d" % (i, a, j))
                Aeq.append(row(lambda tau: tau[i] == a and tau[j] != "*")); beq.append(len(V[j]) - d[i][a])
                names_eq.append("E2in i%d a%d j%d" % (i, a, j))
            for b in V[j]:
                Aeq.append(row(lambda tau: tau[i] == "*" and tau[j] == b)); beq.append(6 - len(V[i]))
                names_eq.append("E3 i%d j%d b%d" % (i, j, b))
            if i < j:
                Aeq.append(row(lambda tau: tau[i] == "*" and tau[j] == "*"))
                beq.append((6 - len(V[i])) * (6 - len(V[j])))
                names_eq.append("E4 i%d j%d" % (i, j))
                for a in V[i]:
                    for b in V[j]:
                        Aub.append(row(lambda tau: tau[i] == a and tau[j] == b)); bub.append(1)
                        names_ub.append("U1 i%d a%d j%d b%d" % (i, a, j, b))
    return types, Aeq, beq, Aub, bub, names_eq, names_ub


def farkas(Aeq, beq, Aub, bub):
    """LP: minimise b_eq.y + b_ub.z subject to A_eq^T y + A_ub^T z >= 0, -1 <= y <= 1, 0 <= z <= 1."""
    me, mu = len(Aeq), len(Aub)
    n = len(Aeq[0])
    c = np.array(list(beq) + list(bub), dtype=float)
    M = np.zeros((n, me + mu))
    if me:
        M[:, :me] = np.array(Aeq, dtype=float).T
    if mu:
        M[:, me:] = np.array(Aub, dtype=float).T
    res = linprog(c, A_ub=-M, b_ub=np.zeros(n), bounds=[(-1, 1)] * me + [(0, 1)] * mu, method="highs")
    if res.status != 0 or res.fun > -1e-9:
        return None
    best = None
    for den in (1, 2, 3, 4, 6, 8, 12, 16, 24, 48, 96, 1000, 10 ** 6):
        y = [Fr(round(v * den), den) for v in res.x[:me]]
        z = [max(Fr(0), Fr(round(v * den), den)) for v in res.x[me:]]
        if verify(Aeq, beq, Aub, bub, y, z):
            best = (y, z)
            break
    return best


def verify(Aeq, beq, Aub, bub, y, z):
    if any(v < 0 for v in z):
        return False
    n = len(Aeq[0])
    for k in range(n):
        s = sum(Aeq[r][k] * y[r] for r in range(len(Aeq)) if Aeq[r][k]) + \
            sum(Aub[r][k] * z[r] for r in range(len(Aub)) if Aub[r][k])
        if s < 0:
            return False
    val = sum(beq[r] * y[r] for r in range(len(beq))) + sum(bub[r] * z[r] for r in range(len(bub)))
    return val < 0


def check_profile(prof, t):
    types, Aeq, beq, Aub, bub, ne, nu = build(prof, t)
    f = farkas(Aeq, beq, Aub, bub)
    if f is None:
        return {"profile": [list(p) for p in prof], "t": t, "excluded": False}
    y, z = f
    cert = {"y": {ne[r]: str(y[r]) for r in range(len(y)) if y[r] != 0},
            "z": {nu[r]: str(z[r]) for r in range(len(z)) if z[r] != 0}}
    return {"profile": [list(p) for p in prof], "t": t, "excluded": True, "certificate": cert,
            "verified": verify(Aeq, beq, Aub, bub, y, z)}


if __name__ == "__main__":
    import large_t_e0 as lte
    out = []
    for t in [int(x) for x in sys.argv[1].split(",")]:
        h = 36 - t
        profs = lte.profiles(h)
        ex = 0
        for p in profs:
            r = check_profile(p, t)
            ex += r["excluded"] and r.get("verified", False)
            out.append(r)
        print("t=%d h=%d profiles=%d LP-excluded(verified)=%d" % (t, h, len(profs), ex), flush=True)
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w") as fh:
            json.dump(out, fh, indent=1)

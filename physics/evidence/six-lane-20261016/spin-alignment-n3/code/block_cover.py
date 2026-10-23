"""Block-decomposition coverage for Song-Chen Conjecture 2, n=3, d=2, Q=I/2 (unnormalized weights w_I = mu_I 2^{-|I^c|};
identity term dropped).

Provable blocks (each majorized by its own aligned-diagonal target), all with arbitrary nonnegative weights:
  B_n  (n in {A,B,C}, {l,m} the other two): alpha_l rho_l + alpha_m rho_m + alpha_lm rho_lm + beta_n rho_n
       = (block on {l,m}) + (singleton on n). The {l,m} part is majorized by the n=2 strong spin alignment theorem
       (Alhejji, Ann. Henri Poincare 27 (2026) 909-932, as cited by Song-Chen); the two parts commute (disjoint
       qubits), so the spectrum is a Kronecker sum and majorization is preserved.
  P    : a rho_AB + b rho_AC + c rho_BC   (Song-Chen Prop. 3)
  F    : f rho  (full set)
If, for some linear order pi of {0,1}^3 that refines the Boolean (support-inclusion) order, the weights w can be split
into such blocks with every block target nonincreasing along pi, Ky Fan subadditivity proves X <= Y for this w.
This script decides that LP for each of the 48 linear extensions and reports coverage on sampled w.
"""
import itertools
import json
import sys

import numpy as np
from scipy.optimize import linprog

STATES = ["".join(b) for b in itertools.product("01", repeat=3)]
SUBS = [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]


def zero(x, I):
    return all(x[l] == "0" for l in I)


def linear_extensions():
    supp = {x: {l for l in range(3) if x[l] == "1"} for x in STATES}
    out = []
    for perm in itertools.permutations(STATES):
        pos = {x: i for i, x in enumerate(perm)}
        if all(pos[x] < pos[y] for x in STATES for y in STATES if supp[x] < supp[y]):
            out.append(perm)
    return out


def block_vars():
    """List of (block_id, subset) variables."""
    v = []
    for n in range(3):
        l, m = [q for q in range(3) if q != n]
        for I in [(l,), (m,), (l, m), (n,)]:
            v.append((f"B{n}", I))
    for I in [(0, 1), (0, 2), (1, 2)]:
        v.append(("P", I))
    v.append(("F", (0, 1, 2)))
    return v


VARS = block_vars()


def lp_feasible(w, order):
    nv = len(VARS)
    A_eq, b_eq = [], []
    for I in SUBS:
        row = np.zeros(nv)
        for j, (b, J) in enumerate(VARS):
            if J == I:
                row[j] = 1
        A_eq.append(row); b_eq.append(w[I])
    A_ub, b_ub = [], []
    for blk in sorted({b for b, _ in VARS}):
        for i in range(7):
            x, y = order[i], order[i + 1]
            row = np.zeros(nv)     # target(y) - target(x) <= 0
            for j, (b, J) in enumerate(VARS):
                if b == blk:
                    row[j] = float(zero(y, J)) - float(zero(x, J))
            if np.any(row):
                A_ub.append(row); b_ub.append(0.0)
    r = linprog(np.zeros(nv), A_ub=np.array(A_ub), b_ub=np.array(b_ub), A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                bounds=[(0, None)] * nv, method="highs")
    return r.status == 0, (r.x if r.status == 0 else None)


if __name__ == "__main__":
    n, seed = int(sys.argv[1]), int(sys.argv[2])
    exts = linear_extensions()
    rng = np.random.default_rng(seed)
    uncovered = []
    covered = 0
    for s in range(n):
        alpha = [1.0, 0.3, 0.1][s % 3]
        vals = rng.dirichlet(np.ones(7) * alpha)
        w = dict(zip(SUBS, vals))
        ok = False
        for order in exts:
            f, _ = lp_feasible(w, order)
            if f:
                ok = True
                break
        if ok:
            covered += 1
        else:
            uncovered.append([float(v) for v in vals])
    print(json.dumps({"linear_extensions": len(exts), "samples": n, "covered": covered,
                      "uncovered_count": len(uncovered), "uncovered_examples": uncovered[:5]}))

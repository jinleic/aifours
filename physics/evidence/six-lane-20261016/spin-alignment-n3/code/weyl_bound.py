"""Compatibility-aware Weyl bound (generalizing Song-Chen's proof of X3 <= T3) for Q = I/2, n = 3:
weights v_l (singletons), c (EQUAL pair weights), f (full). By Song-Chen eq. (31),
   sum_pairs rho_pair (x) 1 = sum_l rho_l (x) 1 - 1 + rho + rho~,   rho~ = s_y^{(x)3} rho^T s_y^{(x)3} >= 0,
so X = D + P with D = sum_l (v_l + c) rho_l (x) 1 - c 1 (a Kronecker sum, spectrum explicit in the local spectra
r_l) and P = (f + c) rho + c rho~ >= 0. Weyl: lambda_i(X) >= lambda_i(D), and lambda_8(X) >= 0, hence
   K_r(X) <= Tr X - sum_{i=r+1}^{7} h_i - max(h_8, 0)   (h = sorted spectrum of D).
Pure global states satisfy the polygon inequalities r_A <= r_B + r_C etc. (0 <= r_l <= 1/2).
This script tests whether the bound is <= K_r(Y) for all r over a fine grid of admissible (r_A, r_B, r_C), for
random (v, c, f) including dominant-singleton weights. Floating point exploration; a pass would be turned into an
exact piecewise-linear verification.
"""
import itertools
import json
import sys

import numpy as np


def target_spectrum(v, c, f):
    vals = []
    for x in itertools.product((0, 1), repeat=3):
        z = [l for l in range(3) if x[l] == 0]
        s = sum(v[l] for l in z) + c * sum(1 for p in itertools.combinations(range(3), 2) if set(p) <= set(z))
        s += f * (len(z) == 3)
        vals.append(s)
    return np.sort(vals)[::-1]


def bound_gap(v, c, f, grid=41):
    TrX = 4 * sum(v) + 6 * c + f
    Ky = np.cumsum(target_spectrum(v, c, f))
    worst = -np.inf
    rs = np.linspace(0, 0.5, grid)
    for rA, rB, rC in itertools.product(rs, rs, rs):
        if rA > rB + rC + 1e-12 or rB > rA + rC + 1e-12 or rC > rA + rB + 1e-12:
            continue
        r = (rA, rB, rC)
        h = np.sort([sum((v[l] + c) * (r[l] if x[l] else 1 - r[l]) for l in range(3)) - c
                     for x in itertools.product((0, 1), repeat=3)])[::-1]
        for k in range(1, 8):
            ub = TrX - h[k:7].sum() - max(h[7], 0.0)
            worst = max(worst, ub - Ky[k - 1])
    return worst


if __name__ == "__main__":
    n, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    out = []
    for s in range(n):
        v = rng.dirichlet(np.ones(3) * (0.4 if s % 2 else 1.0)) * rng.uniform(0.1, 2)
        if s % 3 == 0:
            v = np.array([rng.uniform(1, 2), rng.uniform(0, 0.3), rng.uniform(0, 0.3)])   # dominant singleton
        c = rng.uniform(0, 1.0)
        f = rng.uniform(0, 1.0)
        g = bound_gap(v, c, f)
        out.append({"v": v.tolist(), "c": c, "f": f, "bound_minus_target": g})
    worst = max(out, key=lambda o: o["bound_minus_target"])
    passes = sum(1 for o in out if o["bound_minus_target"] <= 1e-12)
    print(json.dumps({"samples": n, "bound_proves_it": passes, "worst": worst}))
    json.dump(out, open(f"../evidence/weyl_bound_seed{seed}.json", "w"))

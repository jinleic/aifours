"""EXPLORATORY (floats, evidence only): robustness of the row-separable relaxation R_g at d = 8.

U1. Full Cauchy-Schwarz F_g (rows and columns relaxed) with the tuned g, on B_4.
U2. R_g (columns relaxed) on row-stochastic matrices: 96 multistarts, tuned g from explore_d8_tune.json.
U3. Re-tune (beta, gamma) to maximise the row-stochastic margin of R_g (Nelder-Mead, bounded), then recheck with
    96 starts, and scan the 'three uniform rows + one free row' family on a fine simplex grid (denominator 60).
Writes ../evidence/explore_d8_rowrelax.json.  Single-threaded, finite loops.
"""
import itertools
import json
import math
import os
import time

import numpy as np
from scipy.optimize import minimize

import explore_exact_exponent as E
from explore_d8_dualfamilies import B_g, PSIJ, cons_ds, cons_rows, C, D, K
from explore_d8_tune import R_g, min_ratio

J = E.J


def starts_rows(rng, n):
    pts = []
    for s in range(n):
        kind = s % 4
        if kind == 0:
            M = np.exp(rng.normal(scale=rng.choice([1, 2, 4]), size=(K, K)))
        elif kind == 1:
            M = np.full((K, K), 0.25)
            i = rng.integers(K)
            M[i] = rng.dirichlet(np.ones(K) * rng.choice([0.2, 1.0]))
        elif kind == 2:
            M = np.full((K, K), 0.25)
            for i in rng.choice(K, size=2, replace=False):
                M[i] = rng.dirichlet(np.ones(K) * rng.choice([0.2, 1.0]))
        else:
            M = np.array([rng.dirichlet(np.ones(K) * rng.choice([0.1, 0.5, 2.0])) for _ in range(K)])
        pts.append(M / M.sum(axis=1, keepdims=True))
    return pts


def main():
    t0 = time.time()
    rng = np.random.default_rng(80808)
    tuned = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "explore_d8_tune.json")))
    bp = tuple(tuned["T2 Nelder-Mead best (beta, gamma)"])
    out = {"note": "EXPLORATORY numerics (floats); evidence only; no claim.", "tuned g (beta, gamma)": bp}
    ds_pts = []
    for s in range(24):
        if s % 2 == 0:
            ds_pts.append(E.sinkhorn(np.exp(rng.normal(scale=rng.choice([1, 2, 4]), size=(K, K)))))
        else:
            ds_pts.append(E.family(np.eye(K)[rng.permutation(K)], rng.uniform(0.2, 0.95)))

    def F_cs(M, par):
        return B_g(M, (par[0], par[1], 0.0), cs=True)
    out["U1 full Cauchy-Schwarz F_g: min normalised margin on B_4"] = min_ratio(lambda M: F_cs(M, bp), ds_pts)
    rpts = starts_rows(rng, 96)
    out["U2 R_g on row-stochastic, 96 starts"] = min_ratio(lambda M: R_g(M, bp), rpts, rows_only=True)
    # U3: retune for the row-stochastic margin
    sub = rpts[:24]
    hist = []

    def neg(par):
        r = min_ratio(lambda M: R_g(M, (par[0], par[1])), sub, rows_only=True)[0]
        hist.append((float(par[0]), float(par[1]), float(r)))
        return -r
    res = minimize(neg, np.array(bp), method="Nelder-Mead", options={"maxfev": 40, "xatol": 1e-3, "fatol": 1e-6})
    bp2 = (float(res.x[0]), float(res.x[1]))
    out["U3 retuned (beta, gamma) for row-stochastic margin"] = bp2
    out["U3 retuned: R_g on row-stochastic, 96 starts"] = min_ratio(lambda M: R_g(M, bp2), rpts, rows_only=True)
    out["U3 retuned: R_g on B_4"] = min_ratio(lambda M: R_g(M, bp2), ds_pts)
    # grid scan: three uniform rows + one free row r (denominator 60, all simplex points)
    for name, par in (("tuned", bp), ("retuned", bp2)):
        worst = (1e9, None)
        N = 60
        for a in range(N + 1):
            for b in range(N + 1 - a):
                for c in range(N + 1 - a - b):
                    r = np.array([a, b, c, N - a - b - c], dtype=float) / N
                    M = np.full((K, K), 0.25)
                    M[3] = r
                    n2 = float(np.sum((M - J) ** 2))
                    if n2 < 1e-12:
                        continue
                    val = (PSIJ - R_g(M, par)) / n2
                    if val < worst[0]:
                        worst = (val, r.tolist())
        out[f"U3 grid (3 uniform rows + 1 free row, denominator 60), {name}: min normalised margin"] = worst
    out["U3 history tail"] = hist[-6:]
    out["seconds"] = round(time.time() - t0, 1)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "explore_d8_rowrelax.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()

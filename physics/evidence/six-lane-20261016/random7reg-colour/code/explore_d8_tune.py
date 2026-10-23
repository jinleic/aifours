"""EXPLORATORY (floats, evidence only): tune the closed-form restricted-dual bound B_g, g(m) = beta ln m + gamma m,
at d = 8, and test a row-separable relaxation.

T1. For g = (beta, gamma): the minimum normalised margin r_g = min_{M in B_4} (B_g(J) - B_g(M)) / |M-J|^2
    (multistart SLSQP), plus the Hessian quadratic coefficient of B_g at J along random tangent directions.
T2. Nelder-Mead over (beta, gamma) maximising r_g (bounded iterations).
T3. Row-only Cauchy-Schwarz relaxation R_g (keep row sums of Y, relax column sums):
      Y^T A Y <= (3/4)(sum Y)^2 - sum_p S_p^2 + sum Y^2,  S_p = sum_q Y_pq,
    worst case of R_g - Psi(J) on B_4 and on row-stochastic matrices.
Writes ../evidence/explore_d8_tune.json.  Single-threaded, finite loops.
"""
import json
import math
import os
import time

import numpy as np
from scipy.optimize import minimize

import explore_exact_exponent as E
from explore_d8_dualfamilies import B_g, PSIJ, cons_ds, cons_rows, C, D, K

J = E.J


def R_g(M, par):
    m = np.clip(M.reshape(-1), 1e-300, None)
    beta, gamma = par
    g = beta * np.log(m) + gamma * m
    Y = np.exp(g)
    lin = np.sum((D - 1) / 4 * m * np.log(m) - D / 4 * m * g)
    Ym = Y.reshape(K, K)
    S = Ym.sum(axis=1)
    Q = 0.75 * Y.sum() ** 2 - np.sum(S * S) + np.sum(Y * Y)
    return C - (D / 2) * math.log(4 * D) + D / 2 + lin + (D / 2) * math.log(Q)


def starts(rng, n):
    pts = []
    for s in range(n):
        kind = s % 3
        if kind == 0:
            pts.append(E.sinkhorn(np.exp(rng.normal(scale=rng.choice([1, 2, 4]), size=(K, K)))))
        elif kind == 1:
            pts.append(E.family(np.eye(K)[rng.permutation(K)], rng.uniform(0.2, 0.95)))
        else:
            w = rng.dirichlet(np.ones(3))
            pts.append(0.9 * sum(wi * np.eye(K)[rng.permutation(K)] for wi in w) + 0.1 * J)
    return pts


def min_ratio(fun, pts, rows_only=False):
    best = (1e9, None, None)
    cons = cons_rows() if rows_only else cons_ds()
    for M0 in pts:
        def obj(z):
            M = np.clip(z.reshape(K, K), 1e-14, None)
            n2 = float(np.sum((M - J) ** 2))
            if n2 < 1e-9:
                return 1.0
            return (PSIJ - fun(M)) / n2
        res = minimize(obj, M0.reshape(-1), method="SLSQP", bounds=[(1e-12, 1.0)] * 16, constraints=cons,
                       options={"maxiter": 200, "ftol": 1e-12})
        M = np.clip(res.x.reshape(K, K), 1e-14, None)
        M = (M / M.sum(axis=1, keepdims=True)) if rows_only else E.sinkhorn(M, 30)
        n2 = float(np.sum((M - J) ** 2))
        if n2 > 1e-9:
            r = (PSIJ - fun(M)) / n2
            if r < best[0]:
                best = (r, n2, M.round(4).tolist())
    return best


def hess_coeff(fun, rng, n=6):
    vals = []
    for _ in range(n):
        a = rng.normal(size=(K, K))
        a -= a.mean(axis=1, keepdims=True)
        a -= a.mean(axis=0, keepdims=True)
        a /= np.linalg.norm(a)
        e = 1e-3
        vals.append((fun(J + e * a) + fun(J - e * a) - 2 * fun(J)) / (2 * e * e))
    return vals


def main():
    t0 = time.time()
    rng = np.random.default_rng(8088)
    pts = starts(rng, 24)
    out = {"note": "EXPLORATORY numerics (floats); evidence only; no claim."}
    base = (1.25, -1.5)
    fb = lambda M: B_g(M, (base[0], base[1], 0.0))
    out["T1 base g=(1.25,-1.5)"] = {"min normalised margin r_g (value, |M-J|^2, M)": min_ratio(fb, pts),
                                   "Hessian coefficients at J": hess_coeff(fb, rng)}
    # T2: Nelder-Mead on (beta, gamma), maximise r_g using a smaller start set
    sub = pts[:12]
    hist = []

    def neg_r(par):
        f = lambda M: B_g(M, (par[0], par[1], 0.0))
        r = min_ratio(f, sub)[0]
        hist.append((float(par[0]), float(par[1]), float(r)))
        return -r
    res = minimize(neg_r, np.array(base), method="Nelder-Mead", options={"maxfev": 40, "xatol": 1e-3, "fatol": 1e-5})
    bp = (float(res.x[0]), float(res.x[1]))
    fbest = lambda M: B_g(M, (bp[0], bp[1], 0.0))
    out["T2 Nelder-Mead best (beta, gamma)"] = bp
    out["T2 best r_g recheck with all 24 starts"] = min_ratio(fbest, pts)
    out["T2 Hessian coefficients at J for best g"] = hess_coeff(fbest, rng)
    out["T2 history (beta, gamma, r_g on 12 starts)"] = hist
    # T3: row-only Cauchy-Schwarz relaxation
    fr = lambda M: R_g(M, bp)
    out["T3 R_g(J) - Psi(J)"] = R_g(J, bp) - PSIJ
    out["T3 row-relaxed R_g: min normalised margin on B_4"] = min_ratio(fr, pts)
    out["T3 row-relaxed R_g: min normalised margin on row-stochastic"] = min_ratio(fr, pts, rows_only=True)
    out["seconds"] = round(time.time() - t0, 1)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "explore_d8_tune.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()

"""Random-walk exploration of realizable fully-closed marginal boxes (exploratory).

Usage: python closed_mcmc.py N STEPS SEED OUT.jsonl [THIN]
State u = (log increments of the tiling points (n-1), log lead_lo, log(m-1)), lead_hi =
lead_lo*m.  A start point is found by minimizing the realizability violation and then
moved into the interior (maximizing the smallest normalized coefficient width); then an
adaptive Gaussian random walk restricted to the realizable set.  Every THIN-th state is
tested with the closed LP including the exact double-contact equalities.
"""
from __future__ import annotations

import json
import sys

import numpy as np
from scipy.optimize import minimize

from closed_limit import box_from_endpoints, build_endpoints, closed_lp

U_LO, U_HI = -6.0, 2.3   # log increment bounds: x_{i+1}/x_i in (1 + e^-6, 1 + e^2.3)


def decode(u, n):
    inc = np.exp(np.clip(u[:n - 1], U_LO, U_HI))
    x = np.cumprod(np.concatenate([[1.0], 1 + inc]))
    x = x / np.exp(np.mean(np.log(x)))
    llo = float(np.exp(np.clip(u[n - 1], -6, 6)))
    lhi = llo * (1.0 + float(np.exp(np.clip(u[n], -8, 4))))
    return x, llo, lhi


def widths(u, n):
    x, llo, lhi = decode(u, n)
    Em, Ep, Om, Op = build_endpoints(x, n, llo, lhi)
    dE, dO = Ep - Em, Op - Om
    if n % 2 == 0:
        dE = dE[:-1]   # monic top coefficient of E: structurally zero width
    else:
        dO = dO[:-1]
    sc = max(np.abs(Em).max(), np.abs(Om).max(), np.abs(Ep).max(), np.abs(Op).max())
    return np.concatenate([dE, dO]) / sc


def violation(u, n):
    return float(np.sum(np.maximum(0.0, -widths(u, n))))


def neg_slack(u, n):
    w = widths(u, n)
    return float(-w.min())


def in_bounds(u, n):
    return bool(np.all(u[:n - 1] >= U_LO) and np.all(u[:n - 1] <= U_HI))


def find_start(n, rng, tries=300):
    for _ in range(tries):
        u0 = np.concatenate([rng.uniform(U_LO, U_HI, n - 1),
                             [rng.uniform(-3, 3), rng.uniform(-4, 2)]])
        r = minimize(violation, u0, args=(n,), method="Nelder-Mead",
                     options={"maxiter": 6000, "xatol": 1e-10, "fatol": 1e-16})
        if r.fun <= 0 and in_bounds(r.x, n):
            r2 = minimize(neg_slack, r.x, args=(n,), method="Nelder-Mead",
                          options={"maxiter": 4000})
            u = r2.x if (r2.fun < 0 and in_bounds(r2.x, n)) else r.x
            if violation(u, n) <= 0:
                return u
    return None


def grid_for(x, npts=3000):
    g = np.logspace(np.log10(x.min()) - 2, np.log10(x.max()) + 2, npts)
    d = np.array([1e-2, 3e-3, 1e-3, 3e-4, 1e-4])
    near = np.concatenate([xi * (1 + np.concatenate([-d, d])) for xi in x])
    g = np.concatenate([[0.0], g, near])
    keep = np.ones(g.size, bool)
    for xi in x:
        keep &= np.abs(g - xi) > 1e-5 * xi
    return np.unique(g[keep])


def main():
    n, steps, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    thin = int(sys.argv[5]) if len(sys.argv) > 5 else 10
    rng = np.random.default_rng(seed)
    u = find_start(n, rng)
    if u is None:
        print(json.dumps({"n": n, "error": "no realizable start found"}))
        return
    step, acc_win, acc = 0.3, [], 0
    worst, tested, nfail = None, 0, 0
    with open(out, "w") as fh:
        for it in range(steps):
            prop = u + step * rng.standard_normal(u.size)
            ok = in_bounds(prop, n) and violation(prop, n) <= 0
            if ok:
                u = prop
                acc += 1
            acc_win.append(ok)
            if len(acc_win) == 50:
                rate = np.mean(acc_win)
                step *= 1.3 if rate > 0.3 else (0.7 if rate < 0.15 else 1.0)
                step = float(np.clip(step, 1e-4, 2.0))
                acc_win = []
            if it % thin:
                continue
            x, llo, lhi = decode(u, n)
            Em, Ep, Om, Op = build_endpoints(x, n, llo, lhi)
            st, s, beta = closed_lp(Em, Ep, Om, Op, n, grid_for(x), x=x)
            tested += 1
            nfail += st != 0
            lo, hi = box_from_endpoints(Em, Ep, Om, Op, n)
            rec = {"it": it, "u": u.tolist(), "status": st, "s": s, "minwidth": -neg_slack(u, n),
                   "lo": lo.tolist(), "hi": hi.tolist(),
                   "beta": None if beta is None else beta.tolist()}
            fh.write(json.dumps(rec) + "\n")
            key = -np.inf if st != 0 else s
            if worst is None or key < worst[0]:
                worst = (key, it, st, s)
    print(json.dumps({"n": n, "steps": steps, "accept_rate": acc / steps, "tested": tested,
                      "lp_infeasible": int(nfail), "worst": worst}))


if __name__ == "__main__":
    main()

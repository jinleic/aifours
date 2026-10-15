"""Adversarial minimization of the closed-problem margin over realizable fully-closed boxes.

Usage: python closed_opt.py N SEED EVALS OUT.json
Margin (scale-free): after imposing the n-2 exact double contacts (Prop. D) the closed numerators
form the 3-dim space spanned by an orthonormal null basis v1..v3; rows r(t, c) = (P_c(t; v_k) /
|K_c(jw)|^2)_k are normalized to unit length and
    margin = max_{|lam_k| <= 1} min_{t, c} r(t, c) . lam   (LP; >= 0 always, = 0 iff no strictly
    positive closed numerator exists on the grid up to degeneracy).
Strictly, a counterexample needs closed-INfeasibility; this float64 screen only ranks candidates;
minimizers are re-tested with closed_exact3.py (60-digit arithmetic).  Exploratory.
"""
from __future__ import annotations

import json
import sys

import cma
import numpy as np
from numpy.polynomial import polynomial as P
from scipy.optimize import linprog

from closed_limit import build_endpoints
from closed_mcmc import decode, find_start, grid_for, in_bounds, violation


def margin(u, n, npts=1500):
    if not in_bounds(u, n) or violation(u, n) > 0:
        return None
    x, llo, lhi = decode(u, n)
    Em, Ep, Om, Op = build_endpoints(x, n, llo, lhi)
    Es, Os = (Em, Ep), (Om, Op)
    C = []
    for xi in x[1:n - 1]:
        ie = int(np.argmin([abs(P.polyval(xi, E)) for E in Es]))
        io = int(np.argmin([abs(P.polyval(xi, O)) for O in Os]))
        dE = P.polyval(xi, P.polyder(Es[ie]))
        dO = P.polyval(xi, P.polyder(Os[io]))
        r = np.array([(-1) ** (k // 2) * (xi ** (k // 2) * dE if k % 2 == 0 else xi ** (k // 2 + 1) * dO)
                      for k in range(n + 1)])
        C.append(r / np.linalg.norm(r))
    _, S, Vt = np.linalg.svd(np.array(C), full_matrices=True)
    N = Vt[n - 2:].T  # (n+1) x 3
    t = grid_for(x, npts)
    rows = []
    for i in (0, 1):
        for j in (0, 1):
            Ev, Ov = P.polyval(t, Es[i]), P.polyval(t, Os[j])
            den = Ev * Ev + t * Ov * Ov
            B = np.empty((t.size, n + 1))
            for k in range(n + 1):
                l = k // 2
                B[:, k] = (-1) ** l * (t ** l * Ev if k % 2 == 0 else t ** (l + 1) * Ov)
            R = (B @ N) / den[:, None]
            nr = np.linalg.norm(R, axis=1)
            ok = np.isfinite(nr) & (nr > 0)
            rows.append(R[ok] / nr[ok][:, None])
    R = np.vstack(rows)
    res = linprog([0, 0, 0, -1], A_ub=np.hstack([-R, np.ones((len(R), 1))]), b_ub=np.zeros(len(R)),
                  bounds=[(-1, 1)] * 3 + [(None, 1)], method="highs")
    return float(res.x[-1]) if res.status == 0 else None


def main():
    n, seed, evals, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = np.random.default_rng(seed)
    u0 = find_start(n, rng)
    best = {"margin": np.inf}
    hist = []

    def f(u):
        u = np.asarray(u)
        m = margin(u, n)
        # continuous penalty outside the realizable set keeps the landscape informative
        val = (1.0 + 100.0 * violation(u, n)) if m is None else m
        if m is not None and m < best["margin"]:
            best.update(margin=m, u=list(map(float, u)))
        hist.append(val)
        return val

    lo_b = np.array([-6.0] * (n - 1) + [-6.0, -8.0])
    hi_b = np.array([2.3] * (n - 1) + [6.0, 4.0])
    u0 = np.clip(u0, lo_b + 1e-6, hi_b - 1e-6)
    es = cma.CMAEvolutionStrategy(list(u0), 0.1, {"seed": seed, "maxfevals": evals, "verbose": -9,
                                                  "tolflatfitness": 10 ** 6, "tolfun": 0,
                                                  "tolfunhist": 0, "tolx": 1e-9,
                                                  "bounds": [list(lo_b), list(hi_b)]})
    while not es.stop():
        xs = es.ask()
        es.tell(xs, [f(x) for x in xs])
    json.dump({"n": n, "seed": seed, "evals": len(hist), "best": best,
               "hist_min": float(np.min(hist))}, open(out, "w"))
    print(json.dumps({"n": n, "seed": seed, "evals": len(hist), "best_margin": best["margin"]}))


if __name__ == "__main__":
    main()

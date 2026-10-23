"""Experiment G1 (exploratory, float): is the nonnegative-COEFFICIENT width structure of
interval boxes essential?  Generalized rectangle families: endpoint components with the
fully-closed band geometry, but only requiring W_E = E+ - E- >= 0 and W_O >= 0 on [0, inf)
(not coefficientwise).  For n=5, 6, 7 search (random + CMA-ES) for fully-closed generalized
families whose closed problem (3-dim contact kernel) is infeasible on a grid.

Usage: python genrect.py N SEED ITERS OUT.json
"""
from __future__ import annotations

import json
import sys

import numpy as np
from numpy.polynomial import polynomial as NP

from fclosed import (band_roots, xpoly, kernel_scaled, residual_rows, lp_margin,
                     realizable)


def nonneg_halfline(p, tol=1e-12):
    """True if polynomial p (ascending) is >= 0 on [0, inf) (float check via roots)."""
    p = np.trim_zeros(np.asarray(p, float), 'b')
    if p.size == 0:
        return True
    if p[-1] < 0 or p[0] < -tol * np.abs(p).max():
        return False
    r = np.roots(p[::-1])
    for z in r:
        if abs(z.imag) < 1e-9 * max(1, abs(z)) and z.real > 0:
            # sign change at a simple positive real root?
            tt = z.real
            for d in (1e-6, -1e-6):
                if NP.polyval(tt * (1 + d), p) < -tol * np.abs(p).max():
                    return False
    return True


def build(x, n, leads):
    """leads = (lam_Em, lam_Ep, lam_Om, lam_Op); monic constraint is NOT imposed for the
    generalized family except the common top coefficient of the fixed component."""
    Em, Ep, Om, Op = band_roots(x, n)
    return (xpoly(Em, leads[0]), xpoly(Ep, leads[1]), xpoly(Om, leads[2]), xpoly(Op, leads[3]))


def margin_of(params, n, mode):
    """params: log-gaps (n-1) and log-lead ratios; returns (margin, info)."""
    g = np.exp(params[:n - 1])
    x = np.concatenate([[1.0], 1.0 + np.cumsum(g)])
    la = np.exp(params[n - 1:])
    if n % 2 == 1:
        leads = (la[0], la[1], 1.0, 1.0)   # E free leads, O monic
    else:
        leads = (1.0, 1.0, la[0], la[1])
    Em, Ep, Om, Op = build(x, n, leads)
    WE, WO = NP.polysub(Ep, Em), NP.polysub(Op, Om)
    if mode == 'box':
        ok = realizable(Em, Ep, Om, Op, tol=1e-10)
    else:
        ok = nonneg_halfline(WE) and nonneg_halfline(WO)
    if not ok:
        return None, None
    try:
        with np.errstate(over='raise', invalid='raise', divide='raise', under='ignore'):
            K, sv = kernel_scaled(x, n, Em, Ep, Om, Op)
            if K.shape[1] != 3:
                return None, None
            R, keys, tv = residual_rows(x, n, Em, Ep, Om, Op, K)
        if not np.all(np.isfinite(R)):
            return None, None
        if sv[-1] < 1e-6 * sv[0]:
            return None, None
        m, y = lp_margin(R)
        if m is None:
            return None, None
    except (FloatingPointError, ValueError, np.linalg.LinAlgError):
        return None, None
    return m, {'x': x.tolist(), 'leads': list(map(float, leads)), 'WE': WE.tolist(),
               'WO': WO.tolist(), 'b': (K @ y).tolist()}


def main():
    n = int(sys.argv[1]); seed = int(sys.argv[2]); iters = int(sys.argv[3]); out = sys.argv[4]
    mode = sys.argv[5] if len(sys.argv) > 5 else 'gen'
    rng = np.random.default_rng(seed)
    best = (np.inf, None)
    feas = 0
    hist = []
    for it in range(iters):
        p = np.concatenate([rng.normal(0, 2.0, n - 1), rng.normal(0, 3.0, 2)])
        m, info = margin_of(p, n, mode)
        if m is None:
            continue
        feas += 1
        hist.append(m)
        if m < best[0]:
            best = (m, info)
    import cma
    if best[1] is not None:
        # local CMA refinement from best
        x0 = None
        b = best[1]
        xx = np.array(b['x'])
        g0 = np.log(np.diff(xx))
        la = np.array(b['leads'][:2] if n % 2 == 1 else b['leads'][2:])
        x0 = np.concatenate([g0, np.log(la)])

        def f(p):
            m, _ = margin_of(p, n, mode)
            return 10.0 if m is None else m
        es = cma.CMAEvolutionStrategy(x0, 0.5, {'seed': seed, 'maxfevals': 3000,
                                                'verbose': -9})
        es.optimize(f)
        mb, infob = margin_of(es.result.xbest, n, mode)
        if mb is not None and mb < best[0]:
            best = (mb, infob)
    json.dump({'n': n, 'mode': mode, 'seed': seed, 'iters': iters, 'feasible_samples': feas,
               'min_margin': best[0], 'best': best[1],
               'margin_quantiles': np.quantile(hist, [0, 0.01, 0.1, 0.5]).tolist() if hist else None},
              open(out, 'w'), indent=1)
    print(n, mode, 'feasible samples', feas, 'min margin', best[0])


if __name__ == '__main__':
    main()

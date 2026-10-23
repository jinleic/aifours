"""Experiment B1 (exploratory, float): CMA-ES minimisation of the homogeneous LP closed margin
over fully-closed configurations, in two modes:
  box : widths must have nonnegative t-coefficients (genuine monic interval boxes);
  gen : widths only nonnegative on [0, inf) (generalized rectangle families; control showing
        the search CAN find closed-infeasible configurations when they exist).
Parameters: log-gaps of x (x_0 = 1) and log of the two free leads.  Penalised objective when
not realizable.  Records the best (smallest margin) well-conditioned configuration.

Usage: python boxsearch.py N MODE SEED RESTARTS FEVALS OUT.json
"""
from __future__ import annotations

import json
import sys

import numpy as np
from numpy.polynomial import polynomial as NP

from fclosed import (band_roots, xpoly, kernel_scaled, residual_rows, lp_margin,
                     lp_margin_precond)

PRECOND = True
from genrect import nonneg_halfline


def build(x, n, la):
    Em, Ep, Om, Op = band_roots(x, n)
    if n % 2 == 1:
        return xpoly(Em, la[0]), xpoly(Ep, la[1]), xpoly(Om, 1.0), xpoly(Op, 1.0)
    return xpoly(Em, 1.0), xpoly(Ep, 1.0), xpoly(Om, la[0]), xpoly(Op, la[1])


def violation(W):
    sc = np.abs(W).max() + 1e-300
    return float(np.sum(np.maximum(0.0, -W)) / sc)


def evaluate(p, n, mode):
    g = np.exp(np.clip(p[:n - 1], -12, 12))
    x = np.concatenate([[1.0], 1.0 + np.cumsum(g)])
    # gauge: the free component's scale is a symmetry (scale E for n odd, O for n even, numerator
    # part inversely); fix the '-' lead to 1 and vary only the ratio (last parameter).
    la = np.array([1.0, np.exp(np.clip(p[-1], -12, 12))])
    Em, Ep, Om, Op = build(x, n, la)
    WE, WO = NP.polysub(Ep, Em), NP.polysub(Op, Om)
    if mode == 'box':
        v = violation(WE) + violation(WO)
        if v > 0:
            return 1.0 + v, None
    elif mode in ('genmono', 'gen', 'genE', 'genO'):
        # gen: both widths >= 0 pointwise; genmono: both also nondecreasing;
        # genE: W_E pointwise only, W_O nondecreasing; genO: W_O pointwise only, W_E nondecreasing
        polys = [WE, WO]
        if mode == 'genmono':
            polys += [NP.polyder(WE), NP.polyder(WO)]
        elif mode == 'genE':
            polys += [NP.polyder(WO)]
        elif mode == 'genO':
            polys += [NP.polyder(WE)]
        v = 0.0
        for W in polys:
            W = np.trim_zeros(np.asarray(W, float), 'b')
            if W.size == 0:
                continue
            # candidate minimisers on [0, inf): 0 and positive real critical points
            cands = [0.0]
            if W.size > 2:
                for z in np.roots(NP.polyder(W)[::-1]):
                    if abs(z.imag) <= 1e-9 * max(1.0, abs(z)) and z.real > 0:
                        cands.append(z.real)
            cands = np.array(cands)
            vals = NP.polyval(cands, W) / (NP.polyval(cands, np.abs(W)) + 1e-300)
            v += float(np.max(np.maximum(0.0, -vals))) + (1.0 if W[-1] < 0 else 0.0)
        if v > 1e-12:
            return 1.0 + v, None
    # conditioning guard: relative point separation
    sep = np.min(np.diff(np.log(x)))
    if sep < 1e-5:
        return 1.2, None
    try:
        with np.errstate(over='raise', invalid='raise', divide='raise', under='ignore'):
            K, sv = kernel_scaled(x, n, Em, Ep, Om, Op)
            if K.shape[1] != 3 or sv[-1] < 1e-7 * sv[0]:
                return 1.2, None
            R, keys, tv = residual_rows(x, n, Em, Ep, Om, Op, K)
        if not np.all(np.isfinite(R)):
            return 1.2, None
        m, y = lp_margin_precond(R) if PRECOND else lp_margin(R)
    except (FloatingPointError, ValueError, np.linalg.LinAlgError):
        return 1.2, None
    if m is None:
        return 1.2, None
    pen = 0.01 * max(0.0, np.log10(1e-4 * sv[0] / sv[-1])) + 0.01 * max(0.0, np.log10(1e-3 / sep))
    return m + pen, {'margin': m, 'x': x.tolist(), 'la': la.tolist(), 'WE': WE.tolist(), 'WO': WO.tolist(),
               'sv_min_rel': float(sv[-1] / sv[0]), 'min_log_sep': float(sep)}


def main():
    n = int(sys.argv[1]); mode = sys.argv[2]; seed = int(sys.argv[3])
    restarts = int(sys.argv[4]); fevals = int(sys.argv[5]); out = sys.argv[6]
    import cma
    rng = np.random.default_rng(seed)
    best = (np.inf, None, None)
    runs = []
    starts = json.load(open(sys.argv[7])) if len(sys.argv) > 7 else None
    for r in range(restarts):
        x0 = None
        if starts:
            x0 = np.array(starts[r % len(starts)], float)
            if x0.size == n + 1:   # old format (gaps, log lead_m, log lead_p) -> ratio
                x0 = np.concatenate([x0[:n - 1], [x0[n] - x0[n - 1]]])
            x0 = x0 + (rng.normal(0, 0.05, x0.size) if r >= len(starts) else 0.0)
        else:
            for _ in range(20000):
                p = np.concatenate([rng.normal(0, 1.5, n - 1), rng.normal(0, 2.0, 1)])
                val, info = evaluate(p, n, mode)
                if info is not None:
                    x0 = p
                    break
            if x0 is None:
                x0 = p   # let CMA descend the realizability penalty
        sig0 = 0.15 if starts else 0.6
        es = cma.CMAEvolutionStrategy(x0, sig0, {'seed': int(seed * 1000 + r), 'maxfevals': fevals,
                                                 'verbose': -9})
        es.optimize(lambda q: evaluate(q, n, mode)[0])
        val, info = evaluate(es.result.xbest, n, mode)
        runs.append({'restart': r, 'start_found': True, 'best': val, 'info': info,
                     'p': es.result.xbest.tolist()})
        if info is not None and val < best[0]:
            best = (val, info, es.result.xbest.tolist())
    json.dump({'n': n, 'mode': mode, 'seed': seed, 'restarts': restarts, 'fevals': fevals,
               'best_margin': best[0], 'best': best[1], 'best_p': best[2], 'runs': runs},
              open(out, 'w'), indent=1)
    print(n, mode, seed, 'best margin', best[0],
          'per-restart', [round(rr.get('best', np.nan), 6) if rr.get('start_found') else None
                          for rr in runs])


if __name__ == '__main__':
    main()

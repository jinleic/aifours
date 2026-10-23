"""Experiment DERIV (exploratory, float): test the explicit candidate b = c0' + eps * c0 (c0 = box
centre, ' = d/ds) as a common SPR numerator.  Motivation: c0'/c0 is SPR for Hurwitz c0
(log-derivative), and near every lightly damped root of c0 the local SPR condition for the box
reduces to local robust stability exactly when b(i beta) is a positive multiple of c0'(i beta).
Reports the worst normalised pairing cos(arg b - arg c) over corners and a fine grid.

Usage: python derivcand.py N COUNT SEED ETA
"""
from __future__ import annotations

import sys

import numpy as np
from numpy.polynomial import polynomial as NP

from advbox import box_from_params, corners_hurwitz
from sprcore import EO, corner_polys, pairing


def worst_cos(b, lo, hi, grid):
    Eb, Ob = EO(b)
    Ebv, Obv = NP.polyval(grid, Eb), NP.polyval(grid, Ob)
    mb = np.sqrt(Ebv ** 2 + grid * Obv ** 2)
    worst = (np.inf, None, None)
    for k, c in corner_polys(lo, hi).items():
        Ec, Oc = EO(c)
        Ev, Ov = NP.polyval(grid, Ec), NP.polyval(grid, Oc)
        P = Ebv * Ev + grid * Obv * Ov
        mc = np.sqrt(Ev ** 2 + grid * Ov ** 2)
        r = P / (mb * mc + 1e-300)
        i = int(np.argmin(r))
        if r[i] < worst[0]:
            worst = (float(r[i]), k, float(grid[i]))
    return worst


def main():
    n = int(sys.argv[1]); count = int(sys.argv[2]); seed = int(sys.argv[3]); eta = float(sys.argv[4])
    rng = np.random.default_rng(seed)
    grid = np.concatenate([[0.0], np.logspace(-5, 5, 40001)])
    npar = 2 * (n // 2) + (n % 2)
    fails = 0
    res = []
    for it in range(count):
        p = np.concatenate([rng.uniform(-2.3, 2.3, npar) * np.tile([1, 0], npar // 2 + 1)[:npar]
                            + rng.uniform(-3, 3, npar) * np.tile([0, 1], npar // 2 + 1)[:npar],
                            rng.uniform(-5, 1, n)])
        bx = box_from_params(p, n, eta)
        if bx is None:
            continue
        lo, hi = bx
        c0 = np.append((lo + hi) / 2, 1.0)
        d0 = NP.polyder(c0)
        best = None
        for eps in (0.0, 1e-3, 1e-2, 1e-1):
            b = NP.polyadd(d0, eps * c0) if eps > 0 else np.append(d0, 0.0)
            w = worst_cos(b, lo, hi, grid)
            if best is None or w[0] > best[0][0]:
                best = (w, eps)
        res.append(best[0][0])
        if best[0][0] <= 0:
            fails += 1
    res = np.array(res)
    print(n, 'eta', eta, 'boxes', len(res), 'fail', fails, 'quantiles', np.round(np.quantile(res, [0, 0.05, 0.25, 0.5]), 4))


if __name__ == '__main__':
    main()

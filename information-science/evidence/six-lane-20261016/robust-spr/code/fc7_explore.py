"""Exploration (float, not evidence of any universal claim): realizable fully-closed degree-7
boxes; where does the max-margin closed numerator bind?  Classifies each binding point as
'end-low' (t < x_1), 'end-high' (t > x_{n-2}) or 'interior band j'.

Usage: python fc7_explore.py N_SAMPLES SEED OUT.jsonl
"""
from __future__ import annotations

import json
import sys

import numpy as np
from numpy.polynomial import polynomial as NP

from fclosed import (band_roots, endpoints, realizable, kernel_scaled, residual_rows,
                     sphere_margin, grid_for)


def esym(roots):
    p = np.array([1.0])
    for r in roots:
        p = NP.polymul(p, np.array([-r, 1.0]))
    # p(t) = prod (t - r) = t^3 - e1 t^2 + e2 t - e3
    d = len(roots)
    return [(-1) ** k * p[d - k] for k in range(1, d + 1)]


def rho_interval(x, n=7):
    Em, Ep, Om, Op = band_roots(x, n)
    em, ep = esym(Em), esym(Ep)
    om, op = esym(Om), esym(Op)
    # O widths (monic, lead 1 in prod (x - t) form): O(t) = e3 - e2 t + e1 t^2 - t^3
    okO = (op[0] >= om[0]) and (op[1] <= om[1]) and (op[2] >= om[2])
    lo = max(em[0] / ep[0], em[2] / ep[2])
    hi = min(1.0, em[1] / ep[1])
    return okO, lo, hi


def sample_x(rng, n=7):
    g = np.exp(rng.normal(0.0, 1.5, size=n - 1))
    x = np.concatenate([[1.0], 1.0 + np.cumsum(g)])
    # random log-rescaling of gaps to create clusters
    if rng.random() < 0.5:
        g = np.exp(rng.uniform(-4, 3, size=n - 1))
        x = np.concatenate([[1.0], 1.0 + np.cumsum(g)])
    return x


def classify(t, x, n=7):
    if t < x[1]:
        return 'low'
    if t > x[n - 2]:
        return 'high'
    j = int(np.searchsorted(x, t))
    return f'band{j}'


def main():
    N = int(sys.argv[1]); seed = int(sys.argv[2]); out = sys.argv[3]
    rng = np.random.default_rng(seed)
    n = 7
    done = 0
    tries = 0
    with open(out, 'w') as f:
        while done < N and tries < 200 * N:
            tries += 1
            x = sample_x(rng)
            okO, lo, hi = rho_interval(x)
            if not okO or lo > hi:
                continue
            rho = lo + (hi - lo) * rng.random()
            lam_m = np.exp(rng.uniform(-3, 3)) * np.sqrt(x[-1])
            Em, Ep, Om, Op = endpoints(x, n, lam_m, rho * lam_m)
            if not realizable(Em, Ep, Om, Op, tol=1e-9):
                continue
            K, sv = kernel_scaled(x, n, Em, Ep, Om, Op)
            if K.shape[1] != 3:
                continue
            R, keys, tv = residual_rows(x, n, Em, Ep, Om, Op, K)
            m, y = sphere_margin(R, nstart=3000, seed=done)
            vals = R @ y
            idx = np.argsort(vals)[:6]
            bind = [(str(keys[i]), float(tv[i]), float(vals[i]), classify(tv[i], x))
                    for i in idx]
            rec = {'x': x.tolist(), 'rho': rho, 'rho_int': [lo, hi], 'lam_m': lam_m,
                   'margin': m, 'b': (K @ y).tolist(), 'bind': bind}
            f.write(json.dumps(rec) + '\n')
            done += 1
    print('done', done, 'tries', tries)


if __name__ == '__main__':
    main()

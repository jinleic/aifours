"""Generate realizable fully-closed box configurations (nonnegative width coefficients) for a
given n by structured random sampling: geometric band centres, alternating narrow/wide bands
with random widths, then a scan over the free lead ratio.  Output: JSON list of boxsearch
parameter vectors p = (log gaps (n-1), log lead_m, log lead_p).

Usage: python fcstarts.py N COUNT SEED OUT.json
"""
from __future__ import annotations

import json
import sys

import numpy as np
from numpy.polynomial import polynomial as NP

from boxsearch import build


def realizable_ratio(x, n, rng, tries=60):
    for _ in range(tries):
        lm = np.exp(rng.uniform(-3, 3)) * (x[-1] ** 0.5 if n % 2 else 1.0)
        rho = np.exp(rng.uniform(-3, 3))
        la = np.array([lm, lm * rho])
        Em, Ep, Om, Op = build(x, n, la)
        WE, WO = NP.polysub(Ep, Em), NP.polysub(Op, Om)
        sc = max(np.abs(WE).max(), np.abs(WO).max())
        if np.all(WE >= -1e-12 * np.abs(WE).max()) and np.all(WO >= -1e-12 * np.abs(WO).max()):
            return la
    return None


def main():
    n = int(sys.argv[1]); count = int(sys.argv[2]); seed = int(sys.argv[3]); out = sys.argv[4]
    rng = np.random.default_rng(seed)
    starts = []
    tries = 0
    while len(starts) < count and tries < 200000:
        tries += 1
        mode = rng.integers(3)
        ratio = np.exp(rng.uniform(0.3, 3.0))
        centres = ratio ** np.arange(n)
        g = np.empty(n - 1)
        for k in range(n - 1):
            narrow = (k % 2 == 0) if mode == 0 else ((k % 2 == 1) if mode == 1 else rng.random() < 0.5)
            g[k] = np.exp(rng.uniform(-6, -1) if narrow else rng.uniform(-0.5, 1.5))
        x = np.concatenate([[1.0], 1.0 + np.cumsum(g * centres[:-1])])
        la = realizable_ratio(x, n, rng)
        if la is None:
            continue
        starts.append(np.concatenate([np.log(np.diff(x)), np.log(la)]).tolist())
    json.dump(starts, open(out, 'w'))
    print(n, 'starts', len(starts), 'tries', tries)


if __name__ == '__main__':
    main()

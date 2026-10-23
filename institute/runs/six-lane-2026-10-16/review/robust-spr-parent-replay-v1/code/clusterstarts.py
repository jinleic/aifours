"""Targeted fully-closed geometries motivated by G1 (reversed): a tight cluster of k consecutive
band points at LOW frequency followed by wide bands, which monotone (box) widths can support.
Generates box-realizable configurations and reports their gauge-fixed preconditioned closed LP
margins; writes realizable ones as boxsearch starts.

Usage: python clusterstarts.py N COUNT SEED OUT.json
"""
from __future__ import annotations

import json
import sys

import numpy as np
from numpy.polynomial import polynomial as NP

from boxsearch import build, evaluate


def main():
    n = int(sys.argv[1]); count = int(sys.argv[2]); seed = int(sys.argv[3]); out = sys.argv[4]
    rng = np.random.default_rng(seed)
    starts, margins = [], []
    tries = 0
    while len(starts) < count and tries < 400000:
        tries += 1
        k = int(rng.integers(3, n))             # cluster size (points)
        start = int(rng.integers(0, n - k + 1))  # cluster position
        g = np.empty(n - 1)
        for i in range(n - 1):
            in_cluster = start <= i < start + k - 1
            g[i] = np.exp(rng.uniform(-7, -2)) if in_cluster else np.exp(rng.uniform(-1, 4))
        x = np.concatenate([[1.0], 1.0 + np.cumsum(g * np.exp(rng.uniform(-1, 1, n - 1)))])
        for _ in range(30):
            ratio = np.exp(rng.uniform(-4, 4))
            p = np.concatenate([np.log(np.diff(x)), [np.log(ratio)]])
            v, info = evaluate(p, n, 'box')
            if info is not None:
                starts.append(p.tolist()); margins.append(info['margin'])
                break
    json.dump(starts, open(out, 'w'))
    m = np.array(margins)
    print(n, 'starts', len(starts), 'tries', tries,
          'margin quantiles', np.round(np.quantile(m, [0, 0.05, 0.5]), 5) if m.size else None)


if __name__ == '__main__':
    main()

"""Random search over fully-closed marginal boxes; tests the closed problem (exploratory).

Usage: python closed_search.py N TRIALS SEED OUT.jsonl
For each realizable fully-closed configuration records the closed LP margin
s* = max_{beta>=0, sum=1} min_{t,c} P_c(t)/|K_c|^2 (grid), and whether a slightly shrunk
box (toward the coefficient-box center) is robustly Hurwitz.
"""
from __future__ import annotations

import json
import sys

import numpy as np

from closed_limit import (box_from_endpoints, build_endpoints, closed_grid, closed_lp,
                          realizable)
from sprlib import box_is_stable


def sample_config(n, rng):
    inc = 10 ** rng.uniform(-2.0, 1.0, size=n - 1)
    x = np.cumprod(np.concatenate([[1.0], 1 + inc]))
    x = x / np.exp(np.mean(np.log(x)))
    lead_lo = 10 ** rng.uniform(-2, 2)
    m = 10 ** rng.uniform(0, 1.5)
    return x, lead_lo, lead_lo * m


def main():
    n, trials, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    rng = np.random.default_rng(seed)
    acc = 0
    worst = None
    with open(out, "w") as fh:
        for it in range(trials):
            x, llo, lhi = sample_config(n, rng)
            Em, Ep, Om, Op = build_endpoints(x, n, llo, lhi)
            ok, dE, dO = realizable(Em, Ep, Om, Op)
            if not ok:
                continue
            acc += 1
            lo, hi = box_from_endpoints(Em, Ep, Om, Op, n)
            cen = 0.5 * (lo + hi)
            shrunk_ok = box_is_stable(cen + (1 - 1e-6) * (lo - cen), cen + (1 - 1e-6) * (hi - cen))
            st, s, beta = closed_lp(Em, Ep, Om, Op, n, closed_grid(x))
            rec = {"n": n, "it": it, "x": x.tolist(), "lead": [llo, lhi], "status": st,
                   "s": s, "shrunk_stable": shrunk_ok, "lo": lo.tolist(), "hi": hi.tolist(),
                   "beta": None if beta is None else beta.tolist()}
            fh.write(json.dumps(rec) + "\n")
            key = -np.inf if st != 0 else s
            if worst is None or key < worst[0]:
                worst = (key, it, st, s, shrunk_ok)
    print(json.dumps({"n": n, "trials": trials, "accepted": acc, "worst": worst}))


if __name__ == "__main__":
    main()

"""Random search over NON-monic stable interval boxes (leading coefficient also uncertain).

Usage: python search_nonmonic.py N COUNT SEED OUT.jsonl [WORKERS]
Exploratory.  For a fixed numerator, the vertex reduction (Kharitonov rectangle) holds for
any box whose leading-coefficient interval excludes 0, so delta* from margin.py applies
unchanged (it uses a homogeneous numerator, not a monic one).
"""
from __future__ import annotations

import json
import sys
from multiprocessing import Pool

import numpy as np

from margin import delta_star
from search_random import random_center
from sprlib import box_is_stable, scaled_box, stability_radius


def one(args):
    n, seed = args
    rng = np.random.default_rng(seed)
    c = random_center(n, rng)
    p = rng.uniform(0.3, 1.0)
    wl = np.abs(c) * rng.random(n + 1) * (rng.random(n + 1) < p)
    wh = np.abs(c) * rng.random(n + 1) * (rng.random(n + 1) < p)
    # leading coefficient always uncertain here (the variant under test)
    wl[n] = rng.uniform(0.05, 0.95)
    wh[n] = rng.uniform(0.05, 3.0)
    lam = stability_radius(c, wl, wh)
    if not np.isfinite(lam) or lam <= 0:
        return None
    lam = min(lam, 0.999 / wl[n])  # keep the leading interval positive
    eps = 10 ** rng.uniform(-4, -0.5)
    lo, hi = scaled_box(c, wl, wh, lam * (1 - eps))
    if lo[n] <= 0 or not box_is_stable(lo, hi):
        return None
    # frequency normalization (s -> w0 s) and overall scaling by 1/c_n(center)
    k = np.arange(n + 1)
    cn = 0.5 * (lo[n] + hi[n])
    c0 = 0.5 * (lo[0] + hi[0])
    w0 = (c0 / cn) ** (1.0 / n)
    f = w0 ** k / (cn * w0 ** n)
    lo, hi = lo * f, hi * f
    d, dw = delta_star(lo, hi, tol=1e-3)
    return {"n": n, "seed": seed, "eps": eps, "delta": d, "dwin": dw,
            "lead_ratio": float(lo[n] / hi[n]), "lo": lo.tolist(), "hi": hi.tolist()}


def main():
    n, count, seed0, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    workers = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    best = None
    ninf = 0
    with Pool(workers) as pool, open(out, "w") as fh:
        for r in pool.imap_unordered(one, [(n, seed0 + i) for i in range(count)], chunksize=4):
            if r is None:
                continue
            fh.write(json.dumps(r) + "\n")
            ninf += r["delta"] < 0
            if best is None or r["delta"] < best["delta"]:
                best = r
    print(json.dumps({"n": n, "count": count, "grid_infeasible": int(ninf),
                      "min_delta": best and best["delta"], "seed": best and best["seed"],
                      "lead_ratio": best and best["lead_ratio"]}))


if __name__ == "__main__":
    main()

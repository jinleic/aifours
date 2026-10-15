"""Random exploratory search for hard (low rho) stable monic interval boxes.

Usage: python search_random.py N COUNT SEED OUT.jsonl [WORKERS]
Each sample: random Hurwitz center, random relative widths, scaled to (1-eps) times the
stability radius; records delta*, delta_win, rho = delta*/delta_win on the default grid.
Exploratory only (no certification).
"""
from __future__ import annotations

import json
import sys
from multiprocessing import Pool

import numpy as np

from margin import delta_star
from sprlib import normalize_frequency, scaled_box, stability_radius


def random_center(n, rng):
    roots = []
    while len(roots) < n:
        if n - len(roots) >= 2 and rng.random() < 0.7:
            w = 10 ** rng.uniform(-1.5, 1.5)
            z = 10 ** rng.uniform(-2.5, 0) if rng.random() < 0.7 else rng.uniform(0.05, 0.95)
            z = min(z, 0.99)
            re, im = -z * w, w * np.sqrt(1 - z * z)
            roots += [complex(re, im), complex(re, -im)]
        else:
            roots.append(complex(-(10 ** rng.uniform(-1.5, 1.5)), 0))
    c = np.real(np.poly(roots))[::-1]  # ascending, monic
    return c / c[-1]


def random_widths(n, c, rng):
    p = rng.uniform(0.3, 1.0)
    wl = np.abs(c) * rng.random(n + 1) * (rng.random(n + 1) < p)
    wh = np.abs(c) * rng.random(n + 1) * (rng.random(n + 1) < p)
    wl[n] = wh[n] = 0.0
    if wl.sum() + wh.sum() == 0:
        wl[0] = abs(c[0])
    return wl, wh


def one(args):
    n, seed = args
    rng = np.random.default_rng(seed)
    c = random_center(n, rng)
    wl, wh = random_widths(n, c, rng)
    lam = stability_radius(c, wl, wh)
    if not np.isfinite(lam) or lam <= 0:
        return None
    eps = 10 ** rng.uniform(-4, -0.5)
    lo, hi = scaled_box(c, wl, wh, lam * (1 - eps))
    lo, hi, _ = normalize_frequency(lo, hi)
    try:
        d, dw = delta_star(lo, hi, tol=1e-3)
    except Exception as e:  # pragma: no cover
        return {"seed": seed, "error": repr(e)}
    return {"n": n, "seed": seed, "eps": eps, "delta": d, "dwin": dw,
            "rho": d / dw if dw > 0 else None, "lo": lo.tolist(), "hi": hi.tolist()}


def main():
    n, count, seed0, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    workers = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    tasks = [(n, seed0 + i) for i in range(count)]
    best = None
    with Pool(workers) as pool, open(out, "w") as fh:
        for r in pool.imap_unordered(one, tasks, chunksize=4):
            if r is None:
                continue
            fh.write(json.dumps(r) + "\n")
            if r.get("rho") is not None and (best is None or r["rho"] < best["rho"]):
                best = r
    print(json.dumps({"n": n, "count": count, "best_rho": best and best["rho"],
                      "best_seed": best and best["seed"], "best_delta": best and best["delta"],
                      "best_dwin": best and best["dwin"]}))


if __name__ == "__main__":
    main()

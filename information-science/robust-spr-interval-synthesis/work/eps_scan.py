"""Scan rho(eps) toward the stability boundary for one random-search sample (exploratory).

Usage: python eps_scan.py N SEED
Reconstructs the sample of search_random.one(N, SEED) and evaluates delta*, delta_win at
lam = (1 - eps) * lam_stab for eps = 1e-1 ... 1e-6, with a refined grid.
"""
import sys

import numpy as np

from margin import default_grid, delta_star
from search_random import random_center, random_widths
from sprlib import normalize_frequency, scaled_box, stability_radius


def sample(n, seed):
    rng = np.random.default_rng(seed)
    c = random_center(n, rng)
    wl, wh = random_widths(n, c, rng)
    return c, wl, wh


def main():
    n, seed = int(sys.argv[1]), int(sys.argv[2])
    c, wl, wh = sample(n, seed)
    lam = stability_radius(c, wl, wh, iters=80)
    for eps in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 1e-5, 1e-6]:
        lo, hi = scaled_box(c, wl, wh, lam * (1 - eps))
        lo, hi, _ = normalize_frequency(lo, hi)
        g = default_grid(lo, hi, npts=4000, lo_exp=-8, hi_exp=8)
        d, dw = delta_star(lo, hi, grid=g, tol=1e-4)
        print(f"eps={eps:.0e} delta*={d:.3e} dwin={dw:.3e} rho={d / dw:.4f}", flush=True)


if __name__ == "__main__":
    main()

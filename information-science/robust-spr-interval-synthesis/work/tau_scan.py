"""Scan the Re-margin tau*(eps) = max_{beta monic} min_{t,c} Re(beta/K_c) toward the boundary.

Usage: python tau_scan.py N SEED   (sample of search_random.one(N, SEED)); exploratory.
tau* > 0 iff a common SPR numerator exists (tau* <= 1 because Re -> 1 at infinity).
"""
import sys

import numpy as np

from eps_scan import sample
from sprlib import normalize_frequency, scaled_box, stability_radius, synthesis_margin


def main():
    n, seed = int(sys.argv[1]), int(sys.argv[2])
    c, wl, wh = sample(n, seed)
    lam = stability_radius(c, wl, wh, iters=80)
    for eps in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        lo, hi = scaled_box(c, wl, wh, lam * (1 - eps))
        lo, hi, _ = normalize_frequency(lo, hi)
        tau, tt, beta, info = synthesis_margin(lo, hi, max_iter=60)
        print(f"eps={eps:.0e} tau_grid={tau:.4e} tau_true={tt:.4e} iters={len(info['hist'])}",
              flush=True)


if __name__ == "__main__":
    main()

"""Exact verification of a candidate monic interval box (rational endpoints):
  * Kharitonov endpoint components E-, E+, O-, O+ built exactly from lo, hi;
  * widths have nonnegative t-coefficients by construction (checked);
  * robust stability: exact Routh test of the four Kharitonov corners AND certified strict
    band separation (zero exclusion);
  * no common SPR numerator: exact positive dependence sum mu_k F(c_k,t_k) (+ mu_inf e_n) = 0
    from strict_exact.certify (support from a float LP dual on an adaptive grid).
Input JSON: {"n":..., "lo":[...], "hi":[...]} (floats or rational strings, s^0..s^(n-1)).

Usage: python box_exact.py IN.json OUT.json [denominator_limit]
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction

import flint
import numpy as np

from closed_exact import fq
from strict_exact import certify


def kharitonov_exact(lo, hi, n):
    lo1 = list(lo) + [flint.fmpq(1)]
    hi1 = list(hi) + [flint.fmpq(1)]
    Em, Ep, Om, Op = [], [], [], []
    for k in range(n + 1):
        l = k // 2
        s = 1 if l % 2 == 0 else -1
        a, b = s * lo1[k], s * hi1[k]
        mn, mx = (a, b) if a <= b else (b, a)
        if k % 2 == 0:
            Em.append(mn); Ep.append(mx)
        else:
            Om.append(mn); Op.append(mx)
    return (flint.fmpq_poly(Em), flint.fmpq_poly(Ep), flint.fmpq_poly(Om), flint.fmpq_poly(Op))


def main():
    spec = json.load(open(sys.argv[1]))
    lim = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 9
    n = spec['n']
    conv = (lambda v: fq(v) if isinstance(v, str) else fq(Fraction(v).limit_denominator(lim)))
    lo = [conv(v) for v in spec['lo']]
    hi = [conv(v) for v in spec['hi']]
    Em, Ep, Om, Op = kharitonov_exact(lo, hi, n)
    # adaptive grid around corner resonances
    from advbox import adaptive_grid
    lof = np.array([float(v) for v in lo]); hif = np.array([float(v) for v in hi])
    grid = adaptive_grid(lof, hif, base=3000)
    out = certify(n, Em, Ep, Om, Op, grid=grid, tscale=(float(grid[1]), float(grid[-1])))
    out['lo'] = [str(v) for v in lo]; out['hi'] = [str(v) for v in hi]
    out['n'] = n
    json.dump(out, open(sys.argv[2], 'w'), indent=1)
    keys = ['WE_coeffwise_nonneg', 'WO_coeffwise_nonneg', 'corners_routh',
            'bands_strictly_disjoint_alternating', 'band_kinds', 'float_dual_residual',
            'support', 'nullspace_dim', 'strict_infeasible_certified']
    print(json.dumps({k: out[k] for k in keys}, indent=1))


if __name__ == '__main__':
    main()

"""Parent-independent exact-rational enclosure of C8 (no FLINT, SymPy, NumPy or worker imports).
Uses log z=2atanh((z-1)/(z+1)), a geometric tail bound, positive exponential Taylor bounds,
and integer square-root brackets. All displayed decimal bounds are rounded outward as rational numbers.
Also checks moment/local-count constants from the written proof. Refuses to overwrite its receipt.
Usage: python3 -B chi8_parent_rational_check.py OUT.json
"""
from datetime import datetime
from fractions import Fraction as Q
import hashlib
import json
from math import factorial, isqrt
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


def log_bounds(z, n=80):
    x = Q(z - 1, z + 1)
    lo = 2 * sum((x ** (2 * i + 1) / (2 * i + 1) for i in range(n)), Q(0))
    tail = 2 * x ** (2 * n + 1) / ((2 * n + 1) * (1 - x * x))
    return lo, lo + tail


def exp_bounds(lo, hi, n=48):
    lower = sum((lo ** i / factorial(i) for i in range(n + 1)), Q(0))
    upper = sum((hi ** i / factorial(i) for i in range(n + 1)), Q(0))
    ratio = hi / (n + 2)
    if not 0 <= ratio < 1:
        raise ValueError('exponential remainder bound not applicable')
    upper += (hi ** (n + 1) / factorial(n + 1)) / (1 - ratio)
    return lower, upper


def outward(lo, hi, digits=20):
    scale = 10 ** digits
    low_integer = lo.numerator * scale // lo.denominator
    high_integer = -((-hi.numerator * scale) // hi.denominator)
    return {'lower_numerator': low_integer, 'upper_numerator': high_integer, 'denominator': scale,
            'strict_lower': str(Q(low_integer, scale)), 'strict_upper': str(Q(high_integer, scale))}


def main():
    l3, u3 = log_bounds(3)
    l7, u7 = log_bounds(7)
    elo, ehi = exp_bounds(l3 * l7, u3 * u7)
    delta_lo, delta_hi = 1 / ehi - Q(1, 9), 1 / elo - Q(1, 9)
    scale = 10 ** 30
    root = isqrt(2 * scale * scale)
    sqrt_lo, sqrt_hi = Q(root, scale), Q(root + 1, scale)
    c_lo = Q(49, 32) * sqrt_lo * delta_lo
    c_hi = Q(49, 32) * sqrt_hi * delta_hi
    decay = Q(18 * 49, 256)
    out = {
        'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds'),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'method': {'atanh_terms': 80, 'exp_degree': 48, 'sqrt_scale': str(scale),
                   'log_tail': '2*x^(2N+1)/((2N+1)*(1-x*x))',
                   'exp_tail': 'term_(N+1)/(1-hi/(N+2))'},
        'log3': outward(l3, u3), 'log7': outward(l7, u7),
        'a_squared_minus_1_over_9': outward(delta_lo, delta_hi), 'C8': outward(c_lo, c_hi),
        'checks': {
            'sqrt_bracket': sqrt_lo * sqrt_lo < 2 < sqrt_hi * sqrt_hi,
            'log7_upper_below_2': u7 < 2,
            'delta_lower_positive': delta_lo > 0,
            'C8_inside_0.0147_0.0148': Q(147, 10000) < c_lo < c_hi < Q(148, 10000),
            'row_variance_factor_441_over_128': decay == Q(441, 128),
            'H1': 4 * 4 - 2 * 4 - 8 + 2 == 2,
            'series_ratio_7_over_9_lt_1': Q(7, 9) < 1,
            'EY_growth_81_over_64_gt_1': 4 * Q(3, 4) ** 4 == Q(81, 64) > 1,
            'Molloy_Reed_16_over_27_lt_1': 3 * Q(2, 3) ** 4 == Q(16, 27) < 1,
            'Gaussian_tail_polynomial_degree_199_over_2': 8 + Q(145, 2) + 16 + 3 == Q(199, 2),
            'residue_preimages': [factorial(8 * r) // factorial(8) ** r for r in (1, 2, 3)] == [1, 12870, 9465511770]
        },
        'scope': 'Independent rational constant/count arithmetic; does not by itself prove the universal matrix inequality or the probabilistic transfer.'
    }
    out['status'] = 'PASS' if all(out['checks'].values()) else 'FAIL'
    with open(sys.argv[1], 'x') as f:
        json.dump(out, f, indent=2)
        f.write('\n')
    print(json.dumps(out, indent=1))
    return 0 if out['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())

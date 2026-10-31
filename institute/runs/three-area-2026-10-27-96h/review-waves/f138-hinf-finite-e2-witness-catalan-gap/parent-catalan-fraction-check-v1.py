#!/usr/bin/env python3
"""Exact rational arithmetic for the finite Brownian stopping witness.

This checks the Catalan/pi enclosure, coefficient and preview-window bounds;
it does not prove the Brownian exit-time identity or SDE admissibility.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def arctan_bounds(x, n):
    require(0 < x < 1 and n > 0 and n % 2 == 0, 'BAD_ARCTAN_INPUT')
    lower = sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1) for k in range(n)), F(0))
    upper = lower + x ** (2 * n + 1) / (2 * n + 1)
    return lower, upper


def catalan_bounds(n):
    require(n > 0 and n % 2 == 0, 'BAD_CATALAN_INPUT')
    lower = sum((F((-1) ** k, (2 * k + 1) ** 2) for k in range(n)), F(0))
    upper = lower + F(1, (2 * n + 1) ** 2)
    return lower, upper


def main():
    require(len(sys.argv) == 2, 'EXPECTED_NEW_OUTPUT_PATH')
    start = clock()
    alo, ahi = arctan_bounds(F(1, 5), 40)
    blo, bhi = arctan_bounds(F(1, 239), 40)
    pi_lo, pi_hi = 16 * alo - 4 * bhi, 16 * ahi - 4 * blo
    g_lo, g_hi = catalan_bounds(400)
    require(3 < pi_lo < pi_hi < 4 and 0 < g_lo < g_hi < 1, 'INVALID_INTERVALS')
    m2_lo = 32 * g_lo * g_lo / (pi_hi ** 3)
    m2_hi = 32 * g_hi * g_hi / (pi_lo ** 3)
    require(m2_lo > F(9305, 10000) ** 2, 'LOWER_HALF_MOMENT')
    require(m2_hi < F(9306, 10000) ** 2, 'UPPER_HALF_MOMENT')
    wrong_factor = 16 * g_hi * g_hi / pi_lo ** 3
    require(wrong_factor < F(9305, 10000) ** 2, 'WRONG_FACTOR_NOT_DETECTED')
    product = F(8191, 8192) * F(4095, 4096) * F(10000, 9306)
    require(product == F(2329315625, 2168455168) and product > F(107, 100), 'RATIONAL_GAP')
    old = F(8191, 8192) * F(4095, 4096) * F(1944, 1943)
    require(old == F(8150741235, 8149532672) and old > 1, 'PREDECESSOR_GAP')
    cases = []
    for t, h in ((F(1), F(0)), (F(1), F(99999, 100000)), (F(3, 2), F(1)), (F(10), F(9)), (F(1), F(4095, 4096))):
        delta = min((t - h) / 2, t / 8192)
        require(0 < delta <= (t - h) / 2 and delta <= t / 8192, 'PREVIEW_SUPPORT')
        cases.append({'T': str(t), 'h': str(h), 'delta': str(delta)})
    require(F(1, 2) > F(1, 4), 'WRONG_DELTA_CONTROL')
    result = {
        'kind': 'PARENT_EXACT_CATALAN_FINITE_STOPPING_ARITHMETIC',
        'started_native_clock': start,
        'observed_native_clock_after_checks': clock(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'pi_bounds_method': 'Machin identity with rational alternating arctangent bounds',
        'catalan_bounds_method': '400-term alternating sum and next-term bracket',
        'half_moment_square_lower_above_9305_over_10000_squared': True,
        'half_moment_square_upper_below_9306_over_10000_squared': True,
        'gap_factor': str(product),
        'gap_exceeds_107_over_100': True,
        'predecessor_factor': str(old),
        'preview_samples': cases,
        'negative_controls': ['incorrect_half_moment_factor_rejected', 'delta_T_over_2_exceeds_support_for_h_3T_over_4'],
        'limits': 'Exact arithmetic and five preview parameter checks only. Brownian exit-time series, admissibility and Itô steps remain written mathematics; no true gain, RMS gap, synthesis, novelty or formal verification.',
    }
    with Path(sys.argv[1]).open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Independent exact controls for the fixed-lambda privacy candidate.

Uses a diamond-core shell, not the candidate's optimal cost-body shell.  The
all-shift argument and asymptotic theorem remain written-math obligations.
"""
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-peak-floor-low-privacy-universal-v1.md')
EXPECTED = 'd44029e458b8af871d2d849e2a5159e1885e99402d615a88eabe39d89ab4ad43'
OUT = HERE / 'parent-shell-control-result-v1.json'


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          capture_output=True, text=True, check=True).stdout.strip()


def simplex(a, b):
    return F(math.factorial(a) * math.factorial(b), math.factorial(a + b + 2))


def power_sums(b):
    d = 1 - b
    return (1 / d, b / d**2, b * (1 + b) / d**3,
            b * (1 + 4*b + b*b) / d**4,
            b * (1 + 11*b + 11*b*b + b**3) / d**5)


def shell_moment(degree, q, sums):
    return sum(F(math.comb(degree, j)) * q**(degree-j) * sums[j]
               for j in range(degree + 1))


def layer_index(point, q):
    distance = abs(point[0]) + abs(point[1]) - q
    if distance <= 0:
        return 0
    return (distance.numerator + distance.denominator - 1) // distance.denominator


def main():
    started = clock()
    digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    if digest != EXPECTED:
        raise ValueError('SOURCE_HASH_MISMATCH')
    if OUT.exists():
        raise FileExistsError(OUT)

    area = 4 * simplex(0, 0)
    l2_squared = 4 * (simplex(2, 0) + simplex(0, 2))
    l1_squared = 4 * (simplex(2, 0) + 2*simplex(1, 1) + simplex(0, 2))
    l1 = 4 * (simplex(1, 0) + simplex(0, 1))
    if (area, l2_squared, l1_squared, l1) != (2, F(2, 3), 1, F(4, 3)):
        raise AssertionError('DIAMOND_INTEGRALS')

    cases = []
    for b, q in ((F(1, 16), F(1, 2)), (F(1, 256), F(1, 4)),
                 (F(1, 81), F(1, 3))):
        sums = power_sums(b)
        w2 = shell_moment(2, q, sums)
        w4 = shell_moment(4, q, sums)
        normalizer = 2 * (1 - b) * w2
        x = b / normalizer
        # For c=||x||_2^2, the diamond integral is 2/3 and the cost
        # sublevel area is pi. Since pi>3, the A=3 expression is an
        # upper bound on the displayed peak-floor expression at this x.
        actual_cost = F(1, 3) * w4 / w2
        floor_bound_area_three = F(2, 3)*x + b*(1-2*x)**2/(6*x)
        if not (0 < x <= F(1, 2) and actual_cost >= floor_bound_area_three):
            raise AssertionError('NORMALIZER_OR_PEAK_BOUND')
        cases.append({'b': str(b), 'core_radius': str(q),
                      'normalizer': str(normalizer), 'b_times_density_cap': str(x),
                      'l2_squared_cost': str(actual_cost),
                      'gap_above_area_three_floor': str(actual_cost - floor_bound_area_three)})

    grid = [F(i, 2) for i in range(-4, 5)]
    shifts = [(F(i, 2), F(j, 2)) for i in range(-2, 3) for j in range(-2, 3)
              if abs(i) + abs(j) <= 2]
    checked = 0
    for q in (F(1, 2), F(1, 4)):
        for x, y in itertools.product(grid, repeat=2):
            k = layer_index((x, y), q)
            for dx, dy in shifts:
                k2 = layer_index((x + dx, y + dy), q)
                if abs(k - k2) > 1:
                    raise AssertionError('SHELL_SHIFT_CONTROL')
                checked += 1
    # Doubling the layer exponent would violate privacy on this boundary.
    q = F(1, 2)
    before = layer_index((q, F(0)), q)
    after = layer_index((q + 1, F(0)), q)
    if (before, after) != (0, 1) or abs(2*after - 2*before) <= 1:
        raise AssertionError('BAD_LAYER_MUTATION_NOT_CAUGHT')

    result = {
        'kind': 'PARENT_EXACT_PRIVACY_SHELL_CONTROL',
        'started_native_clock': started,
        'finished_native_clock': clock(),
        'candidate_sha256': digest,
        'diamond_integrals': {'area': str(area), 'l2_squared': str(l2_squared),
                              'l1_squared': str(l1_squared), 'l1': str(l1)},
        'cases': cases,
        'bounded_shift_control': {'two_core_radii': True, 'point_shift_pairs': checked,
                                  'all_index_differences_at_most_one': True},
        'negative_control': {'doubled_layer_exponent': 'rejected at exact unit shift'},
        'limits': 'The shift grid is diagnostic, not a proof of all-event privacy. '
                  'The diamond-core costs are upper-bound examples, not optimality '
                  'or a proof of the all-law peak-floor theorem. No priority, human, '
                  'formal or independent-model-family review is implied.',
    }
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()

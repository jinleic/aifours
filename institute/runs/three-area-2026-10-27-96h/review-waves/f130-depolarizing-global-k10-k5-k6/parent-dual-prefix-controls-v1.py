#!/usr/bin/env python3
"""Exact parent controls for four-qubit depolarizing prefix arguments.

Nonblind separate rational checks of spectral constants, actual projectors,
spin-flip dual positivity and the reference polynomial identity. They are
not a universal matrix-inequality proof.
"""
from fractions import Fraction as F
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def require(x, reason):
    if not x:
        raise ValueError(reason)


def psd(matrix):
    a = [row[:] for row in matrix]
    pivots = []
    for k in range(16):
        p = a[k][k]
        if p < 0 or (p == 0 and any(a[j][k] != 0 for j in range(k + 1, 16))):
            return False, pivots + [str(p)]
        pivots.append(str(p))
        if p:
            for i in range(k + 1, 16):
                for j in range(k + 1, 16):
                    a[i][j] -= a[i][k] * a[k][j] / p
    return True, pivots


def build_projector(rank):
    q = [[F(0) for _ in range(16)] for _ in range(16)]
    v = [F(0)] * 16
    v[0], v[15] = F(12, 13), F(5, 13)
    for i in range(16):
        for j in range(16):
            q[i][j] = v[i] * v[j]
    basis = [i for i in range(16) if i.bit_count() == 1]
    basis += [i for i in range(16) if i.bit_count() == 2][:rank - 5]
    for i in basis:
        q[i][i] += 1
    require(sum(q[i][i] for i in range(16)) == rank, 'PROJECTOR_TRACE')
    require(all(sum(q[i][k] * q[k][j] for k in range(16)) == q[i][j] for i in range(16) for j in range(16)), 'PROJECTOR_SQUARE')
    return q


def one_site_marginals(q):
    result = []
    for bit in range(4):
        site = [[F(0), F(0)], [F(0), F(0)]]
        for i in range(16):
            for j in range(16):
                if (i & ~(1 << bit)) == (j & ~(1 << bit)):
                    site[(i >> bit) & 1][(j >> bit) & 1] += q[i][j]
        result.append(site)
    return result


def dual_matrix(q, rank):
    sites = one_site_marginals(q)
    h1 = [[F(0) for _ in range(16)] for _ in range(16)]
    for bit, site in enumerate(sites):
        for i in range(16):
            for j in range(16):
                if (i & ~(1 << bit)) == (j & ~(1 << bit)):
                    h1[i][j] += site[(i >> bit) & 1][(j >> bit) & 1]
    out = [[h1[i][j] + (-1) ** (i.bit_count() + j.bit_count()) * q[15 - j][15 - i] - (2 * rank - 5 if i == j else 0) for j in range(16)] for i in range(16)]
    return out


def main():
    require(len(sys.argv) == 2, 'EXPECTED_NEW_OUTPUT_PATH')
    start = clock()
    z4 = sorted((4 - 2 * i.bit_count() for i in range(16)), reverse=True)
    z3 = sorted((3 - 2 * (i & 7).bit_count() for i in range(16)), reverse=True)
    count = sorted(i.bit_count() for i in range(16))
    table, actual = [], []
    for r in (5, 6, 10, 11):
        require(sum(z4[:r]) == 12 and sum(z3[:r]) <= 10, 'SPECTRAL_CONSTANT')
        require(sum(count[:r]) == 2 * r - 6, 'H1_BOTTOM_CONSTANT')
        table.append({'rank': r, 'top_Z4': sum(z4[:r]), 'top_Z3': sum(z3[:r]), 'bottom_occupancy': sum(count[:r])})
        q = build_projector(r)
        ok, pivots = psd(dual_matrix(q, r))
        require(ok, 'DUAL_PROJECTOR_SAMPLE')
        actual.append({'rank': r, 'PSD': ok, 'exact_LDL_pivots': pivots})
    require([sum(z3[:r]) for r in (7, 8, 9)] == [11, 12, 11], 'EXCLUDED_RANK_CONTROL')
    scalar = 0
    for c in (F(0), F(1, 3), F(1, 2), F(1)):
        for q in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            # Squared off-diagonal avoids introducing an irrational square root.
            det = (1 + c - 2 * c * q) * c * (2 * q - 1) - 4 * c * c * q * (1 - q)
            require(det == c * (2 * q - 1 - c), 'TWO_BY_TWO_DETERMINANT')
            scalar += 1
    for r in (5, 6, 10, 11):
        for p in (F(0), F(2, 5), F(2, 3), F(1)):
            t, b = 1 - p, p / 2
            a = t + b
            value = r * b ** 4 + (2 * r - 6) * t * b ** 3 + (r - 5) * t * t * b * b
            require(value == b ** 4 + 4 * a * b ** 3 + (r - 5) * a * a * b * b, 'REFERENCE_IDENTITY')
    c, q = F(3, 4), F(3, 4)
    require(c * (2 * q - 1 - c) < 0, 'PROJECTOR_THRESHOLD_MUTATION')
    product = [[F(0) for _ in range(16)] for _ in range(16)]
    for i in (0, 1, 2, 4, 8, 3):
        product[i][i] = 1
    tight = dual_matrix(product, 6)
    require(psd(tight)[0], 'TIGHT_POSITIVE')
    wrong = [row[:] for row in tight]
    for i in range(16):
        wrong[i][i] -= F(1, 1000)
    require(not psd(wrong)[0], 'FALSE_STRICT_THRESHOLD')
    result = {'kind': 'PARENT_EXACT_DEPOLARIZING_PREFIX_CONTROLS', 'started_native_clock': start,
              'observed_native_clock_after_checks': clock(), 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'spectral_table': table, 'actual_projectors': actual, 'two_by_two_identity_cases': scalar,
              'all_reference_polynomial_cases': 16, 'negative_controls': ['ranks_7_8_9_do_not_have_three_site_bound_10', 'too_weak_projector_occupancy_gives_negative_determinant', 'threshold_increased_by_1_over_1000_rejected'],
              'limits': 'Exact finite matrices/scalar identities only; the universal inequalities, local covariance, channel mirror and full physical caller require the separately written proof. No k3, full majorization, novelty or formal proof.'}
    with Path(sys.argv[1]).open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()

#!/usr/bin/python3
"""Parent exact arithmetic supporting the BTD(14,18) written proof; no worker-code imports.
Not a proof of nonexistence by itself. Checks actual 14x14 inverse/determinant arithmetic, the H-polynomial
coefficients, complete scalar value sets and row counts, and the six mixed 4x4 determinants.
Usage: python3 -B btd14-18-parent-arithmetic-v1.py NEW-RECEIPT.json. Refuses overwrite.
"""
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys
from fractions import Fraction as F


def det(rows):
    a = [[F(x) for x in row] for row in rows]
    d = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            d = -d
        v = a[i][i]
        d *= v
        for j in range(i + 1, len(a)):
            q = a[j][i] / v
            for k in range(i + 1, len(a)):
                a[j][k] -= q * a[i][k]
    return d


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit('refusing to overwrite receipt')
    n = 14
    A = [[7 * (i == j) + 4 for j in range(n)] for i in range(n)]
    inv = [[(F(i == j) - F(4, 63)) / 7 for j in range(n)] for i in range(n)]
    product = [[sum(A[i][k] * inv[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    determinant = det(A)
    checks = {
        'A_inverse': all(product[i][j] == (i == j) for i in range(n) for j in range(n)),
        'A_determinant': determinant == 9 * 7**14,
        'D4_factor': determinant / 63**4 == F(7**10, 729),
        # H=63I-9G+28J, G^2=7G+196J, GJ=63J, J^2=18J.
        'H2_I': 63**2 == 63 * 63,
        'H2_G': 2 * 63 * -9 + (-9)**2 * 7 == 63 * -9,
        'H2_J': (-9)**2 * 196 + 2 * 63 * 28 + 2 * -9 * 28 * 63 + 28**2 * 18 == 63 * 28,
        'H_one': 63 - 9 * 63 + 28 * 18 == 0,
        'column_type_boundary': 28 - 18 >= 0 and 28 - 36 < 0,
        'total_twos_and_columns': (14, 18 - 14) == (14, 4),
    }
    values = [h for h in range(-math.isqrt(280), math.isqrt(280) + 1) if (h - 1) % 9 == 0]
    checks['complete_entry_set'] = values == [-8, 1, 10]
    checks['count_polynomials'] = all((h - 1) * (h + 8) == 162 * (h == 10)
                                      and (h - 1) * (h - 10) == 162 * (h == -8) for h in values)
    counts = ((530 + 7 * -10 - 8 * 17) // 162, (530 - 11 * -10 + 10 * 17) // 162)
    checks['row_counts'] = counts == (2, 5) and 2 * 10 + 5 * -8 + 10 == -10
    # PSD for y=2e_a+e_k+e_l gives 2h-4>=0, forcing h=10 (Lemma F).
    checks['lemma_F'] = [h for h in values if 2 * h - 4 >= 0] == [10]
    allowed_type1 = [(x, y) for x, y in itertools.product(values, repeat=2)
                     if (x != 10 or y == -8) and (y != 10 or x == -8)
                     and (x != -8 or y == 10) and (y != -8 or x == 10)]
    checks['type1_sum'] = all(x + y == 2 for x, y in allowed_type1)
    checks['u_pigeonhole'] = 14 > 2 * (2 + 1)
    sums = sorted({x + y for x, y in itertools.product(values, repeat=2) if (x + y)**2 <= 112})
    checks['complete_type0_sums'] = sums == [-7, 2]
    minors = []
    for x, y in [(-8, 1), (1, -8)]:
        for w in values:
            D = det([[10, -8, 1, x], [-8, 10, 1, y], [1, 1, 10, w], [x, y, w, 28]])
            minors.append({'x': x, 'y': y, 'w': w, 'det': int(D)})
            checks['minor_%s_%s_%s' % (x, y, w)] = D == (3645 if w != 10 else -2187)
    checks['negative_minor_excluded'] = 7**10 * -2187 < 0
    checks['positive_minor_excluded_mod3'] = F(7**10 * 3645, 729) == 5 * 7**10 and (5 * 7**10) % 3 == 2
    checks['squares_mod3'] = {r*r % 3 for r in range(3)} == {0, 1}
    checks['final_sum'] = 18 * 2 == 36 != 0
    # Positive arithmetic control: the D4 relation is not intrinsically inconsistent.
    checks['D4_positive_control'] = 729 * (7**5)**2 == 7**10 * 729
    record = {'recorded_at_pt': subprocess.check_output(['date', '+%Y-%m-%d %H:%M:%S %Z'], text=True).strip(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'A_determinant': int(determinant), 'D4_factor': str(determinant / 63**4),
              'entry_values': values, 'row_counts_10_minus8': counts, 'type1_pairs': allowed_type1,
              'type0_sums': sums, 'mixed_minors': minors, 'checks': checks,
              'all_ok': all(checks.values()),
              'scope': 'Exact arithmetic supporting the written proof, not universal matrix verification or a kernel proof.'}
    with out.open('x') as f:
        json.dump(record, f, indent=2)
        f.write('\n')
    print(json.dumps({'all_ok': record['all_ok'], 'checks': len(checks), 'receipt': str(out)}))
    return 0 if record['all_ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())

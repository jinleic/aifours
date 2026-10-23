"""Parent exact check of qutrit dual/T-dual tangent rigidity; imports no worker code.
Constructs real Jacobians directly from U U†=I after the specified entry permutations.
Nonzero exact minors plus an exactly annihilated tangent basis certify matching dimensions.
"""
from datetime import datetime
import hashlib
from itertools import combinations, product
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo
from flint import fmpz_mat

PRIME = 1000000007


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def coordinates(d, r, c, cut):
    i, a = divmod(r, d)
    j, b = divmod(c, d)
    if cut == 'U':
        return r, c
    if cut == 'R':
        return d * i + j, d * a + b
    if cut == 'Gamma':
        return d * i + b, d * j + a
    raise ValueError(cut)


def jacobian(d, permutation, cuts):
    n = d * d
    pairs = list(combinations(range(n), 2))
    positions = {p: n + 2 * k for k, p in enumerate(pairs)}
    rows = [[0] * (2 * n * n) for _ in range(len(cuts) * n * n)]
    for which, cut in enumerate(cuts):
        base = [None] * n
        for c, r in enumerate(permutation):
            rr, cc = coordinates(d, r, c, cut)
            if base[cc] is not None:
                raise ValueError('base reshape is not a permutation')
            base[cc] = rr
        if sorted(base) != list(range(n)):
            raise ValueError('base reshape is not unitary')
        offset = which * n * n
        for r, c in product(range(n), repeat=2):
            rr, cc = coordinates(d, r, c, cut)
            t = base[cc]
            real_col = r * n + c
            imaginary_col = n * n + real_col
            # d(QQ†)[E_rc] has entries at (rr,t) and (t,rr).
            if rr == t:
                rows[offset + rr][real_col] = 2
            else:
                first, second = sorted((rr, t))
                row = offset + positions[(first, second)]
                rows[row][real_col] = 1
                rows[row + 1][imaginary_col] = 1 if rr < t else -1
    return rows


def tangent(d, permutation):
    n = d * d
    basis = []
    for a in range(d):
        basis.append([(a, a, 0, 1)])
    for a, b in combinations(range(d), 2):
        basis.append([(a, b, 1, 0), (b, a, -1, 0)])
        basis.append([(a, b, 0, 1), (b, a, 0, 1)])
    columns = []
    for factor in range(4):
        for generator in basis:
            vec = [0] * (2 * n * n)
            for col, row in enumerate(permutation):
                i, a = divmod(row, d)
                j, b = divmod(col, d)
                old = (i, a, j, b)[factor]
                for x, y, re, im in generator:
                    if factor < 2 and y == old:
                        rr = x * d + a if factor == 0 else i * d + x
                        pos = rr * n + col
                    elif factor >= 2 and x == old:
                        cc = y * d + b if factor == 2 else j * d + y
                        pos = row * n + cc
                    else:
                        continue
                    vec[pos] += re
                    vec[n * n + pos] += im
            columns.append(vec)
    return [list(row) for row in zip(*columns)]


def pivot_minor(rows):
    """Modular pivot search selects a square submatrix; its determinant is then exact over Z."""
    a = [[v % PRIME for v in row] for row in rows]
    labels = list(range(len(a)))
    pivot_rows, pivot_cols = [], []
    k = 0
    for c in range(len(a[0])):
        found = next((i for i in range(k, len(a)) if a[i][c]), None)
        if found is None:
            continue
        a[k], a[found] = a[found], a[k]
        labels[k], labels[found] = labels[found], labels[k]
        pivot_rows.append(labels[k])
        pivot_cols.append(c)
        inv = pow(a[k][c], PRIME - 2, PRIME)
        a[k] = [(v * inv) % PRIME for v in a[k]]
        for i in range(k + 1, len(a)):
            if a[i][c]:
                f = a[i][c]
                a[i] = [(x - f * y) % PRIME for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    minor = fmpz_mat([[rows[r][c] for c in pivot_cols] for r in pivot_rows])
    det = int(minor.det())
    if not det:
        raise ValueError('chosen minor is singular over Z')
    return {'rank_lower_bound': k, 'rows': pivot_rows, 'columns': pivot_cols,
            'exact_determinant': str(det)}


def check_case(d, p, cuts, expected_kernel, expected_tangent):
    rows = jacobian(d, p, cuts)
    t = tangent(d, p)
    m, tm = fmpz_mat(rows), fmpz_mat(t)
    product_matrix = m * tm
    annihilated = all(int(x) == 0 for x in product_matrix.entries())
    rank, trank = int(m.rank()), int(tm.rank())
    if not annihilated or 2 * d ** 4 - rank != expected_kernel or trank != expected_tangent:
        raise ValueError((d, cuts, rank, trank, annihilated))
    jminor, tminor = pivot_minor(rows), pivot_minor(t)
    if jminor['rank_lower_bound'] != rank or tminor['rank_lower_bound'] != trank:
        raise ValueError('rank/minor mismatch')
    enphasing = None
    if d == 4:
        n = d * d
        for r in range(n):
            v = [0] * (2 * n * n)
            c = p.index(r)
            v[n * n + r * n + c] = 1
            joined = fmpz_mat([t[i] + [v[i]] for i in range(len(t))])
            if int(joined.rank()) > trank:
                if any(int(x) for x in (m * fmpz_mat([[x] for x in v])).entries()):
                    raise ValueError('enphasing not in constraint kernel')
                enphasing = {'row': r, 'tangent_rank_after_adding': int(joined.rank()),
                             'curve': 'diag(exp(i theta delta_row)) P16; every reshape remains a phased permutation'}
                break
        if enphasing is None:
            raise ValueError('no transverse enphasing direction')
    return {'d': d, 'cuts': cuts, 'constraint_rank': rank, 'kernel_dimension': expected_kernel,
            'tangent_rank': trank, 'jacobian_times_tangent_zero': annihilated,
            'rank_equals_ambient_minus_tangent': rank + trank == 2 * d ** 4,
            'jacobian_sha256': hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest(),
            'jacobian_minor': jminor, 'tangent_minor': tminor, 'transverse_enphasing': enphasing}


def orbit_check():
    points = list(product(range(3), repeat=4))
    code = [(a, b, (2 * a + b) % 3, (a + b) % 3) for a, b in product(range(3), repeat=2)]
    if min(sum(x != y for x, y in zip(a, b)) for a, b in combinations(code, 2)) != 3:
        raise ValueError('distance')
    off = set(points) - set(code)
    if any(sum(sum(x != y for x, y in zip(p, c)) <= 1 for c in code) != 1 for p in points):
        raise ValueError('perfectness')

    def tau(cut):
        other = tuple(q for q in range(4) if q not in cut)
        proj = {tuple(c[q] for q in cut): c for c in code}
        comp = {tuple(c[q] for q in other): c for c in code}
        return {p: tuple(comp[tuple(p[q] for q in other)][i] if i in cut
                         else proj[tuple(p[q] for q in cut)][i] for i in range(4)) for p in points}

    answer = {}
    first = tau((0, 1))
    for name, cut in [('dual', (0, 2)), ('T-dual', (0, 3))]:
        second = tau(cut)
        unused, sizes = set(off), []
        while unused:
            orbit, stack = set(), [next(iter(unused))]
            while stack:
                p = stack.pop()
                if p in orbit:
                    continue
                orbit.add(p)
                stack.extend([first[p], second[p]])
            sizes.append(len(orbit))
            unused -= orbit
        if sorted(sizes) != [6] * 12:
            raise ValueError('off-code orbit structure')
        answer[name] = {'off_code_orbits': sorted(sizes), 'fixed_code_points':
                        sum(first[c] == second[c] == c for c in code),
                        'real_kernel_dimension_from_parity': len(code) + 2 * len(sizes)}
    return answer


def mul4(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return result


def main():
    out = Path(sys.argv[1])
    if out.exists():
        raise ValueError('refusing overwrite')
    started = stamp()
    p9 = [3 * ((2 * a + b) % 3) + (a + b) % 3 for a, b in product(range(3), repeat=2)]
    if sorted((r, c) for c, r in enumerate(p9)) != [(0, 0), (1, 8), (2, 4), (3, 5), (4, 1), (5, 6), (6, 7), (7, 3), (8, 2)]:
        raise ValueError('source C7 pin')
    p16 = [4 * (a ^ b) + (a ^ mul4(2, b)) for a, b in product(range(4), repeat=2)]
    result = {'started_at_pt': started, 'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'definition': 'real derivative of QQ†-I for Q=U and R(U) or Gamma(U); matrix indices and LU generators constructed directly',
              'P9_column_to_row': p9, 'perfect_code_check': orbit_check(),
              'cases': [check_case(3, p9, ['U', 'R'], 33, 33),
                        check_case(3, p9, ['U', 'Gamma'], 33, 33),
                        check_case(3, p9, ['U', 'R', 'Gamma'], 33, 33),
                        check_case(3, p9, ['U', 'U'], 81, 33),
                        check_case(4, p16, ['U', 'R'], 136, 61),
                        check_case(4, p16, ['U', 'Gamma'], 136, 61)],
              'status': 'EXACT_PARENT_JACOBIAN_TANGENT_AND_CONTROLS_PASS',
              'limits': 'Finite exact linear algebra plus the code orbit counts; the nonlinear isolation and qualitative gap require the independently reviewed written argument. No explicit gap bound.'}
    result['finished_at_pt'] = stamp()
    with out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'cases':
                      [(r['d'], r['cuts'], r['kernel_dimension'], r['tangent_rank']) for r in result['cases']]}))


if __name__ == '__main__':
    main()

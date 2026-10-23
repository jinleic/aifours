#!/usr/bin/env python3
"""k63-residue falsification aid v1 for the Row Lemma of K63-RES-v1 (EXPLORATORY; never a premise).

Universe (type data only; justified in falsification-aid-plan-v1.md): an unmarked odd C-vertex v (h_v = 0) with
neighbours u0..u3 (O' = O minus v), i* and d. Row entries x_u in 1..5, x_* in 1..5, x_d in {1, 2}; E in {1, 2}
(only min(E + v2(x_*), 2) can matter); F = 1 (only min(F, 1) can matter); 5-marker in {none, d, i*, u0..u3} with
exponent 1 (only min(h, 1) can matter). Types (exponents of 2, 3, 5):
  u: (v2 x_u, v3 x_u, v5 x_u + h_u);  i*: (E + v2 x_*, v3 x_*, v5 x_* + h_*);  d: (v2 x_d, F + v3 x_d, h_d).
A set S of neighbours is allowed iff every T subset of S with |T| >= 2 has a pair with gcd >= |T|.
LP: maximise sum_j a_j y_j (a_u = x_u, a_* = x_*, a_d = 2 x_d) s.t. sum_{j in S} y_j <= 1 for allowed S, y >= 0.
Checks: (main) every row with x_d = 1 has optimum > 5; (controls) optimum of the all-3 row with x_d = 1, x_* = 3,
no marker is 17/3; some x_d = 2 row has optimum <= 5 (the checker is not vacuous); with bound 6 instead of 5 some
x_d = 1 row survives (the 5/6 strengthening is load-bearing).
Stdlib only; exact Fractions; reads nothing; writes one JSON (exclusive create) given as argv[1]."""
import itertools, json, sys, time
from fractions import Fraction as Fr

T0 = time.monotonic()
BUDGET = 250.0
MAXBYTES = 1 << 20


def v(p, n):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def gcdval(a, b):
    return 2 ** min(a[0], b[0]) * 3 ** min(a[1], b[1]) * 5 ** min(a[2], b[2])


def allowed_sets(types):
    n = len(types)
    g = [[gcdval(types[i], types[j]) for j in range(n)] for i in range(n)]
    ok = {}
    res = []
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if mask >> i & 1]
        if len(idx) == 1:
            ok[mask] = True
        else:
            good = all(ok[mask & ~(1 << i)] for i in idx)
            if good:
                k = len(idx)
                good = any(g[i][j] >= k for i, j in itertools.combinations(idx, 2))
            ok[mask] = good
        if ok[mask]:
            res.append(idx)
    return res


def simplex_max(c, rows):
    """max c.y s.t. sum_{j in row} y_j <= 1 for each row, y >= 0. Exact, Bland's rule."""
    n = len(c)
    m = len(rows)
    # tableau: m constraint rows [A | I | b], objective row [-c | 0 | 0]
    T = []
    for r, row in enumerate(rows):
        line = [Fr(0)] * (n + m + 1)
        for j in row:
            line[j] = Fr(1)
        line[n + r] = Fr(1)
        line[-1] = Fr(1)
        T.append(line)
    obj = [Fr(-x) for x in c] + [Fr(0)] * m + [Fr(0)]
    basis = [n + r for r in range(m)]
    while True:
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            return obj[-1]
        best = None
        for r in range(m):
            if T[r][enter] > 0:
                ratio = T[r][-1] / T[r][enter]
                if best is None or ratio < best[0] or (ratio == best[0] and basis[r] < basis[best[1]]):
                    best = (ratio, r)
        if best is None:
            raise RuntimeError('unbounded')
        r = best[1]
        piv = T[r][enter]
        T[r] = [x / piv for x in T[r]]
        for rr in range(m):
            if rr != r and T[rr][enter] != 0:
                f = T[rr][enter]
                T[rr] = [a - f * b for a, b in zip(T[rr], T[r])]
        if obj[enter] != 0:
            f = obj[enter]
            obj = [a - f * b for a, b in zip(obj, T[r])]
        basis[r] = enter


def row_opt(xs, xstar, xd, E, marker):
    F = 1
    types = []
    for i, x in enumerate(xs):
        h = 1 if marker == 'u%d' % i else 0
        types.append((v(2, x), v(3, x), v(5, x) + h))
    types.append((E + v(2, xstar), v(3, xstar), v(5, xstar) + (1 if marker == 'i*' else 0)))
    types.append((v(2, xd), F + v(3, xd), 1 if marker == 'd' else 0))
    a = list(xs) + [xstar, 2 * xd]
    return simplex_max(a, allowed_sets(types))


def main():
    out = sys.argv[1]
    markers = ['none', 'd', 'i*', 'u0', 'u1', 'u2', 'u3']
    res = {'probe': 'k63res_rowlemma_falsification_aid_v1', 'python': sys.version, 'status': 'INCOMPLETE'}
    checked = 0
    violations = []
    min_opt = None
    min_rows = []
    survivors_bound6 = 0
    for xd in (1,):
        for xs in itertools.product(range(1, 6), repeat=4):
            for xstar in range(1, 6):
                for E in (1, 2):
                    for mk in markers:
                        opt = row_opt(xs, xstar, xd, E, mk)
                        checked += 1
                        if opt <= 5:
                            if len(violations) < 200:
                                violations.append([list(xs), xstar, xd, E, mk, str(opt)])
                        if opt < 6:
                            survivors_bound6 += 1
                        if min_opt is None or opt < min_opt:
                            min_opt, min_rows = opt, [[list(xs), xstar, xd, E, mk]]
                        elif opt == min_opt and len(min_rows) < 20:
                            min_rows.append([list(xs), xstar, xd, E, mk])
                        if time.monotonic() - T0 > BUDGET:
                            res['stopped'] = 'budget'
                            raise SystemExit(write(out, res, checked, violations, min_opt, min_rows,
                                                   survivors_bound6, None))
    controls = {}
    controls['all3_xd1_xs3_none'] = str(row_opt((3, 3, 3, 3), 3, 1, 1, 'none'))
    controls['fours_xd2_xs3_E2_none'] = str(row_opt((4, 4, 4, 4), 3, 2, 2, 'none'))
    xd2_le5 = 0
    for xs in itertools.product(range(1, 6), repeat=4):
        for xstar in range(1, 6):
            if row_opt(xs, xstar, 2, 2, 'none') <= 5:
                xd2_le5 += 1
        if time.monotonic() - T0 > BUDGET:
            break
    controls['xd2_E2_none_rows_with_opt_le5'] = xd2_le5
    res['status'] = 'COMPLETE'
    write(out, res, checked, violations, min_opt, min_rows, survivors_bound6, controls)


def write(out, res, checked, violations, min_opt, min_rows, survivors_bound6, controls):
    res.update({'rows_checked_xd1': checked, 'violations_opt_le_5': violations,
                'n_violations_listed': len(violations), 'min_opt_xd1': str(min_opt), 'argmin_rows': min_rows,
                'xd1_rows_with_opt_lt_6': survivors_bound6, 'controls': controls,
                'seconds': round(time.monotonic() - T0, 3)})
    data = json.dumps(res, indent=1)
    if len(data) > MAXBYTES:
        data = json.dumps({'status': 'OUTPUT_CAP', 'rows_checked_xd1': checked})
    with open(out, 'x') as f:
        f.write(data)
    print(res['status'], checked, len(violations), str(min_opt))
    return 0


if __name__ == '__main__':
    main()

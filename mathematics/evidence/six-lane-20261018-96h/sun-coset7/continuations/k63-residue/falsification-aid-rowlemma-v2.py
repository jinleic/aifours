#!/usr/bin/env python3
"""k63-residue falsification aid v2 for the Row Lemma of K63-RES-v1 (EXPLORATORY; never a premise).
Supersedes the never-run v1 (same universe; v1 had no caching and no optimality certificate).

Universe (type data; justified in falsification-aid-plan-v1.md): an unmarked odd C-vertex v (h_v = 0) with
neighbours u0..u3 (O' = O minus v), i* and d. Row entries x_u in 1..5, x_* in 1..5, x_d in {1, 2}; E in {1, 2}
(only min(E + v2(x_*), 2) can matter); F = 1 (only min(F, 1) can matter); 5-marker in {none, d, i*, u0..u3} with
exponent 1 (only min(h, 1) can matter). Types (exponents of 2, 3, 5):
  u: (v2 x_u, v3 x_u, v5 x_u + h_u);  i*: (E + v2 x_*, v3 x_*, v5 x_* + h_*);  d: (v2 x_d, F + v3 x_d, h_d).
A set S of neighbours is allowed iff every T subset of S with |T| >= 2 has a pair with gcd >= |T|.
LP: maximise sum_j a_j y_j (a_u = x_u, a_* = x_*, a_d = 2 x_d) s.t. sum_{j in S} y_j <= 1 for allowed S, y >= 0
(only maximal allowed S are needed since y >= 0). Each optimum is certified exactly: primal y feasible with value
opt, dual u >= 0 with u^T A >= a and sum(u) = opt.
Checks: (main) every row with x_d = 1 has optimum > 5; (controls) all-3 row x_d = 1, x_* = 3, no marker -> 17/3;
row (4,4,4,4), x_* = 3, x_d = 2, E = 2, no marker -> 5; count of x_d = 2 rows (E = 2, no marker) with optimum <= 5
(> 0 means the checker is not vacuous); count of x_d = 1 rows with optimum < 6 (> 0 means the 5/6 bound is needed).
Stdlib only; exact Fractions; reads nothing; writes one JSON (exclusive create) at argv[1]; self budget 250 s."""
import itertools, json, sys, time
from fractions import Fraction as Fr

T0 = time.monotonic()
BUDGET = 250.0
MAXBYTES = 1 << 20
CACHE = {}


class Budget(Exception):
    pass


def val(p, n):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def gcdval(a, b):
    return 2 ** min(a[0], b[0]) * 3 ** min(a[1], b[1]) * 5 ** min(a[2], b[2])


def maximal_allowed(types):
    n = len(types)
    g = [[gcdval(types[i], types[j]) for j in range(n)] for i in range(n)]
    ok = [False] * (1 << n)
    for mask in range(1, 1 << n):
        idx = [i for i in range(n) if mask >> i & 1]
        if len(idx) == 1:
            ok[mask] = True
            continue
        if not all(ok[mask & ~(1 << i)] for i in idx):
            continue
        k = len(idx)
        ok[mask] = any(g[i][j] >= k for i, j in itertools.combinations(idx, 2))
    allowed = [m for m in range(1, 1 << n) if ok[m]]
    maximal = [m for m in allowed if not any(ok[m | (1 << i)] for i in range(n) if not m >> i & 1)]
    return [[i for i in range(n) if m >> i & 1] for m in maximal]


def simplex_max(c, rows):
    n, m = len(c), len(rows)
    A = [[Fr(1) if j in row else Fr(0) for j in range(n)] for row in rows]
    T = [A[r] + [Fr(1) if s == r else Fr(0) for s in range(m)] + [Fr(1)] for r in range(m)]
    obj = [Fr(-x) for x in c] + [Fr(0)] * m + [Fr(0)]
    basis = [n + r for r in range(m)]
    while True:
        enter = next((j for j in range(n + m) if obj[j] < 0), None)
        if enter is None:
            break
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
        f = obj[enter]
        obj = [a - f * b for a, b in zip(obj, T[r])]
        basis[r] = enter
    opt = obj[-1]
    y = [Fr(0)] * n
    for r, bvar in enumerate(basis):
        if bvar < n:
            y[bvar] = T[r][-1]
    u = obj[n:n + m]
    # exact certificate checks
    assert all(t >= 0 for t in y) and all(sum(y[j] for j in row) <= 1 for row in rows)
    assert sum(c[j] * y[j] for j in range(n)) == opt
    assert all(t >= 0 for t in u) and sum(u) == opt
    assert all(sum(u[r] * A[r][j] for r in range(m)) >= c[j] for j in range(n))
    return opt


def row_opt(xs, xstar, xd, E, marker):
    if time.monotonic() - T0 > BUDGET:
        raise Budget()
    F = 1
    types = []
    for i, x in enumerate(xs):
        types.append((val(2, x), val(3, x), val(5, x) + (1 if marker == 'u%d' % i else 0)))
    types.append((E + val(2, xstar), val(3, xstar), val(5, xstar) + (1 if marker == 'i*' else 0)))
    types.append((val(2, xd), F + val(3, xd), 1 if marker == 'd' else 0))
    a = list(xs) + [xstar, 2 * xd]
    key = tuple(sorted(zip(types, a)))
    if key not in CACHE:
        ts = [k[0] for k in key]
        ws = [k[1] for k in key]
        CACHE[key] = simplex_max(ws, maximal_allowed(ts))
    return CACHE[key]


def main():
    out = sys.argv[1]
    markers = ['none', 'd', 'i*', 'u0', 'u1', 'u2', 'u3']
    res = {'probe': 'k63res_rowlemma_falsification_aid_v2', 'python': sys.version, 'status': 'INCOMPLETE'}
    st = {'checked': 0, 'violations': [], 'min_opt': None, 'argmin': [], 'lt6': 0}
    controls = None
    try:
        for xs in itertools.product(range(1, 6), repeat=4):
            for xstar in range(1, 6):
                for E in (1, 2):
                    for mk in markers:
                        opt = row_opt(xs, xstar, 1, E, mk)
                        st['checked'] += 1
                        rec = [list(xs), xstar, 1, E, mk]
                        if opt <= 5 and len(st['violations']) < 200:
                            st['violations'].append(rec + [str(opt)])
                        if opt < 6:
                            st['lt6'] += 1
                        if st['min_opt'] is None or opt < st['min_opt']:
                            st['min_opt'], st['argmin'] = opt, [rec]
                        elif opt == st['min_opt'] and len(st['argmin']) < 20:
                            st['argmin'].append(rec)
        controls = {'all3_xd1_xstar3_none': str(row_opt((3, 3, 3, 3), 3, 1, 1, 'none')),
                    'fours_xd2_xstar3_E2_none': str(row_opt((4, 4, 4, 4), 3, 2, 2, 'none'))}
        cnt = 0
        for xs in itertools.product(range(1, 6), repeat=4):
            for xstar in range(1, 6):
                if row_opt(xs, xstar, 2, 2, 'none') <= 5:
                    cnt += 1
        controls['xd2_E2_none_rows_opt_le5'] = cnt
        res['status'] = 'COMPLETE'
    except Budget:
        res['status'] = 'STOPPED_BUDGET'
    res.update({'rows_checked_xd1': st['checked'], 'expected_rows_xd1': 625 * 5 * 2 * 7,
                'violations_opt_le_5': st['violations'], 'n_violations_listed': len(st['violations']),
                'min_opt_xd1': str(st['min_opt']), 'argmin_rows': st['argmin'],
                'xd1_rows_opt_lt_6': st['lt6'], 'controls': controls, 'distinct_lps': len(CACHE),
                'seconds': round(time.monotonic() - T0, 3)})
    data = json.dumps(res, indent=1)
    if len(data) > MAXBYTES:
        data = json.dumps({'status': 'OUTPUT_CAP', 'rows_checked_xd1': st['checked']})
    with open(out, 'x') as f:
        f.write(data)
    print(res['status'], st['checked'], len(st['violations']), str(st['min_opt']))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact-arithmetic counterexample search for the two-copy d=4 rank-2 statement T2.

T2: q2(C) = ||C||^2 - 1/2||Tr_1 C||^2 - 1/2||Tr_2 C||^2 + 1/4|Tr C|^2 >= 0 for every complex
C on C^4(x)C^4 of rank <= 2.  Parametrize C = U V^dagger with U, V 16x2 Gaussian-integer
matrices; minimize r = q2(C)/||C||^2 by gradient steps rounded to the integer grid.
ALL arithmetic is on Python integers (Gaussian integers as (re, im) int pairs): every reported
value is an exact rational Q/N.  No floats are used anywhere.  The search is heuristic; only a
returned exact negative Q would be a proof (of failure).  Authorized by Main as an exact
counterexample search; no held input.
"""
import json
import random
import sys
from fractions import Fraction
from pathlib import Path
import hashlib

D = 4
N16 = 16


def mat_c(U, V):
    """C = U V^dagger as two int matrices (re, im)."""
    Cr = [[0] * N16 for _ in range(N16)]
    Ci = [[0] * N16 for _ in range(N16)]
    for x in range(N16):
        ux = U[x]
        for y in range(N16):
            vy = V[y]
            re = 0
            im = 0
            for r in range(2):
                a, b = ux[r]
                c, d = vy[r]
                # (a+ib)(c-id) = ac+bd + i(bc-ad)
                re += a * c + b * d
                im += b * c - a * d
            Cr[x][y] = re
            Ci[x][y] = im
    return Cr, Ci


def traces(Cr, Ci):
    t1r = [[0] * D for _ in range(D)]
    t1i = [[0] * D for _ in range(D)]
    t2r = [[0] * D for _ in range(D)]
    t2i = [[0] * D for _ in range(D)]
    for x1 in range(D):
        for x2 in range(D):
            for y2 in range(D):
                t1r[x2][y2] += Cr[4 * x1 + x2][4 * x1 + y2]
                t1i[x2][y2] += Ci[4 * x1 + x2][4 * x1 + y2]
    for x1 in range(D):
        for y1 in range(D):
            for x2 in range(D):
                t2r[x1][y1] += Cr[4 * x1 + x2][4 * y1 + x2]
                t2i[x1][y1] += Ci[4 * x1 + x2][4 * y1 + x2]
    trr = sum(Cr[x][x] for x in range(N16))
    tri = sum(Ci[x][x] for x in range(N16))
    return t1r, t1i, t2r, t2i, trr, tri


def sq(Mr, Mi):
    return sum(a * a for row in Mr for a in row) + sum(a * a for row in Mi for a in row)


def evaluate(U, V):
    Cr, Ci = mat_c(U, V)
    t1r, t1i, t2r, t2i, trr, tri = traces(Cr, Ci)
    n = sq(Cr, Ci)
    Q = 4 * n - 2 * sq(t1r, t1i) - 2 * sq(t2r, t2i) + trr * trr + tri * tri  # = 4 q2
    return Q, 4 * n, (Cr, Ci, t1r, t1i, t2r, t2i, trr, tri)


def four_w(data):
    Cr, Ci, t1r, t1i, t2r, t2i, trr, tri = data
    Wr = [[4 * Cr[x][y] for y in range(N16)] for x in range(N16)]
    Wi = [[4 * Ci[x][y] for y in range(N16)] for x in range(N16)]
    for x1 in range(D):
        for x2 in range(D):
            for y2 in range(D):
                Wr[4 * x1 + x2][4 * x1 + y2] -= 2 * t1r[x2][y2]
                Wi[4 * x1 + x2][4 * x1 + y2] -= 2 * t1i[x2][y2]
    for x1 in range(D):
        for y1 in range(D):
            for x2 in range(D):
                Wr[4 * x1 + x2][4 * y1 + x2] -= 2 * t2r[x1][y1]
                Wi[4 * x1 + x2][4 * y1 + x2] -= 2 * t2i[x1][y1]
    for x in range(N16):
        Wr[x][x] += trr
        Wi[x][x] += tri
    return Wr, Wi


def mul_mv(Mr, Mi, V, adjoint=False):
    """Return M V (or M^dagger V) for a 16x2 Gaussian-int matrix V."""
    out = [[(0, 0), (0, 0)] for _ in range(N16)]
    for x in range(N16):
        for r in range(2):
            re = 0
            im = 0
            for y in range(N16):
                if adjoint:
                    a, b = Mr[y][x], -Mi[y][x]
                else:
                    a, b = Mr[x][y], Mi[x][y]
                c, d = V[y][r]
                re += a * c - b * d
                im += a * d + b * c
            out[x][r] = (re, im)
    return out


def gradient(U, V, Q, N, data):
    Wr, Wi = four_w(data)
    Cr, Ci = data[0], data[1]
    WV = mul_mv(Wr, Wi, V)
    CV = mul_mv(Cr, Ci, V)
    WU = mul_mv(Wr, Wi, U, adjoint=True)
    CU = mul_mv(Cr, Ci, U, adjoint=True)
    gU = [[(N * WV[x][r][0] - 4 * Q * CV[x][r][0], N * WV[x][r][1] - 4 * Q * CV[x][r][1]) for r in range(2)] for x in range(N16)]
    gV = [[(N * WU[x][r][0] - 4 * Q * CU[x][r][0], N * WU[x][r][1] - 4 * Q * CU[x][r][1]) for r in range(2)] for x in range(N16)]
    return gU, gV


def maxabs(M):
    return max(max(abs(a), abs(b)) for row in M for (a, b) in row)


def shift(M, s):
    if s >= 0:
        return [[(a << s, b << s) for (a, b) in row] for row in M]
    s = -s
    return [[(a >> s, b >> s) for (a, b) in row] for row in M]


def renorm(M, target_bits=30):
    m = maxabs(M)
    if m == 0:
        return M
    return shift(M, target_bits - m.bit_length())


def step(M, g, k):
    """M - floor(g / 2^k) entrywise (exact integer op)."""
    return [[(a - (ga >> k), b - (gb >> k)) for (a, b), (ga, gb) in zip(row, grow)] for row, grow in zip(M, g)]


def less(Q1, N1, Q0, N0):
    return Q1 * N0 < Q0 * N1


def descend(U, V, iters):
    U = renorm(U)
    V = renorm(V)
    Q, N, data = evaluate(U, V)
    for _ in range(iters):
        gU, gV = gradient(U, V, Q, N, data)
        mg = max(maxabs(gU), maxabs(gV))
        if mg == 0:
            break
        k0 = max(0, mg.bit_length() - 28)  # first trial step moves entries by ~2^28 (entries ~2^30)
        improved = False
        for k in range(k0, k0 + 40):
            U1 = step(U, gU, k)
            V1 = step(V, gV, k)
            Q1, N1, data1 = evaluate(U1, V1)
            if N1 > 0 and less(Q1, N1, Q, N):
                U, V, Q, N, data = U1, V1, Q1, N1, data1
                improved = True
                break
        if not improved:
            break
        U = renorm(U)
        V = renorm(V)
        Q, N, data = evaluate(U, V)
    return U, V, Q, N


def rand_mat(rng, bits=20):
    lim = 1 << bits
    return [[(rng.randint(-lim, lim), rng.randint(-lim, lim)) for _ in range(2)] for _ in range(N16)]


def dec(Q, N, digits=10):
    """Exact integer decimal rendering of Q/N, no floats."""
    sign = '-' if Q * N < 0 else ''
    Q, N = abs(Q), abs(N)
    whole = Q // N
    frac = (Q % N) * 10 ** digits // N
    return f"{sign}{whole}.{frac:0{digits}d}"


def main(seed=20261029, starts=8, iters=120):
    rng = random.Random(seed)
    runs = []
    best = None
    for s in range(starts):
        U = rand_mat(rng)
        V = rand_mat(rng)
        Q0, N0, _ = evaluate(renorm(U), renorm(V))
        U, V, Q, N = descend(U, V, iters)
        runs.append({'start': s, 'initial_ratio': dec(Q0, N0), 'final_ratio': dec(Q, N), 'final_Q_sign': (Q > 0) - (Q < 0)})
        if best is None or less(Q, N, best[0], best[1]):
            best = (Q, N, U, V)
    Q, N, U, V = best
    return runs, best


if __name__ == '__main__':
    starts = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    runs, best = main(starts=starts, iters=iters)
    Q, N, U, V = best
    record = {
        'arithmetic': 'Python integers only (Gaussian integers as int pairs); no floats',
        'objective': 'r = q2(UV^dagger)/||UV^dagger||^2, d=4, two sites, rank<=2',
        'starts': starts,
        'iterations_per_start': iters,
        'runs': runs,
        'best_ratio_decimal_exact_truncation': dec(Q, N),
        'best_ratio_numerator_sign': (Q > 0) - (Q < 0),
        'counterexample_found': Q < 0,
        'best_U': U if Q < 0 else None,
        'best_V': V if Q < 0 else None,
        'scope': 'Heuristic exact-arithmetic local search; a nonnegative outcome is NOT a proof of T2. Only an exact negative Q (verified independently) would refute T2.',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out = Path(__file__).resolve().parent / 'frontier-20261029-t2-exact-descent-search-results-v1.json'
    out.write_text(json.dumps(record, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in record.items() if k not in ('best_U', 'best_V')}, sort_keys=True))

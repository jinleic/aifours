#!/usr/bin/env python3
"""Reviewer-owned exact local controls, not a target search or a proof."""
import json

checks = []


def require(name, ok):
    checks.append((name, bool(ok)))
    if not ok:
        raise AssertionError(name)


def walsh(values):
    a = list(values)
    step = 1
    while step < len(a):
        for j in range(0, len(a), 2 * step):
            for i in range(j, j + step):
                x, y = a[i], a[i + step]
                a[i], a[i + step] = x + y, x - y
        step *= 2
    return a


def bit(x):
    return bin(x).count('1') & 1


def anf_degree(values):
    c = list(values)
    for i in range(8):
        for x in range(256):
            if x & (1 << i):
                c[x] ^= c[x ^ (1 << i)]
    return max((bin(x).count('1') for x in range(256) if c[x]), default=-1)


# Fixed rank-two abstract quadratic model; this is not a Boolean target.
def q(x):
    return (x & 1) ^ ((x >> 1) & 1) ^ ((x & 1) & ((x >> 1) & 1))


def B(x, y):
    return q(x ^ y) ^ q(x) ^ q(y)


R = [x for x in range(256) if x & 3 == 0]
W = [x << 2 for x in range(8)]
require('anisotropic q zeros exactly six-dimensional radical',
        len(R) == 64 and all((q(x) == 0) == (x in R) for x in range(256)))
require('radical and rank-two polar pairing',
        all(B(x, y) == 0 for x in R for y in range(256))
        and B(1, 2) == 1 and all(B(x, y) == B(x & 3, y & 3)
                                  for x in range(256) for y in (1, 2, 4, 8, 16, 32, 64, 128)))
require('eight-zero three-space and degree-five indicator',
        len(W) == 8 and all(x ^ y in W for x in W for y in W)
        and anf_degree([int(x in W) for x in range(256)]) == 5)
W_bad = W[:-1] + [32]
require('NEGATIVE nonflat zero set has degree above five',
        len(set(W_bad)) == 8 and anf_degree([int(x in W_bad) for x in range(256)]) > 5)

# A radical phase is normalized by one character; inspect all four Walsh modes.
phase = lambda x: q(x) ^ bit(x & 20)
normalized = lambda x: phase(x) ^ bit(x & 20)
require('NEGATIVE original phase varies along selected zero direction',
        any(phase(x ^ 4) != phase(x) for x in range(256)))
require('translated phase invariant along W',
        all(normalized(x ^ r) == normalized(x) for x in range(256) for r in W))
wg = walsh([1 - 2 * normalized(x) for x in range(256)])
require('rank-two eight-dimensional phase has exactly four amplitudes 128',
        sum(v != 0 for v in wg) == 4 and all(abs(v) == 128 for v in wg if v))

# All eight allowable odd signed coefficients obey the decomposition.
def decomposition(k):
    g = 1 if k % 4 == 1 else -1
    h = int(abs(k) in (3, 5))
    d = (g * (12 * h - 7) - k) // 8
    return g, h, d

require('all eight odd phase decomposition cases',
        all(k == g * (12 * h - 7) - 8 * d and (d != 0) == (abs(k) in (1, 3))
            and d * g == (1 if abs(k) == 3 else -1 if abs(k) == 1 else 0)
            for k in (-7, -5, -3, -1, 1, 3, 5, 7)
            for g, h, d in [decomposition(k)]))

# Three D=16 pair multisets satisfy all single-shift integer arithmetic,
# including m=116. They have no asserted global frequency placement.
def formal_pairs(E):
    even = [(0, 0)] * 4 + [(4, 4)] * 28 + [(2, 2)] * (E // 2) + [(6, 6)] * (96 - E // 2)
    n3 = E - 4
    odd = [(-7, -3)] * n3 + [(1, 5)] * (16 - n3) + [(-7, 5)] * 112
    return even, odd


def stats(even, odd):
    allpairs = even + odd
    E = sum(abs(x) == 2 for p in even for x in p)
    D = sum(abs(x) in (1, 3) for p in odd for x in p)
    e_energy = sum(x * x for p in even for x in p)
    o_energy = sum(x * x for p in odd for x in p)
    corr_pairs = sum(x * y for x, y in allpairs)
    n0 = sum(x == y for x, y in even)
    b = sum(abs(x - y) == 4 for x, y in odd)
    m = e_energy // 64
    n = {j: sum(abs(x) == j for p in odd for x in p) for j in (1, 3, 5, 7)}
    return E, D, e_energy, o_energy, corr_pairs, n0, b, m, n


for E in (4, 8, 12):
    even, odd = formal_pairs(E)
    e, d, ee, oe, corr, n0, b, m, n = stats(even, odd)
    require('D16 formal pair arithmetic E=%d m=%d' % (E, 122 - E // 2),
            len(even) == len(odd) == 128 and e == E and d == 16
            and ee == 7808 - 32 * E and ee % 64 == 0 and oe == 64 * (256 - m)
            and ee + oe == 16384 and corr == 0 and n0 == 128 and b == 16
            and n0 + 2 * b == 160 and m == 122 - E // 2
            and 8 * (m - 60) == 6 * n[1] + 5 * n[3] + 3 * n[5]
            and 0 <= (124 - m) // 2 <= 4 and (124 - m) % 2 == 0
            and all((x - y) % 8 == 0 for x, y in even)
            and all((x - y) % 4 == 0 and abs(x - y) in (4, 12) for x, y in odd))

# Intended-reason countercontrols, separate from any realizability claim.
even, odd = formal_pairs(12)
odd_bad4 = list(odd)
odd_bad4[0] = (-7, 3)
require('NEGATIVE changed odd pair breaks normalized mod-four phase',
        (odd_bad4[0][0] - odd_bad4[0][1]) % 4 != 0)
odd_bad8 = list(odd)
odd_bad8[-1] = (-7, 1)
require('NEGATIVE same-mod-four odd pair breaks phase-one mod-eight condition',
        (odd_bad8[-1][0] - odd_bad8[-1][1]) % 4 == 0
        and (odd_bad8[-1][0] - odd_bad8[-1][1]) % 8 == 0)
even_bad = list(even)
even_bad[32] = (2, -6)
require('NEGATIVE even mod-eight period does not itself imply exact equality',
        (even_bad[32][0] - even_bad[32][1]) % 8 == 0 and even_bad[32][0] != even_bad[32][1])

# Check 8D-to-7D Fourier normalization on one reviewer-built Boolean sign
# example, not claimed to have the target peak, balance, or rank.
u = [0 if y & 1 else 1 for y in range(256)]
v = [0 if not (y & 1) else 1 - 2 * (bit((y >> 1) & 43) ^ (((y >> 1) & 1) & ((y >> 2) & 1))) for y in range(256)]
ku = [z // 2 for z in walsh(u)]
kv = [z // 2 for z in walsh(v)]
require('even exact Fourier period and disjoint sign-pair supports',
        all(ku[a] == ku[a ^ 1] for a in range(256))
        and all(u[y] * u[y] + v[y] * v[y] == 1 for y in range(256)))
a7 = [v[(x << 1) | 1] for x in range(128)]
w7 = walsh(a7)
require('all 128 restricted seven-dimensional Walsh coefficients',
        all(w7[a] == kv[a << 1] - kv[(a << 1) ^ 1] for a in range(128)))
require('NEGATIVE using plus instead of difference is detected',
        any(w7[a] != kv[a << 1] + kv[(a << 1) ^ 1] for a in range(128)))
require('parseval forces 16 fours and 112 twelves if only those magnitudes',
        16 * 4 * 4 + 112 * 12 * 12 == 128 * 128
        and all(16 * a + 144 * (128 - a) != 128 * 128 for a in range(129) if a != 16))

print(json.dumps({'scope': 'reviewer-owned finite local controls only; no target witness or CR7 verification',
                  'checks': len(checks), 'passed': sum(ok for _, ok in checks),
                  'cases': [name for name, _ in checks]}, indent=2))

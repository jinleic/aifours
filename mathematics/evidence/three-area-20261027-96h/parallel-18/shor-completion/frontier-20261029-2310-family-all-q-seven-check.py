#!/usr/bin/env python3
"""Exact residue checks for frontier-20261029-2310-family-all-q-seven-divides-head-v1.md.

Only Python integers, math.gcd and finite loops are used. For n=2310*2^k and
an ODD integer u, gcd(u,n)=gcd(u,1155); every Sands test below compares
elements of opposite parity, so residues modulo 2310 are exact for every k.
Not checked: Laba-Londner Corollary 6.2, Sands' theorem, the actual-word
border theorem, or any written step beyond the finite tables cited.
"""
from functools import lru_cache
from itertools import combinations, product
from math import gcd
import json

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
QBAN = {3, 5, 11}      # odd gcds of old head differences
PBAN = {1, 7}          # odd gcds of old tail differences
G = (0, 1, 7, 2, 3)
T = range(2310)
OUT = {}


def opp(x, y):
    return (x - y) % 2 == 1


def q_ok(x, y):
    return not (opp(x, y) and gcd(x - y, 1155) in QBAN)


def p_ok(x, y):
    return not (opp(x, y) and gcd(x - y, 1155) in PBAN)


def dom(e, r):
    return [z for z in T if z % e == r and all(q_ok(z, y) for y in Y)]


def states(zs, f):
    return sorted({(z % 2, z % f) for z in zs})


# Lemma 3': no admissible head in 4 mod 15, 1 mod 33, 2 mod 55.
for m, r in ((15, 4), (33, 1), (55, 2)):
    bad = [z for z in T if z % m == r]
    assert bad and all(not all(p_ok(z, a) for a in A) for z in bad), (m, r)
assert all(p_ok(a, b) for a, b in combinations(A, 2))
OUT['lemma3'] = 'PASS'

# d=1, e=1155: class 827 (=2 mod 165, =1 mod 7) is empty.
assert 827 % 165 == 2 and 827 % 7 == 1 and dom(1155, 827) == []
OUT['e1155_class827'] = []

# d=3, e=385, free prime 3.
D = {r: dom(385, r) for r in (3, 24, 25)}
assert states(D[3], 3) == [(1, 2)] and states(D[24], 3) == [(1, 2)]
assert states(D[25], 3) == [(0, 0), (0, 2)]
assert not any(q_ok(a, b) and q_ok(a, c) and q_ok(b, c)
               for a in D[3] for b in D[24] for c in D[25])
OUT['e385'] = {r: states(D[r], 3) for r in D}

# d=5, e=231, free prime 5.
D = {r: dom(231, r) for r in (22, 25, 26, 36)}
assert states(D[22], 5) == [(1, 0)] and states(D[25], 5) == [(1, 4)]
assert states(D[26], 5) == [(0, 0), (0, 4), (1, 4)]
assert states(D[36], 5) == [(0, 0), (0, 1), (0, 4)]
assert not any(all(q_ok(u, v) for u, v in combinations(t, 2))
               for t in product(*(D[r] for r in (22, 25, 26, 36))))
OUT['e231'] = {r: states(D[r], 5) for r in D}

# d=11, e=105, free prime 11: unpinned arc consistency over 105 classes.
D = {r: dom(105, r) for r in range(105)}
OUT['e105_initial_domain_size_hist'] = {k: sum(len(v) == k for v in D.values())
                                        for k in sorted({len(v) for v in D.values()})}
changed = True
while changed:
    changed = False
    for r in range(105):
        for s in range(105):
            if r != s:
                keep = [z for z in D[r] if any(q_ok(z, w) for w in D[s])]
                if len(keep) != len(D[r]):
                    D[r], changed = keep, True
assert all(len(D[r]) == 1 for r in range(105))
assert all(D[r][0] % 2 == (1 if r % 3 == 1 else 0) and D[r][0] % 11 == G[r % 5]
           for r in range(105))
S = sorted(D[r][0] for r in range(105))
assert set(Y) <= set(S) and all(q_ok(u, v) for u, v in combinations(S, 2))
OUT['e105_fixpoint'] = 'all 105 classes singleton: odd iff r=1 mod 3, residue mod 11 = g(r mod 5)'


def ptrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return ptrim(out)


def pdivmod(a, m):
    a, m = list(a), ptrim(m)
    dm = len(m) - 1
    assert m[-1] == 1
    if len(a) <= dm:
        return [0], ptrim(a)
    q = [0] * (len(a) - dm)
    for i in range(len(a) - 1, dm - 1, -1):
        c = a[i]
        if c:
            q[i - dm] = c
            for j in range(dm + 1):
                a[i - dm + j] -= c * m[j]
    return ptrim(q), ptrim(a[:dm] if dm else [0])


@lru_cache(None)
def cyclo(m):
    num = [-1] + [0] * (m - 1) + [1]
    for d in range(1, m):
        if m % d == 0:
            num, rem = pdivmod(num, cyclo(d))
            assert not any(rem)
    return tuple(ptrim(num))


fold = [0] * 110
for z in S:
    fold[z % 110] += 1
W = [(2 if z % 2 == 0 else 1) if z % 55 in (0, 1, 7, 13, 14) else 0 for z in range(110)]
assert fold == [7 * w for w in W]
assert all(any(pdivmod(W, cyclo(m))[1]) for m in (11, 22, 55, 110))
prod = [1]
for m in (11, 22, 55, 110):
    prod = pmul(prod, list(cyclo(m)))
assert prod == [1 if i % 10 == 0 else 0 for i in range(101)]
X1 = [z for z in T if z % 110 == 1]
assert len(X1) == 21 and all(not (p_ok(z, 0) and p_ok(z, 8)) for z in X1)
OUT['e105_fourier_and_certificate'] = 'PASS'

# Bounded actual-gcd diagnostics, k=0..3.
diag = {}
for k in range(4):
    n = 2310 * 2 ** k
    GY = {gcd(a - b, n) for a, b in combinations(Y, 2)}
    GA = {gcd(a - b, n) for a, b in combinations(A, 2)}
    assert PBAN <= GY and QBAN <= GA
    Ph = [x for x in range(n) if all(x == a or gcd(x - a, n) not in GY for a in A)]
    assert not any(x % 15 == 4 or x % 33 == 1 or x % 55 == 2 for x in Ph)
    Qt = [x for x in range(n) if all(x == y or gcd(x - y, n) not in GA for y in Y)]
    assert not any(x % 1155 == 827 for x in Qt)
    for e, rs in ((385, (3, 24, 25)), (231, (22, 25, 26, 36)), (105, range(105))):
        for r in rs:
            assert {x % 2310 for x in Qt if x % e == r} <= set(dom(e, r)), (k, e, r)
    diag[n] = {'P_screen': len(Ph), 'Q_screen': len(Qt)}
OUT['bounded_diagnostics'] = diag
OUT['result'] = 'PASS'
print(json.dumps(OUT, indent=1, sort_keys=True, default=str))

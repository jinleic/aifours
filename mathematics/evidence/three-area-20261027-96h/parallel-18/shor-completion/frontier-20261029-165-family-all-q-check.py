#!/usr/bin/env python3
"""Exact residue checks for the all-t n=165*2^t anchored-border candidate.

Companion of frontier-20261029-165-family-all-q-anchored-border-no-go-v1.md.
Only Python integers, math.gcd and finite loops are used.

Why residues modulo 330 suffice for every t>=1: if n=165*2^t and u is an ODD
integer then gcd(u,n)=gcd(u,165). Every Sands test below compares two
elements of OPPOSITE parity, so it depends only on residues modulo 330. The
bounded t=1..6 diagnostics at the end recompute actual old-anchor screens
with gcd(.,n). NOT checked here: the imported Laba-Londner Corollary 6.2
(T2), Sands' theorem, the actual-word border theorem, or any written step of
the packet beyond the finite tables it cites.
"""
from functools import lru_cache
from itertools import combinations, product
from math import gcd
import json

A = (0, 3, 8, 11)          # old heads (in P)
Y = (0, 1, 7, 13, 14)      # old tails (in Q)
QBAN = {3, 5, 11}          # odd gcds that Q may not use (old head differences)
G = (0, 1, 7, 2, 3)        # g(u): residue mod 11 forced on Q-elements with x=u mod 5
T330 = range(330)
OUT = {}


def opp(x, y):
    return (x - y) % 2 == 1


def q_ok(x, y):
    """Type-level rule (SQ) for two Q-elements of residues x, y mod 330."""
    return not (opp(x, y) and gcd(x - y, 165) in QBAN)


def p_ok(x, y):
    """Type-level rule (SP) for two P-elements of residues x, y mod 330."""
    return not (opp(x, y) and gcd(x - y, 165) == 1)


def dom(e, r):
    """Residues z mod 330 in class r mod e passing (SQ) against every old tail."""
    return [z for z in T330 if z % e == r and all(q_ok(z, y) for y in Y)]


def states(zs, f):
    return sorted({(z % 2, z % f) for z in zs})


# Lemma 3: no admissible head in 4 mod 15, 1 mod 33 or 2 mod 55.
for m, r in ((15, 4), (33, 1), (55, 2)):
    bad = [z for z in T330 if z % m == r]
    assert bad and all(not all(p_ok(z, a) for a in A) for z in bad), (m, r)
assert all(p_ok(a, b) for a, b in combinations(A, 2))
OUT['lemma3_missing_head_classes'] = 'PASS: 4 mod 15, 1 mod 33, 2 mod 55'

# Section 4 (e=165): class 2 mod 165 has no admissible tail.
assert dom(165, 2) == []
OUT['e165_class2_domain'] = []

# Section 5 (e=55, free prime 3).
D55 = {r: dom(55, r) for r in (3, 24, 25)}
assert states(D55[3], 3) == [(1, 2)]
assert states(D55[24], 3) == [(1, 2)]
assert states(D55[25], 3) == [(0, 0), (0, 2)]
assert not any(q_ok(a, b) and q_ok(a, c) and q_ok(b, c)
               for a in D55[3] for b in D55[24] for c in D55[25])
OUT['e55_states_(parity,mod3)'] = {r: states(D55[r], 3) for r in D55}

# Section 6 (e=33, free prime 5).
D33 = {r: dom(33, r) for r in (22, 3, 4, 15)}
assert states(D33[22], 5) == [(1, 0)]
assert states(D33[3], 5) == [(0, 0), (0, 4)]
assert states(D33[4], 5) == [(1, 1), (1, 2), (1, 3)]
assert states(D33[15], 5) == [(0, 0), (0, 4), (1, 0)]
assert not any(all(q_ok(u, v) for u, v in combinations(t, 2))
               for t in product(D33[22], D33[3], D33[4], D33[15]))
OUT['e33_states_(parity,mod5)'] = {r: states(D33[r], 5) for r in D33}

# Section 7 (e=15, free prime 11): unpinned arc consistency over all classes.
D0 = {r: dom(15, r) for r in range(15)}
OUT['e15_initial_domain_sizes'] = [len(D0[r]) for r in range(15)]
D15 = {r: list(D0[r]) for r in range(15)}
changed = True
while changed:
    changed = False
    for r in range(15):
        for s in range(15):
            if r != s:
                keep = [z for z in D15[r] if any(q_ok(z, w) for w in D15[s])]
                if len(keep) != len(D15[r]):
                    D15[r], changed = keep, True
pred = {r: [z for z in T330 if z % 15 == r and z % 2 == (1 if r % 3 == 1 else 0)
            and z % 11 == G[r % 5]] for r in range(15)}
assert all(len(pred[r]) == 1 for r in range(15))
assert D15 == pred
S = sorted(pred[r][0] for r in range(15))
assert set(Y) <= set(S) and all(q_ok(u, v) for u, v in combinations(S, 2))
assert sorted({z % 55 for z in S}) == [0, 1, 7, 13, 14]
OUT['e15_fixpoint_types_mod330'] = S

# Mirror of the six written steps of Lemma 4.
assert all(z % 2 == 1 for r in range(15) if r % 3 == 1 for z in D0[r])          # step 1
assert [z % 11 for z in D0[10]] == [0] and [z % 11 for z in D0[4]] == [3]       # step 2
ref = [D0[10][0], D0[4][0], 1, 7, 13]          # odd references, r mod 5 = 0,4,1,2,3
E = {r: [z for z in D0[r] if z % 2 == 0 and all(q_ok(z, w) for w in ref)]
     for r in range(15) if r % 3 != 1}
assert all(len(E[r]) == 1 and E[r][0] % 11 == G[r % 5] for r in E)              # step 3
assert all(z % 2 == 0 for z in D0[5] + D0[9])                                    # step 4
for r in E:                                                                      # step 5
    assert all(not (q_ok(z, E[5][0]) and q_ok(z, E[9][0]))
               for z in D0[r] if z % 2 == 1), r
for r in range(15):                                                              # step 6
    if r % 3 == 1:
        r0 = next(s for s in range(15) if s % 3 == 0 and s % 5 == r % 5)
        assert all(z % 11 == G[r % 5] for z in D0[r] if q_ok(z, E[r0][0])), r
OUT['lemma4_steps'] = 'PASS: steps 1-6'


# Lemma 5 and Lemma 6: exact polynomial arithmetic.
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


W = [(2 if z % 2 == 0 else 1) if z % 55 in (0, 1, 7, 13, 14) else 0 for z in range(110)]
fold = [0] * 110
for z in S:
    fold[z % 110] += 1
assert fold == W                              # Q folded mod 110 when |Q|=15 (b=0)
nonzero = {}
for m in (1, 2, 5, 10, 11, 22, 55, 110):
    nonzero[m] = any(pdivmod(W, cyclo(m))[1])
assert all(nonzero[m] for m in (11, 22, 55, 110))
assert not nonzero[5] and not nonzero[10]
Yp = [1 if i in Y else 0 for i in range(15)]
assert any(pdivmod(Yp, cyclo(55))[1]) and any(pdivmod(Yp, cyclo(11))[1])
prod = [1]
for m in (11, 22, 55, 110):
    prod = pmul(prod, list(cyclo(m)))
assert prod == [1 if i % 10 == 0 else 0 for i in range(101)]
OUT['lemma5_W_nonzero_mod_Phi_m'] = nonzero
OUT['lemma6_Phi11_Phi22_Phi55_Phi110'] = '1+X^10+...+X^100'

# Final P-side certificate: x' = 1 mod 110 against old heads 0 and 8.
assert 11 % 10 == 1 % 10 and 1 % 11 == 1
X1 = [z for z in T330 if z % 110 == 1]
assert [z % 3 for z in X1 if p_ok(z, 0)] == [0]
assert [z % 3 for z in X1 if p_ok(z, 8)] == [2]
assert all(not (p_ok(z, 0) and p_ok(z, 8)) for z in X1)
OUT['final_certificate'] = 'x=1 mod 110: (SP) with 0 forces x=0 mod 3, with 8 forces x=2 mod 3'


# Bounded actual-gcd diagnostics, t=1..6 (written lemma covers every t).
def crt(rems, mods):
    x, M = 0, 1
    for r, m in zip(rems, mods):
        k = ((r - x) * pow(M, -1, m)) % m
        x, M = x + M * k, M * m
    return x % M


diag = {}
for t in range(1, 7):
    n = 165 * 2 ** t
    GY = {gcd(a - b, n) for a, b in combinations(Y, 2)}
    GA = {gcd(a - b, n) for a, b in combinations(A, 2)}
    assert 1 in GY and QBAN <= GA
    Ph = [x for x in range(n) if all(x == a or gcd(x - a, n) not in GY for a in A)]
    assert not any(x % 15 == 4 or x % 33 == 1 or x % 55 == 2 for x in Ph)
    Qt = [x for x in range(n) if all(x == y or gcd(x - y, n) not in GA for y in Y)]
    assert not any(x % 165 == 2 for x in Qt)
    for e, rs in ((55, (3, 24, 25)), (33, (22, 3, 4, 15)), (15, range(15))):
        for r in rs:
            assert {x % 330 for x in Qt if x % e == r} <= set(dom(e, r)), (t, e, r)
    diag[n] = {'GY': sorted(GY), 'GA': sorted(GA), 'P_screen': len(Ph), 'Q_screen': len(Qt)}
OUT['bounded_actual_gcd_diagnostics'] = diag

# Positive Q-only control at n=2640: Lemma 4's structure is jointly consistent.
n = 2640
GA = {gcd(a - b, n) for a, b in combinations(A, 2)}
ctrl = []
for r in range(15):
    par = 1 if r % 3 == 1 else 0
    ctrl.append(crt([r, G[r % 5], r if r in Y else par], [15, 11, 16]))
assert len(set(ctrl)) == 15 and set(Y) <= set(ctrl)
assert sorted(x % 15 for x in ctrl) == list(range(15))
assert sorted(x % 330 for x in ctrl) == S
assert all(gcd(u - v, n) not in GA for u, v in combinations(ctrl, 2))
OUT['Q_only_control_n2640'] = sorted(ctrl)

# Positive P-side type controls: each old-head constraint on x=1 mod 110 is
# individually satisfiable; only their conjunction fails.
assert any(p_ok(z, 0) for z in X1) and any(p_ok(z, 8) for z in X1)
OUT['result'] = 'PASS'
print(json.dumps(OUT, indent=1, sort_keys=True, default=str))

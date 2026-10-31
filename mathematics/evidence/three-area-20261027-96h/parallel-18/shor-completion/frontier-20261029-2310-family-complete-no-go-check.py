#!/usr/bin/env python3
"""Exact finite checks for frontier-20261029-2310-family-complete-no-go-v1.md.

The all-k argument is written in the packet. This script checks only the
finite arithmetic facts the packet quotes, plus non-vacuity controls.
It uses Python integers, math.gcd and finite loops; no solver, no sampling.
"""
import json
from math import gcd
from itertools import combinations

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
OUT = {}


def divisors(m):
    return [d for d in range(1, m + 1) if m % d == 0]


def div_set(S, M):
    return {gcd((x - y) % M, M) for x in S for y in S}


def is_tiling(S, T, M):
    if len(S) * len(T) != M:
        return False
    return len({(s + t) % M for s in S for t in T}) == M


# 1. Literal differences of the anchors.
dA = {x - y for x in A for y in A if x != y}
dY = {x - y for x in Y for y in Y if x != y}
assert sorted({abs(d) for d in dA if d % 2}) == [3, 5, 11]
assert sorted({abs(d) for d in dA if d % 2 == 0}) == [8]
assert sorted({abs(d) for d in dY if d % 2}) == [1, 7, 13]
assert sorted({abs(d) for d in dY if d % 2 == 0}) == [6, 12, 14]
assert (3 - 0, 8 - 3, 11 - 0, 1 - 0) == (3, 5, 11, 1)
OUT['odd_A_differences'] = [3, 5, 11]
OUT['odd_Y_differences'] = [1, 7, 13]

# 2. Lemma 1 / Lemma 1' arithmetic at n = 1155*2^K (bounded K; symbolic in packet).
for K in range(1, 41):
    n = 1155 * 2 ** K
    for p in (3, 5, 11):
        assert gcd(p * (1 - 0), n) == p          # in Div(pY)
    assert (gcd(3, n), gcd(5, n), gcd(11, n)) == (3, 5, 11)   # in Div(A)
    assert gcd(2 * 3, n) == gcd(7 - 1, n) == 6   # |P| even
    assert gcd(1 - 0, n) == 1                      # 1 in Div(Y)
    assert 7 not in div_set(A, n)                 # Lemma 1 cannot force 7 into |Q|
OUT['lemma1_bounded_K'] = [1, 40]

# 3. Lemma 2 (Q-rule) divisor enumeration.
# Odd x with gcd(x,n)=g, g | 1155. Forbidden iff g = t*delta, delta in {3,5,11},
# t | 1155 coprime to |P|.
odd_divs = divisors(1155)
forb_pow2 = [g for g in odd_divs
             if any(g % d == 0 and gcd(g // d, 2) == 1 for d in (3, 5, 11))]
assert forb_pow2 == [g for g in odd_divs if gcd(g, 165) > 1]
forb_7 = [g for g in odd_divs
          if any(g % d == 0 and gcd(g // d, 7) == 1 for d in (3, 5, 11))]
assert forb_7 == [g for g in odd_divs if gcd(g, 165) > 1 and g % 7]
OUT['qrule_case_a_forbidden_odd_gcds'] = forb_pow2
OUT['qrule_case_b_forbidden_odd_gcds'] = forb_7

# 4. Class 6 mod 165 (case |P| = 2^a).
assert (6 % 3, 6 % 5) == (0, 1)
for q in range(6, 6 + 2 * 165 * 12, 165):   # representatives of both parities
    if q % 2:
        assert gcd(q - 0, 165) == 3
    else:
        assert gcd(q - 1, 165) == 5
OUT['class6'] = 'PASS'

# 5. {3,5} generates Z_165; connectivity of the fibre graph r ~ r+3, r+5.
reach = {0}
frontier = [0]
while frontier:
    x = frontier.pop()
    for s in (3, -3, 5, -5):
        y = (x + s) % 165
        if y not in reach:
            reach.add(y)
            frontier.append(y)
assert len(reach) == 165
assert gcd(3, 165) == 3 and gcd(5, 165) == 5
OUT['steps_3_5_generate_Z165'] = True

# 6. Cross-lemma gcd identities (packet section 6, step 6).
for x in range(1155):
    assert gcd(7 * x, 1155) == 7 * gcd(x, 165)
for y in range(0, 1155, 7):
    gy = gcd(y, 165)
    for h in divisors(165):
        if h % gy == 0:
            assert gcd(h * y, 1155) == 7 * h
OUT['cross_lemma_identities'] = 'PASS'

# 7. Lemma H control: exhaustive over all E/O partitions that are g-periodic,
# g in {3,5,11,15}; H must be connected. (The packet's proof covers every proper g.)
def crt(r):
    return (r % 3, r % 5, r % 11)


def H_connected(E):
    parent = list(range(165))

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    coords = [crt(r) for r in range(165)]
    for c in range(3):
        groups = {}
        for r in range(165):
            groups.setdefault(coords[r][c], []).append(r)
        for members in groups.values():
            ins = [r for r in members if r in E]
            outs = [r for r in members if r not in E]
            if ins and outs:
                for r in members:
                    parent[find(r)] = find(members[0])
    return len({find(r) for r in range(165)}) == 1


lemmaH = {}
for g in (3, 5, 11, 15):
    count = 0
    for mask in range(1, 2 ** g - 1):
        Eg = {c for c in range(g) if mask >> c & 1}
        E = {r for r in range(165) if r % g in Eg}
        assert H_connected(E), (g, sorted(Eg))
        count += 1
    lemmaH[g] = count
OUT['lemmaH_exhaustive_partitions'] = lemmaH
# A partition with full period 165 can disconnect H, so only proper periods are claimed.
assert not H_connected({0})
OUT['lemmaH_scope'] = 'proper periods connected; period-165 partition {0} is disconnected'

# 8. Fibres and residues of the anchors.
assert len({y % 165 for y in Y}) == 5
assert [y % 2 for y in Y] == [0, 1, 1, 1, 0]
assert [y % 7 for y in Y] == [0, 1, 0, 6, 0]
assert [a % 7 for a in A] == [0, 3, 1, 4]
for r in (0, 14):
    for s in (1, 7, 13):
        assert (r - s) % 165 != 0
OUT['anchor_residues'] = 'PASS'

# 9. Final contradiction arithmetic: p0 = 0 mod 1155 odd, 8 - p0.
assert gcd(8, 1155) == 1 and 8 % 7 == 1
for K in range(1, 41):
    n = 1155 * 2 ** K
    for j in range(1, 2 ** min(K, 6), 2):          # odd multiples of 1155 below n
        p0 = (1155 * j) % n
        assert p0 % 2 == 1
        assert gcd((8 - p0) % n, n) == 1
OUT['final_step'] = 'PASS'

# 10. Non-vacuity controls: without anchors every cardinality case tiles.
ctl = []
for K in range(1, 5):
    n = 1155 * 2 ** K
    for a in range(0, K + 1):
        for oddP in (1, 7):
            sP = oddP * 2 ** a
            P = list(range(sP))
            Q = [sP * j for j in range(n // sP)]
            assert is_tiling(P, Q, n)
            assert div_set(P, n) & div_set(Q, n) == {n}
            ctl.append([n, sP])
OUT['unanchored_tilings_exist'] = len(ctl)

# 11. Positive control of Sands and Tijdeman on all tilings of small Z_m
# with 0 in both factors.
tij = {}
for m in (12, 18):
    subsets = {}
    for d in divisors(m):
        if d in (1, m):
            continue
        subsets[d] = [((0,) + c, div_set((0,) + c, m))
                      for c in combinations(range(1, m), d - 1)]
    nt = 0
    for d in subsets:
        for Aset, DA in subsets[d]:
            for Bset, DB in subsets[m // d]:
                til = is_tiling(Aset, Bset, m)
                assert til == (DA & DB == {m})
                if til:
                    nt += 1
                    for t in range(1, m):
                        if gcd(t, d) == 1:
                            assert is_tiling([t * x % m for x in Aset], Bset, m)
    tij[m] = nt
OUT['sands_tijdeman_control_tilings'] = tij

OUT['result'] = 'PASS'
if __name__ == '__main__':
    print(json.dumps(OUT, indent=1, sort_keys=True))

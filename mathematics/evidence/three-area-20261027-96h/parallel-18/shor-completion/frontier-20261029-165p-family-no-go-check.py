#!/usr/bin/env python3
"""Exact finite checks for frontier-20261029-165p-family-no-go-v1.md.

The all-p, all-K argument is written in the packet. This script checks the
finite arithmetic facts it quotes for a bounded range of primes p, plus
small-model controls of the Tijdeman/CRT dichotomy step.
Only Python integers, math.gcd and finite loops; no solver, no sampling.
"""
import json
from math import gcd

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
OUT = {}


def primes_upto(m):
    return [q for q in range(2, m + 1) if all(q % r for r in range(2, int(q ** 0.5) + 1))]


def divisors(m):
    return [x for x in range(1, m + 1) if m % x == 0]


def is_tiling(S, T, M):
    return len(S) * len(T) == M and len({(s + t) % M for s in S for t in T}) == M


PR = [q for q in primes_upto(200) if q >= 7 and q != 11]
OUT['primes_checked'] = [PR[0], PR[-1], len(PR)]

# 1. Anchor facts used for every p.
assert sorted({abs(x - y) for x in A for y in A if (x - y) % 2}) == [3, 5, 11]
assert sorted({abs(x - y) for x in Y for y in Y if (x - y) % 2}) == [1, 7, 13]
for p in PR:
    for e in (1, 2):
        pe = p ** e
        assert 0 % p != 1 % p
        assert gcd(8, 165 * pe) == 1
OUT['anchor_facts'] = 'PASS'

# 2. Lemma 1 and the tail rule (S1) for |P| = p^e 2^a, at n = 165 p^e 2^K.
#    Odd divisors g of 165 p^e: forbidden (Lemma 2) iff some l in {3,5,11}
#    divides g with g/l coprime to p.  Claim: iff gcd(g,165)>1 and p does not divide g.
for p in PR:
    for e in (1, 2):
        for K in (1, 2, 5):
            n = 165 * p ** e * 2 ** K
            for l in (3, 5, 11):
                assert gcd(l, n) == l
        for g in divisors(165 * p ** e):
            forb = any(g % l == 0 and gcd(g // l, p) == 1 for l in (3, 5, 11))
            assert forb == (gcd(g, 165) > 1 and g % p != 0)
OUT['tail_rule_S1'] = 'PASS'

# 3. (S6) gcd identities, exhaustively over residues, for p <= 37, e in {1,2}.
for p in [q for q in PR if q <= 37]:
    for e in (1, 2):
        pe = p ** e
        M = 165 * pe
        for x in range(M):
            assert gcd(pe * x, M) == pe * gcd(x, 165)
        for y in range(0, M, pe):
            g0 = gcd(y, 165)
            for h in divisors(165):
                if h % g0 == 0:
                    assert gcd(h * y, M) == pe * h
OUT['S6_identities_p_upto_37'] = 'PASS'

# 4. Lemma 3 class 6 and steps 3,5 generating Z_165.
assert (6 % 3, 6 % 5) == (0, 1)
seen, stack = {0}, [0]
while stack:
    u = stack.pop()
    for s in (3, -3, 5, -5):
        v = (u + s) % 165
        if v not in seen:
            seen.add(v)
            stack.append(v)
assert len(seen) == 165
OUT['class6_and_generation'] = 'PASS'

# 5. Small-model control of (S3) steps 3-5: every tiling V + P = Z_N with
#    N = 7*2^K (K=1,2), 0 in both, |V| a power of 2.
def tilings_with(V, N):
    """All P with 0 in P and P + V = Z_N (exact cover by backtracking)."""
    sols = []
    Vs = sorted(V)

    def rec(cov, chosen):
        if len(cov) == N:
            sols.append(tuple(sorted(chosen)))
            return
        c = min(x for x in range(N) if x not in cov)
        for v in Vs:
            p0 = (c - v) % N
            tile = {(p0 + w) % N for w in Vs}
            if tile & cov:
                continue
            rec(cov | tile, chosen + [p0])

    rec(set(Vs), [0])
    return sorted(set(sols))


from itertools import combinations
ctrl = {}
for K in (1, 2):
    N = 7 * 2 ** K
    count = 0
    for b in range(0, K + 1):
        for rest in combinations(range(1, N), 2 ** b - 1):
            V = (0,) + rest
            for P in tilings_with(V, N):
                assert is_tiling(P, V, N)
                V7 = [7 * v % N for v in V]
                assert len(set(V7)) == len(V) and is_tiling(P, V7, N)   # Tijdeman control
                for gam in range(7):
                    Pg = [x for x in P if x % 7 == gam]
                    A2 = {x % 2 ** K for x in Pg}
                    B2 = {x % 2 ** K for x in V7}
                    assert len(A2) == len(Pg) and is_tiling(sorted(A2), sorted(B2), 2 ** K)
                    podd = len({x % 2 for x in Pg}) == 2
                    vodd = len({x % 2 for x in V}) == 2
                    assert podd != vodd          # exactly one factor has both parities
                count += 1
    ctrl[N] = count
OUT['dichotomy_small_model_tilings'] = ctrl

# 6. Non-vacuity: without anchors every split |P| in {2^a, p 2^a} tiles.
cnt = 0
for p in (7, 13, 17):
    for K in (1, 2):
        n = 165 * p * 2 ** K
        for a in range(K + 1):
            for oddP in (1, p):
                sP = oddP * 2 ** a
                assert is_tiling(list(range(sP)), [sP * j for j in range(n // sP)], n)
                cnt += 1
OUT['unanchored_tilings_exist'] = cnt

OUT['result'] = 'PASS'
if __name__ == '__main__':
    print(json.dumps(OUT, indent=1, sort_keys=True))

#!/usr/bin/env python3
"""Integer/Fraction controls for the single-small-shared-prime written candidate.

No previous author checker output is loaded. All arithmetic is exact. The
universal proof and the named LL/T2 import are not established by these controls.
"""
import json
from fractions import Fraction
from functools import lru_cache
from math import gcd

S = (3, 5, 11)
OUT = {}


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def trim(poly):
    ans = list(poly)
    while len(ans) > 1 and ans[-1] == 0:
        ans.pop()
    return ans


def mul(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                ans[i + j] += x * y
    return trim(ans)


def divmonic(a, b):
    a, b = trim(a), trim(b)
    assert b[-1] == 1
    if len(a) < len(b):
        return [0], a
    ans = [0] * (len(a) - len(b) + 1)
    for i in range(len(a) - len(b), -1, -1):
        c = a[i + len(b) - 1]
        ans[i] = c
        for j, y in enumerate(b):
            a[i + j] -= c * y
    return trim(ans), trim(a)


@lru_cache(None)
def cyclo(n):
    ans = [-1] + [0] * (n - 1) + [1]
    for d in divisors(n):
        if d < n:
            ans, rem = divmonic(ans, cyclo(d))
            assert rem == [0]
    return tuple(ans)


def tiling(P, Q, n):
    return len(P) * len(Q) == n and len({(p + q) % n for p in P for q in Q}) == n


# 1. The odd-difference rule: if either other small prime divides odd x,
# then failure of p^2|x is witnessed by an admissible dilation of an A-difference.
rule_count = 0
for p in S:
    other = [q for q in S if q != p]
    base = other[0] * other[1]
    for R in (base, base * other[0]):
        assert gcd(R, 2 * p) == 1
        for exponent in (2, 3):
            for K in (1, 2, 4):
                n = (1 << K) * p ** exponent * R
                for x in range(1, 2 * p ** exponent * R, 2):
                    if not any(x % q == 0 for q in other) or x % (p * p) == 0:
                        continue
                    delta = next(q for q in other if x % q == 0) if x % p else p
                    g = gcd(x, n)
                    assert g % delta == 0
                    t = g // delta
                    assert gcd(t, 2 * p) == 1
                    assert gcd(t * delta, n) == g < n
                    rule_count += 1
OUT['odd_difference_dilation_witnesses'] = rule_count

# 2. Fractional coset cardinality is impossible, for arbitrary v>=2 in proof.
fractions_count = 0
for p in S:
    for exponent in range(2, 6):
        for a in range(7):
            for b in range(7):
                K = a + b
                if K == 0:
                    continue
                subgroup_order = p ** (exponent - 2) * (1 << K)
                fibre_size = p ** (exponent - 1) * (1 << b)
                count = Fraction(subgroup_order, fibre_size)
                assert count == Fraction(1 << a, p) and count.denominator == p
                fractions_count += 1
OUT['nonintegral_coset_cardinalities'] = fractions_count

# 3. Phi_p * Phi_p^2 = 1+...+X^(p^2-1), used to force Q to own one low factor.
# Also product_{m|R} Phi_(s*m)(X) = Phi_s(X^R) when gcd(s,R)=1.
products = []
nonzero_count = 0
for p in S:
    other = [q for q in S if q != p]
    R = other[0] * other[1]
    assert mul(cyclo(p), cyclo(p * p)) == [1] * (p * p)
    for s in (p, p * p):
        lhs = [1]
        for m in divisors(R):
            lhs = mul(lhs, cyclo(s * m))
        rhs = [0] * (R * (len(cyclo(s)) - 1) + 1)
        for j, value in enumerate(cyclo(s)):
            rhs[R * j] = value
        assert lhs == rhs
        products.append({'p': p, 's': s, 'R': R, 'degree': len(lhs) - 1})
        # A positive mass in one residue mod p^2 cannot vanish at either low root.
        for c in range(p * p):
            mono = [0] * c + [p]
            assert divmonic(mono, cyclo(s))[1] != [0]
            nonzero_count += 1
OUT['cyclotomic_products'] = products
OUT['single_residue_nonvanishing_controls'] = nonzero_count

# 4. Positive controls for fibre nonconstancy: both low cyclotomic choices
# occur in real unanchored tilings, and the R-fibres have multiple p^2 residues.
positive = []
for p in S:
    other = [q for q in S if q != p]
    R = other[0] * other[1]
    n = p * p * R
    for step in (1, p):
        Q = [r + R * step * j for r in range(R) for j in range(p)]
        P = [R * p * j for j in range(p)] if step == 1 else [R * j for j in range(p)]
        assert tiling(P, Q, n)
        for r in range(R):
            fibre = [q for q in Q if q % R == r]
            assert len({q % (p * p) for q in fibre}) == p
        positive.append({'p': p, 'R': R, 'step': step})
OUT['unanchored_low_cyclotomic_controls'] = positive

# 5. The unrestricted agreement graph on Z_R is connected by steps q1,q2.
connections = []
for p in S:
    q1, q2 = [q for q in S if q != p]
    for R in (q1 * q2, q1 * q1 * q2, 13 * q1 * q2):
        seen, stack = {0}, [0]
        while stack:
            u = stack.pop()
            for step in (q1, -q1, q2, -q2):
                v = (u + step) % R
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        assert len(seen) == R
        connections.append({'p': p, 'R': R, 'vertices': len(seen)})
OUT['agreement_graph_connections'] = connections
OUT['result'] = 'PASS'
if __name__ == '__main__':
    print(json.dumps(OUT, indent=1, sort_keys=True))

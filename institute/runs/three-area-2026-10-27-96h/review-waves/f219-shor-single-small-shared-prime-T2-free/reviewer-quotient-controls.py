#!/usr/bin/env python3
"""Exact synthetic controls of the reviewer-reconstructed fibre quotient."""
from math import gcd


def counts(n, a, b):
    result = [0] * n
    for x in a:
        for y in b:
            result[(x + y) % n] += 1
    return result


fibres = 0
for p in (3, 5, 11):
    q1, q2 = [q for q in (3, 5, 11) if q != p]
    rsize = q1 * q2
    v, k = 2, 1
    n = 2 ** k * p ** v * rsize
    N = n // rsize
    for a in (0, 1):
        b = k - a
        width = p * 2 ** a
        P = tuple(range(width))
        Q = tuple(range(0, n, width))
        assert counts(n, P, Q) == [1] * n
        assert not ({0, 3, 8, 11} <= set(P) and {0, 1, 7, 13, 14} <= set(Q))
        assert gcd(rsize, len(P)) == 1
        scaled = tuple((rsize * x) % n for x in P)
        assert len(set(scaled)) == len(P)
        assert counts(n, scaled, Q) == [1] * n
        Pbar = tuple(x % N for x in P)
        for r in range(rsize):
            Qr = tuple(q for q in Q if q % rsize == r)
            assert len(Qr) == p ** (v - 1) * 2 ** b
            Vr = tuple(((q - r) // rsize) % N for q in Qr)
            assert len(set(Vr)) == len(Qr)
            assert counts(N, Pbar, Vr) == [1] * N
            assert len({q % (p * p) for q in Qr}) > 1
            if a == 0:
                even = next(q for q in Qr if q % 2 == 0)
                odd = next(q for q in Qr if q % 2 == 1)
                delta = even - odd
                assert delta % 2 and delta % q1 == 0 and delta % (p * p) != 0
            else:
                assert all(q % 2 == 0 for q in Qr)
            fibres += 1

# Without gcd(R,|P|)=1, dilation may fail and the uniform fibre count may fail.
n, R = 18, 3
P = (0, 1, 2)
Q = tuple(range(0, n, 3))
assert counts(n, P, Q) == [1] * n
assert gcd(R, len(P)) != 1
scaled = tuple((R * x) % n for x in P)
assert counts(n, scaled, Q) != [1] * n
assert [sum(q % R == r for q in Q) for r in range(R)] == [6, 0, 0]

print('quotient controls: synthetic unanchored tilings=6; fibres=', fibres)
print('all fibres: exact cardinality, direct quotient tiling and nonconstancy modulo p^2')
print('a=0 negatives: mixed parity has an odd q1-divisible difference not divisible by p^2; anchors absent')
print('a=1 negatives: every fibre even; the anchor 1 in Q is absent')
print('dilation negative: n=18,R=3,|P|=3 produces fibre counts 6,0,0 and a failed scaled tiling')
print('ALL REVIEWER QUOTIENT CONTROLS COMPLETED')

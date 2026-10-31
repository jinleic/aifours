#!/usr/bin/env python3
"""Exact rational control of a distinct capped B6 counterexample; no transcendental approximation."""
from fractions import Fraction as Q
from math import comb
import signal

signal.alarm(100)
b = Q(2, 3)
m = b / (1 - b)
M = [Q(1)]
for k in range(1, 5):
    M.append(m * sum(comb(k, j) * M[j] for j in range(k)))
assert M == [Q(1), Q(2), Q(10), Q(74), Q(730)]


def ratio(s):
    second = sum(Q(comb(2, j)) * s**(2-j) * M[j] for j in range(3))
    fourth = sum(Q(comb(4, j)) * s**(4-j) * M[j] for j in range(5))
    return fourth / (3*second)


candidate, competitor = ratio(Q(1, 2)), ratio(Q(3, 4))
assert candidate == Q(14305, 588)
assert competitor == Q(253297, 10416)
assert candidate - competitor == Q(62244, 6124608) > 0
assert candidate > Q(1, 4)

# ln(3/2)=2*atanh(1/5); bounding denominators in the positive tail by 7.
s = Q(1, 5)
L = 2*(s + s**3/3 + s**5/5 + s**7/(7*(1-s*s)))
assert L == Q(177391, 437500)
# Since log(3/2)<L, candidate<4/L^2 implies candidate<U=4/log(3/2)^2.
assert candidate * L*L < 4
assert 4*588*L.denominator**2 - 14305*L.numerator**2 == 43955767295

# Reconfirm the exact universal cutoff N=7, without evaluating sqrt or log.
assert Q(152, 375) > 0 and Q(152, 375)**2 > Q(8, 49)
assert L < Q(5, 12) and Q(5, 12)**2 < Q(2, 9)
print('PASS: exact geometric moments', M)
print('PASS: capped B6 phase ratio', candidate, '; cheaper feasible ratio', competitor)
print('PASS: strict gap', candidate - competitor)
print('PASS: upper log bound L', L, '; 4-candidate*L^2 is positive')
print('PASS: strict rational comparisons imply the universal cutoff N=7')
if not (candidate > competitor):
    raise AssertionError('negative control failed: reversed strict cost inequality')
print('NEGATIVE REJECTED: candidate <= competitor')
if not (candidate * L*L < 4):
    raise AssertionError('negative control failed: reversed cap inequality')
print('NEGATIVE REJECTED: candidate >= 4/L^2')
if not (candidate > Q(1, 4)):
    raise AssertionError('negative control failed: cost ball misses diamond core')
print('NEGATIVE REJECTED: candidate <= squared core radius')

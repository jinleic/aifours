#!/usr/bin/env python3
"""Exact finite controls for the all-powers-of-three head obstruction.
Only integer arithmetic; no solver, sampling, floats or previous output files.
"""
import json
from itertools import product
from math import gcd

Y = (0, 1, 7, 13, 14)
FORBIDDEN = {3, 5, 11, 15, 33, 55, 165}


def compatible(x, y):
    if (x - y) % 2 == 0:
        return True
    return gcd(x - y, 495) not in FORBIDDEN


def coordinate_rule(x, y):
    if (x - y) % 2 == 0:
        return True
    if (x - y) % 3 == 0 and (x - y) % 9:
        return False
    if ((x - y) % 5 == 0 or (x - y) % 11 == 0) and (x - y) % 9:
        return False
    return True


for x in range(990):
    for y in range(990):
        assert compatible(x, y) == coordinate_rule(x, y)

assert not any(x % 2 == 0 and x % 3 == 1 and all(compatible(x, y) for y in Y)
               for x in range(990))
D = {r: [x for x in range(990) if x % 55 == r and all(compatible(x, y) for y in Y)]
     for r in (3, 25, 45)}
states = {r: sorted({(x % 2, x % 9) for x in D[r]}) for r in D}
assert states == {3: [(1, 5)], 25: [(0, 0), (0, 2), (0, 3), (0, 5), (0, 6), (0, 8)], 45: [(1, 0)]}
assert not any(compatible(a, b) and compatible(a, c) and compatible(b, c)
               for a, b, c in product(D[3], D[25], D[45]))
# Direct certificate of the final contradiction.
assert (25 - 3) % 11 == 0
assert (25 - 45) % 5 == 0
assert 0 != 5

# Bounded all-exponent arithmetic controls: every forbidden odd difference
# has a dilation t coprime to 3*2 that matches one of A's 3,5,11 differences.
count = 0
for e in range(1, 5):
    for K in range(1, 5):
        for v in (e + 1, e + 2):
            for R in (55, 275, 605, 715):
                n = (1 << K) * 3 ** v * R
                for x in range(1, 990, 2):
                    forbidden = (x % 3 == 0 and x % 9 != 0) or (
                        (x % 5 == 0 or x % 11 == 0) and x % 9 != 0)
                    if not forbidden:
                        continue
                    if x % 3 == 0:
                        delta = 3
                    else:
                        delta = 5 if x % 5 == 0 else 11
                    g = gcd(x, n)
                    assert g % delta == 0
                    t = g // delta
                    assert gcd(t, 6) == 1
                    assert gcd(t * delta, n) == g < n
                    count += 1

print(json.dumps({'result': 'PASS',
                  'type_pair_comparisons': 990 * 990,
                  'class_states_parity_mod9': states,
                  'compatible_class_triples': 0,
                  'generic_dilation_controls': count,
                  'scope': 'finite arithmetic only; all-order proof is written'}, indent=1, sort_keys=True))

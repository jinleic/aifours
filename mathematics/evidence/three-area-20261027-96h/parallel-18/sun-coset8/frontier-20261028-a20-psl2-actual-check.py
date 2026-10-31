#!/usr/bin/env python3
"""Exact PGL-coordinate control for PSL2(19) acting inside A20."""

from math import factorial

p = 19
infinity = p
matrices = set()
for a in range(p):
    for b in range(p):
        for c in range(p):
            if a:
                ds = ((1+b*c)*pow(a, -1, p) % p,)
            elif (-b*c) % p == 1:
                ds = range(p)
            else:
                continue
            for d in ds:
                matrix = (a, b, c, d)
                negated = tuple((-x) % p for x in matrix)
                matrices.add(min(matrix, negated))
assert len(matrices) == 3420


def image(matrix, x):
    a, b, c, d = matrix
    if x == infinity:
        return a*pow(c, -1, p) % p if c else infinity
    denominator = (c*x+d) % p
    return (a*x+b)*pow(denominator, -1, p) % p if denominator else infinity


def is_even(perm):
    seen = set()
    cycles = 0
    for start in range(len(perm)):
        if start not in seen:
            cycles += 1
            pos = start
            while pos not in seen:
                seen.add(pos)
                pos = perm[pos]
    return (len(perm)-cycles) % 2 == 0


actions = {tuple(image(m, x) for x in range(p+1)) for m in matrices}
assert len(actions) == 3420
assert all(set(action) == set(range(p+1)) and is_even(action) for action in actions)
translation = tuple((x+1) % p if x < p else infinity for x in range(p+1))
assert translation in actions and translation[infinity] == infinity
assert all(translation[x] != x for x in range(p))
assert {action[infinity] for action in actions} == set(range(p+1))
a19 = factorial(19)//2
a20 = factorial(20)//2
assert a19 % len(actions) == 0
assert a20 % len(actions) == 0 and (a20//len(actions)) % 20 == 0
print("PSL2(19): 3420 distinct projective actions, all even, transitive on 20 points")
print("translation fixes infinity and is a 19-cycle; index in A20 is divisible by 20")
print("PASS: exact finite construction only, no alternating classification verified")

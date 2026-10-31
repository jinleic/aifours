#!/usr/bin/env python3
"""Exact permutation construction disproving an all-n no-three subgroup claim."""

from collections import deque
from math import gcd


identity = tuple(range(5))


def permutation(*cycles):
    result = list(identity)
    for cycle in cycles:
        z = [x-1 for x in cycle]
        for i, x in enumerate(z):
            result[x] = z[(i+1) % len(z)]
    return tuple(result)


def compose(a, b):
    return tuple(a[b[i]] for i in range(5))


def generated(generators):
    seen = {identity}
    todo = deque([identity])
    while todo:
        current = todo.popleft()
        for generator in generators:
            nxt = compose(current, generator)
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return seen


def even(p):
    return sum(p[i] > p[j] for i in range(5) for j in range(i+1, 5)) % 2 == 0


subgroups = (
    generated((permutation((1, 2, 3)), permutation((1, 2, 4)))),
    generated((permutation((1, 2, 3, 4, 5)), permutation((2, 5), (3, 4)))),
    generated((permutation((1, 2), (3, 4)), permutation((1, 3), (2, 4)))),
    generated((permutation((1, 2, 3)),)),
)
assert tuple(map(len, subgroups)) == (12, 10, 4, 3)
assert all(even(g) for subgroup in subgroups for g in subgroup)
indices = tuple(60//len(group) for group in subgroups)
assert indices == (5, 6, 15, 20)
assert all(gcd(a, b) <= 7 for i, a in enumerate(indices) for b in indices[i+1:])
assert len(generated((permutation((1, 2, 3, 4, 5)), identity))) == 5
print(f"PASS: actual even-permutation subgroup orders={[len(g) for g in subgroups]}, indices={indices}")
print("The identity-generator mutation changes D10 order to 5 as intended")

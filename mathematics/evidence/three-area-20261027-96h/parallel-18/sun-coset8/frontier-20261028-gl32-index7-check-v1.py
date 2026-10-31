#!/usr/bin/env python3
"""Exact arithmetic witness and normal-class proof for GL(3,2)."""
from collections import Counter
from itertools import combinations, product


def act(A, x):
    return sum(((row & x).bit_count() & 1) << k for k, row in enumerate(A))


def compose(A, B):
    return tuple((B[0] if row & 1 else 0) ^ (B[1] if row & 2 else 0) ^ (B[2] if row & 4 else 0) for row in A)


def element_order(A):
    power = (1, 2, 4)
    for k in range(1, 169):
        power = compose(power, A)
        if power == (1, 2, 4):
            return k
    raise ValueError("element order exceeds group order")


def run():
    G = [A for A in product(range(8), repeat=3) if {act(A, x) for x in range(1, 8)} == set(range(1, 8))]
    if len(G) != 168:
        raise ValueError("group order")
    centralizers = [sum(compose(A, B) == compose(B, A) for B in G) for A in G]
    if any(168 % c for c in centralizers):
        raise ValueError("centralizer size")
    frequencies = Counter((168 // c, element_order(A)) for A, c in zip(G, centralizers))
    expected = {(1, 1): 1, (21, 2): 21, (24, 7): 48, (42, 4): 42, (56, 3): 56}
    if frequencies != expected:
        raise ValueError("conjugacy data")
    sizes = [21, 24, 24, 42, 56]
    proper_divisors = {d for d in range(2, 168) if 168 % d == 0}
    for count in range(1, len(sizes) + 1):
        for subset in combinations(sizes, count):
            if 1 + sum(subset) in proper_divisors:
                raise ValueError("possible proper normal order")
    stabilizers, cosets = [], []
    for v in range(1, 8):
        H = {A for A in G if act(A, v) == v}
        if len(H) != 24:
            raise ValueError("stabilizer order")
        stabilizers.append(frozenset(H))
        candidates = {A for A in G if act(A, v) == 1}
        representative = next(iter(candidates))
        if {compose(representative, h) for h in H} != candidates:
            raise ValueError("fiber not left coset")
        cosets.append(candidates)
    if len(set(stabilizers)) != 7:
        raise ValueError("stabilizers not distinct")
    if sum(map(len, cosets)) != 168 or set.union(*cosets) != set(G):
        raise ValueError("cosets do not partition")
    print("PASS order=168; class-size/order frequencies", sorted(frequencies.items()))
    print("PASS no nontrivial proper normal class sum divides 168")
    print("PASS seven distinct order-24 stabilizers, index 7, seven left cosets partition")


if __name__ == "__main__":
    run()

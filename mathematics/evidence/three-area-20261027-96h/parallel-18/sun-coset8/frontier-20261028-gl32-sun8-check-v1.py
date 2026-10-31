#!/usr/bin/env python3
"""Exact GL(3,2) subgroup and six index-seven-coset complement check."""
from collections import Counter
from itertools import combinations, product
from math import gcd


def act(A, x):
    return sum(((row & x).bit_count() & 1) << k for k, row in enumerate(A))


def compose(A, B):
    return tuple((B[0] if row & 1 else 0) ^ (B[1] if row & 2 else 0) ^ (B[2] if row & 4 else 0) for row in A)


def run():
    group = [A for A in product(range(8), repeat=3) if {act(A, x) for x in range(1, 8)} == set(range(1, 8))]
    if len(group) != 168:
        raise ValueError("group order")
    lookup = {A: i for i, A in enumerate(group)}
    table = [[lookup[compose(A, B)] for B in group] for A in group]
    identity = lookup[(1, 2, 4)]

    def generated(gens):
        seen = {identity}
        queue = [identity]
        pos = 0
        while pos < len(queue):
            x = queue[pos]
            pos += 1
            for g in gens:
                y = table[x][g]
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
                    if len(queue) > 24:
                        return None
        return frozenset(seen)

    trivial = frozenset({identity})
    subgroups = {trivial: ()}
    queue = [trivial]
    pos = 0
    while pos < len(queue):
        H = queue[pos]
        pos += 1
        if len(H) == 24:
            continue
        for g in range(168):
            if g in H:
                continue
            generators = subgroups[H] + (g,)
            K = generated(generators)
            if K is not None and K not in subgroups:
                subgroups[K] = generators
                queue.append(K)
    distribution = Counter(map(len, subgroups))
    expected = {1: 1, 2: 21, 3: 28, 4: 35, 6: 28, 7: 8, 8: 21, 12: 14, 21: 8, 24: 14}
    if distribution != expected:
        raise ValueError("subgroup distribution")

    masks = set()
    for H in subgroups:
        if len(H) != 24:
            continue
        for g in range(168):
            mask = 0
            for h in H:
                mask |= 1 << table[g][h]
            masks.add(mask)
    masks = sorted(masks)
    if len(masks) != 98 or any(m.bit_count() != 24 for m in masks):
        raise ValueError("index-seven cosets")
    if len(set(masks[:-1] + [masks[0]])) != 97:
        raise ValueError("duplicate-coset mutation control")
    mask_set = set(masks)
    adjacency = [sum(1 << j for j, b in enumerate(masks) if i != j and not a & b) for i, a in enumerate(masks)]
    whole = (1 << 168) - 1
    leaves = 0

    def find_sixes(candidates, depth, union):
        nonlocal leaves
        if depth == 6:
            leaves += 1
            if whole ^ union not in mask_set:
                raise ValueError("six-coset complement")
            return
        if candidates.bit_count() < 6 - depth:
            return
        while candidates:
            bit = candidates & -candidates
            candidates -= bit
            i = bit.bit_length() - 1
            find_sixes(candidates & adjacency[i], depth + 1, union | masks[i])

    find_sixes((1 << len(masks)) - 1, 0, 0)
    if leaves != 1568:
        raise ValueError("six-coset coverage")
    classes = [[8, 21, 168], [12, 24, 84], [14, 28, 42, 56]]
    expected_divisors = {d for d in range(8, 169) if 168 % d == 0}
    if set(sum(classes, [])) != expected_divisors:
        raise ValueError("divisor coverage")
    if any(2 <= gcd(a, b) <= 7 for c in classes for a, b in combinations(c, 2)):
        raise ValueError("divisor color collision")
    print("PASS proper subgroup sizes", sorted(distribution.items()))
    print("PASS 14 index-seven subgroups, 98 left cosets, 1568 disjoint sixes each extend")
    print("PASS duplicate-coset count control; 3-color partition of all divisors >=8")


if __name__ == "__main__":
    run()

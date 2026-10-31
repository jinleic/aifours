#!/usr/bin/env python3
"""Independent exact squarefree cluster search and cyclic fibre obstruction.

Necessary support constraints overapproximate arbitrary group data. The
cyclic example uses actual finite cosets; neither check proves Sun7.
"""
from math import gcd, prod
from itertools import combinations
import json


PRIMES = (2, 3, 5, 7)
SUPPORTS = tuple(prod(p for j, p in enumerate(PRIMES) if mask & (1 << j))
                 for mask in range(16))


def cluster_search(r):
    counts = [1] + [0] * 8
    first = None
    terminal = 0

    def visit(vals, n7):
        nonlocal first, terminal
        i = len(vals)
        if n7 + (8 - i) < 3:
            return
        if i == 8:
            terminal += 1
            if first is None:
                first = vals
            return
        for ai in SUPPORTS:
            ni = (7 if i < r else 1) * ai
            if all(gcd(ni, (7 if j < r else 1) * aj) <= 7
                   and (i < r and j < r or gcd(ai, aj) >= 2)
                   for j, aj in enumerate(vals)):
                counts[i + 1] += 1
                visit(vals + (ai,), n7 + (ni % 7 == 0))

    visit((), 0)
    return {"r": r, "partial_counts_before_seven_prune": counts,
            "terminal_models": terminal, "first": first}


def cyclic_obstruction():
    modulus = 210
    indices_ = (14, 21, 35, 30)
    offsets = (0, 15, 30, 1)
    cosets = [{x for x in range(modulus) if x % n == a % n}
              for n, a in zip(indices_, offsets)]
    pair_intersections = [len(cosets[i] & cosets[j]) for i, j in combinations(range(4), 2)]
    pair_gcds = [gcd(indices_[i], indices_[j]) for i, j in combinations(range(4), 2)]
    images = [{x % 30 for x in c} for c in cosets]
    joint = sorted(images[0] & images[1] & images[2])
    outside = sorted(images[3])
    bad_outside = {x for x in range(modulus) if x % 30 == 0}
    bad_cluster = {x for x in range(modulus) if x % 21 == 0}
    return {"group": "Z/210Z via CRT to C7 x C30", "offsets": offsets,
            "indices": indices_, "sizes": list(map(len, cosets)),
            "six_pair_intersections": pair_intersections, "six_pair_gcds": pair_gcds,
            "cluster_quotient_intersection": joint, "outside_quotient_coset": outside,
            "merged_and_outside_indices": [30, 30], "merged_gcd": 30,
            "changed_outside_intersects_cluster_0": len(bad_outside & cosets[0]),
            "changed_cluster_intersects_cluster_0": len(bad_cluster & cosets[0])}


print(json.dumps({"cluster_cases": [cluster_search(r) for r in range(2, 8)],
                  "cyclic_obstruction": cyclic_obstruction()}, indent=2))

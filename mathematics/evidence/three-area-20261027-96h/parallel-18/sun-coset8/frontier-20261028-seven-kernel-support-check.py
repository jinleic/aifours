#!/usr/bin/env python3
"""Finite overapproximation for a normal seven-index-power kernel.

Cluster=quotient images with nontrivial kernel index.  Outside images are
pairwise disjoint and disjoint from every cluster image.  Only prime supports
2,3,5,7 are needed under a putative original gcd<=7.
"""
from itertools import combinations, combinations_with_replacement
from math import gcd

PRIMES = (2, 3, 5, 7)


def squarefree(mask):
    n = 1
    for i, p in enumerate(PRIMES):
        if mask & (1 << i):
            n *= p
    return n


SIG = sorted(squarefree(m) for m in range(1, 16))


def main():
    total_models = 0
    for r in range(2, 8):
        clusters = 0
        viable = 0
        for cluster in combinations(SIG, r):
            if any(gcd(a, b) != 1 for a, b in combinations(cluster, 2)):
                continue
            clusters += 1
            outsiders = [x for x in SIG if all(
                2 <= gcd(a, x) <= 7 and gcd(7*a, x) <= 7 for a in cluster
            )]
            for labels in combinations_with_replacement(outsiders, 8-r):
                if r + sum(x % 7 == 0 for x in labels) < 3:
                    continue
                if any(not 2 <= gcd(x, y) <= 7 for x, y in combinations(labels, 2)):
                    continue
                viable += 1
        total_models += viable
        print(f"cluster_size={r}: cluster_support_sets={clusters}; terminal_models={viable}")
    if total_models:
        raise SystemExit("FAIL: necessary-condition abstract model remains")
    print("PASS: no abstract models for cluster sizes 2..7")


if __name__ == "__main__":
    main()

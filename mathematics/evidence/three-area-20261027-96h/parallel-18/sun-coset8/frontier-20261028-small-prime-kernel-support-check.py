#!/usr/bin/env python3
"""Squarefree-support overapproximation for p-power normal kernels, p=2,3,5.

Actual cluster a_i need not be coprime for p=2 or3, so repetitions are
explicitly allowed. Every nontrivial cross/outside gcd <=7 is retained.
"""
from itertools import combinations, combinations_with_replacement
from math import gcd

PRIMES = (2, 3, 5, 7)
SIG = sorted(
    __import__("math").prod(p for j, p in enumerate(PRIMES) if mask & (1 << j))
    for mask in range(1, 16)
)


def run(p):
    total = 0
    for r in range(2, 8):
        cluster_count = 0
        viable = 0
        first = None
        for cluster in combinations_with_replacement(SIG, r):
            if any(gcd(p*a, p*b) > 7 for a, b in combinations(cluster, 2)):
                continue
            cluster_count += 1
            outside = [x for x in SIG if all(
                2 <= gcd(a, x) <= 7 and gcd(p*a, x) <= 7 for a in cluster
            )]
            for labels in combinations_with_replacement(outside, 8-r):
                if sum(x % 7 == 0 for x in cluster + labels) < 3:
                    continue
                if any(not 2 <= gcd(x, y) <= 7 for x, y in combinations(labels, 2)):
                    continue
                viable += 1
                if first is None:
                    first = (cluster, labels)
        total += viable
        print(f"p={p}, cluster_size={r}: cluster_support_sets={cluster_count}; terminal_models={viable}")
        if first is not None:
            print("first_abstract_model:", first)
    return total


def main():
    totals = [run(p) for p in (2, 3, 5)]
    if any(totals):
        raise SystemExit("FAIL: abstract model remains")
    print("PASS: no abstract models for p=2,3,5 and cluster sizes 2..7")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Prime-support overapproximation for a normal five-index-power kernel."""
from itertools import combinations, combinations_with_replacement
from math import gcd

PRIMES = (2, 3, 5, 7)


def support(mask):
    n = 1
    for j, p in enumerate(PRIMES):
        if mask & (1 << j):
            n *= p
    return n


SIG = sorted(support(m) for m in range(1, 16))


def main():
    total = 0
    for r in range(2, 8):
        cluster_count = 0
        models = 0
        first = None
        for cluster in combinations(SIG, r):
            if any(gcd(a, b) != 1 for a, b in combinations(cluster, 2)):
                continue
            cluster_count += 1
            outside = [x for x in SIG if all(
                2 <= gcd(a, x) <= 7 and gcd(5*a, x) <= 7 for a in cluster
            )]
            for labels in combinations_with_replacement(outside, 8-r):
                if sum(x % 7 == 0 for x in cluster + labels) < 3:
                    continue
                if any(not 2 <= gcd(x, y) <= 7 for x, y in combinations(labels, 2)):
                    continue
                models += 1
                if first is None:
                    first = (cluster, labels)
        total += models
        print(f"cluster_size={r}: cluster_support_sets={cluster_count}; terminal_models={models}")
        if first is not None:
            print("first_abstract_model:", first)
    if total:
        raise SystemExit("FAIL: abstract support models remain")
    print("PASS: no abstract models for cluster sizes 2..7")


if __name__ == "__main__":
    main()

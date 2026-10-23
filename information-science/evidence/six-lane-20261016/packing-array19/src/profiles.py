#!/usr/bin/env python3
"""Exhaustive column-profile and profile-multiset enumeration for PA(N,k,q).

A column of an N x k array over q symbols is a partition of N rows into at most q
symbol classes. kappa(profile) = sum C(n_s, 2) = number of row pairs agreeing there.
Validity (rows agree in <= 1 column) forces sum_c kappa_c <= C(N,2).
"""
import itertools
import json
import sys


def partitions(n, parts, maxpart=None):
    """All non-increasing tuples of length `parts` (zeros allowed) summing to n."""
    if maxpart is None:
        maxpart = n
    if parts == 0:
        if n == 0:
            yield ()
        return
    for first in range(min(n, maxpart), -1, -1):
        if first * parts < n:
            break
        for rest in partitions(n - first, parts - 1, first):
            yield (first,) + rest


def kappa(p):
    return sum(x * (x - 1) // 2 for x in p)


def enumerate_profiles(N, k, q):
    pairs = N * (N - 1) // 2
    allp = list(partitions(N, q))
    kmin = min(kappa(p) for p in allp)
    budget = pairs - k * kmin
    profs = sorted((p for p in allp if kappa(p) - kmin <= budget),
                   key=lambda p: (kappa(p), [-x for x in p]))
    multisets = []
    if budget >= 0:
        for combo in itertools.combinations_with_replacement(range(len(profs)), k):
            ex = sum(kappa(profs[i]) - kmin for i in combo)
            if ex <= budget:
                # sort positions by excess non-increasing (normalization step 1)
                ordered = sorted(combo, key=lambda i: (-(kappa(profs[i]) - kmin), i))
                multisets.append({"profiles": [list(profs[i]) for i in ordered],
                                  "excess": ex,
                                  "zero_agreement_pairs": budget - ex})
    return {"N": N, "k": k, "q": q, "row_pairs": pairs, "kappa_min": kmin,
            "budget": budget, "num_partitions_checked": len(allp),
            "profiles": [{"profile": list(p), "kappa": kappa(p),
                          "excess": kappa(p) - kmin} for p in profs],
            "multisets": multisets}


if __name__ == "__main__":
    N, k, q = (int(a) for a in sys.argv[1:4]) if len(sys.argv) >= 4 else (19, 8, 6)
    print(json.dumps(enumerate_profiles(N, k, q), indent=1))

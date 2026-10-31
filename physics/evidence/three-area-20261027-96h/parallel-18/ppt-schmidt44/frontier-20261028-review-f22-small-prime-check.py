#!/usr/bin/env python3
"""Independent necessary prime-support search for p=2,3,5 kernel cases.

Supports are squarefree and repeated labels are allowed. Sorting within the
cluster and outside sectors removes only label permutations. An empty model
set does not prove any actual quotient, Sun7, or arbitrary group theorem.
"""
from functools import lru_cache
from itertools import combinations
from math import gcd, prod
import json


PRIMES = (2, 3, 5, 7)
SUPPORTS = tuple(sorted(prod(p for j,p in enumerate(PRIMES) if mask & (1 << j))
                        for mask in range(16)))


def check(p, r):
    explored = 0

    @lru_cache(maxsize=None)
    def visit(vals, n7):
        nonlocal explored
        explored += 1
        i = len(vals)
        remaining_clusters = max(0, r - i)
        remaining_outside = 8 - max(i, r)
        seen_cluster_seven = any(v % 7 == 0 for v in vals[:r])
        max_future = remaining_outside + int(remaining_clusters > 0 and not seen_cluster_seven)
        if n7 + max_future < 3:
            return None
        if i == 8:
            return vals if n7 >= 3 else None
        lower = vals[-1] if i and i != r else 1
        for ai in SUPPORTS:
            if ai < lower:
                continue
            ni = (p if i < r else 1) * ai
            if all(gcd(ni, (p if j < r else 1) * aj) <= 7
                   and (i < r and j < r or gcd(ai, aj) >= 2)
                   for j, aj in enumerate(vals)):
                found = visit(vals + (ai,), n7 + int(ni % 7 == 0))
                if found is not None:
                    return found
        return None

    model = visit((), 0)
    return {"p":p, "r":r, "nodes":explored, "model":model}


print(json.dumps({"cases":[check(p,r) for p in (2,3,5) for r in range(2,8)],
                  "limits":"necessary support overapproximation only; no actual coset or Sun7 proof"}, indent=2))

#!/usr/bin/env python3
"""Exact necessary incidence condition for a four-dimensional sector.
No physical witness, numeric phase search, or package dependencies.
"""
from itertools import combinations
import json
import time

start = time.monotonic()
L = lambda r, c: (r + c) % 10
survivors = []
excluded = []
for S in combinations(range(10), 4):
    if sum(x % 2 == 0 for x in S) != 2:
        continue
    cells = [(r, c) for r in range(10) for c in range(10)
             if (c - r) % 10 in S]
    contexts = [set(x for x in cells if x[k] == a)
                for k in range(2) for a in range(10)]
    contexts += [set(x for x in cells if L(*x) == a)
                 for a in range(10)]
    if any(len(A) != 4 for A in contexts):
        raise RuntimeError("bad context count")
    obstruction = None
    for i, j in combinations(range(30), 2):
        A, B = contexts[i], contexts[j]
        common = A & B
        if len(common) != 1:
            continue
        x = next(iter(common))
        cross = [(a, b) for a in sorted(A - {x})
                 for b in sorted(B - {x})
                 if a[0] == b[0] or a[1] == b[1]
                 or L(*a) == L(*b)]
        if len(cross) >= 2:
            obstruction = {"contexts": [i, j], "shared": list(x),
                           "forced_3x3_zeros": cross}
            break
    if obstruction is None:
        survivors.append(list(S))
    else:
        excluded.append({"S": list(S), **obstruction})
print(json.dumps({"balanced_masks": len(survivors) + len(excluded),
                  "excluded_masks": len(excluded),
                  "surviving_masks": survivors,
                  "exclusion_certificates": excluded,
                  "elapsed_seconds": time.monotonic() - start,
                  "scope": "A surviving support is not a ray realization."},
                 indent=2))

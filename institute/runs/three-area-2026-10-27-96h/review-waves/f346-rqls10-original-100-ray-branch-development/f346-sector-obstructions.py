#!/usr/bin/env python3
"""f346 fresh exact incidence/support exploration; stdlib; finite <60s.
Inputs: cyclic Latin L(r,c)=r+c mod 10, its one-intercalate trade,
and every circulant rank-4 sector mask c-r in S (|S|=4).
This computes necessary support conditions, NOT any physical rays.
"""
import itertools
import json
import time

START = time.monotonic()
DEADLINE = START + 55.0

def guard():
    if time.monotonic() > DEADLINE:
        raise RuntimeError("55-second cooperative bound exceeded")

def incidence_rank_mod2(L):
    n = len(L)
    rows = [0] * (3 * n)
    for r in range(n):
        for c in range(n):
            bit = 1 << (n * r + c)
            rows[r] |= bit
            rows[n + c] |= bit
            rows[2 * n + L[r][c]] |= bit
    pivots = {}
    for value in rows:
        while value:
            k = value.bit_length() - 1
            if k in pivots:
                value ^= pivots[k]
            else:
                pivots[k] = value
                break
    return len(pivots)

def is_latin(L):
    n = len(L)
    target = list(range(n))
    return (all(sorted(row) == target for row in L)
            and all(sorted(L[r][c] for r in range(n)) == target
                    for c in range(n)))

def sector_counts(L, S):
    n = len(L)
    counts = [0] * (3 * n)
    for r in range(n):
        for c in range(n):
            if (c - r) % n in S:
                counts[r] += 1
                counts[n + c] += 1
                counts[2 * n + L[r][c]] += 1
    return counts

# Every actual nonparallel 4x4 change-of-basis matrix has a support
# among the following masks.  Degree one implies a repeated ray;
# a unique common nonzero entry prevents two rows/columns being orthogonal.
def admissible_support_masks_4():
    result = []
    for mask in range(1 << 16):
        if mask % 4096 == 0:
            guard()
        rows = [(mask >> (4 * r)) & 15 for r in range(4)]
        if any(x.bit_count() < 2 for x in rows):
            continue
        cols = [sum(((rows[r] >> c) & 1) << r for r in range(4))
                for c in range(4)]
        if any(x.bit_count() < 2 for x in cols):
            continue
        if any((a & b).bit_count() == 1
               for family in (rows, cols)
               for a, b in itertools.combinations(family, 2)):
            continue
        result.append(mask)
    return result

def forbidden_mask(S, delta):
    S = sorted(S)
    result = 0
    for a, s in enumerate(S):
        for b, t in enumerate(S):
            if ((s - t - delta) % 10 == 0
                    or (s - t - 2 * delta) % 10 == 0):
                result |= 1 << (4 * a + b)
    return result

L = [[(r + c) % 10 for c in range(10)] for r in range(10)]
T = [row[:] for row in L]
for r in (0, 5):
    T[r][0], T[r][5] = T[r][5], T[r][0]
if not is_latin(L) or not is_latin(T):
    raise RuntimeError("non-Latin input")

supports = admissible_support_masks_4()
cache = {}
all_cases = []
for values in itertools.combinations(range(10), 4):
    guard()
    S = set(values)
    counts = sector_counts(L, S)
    if counts != [4] * 30:
        continue
    failures = []
    for delta in range(1, 10):
        zeros = forbidden_mask(S, delta)
        if zeros not in cache:
            cache[zeros] = any((mask & zeros) == 0 for mask in supports)
        if not cache[zeros]:
            failures.append(delta)
    all_cases.append({"S": list(values), "impossible_deltas": failures})

output = {
    "arithmetic": "exact integer bit masks; no optimizer or approximate matrix",
    "cyclic_incidence_rank_F2": incidence_rank_mod2(L),
    "traded_incidence_rank_F2": incidence_rank_mod2(T),
    "traded_cells": [[0, 0], [0, 5], [5, 0], [5, 5]],
    "rank4_example_counts": sector_counts(L, {0, 1, 2, 3}),
    "rank6_complement_counts": sector_counts(L, {4, 5, 6, 7, 8, 9}),
    "candidate_4x4_support_count": len(supports),
    "balanced_circulant_4_masks": len(all_cases),
    "masks_excluded_by_two_row_support_test": sum(bool(x["impossible_deltas"]) for x in all_cases),
    "masks_not_excluded": [x for x in all_cases if not x["impossible_deltas"]],
    "all_balanced_cases": all_cases,
    "elapsed_seconds": time.monotonic() - START,
    "interpretation": "A failed support test is an exact necessary-condition obstruction. A passed support test is NOT a unitary or ray realization."
}
print(json.dumps(output, indent=2))

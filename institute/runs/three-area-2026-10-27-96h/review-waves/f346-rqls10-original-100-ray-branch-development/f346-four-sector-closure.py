#!/usr/bin/env python3
"""Finite exact support-closure exploration of the cyclic rank-4 family.
At most 55 seconds, no solvers, no approximate arithmetic.
Physical necessity only; survival never asserts realizability.
"""
import itertools
import json
import time

START = time.monotonic()
STOP = START + 55

def guard():
    if time.monotonic() > STOP:
        raise RuntimeError("cooperative 55-second bound")

def candidate_supports(k):
    result = []
    for mask in range(1 << (k * k)):
        rows = [(mask >> (k * r)) & ((1 << k) - 1) for r in range(k)]
        if any(x.bit_count() < 2 for x in rows):
            continue
        cols = [sum(((rows[r] >> c) & 1) << r for r in range(k))
                for c in range(k)]
        if any(x.bit_count() < 2 for x in cols):
            continue
        if any((a & b).bit_count() == 1
               for family in (rows, cols)
               for a, b in itertools.combinations(family, 2)):
            continue
        result.append(mask)
    return result

SUPPORTS = {k: candidate_supports(k) for k in (2, 3, 4)}
CACHE = {}

def union_support(k, zeros):
    key = (k, zeros)
    if key not in CACHE:
        possible = [s for s in SUPPORTS[k] if not (s & zeros)]
        union = 0
        for s in possible:
            union |= s
        CACHE[key] = (bool(possible), union)
    return CACHE[key]

def examine(S):
    cells = [(r, c) for r in range(10) for c in range(10)
             if (c - r) % 10 in S]
    N = len(cells)
    def context(a):
        r, c = a
        return (r, c, (r + c) % 10)
    triples = [context(x) for x in cells]
    ortho = [0] * N
    for i in range(N):
        for j in range(i):
            if any(triples[i][k] == triples[j][k] for k in range(3)):
                ortho[i] |= 1 << j
                ortho[j] |= 1 << i
    initial_edges = sum(x.bit_count() for x in ortho) // 2
    passes = 0
    while True:
        guard()
        passes += 1
        bases = []
        for A in itertools.combinations(range(N), 4):
            if all((ortho[i] >> j) & 1 for i, j in itertools.combinations(A, 2)):
                bases.append(frozenset(A))
        changed = False
        for A, B in itertools.combinations(bases, 2):
            common = A & B
            k = 4 - len(common)
            if k == 1:
                return {"status": "excluded", "reason": "two bases share three rays",
                        "passes": passes, "bases": [sorted(A), sorted(B)]}
            if k == 0:
                continue
            aa, bb = sorted(A - common), sorted(B - common)
            zeros = sum(1 << (k * i + j)
                        for i, a in enumerate(aa) for j, b in enumerate(bb)
                        if (ortho[a] >> b) & 1)
            possible, union = union_support(k, zeros)
            if not possible:
                return {"status": "excluded", "reason": "no necessary unitary support",
                        "passes": passes, "k": k,
                        "bases": [[list(cells[a]) for a in sorted(A)],
                                  [list(cells[b]) for b in sorted(B)]],
                        "zeros": zeros}
            for i, a in enumerate(aa):
                for j, b in enumerate(bb):
                    if not ((union >> (k * i + j)) & 1) and not ((ortho[a] >> b) & 1):
                        ortho[a] |= 1 << b
                        ortho[b] |= 1 << a
                        changed = True
        if not changed:
            return {"status": "not_excluded", "passes": passes,
                    "basis_count": len(bases), "initial_orthogonal_edges": initial_edges,
                    "closed_orthogonal_edges": sum(x.bit_count() for x in ortho) // 2}

balanced = {tuple(S) for S in itertools.combinations(range(10), 4)
            if sum(x % 2 == 0 for x in S) == 2}
orbits = []
while balanced:
    rep = min(balanced)
    orbit = {tuple(sorted((a * x + b) % 10 for x in rep))
             for a in (1, 3, 7, 9) for b in range(10)}
    balanced -= orbit
    orbits.append({"representative": list(rep), "orbit_size": len(orbit),
                   "closure": examine(set(rep))})
print(json.dumps({"support_counts": {str(k): len(v) for k, v in SUPPORTS.items()},
                  "affine_orbits": orbits,
                  "elapsed_seconds": time.monotonic() - START,
                  "scope": "Exact necessary support closure; no ray construction."}, indent=2))

#!/usr/bin/env python3
"""Exact proof-step extraction for S={0,1,3,8}; finite <60s."""
import itertools as it
import json
import time
start = time.monotonic()
S = {0, 1, 3, 8}
cells = [(r, c) for r in range(10) for c in range(10) if (c-r) % 10 in S]
triple = [(r, c, (r+c) % 10) for r, c in cells]
E = {frozenset((i, j)) for i, j in it.combinations(range(40), 2)
     if any(triple[i][k] == triple[j][k] for k in range(3))}
def edge(i,j):
    return frozenset((i,j)) in E
bases = [frozenset(A) for A in it.combinations(range(40),4)
         if all(edge(i,j) for i,j in it.combinations(A,2))]
candidates = {}
for k in (2,3,4):
    masks = []
    for mask in range(1 << (k*k)):
        rr = [(mask >> (k*r)) & ((1<<k)-1) for r in range(k)]
        cc = [sum(((rr[r]>>c)&1)<<r for r in range(k)) for c in range(k)]
        if any(x.bit_count() < 2 for x in rr+cc):
            continue
        if any((a&b).bit_count() == 1 for ff in (rr,cc) for a,b in it.combinations(ff,2)):
            continue
        masks.append(mask)
    candidates[k] = masks
steps = []
for A,B in it.combinations(bases,2):
    if time.monotonic()-start > 55:
        raise RuntimeError("55-second bound")
    shared = A&B
    k = 4-len(shared)
    aa,bb = sorted(A-shared),sorted(B-shared)
    record = {"A": [cells[x] for x in sorted(A)], "B": [cells[x] for x in sorted(B)],
              "shared": [cells[x] for x in sorted(shared)],
              "remaining_A": [cells[x] for x in aa], "remaining_B": [cells[x] for x in bb]}
    if k == 1:
        steps.append({**record, "contradiction": "share three rays"})
        break
    if k == 0:
        continue
    zeros = sum(1 << (k*i+j) for i,a in enumerate(aa) for j,b in enumerate(bb) if edge(a,b))
    possible = [m for m in candidates[k] if not (m & zeros)]
    if not possible:
        steps.append({**record, "zeros": zeros, "contradiction": "no possible necessary support"})
        break
    union = 0
    for m in possible:
        union |= m
    added = [(a,b) for i,a in enumerate(aa) for j,b in enumerate(bb)
             if not ((union >> (k*i+j))&1) and not edge(a,b)]
    if added:
        steps.append({**record, "zeros": zeros,
                      "possible_supports": possible,
                      "new_orthogonal_pairs": [[cells[a],cells[b]] for a,b in added]})
        for a,b in added:
            E.add(frozenset((a,b)))
print(json.dumps({"S": sorted(S), "initial_basis_count": len(bases), "steps": steps,
                  "elapsed_seconds": time.monotonic()-start}, indent=2))

#!/usr/bin/env python3
"""Check an actual 4-coset fibre-collapse obstruction in C7 x C30.

It is a partial configuration, NOT an eight-coset Sun counterexample.
"""
from itertools import combinations
from math import gcd

G = {(x, y) for x in range(7) for y in range(30)}
add = lambda a, b: ((a[0] + b[0]) % 7, (a[1] + b[1]) % 30)
subgroups = [
    {(0, y) for y in range(30) if y % p == 0} for p in (2, 3, 5)
] + [{(x, 0) for x in range(7)}]
reps = [(0, 0), (1, 0), (2, 0), (0, 1)]
cosets = []
for h, g in zip(subgroups, reps):
    if (0, 0) not in h or any(add(a, b) not in h for a in h for b in h):
        raise SystemExit("FAIL subgroup closure")
    cosets.append({add(g, a) for a in h})
indices = [len(G) // len(h) for h in subgroups]
if any(cosets[i] & cosets[j] for i, j in combinations(range(4), 2)):
    raise SystemExit("FAIL actual cosets intersect")
pair_gcds = [gcd(indices[i], indices[j]) for i, j in combinations(range(4), 2)]
if any(d > 7 for d in pair_gcds):
    raise SystemExit("FAIL original pair gcd bound")
quotients = [{y for _, y in c} for c in cosets]
intersection = set.intersection(*quotients[:3])
if intersection != {0} or quotients[3] != {1}:
    raise SystemExit("FAIL quotient collision/intersection")
cluster_index = 30 // len(intersection)
other_index = 30 // len(quotients[3])
print("group_order:", len(G))
print("actual_subgroup_indices:", indices)
print("six_original_pair_gcds:", pair_gcds)
print("actual_pairwise_disjoint:", True)
print("quotient_cluster_intersection:", sorted(intersection))
print("outside_quotient_coset:", sorted(quotients[3]))
print("merged_and_outside_indices:", [cluster_index, other_index])
print("merged_pair_gcd:", gcd(cluster_index, other_index))
print("PASS: merged pair reaches >=8 while no original pair does")

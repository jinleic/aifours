#!/usr/bin/env python3
"""Independent C210 representation of the four-coset bridge obstruction."""
from itertools import combinations
from math import gcd

M = 210
# Under z -> (z mod 7, z mod 30), these are the claimed subgroups and reps.
indices = [14, 21, 35, 30]
reps = [0, 120, 30, 91]


def coset(r, index):
    return {(r + index*j) % M for j in range(M // index)}


def audit(representatives):
    cs = [coset(r, n) for r, n in zip(representatives, indices)]
    if any(cs[i] & cs[j] for i, j in combinations(range(4), 2)):
        return "INTERSECTING_ACTUAL_COSETS"
    if any(gcd(indices[i], indices[j]) > 7 for i, j in combinations(range(4), 2)):
        return "ORIGINAL_GCD_EXCEEDS_7"
    qc = [{z % 30 for z in c} for c in cs]
    if set.intersection(*qc[:3]) != {0} or qc[3] != {1}:
        return "QUOTIENT_CLUSTER_MISMATCH"
    if gcd(30 // len(set.intersection(*qc[:3])), 30 // len(qc[3])) != 30:
        return "MERGED_GCD_MISMATCH"
    return "VALID_BRIDGE_OBSTRUCTION"


print("cyclic_original:", audit(reps))
print("mutated_outside_representative:", audit(reps[:3] + [0]))
print("mutated_cluster_representative:", audit([reps[0], 0, reps[2], reps[3]]))
if audit(reps) != "VALID_BRIDGE_OBSTRUCTION":
    raise SystemExit("FAIL original")
if audit(reps[:3] + [0]) != "INTERSECTING_ACTUAL_COSETS":
    raise SystemExit("FAIL outside mutation")
if audit([reps[0], 0, reps[2], reps[3]]) != "INTERSECTING_ACTUAL_COSETS":
    raise SystemExit("FAIL cluster mutation")
print("PASS: cyclic witness and two intended intersection-negative controls")

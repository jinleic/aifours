"""Finite controls for K5_RESIDUAL_NORMAL_FORM.r1.md, not a vector proof.
Enumerate every nonempty family of nonempty B-supports with minimum size1or2,
and every B-permutation taking a chosen minimum support to the rightmost-k set.
The transformed family's lexicographic minimum must be exactly that set.
Also check every support meeting A is larger than both target vectors.
Two intended controls use the LEFTMOST-k set and must fail on stated families.
No production solver/encoder or leaf ledger is invoked.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

B = (4, 5, 6, 7)
A = {1, 2, 3}
vec = lambda S: tuple(int(i in S) for i in range(1, 8))
sets = [frozenset(B[k] for k in range(4) if (b >> k) & 1) for b in range(1, 16)]
perms = list(itertools.permutations(B))
t0 = time.time()
families = checks = 0
for mask in range(1, 1 << 15):
    family = [S for j, S in enumerate(sets) if (mask >> j) & 1]
    k = min(map(len, family))
    if k not in (1, 2):
        continue
    families += 1
    T = next(S for S in family if len(S) == k)
    target = frozenset(B[-k:])
    for perm in perms:
        sigma = dict(zip(B, perm))
        if frozenset(sigma[x] for x in T) != target:
            continue
        image = [frozenset(sigma[x] for x in S) for S in family]
        if min(image, key=vec) != target:
            raise RuntimeError("rightmost minimum failed")
        checks += 1
mixed = 0
for b in range(1, 128):
    S = {k + 1 for k in range(7) if (b >> k) & 1}
    if S & A:
        for k in (1, 2):
            if not vec(S) > vec(set(B[-k:])):
                raise RuntimeError("A-meeting support is not larger")
            mixed += 1
negative = {
    "leftmost_k1_is_not_minimum": min([{4}, {7}], key=vec) != {4},
    "leftmost_k2_is_not_minimum": min([{4, 5}, {6, 7}], key=vec) != {4, 5},
}
rec = {"script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       "proof_note_sha256": hashlib.sha256((Path(__file__).resolve().parent.parent /
                                           'review/K5_RESIDUAL_NORMAL_FORM.r1.md').read_bytes()).hexdigest(),
       "families": families, "family_permutation_checks": checks,
       "mixed_A_order_checks": mixed, "negative_controls": negative,
       "all_pass": all(negative.values()), "seconds": time.time() - t0,
       "scope": "finite support-order control only; no vector/classicality or CNF exclusion established"}
out = Path(sys.argv[1])
with out.open('x') as f:
    json.dump(rec, f, indent=1)
print(json.dumps(rec), flush=True)

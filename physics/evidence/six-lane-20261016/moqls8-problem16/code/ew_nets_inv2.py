"""Refined isomorphism invariant for the 39 E–W 5-nets (reads evidence/k2_fixed/ew_nets.json).

For an ordered pair of distinct lines (x1, x2) of one class X and a second class Y, a third class Z induces a
permutation of the Y-lines: y -> the Y-line through (Z-line through (x1 ∩ y)) ∩ x2. Its cycle type is recorded.
The invariant of a net is the sorted multiset, over all ordered triples (X, Y, Z) of distinct classes and all
ordered pairs (x1, x2), of these cycle types — invariant under any isomorphism of nets (classes may be permuted,
lines relabelled). Distinct invariants certify non-isomorphism.
python -B ew_nets_inv2.py --nets ../evidence/k2_fixed/ew_nets.json --out ../evidence/k2_fixed/ew_nets_inv2.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter

N = 8


def classes(sqs):
    cells = [(i, j) for i in range(N) for j in range(N)]
    cls = [{c: c[0] for c in cells}, {c: c[1] for c in cells}]
    for L in sqs:
        cls.append({c: L[c[0]][c[1]] for c in cells})
    return cells, cls


def invariant(sqs):
    cells, cls = classes(sqs)
    K = len(cls)
    point = {}            # (class a, line u, class b, line v) -> the unique common point
    for c in cells:
        for a in range(K):
            for b in range(K):
                if a != b:
                    point[(a, cls[a][c], b, cls[b][c])] = c
    cnt = Counter()
    for X, Y, Z in itertools.permutations(range(K), 3):
        for x1, x2 in itertools.permutations(range(N), 2):
            perm = []
            for y in range(N):
                p = point[(X, x1, Y, y)]
                z = cls[Z][p]
                q = point[(Z, z, X, x2)]
                perm.append(cls[Y][q])
            seen, cyc = set(), []
            for s in range(N):
                if s in seen:
                    continue
                L, t = 0, s
                while t not in seen:
                    seen.add(t)
                    t = perm[t]
                    L += 1
                cyc.append(L)
            cnt[tuple(sorted(cyc))] += 1
    return sorted([list(k) + [v] for k, v in cnt.items()])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    d = json.load(open(a.nets))
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "nets_sha256": hashlib.sha256(open(a.nets, "rb").read()).hexdigest(), "invariants": {}}
    for item in d["nets"]:
        res["invariants"][item["tag"]] = invariant(item["squares"])
    keys = {t: json.dumps(v) for t, v in res["invariants"].items()}
    groups = Counter(keys.values())
    res["distinct"] = len(groups)
    res["collisions"] = [[t for t in keys if keys[t] == k] for k, c in groups.items() if c > 1]
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({"distinct": res["distinct"], "collisions": res["collisions"]}))


if __name__ == "__main__":
    main()

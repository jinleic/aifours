"""Third isomorphism invariant for the 39 E–W 5-nets: for every subset of k = 3 and k = 4 of the 5 parallel classes,
the number of transversals of that sub-net (8-point sets meeting every line of the chosen classes exactly once),
as sorted multisets (10 triples, 5 quadruples). Combined with ew_nets.json (intercalates, common transversals,
extendability) and ew_nets_inv2.json (cycle types) to certify that the 39 representatives are pairwise
non-isomorphic (completeness of the list is the imported Egan–Wanless claim).
python -B ew_nets_inv3.py --nets ../evidence/k2_fixed/ew_nets.json --inv2 ../evidence/k2_fixed/ew_nets_inv2.json \\
       --out ../evidence/k2_fixed/ew_nets_inv3.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter

N = 8


def transversal_counts(sqs):
    cells = [(i, j) for i in range(N) for j in range(N)]
    cls = [lambda c: c[0], lambda c: c[1]] + [(lambda L: (lambda c: L[c[0]][c[1]]))(L) for L in sqs]
    # count, for each subset S of classes containing at least 3 classes, point sets meeting every line of S once.
    # Enumerate all 8! permutations sigma (point (i, sigma(i)) meets every row and column once) — every transversal of
    # a subset containing rows and columns is of this form; for subsets without rows/columns, regrid: we count via
    # the general method below (choose two classes of S as coordinates).
    out3, out4 = [], []
    for k, store in ((3, out3), (4, out4)):
        for S in itertools.combinations(range(5), k):
            A, B = S[0], S[1]
            # coordinates: point determined by (A-line a, B-line b); enumerate permutations b = pi(a)
            point = {}
            for c in cells:
                point[(cls[A](c), cls[B](c))] = c
            rest = S[2:]
            cnt = 0
            for pi in itertools.permutations(range(N)):
                pts = [point[(a, pi[a])] for a in range(N)]
                if all(len({cls[t](p) for p in pts}) == N for t in rest):
                    cnt += 1
            store.append(cnt)
    return sorted(out3), sorted(out4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets", required=True)
    ap.add_argument("--inv2", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    d = json.load(open(a.nets))
    inv2 = json.load(open(a.inv2))["invariants"]
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "keys": {}}
    for item in d["nets"]:
        t3, t4 = transversal_counts(item["squares"])
        res["keys"][item["tag"]] = {"intercalates": item["intercalate_multiset"],
                                    "common_transversals": item["common_transversals"],
                                    "fourth_square": item["fourth_square"], "cycle_types": inv2[item["tag"]],
                                    "transversals_k3": t3, "transversals_k4": t4}
    comb = {t: json.dumps(v, sort_keys=True) for t, v in res["keys"].items()}
    groups = Counter(comb.values())
    res["distinct_combined"] = len(groups)
    res["collisions"] = [[t for t in comb if comb[t] == k] for k, c in groups.items() if c > 1]
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({"distinct_combined": res["distinct_combined"], "collisions": res["collisions"]}))


if __name__ == "__main__":
    main()

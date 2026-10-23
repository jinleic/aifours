#!/usr/bin/env python3
"""Exact symmetry audit of a GCDCQS certificate against the generators recorded in its seed
(standard library only).  Checks, with G = <generators>:
  (B) every generator maps the block set onto itself;
  (T) G is transitive on the points;
  (S) Stab_G(0) and whether it preserves the partition (colouring) at point 0;
  (E) for EVERY g in G and EVERY point y, g maps the partition at y onto the partition at g(y)
      (classes as sets of triples; class labels may be permuted), and counts the pairs (g, y) for
      which the labels are preserved as well.
Usage: equivariance_audit.py CERT SEED.json OUT.json"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import xopen  # noqa: E402
from seed_tools import closure, read_cert  # noqa: E402


def main():
    cert, seedp, out = sys.argv[1:4]
    header, head, groups, blocks, col = read_cert(cert)
    v = head["GCDCQS"][0]
    gens = [tuple(p) for p in json.load(open(seedp))["generators"]]
    B = set(blocks)
    gens_ok = all(tuple(sorted(e[p] for p in b)) in B for e in gens for b in B)
    G = closure(gens, v)
    orbit0 = {e[0] for e in G}
    stab0 = [e for e in G if e[0] == 0]
    part = {y: [frozenset(C) for C in col[y]] for y in col}
    pset = {y: set(part[y]) for y in part}

    def image(e, C):
        return frozenset(tuple(sorted(e[p] for p in t)) for t in C)

    stab_preserves = all({image(e, C) for C in part[0]} == pset[0] for e in stab0)
    bad, label_kept, pairs = [], 0, 0
    for e in G:
        for y in range(v):
            imgs = [image(e, C) for C in part[y]]
            pairs += 1
            if set(imgs) != pset[e[y]]:
                bad.append([G.index(e), y])
            elif imgs == part[e[y]]:
                label_kept += 1
    res = {"certificate": cert, "seed": seedp, "group_order": len(G), "generators_preserve_blocks": gens_ok,
           "transitive": len(orbit0) == v, "stabilizer_of_0_order": len(stab0),
           "stabilizer_of_0_preserves_partition_at_0": stab_preserves,
           "pairs_checked": pairs, "pairs_partition_mapped_correctly": pairs - len(bad),
           "pairs_with_class_labels_also_preserved": label_kept,
           "result": "PASS" if gens_ok and len(orbit0) == v and stab_preserves and not bad else "FAIL",
           "failures_first": bad[:5]}
    with xopen(out) as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res))
    return 0 if res["result"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

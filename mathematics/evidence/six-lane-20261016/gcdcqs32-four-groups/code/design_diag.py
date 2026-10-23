#!/usr/bin/env python3
"""Read-only diagnostics of a recorded KM design (README E2/E3): block type counts, and at
x = (0,0) the Lemma P hypotheses of sources/symmetry-notes.md — (i) fraction of hole triples whose
two non-hole points share a group, (ii) fraction of hole-free triples meeting three groups — for
the whole derived design and, if the group has A, for the A-fixed sub-design on Fix(A) x F4.
Also reports whether the block set equals the Boolean CQS (planes a^b^c^d = 0 of F2^7 with label
bits as the top two coordinates) when g is a power of two.
Usage: design_diag.py SUMMARY.json:IDX GROUP G [OUT.json]"""
import lane_guard  # noqa: F401

import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from cqs_km import CQSKM
import groups as grp


def stats(der, hole, group_of):
    vert = skew = trans = two_one = 0
    for t in der:
        hs = [p for p in t if p in hole]
        rest = [group_of[p] for p in t if p not in hole]
        if hs:
            if rest[0] == rest[1]:
                vert += 1
            else:
                skew += 1
        elif len(set(rest)) == 3:
            trans += 1
        else:
            two_one += 1
    return {"hole_triples_vertical": vert, "hole_triples_skew": skew,
            "holefree_transversal": trans, "holefree_2plus1": two_one,
            "lemma_P_hypotheses_hold": skew == 0 and two_one == 0}


def main():
    src, group, g = sys.argv[1], sys.argv[2], int(sys.argv[3])
    path, idx = src.rsplit(":", 1)
    rows = json.load(open(path))["samples"][int(idx)]["rows"]
    spec = grp.build(group, 4, g)
    v = 4 * g
    km = CQSKM(v, spec["group_of"], spec["gens"])
    blocks = [tuple(sorted(b)) for b in km.blocks_of(rows)]
    gof = spec["group_of"]
    types = collections.Counter("+".join(str(c) for c in sorted(collections.Counter(gof[p] for p in b).values(), reverse=True))
                                for b in blocks)
    x = 0
    hole = {p for p in range(v) if gof[p] == 0 and p != 0}
    der = [tuple(p for p in b if p != x) for b in blocks if x in b]
    rec = {"design": src, "group": group, "g": g, "blocks": len(blocks), "block_types": dict(types),
           "derived_at_0": stats(der, hole, gof)}
    if (g & (g - 1)) == 0:
        m = g.bit_length() - 1
        lab = [0, 1, 2, 3]  # F4 labels as 2-bit vectors (XOR = F4 addition)
        vec = lambda p: (lab[p // g] << m) | (p % g)
        rec["equals_boolean_cqs"] = all(vec(a) ^ vec(b) ^ vec(c) ^ vec(d) == 0 for a, b, c, d in blocks)
    if group in ("A4xEA", "A4xEAB"):
        A = spec["res"]["C3A"][0]
        F = {p for p in range(v) if A[p] == p}
        subder = [t for t in der if set(t) <= F]
        rec["fixed_sub_design"] = {"points": len(F), "derived_triples": len(subder),
                                   **stats(subder, hole & F, gof)}
    print(json.dumps(rec))
    if len(sys.argv) > 4:
        with xopen(sys.argv[4]) as fh:
            json.dump(rec, fh, indent=1)


if __name__ == "__main__":
    main()

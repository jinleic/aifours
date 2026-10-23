#!/usr/bin/env python3
"""README E3a diagnostics: extract the A-fixed sub-CQS(8^4 : 0) of a recorded G_E design (blocks
inside Fix(A) x F4, i.e. coordinates 0..7 in every group), relabel (i, a) -> 8i + a, check that it
is a CQS(8^4 : 0) and that it is A4 x F2^3-invariant, and record it as KM rows of the group A4xE
at g = 8 in a summary file usable by pipeline2.py --rows-from (exclusive create).
Usage: subdesign.py SUMMARY.json:IDX OUT.json"""
import lane_guard  # noqa: F401

import json
import os
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from cqs_km import CQSKM
import groups as grp


def main():
    src, out = sys.argv[1], sys.argv[2]
    path, idx = src.rsplit(":", 1)
    rows = json.load(open(path))["samples"][int(idx)]["rows"]
    spec = grp.build("A4xEA", 4, 32)
    km = CQSKM(128, spec["group_of"], spec["gens"])
    blocks = [tuple(sorted(b)) for b in km.blocks_of(rows)]
    F = {p for p in range(128) if p % 32 < 8}
    sub = sorted(tuple(sorted(8 * (p // 32) + p % 32 for p in b)) for b in blocks if set(b) <= F)
    gof = [p // 8 for p in range(32)]
    cover = {}
    for b in sub:
        for t in combinations(b, 3):
            cover[t] = cover.get(t, 0) + 1
    universe = {t for t in combinations(range(32), 3) if len({gof[p] for p in t}) > 1}
    assert set(cover) == universe and set(cover.values()) == {1}, "not a CQS(8^4:0)"
    spec8 = grp.build("A4xE", 4, 8)
    S = set(sub)
    assert all(tuple(sorted(e[p] for p in b)) in S for e in spec8["gens"] for b in sub), "not A4xE-invariant"
    km8 = CQSKM(32, spec8["group_of"], spec8["gens"])
    r8 = [j for j, (lab, _) in enumerate(km8.rows) if tuple(int(x) for x in km8.Q[lab]) in S]
    assert sorted(tuple(sorted(b)) for b in km8.blocks_of(r8)) == sorted(S)
    rec = {"group": "A4xE", "g": 8, "source": f"A-fixed sub-design of {src} (relabel (i,a) -> 8i+a)",
           "samples": [{"sample": 0, "km_status": "SUBDESIGN", "rows": r8}]}
    with xopen(out) as fh:
        json.dump(rec, fh)
    print(out, len(sub), "blocks; A4 x F2^3-invariant;", len(r8), "KM rows over A4xE g=8")


if __name__ == "__main__":
    main()

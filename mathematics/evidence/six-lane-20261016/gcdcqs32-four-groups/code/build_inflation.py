#!/usr/bin/env python3
"""README E9a: x4 inflation of a gcDCQS(8^4 : 0) certificate into a CQS(32^4 : 0) (standard
construction, sources/symmetry-notes.md, "x4 inflation"):
  big point (i, m + 8c) for master point (i, m) and copy c in F2^2 (XOR);
  (A) for every master block {b1..b4}: all {(b_t, c_t)} with c1 ^ c2 ^ c3 ^ c4 = 0 (an H(4,4,4,3));
  (B) for every pair {p, q} of master points in different groups and d in {1, 2, 3}: the blocks
      {(p, c), (p, c ^ d), (q, e), (q, e ^ d)} (a CQS(4^2 : 0) on {p, q} x F2^2).
The result is checked to be a CQS(32^4 : 0) (every non-group triple exactly once) and to be
invariant under the generators of the group A4xC8E2M (README E9a), then written as KM rows of
that group in a summary file usable by pipeline2.py --rows-from OUT.json:0 (exclusive create).
Usage: build_inflation.py MASTER_CERT OUT.json"""
import lane_guard  # noqa: F401

import collections
import hashlib
import json
import os
import sys
from itertools import combinations, product

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from cqs_km import CQSKM
import groups as grp


def read_master_blocks(path):
    blocks, on, head = [], False, None
    for line in open(path):
        s = line.split("#")[0].strip()
        if not s:
            continue
        if s.startswith("GCDCQS"):
            head = [int(z) for z in s.split()[1:]]
        elif s == "BLOCKS":
            on = True
        elif s.startswith("POINT"):
            break
        elif on:
            blocks.append(tuple(int(z) for z in s.split()))
    assert head == [32, 4, 8], head
    return blocks


def main():
    master, out = sys.argv[1], sys.argv[2]
    mb = read_master_blocks(master)
    assert len(mb) == 1184
    big = lambda p, c: 32 * (p // 8) + (p % 8) + 8 * c
    blocks = set()
    for b in mb:
        for c1, c2, c3 in product(range(4), repeat=3):
            cs = (c1, c2, c3, c1 ^ c2 ^ c3)
            blocks.add(tuple(sorted(big(p, c) for p, c in zip(b, cs))))
    pairs = [(p, q) for p, q in combinations(range(32), 2) if p // 8 != q // 8]
    for p, q in pairs:
        for d in (1, 2, 3):
            reps = [c for c in range(4) if c < (c ^ d)]
            for c in reps:
                for e in reps:
                    blocks.add(tuple(sorted((big(p, c), big(p, c ^ d), big(q, e), big(q, e ^ d)))))
    assert len(blocks) == 80384, len(blocks)
    gof = [p // 32 for p in range(128)]
    cover = collections.Counter(t for b in blocks for t in combinations(b, 3))
    universe = {t for t in combinations(range(128), 3) if len({gof[p] for p in t}) > 1}
    assert set(cover) == universe and set(cover.values()) == {1}, "not a CQS(32^4:0)"
    spec = grp.build("A4xC8E2M", 4, 32)
    for e in spec["gens"]:
        assert all(tuple(sorted(e[p] for p in b)) in blocks for b in blocks), "not invariant"
    km = CQSKM(128, spec["group_of"], spec["gens"])
    rows = [j for j, (lab, _) in enumerate(km.rows) if tuple(int(z) for z in km.Q[lab]) in blocks]
    assert sorted(tuple(sorted(b)) for b in km.blocks_of(rows)) == sorted(blocks)
    types = collections.Counter("+".join(str(c) for c in sorted(collections.Counter(gof[p] for p in b).values(),
                                                                  reverse=True)) for b in blocks)
    rec = {"group": "A4xC8E2M", "g": 32, "source": f"x4 inflation of {master}",
           "master_sha256": hashlib.sha256(open(master, "rb").read()).hexdigest(),
           "block_types": dict(types),
           "samples": [{"sample": 0, "km_status": "INFLATION", "rows": rows}]}
    with xopen(out) as fh:
        json.dump(rec, fh)
    print(out, "CQS(32^4:0) verified,", len(rows), "KM rows over A4xC8E2M;", dict(types))


if __name__ == "__main__":
    main()

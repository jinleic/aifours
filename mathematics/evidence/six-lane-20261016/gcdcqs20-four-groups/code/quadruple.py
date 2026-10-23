#!/usr/bin/env python3
"""README E6: quadrupled cyclic SQS(20).

1. A cyclic SQS(20) S on Z20 from the Z20 Kramer–Mesner model (kissat, seed SEED, blocking the
   previously found solutions of this run so that `index` picks the index-th solution).
2. Q(S) on F4 x Z20 (label = 20*l + y, l in F4 = {0,1,2,3}, XOR addition):
   (A') {(l1,y1),..,(l4,y4)} for every block {y1..y4} of S, l1^l2^l3^l4 = 0, labels not all equal;
   (B)  {(l,y),(l^d,y),(m,z),(m^d,z)} for every pair {y,z}, d in {1,2,3}, l, m;
   (C)  {(0,y),(1,y),(2,y),(3,y)} for every y.
   The four groups are the label classes; Q(S) is checked directly as a CQS(20^4:0) (exact
   coverage of the non-group triples) and as A4 x C20-invariant.
3. Writes a summary JSON with the A4xC Kramer–Mesner rows of Q(S), usable by
   `pipeline2.py --rows-from OUT.json:0` (exclusive create).
Usage: quadruple.py OUT.json SEED INDEX
"""
import lane_guard  # noqa: F401

import json
import os
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import xopen
from lanelib import kissat
from cqs_km import CQSKM
import groups as grp


def main():
    out, seed, index = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    d = os.path.dirname(out)
    km20 = CQSKM(20, list(range(20)), [tuple((y + 1) % 20 for y in range(20))])
    cnf, rv = km20.cnf()
    found = []
    for i in range(index + 1):
        p = os.path.join(d, f"z20_km_{i}.cnf")
        cnf.write(p)
        st, model, dt = kissat(p, 300, seed=seed + i, log=p + ".log")
        assert st == "SAT", f"Z20 KM sample {i}: {st}"
        sel = [j for j, x in enumerate(rv) if x in model]
        found.append(sel)
        cnf.add([-rv[j] for j in sel])
    S = sorted(tuple(sorted(b)) for b in km20.blocks_of(found[index]))
    assert len(S) == 285
    cnt = {}
    for b in S:
        for t in combinations(b, 3):
            cnt[t] = cnt.get(t, 0) + 1
    assert len(cnt) == 1140 and set(cnt.values()) == {1}, "not an SQS(20)"
    lab = lambda l, y: 20 * l + y
    Q = set()
    for b in S:
        for l1 in range(4):
            for l2 in range(4):
                for l3 in range(4):
                    l4 = l1 ^ l2 ^ l3
                    if l1 == l2 == l3 == l4:
                        continue
                    Q.add(tuple(sorted((lab(l1, b[0]), lab(l2, b[1]), lab(l3, b[2]), lab(l4, b[3])))))
    for y, z in combinations(range(20), 2):
        for dd in (1, 2, 3):
            for l in range(4):
                for m in range(4):
                    Q.add(tuple(sorted((lab(l, y), lab(l ^ dd, y), lab(m, z), lab(m ^ dd, z)))))
    for y in range(20):
        Q.add(tuple(sorted(lab(l, y) for l in range(4))))
    assert len(Q) == 19400, len(Q)
    cnt = {}
    for b in Q:
        for t in combinations(b, 3):
            cnt[t] = cnt.get(t, 0) + 1
    universe = {t for t in combinations(range(80), 3) if len({p // 20 for p in t}) > 1}
    assert set(cnt) == universe and set(cnt.values()) == {1}, "Q(S) is not a CQS(20^4:0)"
    spec = grp.build("A4xC", 4, 20)
    for gen in spec["gens"]:
        assert all(tuple(sorted(gen[p] for p in b)) in Q for b in Q), "not A4 x C20-invariant"
    km = CQSKM(80, spec["group_of"], spec["gens"])
    rows = [j for j, (lab_, _) in enumerate(km.rows) if tuple(int(x) for x in km.Q[lab_]) in Q]
    assert sorted(tuple(sorted(b)) for b in km.blocks_of(rows)) == sorted(Q)
    rec = {"group": "A4xC", "g": 20, "source": "quadrupled cyclic SQS(20)", "z20_seed": seed, "z20_index": index,
           "sqs20_blocks": S, "samples": [{"sample": 0, "km_status": "CONSTRUCTED", "rows": rows}]}
    with xopen(out) as fh:
        json.dump(rec, fh)
    print("cyclic SQS(20) ok; Q(S) is an A4xC20-invariant CQS(20^4:0) with", len(rows), "KM rows")


if __name__ == "__main__":
    main()

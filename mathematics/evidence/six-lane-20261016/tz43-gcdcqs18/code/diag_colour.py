#!/usr/bin/env python3
"""README A4 diagnostic: for a pipeline_s5 run directory (summary.json with sample rows) rebuild the KM design and
report the derived triples at 0 whose R-orbit has NO admissible class placement in the anchored colouring model
(an empty exactly-one constraint, i.e. an immediate UNSAT), grouped by type.  Read-only on the run.
Usage: diag_colour.py RUNDIR SAMPLE SK AVOID"""
import lane_guard  # noqa: F401

import collections
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lanelib import closure, comp, inverse  # noqa: E402
from cqs_km_s import CQSKMS  # noqa: E402
import colour_model as cm  # noqa: E402
from pipeline_s import derived  # noqa: E402
from pipeline_s2 import cyclic_subgroup  # noqa: E402
import pipeline_s5 as p5  # noqa: E402


def main():
    rundir, sample, sk, avoid = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    summ = json.load(open(os.path.join(rundir, "summary.json")))
    rows = summ["samples"][sample]["rows"]
    N, v = 72, 74
    group_of = [p5.dec(p)[0] % 4 for p in range(N)] + [-1, -1]
    gens = [p5.perm(lambda a_, z1, z2: (a_ + 1, z1, z2), True), p5.perm(lambda a_, z1, z2: (a_, z1 + 1, z2), False),
            p5.perm(lambda a_, z1, z2: (a_, z1, z2 + 1), False)]

    def S(a_, z1, z2):
        for _ in range(sk):
            z1, z2 = (z1 - z2) % 3, (z1 + z2) % 3
        return a_, z1, z2
    gens.append(p5.perm(S, False))
    G = closure(gens, v)
    km = CQSKMS(v, group_of, gens)
    blocks = km.blocks_of(rows)
    x, anchor = 0, 72
    R = [e for e in G if e[x] == x]
    der = derived(blocks, x)
    hole = {q for q in range(v) if (group_of[q] == 0 or group_of[q] == -1) and q != x}
    toks = avoid.split(";")
    stabs = [cyclic_subgroup(R, int(t)) for t in toks]
    seen, aorb = set(), []
    for t in sorted(t for t in der if anchor in t):
        if t in seen:
            continue
        seen |= {cm.img(gg, t) for gg in R}
        aorb.append([gg for gg in R if cm.img(gg, t) == t])
    allst = stabs + aorb
    flags = [True] * len(stabs) + [False] * len(aorb)
    fixed = {q for q in range(v) if all(e[q] == q for e in R)}
    bad = collections.Counter()
    examples = {}
    seen = set()
    for t in sorted(der):
        if t in seen:
            continue
        orb = {cm.img(gg, t) for gg in R}
        seen |= orb
        stab = [gg for gg in R if cm.img(gg, t) == t]
        n_ok = 0
        for k, Sg in enumerate(allst):
            if flags[k] and set(t) & hole:
                continue
            Sset = set(Sg)
            if all(h in Sset for h in stab):  # abelian R: class stabilizer must contain Stab(t)
                n_ok += 1
        if n_ok == 0:
            key = (len(stab), "hole" if set(t) & hole else "free", len(set(t) & fixed))
            bad[key] += 1
            examples.setdefault(key, t)
    print(json.dumps({"R_order": len(R), "class_stabilizer_orders": [len(s) for s in allst],
                      "anchored_orbits": len(aorb), "triple_orbits_without_placement": {str(k): c for k, c in bad.items()},
                      "examples": {str(k): [list(t), [p5.dec(q) if q < 72 else q for q in t]] for k, t in examples.items()}}))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""README E10, ingredient I1: a 1-FG(3, ({4}, {5}), 16) of type 4^4 on AG(2, 4) (stdlib + kissat).

Points of AG(2,4): (u, w), u, w in F4 = {0,1,2,3} (XOR addition, w-multiplication 1->2->3->1),
label 4u + w.  Lines: {(u, w) : a*u + b*w = c}.  Groups G: the parallel class u = const
(lines u = 0, 1, 2, 3); B: the other 16 lines.  Affine hyperovals: 6-subsets of AG(2,4) with no
three collinear (computed by enumeration: the 6-arcs).  T: one 5-subset of each affine hyperoval,
chosen by a SAT model (variable f(O, p): hyperoval O drops point p; exactly one per O; every
non-collinear triple covered exactly once by the chosen 5-arcs).
Usage: ag24_arcs.py OUTDIR   (writes model.cnf, kissat log, fg.json; exclusive create)"""
import itertools
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402

MUL = [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 3, 1], [0, 3, 1, 2]]


def lines():
    pts = [(u, w) for u in range(4) for w in range(4)]
    L = set()
    for a, b in ((1, 0), (0, 1), (1, 1), (1, 2), (1, 3)):
        for c in range(4):
            L.add(frozenset(4 * u + w for (u, w) in pts if MUL[a][u] ^ MUL[b][w] == c))
    L = sorted(tuple(sorted(l)) for l in L)
    assert len(L) == 20 and all(len(l) == 4 for l in L)
    return L


def main():
    out = sys.argv[1]
    fresh_dir(out)
    L = lines()
    coll = {t for l in L for t in itertools.combinations(l, 3)}
    groups = [l for l in L if all(p // 4 == l[0] // 4 for p in l)]
    assert len(groups) == 4
    B = [l for l in L if l not in groups]
    arcs6 = [s for s in itertools.combinations(range(16), 6) if not any(t in coll for t in itertools.combinations(s, 3))]
    triples = [t for t in itertools.combinations(range(16), 3) if t not in coll]
    assert len(triples) == 480
    nv = 0
    var = {}
    for oi, O in enumerate(arcs6):
        for p in O:
            nv += 1
            var[(oi, p)] = nv
    clauses = []
    for oi, O in enumerate(arcs6):
        lits = [var[(oi, p)] for p in O]
        clauses.append(lits)
        clauses += [[-a, -b] for a, b in itertools.combinations(lits, 2)]
    containing = {t: [oi for oi, O in enumerate(arcs6) if set(t) <= set(O)] for t in triples}
    for t in triples:
        # t covered by O iff the dropped point of O is not in t
        cov = [[var[(oi, p)] for p in arcs6[oi] if p not in t] for oi in containing[t]]
        # at least one: OR over O of (OR of cov lits); at most one: no two O both cover
        clauses.append([l for c in cov for l in c])
        for c1, c2 in itertools.combinations(cov, 2):
            for a in c1:
                for b in c2:
                    clauses.append([-a, -b])
    cnf = os.path.join(out, "model.cnf")
    with xopen(cnf) as fh:
        fh.write(f"p cnf {nv} {len(clauses)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in clauses))
    r = subprocess.run(["kissat", "-q", "--time=600", "--seed=1", cnf], capture_output=True, text=True)
    with xopen(cnf + ".log") as fh:
        fh.write(r.stdout)
    model = {int(x) for line in r.stdout.splitlines() if line.startswith("v ") for x in line[2:].split() if int(x) > 0}
    status = "SAT" if "s SATISFIABLE" in r.stdout else ("UNSAT" if "s UNSATISFIABLE" in r.stdout else "UNKNOWN")
    rec = {"points": 16, "lines": L, "groups": groups, "B": B, "affine_hyperovals": len(arcs6),
           "triples_per_hyperoval_pair_check": sorted(set(len(v) for v in containing.values())),
           "cnf_vars": nv, "cnf_clauses": len(clauses), "status": status}
    if status == "SAT":
        T = []
        for oi, O in enumerate(arcs6):
            drop = [p for p in O if var[(oi, p)] in model]
            assert len(drop) == 1
            T.append([p for p in O if p != drop[0]])
        rec["T"] = T
    with xopen(os.path.join(out, "fg.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in rec if k not in ("lines", "B", "T")}))


if __name__ == "__main__":
    main()

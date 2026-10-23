#!/usr/bin/env python3
"""README E10, ingredient I3: an FDH(5, 8, 4, 3) = FDGDD(3, 4, 5{8}) (stdlib + kissat).

Points (i, a) -> 8i + a, i in Z5 (groups), a in {0..7}.  Coordinate group COORD = "E" (F2^3, XOR)
or "C" (Z8).  Design group Gamma = Z5 x COORD acting regularly ((i, a) -> (i + k, a (+) e)).
Coupled model: y_r for every Gamma-orbit r of transverse 4-sets whose development covers every
transverse triple of the column orbits it meets exactly once (KM rows; columns = orbits of
transverse triples, all orbits free); every column covered exactly once.  Kirkman frame at
x = (0, 0): the potential derived triples are the 4-sets through x of valid rows (present iff the
row is chosen); class (y, j), y in {1,2,3,4} the missing group, j in {0..3}; z(t, j) puts a present
triple t (missing group y_t) into class (y_t, j); every class contains every point of the three
groups other than 0 and y exactly once (a parallel class of 24 points).  Symmetry breaking (sound):
for each y, the triples through the least point p_y outside groups 0 and y fill classes j = 0..3
in increasing triple order.  Transport: the frame at g(x) is g(frame at x).
Usage: fdh_search.py COORD OUTDIR TIMEOUT SEED      (writes model.cnf, log, fdh certificate)"""
import itertools
import json
import os
import subprocess
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import CNF  # noqa: E402


def coord_ops(kind):
    if kind == "E":
        return (lambda a, e: a ^ e), list(range(8))
    return (lambda a, e: (a + e) % 8), list(range(8))


def main():
    kind, out, tl, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    fresh_dir(out)
    add, E = coord_ops(kind)
    G = [(k, e) for k in range(5) for e in E]
    act = lambda g, p: 8 * ((p // 8 + g[0]) % 5) + add(p % 8, g[1])
    gof = lambda p: p // 8
    trans = lambda S: len({gof(p) for p in S}) == len(S)
    canon = lambda S: min(tuple(sorted(act(g, p) for p in S)) for g in G)
    cols = sorted({canon(t) for t in itertools.combinations(range(40), 3) if trans(t)})
    cidx = {c: i for i, c in enumerate(cols)}
    quads = sorted({canon(q) for q in itertools.combinations(range(40), 4) if trans(q)})
    rows = []
    for q in quads:
        sub = [cidx[canon(t)] for t in itertools.combinations(q, 3)]
        if len(set(sub)) == 4:  # free orbits: each column met once (multiplicity 1)
            rows.append((q, sub))
    cnf = CNF()
    yv = [cnf.var() for _ in rows]
    bycol = defaultdict(list)
    for ri, (q, sub) in enumerate(rows):
        for c in sub:
            bycol[c].append(yv[ri])
    assert len(bycol) == len(cols)
    for c in range(len(cols)):
        cnf.exactly_one(bycol[c])
    x = 0
    pot = {}  # derived triple at x -> row index
    for ri, (q, _) in enumerate(rows):
        for g in G:
            img = tuple(sorted(act(g, p) for p in q))
            if x in img:
                t = tuple(p for p in img if p != x)
                assert t not in pot or pot[t] == ri
                pot[t] = ri
    missing = {t: ({1, 2, 3, 4} - {gof(p) for p in t}).pop() for t in pot}
    z = {}
    for t, ri in pot.items():
        lits = []
        for j in range(4):
            z[(t, j)] = cnf.var()
            lits.append(z[(t, j)])
            cnf.add([-z[(t, j)], yv[ri]])
        cnf.add([-yv[ri]] + lits)
        cnf.amo(lits)
    for y in range(1, 5):
        for j in range(4):
            for p in range(8, 40):
                if gof(p) == y:
                    continue
                cnf.exactly_one([z[(t, j)] for t in pot if missing[t] == y and p in t])
    nsb = 0
    for y in range(1, 5):
        py = min(p for p in range(8, 40) if gof(p) != y)
        Ts = sorted(t for t in pot if missing[t] == y and py in t)
        for a, b in itertools.combinations(range(len(Ts)), 2):
            for ja in range(4):
                for jb in range(ja + 1):
                    cnf.add([-z[(Ts[a], ja)], -z[(Ts[b], jb)]])
                    nsb += 1
    path = os.path.join(out, "model.cnf")
    sha = cnf.write(path)
    r = subprocess.run(["kissat", "-q", f"--time={tl}", f"--seed={seed}", path], capture_output=True, text=True)
    with xopen(path + ".log") as fh:
        fh.write(r.stdout)
    status = "SAT" if "s SATISFIABLE" in r.stdout else ("UNSAT" if "s UNSATISFIABLE" in r.stdout else "UNKNOWN")
    rec = {"coord": kind, "columns": len(cols), "rows": len(rows), "potential_derived_triples": len(pot),
           "vars": cnf.nv, "clauses": len(cnf.clauses), "symbreak_clauses": nsb, "cnf_sha256": sha, "status": status}
    if status == "SAT":
        model = {int(v) for line in r.stdout.splitlines() if line.startswith("v ") for v in line[2:].split() if int(v) > 0}
        chosen = [rows[ri][0] for ri in range(len(rows)) if yv[ri] in model]
        blocks = sorted({tuple(sorted(act(g, p) for p in q)) for q in chosen for g in G})
        classes = [[t for t in pot if missing[t] == y and z[(t, j)] in model] for y in range(1, 5) for j in range(4)]
        frames = {}
        for g in G:
            xp = act(g, x)
            frames[xp] = [sorted(tuple(sorted(act(g, p) for p in t)) for t in C) for C in classes]
        lines = ["FDH 5 8", "GROUPS"] + [" ".join(str(8 * i + a) for a in range(8)) for i in range(5)] + ["BLOCKS"]
        lines += [" ".join(map(str, b)) for b in blocks]
        for p in range(40):
            lines.append(f"POINT {p}")
            for j, C in enumerate(frames[p]):
                lines.append(f"CLASS {j}")
                lines += [" ".join(map(str, t)) for t in C]
        cert = os.path.join(out, "fdh_5_8.txt")
        with xopen(cert) as fh:
            fh.write("\n".join(lines) + "\n")
        rec["certificate"] = cert
        rec["blocks"] = len(blocks)
    with xopen(os.path.join(out, "summary.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


if __name__ == "__main__":
    main()

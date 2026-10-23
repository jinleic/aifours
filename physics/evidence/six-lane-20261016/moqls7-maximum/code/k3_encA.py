#!/usr/bin/env python3
"""k3_encA.py: K3 support-pattern CNF (encoder A). Lane moqls7-maximum.

K3 = {Psi1, Psi2, Psi3}, all non-classical, mutually orthogonal, standard form (row 0 = e_0..e_6).
Necessary conditions (same families as k2_encA without a classical square):
  allowed: supp Psi_a(i,j) avoids j;
  D   pairwise disjointness at every cell off row 0;
  per square: F1-F4 on rows and columns;
  for every pair of squares (a,b): T2 (no cell pair with single overlaps in both), T3 (off-diagonal coordinate
  pairs covered), T4 (single coverage forces weight 1 in both);
  W3  (--w3) every square has an entry of weight >= 3 (review/K1-THEOREM.r1.md section 8); with --sym the weight-3
      entry of Psi1 is placed at cell (1,0) (row permutation fixing row 0, and column permutation with the same
      relabelling of the basis in all squares, preserve standard form).
Usage: k3_encA.py [--w3] [--sym] [--fix-json F] --out F.cnf
"""
import argparse
import itertools
import json

from k2_encA import CNF, at_least

P = 7
CELLS = [(i, j) for i in range(1, P) for j in range(P)]


def build(w3=False, sym=False, fix=None, squares=(1, 2, 3)):
    F = CNF()
    x = {}
    for a in squares:
        for (i, j) in CELLS:
            for k in range(P):
                if k != j:
                    x[(a, i, j, k)] = F.new()
    lits = lambda a, p: [x[(a, p[0], p[1], k)] for k in range(P) if k != p[1]]
    for a in squares:
        for p in CELLS:
            F.add(lits(a, p))                                           # F1
    for a, b in itertools.combinations(squares, 2):                     # D
        for p in CELLS:
            for k in range(P):
                if k != p[1]:
                    F.add([-x[(a, p[0], p[1], k)], -x[(b, p[0], p[1], k)]])
    o = {}
    def ov(a, p, q, k):
        key = (a, p, q, k)
        if key not in o:
            v = F.new()
            o[key] = v
            F.add([-v, x[(a, p[0], p[1], k)]])
            F.add([-v, x[(a, q[0], q[1], k)]])
            F.add([v, -x[(a, p[0], p[1], k)], -x[(a, q[0], q[1], k)]])
        return o[key]
    pairs = list(itertools.combinations(CELLS, 2))
    common = {(p, q): [k for k in range(P) if k != p[1] and k != q[1]] for p, q in pairs}
    def nsingle(a, p, q, k):
        return [-ov(a, p, q, k)] + [ov(a, p, q, k2) for k2 in common[(p, q)] if k2 != k]
    for a in squares:                                                   # F2 rows/columns
        for p, q in pairs:
            if p[0] == q[0] or p[1] == q[1]:
                for k in common[(p, q)]:
                    F.add(nsingle(a, p, q, k))
    for a, b in itertools.combinations(squares, 2):                     # T2
        for p, q in pairs:
            if p[0] == q[0] or p[1] == q[1]:
                continue
            for k in common[(p, q)]:
                for k2 in common[(p, q)]:
                    F.add(nsingle(a, p, q, k) + nsingle(b, p, q, k2))
    for a in squares:                                                   # F3/F4 rows, columns
        for i in range(1, P):
            line = [(i, j) for j in range(P)]
            for k in range(P):
                cov = [p for p in line if k != p[1]]
                F.add([x[(a, p[0], p[1], k)] for p in cov])
                for p in cov:
                    others = [x[(a, q[0], q[1], k)] for q in cov if q != p]
                    for k2 in range(P):
                        if k2 != k and k2 != p[1]:
                            F.add([-x[(a, p[0], p[1], k)]] + others + [-x[(a, p[0], p[1], k2)]])
        for j in range(P):
            line = [(i, j) for i in range(1, P)]
            for k in range(P):
                if k == j:
                    continue
                F.add([x[(a, p[0], p[1], k)] for p in line])
                for p in line:
                    others = [x[(a, q[0], q[1], k)] for q in line if q != p]
                    for k2 in range(P):
                        if k2 != k and k2 != j:
                            F.add([-x[(a, p[0], p[1], k)]] + others + [-x[(a, p[0], p[1], k2)]])
    for a, b in itertools.combinations(squares, 2):                     # T3, T4
        for k1 in range(P):
            for k2 in range(P):
                if k1 == k2:
                    continue
                cells = [p for p in CELLS if k1 != p[1] and k2 != p[1]]
                z = {}
                for p in cells:
                    v = F.new()
                    z[p] = v
                    F.add([-v, x[(a, p[0], p[1], k1)]])
                    F.add([-v, x[(b, p[0], p[1], k2)]])
                    F.add([v, -x[(a, p[0], p[1], k1)], -x[(b, p[0], p[1], k2)]])
                F.add([z[p] for p in cells])
                for p in cells:
                    others = [z[q] for q in cells if q != p]
                    for c, kk in ((a, k1), (b, k2)):
                        for k3 in range(P):
                            if k3 != kk and k3 != p[1]:
                                F.add([-z[p]] + others + [-x[(c, p[0], p[1], k3)]])
    if w3:
        for a in squares:
            if sym and a == squares[0]:
                at_least(F, lits(a, (1, 0)), 3)
                continue
            ws = []
            for p in CELLS:
                g = F.new()
                ws.append(g)
                at_least(F, lits(a, p), 3, guard=g)
            F.add(ws)
    if fix:
        for a in squares:
            key = "S%d" % a
            if key in fix:
                for (i, j) in CELLS:
                    S = set(fix[key][i][j])
                    for k in range(P):
                        if k != j:
                            F.add([x[(a, i, j, k)]] if k in S else [-x[(a, i, j, k)]])
    return F, {"%d,%d,%d,%d" % key: v for key, v in x.items()}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--w3", action="store_true")
    ap.add_argument("--sym", action="store_true")
    ap.add_argument("--fix-json", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map", default=None)
    a = ap.parse_args()
    F, vmap = build(a.w3, a.sym, json.load(open(a.fix_json)) if a.fix_json else None)
    open(a.out, "w").write(F.text())
    if a.map:
        json.dump(vmap, open(a.map, "w"))
    print("vars", F.nv, "clauses", len(F.cl))

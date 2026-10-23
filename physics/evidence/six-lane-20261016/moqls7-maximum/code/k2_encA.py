#!/usr/bin/env python3
"""k2_encA.py: K2 support-pattern CNF (encoder A). Lane moqls7-maximum.

K2 = {Psi1, Psi2, L}: Psi1, Psi2 non-classical, L classical, all mutually orthogonal, all in standard form
(row 0 = e_0..e_6). Rows 1..6 are permuted so that L is reduced (L(0,j) = j, L(i,0) = i). Necessary conditions
(review/K2-ENCODING.md):
  allowed: supp Psi_a(i,j) avoids j (column ONB through (0,j)) and L(i,j) (L-line ONB through (0,L(i,j)));
  D   disjointness at every cell off row 0 (Psi1 x Psi2 orthogonal to e_k x e_k = (0,k) product);
  per square a, on every row, column and L-line: F1 nonempty, F2 no single shared coordinate, F3 coverage,
  F4 single coverage forces weight 1;
  T2  for every two cells p != q: not (|S1p & S1q| = 1 and |S2p & S2q| = 1) (product-vector orthogonality);
  T3  every off-diagonal coordinate pair (k1,k2), k1 != k2, lies in S1(p) x S2(p) for some cell p off row 0;
  T4  a pair (k1,k2) covered by exactly one cell forces weight 1 in both squares there;
  W3  (--w3) each of Psi1, Psi2 has an entry of weight >= 3 (reduction in review/K1-THEOREM.r1.md section 8).
Options for controls: --fix-json F (unit clauses for L and supports), --drop-psi2, --drop-L-lines-for-psi2.
Usage: k2_encA.py [--w3] [--fix-json F] --out F.cnf --map F.json
"""
import argparse
import itertools
import json

P = 7
CELLS = [(i, j) for i in range(1, P) for j in range(P)]


class CNF:
    def __init__(self):
        self.nv = 0
        self.cl = []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.cl.append(list(c))

    def text(self):
        return "p cnf %d %d\n" % (self.nv, len(self.cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in self.cl)


def at_least(F, lits, t, guard=None):
    """guard -> at least t of lits true (via: every subset of size len-t+1 has a true literal)."""
    n = len(lits)
    if t <= 0:
        return
    if t > n:
        F.add([-guard] if guard else [])
        return
    for sub in itertools.combinations(lits, n - t + 1):
        F.add(([-guard] if guard else []) + list(sub))


def build(w3=False, fix=None, drop_psi2=False):
    F = CNF()
    squares = (1,) if drop_psi2 else (1, 2)
    # Latin square L (reduced)
    l = {}
    for i in range(P):
        for j in range(P):
            for s in range(P):
                l[(i, j, s)] = F.new()
    for i in range(P):
        for j in range(P):
            fixed = j if i == 0 else (i if j == 0 else None)
            if fixed is not None:
                for s in range(P):
                    F.add([l[(i, j, s)]] if s == fixed else [-l[(i, j, s)]])
            F.add([l[(i, j, s)] for s in range(P)])
            for s, t in itertools.combinations(range(P), 2):
                F.add([-l[(i, j, s)], -l[(i, j, t)]])
    for s in range(P):
        for i in range(P):
            F.add([l[(i, j, s)] for j in range(P)])
            for j, j2 in itertools.combinations(range(P), 2):
                F.add([-l[(i, j, s)], -l[(i, j2, s)]])
        for j in range(P):
            F.add([l[(i, j, s)] for i in range(P)])
            for i, i2 in itertools.combinations(range(P), 2):
                F.add([-l[(i, j, s)], -l[(i2, j, s)]])
    # supports
    x = {}
    for a in squares:
        for (i, j) in CELLS:
            for k in range(P):
                if k != j:
                    x[(a, i, j, k)] = F.new()
                    F.add([-x[(a, i, j, k)], -l[(i, j, k)]])            # avoids L(i,j)
    def X(a, p, k):
        i, j = p
        if i == 0:
            return "T" if k == j else "F"
        if k == j:
            return "F"
        return x[(a, i, j, k)]
    def lits(a, p):
        return [X(a, p, k) for k in range(P) if X(a, p, k) not in ("T", "F")]
    for a in squares:
        for p in CELLS:
            F.add(lits(a, p))                                           # F1
    if not drop_psi2:
        for p in CELLS:                                                 # D
            for k in range(P):
                if k != p[1]:
                    F.add([-x[(1, p[0], p[1], k)], -x[(2, p[0], p[1], k)]])
    # overlap indicators for all pairs of off-row-0 cells
    o = {}
    def ov(a, p, q, k):
        key = (a, p, q, k)
        if key not in o:
            v = F.new()
            o[key] = v
            F.add([-v, X(a, p, k)])
            F.add([-v, X(a, q, k)])
            F.add([v, -X(a, p, k), -X(a, q, k)])
        return o[key]
    pairs = list(itertools.combinations(CELLS, 2))
    common = {}
    for p, q in pairs:
        common[(p, q)] = [k for k in range(P) if k != p[1] and k != q[1]]
    def single_clauses(a, p, q, k):
        """literals whose disjunction says: NOT(single overlap exactly at k)."""
        return [-ov(a, p, q, k)] + [ov(a, p, q, k2) for k2 in common[(p, q)] if k2 != k]
    # same-symbol indicator e(p,q) for pairs not in the same row/column
    e = {}
    for p, q in pairs:
        if p[0] != q[0] and p[1] != q[1]:
            v = F.new()
            e[(p, q)] = v
            for s in range(P):
                F.add([-l[(p[0], p[1], s)], -l[(q[0], q[1], s)], v])
                F.add([-v, -l[(p[0], p[1], s)], l[(q[0], q[1], s)]])
    for a in squares:                                                   # F2 on rows, columns, L-lines
        for p, q in pairs:
            for k in common[(p, q)]:
                if p[0] == q[0] or p[1] == q[1]:
                    F.add(single_clauses(a, p, q, k))
                else:
                    F.add([-e[(p, q)]] + single_clauses(a, p, q, k))
    if not drop_psi2:                                                   # T2
        for p, q in pairs:
            if p[0] == q[0] or p[1] == q[1]:
                continue                                                # implied by F2
            for k in common[(p, q)]:
                for k2 in common[(p, q)]:
                    F.add([e[(p, q)]] + single_clauses(1, p, q, k) + single_clauses(2, p, q, k2))
    # F3/F4 on rows and columns (row 0 fixed; column j contains (0,j) with e_j)
    for a in squares:
        for i in range(1, P):
            line = [(i, j) for j in range(P)]
            for k in range(P):
                cov = [X(a, p, k) for p in line if X(a, p, k) != "F"]
                F.add(cov)
                for p in line:
                    if X(a, p, k) == "F":
                        continue
                    others = [X(a, q, k) for q in line if q != p and X(a, q, k) != "F"]
                    for k2 in range(P):
                        if k2 != k and X(a, p, k2) != "F":
                            F.add([-X(a, p, k)] + others + [-X(a, p, k2)])
        for j in range(P):
            line = [(i, j) for i in range(1, P)]                     # coordinate j is covered by (0,j) only
            for k in range(P):
                if k == j:
                    continue
                cov = [X(a, p, k) for p in line]
                F.add(cov)
                for p in line:
                    others = [X(a, q, k) for q in line if q != p]
                    for k2 in range(P):
                        if k2 != k and k2 != j:
                            F.add([-X(a, p, k)] + others + [-X(a, p, k2)])
    # F3/F4 on L-lines: symbol s line = (0,s) plus cells with L = s; coordinate s covered only by (0,s)
    y = {}
    for a in squares:
        for p in CELLS:
            for s in range(P):
                for k in range(P):
                    if k == s or k == p[1]:
                        continue
                    v = F.new()
                    y[(a, p, s, k)] = v
                    F.add([-v, l[(p[0], p[1], s)]])
                    F.add([-v, x[(a, p[0], p[1], k)]])
                    F.add([v, -l[(p[0], p[1], s)], -x[(a, p[0], p[1], k)]])
        for s in range(P):
            for k in range(P):
                if k == s:
                    continue
                cells = [p for p in CELLS if (a, p, s, k) in y]
                F.add([y[(a, p, s, k)] for p in cells])
                for p in cells:
                    others = [y[(a, q, s, k)] for q in cells if q != p]
                    for k2 in range(P):
                        if k2 != k and k2 != p[1]:
                            F.add([-y[(a, p, s, k)]] + others + [-x[(a, p[0], p[1], k2)]])
    if not drop_psi2:                                                   # T3, T4
        z = {}
        for k1 in range(P):
            for k2 in range(P):
                if k1 == k2:
                    continue
                cells = [p for p in CELLS if k1 != p[1] and k2 != p[1]]
                for p in cells:
                    v = F.new()
                    z[(p, k1, k2)] = v
                    F.add([-v, x[(1, p[0], p[1], k1)]])
                    F.add([-v, x[(2, p[0], p[1], k2)]])
                    F.add([v, -x[(1, p[0], p[1], k1)], -x[(2, p[0], p[1], k2)]])
                F.add([z[(p, k1, k2)] for p in cells])
                for p in cells:
                    others = [z[(q, k1, k2)] for q in cells if q != p]
                    for a, kk in ((1, k1), (2, k2)):
                        for k3 in range(P):
                            if k3 != kk and k3 != p[1]:
                                F.add([-z[(p, k1, k2)]] + others + [-x[(a, p[0], p[1], k3)]])
    if w3:                                                              # W3
        for a in squares:
            ws = []
            for p in CELLS:
                g = F.new()
                ws.append(g)
                at_least(F, lits(a, p), 3, guard=g)
            F.add(ws)
    if fix:
        if "L" in fix:
            for i in range(P):
                for j in range(P):
                    F.add([l[(i, j, fix["L"][i][j])]])
        for a in squares:
            key = "S%d" % a
            if key in fix:
                for (i, j) in CELLS:
                    S = set(fix[key][i][j])
                    for k in range(P):
                        if k != j:
                            F.add([x[(a, i, j, k)]] if k in S else [-x[(a, i, j, k)]])
    vmap = {"l": {"%d,%d,%d" % key: v for key, v in l.items()},
            "x": {"%d,%d,%d,%d" % key: v for key, v in x.items()}}
    return F, vmap


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--w3", action="store_true")
    ap.add_argument("--fix-json", default=None)
    ap.add_argument("--drop-psi2", action="store_true")
    ap.add_argument("--out", required=True)
    ap.add_argument("--map", default=None)
    a = ap.parse_args()
    fix = json.load(open(a.fix_json)) if a.fix_json else None
    F, vmap = build(a.w3, fix, a.drop_psi2)
    open(a.out, "w").write(F.text())
    if a.map:
        json.dump(vmap, open(a.map, "w"))
    print("vars", F.nv, "clauses", len(F.cl))

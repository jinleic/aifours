#!/usr/bin/env python3
"""k1_sat.py: K1 support-pattern CNF (encoder A) for an ONB-assignment on a 4-net of order 7. Lane moqls7-maximum.

Frame: line 0 of class 0 ("row 0") carries the standard basis; the point of row 0 on the class-1 line labelled j
gets e_j. For a point p off row 0 let a_c(p) (c = 1, 2, 3) be the class-1 label of the point where p's class-c line
meets row 0. Then psi_p is orthogonal to e_{a_1(p)}, e_{a_2(p)}, e_{a_3(p)} (three distinct coordinates), so
supp(psi_p) is a subset of A(p) = [7] minus those 3.
Variables x[p,k] (k in A(p)): k in supp(psi_p). Clause families (each a necessary condition, see review/LEMMAS.md):
 F1 every point has nonempty support;
 F2 two points on a common line never share exactly one support coordinate (aux o = x[p,k] AND x[q,k]);
 F3 every coordinate is in some support on every line (a unitary has no zero column);
 F4 a coordinate covered by exactly one point of a line forces that point to have weight 1;
 F5 (optional, --hall) Hall conditions on every line: for 2 or 3 points, the union of supports has at least as many
    coordinates; for 2 or 3 coordinates, at least as many points meet them;
 F6 (--w3) some point off row 0 has weight >= 3 (K1 weight lemma, review/LEMMAS.md).
Output: DIMACS CNF on stdout or --out; a JSON variable map with --map.
Usage: k1_sat.py CLASSFILE IDX [--w3] [--hall] [--out F.cnf] [--map F.json]
"""
import argparse
import itertools
import json

P = 7


class CNF:
    def __init__(self):
        self.nv = 0
        self.cl = []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, c):
        self.cl.append(list(c))

    def dimacs(self):
        return "p cnf %d %d\n" % (self.nv, len(self.cl)) + "".join(" ".join(map(str, c)) + " 0\n" for c in self.cl)


def build(net, w3=True, hall=False):
    lines = [[q for q in range(49) if net[q][c] == b] for c in range(4) for b in range(P)]
    row0 = [q for q in range(49) if net[q][0] == 0]
    col_of = {q: net[q][1] for q in row0}                     # basis index of row-0 points
    meet = {}                                                 # (point, class) -> basis index where its line meets row 0
    for p in range(49):
        for c in (1, 2, 3):
            hit = [q for q in row0 if net[q][c] == net[p][c]]
            assert len(hit) == 1
            meet[(p, c)] = col_of[hit[0]]
    A = {}
    for p in range(49):
        if p in col_of:
            A[p] = {col_of[p]}
        else:
            bad = {meet[(p, c)] for c in (1, 2, 3)}
            assert len(bad) == 3
            A[p] = set(range(P)) - bad
    F = CNF()
    x = {}
    for p in range(49):
        for k in sorted(A[p]):
            x[(p, k)] = F.new()
    for p in col_of:
        F.add([x[(p, col_of[p])]])                            # row 0 fixed
    for p in range(49):                                       # F1
        F.add([x[(p, k)] for k in sorted(A[p])])
    for l in lines:                                           # F2
        for p, q in itertools.combinations(l, 2):
            common = sorted(A[p] & A[q])
            if not common:
                continue
            o = {}
            for k in common:
                o[k] = F.new()
                F.add([-o[k], x[(p, k)]])
                F.add([-o[k], x[(q, k)]])
                F.add([o[k], -x[(p, k)], -x[(q, k)]])
            for k in common:
                F.add([-o[k]] + [o[k2] for k2 in common if k2 != k])
    for l in lines:                                           # F3, F4
        for k in range(P):
            cov = [p for p in l if k in A[p]]
            if not cov:
                F.add([])
                continue
            F.add([x[(p, k)] for p in cov])
            for p in cov:
                others = [x[(q, k)] for q in cov if q != p]
                for k2 in sorted(A[p] - {k}):
                    F.add([-x[(p, k)]] + others + [-x[(p, k2)]])
    if hall:                                                  # F5
        for l in lines:
            for r in (2, 3):
                for R in itertools.combinations(l, r):
                    U = sorted(set().union(*[A[p] for p in R]))
                    # union of supports >= r : for every set Kc of size len(U)-r+1 of coordinates of U, some p in R
                    # has a support coordinate outside... encode directly: not (all supports inside a set of r-1 coords)
                    for K in itertools.combinations(U, r - 1):
                        out = [x[(p, k)] for p in R for k in sorted(A[p]) if k not in K]
                        F.add(out)
            for r in (2, 3):
                for K in itertools.combinations(range(P), r):
                    meeting = [p for p in l if A[p] & set(K)]
                    # at least r points of the line meet K: for every set of len(meeting)-r+1 points, one meets K
                    for S in itertools.combinations(meeting, max(len(meeting) - r + 1, 0)):
                        F.add([x[(p, k)] for p in S for k in sorted(A[p] & set(K))])
    if w3:                                                    # F6
        ws = []
        for p in range(49):
            if p in col_of or len(A[p]) < 3:
                continue
            w = F.new()
            ws.append(w)
            ks = sorted(A[p])
            for a_, b_ in itertools.combinations(ks, 2):
                F.add([-w, x[(p, a_)], x[(p, b_)]])
        F.add(ws)
    vmap = {"%d:%d" % k: v for k, v in x.items()}
    return F, vmap, {p: sorted(A[p]) for p in range(49)}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("classfile")
    ap.add_argument("idx", type=int)
    ap.add_argument("--w3", action="store_true")
    ap.add_argument("--hall", action="store_true")
    ap.add_argument("--out", default=None)
    ap.add_argument("--map", default=None)
    a = ap.parse_args()
    net = [tuple(q) for q in json.load(open(a.classfile))["classes"][a.idx]["net"]]
    F, vmap, A = build(net, a.w3, a.hall)
    txt = F.dimacs()
    if a.out:
        open(a.out, "w").write(txt)
    else:
        print(txt, end="")
    if a.map:
        json.dump({"x": vmap, "A": {str(p): v for p, v in A.items()}}, open(a.map, "w"))

#!/usr/bin/env python3
"""gram_enc.py: frame-free Gram-support CNF for sets of mutually orthogonal QLS(7). Lane moqls7-maximum.

Unknowns: for each quantum square a and each pair of cells p != q, g[a,p,q] <=> <psi_a,p, psi_a,q> != 0.
Lines: rows and columns (ONB lines of every square) plus, with --net-L, the symbol lines of a FIXED classical square L
(ONB lines of every quantum square by (C1)). Necessary conditions (review/GRAM-ENCODING.md):
  G1 collinear cells are orthogonal: g = 0 on every line;
  G2 frame consistency: for every line l and cells p, q off l, expanding in the ONB of l gives
     G_pq = sum_{r in l} conj(G_rp) G_rq, so #{r in l : g(p,r) and g(q,r)} = 0 forces g(p,q) = 0 and = 1 forces
     g(p,q) = 1;
  G3 the transition matrix between two lines is unitary: every point of one line off the other has a neighbour on it;
     a point with exactly one neighbour q on the other line is q's only neighbour on its own line;
  G5 product-vector orthogonality of squares a != b is exactly g_a(p,q) g_b(p,q) = 0 for all p != q;
     orthogonality to the classical L is exactly G1 on the L lines;
  G4 (--heavy) minimal-counterexample reduction (review/K1-THEOREM.r1.md section 8 plus Lemma 10 in an arbitrary
     basis): every quantum square has, for every one of its ONB lines l, a point with >= 3 neighbours on l.
Symmetry (--sym, K3 only): square 1 is heavy in the frame of row 0 at cell (1,0) with neighbours (0,1),(0,2),(0,3)
(row and column permutations preserve all conditions).
Usage: gram_enc.py --squares 3 [--net-L LJSON] [--heavy] [--sym] [--fix-json F] --out F.cnf [--map F.json]
"""
import argparse
import itertools
import json

P = 7
CELLS = [(i, j) for i in range(P) for j in range(P)]


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
    n = len(lits)
    if t > n:
        F.add([-guard] if guard else [])
        return
    for sub in itertools.combinations(lits, n - t + 1):
        F.add(([-guard] if guard else []) + list(sub))


def build(nsq=3, L=None, heavy=False, sym=False, fix=None):
    lines = [[(i, j) for j in range(P)] for i in range(P)] + [[(i, j) for i in range(P)] for j in range(P)]
    if L is not None:
        lines += [[c for c in CELLS if L[c[0]][c[1]] == s] for s in range(P)]
    collinear = set()
    for l in lines:
        for p, q in itertools.combinations(l, 2):
            collinear.add((p, q))
            collinear.add((q, p))
    F = CNF()
    squares = list(range(1, nsq + 1))
    g = {}
    for a in squares:
        for p, q in itertools.combinations(CELLS, 2):
            if (p, q) not in collinear:
                v = F.new()
                g[(a, p, q)] = v
                g[(a, q, p)] = v
    def G(a, p, q):
        return g.get((a, p, q))          # None means constant false (collinear)
    h = {}
    def H(a, p, q, r):
        """h = g(p,r) AND g(q,r); None if constant false."""
        if G(a, p, r) is None or G(a, q, r) is None:
            return None
        key = (a,) + tuple(sorted((p, q))) + (r,)
        if key not in h:
            v = F.new()
            h[key] = v
            F.add([-v, G(a, p, r)])
            F.add([-v, G(a, q, r)])
            F.add([v, -G(a, p, r), -G(a, q, r)])
        return h[key]
    for a in squares:
        for l in lines:                                                  # G2
            ls = set(l)
            off = [c for c in CELLS if c not in ls]
            for p, q in itertools.combinations(off, 2):
                hs = [H(a, p, q, r) for r in l]
                hs = [x for x in hs if x is not None]
                gpq = G(a, p, q)
                if gpq is not None:
                    F.add(hs + [-gpq])
                for x in hs:
                    others = [y for y in hs if y != x]
                    F.add([-x] + others + ([gpq] if gpq is not None else []))
        for l1, l2 in itertools.permutations(lines, 2):                  # G3 (ordered pairs)
            s1, s2 = set(l1), set(l2)
            for r in l1:
                if r in s2:
                    continue
                nb = [G(a, r, q) for q in l2 if q not in s1 and G(a, r, q) is not None]
                F.add(nb)
                for q in l2:
                    if q in s1 or G(a, r, q) is None:
                        continue
                    rest = [G(a, r, q2) for q2 in l2 if q2 != q and q2 not in s1 and G(a, r, q2) is not None]
                    for r2 in l1:
                        if r2 == r or r2 in s2 or G(a, r2, q) is None:
                            continue
                        F.add([-G(a, r, q)] + rest + [-G(a, r2, q)])
    for a, b in itertools.combinations(squares, 2):                      # G5
        for p, q in itertools.combinations(CELLS, 2):
            if G(a, p, q) is not None:
                F.add([-G(a, p, q), -G(b, p, q)])
    if heavy:                                                            # G4
        for a in squares:
            for li, l in enumerate(lines):
                ls = set(l)
                if sym and a == 1 and li == 0:
                    for r in [(0, 1), (0, 2), (0, 3)]:
                        F.add([G(1, (1, 0), r)])
                    continue
                guards = []
                for p in CELLS:
                    if p in ls:
                        continue
                    nb = [G(a, p, r) for r in l if G(a, p, r) is not None]
                    if len(nb) < 3:
                        continue
                    w = F.new()
                    guards.append(w)
                    at_least(F, nb, 3, guard=w)
                F.add(guards)
    if fix:
        for a in squares:
            key = "g%d" % a
            if key in fix:
                ones = {tuple(map(tuple, e)) for e in fix[key]}
                for p, q in itertools.combinations(CELLS, 2):
                    v = G(a, p, q)
                    if v is None:
                        assert (p, q) not in ones and (q, p) not in ones, ("collinear pair marked nonzero", a, p, q)
                        continue
                    F.add([v] if ((p, q) in ones or (q, p) in ones) else [-v])
    vmap = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v for (a, p, q), v in g.items() if p < q}
    return F, vmap


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--squares", type=int, default=3)
    ap.add_argument("--net-L", default=None, help="JSON 7x7 classical square (fixed)")
    ap.add_argument("--heavy", action="store_true")
    ap.add_argument("--sym", action="store_true")
    ap.add_argument("--fix-json", default=None)
    ap.add_argument("--out", required=True)
    ap.add_argument("--map", default=None)
    a = ap.parse_args()
    L = json.load(open(a.net_L)) if a.net_L else None
    F, vmap = build(a.squares, L, a.heavy, a.sym, json.load(open(a.fix_json)) if a.fix_json else None)
    open(a.out, "w").write(F.text())
    if a.map:
        json.dump(vmap, open(a.map, "w"))
    print("vars", F.nv, "clauses", len(F.cl))

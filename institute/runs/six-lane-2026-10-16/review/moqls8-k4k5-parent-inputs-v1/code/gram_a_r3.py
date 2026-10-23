"""Encoder GA revision 3 (adds --weight1: a classical square encoded as a weight-1 Gram square, with its K4 SB2).
Encoder GA revision 2 (adds --p4-all-cols; P4 flag variable names changed; otherwise as gram_a.py).
Encoder GA (exploratory; README §2 to be frozen before use as evidence): ALL-FRAMES Gram-pattern encoding of class K_m.

Variables g_s(p,q) for each quantum square s and unordered pair of distinct cells: "<Psi_s(p), Psi_s(q)> != 0".
Necessary conditions for a genuine configuration (Prop 1, Lemma 2, Parseval):
 G1  g_s(p,q) = 0 if p, q lie on a common line (row, column, classical symbol line).
 G2  not (g_s(p,q) and g_u(p,q)) for quantum s != u (Prop 1).
 G3  for two distinct FIXED lines l, l' (rows/columns; also classical lines in FIXED mode) the 8x8 overlap pattern
     [g_s(a,b)]_{a in l, b in l'} (diagonal entry 1 at the common point, if any) is the support of a unitary:
     every row/column nonempty, no two rows share exactly one column, no two columns share exactly one row.
 G4  for a FIXED line l and p, q not on l, with I = {a in l : g_s(a,p) and g_s(a,q)}:
     |I| = 1  =>  g_s(p,q) = 1   (single Parseval term);   |I| = 0  =>  g_s(p,q) = 0.
 G5  classical squares: GENERIC MOLS variables (first row identity, first square sorted L(i,0) = i), or FIXED.
 P4  every quantum square has a point off row 0 with >= 3 nonzero overlaps with row 0 (frame row 0; option: every row).
 SB2 (generic): Psi1's weight-3 point is (1,0); classical symbols at (1,0) are 1, 2, ...; the row-0 overlaps of (1,0)
     are: Psi1 -> three smallest remaining coordinates, Psi2.. -> one each.
Order N = 7 (Z7 slopes) or 8 (GF(8) slopes, x^3 = x + 1).
python -B gram_a.py --order 8 --mode generic --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --cnf X.cnf --map X.map.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys


def gmul8(a, b):
    r = 0
    for k in range(3):
        if (b >> k) & 1:
            r ^= a << k
    for d in (4, 3):
        if (r >> d) & 1:
            r ^= 0b1011 << (d - 3)
    return r


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []
        self.names = {}

    def var(self, name):
        if name not in self.names:
            self.nv += 1
            self.names[name] = self.nv
        return self.names[name]

    def add(self, lits):
        out = []
        for l in lits:
            if l is True:
                return
            if l is False:
                continue
            out.append(l)
        if not out:
            raise ValueError("empty clause")
        self.clauses.append(out)

    def AND(self, name, a, b):
        if a is False or b is False:
            return False
        if a is True:
            return b
        if b is True:
            return a
        if name in self.names:
            return self.names[name]
        v = self.var(name)
        self.add([-v, a])
        self.add([-v, b])
        self.add([v, -a, -b])
        return v


def neg(l):
    return (not l) if isinstance(l, bool) else -l


def build(N, mode, slopes, quantum, ngeneric, p4, p4_all_rows, sb2, fixg=None, g5=False, rowlex=False,
          p4_all_cols=False, weight1=None):
    f = CNF()
    cells = [(i, j) for i in range(N) for j in range(N)]
    base = max(quantum) + 1
    CL = list(range(base, base + (len(slopes) if mode == "fixed" else ngeneric)))

    def lin(s, i, j):
        return (j ^ gmul8(s, i)) if N == 8 else (j + s * i) % N

    def L(t, c, x):
        i, j = c
        if i == 0:
            return x == j
        if mode == "fixed":
            return x == lin(slopes[CL.index(t)], i, j)
        return f.var(("L%d" % t, c, x))

    if mode == "generic":
        off = [c for c in cells if c[0] > 0]
        for t in CL:
            for c in off:
                f.add([L(t, c, x) for x in range(N)])
                for x, y in itertools.combinations(range(N), 2):
                    f.add([neg(L(t, c, x)), neg(L(t, c, y))])
            for x in range(N):
                for i in range(N):
                    for j1, j2 in itertools.combinations(range(N), 2):
                        f.add([neg(L(t, (i, j1), x)), neg(L(t, (i, j2), x))])
                for j in range(N):
                    for i1, i2 in itertools.combinations(range(N), 2):
                        f.add([neg(L(t, (i1, j), x)), neg(L(t, (i2, j), x))])
        for ta, tb in itertools.combinations(CL, 2):
            for c in off:
                for x in range(N):
                    f.add([neg(L(ta, c, x)), neg(L(tb, c, x))])
            for c1, c2 in itertools.combinations(off, 2):
                for x in range(N):
                    for y in range(N):
                        if x != y:
                            f.add([neg(L(ta, c1, x)), neg(L(tb, c1, y)), neg(L(ta, c2, x)), neg(L(tb, c2, y))])
        if CL:
            for i in range(1, N):
                f.add([L(CL[0], (i, 0), i)])

    def g(s, p, q):
        if p == q:
            return True
        if p[0] == q[0] or p[1] == q[1]:
            return False
        if mode == "fixed":
            for t in CL:
                sl = slopes[CL.index(t)]
                if lin(sl, *p) == lin(sl, *q):
                    return False
        a, b = sorted((p, q))
        return f.var(("g", s, a, b))

    # G1 for generic classical lines
    if mode == "generic":
        for s in quantum:
            for p, q in itertools.combinations(cells, 2):
                gv = g(s, p, q)
                if gv is False:
                    continue
                for t in CL:
                    for x in range(N):
                        f.add([neg(gv), neg(L(t, p, x)), neg(L(t, q, x))])
    # G2
    for s, u in itertools.combinations(quantum, 2):
        for p, q in itertools.combinations(cells, 2):
            f.add([neg(g(s, p, q)), neg(g(u, p, q))])
    if fixg:
        for s, pairs in fixg.items():
            on = {tuple(map(tuple, pq)) for pq in pairs}
            for p, q in itertools.combinations(cells, 2):
                gv = g(s, p, q)
                if gv is False:
                    if (p, q) in on:
                        raise ValueError("fixed pattern violates a constant zero")
                    continue
                f.add([gv if (p, q) in on else neg(gv)])
    # fixed lines
    lines = [[(i, j) for j in range(N)] for i in range(N)] + [[(i, j) for i in range(N)] for j in range(N)]
    if mode == "fixed":
        for t in CL:
            sl = slopes[CL.index(t)]
            for x in range(N):
                lines.append([c for c in cells if lin(sl, *c) == x])

    def exactly_one_forbidden(lits):
        """forbid 'exactly one of lits true' (lits may contain constants)."""
        for k, l in enumerate(lits):
            if l is False:
                continue
            f.add([neg(l)] + [m for kk, m in enumerate(lits) if kk != k])

    # G3
    for s in quantum:
        for l1, l2 in itertools.combinations(lines, 2):
            M = [[g(s, a, b) for b in l2] for a in l1]
            for r in range(N):
                f.add(M[r])
                f.add([M[k][r] for k in range(N)])
            for r1, r2 in itertools.combinations(range(N), 2):
                both = [f.AND(("b3", s, l1[r1], l1[r2], l2[k]), M[r1][k], M[r2][k]) for k in range(N)]
                exactly_one_forbidden(both)
                bothc = [f.AND(("b3", s, l2[r1], l2[r2], l1[k]), M[k][r1], M[k][r2]) for k in range(N)]
                exactly_one_forbidden(bothc)
    # G4
    for s in quantum:
        for l in lines:
            ls = set(l)
            rest = [c for c in cells if c not in ls]
            for p, q in itertools.combinations(rest, 2):
                gpq = g(s, p, q)
                cs = []
                for a in l:
                    x, y = g(s, a, p), g(s, a, q)
                    cs.append(f.AND(("c4", s, a) + tuple(sorted((p, q))), x, y))
                for k, ck in enumerate(cs):          # |I| = 1  =>  g(p,q)
                    if ck is False:
                        continue
                    f.add([neg(ck)] + [m for kk, m in enumerate(cs) if kk != k] + [gpq])
                f.add([neg(gpq)] + cs)               # |I| = 0  =>  not g(p,q)
    # G5 (same ray): if in the frame of a fixed line l the support of q is {a}, then Psi_s(q) is proportional to
    # Psi_s(a), so g_s(p,q) = g_s(p,a) for every other point p.
    if g5:
        for s in quantum:
            for l in lines:
                ls = set(l)
                for q in cells:
                    if q in ls:
                        continue
                    ov = [g(s, a, q) for a in l]
                    for k, a in enumerate(l):
                        if ov[k] is False:
                            continue
                        u = f.var(("u5", s, tuple(l[0]), tuple(l[1]), q, a))
                        # u -> exactly {a}
                        f.add([-u, ov[k]])
                        for kk in range(N):
                            if kk != k:
                                f.add([-u, neg(ov[kk])])
                        f.add([u, neg(ov[k])] + [ov[kk] for kk in range(N) if kk != k])
                        for p in cells:
                            if p == q or p == a:
                                continue
                            gpq, gpa = g(s, p, q), g(s, p, a)
                            f.add([-u, neg(gpq), gpa])
                            f.add([-u, neg(gpa), gpq])
    # P4 (frame row 0; optionally every row frame and every column frame)
    frame_lines = [[(r, j) for j in range(N)] for r in (range(N) if p4_all_rows else [0])]
    if p4_all_cols:
        frame_lines += [[(i, c) for i in range(N)] for c in range(N)]
    for s in p4:
        for fl in frame_lines:
            fset = set(fl)
            flags = []
            for p in cells:
                if p in fset:
                    continue
                w = f.var(("w3", s, fl[0], fl[1], p))
                ov = [g(s, a, p) for a in fl]
                for K in itertools.combinations(range(N), N - 2):
                    f.add([-w] + [ov[k] for k in K])
                flags.append(w)
            f.add(flags)
    # ROWLEX (no classical squares only): rows 2..N-1 sorted so that the row-0-frame overlap vectors of the column-0
    # cells of Psi1 are lexicographically non-decreasing (bit k = g_1((0,k),(i,0)), k = 0..N-1 most significant first).
    if rowlex:
        assert mode == "generic" and not CL
        s1 = quantum[0]
        for i in range(2, N - 1):
            A = [g(s1, (0, k), (i, 0)) for k in range(N)]
            B = [g(s1, (0, k), (i + 1, 0)) for k in range(N)]
            # lexleq(A, B): prefix-equality chain e_k ("A[0..k-1] == B[0..k-1]")
            e_prev = True
            for k in range(N):
                # e_prev -> (A[k] -> B[k])
                f.add([neg(e_prev), neg(A[k]), B[k]])
                if k < N - 1:
                    e = f.var(("lexeq", i, k))
                    # e <-> e_prev and (A[k] <-> B[k]); only the direction e_prev & (A==B) -> e is needed for
                    # soundness of the lex constraint, both are added for fidelity
                    f.add([neg(e), e_prev] if e_prev is not True else [True])
                    f.add([neg(e), neg(A[k]), B[k]])
                    f.add([neg(e), A[k], neg(B[k])])
                    f.add([e, neg(e_prev), A[k], B[k]])
                    f.add([e, neg(e_prev), neg(A[k]), neg(B[k])])
                    e_prev = e
    # WEIGHT1 (K4 as five Gram squares): the label `weight1` is a classical square written as a Gram-pattern square:
    # every off-row-0 cell has exactly one nonzero overlap with row 0 (at least one is already implied by G3).
    if weight1:
        t = weight1
        for p in cells:
            if p[0] == 0:
                continue
            ov = [g(t, (0, k), p) for k in range(N)]
            for k1, k2 in itertools.combinations(range(N), 2):
                f.add([neg(ov[k1]), neg(ov[k2])])
    if sb2 and weight1:
        # K4 normalisation (README §7): weight-1 square symbol 1 at (1,0); Psi1 -> {2,3,4}; the other three quantum
        # squares -> {5}, {6}, {7}; rows 2..N-1 sorted by the weight-1 square's column 0 (symbol i at row i).
        qs = [s_ for s_ in quantum if s_ != weight1]
        assert mode == "generic" and not CL and len(qs) == 4
        for k in range(N):
            gv = g(weight1, (0, k), (1, 0))
            f.add([gv if k == 1 else neg(gv)])
        parts = [[2, 3, 4], [5], [6], [7]]
        for s_, part in zip(qs, parts):
            for k in range(N):
                gv = g(s_, (0, k), (1, 0))
                f.add([gv if k in part else neg(gv)])
        for i in range(2, N):
            f.add([g(weight1, (0, i), (i, 0))])
    # SB2
    if sb2 and not weight1:
        assert mode == "generic" and len(quantum) + len(CL) == N - 3
        for idx, t in enumerate(CL):
            f.add([L(t, (1, 0), idx + 1)])
        free = [k for k in range(1, N) if k > len(CL)]
        parts = [free[:3]] + [[k] for k in free[3:]]
        for s, part in zip(quantum, parts):
            for k in range(N):
                gv = g(s, (0, k), (1, 0))
                f.add([gv if k in part else neg(gv)])
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--order", type=int, choices=[7, 8], required=True)
    ap.add_argument("--mode", choices=["fixed", "generic"], required=True)
    ap.add_argument("--slopes", default="")
    ap.add_argument("--quantum", required=True)
    ap.add_argument("--ngeneric", type=int, default=0)
    ap.add_argument("--p4", default="none")
    ap.add_argument("--p4-all-rows", action="store_true")
    ap.add_argument("--p4-all-cols", action="store_true", help="P4 also in every column frame")
    ap.add_argument("--weight1", type=int, default=None, help="label of a quantum square forced to weight 1 (classical)")
    ap.add_argument("--sb2", action="store_true")
    ap.add_argument("--g5", action="store_true", help="same-ray condition G5")
    ap.add_argument("--rowlex", action="store_true", help="lex-leader on rows 2..N-1 (no classical squares)")
    ap.add_argument("--fixg", default=None, help="controls: JSON {label: [[p,q],...] nonzero pairs}")
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--map", required=True)
    a = ap.parse_args()
    slopes = [int(x) for x in a.slopes.split(",") if x]
    quantum = [int(ch) for ch in a.quantum]
    p4 = [] if a.p4 == "none" else [int(ch) for ch in a.p4]
    fixg = {int(k): v for k, v in json.load(open(a.fixg)).items()} if a.fixg else None
    f = build(a.order, a.mode, slopes, quantum, a.ngeneric, p4, a.p4_all_rows, a.sb2, fixg, a.g5, a.rowlex,
              a.p4_all_cols, a.weight1)
    with open(a.cnf, "x") as fh:
        fh.write("p cnf %d %d\n" % (f.nv, len(f.clauses)))
        for cl in f.clauses:
            fh.write(" ".join(map(str, cl)) + " 0\n")
    names = {json.dumps(k): v for k, v in f.names.items() if isinstance(k, tuple) and k[0] in ("g",)
             or isinstance(k, tuple) and isinstance(k[0], str) and k[0].startswith("L")}
    meta = {"encoder": "GA-r3", "argv": sys.argv, "python": sys.version, "vars": f.nv, "clauses": len(f.clauses),
            "cnf_sha256": hashlib.sha256(open(a.cnf, "rb").read()).hexdigest(),
            "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    with open(a.map, "x") as fh:
        json.dump({"meta": meta, "vars": names}, fh)
    print(json.dumps(meta))


if __name__ == "__main__":
    main()

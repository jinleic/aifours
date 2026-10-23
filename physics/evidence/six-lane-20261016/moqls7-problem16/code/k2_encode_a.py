"""Encoder A for class K2 (2 quantum + 2 classical squares of order 7), conditions (P1)-(P5) of README §2.

python -B k2_encode_a.py --mode fixed --s3 1 --s4 2 --cnf ../evidence/k2/a_fixed_1_2.cnf --map ../evidence/k2/a_fixed_1_2.map.json
python -B k2_encode_a.py --mode generic --cnf ../evidence/k2/a_generic.cnf --map ../evidence/k2/a_generic.map.json
python -B k2_encode_a.py --decode MODEL.txt --map MAP.json --out PATTERN.json      (decode a solver model)

Cells c = (i,j), id 7i+j; row 0 is the reference row (standard form). Coordinates k in 0..6.
Auxiliary variables are defined by full equivalences (faithful decoding; canonical extension of any real
configuration satisfies every clause).
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os

N = 7
CELLS = [(i, j) for i in range(N) for j in range(N)]


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
        """lits: ints or bools; True satisfies the clause, False literals are dropped."""
        out = []
        for l in lits:
            if l is True:
                return
            if l is False:
                continue
            out.append(l)
        if not out:
            raise ValueError("empty clause generated")
        self.clauses.append(out)

    def AND(self, name, a, b):
        """returns literal equivalent to a & b (bool-folded)."""
        if a is False or b is False:
            return False
        if a is True:
            return b
        if b is True:
            return a
        v = self.var(name)
        self.add([-v, a])
        self.add([-v, b])
        self.add([v, -a, -b])
        return v


def neg(l):
    if l is True:
        return False
    if l is False:
        return True
    return -l


def build(mode, slopes=(1, 2), quantum=(1, 2), p3=True, p4=(1, 2), fixpat=None, ngeneric=2, sb2=False):
    """mode 'fixed': classical squares L_t(i,j) = j + slopes[t] i; 'generic': two variable MOLS (labels 3, 4).
    quantum: labels of quantum squares (pattern variables); fixpat: {label: 7x7 list of supports} unit clauses."""
    f = CNF()
    base = max(quantum) + 1
    CL = list(range(base, base + len(slopes))) if mode == "fixed" else list(range(base, base + ngeneric))
    slope_of = dict(zip(CL, slopes)) if mode == "fixed" else {}

    # ---------------- classical squares
    def Lvar(t, c, x):
        i, j = c
        if i == 0:
            return x == j
        if mode == "fixed":
            return x == (j + slope_of[t] * i) % N
        return f.var(("L%d" % t, c, x))

    if mode == "generic":
        for t in CL:
            for c in CELLS:
                if c[0] == 0:
                    continue
                f.add([Lvar(t, c, x) for x in range(N)])
                for x, y in itertools.combinations(range(N), 2):
                    f.add([neg(Lvar(t, c, x)), neg(Lvar(t, c, y))])
            for x in range(N):
                for i in range(N):      # rows: symbol x at most once (with cell-exactly-one => Latin rows)
                    for j1, j2 in itertools.combinations(range(N), 2):
                        f.add([neg(Lvar(t, (i, j1), x)), neg(Lvar(t, (i, j2), x))])
                for j in range(N):      # columns
                    for i1, i2 in itertools.combinations(range(N), 2):
                        f.add([neg(Lvar(t, (i1, j), x)), neg(Lvar(t, (i2, j), x))])
        offrow = [c for c in CELLS if c[0] > 0]
        for ta, tb in itertools.combinations(CL, 2):
            for c in offrow:             # La(c) != Lb(c) off the first row
                for x in range(N):
                    f.add([neg(Lvar(ta, c, x)), neg(Lvar(tb, c, x))])
            for c1, c2 in itertools.combinations(offrow, 2):     # orthogonality: no repeated pair (count => exactly once)
                for x in range(N):
                    for y in range(N):
                        if x != y:
                            f.add([neg(Lvar(ta, c1, x)), neg(Lvar(tb, c1, y)), neg(Lvar(ta, c2, x)), neg(Lvar(tb, c2, y))])
        if CL:
            for i in range(1, N):        # symmetry breaking: L_first(i,0) = i (simultaneous permutation of rows 1..6)
                f.add([Lvar(CL[0], (i, 0), i)])

    # ---------------- pattern variables
    def S(s, c, k):
        i, j = c
        if i == 0:
            return k == j
        return f.var(("S%d" % s, c, k))

    for s in quantum:
        for c in CELLS:
            if c[0] == 0:
                continue
            f.add([S(s, c, k) for k in range(N)])                     # P1 nonempty
            f.add([neg(S(s, c, c[1]))])                               # rule #2
            for t in CL:
                for x in range(N):
                    f.add([neg(Lvar(t, c, x)), neg(S(s, c, x))])      # rule #3 vs classical squares
    for s1, s2 in itertools.combinations(quantum, 2):
        for c in CELLS:
            if c[0] == 0:
                continue
            for k in range(N):
                f.add([neg(S(s1, c, k)), neg(S(s2, c, k))])           # rule #3 between quantum squares
    if fixpat:
        for s, pat in fixpat.items():
            for c in CELLS:
                if c[0] == 0:
                    continue
                for k in range(N):
                    f.add([S(s, c, k) if k in pat[c[0]][c[1]] else neg(S(s, c, k))])

    # ---------------- pairwise "share exactly one" indicators X_s[c,c']
    X = {}
    for s in quantum:
        for c1, c2 in itertools.combinations(CELLS, 2):
            b = [f.AND(("b", s, c1, c2, k), S(s, c1, k), S(s, c2, k)) for k in range(N)]
            if all(l is False for l in b):
                X[(s, c1, c2)] = False
                continue
            x = f.var(("X", s, c1, c2))
            X[(s, c1, c2)] = x
            for k in range(N):                    # exactly one shared -> X
                f.add([neg(b[k])] + [b[k2] for k2 in range(N) if k2 != k] + [x])
            f.add([-x] + [l for l in b])          # X -> at least one shared
            for k1, k2 in itertools.combinations(range(N), 2):
                f.add([-x, neg(b[k1]), neg(b[k2])])   # X -> at most one shared

    def Xl(s, c1, c2):
        return X[(s, c1, c2)] if (s, c1, c2) in X else X[(s, c2, c1)]

    # (P2b) common lines: rows, columns, classical-square lines; (P3) cross-square
    for c1, c2 in itertools.combinations(CELLS, 2):
        for s in quantum:
            if c1[0] == c2[0] or c1[1] == c2[1]:
                f.add([neg(Xl(s, c1, c2))])
            else:
                for t in CL:
                    for x in range(N):
                        f.add([neg(Lvar(t, c1, x)), neg(Lvar(t, c2, x)), neg(Xl(s, c1, c2))])
        if p3:
            for s1, s2 in itertools.combinations(quantum, 2):
                f.add([neg(Xl(s1, c1, c2)), neg(Xl(s2, c1, c2))])

    # (P2a) coverage and (P2c) coordinate pairs
    rows = [[(i, j) for j in range(N)] for i in range(N)]
    cols = [[(i, j) for i in range(N)] for j in range(N)]
    for s in quantum:
        for line in rows + cols:
            for k in range(N):
                f.add([S(s, c, k) for c in line])
            for k1, k2 in itertools.combinations(range(N), 2):
                v = [f.AND(("v", s, c, k1, k2), S(s, c, k1), S(s, c, k2)) for c in line]
                for a_ in range(N):
                    f.add([neg(v[a_])] + [v[b_] for b_ in range(N) if b_ != a_])
        for t in CL:
            for x in range(N):
                for k in range(N):
                    us = [f.AND(("u", s, t, c, x, k), Lvar(t, c, x), S(s, c, k)) for c in CELLS]
                    f.add(us)
                for k1, k2 in itertools.combinations(range(N), 2):
                    ts = []
                    for c in CELLS:
                        vv = f.AND(("v", s, c, k1, k2), S(s, c, k1), S(s, c, k2))
                        ts.append(f.AND(("t", s, t, c, x, k1, k2), Lvar(t, c, x), vv))
                    for a_ in range(len(ts)):
                        if ts[a_] is False:
                            continue
                        f.add([neg(ts[a_])] + [ts[b_] for b_ in range(len(ts)) if b_ != a_])
    # (SB2) symmetry breaking at cell (1,0) (README §2 addendum): WLOG Psi1 has its weight-3 entry at (1,0);
    # the generic classical squares take symbols 1, 2, ... there; the free coordinates are split
    # S1 = first three, S2, S3, ... = one each (4 squares in total, so this is forced up to relabelling).
    if sb2:
        assert mode == "generic" and len(quantum) + len(CL) == 4
        for t_idx, t in enumerate(CL):
            f.add([Lvar(t, (1, 0), t_idx + 1)])
        free = [k for k in range(1, N) if k > len(CL)]
        parts = [free[:3]] + [[k] for k in free[3:]]
        for s, part in zip(quantum, parts):
            for k in range(N):
                f.add([S(s, (1, 0), k) if k in part else neg(S(s, (1, 0), k))])
    # (P4) weight >= 3 existence (both squares in the K2 run; diagnostic runs may restrict to a subset)
    for s in p4:
        ws = []
        for c in CELLS:
            if c[0] == 0:
                continue
            w = f.var(("w3", s, c))
            for K in itertools.combinations(range(N), 5):
                f.add([-w] + [S(s, c, k) for k in K])
            ws.append(w)
        f.add(ws)
    return f


def write(f, cnf_path, map_path, meta):
    os.makedirs(os.path.dirname(cnf_path), exist_ok=True)
    with open(cnf_path, "w") as fh:
        fh.write("p cnf %d %d\n" % (f.nv, len(f.clauses)))
        for cl in f.clauses:
            fh.write(" ".join(map(str, cl)) + " 0\n")
    names = {json.dumps(k): v for k, v in f.names.items()
             if isinstance(k[0], str) and k[0][0] in "LS" and k[0][1:].isdigit()}
    json.dump({"meta": meta, "vars": names}, open(map_path, "w"))
    return hashlib.sha256(open(cnf_path, "rb").read()).hexdigest()


def decode(model_path, map_path, out_path):
    true = set()
    for line in open(model_path):
        if line.startswith("v "):
            for t in line.split()[1:]:
                v = int(t)
                if v > 0:
                    true.add(v)
    m = json.load(open(map_path))
    meta = m["meta"]
    slopes = meta.get("slopes") or []
    base = max(meta["quantum"]) + 1
    CL = list(range(base, base + len(slopes))) if meta["mode"] == "fixed" else list(range(base, base + meta.get("ngeneric", 2)))
    L = {t: {} for t in CL}
    S = {s: {} for s in meta["quantum"]}
    for key, v in m["vars"].items():
        k = json.loads(key)
        if v in true:
            if k[0][0] == "L":
                L[int(k[0][1:])][tuple(k[1])] = k[2]
            else:
                S[int(k[0][1:])].setdefault(tuple(k[1]), []).append(k[2])
    for c in CELLS:
        if c[0] == 0:
            for t in CL:
                L[t][c] = c[1]
            for s in S:
                S[s][c] = [c[1]]
        elif meta["mode"] == "fixed":
            for t, sl in zip(CL, slopes):
                L[t][c] = (c[1] + sl * c[0]) % N
    out = {"meta": meta}
    for t in CL:
        out["L%d" % t] = [[L[t][(i, j)] for j in range(N)] for i in range(N)]
    for s in S:
        out["S%d" % s] = [[sorted(S[s].get((i, j), [])) for j in range(N)] for i in range(N)]
    json.dump(out, open(out_path, "w"), indent=1)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["fixed", "generic"])
    ap.add_argument("--slopes", default="1,2", help="fixed mode: slopes of the classical squares j + s*i")
    ap.add_argument("--quantum", default="12", help="labels of quantum squares")
    ap.add_argument("--fixpat", default=None, help="controls: JSON {label: 7x7 supports} fixed by unit clauses")
    ap.add_argument("--cnf")
    ap.add_argument("--map")
    ap.add_argument("--decode")
    ap.add_argument("--out")
    ap.add_argument("--no-p3", action="store_true", help="diagnostic only")
    ap.add_argument("--p4", default="12", help="squares required to have weight >= 3 (e.g. 12, 1, none)")
    ap.add_argument("--ngeneric", type=int, default=2, help="generic mode: number of variable classical squares")
    ap.add_argument("--sb2", action="store_true", help="symmetry breaking at cell (1,0), README §2 addendum")
    a = ap.parse_args()
    if a.decode:
        decode(a.decode, a.map, a.out)
        print("decoded", a.out)
        return
    p4 = () if a.p4 == "none" else tuple(int(ch) for ch in a.p4)
    quantum = tuple(int(ch) for ch in a.quantum)
    slopes = tuple(int(x) for x in a.slopes.split(",") if x != "") if a.mode == "fixed" else ()
    fixpat = None
    if a.fixpat:
        fixpat = {int(k): v for k, v in json.load(open(a.fixpat)).items()}
    f = build(a.mode, slopes, quantum, p3=not a.no_p3, p4=p4, fixpat=fixpat, ngeneric=a.ngeneric, sb2=a.sb2)
    meta = {"encoder": "A", "mode": a.mode, "slopes": list(slopes), "quantum": list(quantum), "p3": not a.no_p3,
            "p4": list(p4), "fixpat": a.fixpat, "ngeneric": a.ngeneric if a.mode == "generic" else None, "sb2": a.sb2,
            "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    h = write(f, a.cnf, a.map, meta)
    print(json.dumps({"vars": f.nv, "clauses": len(f.clauses), "cnf_sha256": h, **meta}))


if __name__ == "__main__":
    main()

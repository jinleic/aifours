"""Encoder GB: independent implementation of the all-frames Gram-pattern conditions of README §2 (G1-G4, P4, SB2),
GENERIC mode only (classical squares as MOLS variables; G3/G4 over rows and columns). Different construction from
gram_a.py: unary sequential counters for every cardinality statement, classical orthogonality via pair indicators
with exactly-one, explicit TRUE literal for constants, no row sorting.

python -B gram_b.py --order 8 --quantum 12345 --ngeneric 0 --p4 12345 --sb2 --cnf X.cnf
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from itertools import combinations


class F:
    def __init__(self):
        self.n = 0
        self.cl = []
        self.tab = {}

    def new(self, key=None):
        self.n += 1
        if key is not None:
            self.tab[key] = self.n
        return self.n

    def c(self, *lits):
        self.cl.append(list(lits))


def encode(n, Q, ngen, p4, sb2, fixg=None, g5=False, allrows=False):
    F_ = F()
    T = F_.new("TRUE")
    F_.c(T)
    pts = [(r, c) for r in range(n) for c in range(n)]
    classical = list(range(100, 100 + ngen))          # separate label space
    Lv = {}

    def Llit(t, r, c, x):
        if r == 0:
            return T if x == c else -T
        if (t, r, c, x) not in Lv:
            Lv[(t, r, c, x)] = F_.new(("L", t, r, c, x))
        return Lv[(t, r, c, x)]

    def exactly_one(lits):
        F_.c(*lits)
        for a, b in combinations(lits, 2):
            F_.c(-a, -b)
    for t in classical:
        for r in range(1, n):
            for c in range(n):
                exactly_one([Llit(t, r, c, x) for x in range(n)])
        for x in range(n):
            for r in range(1, n):
                exactly_one([Llit(t, r, c, x) for c in range(n)])
            for c in range(n):
                if x == c:
                    for r in range(1, n):
                        F_.c(-Llit(t, r, c, x))
                else:
                    exactly_one([Llit(t, r, c, x) for r in range(1, n)])
    for ta, tb in combinations(classical, 2):
        z = {}
        for (r, c) in pts:
            if r == 0:
                continue
            for x in range(n):
                for y in range(n):
                    v = F_.new()
                    z[(r, c, x, y)] = v
                    F_.c(-v, Llit(ta, r, c, x))
                    F_.c(-v, Llit(tb, r, c, y))
                    F_.c(v, -Llit(ta, r, c, x), -Llit(tb, r, c, y))
        for x in range(n):
            for y in range(n):
                grp = [z[(r, c, x, y)] for (r, c) in pts if r > 0]
                if x == y:
                    for v in grp:
                        F_.c(-v)
                else:
                    exactly_one(grp)

    G = {}

    def glit(s, p, q):
        if p == q:
            return T
        if p[0] == q[0] or p[1] == q[1]:
            return -T
        key = (s,) + tuple(sorted((p, q)))
        if key not in G:
            G[key] = F_.new(("g",) + key)
        return G[key]

    def conj(a, b):
        v = F_.new()
        F_.c(-v, a)
        F_.c(-v, b)
        F_.c(v, -a, -b)
        return v

    def counter2(lits):
        """returns (ge1, ge2) with full equivalence (sequential counter)."""
        ge1, ge2 = -T, -T
        for l in lits:
            n1, n2 = F_.new(), F_.new()
            # n1 <-> ge1 or l ; n2 <-> ge2 or (ge1 and l)
            F_.c(-ge1, n1)
            F_.c(-l, n1)
            F_.c(-n1, ge1, l)
            F_.c(-ge2, n2)
            F_.c(-ge1, -l, n2)
            F_.c(-n2, ge2, ge1)
            F_.c(-n2, ge2, l)
            ge1, ge2 = n1, n2
        return ge1, ge2

    def atleast3(lits):
        ge = [-T, -T, -T]
        for l in lits:
            nxt = []
            for k in range(3):
                v = F_.new()
                carry = T if k == 0 else ge[k - 1]
                F_.c(-ge[k], v)
                F_.c(-carry, -l, v)
                F_.c(-v, ge[k], carry)
                F_.c(-v, ge[k], l)
                nxt.append(v)
            ge = nxt
        return ge[2]

    # G1 on classical lines
    for s in Q:
        for p, q in combinations(pts, 2):
            gl = glit(s, p, q)
            if abs(gl) == T:
                continue
            for t in classical:
                for x in range(n):
                    F_.c(-gl, -Llit(t, p[0], p[1], x), -Llit(t, q[0], q[1], x))
    # G2
    for s, u in combinations(Q, 2):
        for p, q in combinations(pts, 2):
            a, b = glit(s, p, q), glit(u, p, q)
            if a == -T or b == -T:
                continue
            F_.c(-a, -b)
    if fixg:
        for s, pairs in fixg.items():
            on = {tuple(sorted((tuple(p), tuple(q)))) for p, q in pairs}
            for p, q in combinations(pts, 2):
                gl = glit(s, p, q)
                key = tuple(sorted((p, q)))
                F_.c(gl if key in on else -gl)
    lines = [[(r, c) for c in range(n)] for r in range(n)] + [[(r, c) for r in range(n)] for c in range(n)]
    # G3
    for s in Q:
        for A, B in combinations(lines, 2):
            for a in A:
                F_.c(*[glit(s, a, b) for b in B])
            for b in B:
                F_.c(*[glit(s, a, b) for a in A])
            for a1, a2 in combinations(A, 2):
                ge1, ge2 = counter2([conj(glit(s, a1, b), glit(s, a2, b)) for b in B])
                F_.c(-ge1, ge2)
            for b1, b2 in combinations(B, 2):
                ge1, ge2 = counter2([conj(glit(s, a, b1), glit(s, a, b2)) for a in A])
                F_.c(-ge1, ge2)
    # G4
    for s in Q:
        for line in lines:
            on = set(line)
            others = [p for p in pts if p not in on]
            for p, q in combinations(others, 2):
                ge1, ge2 = counter2([conj(glit(s, a, p), glit(s, a, q)) for a in line])
                gpq = glit(s, p, q)
                F_.c(-ge1, ge2, gpq)                # exactly one => g(p,q)
                F_.c(ge1, -gpq)                     # none => not g(p,q)
    # G5 same ray: support of q in the frame of a row/column is exactly {a}  =>  g(p,q) <-> g(p,a) for all p
    if g5:
        for s in Q:
            for line in lines:
                on = set(line)
                for q in pts:
                    if q in on:
                        continue
                    ov = [glit(s, a, q) for a in line]
                    for k, a in enumerate(line):
                        if ov[k] == -T:
                            continue
                        single = F_.new()
                        F_.c(-single, ov[k])
                        for kk, o2 in enumerate(ov):
                            if kk != k:
                                F_.c(-single, -o2)
                        F_.c(single, -ov[k], *[o2 for kk, o2 in enumerate(ov) if kk != k])
                        for p in pts:
                            if p in (q, a):
                                continue
                            x, y = glit(s, p, q), glit(s, p, a)
                            F_.c(-single, -x, y)
                            F_.c(-single, -y, x)
    # P4 (frame row 0, or every row frame)
    for s in p4:
        for r0 in (range(n) if allrows else [0]):
            F_.c(*[atleast3([glit(s, (r0, k), p) for k in range(n)]) for p in pts if p[0] != r0])
    # SB2
    if sb2:
        assert len(Q) + len(classical) == n - 3
        for idx, t in enumerate(classical):
            F_.c(Llit(t, 1, 0, idx + 1))
        rest = list(range(1 + len(classical), n))
        alloc = {Q[0]: rest[:3]}
        for pos, s in enumerate(Q[1:]):
            alloc[s] = [rest[3 + pos]]
        for s in Q:
            for k in range(n):
                gl = glit(s, (0, k), (1, 0))
                F_.c(gl if k in alloc[s] else -gl)
    return F_


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--order", type=int, choices=[7, 8], required=True)
    ap.add_argument("--quantum", required=True)
    ap.add_argument("--ngeneric", type=int, default=0)
    ap.add_argument("--p4", default="none")
    ap.add_argument("--sb2", action="store_true")
    ap.add_argument("--g5", action="store_true")
    ap.add_argument("--p4-all-rows", action="store_true")
    ap.add_argument("--fixg", default=None)
    ap.add_argument("--cnf", required=True)
    a = ap.parse_args()
    Q = [int(ch) for ch in a.quantum]
    p4 = [] if a.p4 == "none" else [int(ch) for ch in a.p4]
    fixg = {int(k): v for k, v in json.load(open(a.fixg)).items()} if a.fixg else None
    F_ = encode(a.order, Q, a.ngeneric, p4, a.sb2, fixg, a.g5, a.p4_all_rows)
    with open(a.cnf, "x") as fh:
        fh.write("p cnf %d %d\n" % (F_.n, len(F_.cl)))
        for cl in F_.cl:
            fh.write(" ".join(map(str, cl)) + " 0\n")
    with open(a.cnf + ".map.json", "x") as fh:
        json.dump({json.dumps(k): v for k, v in F_.tab.items()}, fh)
    print(json.dumps({"encoder": "GB", "argv": sys.argv, "python": sys.version, "vars": F_.n, "clauses": len(F_.cl),
                      "cnf_sha256": hashlib.sha256(open(a.cnf, "rb").read()).hexdigest(),
                      "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}))


if __name__ == "__main__":
    main()

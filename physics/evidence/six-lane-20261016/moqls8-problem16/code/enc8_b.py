"""Encoder B8: order-8 version of the n = 7 lane's encoder B (k2_encode_b_r2.py; same clause families,
sequential counters, pair indicators). Changes: n = 8; FIXED classical squares are AG(2,8) squares
c XOR s*r over GF(8) (x^3 = x + 1); (SB2) requires #quantum + #classical = n - 3 = 5. Row sorting (--symbreak) OFF
by default. Classical labels 3, 4, ... live in a namespace separate from the quantum supports.

python -B enc8_b.py --mode generic --sb2 --quantum 12 --ngeneric 3 --p4 12 --cnf X.cnf
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from itertools import combinations

n = 8


def field_mul(u, v):
    """multiplication in GF(2)[x]/(x^3+x+1) on 3-bit integers (independent implementation)."""
    acc = 0
    while v:
        if v & 1:
            acc ^= u
        v >>= 1
        u <<= 1
        if u & 0b1000:
            u ^= 0b1011
    return acc
cells = [(r, c) for r in range(n) for c in range(n)]


class Formula:
    def __init__(self):
        self.count = 0
        self.cls = []
        self.table = {}

    def new(self, key=None):
        self.count += 1
        if key is not None:
            self.table[key] = self.count
        return self.count

    def clause(self, *lits):
        self.cls.append(list(lits))


def encode(mode, slopes, symbreak, p4_labels=(1, 2), Q=(1, 2), fixpat=None, p3=True, ngeneric=2, sb2=False):
    F = Formula()
    T = tuple(range(3, 3 + len(slopes))) if mode == "fixed" else tuple(range(3, 3 + ngeneric))
    one_hot = {}
    # classical squares: one-hot on off-first-row cells; constants on the first row
    for t in T:
        for (r, c) in cells:
            for x in range(n):
                if r == 0:
                    continue
                if mode == "fixed":
                    continue
                one_hot[(t, r, c, x)] = F.new(("L", t, r, c, x))
    TRUE = F.new("TRUE")
    F.clause(TRUE)

    def lit_L(t, r, c, x):
        if r == 0:
            return TRUE if x == c else -TRUE
        if mode == "fixed":
            return TRUE if x == (c ^ field_mul(slopes[T.index(t)], r)) else -TRUE
        return one_hot[(t, r, c, x)]

    def exactly_one(lits):
        F.clause(*lits)
        for a, b in combinations(lits, 2):
            F.clause(-a, -b)

    if mode == "generic":
        for t in T:
            for r in range(1, n):
                for c in range(n):
                    exactly_one([lit_L(t, r, c, x) for x in range(n)])
            for x in range(n):
                for r in range(1, n):
                    exactly_one([lit_L(t, r, c, x) for c in range(n)])
                for c in range(n):
                    if x != c:
                        exactly_one([lit_L(t, r, c, x) for r in range(1, n)])
                    else:
                        for r in range(1, n):
                            F.clause(-lit_L(t, r, c, x))
        # orthogonality: each ordered pair (x,y), x != y, exactly once off the first row; x == y never
        for ta, tb in combinations(T, 2):
            z = {}
            for (r, c) in cells:
                if r == 0:
                    continue
                for x in range(n):
                    for y in range(n):
                        v = F.new()
                        z[(r, c, x, y)] = v
                        F.clause(-v, lit_L(ta, r, c, x))
                        F.clause(-v, lit_L(tb, r, c, y))
                        F.clause(v, -lit_L(ta, r, c, x), -lit_L(tb, r, c, y))
            for x in range(n):
                for y in range(n):
                    group = [z[(r, c, x, y)] for (r, c) in cells if r > 0]
                    if x == y:
                        for v in group:
                            F.clause(-v)
                    else:
                        exactly_one(group)
        if symbreak and T:
            for r in range(1, n):
                F.clause(lit_L(T[0], r, 0, r))

    # supports
    sup = {}
    for s in Q:
        for (r, c) in cells:
            for k in range(n):
                if r == 0:
                    sup[(s, r, c, k)] = TRUE if k == c else -TRUE
                else:
                    sup[(s, r, c, k)] = F.new(("S", s, r, c, k))
    for (r, c) in cells:
        if r == 0:
            continue
        for s in Q:
            F.clause(*[sup[(s, r, c, k)] for k in range(n)])
            F.clause(-sup[(s, r, c, c)])
            for t in T:
                for x in range(n):
                    F.clause(-lit_L(t, r, c, x), -sup[(s, r, c, x)])
        for s1, s2 in combinations(Q, 2):
            for k in range(n):
                F.clause(-sup[(s1, r, c, k)], -sup[(s2, r, c, k)])
    if fixpat:
        for s, pat in fixpat.items():
            for (r, c) in cells:
                if r:
                    for k in range(n):
                        F.clause(sup[(s, r, c, k)] if k in pat[r][c] else -sup[(s, r, c, k)])

    def AND2(a, b):
        v = F.new()
        F.clause(-v, a)
        F.clause(-v, b)
        F.clause(v, -a, -b)
        return v

    def counter(lits, upto):
        """unary sequential counter; returns [ge1, ..., ge_upto] literals with full equivalence."""
        prev = [-TRUE] * upto
        for l in lits:
            cur = []
            for m in range(upto):
                v = F.new()
                carry = TRUE if m == 0 else prev[m - 1]
                # v <-> prev[m] or (carry and l)
                F.clause(-prev[m], v)
                F.clause(-carry, -l, v)
                F.clause(-v, prev[m], carry)
                F.clause(-v, prev[m], l)
                cur.append(v)
            prev = cur
        return prev

    # exactly-one-shared indicator per square and pair of cells
    E = {}
    for s in Q:
        for c1, c2 in combinations(cells, 2):
            shared = [AND2(sup[(s,) + c1 + (k,)], sup[(s,) + c2 + (k,)]) for k in range(n)]
            ge1, ge2 = counter(shared, 2)
            e = F.new()
            F.clause(-e, ge1)
            F.clause(-e, -ge2)
            F.clause(e, -ge1, ge2)
            E[(s, c1, c2)] = e
    # same-line indicator for classical lines
    for c1, c2 in combinations(cells, 2):
        same_rc = c1[0] == c2[0] or c1[1] == c2[1]
        for s in Q:
            if same_rc:
                F.clause(-E[(s, c1, c2)])
        if not same_rc:
            for t in T:
                for x in range(n):
                    for s in Q:
                        F.clause(-lit_L(t, c1[0], c1[1], x), -lit_L(t, c2[0], c2[1], x), -E[(s, c1, c2)])
        if p3:
            for s1, s2 in combinations(Q, 2):
                F.clause(-E[(s1, c1, c2)], -E[(s2, c1, c2)])

    # lines: rows/cols fixed; classical lines via membership literals
    lines = []
    for r in range(n):
        lines.append([((r, c), TRUE) for c in range(n)])
    for c in range(n):
        lines.append([((r, c), TRUE) for r in range(n)])
    for t in T:
        for x in range(n):
            lines.append([((r, c), lit_L(t, r, c, x)) for (r, c) in cells])
    for s in Q:
        for line in lines:
            for k in range(n):
                ys = []
                for (cell, mem) in line:
                    y = F.new()
                    F.clause(-y, mem)
                    F.clause(-y, sup[(s,) + cell + (k,)])
                    ys.append(y)
                F.clause(*ys)
            for k1, k2 in combinations(range(n), 2):
                ind = []
                for (cell, mem) in line:
                    both = AND2(sup[(s,) + cell + (k1,)], sup[(s,) + cell + (k2,)])
                    ind.append(AND2(mem, both))
                ge1, ge2 = counter(ind, 2)
                F.clause(-ge1, ge2)
    # SB2 (independent restatement): weight-3 entry of square Q[0] at (1,0); classical squares (in order) carry
    # symbols 1, 2, ... at (1,0); remaining coordinates: three to Q[0], then one to each further quantum square.
    if sb2:
        assert mode == "generic" and len(Q) + len(T) == n - 3
        for idx, t in enumerate(T):
            F.clause(lit_L(t, 1, 0, idx + 1))
        rest = list(range(1 + len(T), n))
        alloc = {Q[0]: rest[0:3]}
        for pos, s in enumerate(Q[1:]):
            alloc[s] = [rest[3 + pos]]
        for s in Q:
            for k in range(n):
                F.clause(sup[(s, 1, 0, k)] if k in alloc[s] else -sup[(s, 1, 0, k)])
    # weight >= 3 somewhere in each square
    for s in p4_labels:
        flags = []
        for (r, c) in cells:
            if r == 0:
                continue
            flags.append(counter([sup[(s, r, c, k)] for k in range(n)], 3)[2])
        F.clause(*flags)
    return F


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["fixed", "generic"], required=True)
    ap.add_argument("--slopes", default="1,2")
    ap.add_argument("--symbreak", action="store_true")
    ap.add_argument("--p4", default="12")
    ap.add_argument("--quantum", default="12")
    ap.add_argument("--fixpat", default=None)
    ap.add_argument("--no-p3", action="store_true")
    ap.add_argument("--ngeneric", type=int, default=2)
    ap.add_argument("--sb2", action="store_true")
    ap.add_argument("--cnf", required=True)
    ap.add_argument("--map", default=None, help="ignored (interface compatibility with encoder A controls)")
    a = ap.parse_args()
    slopes = [int(x) for x in a.slopes.split(",") if x != ""]
    p4 = () if a.p4 == "none" else tuple(int(ch) for ch in a.p4)
    Q = tuple(int(ch) for ch in a.quantum)
    fixpat = {int(k): v for k, v in json.load(open(a.fixpat)).items()} if a.fixpat else None
    F = encode(a.mode, slopes, a.symbreak, p4, Q, fixpat, not a.no_p3, a.ngeneric, a.sb2)
    with open(a.cnf, "w") as fh:
        fh.write("p cnf %d %d\n" % (F.count, len(F.cls)))
        for cl in F.cls:
            fh.write(" ".join(map(str, cl)) + " 0\n")
    json.dump({json.dumps(k): v for k, v in F.table.items()}, open(a.cnf + ".map.json", "w"))
    meta = {"encoder": "B8", "argv": sys.argv, "python": sys.version, "mode": a.mode,
            "slopes": slopes if a.mode == "fixed" else None, "symbreak": a.symbreak, "quantum": list(Q),
            "ngeneric": a.ngeneric, "sb2": a.sb2, "p3": not a.no_p3, "fixpat": a.fixpat,
            "fixpat_sha256": hashlib.sha256(open(a.fixpat, "rb").read()).hexdigest() if a.fixpat else None,
            "p4": list(p4), "vars": F.count, "clauses": len(F.cls),
            "cnf_sha256": hashlib.sha256(open(a.cnf, "rb").read()).hexdigest(),
            "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest()}
    print(json.dumps(meta))


if __name__ == "__main__":
    main()

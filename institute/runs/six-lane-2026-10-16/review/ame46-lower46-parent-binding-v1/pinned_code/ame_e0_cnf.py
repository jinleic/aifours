#!/usr/bin/env python3
"""ame_e0_cnf.py: CNF for the e = 0 case of the AME(4,6) support problem (lane ame46-support).

Model (README 0.2 RCM specialised to e = 0; all constraints are necessary conditions, see review/LEMMAS):
  variables n_x (x in N, non-classical support) and c_x (x in T, classical officers), x in [6]^4;
  every P-line L (6 coordinate pairs x 36 values) has weight sum_{x in L} (n_x + 2 c_x) = 2, i.e. either exactly one
  classical officer and nothing else, or exactly two non-classical elements (e = 0: all components are 2x2);
  row overlap in each reshaping: two rows sharing a column share a second column (with exact-two rows this is the
  2x2 block property; the column version is then implied);
  |T| = t, counted on the 36 rows of 12|34;
  optional symmetry breaking (SB1/SB2 of review/LEMMAS: c_(0,j,j,j) for j < tau, and every slice count t_{i,a} <= tau);
  optional phase-obstruction families (each clause excludes a set of six N-elements whose three 2x2 blocks have
  inconsistent phase congruences; proofs in review/LEMMAS): TBL (three-block lemma on a 2^4 subcube) and TWIN
  (twin triangle).
Writes DIMACS to the given path and a JSON variable map next to it.
"""
import argparse
import itertools
import json

R = range(6)
PAIRS = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]
RESHAPINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]


def idx(x):
    return x[0] * 216 + x[1] * 36 + x[2] * 6 + x[3]


class CNF:
    def __init__(self):
        self.nv = 2 * 1296
        self.clauses = []

    def n(self, x):
        return 1 + idx(x)

    def c(self, x):
        return 1 + 1296 + idx(x)

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, cl):
        self.clauses.append(cl)

    def at_most_k(self, lits, k):
        """Sinz sequential counter: at most k of lits."""
        m = len(lits)
        if k >= m:
            return
        if k == 0:
            for l in lits:
                self.add([-l])
            return
        s = [[self.new() for _ in range(k)] for _ in range(m - 1)]
        self.add([-lits[0], s[0][0]])
        for j in range(1, k):
            self.add([-s[0][j]])
        for i in range(1, m - 1):
            self.add([-lits[i], s[i][0]])
            self.add([-s[i - 1][0], s[i][0]])
            for j in range(1, k):
                self.add([-lits[i], -s[i - 1][j - 1], s[i][j]])
                self.add([-s[i - 1][j], s[i][j]])
            self.add([-lits[i], -s[i - 1][k - 1]])
        self.add([-lits[m - 1], -s[m - 2][k - 1]])

    def at_least_k(self, lits, k):
        self.at_most_k([-l for l in lits], len(lits) - k)


def line_members(P, z):
    out = []
    rest = [i for i in range(4) if i not in P]
    for y in itertools.product(R, repeat=2):
        x = [0] * 4
        x[P[0]], x[P[1]] = z
        x[rest[0]], x[rest[1]] = y
        out.append(tuple(x))
    return out


def tbl_sets():
    """Three-block-lemma 6-sets: in every 2^4 subcube {a1,h1}x..x{a4,h4}, each of the two 'even codes' is the union
    of four antipodal pairs {a,h}, D12, D13, D14; any three of the four pairs form an obstruction."""
    out = []
    for vals in itertools.product(itertools.combinations(R, 2), repeat=4):
        for parity in (0, 1):
            code = [tuple(vals[i][b[i]] for i in range(4)) for b in itertools.product((0, 1), repeat=4)
                    if sum(b) % 2 == parity]
            pairs, seen = [], set()
            for x in code:
                if x in seen:
                    continue
                y = tuple(vals[i][1] if x[i] == vals[i][0] else vals[i][0] for i in range(4))
                seen.update((x, y))
                pairs.append((x, y))
            assert len(pairs) == 4
            for three in itertools.combinations(pairs, 3):
                out.append([e for p in three for e in p])
    return out


def twin_sets():
    """Twin-triangle 6-sets: twin coordinate i, other coordinates (j,k,l) increasing; twin pairs over
    p=(al,be,ga), q=(al2,be2,ga), r=(al2,be,ga2) in coordinates (j,k,l), twin values {d,d2}."""
    out = []
    for i in range(4):
        j, k, l = [m for m in range(4) if m != i]
        for al, al2 in itertools.permutations(R, 2):
            for be, be2 in itertools.permutations(R, 2):
                for ga, ga2 in itertools.permutations(R, 2):
                    for d, d2 in itertools.combinations(R, 2):
                        s = []
                        for (u, v, w) in ((al, be, ga), (al2, be2, ga), (al2, be, ga2)):
                            for dd in (d, d2):
                                x = [0] * 4
                                x[j], x[k], x[l], x[i] = u, v, w, dd
                                s.append(tuple(x))
                        out.append(s)
    return out


def build(t, tau=None, phase=("TBL", "TWIN"), fix=None):
    F = CNF()
    lines = [(P, z) for P in PAIRS for z in itertools.product(R, repeat=2)]
    tr = {}
    for x in itertools.product(R, repeat=4):
        F.add([-F.n(x), -F.c(x)])
    for (P, z) in lines:
        mem = line_members(P, z)
        # at most one classical officer, and a classical officer excludes every other element of its line
        for a, b in itertools.combinations(mem, 2):
            F.add([-F.c(a), -F.c(b)])
            F.add([-F.c(a), -F.n(b)])
            F.add([-F.c(b), -F.n(a)])
        # weight >= 2: some classical officer, or for every x some other non-classical element
        cs = [F.c(x) for x in mem]
        for x in mem:
            F.add(cs + [F.n(y) for y in mem if y != x])
        # at most two non-classical elements
        F.at_most_k([F.n(x) for x in mem], 2)
        # line-has-classical indicator
        v = F.new()
        tr[(P, z)] = v
        F.add([-v] + cs)
        for cx in cs:
            F.add([-cx, v])
    # row overlap (rows of each reshaping); column version implied with exact-two lines
    for rows, cols in RESHAPINGS:
        rvals = list(itertools.product(R, repeat=2))
        for r1, r2 in itertools.combinations(rvals, 2):
            aux = {}
            for cv in rvals:
                a = F.new()
                aux[cv] = a
                x1 = [0] * 4
                x2 = [0] * 4
                x1[rows[0]], x1[rows[1]] = r1
                x2[rows[0]], x2[rows[1]] = r2
                x1[cols[0]], x1[cols[1]] = cv
                x2[cols[0]], x2[cols[1]] = cv
                F.add([-a, F.n(tuple(x1))])
                F.add([-a, F.n(tuple(x2))])
            for cv in rvals:
                x1 = [0] * 4
                x2 = [0] * 4
                x1[rows[0]], x1[rows[1]] = r1
                x2[rows[0]], x2[rows[1]] = r2
                x1[cols[0]], x1[cols[1]] = cv
                x2[cols[0]], x2[cols[1]] = cv
                F.add([-F.n(tuple(x1)), -F.n(tuple(x2))] + [aux[c2] for c2 in rvals if c2 != cv])
    # |T| = t counted on the 36 rows of 12|34
    trow = [tr[((0, 1), z)] for z in itertools.product(R, repeat=2)]
    F.at_most_k(trow, t)
    F.at_least_k(trow, t)
    if tau is not None:
        for j in range(tau):
            F.add([F.c((0, j, j, j))])
        for i in range(4):
            jj = 1 if i == 0 else 0
            P = (min(i, jj), max(i, jj))
            for a in R:
                lits = [tr[(P, (a, b) if P[0] == i else (b, a))] for b in R]
                F.at_most_k(lits, tau)
    if "TBL" in phase:
        for s in tbl_sets():
            F.add([-F.n(x) for x in s])
    if "TWIN" in phase:
        for s in twin_sets():
            F.add([-F.n(x) for x in s])
    if fix is not None:
        for x in itertools.product(R, repeat=4):
            if x in fix["T"]:
                F.add([F.c(x)])
            elif x in fix["N"]:
                F.add([F.n(x)])
            else:
                F.add([-F.n(x)])
                F.add([-F.c(x)])
    return F


def write(F, path, meta):
    with open(path, "w") as fh:
        fh.write(f"p cnf {F.nv} {len(F.clauses)}\n")
        for cl in F.clauses:
            fh.write(" ".join(map(str, cl)) + " 0\n")
    with open(path + ".meta.json", "w") as fh:
        json.dump(dict(meta, nvars=F.nv, nclauses=len(F.clauses),
                       var_n="1 + 216*x1 + 36*x2 + 6*x3 + x4", var_c="1297 + 216*x1 + 36*x2 + 6*x3 + x4"), fh,
                  indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t", type=int, required=True)
    ap.add_argument("--tau", type=int, default=None)
    ap.add_argument("--phase", default="TBL,TWIN")
    ap.add_argument("--fix-pandya", action="store_true")
    ap.add_argument("out")
    a = ap.parse_args()
    phase = tuple(p for p in a.phase.split(",") if p)
    fix = None
    if a.fix_pandya:
        import pandya_control as pc
        W = pc.build()
        fix = {"T": {x for x, v in W.items() if v == pc.R2}, "N": {x for x, v in W.items() if v != pc.R2}}
    F = build(a.t, a.tau, phase, fix)
    write(F, a.out, {"t": a.t, "tau": a.tau, "phase": list(phase), "fix_pandya": a.fix_pandya})
    print(a.out, F.nv, len(F.clauses))


if __name__ == "__main__":
    main()

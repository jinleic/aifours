#!/usr/bin/env python3
"""brd_cnf.py -- generic group-invariant CNF encoder for BRD(v,b,r,k,L) (README 1.4).

Input: a model spec from code/brd_models.py.  Cells (i,j) are merged into orbits under the generators with relative
signs (union-find with parity: W[pi(i)][tau(j)] = rho(i) sigma(j) W[i][j]); an orbit that contains a cell together
with its own negative is forced to 0.  Variables per remaining orbit: A (cell nonzero) and S (sign of the orbit
representative is +1).  Constraints, for orbit representatives only (the other rows / columns / pairs are images):
  rows: exactly r nonzeros; columns: exactly k nonzeros;
  every orbit of unordered row pairs {i,i'}: exactly L/2 columns with E (both nonzero, equal signs) and exactly L/2
  columns with D (both nonzero, opposite signs), E and D defined by full Tseitin equivalences;
  cardinalities by bidirectional sequential counters.
Options: --s0  symmetry breaking (S0)+(S0') of README 1.4 for the trivial group only: row 0 nonzero exactly in columns
               0..r-1 with +1 there, and column 0 equal to +1 on rows 0..k-1 and 0 elsewhere.
         --unsigned  design only (A variables; pair co-occurrence exactly L); for the two-phase route.
Usage: brd_cnf.py SPEC.json OUT.cnf [--s0] [--unsigned]   writes OUT.cnf and OUT.cnf.map.json (both exclusive).
Stdlib only.
"""
import hashlib
import json
import sys


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []

    def new(self):
        self.nv += 1
        return self.nv

    def add(self, *lits):
        self.clauses.append(lits)


TRUE, FALSE = "T", "F"


def exactly(cnf, lits, k):
    """Bidirectional sequential counter; lits may contain constants TRUE/FALSE.  Asserts sum(lits) == k."""
    lits = [x for x in lits if x != FALSE]
    ntrue = sum(1 for x in lits if x == TRUE)
    lits = [x for x in lits if x != TRUE]
    k -= ntrue
    n = len(lits)
    if k < 0 or k > n:
        cnf.add()  # empty clause: unsatisfiable
        return
    if k == 0:
        for x in lits:
            cnf.add(-x)
        return
    if k == n:
        for x in lits:
            cnf.add(x)
        return
    # prev[m] = literal or constant for "at least m of the first i literals", m = 0..k+1
    prev = [TRUE] + [FALSE] * (k + 1)
    for i, x in enumerate(lits, start=1):
        cur = [TRUE]
        for m in range(1, k + 2):
            if m > i:
                cur.append(FALSE)
                continue
            a, b = prev[m], prev[m - 1]  # s = a OR (x AND b)
            if a == TRUE:
                cur.append(TRUE)
                continue
            if a == FALSE and b == FALSE:
                cur.append(FALSE)
                continue
            s = cnf.new()
            if a != FALSE:
                cnf.add(-a, s)
                cnf.add(-s, a, x)
            else:
                cnf.add(-s, x)
            if b == TRUE:
                cnf.add(-x, s)
            elif b != FALSE:
                cnf.add(-x, -b, s)
                if a != FALSE:
                    cnf.add(-s, a, b)
                else:
                    cnf.add(-s, b)
            else:  # b FALSE: s == a (a is a literal here)
                cnf.add(-s, a)
            cur.append(s)
        prev = cur
    # assert at least k and not at least k+1
    if prev[k] == FALSE:
        cnf.add()
    elif prev[k] != TRUE:
        cnf.add(prev[k])
    if prev[k + 1] == TRUE:
        cnf.add()
    elif prev[k + 1] != FALSE:
        cnf.add(-prev[k + 1])


def build(spec, s0=False, unsigned=False):
    v, b, r, k, lam = spec["params"]
    gens = spec["generators"]
    ncell = v * b
    parent = list(range(ncell))
    par = [0] * ncell  # parity relative to parent

    def find(c):
        path = []
        while parent[c] != c:
            path.append(c)
            c = parent[c]
        root = c
        # path compression with parity
        acc = 0
        for node in reversed(path):
            acc ^= par[node]
            par[node] = acc
            parent[node] = root
        return root

    def find_par(c):
        root = find(c)
        return root, (par[c] if c != root else 0)

    conflicts = []
    for g in gens:
        rows, cols = g["rows"], g["cols"]
        for i in range(v):
            ri, rs = rows[i]
            for j in range(b):
                cj, cs = cols[j]
                c1 = i * b + j
                c2 = ri * b + cj
                rel = 0 if rs * cs == 1 else 1
                r1, p1 = find_par(c1)
                r2, p2 = find_par(c2)
                if r1 == r2:
                    if p1 ^ p2 != rel:
                        conflicts.append(c1)
                else:
                    parent[r2] = r1
                    par[r2] = p1 ^ p2 ^ rel
    zero_roots = {find(c) for c in conflicts}
    cnf = CNF()
    var_a, var_s = {}, {}
    cells = []
    for c in range(ncell):
        root, p = find_par(c)
        if root in zero_roots:
            cells.append(0)
            continue
        if root not in var_a:
            var_a[root] = cnf.new()
            var_s[root] = None if unsigned else cnf.new()
        cells.append([var_a[root], var_s[root], p])

    def A(i, j):
        c = cells[i * b + j]
        return FALSE if c == 0 else c[0]

    def POS(i, j):
        c = cells[i * b + j]
        return c[1] if c[2] == 0 else -c[1]

    # orbits of rows, columns and unordered row pairs under the permutation parts
    def orbit_reps(points, act):
        seen, reps = set(), []
        for p in points:
            if p in seen:
                continue
            reps.append(p)
            stack = [p]
            seen.add(p)
            while stack:
                q = stack.pop()
                for g in gens:
                    q2 = act(g, q)
                    if q2 not in seen:
                        seen.add(q2)
                        stack.append(q2)
        return reps

    row_reps = orbit_reps(range(v), lambda g, i: g["rows"][i][0])
    col_reps = orbit_reps(range(b), lambda g, j: g["cols"][j][0])
    pairs = [(i, i2) for i in range(v) for i2 in range(i + 1, v)]

    def pact(g, p):
        a, c = g["rows"][p[0]][0], g["rows"][p[1]][0]
        return (a, c) if a < c else (c, a)

    pair_reps = orbit_reps(pairs, pact)

    for i in row_reps:
        exactly(cnf, [A(i, j) for j in range(b)], r)
    for j in col_reps:
        exactly(cnf, [A(i, j) for i in range(v)], k)
    for (i, i2) in pair_reps:
        if unsigned:
            both = []
            for j in range(b):
                a1, a2 = A(i, j), A(i2, j)
                if a1 == FALSE or a2 == FALSE:
                    continue
                if a1 == a2:
                    both.append(a1)
                    continue
                c = cnf.new()
                cnf.add(-c, a1)
                cnf.add(-c, a2)
                cnf.add(-a1, -a2, c)
                both.append(c)
            exactly(cnf, both, lam)
            continue
        E, D = [], []
        for j in range(b):
            c1, c2 = cells[i * b + j], cells[i2 * b + j]
            if c1 == 0 or c2 == 0:
                continue
            a1, a2 = c1[0], c2[0]
            if a1 == a2:  # same orbit: sign relation fixed
                if c1[2] == c2[2]:
                    E.append(a1)
                else:
                    D.append(a1)
                continue
            x, y = POS(i, j), POS(i2, j)
            e = cnf.new()
            cnf.add(-e, a1)
            cnf.add(-e, a2)
            cnf.add(-e, -x, y)
            cnf.add(-e, x, -y)
            cnf.add(-a1, -a2, -x, -y, e)
            cnf.add(-a1, -a2, x, y, e)
            d = cnf.new()
            cnf.add(-d, a1)
            cnf.add(-d, a2)
            cnf.add(-d, x, y)
            cnf.add(-d, -x, -y)
            cnf.add(-a1, -a2, -x, y, d)
            cnf.add(-a1, -a2, x, -y, d)
            E.append(e)
            D.append(d)
        exactly(cnf, E, lam // 2)
        exactly(cnf, D, lam // 2)
    if s0:
        if gens:
            raise SystemExit("--s0 is only valid for the trivial group")
        for j in range(b):
            cnf.add(A(0, j) if j < r else -A(0, j))
            if j < r and not unsigned:
                cnf.add(POS(0, j))
        for i in range(v):
            cnf.add(A(i, 0) if i < k else -A(i, 0))
            if i < k and not unsigned:
                cnf.add(POS(i, 0))
    stats = {"cells": ncell, "forced_zero_cells": sum(1 for c in cells if c == 0), "orbit_vars": len(var_a),
             "row_reps": len(row_reps), "col_reps": len(col_reps), "pair_reps": len(pair_reps),
             "vars": cnf.nv, "clauses": len(cnf.clauses)}
    return cnf, cells, stats


def main(argv):
    args = argv[1:]
    if len(args) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    spec_path, out = args[0], args[1]
    s0 = "--s0" in args[2:]
    unsigned = "--unsigned" in args[2:]
    spec_bytes = open(spec_path, "rb").read()
    spec = json.loads(spec_bytes)
    cnf, cells, stats = build(spec, s0=s0, unsigned=unsigned)
    with open(out, "x") as f:
        f.write(f"p cnf {cnf.nv} {len(cnf.clauses)}\n")
        for cl in cnf.clauses:
            f.write(" ".join(map(str, cl)) + " 0\n")
    mp = {"spec": spec_path, "spec_sha256": hashlib.sha256(spec_bytes).hexdigest(), "model": spec["model"],
          "params": spec["params"], "s0": s0, "unsigned": unsigned, "stats": stats, "cells": cells}
    with open(out + ".map.json", "x") as f:
        json.dump(mp, f)
        f.write("\n")
    print(json.dumps({"model": spec["model"], **stats,
                      "cnf_sha256": hashlib.sha256(open(out, "rb").read()).hexdigest()}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

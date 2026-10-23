#!/usr/bin/env python3
"""inv_cnf.py -- CNF for a RESTRICTED group-invariant model of BTD(14,28;8,3,14;7,6) (README 1.3 and amendment A1).

Encoding A of code/btd_cnf_a.py WITHOUT symmetry breaking (thermometer a = [m >= 1], b = [m = 2], (b -> a), row
counts, column sums, pairwise products; the same calls as btd_cnf_a.main with --no-symmetry), plus for the model's
generator (g on rows, h on columns) the equivalences a[g(i)][h(j)] <-> a[i][j] and b[g(i)][h(j)] <-> b[i][j], i.e.
M(g(i), h(j)) = M(i, j); invariance under the generator is invariance under the cyclic group it generates.
Models (row index i, column index j):
  R1     rows 7r+s (r<2), columns 7c+u (c<4); s -> s+1, u -> u+1 (mod 7)
  R2     rows s (mod 14); columns 14c+u (c<2), u -> u+1 (mod 14)
  R3     rows s<13 cycle (mod 13), row 13 fixed; columns 13c+u (c<2) cycle, columns 26, 27 fixed
  R4-k3  rows as R1; columns 7c+u (c<3) cycle, columns 21..27 fixed
  R4-k2  rows as R1; columns 7c+u (c<2) cycle, columns 14..27 fixed
  R5-kK  rows 0..6 cycle (mod 7), rows 7..13 fixed; columns 7c+u (c<K) cycle, the other columns fixed (K = 1, 2, 3)
A model is satisfiable iff a BTD invariant under that permutation pair exists.  RESTRICTED: UNSAT never excludes the
target.  Writes OUT.cnf (exclusive) and OUT.cnf.map.json (exclusive).  Usage: inv_cnf.py MODEL OUT.cnf   (stdlib)
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btd_cnf_a import CNF  # noqa: E402

V, B, P1, P2, R, K, L = 14, 28, 8, 3, 14, 7, 6


def cyc(n_orbits, size, total):
    """permutation of range(total): the first n_orbits*size points in cycles of `size`, the rest fixed"""
    out = []
    for p in range(total):
        if p < n_orbits * size:
            o, s = divmod(p, size)
            out.append(o * size + (s + 1) % size)
        else:
            out.append(p)
    return out


def generator(model):
    if model == "R1":
        return cyc(2, 7, V), cyc(4, 7, B)
    if model == "R2":
        return cyc(1, 14, V), cyc(2, 14, B)
    if model == "R3":
        return cyc(1, 13, V), cyc(2, 13, B)
    if model == "R4-k3":
        return cyc(2, 7, V), cyc(3, 7, B)
    if model == "R4-k2":
        return cyc(2, 7, V), cyc(2, 7, B)
    if model in ("R5-k1", "R5-k2", "R5-k3"):
        return cyc(1, 7, V), cyc(int(model[-1]), 7, B)
    raise SystemExit(f"unknown model {model}")


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    model, out = argv[1], argv[2]
    g, h = generator(model)
    assert sorted(g) == list(range(V)) and sorted(h) == list(range(B))
    F = CNF()
    a = [[F.new() for j in range(B)] for i in range(V)]
    b = [[F.new() for j in range(B)] for i in range(V)]
    for i in range(V):
        for j in range(B):
            F.add(-b[i][j], a[i][j])
    for i in range(V):
        F.exactly([a[i][j] for j in range(B)], P1 + P2)
        F.exactly([b[i][j] for j in range(B)], P2)
    for j in range(B):
        F.exactly([lit for i in range(V) for lit in (a[i][j], b[i][j])], K)
    for i in range(V):
        for k in range(i + 1, V):
            prods = []
            for j in range(B):
                for x in (a[i][j], b[i][j]):
                    for y in (a[k][j], b[k][j]):
                        prods.append(F.AND(x, y))
            F.exactly(prods, L)
    n_base = len(F.clauses)
    for i in range(V):
        for j in range(B):
            for X in (a, b):
                p, q = X[g[i]][h[j]], X[i][j]
                if p != q:
                    F.add(-p, q)
                    F.add(p, -q)
    me = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    with open(out, "x") as f:
        f.write(f"c inv_cnf.py sha256 {me} RESTRICTED model {model} base_clauses {n_base}\n"
                f"p cnf {F.nv} {len(F.clauses)}\n")
        for c in F.clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
    with open(out + ".map.json", "x") as f:
        json.dump({"generator_sha256": me, "model": model, "params": [V, B, P1, P2, R, K, L], "row_perm": g,
                   "col_perm": h, "a": a, "b": b, "vars": F.nv, "clauses": len(F.clauses)}, f)
    print(json.dumps({"model": model, "out": out, "vars": F.nv, "clauses": len(F.clauses)}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

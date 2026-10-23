#!/usr/bin/env python3
"""type_cnf.py -- CNF for one column-type case of BTD(14,28;8,3,14;7,6) (exploratory; a case split built on it must be
frozen in a README amendment before use).  Stdlib.

Every column has a_j ones and d_j twos with a_j + 2 d_j = 7, so (a_j, d_j) is (7,0), (5,1), (3,2) or (1,3).  For a
type vector (n1, n3, n5, n7) (numbers of columns with a_j = 1, 3, 5, 7) the case CNF is encoding A of
code/btd_cnf_a.py without its own symmetry breaking (thermometer a = [m >= 1], b = [m = 2], (b -> a), row counts,
column sums, pairwise products: the same calls as btd_cnf_a.main with --no-symmetry) plus
  * column types: columns 0..n7-1 have exactly 0 twos, the next n5 columns exactly 1, the next n3 exactly 2, the last
    n1 exactly 3 (with the column sum 7 this fixes a_j);
  * symmetry: rows lexicographically nondecreasing (top to bottom, each row read left to right) and, inside each type
    block, columns lexicographically nondecreasing (left to right, each column read top to bottom), compared through
    the order-preserving pair map 0 -> (0,0), 1 -> (1,0), 2 -> (1,1) of (a, b) as in btd_cnf_a (CNF.lex_leq).
Completeness of the symmetry breaking for one case: permuting columns inside a type block and permuting rows preserve
the definition and the case; the min-flattening argument of btd12-15 README 1.3 applied to the group
S_14 x (product of the symmetric groups of the blocks) gives a member of every orbit satisfying both lex conditions.
Writes OUT.cnf (exclusive) and OUT.cnf.map.json (exclusive).  Usage: type_cnf.py n1 n3 n5 n7 OUT.cnf
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btd_cnf_a import CNF  # noqa: E402

V, B, P1, P2, R, K, L = 14, 28, 8, 3, 14, 7, 6


def main(argv):
    if len(argv) != 6:
        print(__doc__, file=sys.stderr)
        return 2
    n1, n3, n5, n7 = (int(x) for x in argv[1:5])
    out = argv[5]
    if n1 + n3 + n5 + n7 != B or n1 + 3 * n3 + 5 * n5 + 7 * n7 != V * P1:
        print("type vector must have 28 columns and 112 ones", file=sys.stderr)
        return 2
    dcol = [0] * n7 + [1] * n5 + [2] * n3 + [3] * n1
    blocks = [(0, n7), (n7, n7 + n5), (n7 + n5, n7 + n5 + n3), (n7 + n5 + n3, B)]
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
    for j in range(B):
        F.exactly([b[i][j] for i in range(V)], dcol[j])
    for i in range(V - 1):
        F.lex_leq([v for j in range(B) for v in (a[i][j], b[i][j])],
                  [v for j in range(B) for v in (a[i + 1][j], b[i + 1][j])])
    for lo, hi in blocks:
        for j in range(lo, hi - 1):
            F.lex_leq([v for i in range(V) for v in (a[i][j], b[i][j])],
                      [v for i in range(V) for v in (a[i][j + 1], b[i][j + 1])])
    me = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    with open(out, "x") as f:
        f.write(f"c type_cnf.py sha256 {me} types n1 {n1} n3 {n3} n5 {n5} n7 {n7} base_clauses {n_base}\n"
                f"p cnf {F.nv} {len(F.clauses)}\n")
        for c in F.clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
    with open(out + ".map.json", "x") as f:
        json.dump({"generator_sha256": me, "params": [V, B, P1, P2, R, K, L], "types": [n1, n3, n5, n7],
                   "a": a, "b": b, "vars": F.nv, "clauses": len(F.clauses)}, f)
    print(json.dumps({"out": out, "types": [n1, n3, n5, n7], "vars": F.nv, "clauses": len(F.clauses)}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

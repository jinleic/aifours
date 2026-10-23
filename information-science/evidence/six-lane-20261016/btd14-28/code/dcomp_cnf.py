#!/usr/bin/env python3
"""dcomp_cnf.py -- dedicated CNF for the 2-pattern completion of a fixed 1-pattern (structure route, README 1.4(a)).

Given BTD parameters (V,B;p1,p2,R;K,L) and a 1-pattern A (V rows, each a set of exactly p1 columns), the CNF is
satisfiable iff there is a V x B matrix M = A + 2D over {0,1,2} that is a BTD(V,B;p1,p2,R;K,L), i.e. iff a 0/1 matrix
D with D_ij = 0 wherever A_ij = 1 satisfies
  (R) every row of D has exactly p2 ones                         (row i of M: p1 ones, p2 twos);
  (C) column j: a_j + 2 sum_i D_ij = K, a_j = #{i : A_ij = 1}       (column sums);
  (P) rows i < k: x_ik + 2 u_ik + 4 z_ik = L, where x_ik = |A_i cap A_k|, u_ik = |A_i cap D_k| + |D_i cap A_k|,
      z_ik = |D_i cap D_k|                                          (since M_i . M_k = x + 2u + 4z).
Variables: d_ij for each cell with A_ij = 0 (numbered row-major), then auxiliaries.  Encoding: (C) is
"exactly (K - a_j)/2 of {d_ij}" (empty clause if K - a_j is negative or odd); (P) is "exactly (L - x_ik)/2" of the
literal list [d_kj : j in A_i \ A_k] + [d_ij : j in A_k \ A_i] + twice [p_ikj : j outside A_i cup A_k] with
p_ikj <-> d_ij & d_kj (empty clause if L - x_ik is negative or odd).  Cardinality: the two-sided Sinz counter
CNF.exactly of code/btd_cnf_a.py (imported unchanged), which counts list positions, so a literal listed twice counts
twice.  (Cells with A_ij = 1 have no D-variable: D_kj for j in A_k is 0 by construction.)
Input CASE.json: {"name": ..., "rows": [[p1 columns] x V]}; parameters default to 12 20 4 3 10 6 4 or are given by
--params V B p1 p2 R K L.  Writes OUT.cnf (exclusive) and OUT.cnf.map.json (exclusive: d-variable numbers).
Usage: dcomp_cnf.py CASE.json OUT.cnf [--params V B p1 p2 R K L]
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btd_cnf_a import CNF  # noqa: E402


def build(params, rows):
    V, B, p1, p2, R, K, L = params
    if R != p1 + 2 * p2:
        raise ValueError("R != p1 + 2 p2")
    A = [set(r) for r in rows]
    if len(A) != V or any(len(r) != p1 or len(set(rows[i])) != p1 or not all(0 <= c < B for c in r)
                          for i, r in enumerate(A)):
        raise ValueError("A must have V rows of p1 distinct columns in 0..B-1")
    F = CNF()
    d = [[F.new() if j not in A[i] else None for j in range(B)] for i in range(V)]
    for i in range(V):
        F.exactly([d[i][j] for j in range(B) if d[i][j] is not None], p2)
    for j in range(B):
        aj = sum(1 for i in range(V) if j in A[i])
        need = K - aj
        if need < 0 or need % 2:
            F.add()
            continue
        F.exactly([d[i][j] for i in range(V) if d[i][j] is not None], need // 2)
    for i in range(V):
        for k in range(i + 1, V):
            t = L - len(A[i] & A[k])
            if t < 0 or t % 2:
                F.add()
                continue
            lits = [d[k][j] for j in sorted(A[i] - A[k])] + [d[i][j] for j in sorted(A[k] - A[i])]
            for j in range(B):
                if j not in A[i] and j not in A[k]:
                    p = F.AND(d[i][j], d[k][j])
                    lits += [p, p]
            F.exactly(lits, t // 2)
    return F, d


def main(argv):
    args = argv[1:]
    params = (12, 20, 4, 3, 10, 6, 4)
    if len(args) == 10 and args[2] == "--params":
        params = tuple(int(x) for x in args[3:10])
        args = args[:2]
    if len(args) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    case_bytes = open(args[0], "rb").read()
    case = json.loads(case_bytes)
    rows = [list(r) for r in case["rows"]]
    F, d = build(params, rows)
    me = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    text = (f"c dcomp_cnf.py sha256 {me}\nc params {' '.join(map(str, params))} case {case.get('name')}\n"
            f"p cnf {F.nv} {len(F.clauses)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in F.clauses))
    with open(args[1], "x") as f:
        f.write(text)
    with open(args[1] + ".map.json", "x") as f:
        json.dump({"generator": "dcomp_cnf.py", "generator_sha256": me, "params": list(params),
                   "case_sha256": hashlib.sha256(case_bytes).hexdigest(), "rows": rows, "d": d,
                   "vars": F.nv, "clauses": len(F.clauses)}, f)
    print(json.dumps({"case": case.get("name"), "out": args[1], "vars": F.nv, "clauses": len(F.clauses),
                      "cnf_sha256": hashlib.sha256(text.encode()).hexdigest()}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

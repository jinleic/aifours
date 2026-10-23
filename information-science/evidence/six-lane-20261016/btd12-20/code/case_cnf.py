#!/usr/bin/env python3
"""case_cnf.py -- CNF for one A-pattern case of BTD(12,20;4,3,10;6,4) (structure route, README 1.4(a)).  Stdlib.

The formula is encoding A of code/btd_cnf_a.py (unchanged import, copied with SHA from btd12-15/btd14-18) for the
parameters 12 20 4 3 10 6 4 WITHOUT any symmetry breaking -- the clauses (b -> a), (D2) row counts, (D3) column sums
and (D4) pairwise products, built by the same calls in the same order as btd_cnf_a.main with --no-symmetry -- plus
the case clauses that fix the 1-pattern to the given A:
  A_ij = 1:  a_ij  and  -b_ij              (m_ij = 1)
  A_ij = 0:  -a_ij v b_ij                  (with b -> a: m_ij in {0, 2})
So the formula is satisfiable iff some BTD(12,20;4,3,10;6,4) has 1-pattern exactly A.
Input: a JSON object {"name": ..., "rows": [[4 columns] x 12]} (one line of a --rows file, or one d-type multigraph
converted by code/case_list.py).  Writes OUT.cnf (exclusive; plain DIMACS, or zstd-compressed when OUT ends in .zst).
Usage: case_cnf.py CASE.json OUT.cnf[.zst]
"""
import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import btd_cnf_a  # noqa: E402

PARAMS = (12, 20, 4, 3, 10, 6, 4)


def build(rows):
    V, B, p1, p2, R, K, L = PARAMS
    if len(rows) != V or any(len(set(r)) != p1 or not all(0 <= c < B for c in r) for r in rows):
        raise ValueError("A must be 12 rows of 4 distinct columns in 0..19")
    F = btd_cnf_a.CNF()
    a = [[F.new() for j in range(B)] for i in range(V)]
    b = [[F.new() for j in range(B)] for i in range(V)]
    for i in range(V):
        for j in range(B):
            F.add(-b[i][j], a[i][j])
    for i in range(V):
        F.exactly([a[i][j] for j in range(B)], p1 + p2)
        F.exactly([b[i][j] for j in range(B)], p2)
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
            if j in rows[i]:
                F.add(a[i][j])
                F.add(-b[i][j])
            else:
                F.add(-a[i][j], b[i][j])
    return F, n_base


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    case = json.loads(open(argv[1]).read())
    rows = [sorted(r) for r in case["rows"]]
    F, n_base = build(rows)
    me = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    enc = hashlib.sha256(open(btd_cnf_a.__file__, "rb").read()).hexdigest()
    text = (f"c case_cnf.py sha256 {me} btd_cnf_a.py sha256 {enc}\n"
            f"c params {' '.join(map(str, PARAMS))} symmetry none base_clauses {n_base} case {case.get('name')}\n"
            f"p cnf {F.nv} {len(F.clauses)}\n" + "".join(" ".join(map(str, c)) + " 0\n" for c in F.clauses))
    out = argv[2]
    if out.endswith(".zst"):
        if os.path.exists(out):
            raise SystemExit(f"{out} exists")
        p = subprocess.run(["zstd", "-q", "-19", "-o", out], input=text.encode(), capture_output=True)
        if p.returncode != 0:
            raise SystemExit(p.stderr.decode())
    else:
        with open(out, "x") as f:
            f.write(text)
    print(json.dumps({"case": case.get("name"), "out": out, "vars": F.nv, "clauses": len(F.clauses),
                      "cnf_sha256": hashlib.sha256(text.encode()).hexdigest()}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

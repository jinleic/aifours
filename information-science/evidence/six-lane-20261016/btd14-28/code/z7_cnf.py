#!/usr/bin/env python3
"""z7_cnf.py -- CNF of the RESTRICTED model (R1) in orbit form (same conditions as code/z7_reduced.py; README 1.3).

Variables: a[r][c][t] = [v = 1], b[r][c][t] = [v = 2] (r < 2, c < 4, t in Z_7), with (-a v -b).  Constraints, all with
the two-sided Sinz counter CNF.exactly of code/btd_cnf_a.py (a literal listed k times counts k times):
  rows:    exactly 8 of a[r][*][*], exactly 3 of b[r][*][*]                         (r = 0, 1);
  columns: exactly 7 of [a[r][c][t] once, b[r][c][t] twice : r, t]                 (c = 0..3);
  pairs:   for (r,r',d) in (0,0,1..3), (1,1,1..3), (0,1,0..6): exactly 6 of the list
           [aa once, ab twice, ba twice, bb four times] over c, t, where aa = a[r][c][t] AND a[r'][c][t+d] etc.
A model gives the 56 values v and the full matrix M[(r,s)][(c,u)] = v[r][c][u-s] (code/z7_reduced.py documents why this
is exactly the Z_7-invariant BTD condition).  RESTRICTED: UNSAT or UNKNOWN never excludes the target.
Writes OUT.cnf (exclusive) and OUT.cnf.map.json (exclusive; variable numbers).  Usage: z7_cnf.py OUT.cnf   (stdlib)
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from btd_cnf_a import CNF  # noqa: E402


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    F = CNF()
    a = {(r, c, t): F.new() for r in range(2) for c in range(4) for t in range(7)}
    b = {(r, c, t): F.new() for r in range(2) for c in range(4) for t in range(7)}
    for k in a:
        F.add(-a[k], -b[k])
    for r in range(2):
        F.exactly([a[r, c, t] for c in range(4) for t in range(7)], 8)
        F.exactly([b[r, c, t] for c in range(4) for t in range(7)], 3)
    for c in range(4):
        F.exactly([lit for r in range(2) for t in range(7) for lit in (a[r, c, t], b[r, c, t], b[r, c, t])], 7)
    cons = [(0, 0, d) for d in (1, 2, 3)] + [(1, 1, d) for d in (1, 2, 3)] + [(0, 1, d) for d in range(7)]
    for r, rp, d in cons:
        lits = []
        for c in range(4):
            for t in range(7):
                u = (t + d) % 7
                lits += [F.AND(a[r, c, t], a[rp, c, u])]
                lits += [F.AND(a[r, c, t], b[rp, c, u])] * 2
                lits += [F.AND(b[r, c, t], a[rp, c, u])] * 2
                lits += [F.AND(b[r, c, t], b[rp, c, u])] * 4
        F.exactly(lits, 6)
    me = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    with open(argv[1], "x") as f:
        f.write(f"c z7_cnf.py sha256 {me} RESTRICTED model R1 orbit form\np cnf {F.nv} {len(F.clauses)}\n")
        for c in F.clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
    with open(argv[1] + ".map.json", "x") as f:
        json.dump({"generator_sha256": me, "a": {f"{r}{c}{t}": v for (r, c, t), v in a.items()},
                   "b": {f"{r}{c}{t}": v for (r, c, t), v in b.items()}, "vars": F.nv, "clauses": len(F.clauses)}, f)
    print(json.dumps({"out": argv[1], "vars": F.nv, "clauses": len(F.clauses)}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

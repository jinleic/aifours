#!/usr/bin/env python3
"""restricted_afix.py -- RESTRICTED witness search for BTD(12,20;4,3,10;6,4) with the 1-pattern A fixed (README 1.3, 1.4(b)).

M = A + 2D.  The 12 rows of A are given as tetrads (4-subsets of the 20 columns).  CP-SAT decides the 2-pattern D:
Boolean d[i][j] for j not in A_i; row i: sum_j d[i][j] = 3; column j: a_j + 2 sum_i d[i][j] = 6; rows i < k:
|A_i cap A_k| + 2 |A_i cap D_k| + 2 |D_i cap A_k| + 4 |D_i cap D_k| = 4 (products of Booleans linearised exactly with
fully defined AND variables).  Every solution is a full BTD matrix; it is written in strict format and must still pass
both checkers.  INFEASIBLE / UNKNOWN only say that THIS A-pattern has no completion (or none was found): a RESTRICTED
miss is never an exclusion of the target.

Usage (OR-Tools from tools/pydeps312 under the uv CPython 3.12):
  restricted_afix.py SPEC.json OUTDIR --time S [--seed N]
SPEC.json: {"name": ..., "rows": [[c1,c2,c3,c4], ... 12 tetrads, 0-based columns]}.  OUTDIR must not exist.
Writes OUTDIR/result.json (and OUTDIR/witness.btd when FEASIBLE).  Exit 10 found, 20 infeasible, 0 unknown, 2 usage.
"""
import hashlib
import json
import os
import sys
import time

from ortools.sat.python import cp_model

V, B, P1, P2, R, K, L = 12, 20, 4, 3, 10, 6, 4


def main(argv):
    args = argv[1:]
    if len(args) < 4 or args[2] != "--time":
        print(__doc__, file=sys.stderr)
        return 2
    spec_path, outdir, tlim = args[0], args[1], float(args[3])
    seed = 0
    if len(args) == 6 and args[4] == "--seed":
        seed = int(args[5])
    elif len(args) != 4:
        print(__doc__, file=sys.stderr)
        return 2
    spec_bytes = open(spec_path, "rb").read()
    spec = json.loads(spec_bytes)
    rows = [sorted(set(r)) for r in spec["rows"]]
    if len(rows) != V or any(len(r) != P1 or not all(0 <= c < B for c in r) for r in rows):
        print("bad spec: need 12 tetrads of distinct columns in 0..19", file=sys.stderr)
        return 2
    A = [[1 if j in r else 0 for j in range(B)] for r in rows]
    a = [sum(A[i][j] for i in range(V)) for j in range(B)]
    os.makedirs(outdir)
    rec = {"program": "restricted_afix.py", "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "spec": spec_path, "spec_sha256": hashlib.sha256(spec_bytes).hexdigest(), "name": spec.get("name"),
           "time_limit_s": tlim, "workers": 1, "seed": seed, "restricted": True, "column_ones": a}
    pre_ok = all((K - aj) >= 0 and (K - aj) % 2 == 0 for aj in a)
    if not pre_ok:
        rec.update({"status": "INFEASIBLE_PRECHECK", "reason": "some column has an odd or > 6 number of ones"})
        with open(os.path.join(outdir, "result.json"), "x") as f:
            json.dump(rec, f, indent=1)
        print(json.dumps({"name": rec["name"], "status": rec["status"]}))
        return 20
    m = cp_model.CpModel()
    d = [[m.NewBoolVar(f"d{i}_{j}") if not A[i][j] else None for j in range(B)] for i in range(V)]
    for i in range(V):
        m.Add(sum(d[i][j] for j in range(B) if d[i][j] is not None) == P2)
    for j in range(B):
        m.Add(a[j] + 2 * sum(d[i][j] for i in range(V) if d[i][j] is not None) == K)
    for i in range(V):
        for k in range(i + 1, V):
            x = sum(A[i][j] * A[k][j] for j in range(B))
            terms = []
            for j in range(B):
                if A[i][j] and d[k][j] is not None:
                    terms.append(2 * d[k][j])
                if A[k][j] and d[i][j] is not None:
                    terms.append(2 * d[i][j])
                if d[i][j] is not None and d[k][j] is not None:
                    p = m.NewBoolVar(f"p{i}_{k}_{j}")
                    m.AddBoolAnd([d[i][j], d[k][j]]).OnlyEnforceIf(p)
                    m.AddBoolOr([d[i][j].Not(), d[k][j].Not()]).OnlyEnforceIf(p.Not())
                    terms.append(4 * p)
            m.Add(x + sum(terms) == L)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = tlim
    s.parameters.num_workers = 1
    s.parameters.random_seed = seed
    t0 = time.time()
    st = s.Solve(m)
    el = time.time() - t0
    status = s.StatusName(st)
    rec.update({"status": status, "wall_s": round(el, 3)})
    code = 0
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        Mx = [[A[i][j] + (2 * s.Value(d[i][j]) if d[i][j] is not None else 0) for j in range(B)] for i in range(V)]
        txt = f"BTD {V} {B} {P1} {P2} {R} {K} {L}\n" + "".join(" ".join(map(str, r)) + "\n" for r in Mx)
        with open(os.path.join(outdir, "witness.btd"), "x", newline="") as f:
            f.write(txt)
        rec["witness_sha256"] = hashlib.sha256(txt.encode()).hexdigest()
        code = 10
    elif st == cp_model.INFEASIBLE:
        code = 20
    with open(os.path.join(outdir, "result.json"), "x") as f:
        json.dump(rec, f, indent=1)
    print(json.dumps({"name": rec["name"], "status": status, "wall_s": rec["wall_s"]}))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))

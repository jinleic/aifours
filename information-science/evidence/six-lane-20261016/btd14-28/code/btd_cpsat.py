#!/usr/bin/env python3
"""btd_cpsat.py -- CP-SAT witness search for BTD(V,B;p1,p2,R;K,L) (lane btd12-15, README 1.6 item W).

Model: Boolean x[i][j][v] (v = 0, 1, 2), exactly one per cell; row i: sum_j x[i][j][1] = p1, sum_j x[i][j][2] = p2;
column j: sum_i (x[i][j][1] + 2 x[i][j][2]) = K; rows i < k: sum_j sum_{u,w in {1,2}} u*w*y[i][k][j][u][w] = L with
y = x[i][j][u] AND x[k][j][w] (fully defined: y <= both, y >= sum - 1).  Symmetry (S0): row 0 = 0^z 1^p1 2^p2 in
this order (z = B - p1 - p2).  --strengthen adds (C1): every column has at most two 2s (only for the target
parameters, README 1.4; refused otherwise).  Native time limit max_time_in_seconds; num_workers as given.
A CP-SAT INFEASIBLE is information only, never an exclusion.

Usage (OR-Tools 9.15 from tools/pydeps312 under the uv CPython 3.12):
  btd_cpsat.py V B p1 p2 R K L OUTPREFIX --time S --workers W [--seed N] [--strengthen]
Writes (exclusive) OUTPREFIX.json (receipt), OUTPREFIX.log (solver log), and OUTPREFIX.btd when a solution is found
(strict format, README 1.5).  Exit 10 solution, 20 infeasible, 0 unknown/timeout, 2 usage.
"""
import hashlib
import json
import os
import sys
import time

from ortools.sat.python import cp_model


def main(argv):
    args = argv[1:]
    if len(args) < 8:
        print(__doc__, file=sys.stderr)
        return 2
    V, B, p1, p2, R, K, L = (int(x) for x in args[:7])
    pre = args[7]
    opts = args[8:]
    tlim, workers, seed, strengthen = None, None, 0, False
    while opts:
        o = opts.pop(0)
        if o == "--time":
            tlim = float(opts.pop(0))
        elif o == "--workers":
            workers = int(opts.pop(0))
        elif o == "--seed":
            seed = int(opts.pop(0))
        elif o == "--strengthen":
            strengthen = True
        else:
            print(f"bad option {o}", file=sys.stderr)
            return 2
    if tlim is None or workers is None or R != p1 + 2 * p2:
        print("need --time and --workers; R must equal p1 + 2 p2", file=sys.stderr)
        return 2
    if strengthen and (V, B, p1, p2, R, K, L) != (12, 15, 6, 2, 10, 8, 6):
        print("--strengthen is proved only for the target parameters", file=sys.stderr)
        return 2
    m = cp_model.CpModel()
    x = [[[m.NewBoolVar(f"x{i}_{j}_{v}") for v in range(3)] for j in range(B)] for i in range(V)]
    for i in range(V):
        for j in range(B):
            m.AddExactlyOne(x[i][j])
    for i in range(V):
        m.Add(sum(x[i][j][1] for j in range(B)) == p1)
        m.Add(sum(x[i][j][2] for j in range(B)) == p2)
    for j in range(B):
        m.Add(sum(x[i][j][1] + 2 * x[i][j][2] for i in range(V)) == K)
    for i in range(V):
        for k in range(i + 1, V):
            terms = []
            for j in range(B):
                for u in (1, 2):
                    for w in (1, 2):
                        y = m.NewBoolVar(f"y{i}_{k}_{j}_{u}{w}")
                        m.AddImplication(y, x[i][j][u])
                        m.AddImplication(y, x[k][j][w])
                        m.AddBoolOr([x[i][j][u].Not(), x[k][j][w].Not(), y])
                        terms.append(u * w * y)
            m.Add(sum(terms) == L)
    z = B - p1 - p2
    row0 = [0] * z + [1] * p1 + [2] * p2
    for j in range(B):
        m.Add(x[0][j][row0[j]] == 1)
    if strengthen:
        for j in range(B):
            m.Add(sum(x[i][j][2] for i in range(V)) <= 2)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = tlim
    solver.parameters.num_workers = workers
    solver.parameters.random_seed = seed
    solver.parameters.log_search_progress = True
    solver.parameters.log_to_stdout = False
    logf = open(pre + ".log", "x")
    solver.log_callback = lambda s: (logf.write(s + "\n"), logf.flush())
    t0 = time.time()
    st = solver.Solve(m)
    el = time.time() - t0
    logf.close()
    status = solver.StatusName(st)
    rec = {"program": "btd_cpsat.py", "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "params": [V, B, p1, p2, R, K, L], "strengthen": strengthen, "symmetry": "S0 (row 0 fixed)",
           "time_limit_s": tlim, "workers": workers, "seed": seed, "status": status, "wall_s": round(el, 3),
           "conflicts": solver.NumConflicts(), "branches": solver.NumBranches(),
           "ortools_version": __import__("ortools").__version__}
    rc = 0
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        rows = [[next(v for v in range(3) if solver.Value(x[i][j][v])) for j in range(B)] for i in range(V)]
        content = f"BTD {V} {B} {p1} {p2} {R} {K} {L}\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)
        with open(pre + ".btd", "x") as f:
            f.write(content)
        rec["witness_sha256"] = hashlib.sha256(content.encode()).hexdigest()
        rc = 10
    elif st == cp_model.INFEASIBLE:
        rc = 20
    with open(pre + ".json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps(rec))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))

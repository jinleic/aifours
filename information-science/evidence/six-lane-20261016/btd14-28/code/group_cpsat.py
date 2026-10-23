#!/usr/bin/env python3
"""group_cpsat.py -- RESTRICTED group-invariant CP-SAT search for BTD(14,28;8,3,14;7,6) (README 1.3 (R1)-(R3)).

The model is the plain model of code/btd_cpsat.py (Boolean x[i][j][v], v = 0,1,2, exactly one per cell; row counts;
column sums; pairwise products through fully defined AND variables) WITHOUT the (S0) row fixing, plus the invariance
equalities x[g(i)][h(j)][v] = x[i][j][v] for every generator (g on rows, h on columns) of the chosen group.  Every
solution is a full BTD matrix (written in strict format; it must still pass both checkers).  INFEASIBLE / UNKNOWN only
concern the restricted model: never an exclusion of the target.

Models: R1 = Z_7 (rows 7r+s, r < 2; columns 7c+s, c < 4; s -> s+1 mod 7);
        R2 = Z_14 (rows s; columns 14c+s, c < 2; s -> s+1 mod 14);
        R3 = Z_13 (rows s < 13 cycle, row 13 fixed; columns 13c+s, c < 2, cycle, columns 26, 27 fixed).
Usage (OR-Tools from tools/pydeps312 under the uv CPython 3.12):
  group_cpsat.py MODEL OUTPREFIX --time S [--seed N]
Writes OUTPREFIX.json (exclusive), OUTPREFIX.log and OUTPREFIX.btd when a solution is found.
Exit 10 solution, 20 infeasible, 0 unknown, 2 usage.
"""
import hashlib
import json
import sys
import time

from ortools.sat.python import cp_model

V, B, P1, P2, R, K, L = 14, 28, 8, 3, 14, 7, 6


def generators(model):
    if model == "R1":
        g = [7 * (i // 7) + (i % 7 + 1) % 7 for i in range(V)]
        h = [7 * (j // 7) + (j % 7 + 1) % 7 for j in range(B)]
    elif model == "R2":
        g = [(i + 1) % 14 for i in range(V)]
        h = [14 * (j // 14) + (j % 14 + 1) % 14 for j in range(B)]
    elif model == "R3":
        g = [(i + 1) % 13 if i < 13 else 13 for i in range(V)]
        h = [13 * (j // 13) + (j % 13 + 1) % 13 if j < 26 else j for j in range(B)]
    else:
        raise SystemExit(f"unknown model {model}")
    assert sorted(g) == list(range(V)) and sorted(h) == list(range(B))
    return [(g, h)]


def main(argv):
    args = argv[1:]
    if len(args) not in (4, 6) or args[2] != "--time":
        print(__doc__, file=sys.stderr)
        return 2
    model, pre, tlim = args[0], args[1], float(args[3])
    seed = int(args[5]) if len(args) == 6 and args[4] == "--seed" else 0
    gens = generators(model)
    m = cp_model.CpModel()
    x = [[[m.NewBoolVar(f"x{i}_{j}_{v}") for v in range(3)] for j in range(B)] for i in range(V)]
    for i in range(V):
        for j in range(B):
            m.AddExactlyOne(x[i][j])
    for i in range(V):
        m.Add(sum(x[i][j][1] for j in range(B)) == P1)
        m.Add(sum(x[i][j][2] for j in range(B)) == P2)
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
    for g, h in gens:
        for i in range(V):
            for j in range(B):
                for v in range(3):
                    m.Add(x[g[i]][h[j]][v] == x[i][j][v])
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = tlim
    solver.parameters.num_workers = 1
    solver.parameters.random_seed = seed
    solver.parameters.log_search_progress = True
    solver.parameters.log_to_stdout = False
    logf = open(pre + ".log", "x")
    solver.log_callback = lambda s: (logf.write(s + "\n"), logf.flush())
    t0 = time.time()
    st = solver.Solve(m)
    el = time.time() - t0
    logf.close()
    rec = {"program": "group_cpsat.py", "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "model": model, "restricted": True, "generators": gens, "time_limit_s": tlim, "workers": 1, "seed": seed,
           "status": solver.StatusName(st), "wall_s": round(el, 3), "conflicts": solver.NumConflicts()}
    rc = 0
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        rows = [[next(v for v in range(3) if solver.Value(x[i][j][v])) for j in range(B)] for i in range(V)]
        content = f"BTD {V} {B} {P1} {P2} {R} {K} {L}\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)
        with open(pre + ".btd", "x") as f:
            f.write(content)
        rec["witness_sha256"] = hashlib.sha256(content.encode()).hexdigest()
        rc = 10
    elif st == cp_model.INFEASIBLE:
        rc = 20
    with open(pre + ".json", "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print(json.dumps({k: rec[k] for k in ("model", "status", "wall_s")}))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv))

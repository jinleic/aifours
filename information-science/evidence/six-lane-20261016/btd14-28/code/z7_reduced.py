#!/usr/bin/env python3
"""z7_reduced.py -- RESTRICTED model (R1) of README 1.3 in orbit form: Z_7 acting semiregularly on the 14 rows
(2 orbits) and the 28 columns (4 orbits) of a BTD(14,28;8,3,14;7,6).

Rows (r, s), columns (c, u), r < 2, c < 4, s, u in Z_7 (row index 7r + s, column index 7c + u); invariance under
s -> s+1, u -> u+1 means M[(r,s)][(c,u)] = v[r][c][u - s mod 7] for 56 values v in {0,1,2} (every semiregular Z_7
action on rows and columns has this form after relabelling).  The BTD conditions become exactly:
  rows:    for each r: #{(c,t) : v[r][c][t] = 1} = 8 and #{(c,t) : v[r][c][t] = 2} = 3;
  columns: for each c: sum_r sum_t v[r][c][t] = 7;
  pairs:   P(r,r',d) = sum_c sum_t v[r][c][t] v[r'][c][t+d] = 6 for (r,r') = (0,0), (1,1) with d = 1,2,3 (P(r,r,-d) =
           P(r,r,d)) and for (r,r') = (0,1) with d = 0..6 (rows (r,s), (r',s') have inner product P(r,r',s'-s)).
CP-SAT on Booleans x1 = [v = 1], x2 = [v = 2] with fully defined AND products.  A solution is expanded to the full
14 x 28 matrix and written in strict format (it must still pass both checkers).  INFEASIBLE / UNKNOWN concern only
this restricted model, never the target.
Usage: z7_reduced.py OUTPREFIX --time S [--seed N] [--workers W]
"""
import hashlib
import json
import sys
import time

from ortools.sat.python import cp_model


def main(argv):
    args = argv[1:]
    if len(args) < 3 or args[1] != "--time":
        print(__doc__, file=sys.stderr)
        return 2
    pre, tlim = args[0], float(args[2])
    seed, workers = 0, 1
    rest = args[3:]
    while rest:
        o = rest.pop(0)
        if o == "--seed":
            seed = int(rest.pop(0))
        elif o == "--workers":
            workers = int(rest.pop(0))
        else:
            print(__doc__, file=sys.stderr)
            return 2
    m = cp_model.CpModel()
    x = {}
    for r in range(2):
        for c in range(4):
            for t in range(7):
                a, b = m.NewBoolVar(f"a{r}{c}{t}"), m.NewBoolVar(f"b{r}{c}{t}")
                m.AddBoolOr([a.Not(), b.Not()])
                x[r, c, t] = (a, b)
    for r in range(2):
        m.Add(sum(x[r, c, t][0] for c in range(4) for t in range(7)) == 8)
        m.Add(sum(x[r, c, t][1] for c in range(4) for t in range(7)) == 3)
    for c in range(4):
        m.Add(sum(x[r, c, t][0] + 2 * x[r, c, t][1] for r in range(2) for t in range(7)) == 7)

    def prod(p, q):
        y = m.NewBoolVar("")
        m.AddImplication(y, p)
        m.AddImplication(y, q)
        m.AddBoolOr([p.Not(), q.Not(), y])
        return y

    cons = [(0, 0, d) for d in (1, 2, 3)] + [(1, 1, d) for d in (1, 2, 3)] + [(0, 1, d) for d in range(7)]
    for r, rp, d in cons:
        terms = []
        for c in range(4):
            for t in range(7):
                (a1, b1), (a2, b2) = x[r, c, t], x[rp, c, (t + d) % 7]
                terms += [prod(a1, a2), 2 * prod(a1, b2), 2 * prod(b1, a2), 4 * prod(b1, b2)]
        m.Add(sum(terms) == 6)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = tlim
    s.parameters.num_workers = workers
    s.parameters.random_seed = seed
    t0 = time.time()
    st = s.Solve(m)
    el = time.time() - t0
    rec = {"program": "z7_reduced.py", "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "model": "R1 orbit form", "restricted": True, "time_limit_s": tlim, "workers": workers, "seed": seed,
           "status": s.StatusName(st), "wall_s": round(el, 3), "conflicts": s.NumConflicts()}
    rc = 0
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        v = {k: (1 if s.Value(ab[0]) else 2 if s.Value(ab[1]) else 0) for k, ab in x.items()}
        M = [[v[r, c, (u - si) % 7] for c in range(4) for u in range(7)] for r in range(2) for si in range(7)]
        content = "BTD 14 28 8 3 14 7 6\n" + "".join(" ".join(map(str, row)) + "\n" for row in M)
        with open(pre + ".btd", "x") as f:
            f.write(content)
        rec["orbit_values"] = {f"{r}{c}": [v[r, c, t] for t in range(7)] for r in range(2) for c in range(4)}
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

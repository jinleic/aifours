#!/usr/bin/env python3
"""gram_cpsat_crosscheck.py -- supporting cross-check, in a different style from code/proof_check.py, of the finite
part of notes/nonexistence-proof.md (r1).  It searches directly for the whole 15 x 15 integer matrix H (no classes,
no Schur complements, no case analysis): CP-SAT over all entries of H.

Model (for each column-type split (n0, n1, n2) in {(0,6,9), (1,4,10), (2,2,11), (3,0,12)}; columns ordered by type,
which loses nothing because H is only defined up to a simultaneous permutation of rows and columns):
  H symmetric integer; H_jj = 24 - 10 c_j (c_j = 2, 1, 0 for type-2, type-1, type-0);
  off-diagonal H_jk = 5 t_jk - 1 (t_jk integer) with H_jk^2 <= H_jj H_kk          (Step 1, Step 2(b));
  H 1 = 0 and H^2 = 40 H, every entry (products of integer variables)              (Step 1);
  optional --lemma-d: for every 3 columns, det H[S] is a perfect square >= 0 (allowed triples precomputed exactly
  from the three diagonal values; table constraints)                               (Step 6).
Expected (from the r1 proof): with --lemma-d no H exists in any split; without --lemma-d some splits are feasible
(e.g. the n2 = 12 configuration that the proof kills only with Lemma D).  A CP-SAT INFEASIBLE here is supporting
evidence only, never an exclusion by itself.
Usage: gram_cpsat_crosscheck.py OUTDIR --time S --workers W [--lemma-d]          (OUTDIR fresh)
"""
import hashlib
import itertools
import json
import math
import os
import sys
import time

from ortools.sat.python import cp_model


def is_sq(x):
    return x >= 0 and math.isqrt(x) ** 2 == x


def det3(a, b, c, x, y, z):
    # [[a, x, y], [x, b, z], [y, z, c]]
    return a * b * c + 2 * x * y * z - a * z * z - b * y * y - c * x * x


def solve_split(n0, n1, n2, lemma_d, tlim, workers, logpath):
    diag = [4] * n2 + [14] * n1 + [24] * n0
    n = len(diag)
    m = cp_model.CpModel()
    H = {}
    dom = {}
    for j, k in itertools.combinations(range(n), 2):
        bound = math.isqrt(diag[j] * diag[k])
        vals = [v for v in range(-bound, bound + 1) if v % 5 == 4]
        dom[(j, k)] = vals
        H[(j, k)] = m.NewIntVarFromDomain(cp_model.Domain.FromValues(vals), f"H{j}_{k}")

    def h(j, k):
        if j == k:
            return diag[j]
        return H[(min(j, k), max(j, k))]
    # H 1 = 0
    for j in range(n):
        m.Add(sum(h(j, k) for k in range(n)) == 0)
    # products
    prod = {}

    def p(x, y):
        key = (x, y) if (x, y) in prod or (y, x) not in prod else (y, x)
        if key in prod:
            return prod[key]
        jx, kx = x
        jy, ky = y
        vx, vy = H[x], H[y]
        lo = min(a * b for a in dom[x] for b in dom[y])
        hi = max(a * b for a in dom[x] for b in dom[y])
        v = m.NewIntVar(lo, hi, f"P{jx}_{kx}x{jy}_{ky}")
        m.AddMultiplicationEquality(v, [vx, vy])
        prod[key] = v
        return v

    def term(j, l, k):
        # H_jl * H_lk as a linear expression (constant when j == l or l == k)
        if j == l and l == k:
            return diag[j] * diag[j]
        if j == l:
            return diag[j] * h(l, k)
        if l == k:
            return diag[k] * h(j, l)
        a = (min(j, l), max(j, l))
        b = (min(l, k), max(l, k))
        return p(a, b)
    for j in range(n):
        for k in range(j, n):
            m.Add(sum(term(j, l, k) for l in range(n)) == 40 * h(j, k))
    if lemma_d:
        for j, k, l in itertools.combinations(range(n), 3):
            allowed = [(x, y, z) for x in dom[(j, k)] for y in dom[(j, l)] for z in dom[(k, l)]
                       if is_sq(det3(diag[j], diag[k], diag[l], x, y, z))]
            m.AddAllowedAssignments([H[(j, k)], H[(j, l)], H[(k, l)]], allowed)
    s = cp_model.CpSolver()
    s.parameters.max_time_in_seconds = tlim
    s.parameters.num_workers = workers
    s.parameters.log_search_progress = True
    s.parameters.log_to_stdout = False
    lf = open(logpath, "x")
    s.log_callback = lambda line: (lf.write(line + "\n"), lf.flush())
    t0 = time.time()
    st = s.Solve(m)
    el = time.time() - t0
    lf.close()
    res = {"split": [n0, n1, n2], "lemma_d": lemma_d, "status": s.StatusName(st), "wall_s": round(el, 3),
           "conflicts": s.NumConflicts()}
    if st in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        res["H"] = [[diag[j] if j == k else s.Value(h(j, k)) for k in range(n)] for j in range(n)]
    return res


def main(argv):
    args = argv[1:]
    if len(args) < 5:
        print(__doc__, file=sys.stderr)
        return 2
    out = args.pop(0)
    tlim, workers, lemma_d = None, None, False
    while args:
        o = args.pop(0)
        if o == "--time":
            tlim = float(args.pop(0))
        elif o == "--workers":
            workers = int(args.pop(0))
        elif o == "--lemma-d":
            lemma_d = True
        else:
            print(f"bad option {o}", file=sys.stderr)
            return 2
    os.makedirs(out)
    results = []
    for n0, n1, n2 in ((0, 6, 9), (1, 4, 10), (2, 2, 11), (3, 0, 12)):
        r = solve_split(n0, n1, n2, lemma_d, tlim, workers, os.path.join(out, f"split_{n0}_{n1}_{n2}.log"))
        if "H" in r:
            Hm = r["H"]
            n = len(Hm)
            r["check_H1_zero"] = all(sum(row) == 0 for row in Hm)
            r["check_H2_40H"] = all(sum(Hm[j][l] * Hm[l][k] for l in range(n)) == 40 * Hm[j][k]
                                    for j in range(n) for k in range(n))
            r["lemma_d_violations"] = sum(1 for j, k, l in itertools.combinations(range(n), 3)
                                          if not is_sq(det3(Hm[j][j], Hm[k][k], Hm[l][l], Hm[j][k], Hm[j][l], Hm[k][l])))
        results.append(r)
        print(json.dumps({k: v for k, v in r.items() if k != "H"}))
    rec = {"script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
           "ortools": __import__("ortools").__version__, "time_limit_s": tlim, "workers": workers,
           "lemma_d": lemma_d, "results": results}
    with open(os.path.join(out, "gram-crosscheck.json"), "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

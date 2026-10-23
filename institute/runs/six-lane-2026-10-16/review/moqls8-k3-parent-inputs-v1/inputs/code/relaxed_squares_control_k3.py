"""K3 analogue of relaxed_squares_control.py (README §4): production --squares path of enc8_a2.py / enc8_b2.py with
THREE quantum squares on the AG(2,8) pair (an extendable 2-MOLS(8) net; file names keep the label "nmax0000"
for the pair slot, but the squares are the AG pair recorded in the output).
 1. Find three Latin squares X, Y, Z (first row 0..7) completing the pair to 5 MOLS(8) (exact SAT).
 2. For each encoder: build the FK2 CNF through its CLI with --mode fixed --slopes "" --squares nmax00.json
    --quantum 12 --p4 none (the production --squares branch, only P4 relaxed).
    (i) solve: must be SAT; the returned model must satisfy EVERY clause (checked here independently);
    (ii) add unit clauses fixing all pattern variables S1, S2 to the explicit classical configuration
         S1(c) = {X(c)}, S2(c) = {Y(c)} (variables located through the encoder's own variable map); solve: must be SAT
         and the model must satisfy every clause (this shows the CNF accepts the explicit classical configuration).
Fail-closed (exit 1 on any failure). Fresh directory; nothing deleted.
python -B relaxed_squares_control_k3.py --nets UNUSED --outdir ../evidence/k3_fixed/relaxed_ctrl_v1
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
N = 8


def complete(sqs, t_new):
    var = lambda t, i, j, x: 1 + ((t * N + i) * N + j) * N + x
    cls = []
    cells = [(i, j) for i in range(N) for j in range(N)]
    for t in range(t_new):
        for i, j in cells:
            cls.append([var(t, i, j, x) for x in range(N)])
            for x, y in itertools.combinations(range(N), 2):
                cls.append([-var(t, i, j, x), -var(t, i, j, y)])
        for x in range(N):
            for i in range(N):
                for j1, j2 in itertools.combinations(range(N), 2):
                    cls.append([-var(t, i, j1, x), -var(t, i, j2, x)])
            for j in range(N):
                for i1, i2 in itertools.combinations(range(N), 2):
                    cls.append([-var(t, i1, j, x), -var(t, i2, j, x)])
        for j in range(N):
            cls.append([var(t, 0, j, j)])
        for L in sqs:
            for c1, c2 in itertools.combinations(cells, 2):
                if L[c1[0]][c1[1]] == L[c2[0]][c2[1]]:
                    for x in range(N):
                        cls.append([-var(t, c1[0], c1[1], x), -var(t, c2[0], c2[1], x)])
    for t1, t2 in itertools.combinations(range(t_new), 2):
        for c1, c2 in itertools.combinations(cells, 2):
            for x in range(N):
                for y in range(N):
                    cls.append([-var(t1, c1[0], c1[1], x), -var(t1, c2[0], c2[1], x),
                                -var(t2, c1[0], c1[1], y), -var(t2, c2[0], c2[1], y)])
    text = "p cnf %d %d\n" % (t_new * N ** 3, len(cls)) + "".join(" ".join(map(str, c)) + " 0\n" for c in cls)
    r = subprocess.run(["cadical", "-q", "-t", "1200"], input=text, capture_output=True, text=True)
    assert r.returncode == 10, r.returncode
    true = {int(t) for l in r.stdout.splitlines() if l.startswith("v ") for t in l.split()[1:] if int(t) > 0}
    new = [[[next(x for x in range(N) if var(t, i, j, x) in true) for j in range(N)] for i in range(N)]
           for t in range(t_new)]
    allsq = sqs + new
    assert all(len({(A[i][j], B[i][j]) for i in range(N) for j in range(N)}) == 64
               for A, B in itertools.combinations(allsq, 2))
    return new


def read_cnf(path):
    clauses = []
    with open(path) as fh:
        header = fh.readline().split()
        for line in fh:
            lits = [int(t) for t in line.split()]
            clauses.append(lits[:-1])
    return int(header[2]), clauses


def solve(solver, path):
    cmd = ["cadical", "-q", "-t", "1200", path] if solver == "cadical" else ["kissat", "-q", "--time=1200", path]
    r = subprocess.run(cmd, capture_output=True, text=True)
    model = {int(t) for l in r.stdout.splitlines() if l.startswith("v ") for t in l.split()[1:] if t != "0"}
    return r.returncode, model


def satisfied(clauses, model):
    return all(any(l in model for l in cl) for cl in clauses)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nets", required=True)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=False)
    # the AG(2,8) pair L_s(i,j) = j XOR s*i (s = 1, x) — an extendable 2-MOLS(8) net, so a classical completion exists
    from enc8_a2 import gmul
    pair = [[[j ^ gmul(sl, i) for j in range(N)] for i in range(N)] for sl in (1, 2)]
    sqp = os.path.join(a.outdir, "nmax0000.squares.json")
    with open(sqp, "x") as fh:
        json.dump(pair, fh)
    X, Y, Z = complete(pair, 3)
    res = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "enc8_a2_sha256": hashlib.sha256(open(os.path.join(HERE, "enc8_a2.py"), "rb").read()).hexdigest(),
           "enc8_b2_sha256": hashlib.sha256(open(os.path.join(HERE, "enc8_b2.py"), "rb").read()).hexdigest(),
           "completion": {"X": X, "Y": Y, "Z": Z}, "checks": []}
    ok = True
    for enc, solver in (("a", "cadical"), ("b", "kissat")):
        cnf = os.path.join(a.outdir, "%s_nmax0000_noP4.cnf" % enc)
        cmd = [sys.executable, "-B", os.path.join(HERE, "enc8_%s2.py" % enc), "--mode", "fixed", "--slopes", "",
               "--squares", sqp, "--quantum", "123", "--p4", "none", "--cnf", cnf]
        if enc == "a":
            cmd += ["--map", cnf + ".map.json"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        nv, clauses = read_cnf(cnf)
        rc, model = solve(solver, cnf)
        free_ok = rc == 10 and satisfied(clauses, model)
        # fix the explicit classical configuration through the encoder's variable map
        if enc == "a":
            vmap = {tuple(json.loads(k)[0:1]) + tuple(json.loads(k)[1]) + (json.loads(k)[2],): v
                    for k, v in json.load(open(cnf + ".map.json"))["vars"].items() if json.loads(k)[0] in ("S1", "S2", "S3")}
            key = lambda s, i, j, k: ("S%d" % s, i, j, k)
        else:
            tab = json.load(open(cnf + ".map.json"))
            vmap = {tuple(json.loads(k)): v for k, v in tab.items() if json.loads(k)[0] == "S"}
            key = lambda s, i, j, k: ("S", s, i, j, k)
        units = []
        for s, W in ((1, X), (2, Y), (3, Z)):
            for i in range(1, N):
                for j in range(N):
                    for k in range(N):
                        v = vmap[key(s, i, j, k)]
                        units.append([v] if W[i][j] == k else [-v])
        fixed = os.path.join(a.outdir, "%s_nmax0000_noP4_fixedclassical.cnf" % enc)
        with open(fixed, "x") as fh:
            fh.write("p cnf %d %d\n" % (nv, len(clauses) + len(units)))
            for cl in clauses + units:
                fh.write(" ".join(map(str, cl)) + " 0\n")
        rc2, model2 = solve(solver, fixed)
        fixed_ok = rc2 == 10 and satisfied(clauses + units, model2)
        rec = {"encoder": enc, "cnf_sha256": hashlib.sha256(open(cnf, "rb").read()).hexdigest(), "clauses": len(clauses),
               "free_exit": rc, "free_model_satisfies_all": free_ok, "fixed_units": len(units), "fixed_exit": rc2,
               "fixed_model_satisfies_all": fixed_ok}
        res["checks"].append(rec)
        ok &= free_ok and fixed_ok
        print(json.dumps(rec), flush=True)
    res["all_ok"] = ok
    with open(os.path.join(a.outdir, "RECEIPT.json"), "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({"all_ok": ok}))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

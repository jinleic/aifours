#!/usr/bin/env python3
"""dcomp_controls.py -- controls for code/dcomp_cnf.py (structure route, README 1.4(a)).  Stdlib + kissat + checkers.

1. Positive: for every published BTD fixture in controls/checkers-v1 (BTD(3,3;1,1,3;3,2), the doubled BTD(3,6;2,2,6;3,4),
   Francel-Hurd BTD(4,12;3,6,15;5,16), CPro1 BTD(12,16;4,4,12;9,8), BTD(14,21;6,3,12;8,6), BTD(16,22;9,1,11;8,5)) the
   CNF for its own 1-pattern must be SAT (kissat exit 10); the model's D gives M' = A + 2D, written in strict format,
   which both checkers (code/verify_btd.py --expect, bin/btd_check) must accept.
2. Intended-reason negative: the BTD(12,16;4,4,12;9,8) 1-pattern with one 1 of row 0 moved to a 0-cell: two column
   counts change parity, so the CNF must contain the empty clause and kissat must answer UNSAT (exit 20).
3. Counting: for BTD(3,3;1,1,3;3,2) (all 27 one-patterns with one 1 per row) and BTD(3,6;2,2,6;3,4) (60 one-patterns
   drawn with a fixed seed), the number of D-completions by brute force over all D (row sums p2, off A; check column
   sums and pair products directly) must equal the number of assignments of the d-variables that extend to a model of
   the CNF (unit propagation from a full d-assignment; every auxiliary is a two-sided definition, so propagation
   either conflicts or assigns everything, which is asserted).
Writes OUTDIR (fresh) with the CNFs, models, decoded matrices and controls.json.  Usage: dcomp_controls.py OUTDIR
"""
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
sys.path.insert(0, CODE)
import dcomp_cnf  # noqa: E402

FIX = os.path.join(LANE, "controls", "checkers-v1")
PUBLISHED = ["btd_3_3_1_1_3_3_2_rows_201_120_012", "btd_3_6_2_2_6_3_4_doubled_repeated_columns",
             "francel_hurd_fig2_btd_4_12_3_6_15_5_16", "cpro1_2501_fig20_btd_12_16_4_4_12_9_8",
             "cpro1_2501_fig19_btd_14_21_6_3_12_8_6", "cpro1_2505_fig4_btd_16_22_9_1_11_8_5"]


def read_btd(path):
    lines = open(path).read().split("\n")
    params = tuple(int(x) for x in lines[0].split()[1:])
    V, B = params[0], params[1]
    return params, [[int(t) for t in lines[1 + i].split(" ")] for i in range(V)]


def write_cnf(path, F):
    with open(path, "x") as f:
        f.write(f"p cnf {F.nv} {len(F.clauses)}\n")
        for c in F.clauses:
            f.write(" ".join(map(str, c)) + " 0\n")


def kissat(cnf):
    p = subprocess.run(["kissat", "--time=600", cnf], capture_output=True, text=True)
    vals = {}
    for line in p.stdout.splitlines():
        if line.startswith("v "):
            for t in line.split()[1:]:
                v = int(t)
                if v:
                    vals[abs(v)] = v > 0
    return p.returncode, vals, p.stdout


def up_model(clauses, nv, assign):
    """unit propagation from a partial assignment (dict var -> bool); returns (ok, full) where ok is False on conflict"""
    val = dict(assign)
    changed = True
    while changed:
        changed = False
        for c in clauses:
            unassigned, sat = [], False
            for lit in c:
                v = val.get(abs(lit))
                if v is None:
                    unassigned.append(lit)
                elif v == (lit > 0):
                    sat = True
                    break
            if sat:
                continue
            if not unassigned:
                return False, val
            if len(unassigned) == 1:
                lit = unassigned[0]
                val[abs(lit)] = lit > 0
                changed = True
    return True, val


def cnf_count(params, A_rows):
    F, d = dcomp_cnf.build(params, A_rows)
    dv = [d[i][j] for i in range(len(d)) for j in range(len(d[0])) if d[i][j] is not None]
    n = 0
    for bits in itertools.product((False, True), repeat=len(dv)):
        ok, val = up_model(F.clauses, F.nv, dict(zip(dv, bits)))
        if ok:
            assert len(val) == F.nv, "propagation left an auxiliary unassigned"
            n += 1
    return n


def brute_count(params, A_rows):
    V, B, p1, p2, R, K, L = params
    A = [set(r) for r in A_rows]
    choices = [list(itertools.combinations([j for j in range(B) if j not in A[i]], p2)) for i in range(V)]
    n = 0
    for Ds in itertools.product(*choices):
        M = [[(1 if j in A[i] else 0) + (2 if j in Ds[i] else 0) for j in range(B)] for i in range(V)]
        if any(sum(M[i][j] for i in range(V)) != K for j in range(B)):
            continue
        if any(sum(M[i][j] * M[k][j] for j in range(B)) != L for i in range(V) for k in range(i + 1, V)):
            continue
        n += 1
    return n


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)
    res, ok_all = [], True
    for name in PUBLISHED:
        params, M = read_btd(os.path.join(FIX, name + ".btd"))
        V, B = params[0], params[1]
        A_rows = [[j for j in range(B) if M[i][j] == 1] for i in range(V)]
        F, d = dcomp_cnf.build(params, A_rows)
        cnf = os.path.join(out, f"pos_{name}.cnf")
        write_cnf(cnf, F)
        rc, vals, _ = kissat(cnf)
        rec = {"control": f"positive {name}", "params": list(params), "kissat_rc": rc}
        good = rc == 10
        if good:
            Mp = [[(1 if j in A_rows[i] else 0) + (2 if (d[i][j] is not None and vals.get(d[i][j], False)) else 0)
                   for j in range(B)] for i in range(V)]
            txt = "BTD " + " ".join(map(str, params)) + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in Mp)
            mpath = os.path.join(out, f"pos_{name}.decoded.btd")
            with open(mpath, "x", newline="") as f:
                f.write(txt)
            py = subprocess.run([sys.executable, "-B", os.path.join(CODE, "verify_btd.py"), mpath, "--expect",
                                 *map(str, params)], capture_output=True, text=True)
            nc = subprocess.run([os.path.join(LANE, "bin", "btd_check"), mpath, *map(str, params)],
                                capture_output=True, text=True)
            vpy = py.stdout.strip().split("\n")[-1] if py.stdout.strip() else ""
            vc = nc.stdout.strip()
            rec.update({"decoded_sha256": hashlib.sha256(txt.encode()).hexdigest(),
                        "same_as_published": Mp == M, "verify_btd": vpy[:120], "verify_rc": py.returncode,
                        "btd_check": vc[:120], "btd_check_rc": nc.returncode})
            good = py.returncode == 0 and vpy.startswith("VALID") and nc.returncode == 0 and vc.startswith("VALID")
        rec["as_intended"] = good
        ok_all &= good
        res.append(rec)
        print(("ok " if good else "BAD"), rec["control"], rc)
    # 2. intended-reason negative
    params, M = read_btd(os.path.join(FIX, "cpro1_2501_fig20_btd_12_16_4_4_12_9_8.btd"))
    V, B = params[0], params[1]
    A_rows = [[j for j in range(B) if M[i][j] == 1] for i in range(V)]
    j1 = A_rows[0][0]
    j0 = next(j for j in range(B) if M[0][j] == 0)
    A_rows[0] = sorted([j for j in A_rows[0] if j != j1] + [j0])
    F, d = dcomp_cnf.build(params, A_rows)
    cnf = os.path.join(out, "neg_move_one_in_row0_btd12_16.cnf")
    write_cnf(cnf, F)
    rc, _, _ = kissat(cnf)
    has_empty = any(len(c) == 0 for c in F.clauses)
    good = rc == 20 and has_empty
    ok_all &= good
    res.append({"control": "negative: moved one 1 in row 0 of BTD(12,16) (column parity)", "kissat_rc": rc,
                "empty_clause": has_empty, "as_intended": good})
    print(("ok " if good else "BAD"), "negative column parity", rc, has_empty)
    # 3. counting
    rng = random.Random(20261017)
    for params, A_list in (
            ((3, 3, 1, 1, 3, 3, 2), [[[a], [b], [c]] for a in range(3) for b in range(3) for c in range(3)]),
            ((3, 6, 2, 2, 6, 3, 4), [[sorted(rng.sample(range(6), 2)) for _ in range(3)] for _ in range(60)])):
        tot_b = tot_c = mism = 0
        for A_rows in A_list:
            nb, nc = brute_count(params, A_rows), cnf_count(params, A_rows)
            tot_b += nb
            tot_c += nc
            mism += nb != nc
        good = mism == 0 and tot_b > 0
        ok_all &= good
        res.append({"control": f"counting {params}", "patterns": len(A_list), "brute_total": tot_b,
                    "cnf_total": tot_c, "mismatches": mism, "as_intended": good})
        print(("ok " if good else "BAD"), "counting", params, tot_b, tot_c, mism)
    with open(os.path.join(out, "controls.json"), "x") as f:
        json.dump({"dcomp_cnf_sha256": hashlib.sha256(open(dcomp_cnf.__file__, "rb").read()).hexdigest(),
                   "controls_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "results": res, "all_as_intended": ok_all}, f, indent=1)
    print("DCOMP-CONTROLS", "PASS" if ok_all else "FAIL")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

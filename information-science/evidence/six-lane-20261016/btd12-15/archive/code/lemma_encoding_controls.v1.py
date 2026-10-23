#!/usr/bin/env python3
"""lemma_encoding_controls.py -- controls for the implied-constraint clauses of encoding A (--lemmas 2|3,
README amendment 1.8), using its --lemma-test mode (D2-D4 and symmetry omitted; b -> a, (C1) and lemma clauses kept).

For a 12 x 15 matrix X over {0,1,2} with at most two 2s per column, all auxiliary variables of the lemma part are
functionally defined by X, so "CNF + units fixing X" is SAT iff X satisfies the encoded conditions.  This script
compares that with an independent direct evaluation (reference) of the same conditions:
  d_j: column j has two 2s; o_j: exactly one 2; g_jk = sum_i X_ij X_ik; G_jk(c) = [g_jk >= c] for c <= 7;
  (C3) d_j & d_k -> 4 <= g_jk <= 5;  (C4) d_j & o_k -> g_jk >= 4;
  (Step 4) d_j -> all k != j: 3 <= g_jk <= 6 and (#g=3, #g=4, #g=6) in {(0,4,2), (1,1,1)};
  (Step 5) d_j & d_k & g_jk <= 4 -> min(g_jl,7) = min(g_kl,7) for all other l  (as encoded: G thresholds 1..7);
  level 3 adds: no three type-2 columns with pairwise g_jk >= 5.
Test matrices: planted single-type-2-column configurations (both distributions), their mutations, configurations
found by a seeded local search that satisfy the level-2 reference with 2 and 3 type-2 columns (when found), and
seeded random matrices.  Solver: cadical, 60 s native limit.  OUTDIR fresh; nothing deleted or overwritten.
Usage: lemma_encoding_controls.py OUTDIR
"""
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
V, B = 12, 15


def ref_ok(X, level):
    two = [sum(1 for i in range(V) if X[i][j] == 2) for j in range(B)]
    assert all(t <= 2 for t in two)
    d = [t == 2 for t in two]
    o = [t == 1 for t in two]
    g = [[sum(X[i][j] * X[i][k] for i in range(V)) for k in range(B)] for j in range(B)]
    for j, k in itertools.combinations(range(B), 2):
        if d[j] and d[k] and not 4 <= g[j][k] <= 5:
            return False
    for j in range(B):
        for k in range(B):
            if j != k and d[j] and o[k] and g[j][k] < 4:
                return False
    for j in range(B):
        if not d[j]:
            continue
        others = [g[j][k] for k in range(B) if k != j]
        if any(not 3 <= x <= 6 for x in others):
            return False
        cnt = (others.count(3), others.count(4), others.count(6))
        if cnt not in ((0, 4, 2), (1, 1, 1)):
            return False
    for j, k in itertools.combinations(range(B), 2):
        if d[j] and d[k] and g[j][k] <= 4:
            for l in range(B):
                if l not in (j, k) and min(g[j][l], 7) != min(g[k][l], 7):
                    return False
    if level >= 3:
        for j, k, l in itertools.combinations(range(B), 3):
            if d[j] and d[k] and d[l] and g[j][k] >= 5 and g[j][l] >= 5 and g[k][l] >= 5:
                return False
    return True


def violations(X):
    # smooth objective for the local search (level-2 conditions), only meaningful when some column has two 2s
    two = [sum(1 for i in range(V) if X[i][j] == 2) for j in range(B)]
    d = [t == 2 for t in two]
    g = [[sum(X[i][j] * X[i][k] for i in range(V)) for k in range(B)] for j in range(B)]
    v = 0
    for j in range(B):
        if not d[j]:
            continue
        others = [g[j][k] for k in range(B) if k != j]
        v += sum(max(0, 3 - x) + max(0, x - 6) for x in others)
        c3, c4, c6 = others.count(3), others.count(4), others.count(6)
        v += min(abs(c3) + abs(c4 - 4) + abs(c6 - 2), abs(c3 - 1) + abs(c4 - 1) + abs(c6 - 1))
        for k in range(B):
            if k != j and d[k]:
                v += max(0, 4 - g[j][k]) + max(0, g[j][k] - 5)
    return v


def search(ntype2, rng, steps=40000):
    X = [[0] * B for _ in range(V)]
    cols2 = rng.sample(range(B), ntype2)
    for j in range(B):
        rows = rng.sample(range(V), 6)
        for i in rows[:4]:
            X[i][j] = 1
        if j in cols2:
            for i in rows[4:6]:
                X[i][j] = 2
    best = violations(X)
    for _ in range(steps):
        if best == 0 and ref_ok(X, 2):
            return X
        i, j = rng.randrange(V), rng.randrange(B)
        old = X[i][j]
        new = rng.choice([v for v in (0, 1) if v != old] or [0]) if old != 2 else 2
        if old == 2:
            continue  # keep the planted 2s (the number of type-2 columns stays fixed)
        X[i][j] = new
        v = violations(X)
        if v <= best or rng.random() < 0.02:
            best = v
        else:
            X[i][j] = old
    return X if ref_ok(X, 2) else None


def cert(X):
    return "BTD 12 15 6 2 10 8 6\n" + "".join(" ".join(map(str, r)) + "\n" for r in X)


def run_case(out, name, X, level):
    path = os.path.join(out, name + ".btd")
    with open(path, "x") as f:
        f.write(cert(X))
    cnf = os.path.join(out, f"{name}.L{level}.cnf")
    p = subprocess.run([sys.executable, os.path.join(CODE, "btd_cnf_a.py"), "12", "15", "6", "2", "10", "8", "6", cnf,
                        "--lemmas", str(level), "--lemma-test", "--fix", path], capture_output=True, text=True)
    assert p.returncode == 0, p.stderr
    s = subprocess.run(["/opt/homebrew/bin/cadical", "-t", "60", "-q", cnf], capture_output=True, text=True)
    status = "SAT" if "s SATISFIABLE" in s.stdout else ("UNSAT" if "s UNSATISFIABLE" in s.stdout else "UNKNOWN")
    return status


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)
    rng = random.Random(1017)
    cases = []
    Z = [[0] * B for _ in range(V)]
    cases.append(("all_zero", Z))
    # planted: column 0 = (2,2,1,1,1,1,0,...); other columns 0/1 with g realised by row choices
    base = [[0] * B for _ in range(V)]
    for i, v in enumerate([2, 2, 1, 1, 1, 1]):
        base[i][0] = v
    pattern = {3: [0, 2], 4: [0, 1], 5: [0, 1, 2], 6: [0, 1, 2, 3]}

    def planted(gvals):
        X = [list(r) for r in base]
        for k, gv in enumerate(gvals, start=1):
            for i in pattern[gv]:
                X[i][k] = 1
            X[11][k] = 1  # an extra 1 outside column 0's support: g unchanged
        return X
    dist_a = [4, 4, 4, 4, 6, 6] + [5] * 8
    dist_b = [3, 4, 6] + [5] * 11
    cases.append(("planted_dist_042", planted(dist_a)))
    cases.append(("planted_dist_111", planted(dist_b)))
    cases.append(("planted_bad_143", planted([3] + dist_a[1:])))
    cases.append(("planted_bad_c6_is_3", planted([4, 4, 4, 4, 6, 6, 5, 5, 5, 5, 5, 5, 5, 6])))
    for t in (2, 3):
        for attempt in range(6):
            X = search(t, rng)
            if X is not None:
                cases.append((f"search_{t}type2_{attempt}", X))
    for r in range(12):
        X = [[0] * B for _ in range(V)]
        for j in range(B):
            n2 = rng.choice([0, 1, 2, 2])
            rows = rng.sample(range(V), 6)
            for i in rows[:4]:
                X[i][j] = 1
            for i in rows[4:4 + n2]:
                X[i][j] = 2
        cases.append((f"random_{r}", X))
    results, ok = [], True
    for name, X in cases:
        for level in (2, 3):
            want = "SAT" if ref_ok(X, level) else "UNSAT"
            got = run_case(out, f"{name}", X, level) if level == 2 else run_case(out, f"{name}_l3", X, level)
            good = want == got
            ok &= good
            results.append({"case": name, "level": level, "reference": want, "cnf": got, "agree": good})
            print(f"{'ok ' if good else 'BAD'} {name} L{level}: reference {want}, cnf {got}")
    summary = {lv: {"SAT": sum(1 for r in results if r["level"] == lv and r["reference"] == "SAT"),
                    "UNSAT": sum(1 for r in results if r["level"] == lv and r["reference"] == "UNSAT")} for lv in (2, 3)}
    with open(os.path.join(out, "lemma-controls.json"), "x") as f:
        json.dump({"script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "generator_sha256": hashlib.sha256(open(os.path.join(CODE, "btd_cnf_a.py"), "rb").read()).hexdigest(),
                   "reference_counts": summary, "results": results, "all_agree": ok}, f, indent=1)
        f.write("\n")
    print("reference counts", summary)
    print("LEMMA-CONTROLS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

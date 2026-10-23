"""Controls for the K2 pattern encoders (README §2).

Direct pattern checker (independent of the CNF encoders) + positive/mutation controls built from the exact
Corollary-7 square of order 7 (Example 15, H = {1,2,4}), whose row-0-frame support pattern is computed exactly with
the seventh-root criterion (a sum of 7 seventh roots of unity vanishes iff the exponents are a permutation of Z_7).

python -B k2_controls.py --encoder k2_encode_a.py --solver cadical --out ../evidence/k2/controls_a.json
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import os
import subprocess

N = 7
H = {1, 2, 4}


def is_perm(seq):
    return sorted(s % N for s in seq) == list(range(N))


def cor7():
    f = [x if x in H else 0 for x in range(N)]
    M = [m for m in range(N) if is_perm([f[x] - m * x for x in range(N)])]
    m0 = M[0]
    f0 = [(f[x] - m0 * x) % N for x in range(N)]
    slope = (M[1] - m0) % N
    pat = [[[j] if i == 0 else [y for y in range(N) if not is_perm([i * f0[x] + (j - y) * x for x in range(N)])]
            for j in range(N)] for i in range(N)]
    return M, f0, slope, pat


def classical(slope):
    return [[(j + slope * i) % N for j in range(N)] for i in range(N)]


def singletons(sq):
    return [[[sq[i][j]] for j in range(N)] for i in range(N)]


def lines_of(squares):
    L = [[(i, j) for j in range(N)] for i in range(N)] + [[(i, j) for i in range(N)] for j in range(N)]
    for sq in squares:
        for x in range(N):
            L.append([(i, j) for i in range(N) for j in range(N) if sq[i][j] == x])
    return L


def subsquare_latin():
    """Latin square of order 7, first row 0..6, with the 3x3 subsquare L[1+u][v] = 3 + (u+v) mod 3 (DFS)."""
    L = [[None] * N for _ in range(N)]
    L[0] = list(range(N))
    for u in range(3):
        for v in range(3):
            L[1 + u][v] = 3 + (u + v) % 3
    free = [(i, j) for i in range(1, N) for j in range(N) if L[i][j] is None]

    def ok(i, j, x):
        return all(L[i][k] != x for k in range(N)) and all(L[k][j] != x for k in range(N))

    def dfs(t):
        if t == len(free):
            return True
        i, j = free[t]
        for x in range(N):
            if ok(i, j, x):
                L[i][j] = x
                if dfs(t + 1):
                    return True
                L[i][j] = None
        return False
    assert dfs(0)
    return L


def check(squares, pats, need_w3=()):
    """direct evaluation of (P1)-(P4); returns list of violation strings (empty = pattern passes)."""
    bad = []
    cells = [(i, j) for i in range(N) for j in range(N)]
    for s, P in pats.items():
        for (i, j) in cells:
            S = set(P[i][j])
            if i == 0:
                if S != {j}:
                    bad.append("P1 row0 %s %s" % (s, (i, j)))
                continue
            if not S:
                bad.append("P1 empty %s %s" % (s, (i, j)))
            if j in S or any(sq[i][j] in S for sq in squares):
                bad.append("P1 forbidden %s %s" % (s, (i, j)))
        for line in lines_of(squares):
            sup = [set(P[i][j]) for (i, j) in line]
            if set().union(*sup) != set(range(N)):
                bad.append("P2a %s %s" % (s, line[:2]))
            for a, b in itertools.combinations(range(N), 2):
                if len(sup[a] & sup[b]) == 1:
                    bad.append("P2b %s %s %s" % (s, line[a], line[b]))
            for k1, k2 in itertools.combinations(range(N), 2):
                if sum(1 for S in sup if k1 in S and k2 in S) == 1:
                    bad.append("P2c %s %s %s" % (s, line[:2], (k1, k2)))
    labels = sorted(pats)
    for s1, s2 in itertools.combinations(labels, 2):
        for (i, j) in cells:
            if i and set(pats[s1][i][j]) & set(pats[s2][i][j]):
                bad.append("P1 overlap %s" % ((i, j),))
        for c1, c2 in itertools.combinations(cells, 2):
            a = len(set(pats[s1][c1[0]][c1[1]]) & set(pats[s1][c2[0]][c2[1]])) == 1
            b = len(set(pats[s2][c1[0]][c1[1]]) & set(pats[s2][c2[0]][c2[1]])) == 1
            if a and b:
                bad.append("P3 %s %s" % (c1, c2))
    for s in need_w3:
        if not any(len(pats[s][i][j]) >= 3 for i in range(1, N) for j in range(N)):
            bad.append("P4 %s" % s)
    return bad


def run_encoder(enc, solver, tag, outdir, slopes, quantum, fixpat, p4, p3=True):
    fp = os.path.join(outdir, tag + ".fix.json")
    json.dump({str(k): v for k, v in fixpat.items()}, open(fp, "w"))
    cnf = os.path.join(outdir, tag + ".cnf")
    args = ["--mode", "fixed", "--slopes", ",".join(map(str, slopes)), "--quantum", "".join(map(str, quantum)),
            "--fixpat", fp, "--p4", "".join(map(str, p4)) or "none", "--cnf", cnf, "--map", cnf + ".map.json"]
    if not p3:
        args.append("--no-p3")
    import sys
    subprocess.run([sys.executable, "-B", enc] + args, check=True, capture_output=True)
    r = subprocess.run([solver, cnf] if solver == "kissat" else [solver, "-q", cnf], capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(r.returncode, "ERR%d" % r.returncode)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--encoder", required=True)
    ap.add_argument("--solver", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    outdir = os.path.join(os.path.dirname(a.out), "controls_" + os.path.basename(a.encoder).split(".")[0])
    os.makedirs(outdir, exist_ok=True)
    M, f0, sl, pat = cor7()
    weights = sorted({len(pat[i][j]) for i in range(1, N) for j in range(N)})
    res = {"cor7_M": M, "cor7_f0": f0, "cor7_slope": sl, "cor7_weights": weights, "controls": []}

    def ctrl(tag, slopes, pats, p4, expect_direct, p3=True):
        direct = check([classical(s) for s in slopes], pats, p4 if p4 else ())
        if not p3:
            direct = [d for d in direct if not d.startswith("P3")]
        enc = run_encoder(a.encoder, a.solver, tag, outdir, slopes, sorted(pats), pats, p4, p3)
        rec = {"tag": tag, "direct_pass": not direct, "direct_first": direct[:3], "encoder": enc,
               "agree": (enc == "SAT") == (not direct), "expected_direct_pass": expect_direct}
        res["controls"].append(rec)
        print(json.dumps(rec), flush=True)

    ctrl("C1_cor7_3net_positive", [sl], {1: pat}, (1,), True)
    ctrl("C2_cor7_plus_classical_as_quantum", [], {1: pat, 2: singletons(classical(sl))}, (1,), True)
    cell = next((i, j) for i in range(1, N) for j in range(N) if len(pat[i][j]) >= 3)
    mut = [[list(x) for x in row] for row in pat]
    mut[cell[0]][cell[1]] = mut[cell[0]][cell[1]][:-1]
    ctrl("C4_cor7_drop_one_coordinate", [sl], {1: mut}, (1,), None)
    # real QLS with a 3x3 Fourier-rotated Latin subsquare (rows 1-3, cols 0-2, symbols 3-5): weight-3 entries
    L = subsquare_latin()
    w3 = [[[L[i][j]] for j in range(N)] for i in range(N)]
    for i in (1, 2, 3):
        for j in (0, 1, 2):
            w3[i][j] = [3, 4, 5]
    res["subsquare_latin"] = L
    ctrl("C5_weight3_subsquare_qls_positive", [], {1: w3}, (1,), True)
    bad3 = [[list(x) for x in row] for row in w3]
    bad3[2][1] = [3]
    ctrl("C6_weight3_subsquare_mutated_singleton", [], {1: bad3}, (), False)
    # P3: Psi1 = singletons of j+i, Psi2 = singletons of j+sigma(i): orthogonal iff sigma(i)-i is a permutation
    sig_bad = [0, 2, 1, 4, 3, 6, 5]
    sig_ok = [(2 * i) % N for i in range(N)]
    shift = lambda sg: [[[(j + sg[i]) % N] for j in range(N)] for i in range(N)]
    ctrl("C7_P3_orthogonal_pair_positive", [], {1: shift(list(range(N))), 2: shift(sig_ok)}, (), True)
    ctrl("C8_P3_nonorthogonal_pair_mutation", [], {1: shift(list(range(N))), 2: shift(sig_bad)}, (), False)
    # P2 on classical lines: singletons of j+sigma(i) against the classical slope-1 square
    ctrl("C9_P2_classical_line_mutation", [1], {1: shift([0, 3, 1, 4, 6, 2, 5])}, (), None)
    ctrl("C10_P2_classical_line_positive", [1], {1: shift(sig_ok)}, (), True)
    ctrl("C11_classical_pair_no_w3", [1, 2], {1: singletons(classical(3)), 2: singletons(classical(4))}, (), True)
    ctrl("C12_classical_pair_needs_w3", [1, 2], {1: singletons(classical(3)), 2: singletons(classical(4))}, (1,),
         False)
    res["all_agree"] = all(r["agree"] for r in res["controls"])
    res["expected_ok"] = all(r["expected_direct_pass"] is None or r["expected_direct_pass"] == r["direct_pass"]
                             for r in res["controls"])
    res["script_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    res["encoder_sha256"] = hashlib.sha256(open(a.encoder, "rb").read()).hexdigest()
    json.dump(res, open(a.out, "w"), indent=1)
    print(json.dumps({k: res[k] for k in ("cor7_M", "cor7_slope", "cor7_weights", "all_agree", "expected_ok")}))


if __name__ == "__main__":
    main()

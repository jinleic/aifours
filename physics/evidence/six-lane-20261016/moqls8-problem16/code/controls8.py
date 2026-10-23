"""Fail-closed controls for the order-8 pattern encoders (enc8_a.py / enc8_b.py), README §0.

Direct pattern checker (independent of the CNF encoders) + positive/mutation controls built from the exact
Ball–Simoens Theorem-6 square Psi^(f) over GF(8) (chi = (-1)^Tr), whose row-0-frame support pattern is computed
exactly (+-1 vectors, integer inner products), a genuine QLS(8) with a Fourier-rotated 3x3 Latin subsquare (weight 3),
XOR-shift pairs (P3), classical-line P2, classical pairs with/without (P4). Each encoder verdict must equal the exact
expected status (SAT iff the direct predicate passes); solver errors/timeouts fail.

python -B controls8.py --encoder enc8_a.py --solver cadical --out ../evidence/controls/controls8_a.json
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import os
import subprocess
import sys

N = 8


def gmul(a, b):
    r = 0
    for k in range(3):
        if (b >> k) & 1:
            r ^= a << k
    for d in (4, 3):
        if (r >> d) & 1:
            r ^= 0b1011 << (d - 3)
    return r


def trace(x):
    t = x ^ gmul(x, x) ^ gmul(gmul(x, x), gmul(x, x))
    assert t in (0, 1)
    return t


def is_perm(seq):
    return sorted(s % N for s in seq) == list(range(N))


def gf2_affine(f):
    c = f[0]
    return all(f[x ^ y] ^ c == (f[x] ^ c) ^ (f[y] ^ c) for x in range(N) for y in range(N))


def thm6():
    """Ball–Simoens Theorem 6 pair over the Frobenius ring Z2 x Z4 (code e = 4a + b; chi(a,b) = (-1)^a i^b; unit
    u = (1,1)); first non-additive permutation f, f(0) = 0, with f - u x a permutation (same search as exact8_a.py).
    Returns (f, u, row-0-frame support pattern of Psi^(f), singleton pattern of Phi^(u) = |u i + j>)."""
    dec = lambda e: (e >> 2, e & 3)
    enc = lambda a_, b_: ((a_ % 2) << 2) | (b_ % 4)
    add = lambda x, y: enc(dec(x)[0] + dec(y)[0], dec(x)[1] + dec(y)[1])
    mul = lambda x, y: enc(dec(x)[0] * dec(y)[0], dec(x)[1] * dec(y)[1])
    neg = lambda x: enc(-dec(x)[0], -dec(x)[1])

    def chi(x):
        a_, b_ = dec(x)
        re, im = [(1, 0), (0, 1), (-1, 0), (0, -1)][b_]
        return (-re, -im) if a_ else (re, im)
    u = enc(1, 1)
    for perm in itertools.permutations(range(1, N)):
        f = [0] + list(perm)
        if all(f[add(x, y)] == add(f[x], f[y]) for x in range(N) for y in range(N)):
            continue
        if is_perm([add(f[x], neg(mul(u, x))) for x in range(N)]):
            break
    vec = {(i, j): [chi(add(mul(i, f[x]), mul(j, x))) for x in range(N)] for i in range(N) for j in range(N)}

    def nz(v, w):
        re = sum(p[0] * q[0] + p[1] * q[1] for p, q in zip(v, w))
        im = sum(p[0] * q[1] - p[1] * q[0] for p, q in zip(v, w))
        return (re, im) != (0, 0)
    pat = [[[j] if i == 0 else [y for y in range(N) if nz(vec[(0, y)], vec[(i, j)])] for j in range(N)]
           for i in range(N)]
    phi = [[[add(mul(u, i), j)] for j in range(N)] for i in range(N)]
    return f, u, pat, phi


def classical(slope):
    return [[j ^ gmul(slope, i) for j in range(N)] for i in range(N)]


def singletons(sq):
    return [[[sq[i][j]] for j in range(N)] for i in range(N)]


def lines_of(squares):
    L = [[(i, j) for j in range(N)] for i in range(N)] + [[(i, j) for i in range(N)] for j in range(N)]
    for sq in squares:
        for x in range(N):
            L.append([(i, j) for i in range(N) for j in range(N) if sq[i][j] == x])
    return L


def subsquare_latin():
    """Latin square of order 8, first row 0..7, with the 3x3 subsquare L[1+u][v] = 3 + (u+v) mod 3 (DFS)."""
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
    """returns (status, record) where status is SAT/UNSAT/ERR...; every subprocess is recorded."""
    import sys
    fp = os.path.join(outdir, tag + ".fix.json")
    json.dump({str(k): v for k, v in fixpat.items()}, open(fp, "w"))
    cnf = os.path.join(outdir, tag + ".cnf")
    args = ["--mode", "fixed", "--slopes", ",".join(map(str, slopes)), "--quantum", "".join(map(str, quantum)),
            "--fixpat", fp, "--p4", "".join(map(str, p4)) or "none", "--cnf", cnf, "--map", cnf + ".map.json"]
    if not p3:
        args.append("--no-p3")
    e = subprocess.run([sys.executable, "-B", enc] + args, capture_output=True, text=True)
    rec = {"encoder_argv": [sys.executable, "-B", enc] + args, "encoder_exit": e.returncode,
           "encoder_stderr": e.stderr[-2000:]}
    if e.returncode != 0:
        return "ERR_ENCODER%d" % e.returncode, rec
    rec["cnf_sha256"] = hashlib.sha256(open(cnf, "rb").read()).hexdigest()
    cmd = [solver, cnf] if solver == "kissat" else [solver, "-q", cnf]
    r = subprocess.run(cmd, capture_output=True, text=True)
    rec.update({"solver_argv": cmd, "solver_exit": r.returncode,
                "solver_status_line": next((l for l in r.stdout.splitlines() if l.startswith("s ")), None)})
    return {10: "SAT", 20: "UNSAT"}.get(r.returncode, "ERR%d" % r.returncode), rec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--encoder", required=True)
    ap.add_argument("--solver", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    # fresh per-run directory derived from the output path (never reuses an earlier control directory)
    outdir = os.path.splitext(a.out)[0] + "_files"
    os.makedirs(outdir, exist_ok=False)
    f6, u6, pat, phi6 = thm6()
    weights = sorted({len(pat[i][j]) for i in range(1, N) for j in range(N)})
    res = {"thm6_ring": "Z2xZ4", "thm6_f": f6, "thm6_u": u6, "thm6_weights": weights, "controls": []}

    def ctrl(tag, slopes, pats, p4, expect_direct, p3=True):
        direct = check([classical(s) for s in slopes], pats, p4 if p4 else ())
        if not p3:
            direct = [d for d in direct if not d.startswith("P3")]
        expected_status = "SAT" if not direct else "UNSAT"
        enc, sub = run_encoder(a.encoder, a.solver, tag, outdir, slopes, sorted(pats), pats, p4, p3)
        rec = {"tag": tag, "direct_pass": not direct, "direct_first": direct[:3], "expected_status": expected_status,
               "encoder_status": enc, "agree": enc == expected_status, "expected_direct_pass": expect_direct,
               **sub}
        res["controls"].append(rec)
        print(json.dumps({k: rec[k] for k in ("tag", "direct_pass", "expected_status", "encoder_status", "agree")}),
              flush=True)

    ctrl("C2_thm6_pair_as_two_patterns_positive", [], {1: pat, 2: phi6}, (1,), True)
    cell = next((i, j) for i in range(1, N) for j in range(N) if len(pat[i][j]) >= 3)
    mut = [[list(x) for x in row] for row in pat]
    mut[cell[0]][cell[1]] = mut[cell[0]][cell[1]][:-1]
    ctrl("C4_thm6_drop_one_coordinate", [], {1: mut, 2: phi6}, (1,), None)
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
    sig_bad = [0, 2, 1, 4, 3, 6, 7, 5]          # i ^ sigma(i) not injective (1^2 = 2^1 = 3)
    sig_ok = [gmul(2, i) for i in range(N)]      # i ^ 2i = 3i is a permutation
    shift = lambda sg: [[[j ^ sg[i]] for j in range(N)] for i in range(N)]
    ctrl("C7_P3_orthogonal_pair_positive", [], {1: shift(list(range(N))), 2: shift(sig_ok)}, (), True)
    ctrl("C8_P3_nonorthogonal_pair_mutation", [], {1: shift(list(range(N))), 2: shift(sig_bad)}, (), False)
    # P2 on classical lines: singletons of j+sigma(i) against the classical slope-1 square
    ctrl("C9_P2_classical_line_mutation", [1], {1: shift(sig_bad)}, (), None)
    ctrl("C10_P2_classical_line_positive", [1], {1: shift(sig_ok)}, (), True)
    ctrl("C11_classical_pair_no_w3", [1, 2], {1: singletons(classical(3)), 2: singletons(classical(4))}, (), True)
    ctrl("C12_classical_pair_needs_w3", [1, 2], {1: singletons(classical(3)), 2: singletons(classical(4))}, (1,),
         False)
    res["all_agree"] = all(r["agree"] for r in res["controls"])
    res["expected_ok"] = all(r["expected_direct_pass"] is None or r["expected_direct_pass"] == r["direct_pass"]
                             for r in res["controls"])
    res["argv"] = sys.argv
    res["python"] = sys.version
    res["script_sha256"] = hashlib.sha256(open(__file__, "rb").read()).hexdigest()
    res["encoder_sha256"] = hashlib.sha256(open(a.encoder, "rb").read()).hexdigest()
    json.dump(res, open(a.out, "x"), indent=1)
    print(json.dumps({k: res[k] for k in ("thm6_f", "thm6_u", "thm6_weights", "all_agree", "expected_ok")}))
    if not (res["all_agree"] and res["expected_ok"]):
        sys.exit("CONTROL FAILURE: disagreement or unexpected direct verdict")


if __name__ == "__main__":
    main()

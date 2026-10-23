#!/usr/bin/env python3
"""gram_controls.py: controls for gram_enc.py with exact Gram supports. Lane moqls7-maximum.
  GC1 classical triple L_a(i,j) = a i + j (a = 1,2,3): g_a(p,q) = [L_a(p) = L_a(q)]; nsq=3, no heavy: SAT expected.
  GC2 genuine non-classical pair (Psi(f), Phi(m)) (Ball-Simoens Example 15, q = 7, H = {1,2,4}, f shifted by m0):
      g_1(p,q) = [x -> (k-i) f(x) + (l-j) x is NOT a permutation] (exact: 7 seventh roots of unity),
      g_2 = same symbol of Phi(m); nsq=2, no heavy: SAT expected.
  GC3 Psi(f) alone on the fixed 3-net (rows, columns, Phi(m)) with --heavy: reports SAT/UNSAT (records whether the
      genuine square is heavy in every line frame).
  GC4 single-bit mutations of GC2's g_1 at 40 deterministic positions: report how many are rejected (UNSAT).
Usage: python gram_controls.py OUT.json
"""
import itertools
import json
import subprocess
import sys

import gram_enc

P = 7
CELLS = gram_enc.CELLS


def solve(F):
    p = subprocess.run(["cadical", "-q"], input=F.text(), capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(p.returncode, "rc%d" % p.returncode)


def psi_f_data():
    H = {1, 2, 4}
    f0 = [x if x in H else 0 for x in range(P)]
    is_perm = lambda g: len({g(x) % P for x in range(P)}) == P
    M0 = [m for m in range(P) if is_perm(lambda x: f0[x] - m * x)]
    m0 = M0[0]
    f = [(f0[x] - m0 * x) % P for x in range(P)]
    m = [(mm - m0) % P for mm in M0 if mm != m0][0]
    g1 = []
    for p, q in itertools.combinations(CELLS, 2):
        (i, j), (k, l) = p, q
        if not is_perm(lambda x: (k - i) * f[x] + (l - j) * x):
            g1.append([list(p), list(q)])
    Lm = [[(m * i + j) % P for j in range(P)] for i in range(P)]
    g2 = [[list(p), list(q)] for p, q in itertools.combinations(CELLS, 2) if Lm[p[0]][p[1]] == Lm[q[0]][q[1]]]
    return m0, m, f, g1, g2, Lm


def main(out):
    res = {}
    fix = {}
    for a in (1, 2, 3):
        La = [[(a * i + j) % P for j in range(P)] for i in range(P)]
        fix["g%d" % a] = [[list(p), list(q)] for p, q in itertools.combinations(CELLS, 2)
                          if La[p[0]][p[1]] == La[q[0]][q[1]]]
    F, _ = gram_enc.build(3, None, False, False, fix)
    res["GC1_classical_triple"] = solve(F)
    m0, m, f, g1, g2, Lm = psi_f_data()
    res["psi_f"] = {"m0": m0, "m": m, "f": f, "nonzero_pairs_g1": len(g1)}
    F, _ = gram_enc.build(2, None, False, False, {"g1": g1, "g2": g2})
    res["GC2_genuine_pair"] = solve(F)
    F, _ = gram_enc.build(1, Lm, True, False, {"g1": g1})
    res["GC3_psi_f_on_net_heavy"] = solve(F)
    F, _ = gram_enc.build(1, Lm, False, False, {"g1": g1})
    res["GC3b_psi_f_on_net_noheavy"] = solve(F)
    allpairs = [(p, q) for p, q in itertools.combinations(CELLS, 2) if p[0] != q[0] and p[1] != q[1]]
    picks = allpairs[::max(1, len(allpairs) // 40)][:40]
    g1set = {(tuple(a), tuple(b)) for a, b in g1}
    rej = []
    for p, q in picks:
        mut = set(g1set) ^ {(p, q)}
        r = solve(gram_enc.build(2, None, False, False, {"g1": [[list(a), list(b)] for a, b in mut], "g2": g2})[0])
        rej.append(r)
    res["GC4_mutations"] = {"n": len(rej), "UNSAT": rej.count("UNSAT"), "SAT": rej.count("SAT")}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    main(sys.argv[1])

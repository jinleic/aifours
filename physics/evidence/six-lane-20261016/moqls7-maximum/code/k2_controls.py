#!/usr/bin/env python3
"""k2_controls.py: controls for the K2 pattern encoding. Lane moqls7-maximum.
  K2C1 classical triple L = i+j, Psi1 = 2i+j, Psi2 = 3i+j (standard form, reduced L): encoder A with these unit
       clauses (no W3) must be SAT; each single-coordinate mutation of Psi1 at one cell is reported (SAT/UNSAT).
  K2C2 genuine non-classical Psi(f) (Ball-Simoens Example 15, q = 7, H = {1,2,4}, shifted by m0) with its classical
       mate Phi(m), rows permuted so that L = Phi(m) becomes reduced (L = i+j): encoder A with --drop-psi2 and
       these unit clauses must be SAT.
  K2C3 independent evaluation of D, T2, T3, T4 on the genuine orthogonal pair (Psi(f), Phi(m)) in standard form
       (both squares as patterns): must pass.
Usage: python k2_controls.py OUT.json
"""
import itertools
import json
import subprocess
import sys

import k2_encA

P = 7


def psi_f_supports():
    H = {1, 2, 4}
    f0 = [x if x in H else 0 for x in range(P)]
    is_perm = lambda g: len({g(x) % P for x in range(P)}) == P
    M0 = [m for m in range(P) if is_perm(lambda x: f0[x] - m * x)]
    out = []
    for m0 in M0:
        f = [(f0[x] - m0 * x) % P for x in range(P)]
        for m in [(mm - m0) % P for mm in M0 if mm != m0]:
            S = [[sorted(y for y in range(P) if not is_perm(lambda x: i * f[x] + (j - y) * x)) for j in range(P)]
                 for i in range(P)]
            minv = pow(m, P - 2, P)
            Sp = [[S[(minv * i) % P][j] for j in range(P)] for i in range(P)]          # rows permuted
            out.append((m0, m, Sp))
    return out


def solve_fixed(fix, drop_psi2=False):
    F, _ = k2_encA.build(False, fix, drop_psi2)
    p = subprocess.run(["cadical", "-q"], input=F.text(), capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(p.returncode, "rc%d" % p.returncode)


def eval_T(S1, S2):
    bad = set()
    cells = [(i, j) for i in range(1, P) for j in range(P)]
    for p in cells:
        if set(S1[p[0]][p[1]]) & set(S2[p[0]][p[1]]):
            bad.add("D")
    allc = [(i, j) for i in range(P) for j in range(P)]
    for p, q in itertools.combinations(allc, 2):
        a = len(set(S1[p[0]][p[1]]) & set(S1[q[0]][q[1]]))
        b = len(set(S2[p[0]][p[1]]) & set(S2[q[0]][q[1]]))
        if a == 1 and b == 1:
            bad.add("T2")
    for k1 in range(P):
        for k2 in range(P):
            if k1 == k2:
                continue
            cov = [p for p in cells if k1 in S1[p[0]][p[1]] and k2 in S2[p[0]][p[1]]]
            if not cov:
                bad.add("T3")
            if len(cov) == 1 and (len(S1[cov[0][0]][cov[0][1]]) != 1 or len(S2[cov[0][0]][cov[0][1]]) != 1):
                bad.add("T4")
    return sorted(bad)


def main(out):
    res = {}
    L = [[(i + j) % P for j in range(P)] for i in range(P)]
    S1 = [[[(2 * i + j) % P] for j in range(P)] for i in range(P)]
    S2 = [[[(3 * i + j) % P] for j in range(P)] for i in range(P)]
    res["K2C1_classical"] = solve_fixed({"L": L, "S1": S1, "S2": S2})
    muts = []
    for (i, j) in [(1, 0), (2, 3), (5, 6)]:
        for k in range(P):
            if k == j:
                continue
            T = [[list(c) for c in row] for row in S1]
            T[i][j] = sorted(set(T[i][j]) ^ {k})
            if not T[i][j]:
                continue
            muts.append({"cell": [i, j], "toggle": k, "result": solve_fixed({"L": L, "S1": T, "S2": S2})})
    res["K2C1_mutations"] = muts
    res["K2C2_psi_f"] = []
    res["K2C3_tensor_eval"] = []
    for m0, m, Sp in psi_f_supports():
        res["K2C2_psi_f"].append({"m0": m0, "m": m, "weights": sorted({len(s) for row in Sp for s in row}),
                                  "result": solve_fixed({"L": L, "S1": Sp}, drop_psi2=True)})
        Sphi = [[[(i + j) % P] for j in range(P)] for i in range(P)]   # Phi(m) after the same row permutation
        res["K2C3_tensor_eval"].append({"m0": m0, "m": m, "violations": eval_T(Sp, Sphi)})
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({"K2C1": res["K2C1_classical"],
                      "K2C1_mut": [(d["cell"], d["toggle"], d["result"]) for d in muts],
                      "K2C2": [(d["m0"], d["m"], d["weights"], d["result"]) for d in res["K2C2_psi_f"]],
                      "K2C3": res["K2C3_tensor_eval"]}))


if __name__ == "__main__":
    main(sys.argv[1])

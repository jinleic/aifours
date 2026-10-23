#!/usr/bin/env /usr/bin/python3
"""gram_controlsB.py: genuine-data controls for encoder B (gram_encB.py), stdlib only. Lane moqls7-maximum.
Same data as gram_controls.py, computed here independently:
  GB1 classical triple L_a = a i + j (a=1,2,3), 3 squares, no heavy: SAT expected;
  GB2 genuine pair (Psi(f), Phi(m)) (Example 15, q=7, H={1,2,4}, f shifted by the first undetermined direction m0):
      2 squares, no heavy: SAT expected;
  GB3 Psi(f) alone on its 3-net (net-L = Phi(m)) with heavy: SAT expected;
  GB4 classical triple restricted: net-L = L_1, squares L_2, L_3, no heavy: SAT expected (K2-shaped classical data).
Sequential (one busy process at a time); scratch files under explore/scratch/.
Usage: /usr/bin/python3 gram_controlsB.py OUT.json
"""
import itertools
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = 7
CELLS = [(i, j) for i in range(P) for j in range(P)]
SCR = os.path.join(HERE, "..", "explore", "scratch")


def is_perm(g):
    return len({g(x) % P for x in range(P)}) == P


def run(args, fix):
    os.makedirs(SCR, exist_ok=True)
    fj = os.path.join(SCR, "ctlB_fix.json")
    cnf = os.path.join(SCR, "ctlB.cnf")
    with open(fj, "w") as f:
        json.dump(fix, f)
    subprocess.run([sys.executable, "-B", os.path.join(HERE, "gram_encB.py")] + args + ["--fix-json", fj, "--out", cnf],
                   check=True, capture_output=True)
    p = subprocess.run(["kissat", "-q", cnf], capture_output=True, text=True)
    return {10: "SAT", 20: "UNSAT"}.get(p.returncode, "rc%d" % p.returncode)


def same_symbol_pairs(Lsq):
    return [[list(p), list(q)] for p, q in itertools.combinations(CELLS, 2) if Lsq[p[0]][p[1]] == Lsq[q[0]][q[1]]]


def main(out):
    res = {}
    Ls = {a: [[(a * i + j) % P for j in range(P)] for i in range(P)] for a in (1, 2, 3)}
    res["GB1_classical_triple"] = run(["--squares", "3"], {"g%d" % a: same_symbol_pairs(Ls[a]) for a in (1, 2, 3)})
    H = {1, 2, 4}
    f0 = [x if x in H else 0 for x in range(P)]
    M0 = [m for m in range(P) if is_perm(lambda x: f0[x] - m * x)]
    m0 = M0[0]
    f = [(f0[x] - m0 * x) % P for x in range(P)]
    m = [(mm - m0) % P for mm in M0 if mm != m0][0]
    g1 = [[list(p), list(q)] for p, q in itertools.combinations(CELLS, 2)
          if not is_perm(lambda x: (q[0] - p[0]) * f[x] + (q[1] - p[1]) * x)]
    Lm = [[(m * i + j) % P for j in range(P)] for i in range(P)]
    res["GB2_genuine_pair"] = run(["--squares", "2"], {"g1": g1, "g2": same_symbol_pairs(Lm)})
    lj = os.path.join(SCR, "ctlB_L.json")
    with open(lj, "w") as fh:
        json.dump(Lm, fh)
    res["GB3_psi_f_on_net_heavy"] = run(["--squares", "1", "--net-L", lj, "--heavy"], {"g1": g1})
    with open(lj, "w") as fh:
        json.dump(Ls[1], fh)
    res["GB4_classical_K2_shape"] = run(["--squares", "2", "--net-L", lj],
                                        {"g1": same_symbol_pairs(Ls[2]), "g2": same_symbol_pairs(Ls[3])})
    res["psi_f"] = {"m0": m0, "m": m, "f": f, "g1_pairs": len(g1)}
    with open(out, "w") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res))


if __name__ == "__main__":
    main(sys.argv[1])

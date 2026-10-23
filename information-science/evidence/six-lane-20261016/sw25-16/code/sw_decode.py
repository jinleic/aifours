#!/usr/bin/env python3
"""Decode a solver model of a code/sw_cnf.py CNF into a strict witness file and run both checkers.

Usage: python3 -B code/sw_decode.py CNF.map.json SOLVER_STDOUT OUT.sw
Writes OUT.sw (mode x) and prints both checker lines plus an invariance check against the spec generators.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sw_common as C  # noqa: E402

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    mpath, sol, out = sys.argv[1], sys.argv[2], sys.argv[3]
    cmap = json.load(open(mpath))
    n, w = cmap["n"], cmap["w"]
    true = set()
    for line in open(sol):
        if line.startswith("v "):
            true.update(int(t) for t in line.split()[1:] if int(t) > 0)
    W = [[0] * n for _ in range(n)]
    for key, ent in cmap["cells"].items():
        i, j = map(int, key.split(","))
        if ent is None:
            v = 0
        else:
            a, s, p = ent
            if a in true:
                v = -1 if (s in true) else 1
                if p == 1:
                    v = -v
            else:
                v = 0
        W[i][j] = W[j][i] = v
    with open(out, "x") as f:
        f.write(C.to_strict(W, n, w))
    spec = json.load(open(cmap["spec"]))
    inv_ok = all(W[g["perm"][i]][g["perm"][j]] == g["sign"][i] * g["sign"][j] * W[i][j]
                 for g in spec["generators"] for i in range(n) for j in range(n))
    py = subprocess.run([sys.executable, "-B", os.path.join(LANE, "code/verify_sw.py"), out, "--expect", str(n),
                         str(w)], capture_output=True, text=True).stdout.strip()
    cc = subprocess.run([os.path.join(LANE, "bin/sw_check"), out, str(n), str(w)], capture_output=True,
                        text=True).stdout.strip()
    print(json.dumps({"out": out, "invariant_under_spec_generators": inv_ok, "verify_sw_py": py, "sw_check_c": cc}))


if __name__ == "__main__":
    main()

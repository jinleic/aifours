#!/usr/bin/env python3
"""Decode a SAT model of cfr_cnf.py into a cfr-raw-v1 CFR candidate (lane cfr33).

Usage: cfr_decode.py MAP.json SOLVER_OUTPUT OUT_RAW
Reads solver 'v' lines, reconstructs f_j (j = 1..r-1) from the X variables (each (j,x) must have exactly one true
value), sets f_0 = id and f_j(0) = 0, and writes rows R_0 = identity, R_j[f_j(s)] = s (mode 'x').
No validity is assumed or checked here beyond decodability; use cfr_check_events.py and cfr_check_posdiff.py.
"""
import hashlib, json, sys


def main():
    info = json.load(open(sys.argv[1]))
    n, r = int(info["spec"]["n"]), int(info["spec"]["r"])
    true = set()
    status = None
    for line in open(sys.argv[2]):
        if line.startswith("s "):
            status = line.strip()
        if line.startswith("v "):
            for t in line.split()[1:]:
                k = int(t)
                if k > 0:
                    true.add(k)
    if status != "s SATISFIABLE":
        print("DECODE FAIL: solver status %r" % status)
        sys.exit(1)
    f = {j: {0: 0} for j in range(1, r)}
    for j, x, v, var in info["xmap"]:
        if var in true:
            if x in f[j]:
                print("DECODE FAIL: f_%d(%d) has two values" % (j, x))
                sys.exit(1)
            f[j][x] = v
    rows = [list(range(n))]
    for j in range(1, r):
        if len(f[j]) != n:
            print("DECODE FAIL: f_%d undefined somewhere" % j)
            sys.exit(1)
        row = [None] * n
        for s in range(n):
            if row[f[j][s]] is not None:
                print("DECODE FAIL: f_%d not injective" % j)
                sys.exit(1)
            row[f[j][s]] = s
        rows.append(row)
    text = "".join(" ".join(map(str, row)) + "\n" for row in rows)
    with open(sys.argv[3], "x") as fh:
        fh.write(text)
    print("decoded %s r %d n %d sha256 %s" % (sys.argv[3], r, n, hashlib.sha256(text.encode()).hexdigest()))


if __name__ == "__main__":
    main()

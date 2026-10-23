#!/usr/bin/env python3
"""Decode a SAT model of dm_orbit_cnf.py into a (Z_n,k;1) DM in dm-raw format (lane cfr33).
Usage: dm_orbit_decode.py MAP.json SOLVER_OUTPUT OUT_DMRAW
Expands every orbit: column g(b) has entries mu_g * (b_{pi_g^-1(i)} - b_{pi_g^-1(0)}) (normalised so row 0 = 0).
No validity assumed; check with dm_check.py, then dm_to_cfr.py and the CFR checkers."""
import hashlib, json, sys

info = json.load(open(sys.argv[1]))
n, k = int(info["spec"]["n"]), int(info["spec"]["k"])
true = set()
status = None
for line in open(sys.argv[2]):
    if line.startswith("s "):
        status = line.strip()
    if line.startswith("v "):
        true.update(int(t) for t in line.split()[1:] if int(t) > 0)
if status != "s SATISFIABLE":
    print("DECODE FAIL: status %r" % status); sys.exit(1)
norb = len(info["reps"])
base = [[0] * k for _ in range(norb)]
seen = set()
for o, i, v, var in info["E"]:
    if var in true:
        if (o, i) in seen:
            print("DECODE FAIL: two values"); sys.exit(1)
        seen.add((o, i)); base[o][i] = v
cols = []
for o in range(norb):
    for mu, pi in info["reps"][o]:
        pinv = [0] * k
        for a, x in enumerate(pi):
            pinv[x] = a
        col = [(mu * (base[o][pinv[i]] - base[o][pinv[0]])) % n for i in range(k)]
        cols.append(col)
assert len(cols) == n
text = "".join(" ".join(str(cols[t][i]) for t in range(n)) + "\n" for i in range(k))
with open(sys.argv[3], "x") as fh:
    fh.write(text)
print("decoded DM %s k %d n %d sha256 %s" % (sys.argv[3], k, n, hashlib.sha256(text.encode()).hexdigest()))

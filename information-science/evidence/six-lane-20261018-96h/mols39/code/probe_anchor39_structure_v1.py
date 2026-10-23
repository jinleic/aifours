#!/usr/bin/env python3
"""probe_anchor39_structure_v1.py (ContinueCFR21, mols39 lane; frozen before execution; stdlib only; <=280 s).
Read-only analysis of the known six-row anchor DM_39_6_1 (Sage database, Handbook III.3.61), re-implemented from the
pinned Sage source (code table re-typed; the source file is only re-hashed, never executed/imported):
 (1) DM check; (2) exact-vector invariance of the column set under s3 = (16, pi), pi = (0 1 2)(3 4 5) with
 (s.c)_x = 16 c_{pi^-1(x)}, and under (-1, id); (3) orbit sizes and fixed columns; (4) which rows are bijections;
 (5) the full untwisted automorphism group of the column set (mu in Z39^*, pi in S6) acting exactly on vectors, and
 also acting modulo constants (columns as classes c + Z39*1).
Args: sage_source sha. Prints one JSON object."""
import sys, json, hashlib, itertools, time
T0 = time.monotonic()
raw = open(sys.argv[1], 'rb').read(); got = hashlib.sha256(raw).hexdigest()
if got != sys.argv[2]: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": got})); sys.exit(2)
n = 39
M = [[0,0,0,0,0,0],[4,23,13,5,12,11],[25,11,22,34,23,6],[13,4,20,17,15,29],[27,21,8,16,19,26],[16,19,34,38,26,21]]
Mb = [[0,0,0,0,0,0],[1,16,22,17,38,23],[-1,-16,-22,-17,-38,-23]]
for R in zip(*M):
    a,b,c,d,e,f = (x % n for x in R)
    for i in range(3):
        Mb.append([a,b,c,d,e,f]); Mb.append([-a,-b,-c,-d,-e,-f])
        a,b,c,d,e,f = ((16*x) % n for x in [c,a,b,f,d,e])
cols = [tuple(x % n for x in col) for col in Mb]
k = 6
rows = [[c[i] for c in cols] for i in range(k)]
out = {"status": "OK", "source_sha256": got, "n_cols": len(cols), "distinct_cols": len(set(cols))}
out["dm_ok"] = all(len({(rows[i][c] - rows[j][c]) % n for c in range(n)}) == n for i in range(k) for j in range(i + 1, k))
out["row_is_bijection"] = [len(set(r)) == n for r in rows]
S = set(cols)
def act(mu, pinv, c): return tuple((mu * c[pinv[x]]) % n for x in range(k))
pi_inv = [2, 0, 1, 5, 3, 4]   # pi = (0 1 2)(3 4 5): pi^-1(0)=2, pi^-1(1)=0, ...
out["inv_s3_exact"] = all(act(16, pi_inv, c) in S for c in cols)
out["inv_neg_exact"] = all(act(n - 1, list(range(k)), c) in S for c in cols)
# orbits under G6
gens = [(16, pi_inv), (n - 1, list(range(k)))]
seen = set(); orbits = []
for c in cols:
    if c in seen: continue
    orb = {c}; frontier = [c]
    while frontier:
        nf = []
        for x in frontier:
            for mu, pinv in gens:
                y = act(mu, pinv, x)
                if y not in orb: orb.add(y); nf.append(y)
        frontier = nf
    seen |= orb; orbits.append(sorted(orb))
out["orbit_sizes"] = sorted(len(o) for o in orbits)
out["orbit_reps"] = [o[0] for o in orbits]
# full untwisted automorphism group: exact vectors, and modulo constants
units = [u for u in range(1, n) if u % 3 and u % 13]
def norm(c): return tuple((x - c[0]) % n for x in c)
Sn = set(norm(c) for c in cols)
exact = []; modc = []
for mu in units:
    for perm in itertools.permutations(range(k)):
        pinv = [0] * k
        for x in range(k): pinv[perm[x]] = x
        if all(act(mu, pinv, c) in S for c in cols): exact.append([mu, list(perm)])
        if all(norm(act(mu, pinv, c)) in Sn for c in cols): modc.append([mu, list(perm)])
out["aut_exact_order"] = len(exact); out["aut_modconst_order"] = len(modc)
out["aut_exact"] = exact; out["aut_modconst"] = modc
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))

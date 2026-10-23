#!/usr/bin/env python3
"""probe_sign_patterns_v1.py (ContinueCFR21; frozen before execution; stdlib only; <=280 s).
Exploratory data probe (no claim): for every pinned DM (96 P21 Z21 DM6; 2 Z27 DM6), compute the permutation sign of
each row-pair difference map delta_ij : column index -> Z_n, and products over all row triangles and over all
4-cycles; report whether any product is constant across all inputs of the same n (a candidate sign relation)."""
import sys, json, time, hashlib, itertools
T0 = time.monotonic()
def pinned(p, w):
    raw = open(p, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != w: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": p, "got": h})); sys.exit(2)
    return raw
def sign(perm):
    n = len(perm); seen = [False] * n; s = 1
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = perm[j]; L += 1
            if L % 2 == 0: s = -s
    return s
p21 = json.loads(pinned(sys.argv[1], sys.argv[2]))
dms = [(21, dm["rows"]) for dm in p21["dms"]]
for path, w in ((sys.argv[3], sys.argv[4]), (sys.argv[5], sys.argv[6])):
    dms.append((27, [list(map(int, ln.split())) for ln in pinned(path, w).decode().strip().splitlines()]))
res = {}
for n, R in dms:
    k = len(R); s = {}
    for i, j in itertools.permutations(range(k), 2):
        s[(i, j)] = sign([(R[i][c] - R[j][c]) % n for c in range(n)])
    tri = tuple(s[(a, b)] * s[(b, c)] * s[(c, a)] for a, b, c in itertools.combinations(range(k), 3))
    sym = tuple(s[(a, b)] * s[(b, a)] for a, b in itertools.combinations(range(k), 2))
    allp = 1
    for a, b in itertools.combinations(range(k), 2): allp *= s[(a, b)]
    key = str(n)
    r = res.setdefault(key, {"dms": 0, "triangle_products": {}, "antisym_products": {}, "product_all_pairs": {}})
    r["dms"] += 1
    r["triangle_products"][str(tri)] = r["triangle_products"].get(str(tri), 0) + 1
    r["antisym_products"][str(sym)] = r["antisym_products"].get(str(sym), 0) + 1
    r["product_all_pairs"][str(allp)] = r["product_all_pairs"].get(str(allp), 0) + 1
print(json.dumps({"status": "OK", "by_n": res, "wall_s": round(time.monotonic() - T0, 3)}, sort_keys=True))

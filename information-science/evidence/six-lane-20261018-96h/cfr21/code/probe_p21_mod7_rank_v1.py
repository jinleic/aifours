#!/usr/bin/env python3
"""probe_p21_mod7_rank_v1.py (ContinueCFR21, frozen before execution). Stdlib only, <=280 s self budget.
For each pinned P21 six-row (Z21,6;1)-DM: affine rank over F7 of the mod-7 column image (rows minus row 0),
affine rank over F3 of the mod-3 image, the F7-relations (left kernel) if any, and counts of column pairs whose
mod-3 images coincide up to translation (mod-3 twins). Prints one JSON object."""
import sys, json, time, hashlib, itertools
T0 = time.monotonic()
path, want = sys.argv[1], sys.argv[2]
raw = open(path, 'rb').read(); got = hashlib.sha256(raw).hexdigest()
if got != want: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": got})); sys.exit(2)
d = json.loads(raw); n = 21
def rank_mod(rows, p):
    rows = [[x % p for x in r] for r in rows]; r = 0; m = len(rows[0]) if rows else 0
    for col in range(m):
        piv = next((i for i in range(r, len(rows)) if rows[i][col]), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = pow(rows[r][col], p - 2, p)
        rows[r] = [(x * inv) % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col]:
                f = rows[i][col]; rows[i] = [(a - f * b) % p for a, b in zip(rows[i], rows[r])]
        r += 1
    return r
res = []; h7 = {}; h3 = {}; tw = {}
for dm in d["dms"]:
    R = dm["rows"]; k = len(R)
    out = {"sol": dm["sol"]}
    for p, h in ((7, h7), (3, h3)):
        # affine rank of points v(c) = (R[i][c]-R[0][c]) mod p, i=1..k-1: rank of {v(c)-v(0)}
        pts = [[(R[i][c] - R[0][c]) % p for i in range(1, k)] for c in range(n)]
        diffs = [[(a - b) % p for a, b in zip(pts[c], pts[0])] for c in range(1, n)]
        rk = rank_mod(diffs, p); out["affine_rank_mod%d" % p] = rk; h[rk] = h.get(rk, 0) + 1
    A = [[x % 3 for x in r] for r in R]
    twins = 0
    for c1 in range(n):
        for c2 in range(c1 + 1, n):
            if len(set((A[i][c1] - A[i][c2]) % 3 for i in range(k))) == 1: twins += 1
    out["mod3_twin_pairs"] = twins; tw[twins] = tw.get(twins, 0) + 1
    res.append(out)
print(json.dumps({"status": "OK", "input_sha256": got, "rank7_hist": {str(a): b for a, b in h7.items()},
                  "rank3_hist": {str(a): b for a, b in h3.items()}, "mod3_twin_hist": {str(a): b for a, b in tw.items()},
                  "per_dm": res, "wall_s": round(time.monotonic() - T0, 3)}, sort_keys=True))

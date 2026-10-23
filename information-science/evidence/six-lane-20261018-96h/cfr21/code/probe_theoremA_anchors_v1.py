#!/usr/bin/env python3
"""probe_theoremA_anchors_v1.py (ContinueCFR21; frozen before execution; stdlib only; self budget 280 s).
Anchor/boundary controls for Theorem A (mod-3 constant characters):
 (a) for every input DM (k x n over Z_n): K = {chi in F3^k : sum chi = 0, sum_i chi_i D_i(c) mod 3 constant in c},
     its support distribution and the mod-3 affine rank r = (k-1) - dim K; DM validity is re-checked.
 (b) Fourier-identity control: exhaustive count of pairs f,g: [m] -> F3 with f, g, f+g, f-g balanced, m in {3,6};
     constructive positive pair for m = 9.
Inputs: p21-detail.json sha, A-DM.raw sha, B-DM.raw sha (Z27 six-row DMs; 9 | 27 is the boundary case)."""
import sys, json, time, hashlib, itertools
T0 = time.monotonic()
def pinned(path, want):
    raw = open(path, 'rb').read(); h = hashlib.sha256(raw).hexdigest()
    if h != want: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "path": path, "got": h})); sys.exit(2)
    return raw
p21 = json.loads(pinned(sys.argv[1], sys.argv[2]))
z27 = []
for path, want in ((sys.argv[3], sys.argv[4]), (sys.argv[5], sys.argv[6])):
    rows = [list(map(int, ln.split())) for ln in pinned(path, want).decode().strip().splitlines()]
    z27.append((path.rsplit('/', 1)[-1], rows))
def is_dm(D, n):
    return all(sorted((D[i][c] - D[j][c]) % n for c in range(n)) == list(range(n)) for i in range(len(D)) for j in range(len(D)) if i != j)
def K_info(D, n):
    k = len(D); A = [[x % 3 for x in r] for r in D]
    Ks = []
    for chi in itertools.product(range(3), repeat=k):
        if not any(chi) or sum(chi) % 3: continue
        vals = set(sum(chi[i] * A[i][c] for i in range(k)) % 3 for c in range(n))
        if len(vals) == 1: Ks.append(chi)
    dimK = 0
    while 3 ** dimK - 1 < len(Ks): dimK += 1
    assert 3 ** dimK - 1 == len(Ks)
    sup = {}
    for chi in Ks: s = sum(1 for x in chi if x); sup[s] = sup.get(s, 0) + 1
    return {"dimK": dimK, "affine_rank": (k - 1) - dimK, "support_hist": {str(a): b for a, b in sorted(sup.items())},
            "min_support": min((sum(1 for x in chi if x) for chi in Ks), default=None), "examples": [list(c) for c in Ks[:4]]}
out = {"status": "OK"}
agg = {}
for dm in p21["dms"]:
    R = dm["rows"]; assert is_dm(R, 21)
    info = K_info(R, 21); key = json.dumps({"dimK": info["dimK"], "r": info["affine_rank"]})
    agg[key] = agg.get(key, 0) + 1
out["p21_n21_k6"] = agg
out["z27_k6"] = []
for name, R in z27:
    out["z27_k6"].append({"file": name, "dm_ok": is_dm(R, 27), **K_info(R, 27)})
# Fourier identity control
def bal(v, m): return all(v.count(t) == m // 3 for t in range(3))
fc = {}
for m in (3, 6):
    cnt = 0
    for f in itertools.product(range(3), repeat=m):
        if not bal(list(f), m): continue
        for g in itertools.product(range(3), repeat=m):
            if not bal(list(g), m): continue
            s = [(a + b) % 3 for a, b in zip(f, g)]; d = [(a - b) % 3 for a, b in zip(f, g)]
            if bal(s, m) and bal(d, m): cnt += 1
    fc[str(m)] = cnt
pts = [(u, v) for u in range(3) for v in range(3)]
f9 = [u for u, v in pts]; g9 = [v for u, v in pts]
fc["9_constructive_pair_all_balanced"] = all(bal(x, 9) for x in (f9, g9, [(a + b) % 3 for a, b in zip(f9, g9)], [(a - b) % 3 for a, b in zip(f9, g9)]))
out["fourier_control_pair_counts"] = fc
out["wall_s"] = round(time.monotonic() - T0, 3)
print(json.dumps(out, sort_keys=True))

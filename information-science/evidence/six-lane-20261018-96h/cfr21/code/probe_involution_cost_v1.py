#!/usr/bin/env python3
"""probe_involution_cost_v1.py (ContinueCFR21; frozen before execution; stdlib only; self wall budget 280 s).
Cost calibration (NOT a production search) for the open order-2 models g00 (mu=1) and g10 (mu=8), pi=(12)(34)(56),
in the old exact representation (rows 0, t, mu h(t), g(t), mu g(h(t)), j(t), mu j(h(t)); h an involution of Z21 with
t - mu h(t) bijective, g(0)=j(0)=0 after the proved affine normalisation). For the first H canonical involutions of
the pinned old H list: enumerate G_h = {g : g(0)=0, g, g-id, g-mu h, g-mu g(h) bijective} by bitmask DFS over the
orbits of h (static order), count DFS nodes, then count compatible pairs (g,j) (g-j and g-mu j(h) bijective) and
directly re-check every resulting 7-row DM. Prints one JSON object. Args: hlist_path sha mu H_max."""
import sys, json, time, hashlib
T0 = time.monotonic(); BUD = 270.0
path, want, mu, HMAX = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
raw = open(path, 'rb').read(); got = hashlib.sha256(raw).hexdigest()
if got != want: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": got})); sys.exit(2)
n = 21; FULL = (1 << n) - 1
hs = []
for ln in raw.decode().splitlines():
    if ln.startswith('c hl '):
        parts = ln.split(); hh = list(map(int, parts[4:]))
        assert len(hh) == n; hs.append(hh)
def is_dm(D):
    return all(sorted((D[i][c] - D[j][c]) % n for c in range(n)) == list(range(n)) for i in range(len(D)) for j in range(len(D)) if i != j)
res = []; tot_nodes = 0; tot_g = 0; tot_pairs = 0; done = 0
for hidx, h in enumerate(hs[:HMAX]):
    if time.monotonic() - T0 > BUD: break
    assert all(h[h[x]] == x for x in range(n)) and h[0] == 0
    assert sorted((x - mu * h[x]) % n for x in range(n)) == list(range(n))
    fixed = [x for x in range(1, n) if h[x] == x]
    pairs = [(x, h[x]) for x in range(1, n) if h[x] > x]
    items = [('f', z) for z in fixed] + [('p', x, y) for x, y in pairs]
    G = []; nodes = [0]; g = [None] * n; g[0] = 0
    def bit(v): return 1 << (v % n)
    A0 = bit(0); B0 = bit(0); C0 = bit(0); D0 = bit(0)
    def dfs(k, A, B, C, D):
        nodes[0] += 1
        if k == len(items):
            G.append(g[:]); return
        it = items[k]
        if it[0] == 'f':
            z = it[1]
            for w in range(n):
                a = bit(w); b = bit(w - z); c = bit(w - mu * z); d = bit(w - mu * w)
                if A & a or B & b or C & c or D & d: continue
                g[z] = w; dfs(k + 1, A | a, B | b, C | c, D | d)
            g[z] = None
        else:
            x, y = it[1], it[2]
            for u in range(n):
                a1 = bit(u); b1 = bit(u - x); c1 = bit(u - mu * y)
                if A & a1 or B & b1 or C & c1: continue
                for v in range(n):
                    if v == u: continue
                    a2 = bit(v); b2 = bit(v - y); c2 = bit(v - mu * x)
                    if A & a2 or B & b2 or C & c2: continue
                    if b1 == b2 or c1 == c2: continue
                    d1 = bit(u - mu * v); d2 = bit(v - mu * u)
                    if D & d1 or D & d2 or d1 == d2: continue
                    g[x] = u; g[y] = v
                    dfs(k + 1, A | a1 | a2, B | b1 | b2, C | c1 | c2, D | d1 | d2)
            g[x] = None; g[y] = None
    t1 = time.monotonic()
    dfs(0, A0, B0, C0, D0)
    t2 = time.monotonic()
    # pairs (g, j)
    npair = 0; found = []
    for i1 in range(len(G)):
        g1 = G[i1]
        for i2 in range(len(G)):
            if i2 == i1: continue
            j1 = G[i2]
            if len(set((g1[x] - j1[x]) % n for x in range(n))) != n: continue
            if len(set((g1[x] - mu * j1[h[x]]) % n for x in range(n))) != n: continue
            npair += 1
            D = [[0] * n, list(range(n)), [(mu * h[t]) % n for t in range(n)], g1, [(mu * g1[h[t]]) % n for t in range(n)],
                 j1, [(mu * j1[h[t]]) % n for t in range(n)]]
            found.append({"g": g1, "j": j1, "is_dm": is_dm(D)})
    res.append({"h_index": hidx + 1, "fixed_points_besides_0": len(fixed), "G_size": len(G), "dfs_nodes": nodes[0],
                "dfs_s": round(t2 - t1, 3), "compatible_pairs": npair})
    tot_nodes += nodes[0]; tot_g += len(G); tot_pairs += npair; done += 1
    if found: res[-1]["solutions"] = found[:2]
out = {"status": "OK", "input_sha256": got, "mu": mu, "h_total_in_list": len(hs), "h_processed": done,
       "total_dfs_nodes": tot_nodes, "total_G": tot_g, "total_compatible_pairs": tot_pairs, "per_h": res,
       "wall_s": round(time.monotonic() - T0, 3)}
print(json.dumps(out, sort_keys=True))

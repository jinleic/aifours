#!/usr/bin/env python3
"""probe_involution_mrv_cost_v2.py (ContinueCFR21; frozen before execution; stdlib only).
v2 of probe_involution_mrv_cost_v1.py (1189f999…): v1 had a coverage-test bug (compared against a mask without
value 0 while the used mask contains it, so every H was pruned at the root; v1 output is INVALID).
Cost calibration only (no exclusion claim). Model rows 0, t, mu h(t), g, mu g(h), j, mu j(h); g(0) = 0.
For the first H canonical involutions of a pinned H list (n, mu read from its header): enumerate
G_h = {g : g, g-id, g-mu h, g-mu g(h) bijective} with orbit-MRV + value-coverage pruning; count nodes, time;
then count compatible pairs (g, j) (g-j, g-mu j(h) bijective) and re-check each resulting 7-row matrix as a DM.
Budget checked at every 256 nodes. Args: hlist sha H_max budget_s."""
import sys, json, time, hashlib
T0 = time.monotonic()
path, want, HMAX, BUD = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
raw = open(path, 'rb').read(); got = hashlib.sha256(raw).hexdigest()
if got != want: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": got})); sys.exit(2)
lines = raw.decode().splitlines()
hdr = lines[0].split(); n = int(hdr[hdr.index('n') + 1]); mu = int(hdr[hdr.index('mu') + 1])
hs = [list(map(int, ln.split()[4:])) for ln in lines if ln.startswith('c hl ')]
class Budget(Exception): pass
def B(v): return 1 << (v % n)
FULL = (1 << n) - 1
def is_dm(D):
    return all(sorted((D[i][c] - D[j][c]) % n for c in range(n)) == list(range(n)) for i in range(len(D)) for j in range(len(D)) if i != j)
res = []; status = "OK"
for hidx, h in enumerate(hs[:HMAX]):
    assert len(h) == n and all(h[h[x]] == x for x in range(n)) and h[0] == 0
    fixed = [x for x in range(1, n) if h[x] == x]
    orbits = [(x,) for x in fixed] + [(x, h[x]) for x in range(1, n) if h[x] > x]
    opts = []
    for o in orbits:
        L = []
        if len(o) == 1:
            z = o[0]
            for w in range(1, n):
                b, c, d = B(w - z), B(w - mu * z), B(w - mu * w)
                if (b | c | d) & 1: continue
                L.append((B(w), b, c, d, ((z, w),)))
        else:
            x, y = o
            for u in range(1, n):
                for v in range(1, n):
                    if u == v: continue
                    b1, b2 = B(u - x), B(v - y); c1, c2 = B(u - mu * y), B(v - mu * x); d1, d2 = B(u - mu * v), B(v - mu * u)
                    if b1 == b2 or c1 == c2 or d1 == d2: continue
                    bb, cc, dd = b1 | b2, c1 | c2, d1 | d2
                    if (bb | cc | dd) & 1: continue
                    L.append((B(u) | B(v), bb, cc, dd, ((x, u), (y, v))))
        opts.append(L)
    G = []; nodes = [0]; cur = list(opts)
    def rec(rem, uA, uB, uC, uD, assign):
        nodes[0] += 1
        if (nodes[0] & 255) == 0 and time.monotonic() - T0 > BUD: raise Budget()
        if not rem:
            g = [0] * n
            for x, val in assign: g[x] = val
            G.append(g); return
        filt = {}; best = None
        for oi in rem:
            L = [op for op in cur[oi] if not (op[0] & uA or op[1] & uB or op[2] & uC or op[3] & uD)]
            if not L: return
            filt[oi] = L
            if best is None or len(L) < len(filt[best]): best = oi
        cA, cB, cC, cD = uA, uB, uC, uD
        for L in filt.values():
            for op in L: cA |= op[0]; cB |= op[1]; cC |= op[2]; cD |= op[3]
        if cA != FULL or cB != FULL or cC != FULL or cD != FULL: return
        saved = {oi: cur[oi] for oi in filt}
        for oi, L in filt.items(): cur[oi] = L
        rem2 = [oi for oi in rem if oi != best]
        for op in filt[best]:
            assign.extend(op[4])
            rec(rem2, uA | op[0], uB | op[1], uC | op[2], uD | op[3], assign)
            del assign[-len(op[4]):]
        for oi, L in saved.items(): cur[oi] = L
    t1 = time.monotonic(); st = "COMPLETE"
    try:
        rec(list(range(len(orbits))), 1, 1, 1, 1, [])
    except Budget:
        st = "INCOMPLETE_BUDGET"; status = "PARTIAL"
    t2 = time.monotonic()
    # verify each g and count pairs
    okg = all(len(set(g)) == n and len(set((g[x] - x) % n for x in range(n))) == n and
              len(set((g[x] - mu * h[x]) % n for x in range(n))) == n and
              len(set((g[x] - mu * g[h[x]]) % n for x in range(n))) == n for g in G)
    pairs = 0; dm_ok = 0
    for a in range(len(G)):
        for bidx in range(len(G)):
            if a == bidx: continue
            g, j = G[a], G[bidx]
            if len(set((g[x] - j[x]) % n for x in range(n))) != n: continue
            if len(set((g[x] - mu * j[h[x]]) % n for x in range(n))) != n: continue
            pairs += 1
            D = [[0] * n, list(range(n)), [(mu * h[t]) % n for t in range(n)], g, [(mu * g[h[t]]) % n for t in range(n)],
                 j, [(mu * j[h[t]]) % n for t in range(n)]]
            if is_dm(D): dm_ok += 1
    res.append({"h_index": hidx + 1, "fixed_besides_0": len(fixed), "status": st, "nodes": nodes[0], "G_found": len(G),
                "G_all_verified": okg, "seconds": round(t2 - t1, 3), "compatible_ordered_pairs": pairs, "pairs_dm_verified": dm_ok})
    if st != "COMPLETE": break
print(json.dumps({"status": status, "input_sha256": got, "n": n, "mu": mu, "per_h": res, "wall_s": round(time.monotonic() - T0, 3)}, sort_keys=True))

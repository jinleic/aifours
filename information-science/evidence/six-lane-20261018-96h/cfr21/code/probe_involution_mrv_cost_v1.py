#!/usr/bin/env python3
"""probe_involution_mrv_cost_v1.py (ContinueCFR21; frozen before execution; stdlib only).
Cost calibration only (NOT a production search; no exclusion claim). For the first H canonical involutions h of a
pinned old H list (model rows 0, t, mu h(t), g, mu g(h), j, mu j(h); g(0)=0), enumerate
G_h = {g : g, g-id, g-mu h, g-mu g(h) bijective} with orbit-MRV + value-coverage pruning, counting nodes and time.
The self wall budget is checked at EVERY node (lesson from deviation CFR21-D2); an over-budget H is reported
INCOMPLETE with its partial node count. Prints one JSON object. Args: hlist sha mu H_max budget_s."""
import sys, json, time, hashlib
T0 = time.monotonic()
path, want, mu, HMAX, BUD = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
raw = open(path, 'rb').read(); got = hashlib.sha256(raw).hexdigest()
if got != want: print(json.dumps({"status": "INPUT_PIN_MISMATCH", "got": got})); sys.exit(2)
n = 21
hs = [list(map(int, ln.split()[4:])) for ln in raw.decode().splitlines() if ln.startswith('c hl ')]
class Budget(Exception): pass
def B(v): return 1 << (v % n)
res = []; status = "OK"
for hidx, h in enumerate(hs[:HMAX]):
    assert all(h[h[x]] == x for x in range(n)) and h[0] == 0
    fixed = [x for x in range(1, n) if h[x] == x]
    orbits = [(x,) for x in fixed] + [(x, h[x]) for x in range(1, n) if h[x] > x]
    # options per orbit: tuples (a, b, c, d, assignment)
    opts = []
    for o in orbits:
        L = []
        if len(o) == 1:
            z = o[0]
            for w in range(1, n):
                a, b, c, d = B(w), B(w - z), B(w - mu * z), B(w - mu * w)
                if b == B(0) or c == B(0) or d == B(0): continue
                L.append((a, b, c, d, ((z, w),)))
        else:
            x, y = o
            for u in range(1, n):
                for v in range(1, n):
                    if u == v: continue
                    a = B(u) | B(v)
                    b1, b2 = B(u - x), B(v - y); c1, c2 = B(u - mu * y), B(v - mu * x); d1, d2 = B(u - mu * v), B(v - mu * u)
                    if b1 == b2 or c1 == c2 or d1 == d2: continue
                    bb, cc, dd = b1 | b2, c1 | c2, d1 | d2
                    if (bb | cc | dd) & B(0): continue
                    L.append((a, bb, cc, dd, ((x, u), (y, v))))
        opts.append(L)
    FULLx = ((1 << n) - 1) & ~B(0)
    G = []; nodes = [0]
    def rec(rem, uA, uB, uC, uD, assign):
        nodes[0] += 1
        if (nodes[0] & 1023) == 0 and time.monotonic() - T0 > BUD: raise Budget()
        if not rem:
            G.append(dict(assign)); return
        # filter options of remaining orbits
        filt = {}
        best = None
        for oi in rem:
            L = [op for op in opts_cur[oi] if not (op[0] & uA or op[1] & uB or op[2] & uC or op[3] & uD)]
            if not L: return
            filt[oi] = L
            if best is None or len(L) < len(filt[best]): best = oi
        # coverage pruning: every unused value of each family must be coverable
        cA = cB = cC = cD = 0
        for L in filt.values():
            for op in L: cA |= op[0]; cB |= op[1]; cC |= op[2]; cD |= op[3]
        if (cA | uA) != FULLx or (cB | uB) != FULLx or (cC | uC) != FULLx or (cD | uD) != FULLx: return
        saved = {oi: opts_cur[oi] for oi in filt}
        for oi, L in filt.items(): opts_cur[oi] = L
        rem2 = [oi for oi in rem if oi != best]
        for op in filt[best]:
            assign.extend(op[4])
            rec(rem2, uA | op[0], uB | op[1], uC | op[2], uD | op[3], assign)
            del assign[-len(op[4]):]
        for oi, L in saved.items(): opts_cur[oi] = L
    opts_cur = list(opts)
    t1 = time.monotonic(); st = "COMPLETE"
    try:
        rec(list(range(len(orbits))), B(0), B(0), B(0), B(0), [(0, 0)])
    except Budget:
        st = "INCOMPLETE_BUDGET"; status = "PARTIAL"
    t2 = time.monotonic()
    res.append({"h_index": hidx + 1, "fixed_besides_0": len(fixed), "status": st, "nodes": nodes[0], "G_found": len(G),
                "seconds": round(t2 - t1, 3)})
    if st != "COMPLETE": break
print(json.dumps({"status": status, "input_sha256": got, "mu": mu, "per_h": res, "wall_s": round(time.monotonic() - T0, 3)}, sort_keys=True))

#!/usr/bin/env python3
"""E6 (plan-E6.md): interval-feasibility statistics and a raw-DP counterexample probe inside RES_<(p).
Output: out/e6_interval_probe.json (exclusive create)."""
import json, os, random, sys, hashlib, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
rng = random.Random(20261018)

def lam_int(p, kap, B, x):
    return min(p, x + B - kap + 1, (x + B) // 2 + 1)

def interval_dfs(p, kap, a, b, l, cap_nodes, cap_keep, Nlen):
    """all-odd representation; returns (status, nodes, kept assignments list of y)."""
    k = len(a); A = sum(a); B = sum(b); Dt = A - B
    d = [a[i] - b[i] for i in range(k)]
    pref = [0] * (k + 1)
    for i in range(k): pref[i + 1] = pref[i] + d[i]
    def Dint(x, y):   # runs x+1..y cyclic (block x before, block y after)
        if x < y: return pref[y + 1] - pref[x + 1]
        return (pref[k] - pref[x + 1]) + pref[y + 1]
    inv2 = (p + 1) // 2
    forb = {}
    for x in range(k):
        for y in range(k):
            if x == y: continue
            DQ = Dint(x, y)
            lq = lam_int(p, kap, B, DQ); lc = lam_int(p, kap, B, Dt - DQ)
            forb[(x, y)] = {v % p for v in range(1 - lc, lq)}
            if len(forb[(x, y)]) >= p:
                return "full_window", 0, []
    lo0 = -min(p, A - kap - 1, A // 2); hi0 = min(p, B - kap - 1, B // 2)
    if any(v % p == 0 for v in range(lo0, hi0 + 1)):
        return "zero_pattern", 0, []
    y = [None] * k; y[k - 1] = 0
    st = {"nodes": 0, "kept": [], "leaves": 0}
    def ok(j):
        for x in range(k):
            if x == j or y[x] is None: continue
            if (inv2 * (y[x] - y[j])) % p in forb[(x, j)]: return False
        for i in (j, (j + 1) % k):
            if a[i] + b[i] == 0:
                bl, br = (i - 1) % k, i
                if y[bl] is not None and y[br] is not None and y[bl] == y[br]: return False
        return True
    def rec(j):
        if st["nodes"] > cap_nodes: return
        if j == k - 1:
            st["leaves"] += 1
            if len(st["kept"]) < cap_keep:
                st["kept"].append(list(y))
            return
        vals = list(range(p)); rng.shuffle(vals)
        for v in vals:
            y[j] = v; st["nodes"] += 1
            if ok(j): rec(j + 1)
            y[j] = None
    # block k-1 is fixed to 0; check its genuineness constraints lazily inside ok() of neighbours
    rec(0)
    status = "capped" if st["nodes"] > cap_nodes else "complete"
    return status, st["leaves"], st["kept"]

def rand_res(p, kap, B, k):
    H = p - 1 - kap; F = 2 * H + k; Nlen = 4 * p - 2; R = Nlen - F; A = R - B
    if A < B or A > 2 * p - 1 or R < 1: return None
    for _ in range(400):
        g = rng.randint(1, min(k - 1, 2 * kap))
        ne = rng.sample(range(k), k - g)
        if R < len(ne) or not ne: continue
        if B == 0: nb = 0
        else:
            hi = min(B, len(ne) - (1 if A > 0 else 0))
            if hi < 1: continue
            nb = rng.randint(1, hi)
        bruns = rng.sample(ne, nb); aruns = [i for i in ne if i not in bruns]
        if (A > 0 and not aruns) or A < len(aruns) or B < len(bruns): continue
        a = [0] * k; b = [0] * k
        for i in aruns: a[i] = 1
        for i in bruns: b[i] = 1
        for _ in range(A - len(aruns)): a[rng.choice(aruns)] += 1
        for _ in range(B - len(bruns)): b[rng.choice(bruns)] += 1
        if g + sum(1 for i in ne if (a[i] + b[i]) % 2 == 0) > 2 * kap: continue
        l = [1] * k; l[rng.randrange(k)] += 2 * H
        return a, b, l
    return None

out = {"control": {}, "strata": [], "candidates": []}
t0 = time.time()
# positive control: sharpness family at length 4p-3 (kappa computed as p-1-H = 0 there)
for p in (7, 11):
    a = [0, 2 * p - 3]; b = [0, 0]; l = [1, 2 * p - 1]   # run 0 empty (between block 1 and block 0), run 1 = rho^(2p-3)
    kap = p - 1 - sum(x // 2 for x in l)
    status, leaves, kept = interval_dfs(p, kap, a, b, l, 10 ** 6, 10 ** 4, 4 * p - 3)
    found = 0
    for yv in kept:
        if not dp.dp1(gwin.word_of(a, b, l, yv, p), p):
            found += 1
    out["control"][str(p)] = dict(status=status, interval_feasible=leaves, dp_avoiders_among_kept=found)
# strata
plan = []
for p, kaps in ((7, range(2, 7)), (11, range(2, 11))):
    for kap in kaps:
        for B in range(0, kap):
            kmin = 2 * kap - B + 1; kmax = p + 2 * kap
            for k in range(kmin, kmax + 1):
                H = p - 1 - kap; R = 4 * p - 2 - 2 * H - k; A = R - B
                if R < 1 or A < B or A > 2 * p - 1: continue
                plan.append((p, kap, B, k))
rng.shuffle(plan)
budget_s = 1500
for (p, kap, B, k) in plan:
    if time.time() - t0 > budget_s: break
    if p == 11 and k > 16: continue
    rd = rand_res(p, kap, B, k)
    if rd is None: continue
    a, b, l = rd
    status, leaves, kept = interval_dfs(p, kap, a, b, l, 60000 if p == 7 else 20000, 40, 4 * p - 2)
    dpn = 0; avoid = 0
    for yv in kept:
        w = gwin.word_of(a, b, l, yv, p)
        dpn += 1
        if not dp.dp1(w, p):
            if not dp.dp2(w, p):
                avoid += 1
                out["candidates"].append(dict(p=p, kappa=kap, B=B, k=k, a=a, b=b, l=l, y=yv))
    out["strata"].append(dict(p=p, kappa=kap, B=B, k=k, status=status, interval_feasible=leaves, dp_checked=dpn, avoiders=avoid))
out["elapsed_s"] = round(time.time() - t0, 1)
srcs = {}
for fn in ("dp.py", "gwin.py", "e6_interval_probe.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(HERE, "..", "plan-E6.md"), "rb") as f:
    srcs["plan-E6.md"] = hashlib.sha256(f.read()).hexdigest()
out["sources_sha256"] = srcs
with open(os.path.join(HERE, "..", "out", "e6_interval_probe.json"), "x") as f:
    json.dump(out, f, indent=0)
tot_if = sum(1 for s in out["strata"] if s["interval_feasible"] > 0)
print(json.dumps(out["control"]))
print("strata", len(out["strata"]), "with interval-feasible", tot_if, "dp_checked", sum(s["dp_checked"] for s in out["strata"]),
      "candidates", len(out["candidates"]), "elapsed", out["elapsed_s"])

#!/usr/bin/env python3
"""E13 (plan-E13.md): regime III family p = 7, kappa = 3, k = 13, R = 7.  Output out/e13_regime3_p7.json (x)."""
import json, os, sys, hashlib, itertools
from collections import Counter
sys.setrecursionlimit(10000)
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
p, kap, k = 7, 3, 13
H = p - 1 - kap
def g(m, E): return min(p - m, E + m - kap - 1, E // 2)
def mof_mask(mask):
    m = 0; prev = (mask >> (k - 1)) & 1
    for i in range(k):
        cur = (mask >> i) & 1
        if cur and not prev: m += 1
        prev = cur
    return m
MOF = [mof_mask(mask) for mask in range(1 << k)]
st = Counter(); bad = []
seen = set()
for emp in itertools.combinations(range(k), 6):
    r = tuple(0 if i in emp else 1 for i in range(k))
    c = min(r[i:] + r[:i] for i in range(k))
    if c in seen: continue
    seen.add(c)
    r = list(r); R = sum(r)
    pref = [0] * (k + 1)
    for i in range(k): pref[i + 1] = pref[i] + r[i]
    forb = {}
    for i in range(k):
        for j in range(i + 1, k + 1):
            if j - i == k: continue
            E = pref[j] - pref[i]; lo = -g(1, R - E); hi = g(1, E)
            forb[(i, j)] = set(v % p for v in range(lo, hi + 1))
    gaps = [(g(1, r[t]) + 1, p - g(1, R - r[t]) - 1) for t in range(k)]
    masses = [sum(r[i] for i in range(k) if (mask >> i) & 1) for mask in range(1 << k)]
    U = [0] * (k + 1); loc = Counter(); sols = []
    def rep(t, ut):
        lo, hi = gaps[t]
        for v in range(lo, hi + 1):
            if (v - ut) % p == 0: return v
    def rec(j):
        if loc["nodes"] >= 20000: return
        loc["nodes"] += 1
        if j == k - 1:
            uk = (-U[k - 1]) % p
            if r[k - 1] == 0 and uk == 0: return
            UU = U[:k] + [0]
            for i in range(1, k):
                if (UU[k] - UU[i]) % p in forb[(i, k)]: return
            uu = [(UU[t + 1] - UU[t]) % p for t in range(k)]
            loc["sols"] += 1
            st["J=%d" % (sum(rep(t, uu[t]) for t in range(k)) // p - 1)] += 1
            if len(sols) < 30: sols.append(uu)
            return
        for uj in range(p):
            if r[j] == 0 and uj == 0: continue
            U[j + 1] = (U[j] + uj) % p
            if all((U[j + 1] - U[i]) % p not in forb[(i, j + 1)] for i in range(j + 1)):
                rec(j + 1)
    rec(0)
    st["run_data"] += 1; st["solutions"] += loc["sols"]
    for u in sols:
        usum = [0] * (1 << k)
        best = None
        for mask in range(1, 1 << k):
            low = mask & -mask; i = low.bit_length() - 1
            usum[mask] = (usum[mask ^ low] + u[i]) % p
        for mask in range(1, (1 << k) - 1):
            m = MOF[mask]; E = masses[mask]
            lo = -g(m, R - E); hi = g(m, E)
            if hi - lo + 1 >= p or any((v - usum[mask]) % p == 0 for v in range(lo, hi + 1)):
                if best is None or m < best: best = m
                if best == 2: break
        st["min_m=%s" % best] += 1
        if best is None:
            y = [0] * k; prev = 0
            for i in range(k):
                y[i] = (prev - 2 * u[i]) % p; prev = y[i]
            l = [1] * k; l[0] += 2 * H
            bad.append(dict(r=r, u=u, dp_solvable=dp.solvable(gwin.word_of(r, [0] * k, l, y, p), p)))
out = {"stats": dict(st), "unkilled": bad[:20]}
with open(os.path.join(HERE, "e13_regime3_p7.py"), "rb") as f:
    out["script_sha256"] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(HERE, "..", "out", "e13_regime3_p7.json"), "x") as f:
    json.dump(out, f, indent=0)
print(out["stats"], len(bad))

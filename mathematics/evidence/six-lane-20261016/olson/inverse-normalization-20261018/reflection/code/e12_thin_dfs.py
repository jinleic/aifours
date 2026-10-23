#!/usr/bin/env python3
"""E12 (plan-E12.md): DFS over interval-feasible assignments of one thin B = 0 datum; J statistics.  Output out/e12_thin_dfs.json (x)."""
import json, os, sys, hashlib
from collections import Counter
sys.setrecursionlimit(10000)
HERE = os.path.dirname(os.path.abspath(__file__))
p, kap = 13, 3
r = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
k = len(r); R = sum(r)
def g(m, E): return min(p - m, E + m - kap - 1, E // 2)
pref = [0] * (k + 1)
for i in range(k): pref[i + 1] = pref[i] + r[i]
forb = {}
for i in range(k):
    for j in range(i + 1, k + 1):
        if j - i == k: continue
        E = pref[j] - pref[i]
        lo = -g(1, R - E); hi = g(1, E)
        forb[(i, j)] = set(v % p for v in range(lo, hi + 1))
gaps = [(g(1, r[t]) + 1, p - g(1, R - r[t]) - 1) for t in range(k)]
def rep(t, ut):
    lo, hi = gaps[t]
    for v in range(lo, hi + 1):
        if (v - ut) % p == 0: return v
U = [0] * (k + 1); st = Counter(); leaves = []
def rec(j):
    if st["nodes"] >= 400000: return
    st["nodes"] += 1
    if j == k - 1:
        uk = (-U[k - 1]) % p
        if r[k - 1] == 0 and uk == 0: return
        UU = U[:k] + [0]
        for i in range(1, k):
            if (UU[k] - UU[i]) % p in forb[(i, k)]: return
        uu = [(UU[t + 1] - UU[t]) % p for t in range(k)]
        J = sum(rep(t, uu[t]) for t in range(k)) // p - 1
        st["J=%d" % J] += 1
        if len(leaves) < 20: leaves.append(uu)
        return
    for uj in range(p):
        if r[j] == 0 and uj == 0: continue
        U[j + 1] = (U[j] + uj) % p
        if all((U[j + 1] - U[i]) % p not in forb[(i, j + 1)] for i in range(j + 1)):
            rec(j + 1)
rec(0)
def killed(u):
    for mask in range(1, (1 << k) - 1):
        m = 0; prev = (mask >> (k - 1)) & 1
        for i in range(k):
            cur = (mask >> i) & 1
            if cur and not prev: m += 1
            prev = cur
        E = sum(r[i] for i in range(k) if (mask >> i) & 1)
        us = sum(u[i] for i in range(k) if (mask >> i) & 1) % p
        lo = -g(m, R - E); hi = g(m, E)
        if hi - lo + 1 >= p or any((v - us) % p == 0 for v in range(lo, hi + 1)):
            return m
    return None
kill_m = [killed(u) for u in leaves]
out = {"stats": dict(st), "first_leaves_kill_m": kill_m}
with open(os.path.join(HERE, "e12_thin_dfs.py"), "rb") as f:
    out["script_sha256"] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(HERE, "..", "out", "e12_thin_dfs.json"), "x") as f:
    json.dump(out, f, indent=0)
print(out)

#!/usr/bin/env python3
"""E9 (plan-E9.md): exploration for B = 0, k >= p + 1 (aid; no claim).  Output out/e9_b0l_probe.json (x)."""
import json, os, random, sys, hashlib
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
rng = random.Random(909)

def g1(p, kap, m, E):
    return min(p - m, E + m - kap - 1, E // 2)

def mof(P, k):
    if not P or len(P) == k: return 0
    return sum(1 for j in range(k) if (j in P) and ((j - 1) % k not in P))

def gen_b0l(p):
    for _ in range(2000):
        kap = rng.randint(2, p - 2)
        k = rng.randint(p + 1, min(2 * p - 1, p + 2 * kap))
        R = 2 * p - k + 2 * kap
        if R > 2 * p - 1 or R < 1: continue
        nE_min = max(1, k - R)
        if nE_min > min(2 * kap, k - 1): continue
        nE = rng.randint(nE_min, min(2 * kap, k - 1))
        nne = k - nE
        if nne > R or nne < 1: continue
        idx = list(range(k)); rng.shuffle(idx)
        ne = idx[:nne]
        r = [0] * k
        for t in ne: r[t] = 1
        mode = rng.random()
        for _ in range(R - nne):
            t = ne[0] if mode < 0.3 else rng.choice(ne)
            r[t] += 1
        eR = sum(1 for t in ne if r[t] % 2 == 0)
        if eR + nE > 2 * kap: continue
        return r, kap
    return None

def lifts(r, kap, p):
    k = len(r); R = sum(r)
    for attempt in range(80):
        V = [0] * (k + 1); V[k] = p; rho = 0
        for j in range(1, k):
            rho += r[j - 1]
            lo = -g1(p, kap, 1, R - rho); hi = g1(p, kap, 1, rho)
            if hi - lo + 1 >= p: return None, "full_prefix"
            V[j] = rng.randint(hi + 1, lo + p - 1)
        x = [V[t + 1] - V[t] for t in range(k)]
        u = [v % p for v in x]
        if any(r[t] == 0 and u[t] == 0 for t in range(k)): continue
        feas = True
        for a in range(k):
            E = 0; us = 0
            for L in range(1, k):
                t = (a + L - 1) % k; E += r[t]; us = (us + u[t]) % p
                lo = -g1(p, kap, 1, R - E); hi = g1(p, kap, 1, E)
                if hi - lo + 1 >= p or any((v - us) % p == 0 for v in range(lo, hi + 1)):
                    feas = False; break
            if not feas: break
        if feas: return x, "ok"
    return None, "no_feasible"

out = {"stats": {}, "nokill_examples": [], "step1_fail_examples": []}
st = Counter()
for p in (7, 11):
    made = 0; tries = 0
    while made < 400 and tries < 40000:
        tries += 1
        gd = gen_b0l(p)
        if gd is None: continue
        r, kap = gd
        x, why = lifts(r, kap, p)
        st[(p, why)] += 1
        if x is None: continue
        made += 1
        k = len(r); R = sum(r)
        s1 = all(x[t] >= -g1(p, kap, 1, R - r[t]) for t in range(k))
        st[(p, "step1", s1)] += 1
        if not s1 and len(out["step1_fail_examples"]) < 10:
            out["step1_fail_examples"].append(dict(p=p, r=r, kap=kap, x=x))
        if k <= 12:
            u = [v % p for v in x]
            mins = None; nk = 0
            for mask in range(1, (1 << k) - 1):
                P = set(i for i in range(k) if (mask >> i) & 1)
                m = mof(P, k); E = sum(r[i] for i in P)
                lo = -g1(p, kap, m, R - E); hi = g1(p, kap, m, E)
                up = sum(u[i] for i in P) % p
                if hi - lo + 1 >= p or any((v - up) % p == 0 for v in range(lo, hi + 1)):
                    nk += 1
                    if mins is None or m < mins: mins = m
            st[(p, "killed", nk > 0)] += 1
            if nk: st[(p, "min_m", mins)] += 1
            elif len(out["nokill_examples"]) < 10:
                out["nokill_examples"].append(dict(p=p, r=r, kap=kap, x=x))
out["stats"] = {str(k_): v for k_, v in st.items()}
with open(os.path.join(HERE, "e9_b0l_probe.py"), "rb") as f:
    out["script_sha256"] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(HERE, "..", "out", "e9_b0l_probe.json"), "x") as f:
    json.dump(out, f, indent=0)
for k_ in sorted(out["stats"]): print(k_, out["stats"][k_])
print("nokill", len(out["nokill_examples"]), "step1fail", len(out["step1_fail_examples"]))

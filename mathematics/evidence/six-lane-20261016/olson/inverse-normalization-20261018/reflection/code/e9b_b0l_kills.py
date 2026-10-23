#!/usr/bin/env python3
"""E9b (plan-E9b.md): classification of kills for B = 0, k >= p + 1 interval-feasible data (aid).  Output out/e9b_b0l_kills.json (x)."""
import json, os, random, sys, hashlib
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
rng = random.Random(9092)

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
            if hi - lo + 1 >= p: return None
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
        if feas: return x
    return None

out = {"stats": {}, "examples": {}}
st = Counter()
def note(key, ex=None):
    st[key] += 1
    if ex is not None and key not in out["examples"]:
        out["examples"][key] = ex
for p in (7, 11, 13):
    made = 0; tries = 0
    cap = {7: 300000, 11: 900000, 13: 900000}[p]
    while made < 300 and tries < cap:
        tries += 1
        gd = gen_b0l(p)
        if gd is None: continue
        r, kap = gd
        x = lifts(r, kap, p)
        if x is None: continue
        made += 1
        k = len(r); R = sum(r); u = [v % p for v in x]
        nE = sum(1 for t in range(k) if r[t] == 0)
        bh = [2 * x[t] - r[t] for t in range(k)]
        Z = [t for t in range(k) if bh[t] <= 0]
        def kills(P):
            P = set(P); m = mof(P, k); E = sum(r[i] for i in P)
            lo = -g1(p, kap, m, R - E); hi = g1(p, kap, m, E)
            up = sum(u[i] for i in P) % p
            return hi - lo + 1 >= p or any((v - up) % p == 0 for v in range(lo, hi + 1))
        def nonadj(a, b): return a != b and (a - b) % k not in (1, k - 1)
        PhiZ = sum(r[t] for t in Z) + 2 * mof(set(Z), k) - sum(bh[t] for t in Z)
        caseI = PhiZ >= 2 * kap + 2
        ex = dict(p=p, r=r, kap=kap, x=x)
        note((p, "caseI" if caseI else "caseII"))
        note((p, "k<=p+kap+1", k <= p + kap + 1))
        A_ = any(kills([a, b]) for a in Z for b in Z if a < b and nonadj(a, b))
        B_ = any(kills([a, b]) for a in Z for b in range(k) if b not in Z and nonadj(a, b))
        C_ = A_ or B_ or any(kills([a, b]) for a in range(k) for b in range(a + 1, k) if a not in Z and b not in Z and nonadj(a, b))
        note((p, "pair_defects", A_)); note((p, "pair_def_nondef", B_)); note((p, "any_pair", C_), None if C_ else ex)
        # two-interval patterns inside Z (m = 2)
        Dz = False
        zl = list(Z)
        if len(zl) <= 14:
            for mask in range(1, 1 << len(zl)):
                P = [zl[i] for i in range(len(zl)) if (mask >> i) & 1]
                if mof(set(P), k) == 2 and kills(P): Dz = True; break
        note((p, "m2_inside_Z", Dz))
        if caseI:
            P = set()
            for t in Z:
                P.add(t)
                if sum(r[i] for i in P) + 2 * mof(P, k) - sum(bh[i] for i in P) >= 2 * kap + 2: break
            note((p, "caseI_greedy_kills", kills(P)), None if kills(P) else ex)
        if k <= 12:
            anyk = False; m2 = False
            for mask in range(1, (1 << k) - 1):
                P = [i for i in range(k) if (mask >> i) & 1]
                if kills(P):
                    anyk = True
                    if mof(set(P), k) == 2: m2 = True; break
            note((p, "any_kill", anyk), None if anyk else ex); note((p, "m2_kill", m2))
    st[(p, "made")] = made; st[(p, "tries")] = tries
out["stats"] = {str(k_): v for k_, v in st.items()}
with open(os.path.join(HERE, "e9b_b0l_kills.py"), "rb") as f:
    out["script_sha256"] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(HERE, "..", "out", "e9b_b0l_kills.json"), "x") as f:
    json.dump(out, f, indent=0)
for k_ in sorted(out["stats"]): print(k_, out["stats"][k_])
print("examples", list(out["examples"].keys()))

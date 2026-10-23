#!/usr/bin/env python3
"""E11 (plan-E11.md): search for interval-feasible B = 0, k >= p + 1 data with sum of singleton reps != p.  Output out/e11_sigma_search.json (x)."""
import json, os, random, sys, hashlib
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
rng = random.Random(1111)

def g(p, kap, m, E):
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

def interval_feasible(r, u, p, kap):
    k = len(r); R = sum(r)
    for a in range(k):
        E = 0; us = 0
        for L in range(1, k):
            t = (a + L - 1) % k; E += r[t]; us = (us + u[t]) % p
            lo = -g(p, kap, 1, R - E); hi = g(p, kap, 1, E)
            if hi - lo + 1 >= p or any((v - us) % p == 0 for v in range(lo, hi + 1)):
                return False
    return True

out = {"stats": {}, "found": []}
st = Counter()
for p in (7, 11, 13):
    assigns = 0; data = 0
    while assigns < 2000000 and data < 200000:
        gd = gen_b0l(p)
        if gd is None: continue
        r, kap = gd; data += 1
        k = len(r); R = sum(r)
        gaps = []
        ok = True
        for t in range(k):
            lo = g(p, kap, 1, r[t]) + 1; hi = p - g(p, kap, 1, R - r[t]) - 1
            if lo > hi: ok = False; break
            gaps.append((lo, hi))
        if not ok: continue
        for trial in range(10):
            assigns += 1
            target = rng.choice([2 * p, 0])
            w = []
            biased = rng.random() < 0.5
            for t in range(k - 1):
                lo, hi = gaps[t]
                if biased and r[t] <= 2 * kap:
                    w.append(hi if target == 2 * p else lo)
                else:
                    w.append(rng.randint(lo, hi))
            last = target - sum(w)
            lo, hi = gaps[k - 1]
            if not (lo <= last <= hi): continue
            w.append(last)
            u = [v % p for v in w]
            if any(r[t] == 0 and u[t] == 0 for t in range(k)): continue
            st[(p, "candidate")] += 1
            if not interval_feasible(r, u, p, kap): continue
            st[(p, "sigma_violating_interval_feasible")] += 1
            # kill search
            killed2 = False; killed_any = None
            for mask in range(1, (1 << k) - 1):
                P = set(i for i in range(k) if (mask >> i) & 1)
                m = mof(P, k)
                if k > 14 and m != 2: continue
                E = sum(r[i] for i in P)
                lo2 = -g(p, kap, m, R - E); hi2 = g(p, kap, m, E)
                up = sum(u[i] for i in P) % p
                if hi2 - lo2 + 1 >= p or any((v - up) % p == 0 for v in range(lo2, hi2 + 1)):
                    if m == 2: killed2 = True
                    killed_any = True
                    if killed2: break
            rec = dict(p=p, r=r, kap=kap, w=w, sum_w=sum(w), killed_m2=killed2, killed_any=bool(killed_any))
            if p <= 11:
                y = [0] * k; prev = 0
                for i in range(k):
                    y[i] = (prev - 2 * u[i]) % p; prev = y[i]
                rec["dp_solvable"] = dp.solvable(gwin.word_of(r, [0] * k, [1] * (k - 1) + [1 + 2 * (p - 1 - kap)], y, p), p)
            if len(out["found"]) < 100: out["found"].append(rec)
            st[(p, "killed_m2", killed2)] += 1
    st[(p, "assignments")] = assigns; st[(p, "run_data")] = data
out["stats"] = {str(k_): v for k_, v in st.items()}
for k_ in sorted(out["stats"]): print(k_, out["stats"][k_])
with open(os.path.join(HERE, "e11_sigma_search.py"), "rb") as f:
    out["script_sha256"] = hashlib.sha256(f.read()).hexdigest()
with open(os.path.join(HERE, "..", "out", "e11_sigma_search.json"), "x") as f:
    json.dump(out, f, indent=0)
print("found", len(out["found"]))
for rec in out["found"][:5]: print(rec)

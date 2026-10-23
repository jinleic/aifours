#!/usr/bin/env python3
"""E10b (plan-E10b.md): residual-biased lift-first data for the MXG replay of e10_mxg_replay_v2.py (function reused)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
srcv2 = open(os.path.join(HERE, "e10_mxg_replay_v2.py")).read()
cut = srcv2.index("def gen(p):")
ns = {}
exec(compile(srcv2[:cut], "e10_mxg_replay_v2_head", "exec"), ns)
replay, Fail = ns["replay"], ns["Fail"]
rng = random.Random(1011)

def gen_resid(p):
    while True:
        k = rng.randint(5, p)
        g = rng.randint(1, (k - 2) // 2)
        Bmax = min(g, k - 1 - 2 * g)
        if Bmax < 1: continue
        B = rng.randint(1, Bmax)
        kap = g + B; H = p - 1 - kap
        if H < 0: continue
        Dt = 2 * p - k + 2 * g; A = Dt + B
        if A > 2 * p - 1: continue
        na = rng.randint(1, min(B, k - 2))
        ne = rng.randint(0, min(2 * g, k - na - 1))
        nal = k - na - ne
        if nal < 1 or nal > A: continue
        typ = ["al"] * nal + ["an"] * na + ["e"] * ne
        rng.shuffle(typ)
        d = [0] * k
        ali = [t for t in range(k) if typ[t] == "al"]; ani = [t for t in range(k) if typ[t] == "an"]
        for t in ali: d[t] = 1
        for t in ani: d[t] = -1
        for _ in range(A - nal): d[rng.choice(ali)] += 1
        for _ in range(B - na): d[rng.choice(ani)] -= 1
        # bh values: small, right parity
        bh = []
        for t in range(k):
            if typ[t] == "e":
                bh.append(rng.choice([-2, -2, 2, 2, 4, -4]))
            elif typ[t] == "an":
                c = -d[t]
                bh.append(rng.choice([-c, -c, -c + 2, -c - 2, 1 if c % 2 else 2]))
            else:
                bh.append(rng.choice([1, 1, 1, -1, 3]) if d[t] % 2 else rng.choice([0, 2, 0, -2]))
        diff = (k - 2 * g) - sum(bh)
        # repair the sum with parity-preserving steps of 2 on random runs
        if diff % 2: continue
        for _ in range(abs(diff) // 2):
            t = rng.randrange(k); bh[t] += 2 if diff > 0 else -2
        if any(typ[t] == "e" and bh[t] == 0 for t in range(k)): continue
        x = [(d[t] + bh[t]) // 2 for t in range(k)]
        if sum(x) != p: continue
        l = [1] * k; l[rng.randrange(k)] += 2 * H
        return d, l, x, g, B

def feasible(d, x, p, g, B):
    k = len(d); A = sum(v for v in d if v > 0); Bt = -sum(v for v in d if v < 0); Dt = A - Bt
    if Bt != B: return False
    def G(m, E): return min(p - m, E - g + m - 1, (E + Bt) // 2)
    if any(d[t] == 0 and x[t] % p == 0 for t in range(k)): return False
    for a in range(k):
        E = 0; xs = 0
        for L in range(1, k):
            t = (a + L - 1) % k; E += d[t]; xs += x[t]
            U = G(1, E); Lq = G(1, Dt - E)
            if U + Lq + 1 >= p or not (U + 1 <= xs <= p - Lq - 1): return False
    return True

res = {"kept": 0, "tried": 0, "stats": {}, "failures": [], "dp": {"checked": 0, "solvable": 0}, "by_p": {}}
for p in (11, 13, 17, 19, 23):
    kept = 0; tries = 0
    while kept < 3000 and tries < 3000000:
        tries += 1
        d, l, x, g, B = gen_resid(p)
        if not feasible(d, x, p, g, B): continue
        kept += 1
        try:
            name = replay(d, l, x, p, res["stats"])
        except Fail as e:
            res["failures"].append(dict(p=p, d=d, l=l, x=x, err=str(e))); name = "FAIL"
        bp = res["by_p"].setdefault(str(p), {}); bp[name] = bp.get(name, 0) + 1
        if p == 11 and kept % 3 == 0:
            k = len(d); u = [v % p for v in x]; y = [0] * k; prev = 0
            for i in range(k):
                y[i] = (prev - 2 * u[i]) % p; prev = y[i]
            a_ = [max(v, 0) for v in d]; b_ = [max(-v, 0) for v in d]
            res["dp"]["checked"] += 1; res["dp"]["solvable"] += dp.solvable(gwin.word_of(a_, b_, l, y, p), p)
    res["tried"] += tries; res["kept"] += kept
srcs = {}
for fn in ("dp.py", "gwin.py", "e10_mxg_replay_v2.py", "e10b_mxg_residual.py"):
    with open(os.path.join(HERE, fn), "rb") as f: srcs[fn] = hashlib.sha256(f.read()).hexdigest()
for fn in ("plan-E10b.md", "proof-MXG-r2.md"):
    with open(os.path.join(HERE, "..", fn), "rb") as f: srcs[fn] = hashlib.sha256(f.read()).hexdigest()
res["sources_sha256"] = srcs; res["failures"] = res["failures"][:200]
with open(os.path.join(HERE, "..", "out", "e10b_mxg_residual.json"), "x") as f:
    json.dump(res, f, indent=0)
print(json.dumps({k_: v for k_, v in res.items() if k_ not in ("failures", "sources_sha256")}))
print("failures", len(res["failures"]))
for fl in res["failures"][:5]: print(fl)

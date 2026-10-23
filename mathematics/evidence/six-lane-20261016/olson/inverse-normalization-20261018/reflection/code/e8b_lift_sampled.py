#!/usr/bin/env python3
"""E8b (plan-E8b.md): lift-sampled values; replay function copied verbatim from e8_b0s_replay.py.  Output out/e8b_lift_sampled.json (x)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
rng = random.Random(8081)

def gm(p, kap, m, E):
    return min(p - m, E + m - kap - 1, E // 2)

def m_of(P, k):
    inP = [i in P for i in range(k)]
    return sum(1 for j in range(k) if inP[j] and not inP[j - 1]) if 0 < len(P) < k else 0

def replay(r, l, y, p):
    """returns dict with outcome; r = run lengths (all rho_1), l odd blocks, y values; run i between block i-1 and block i."""
    k = len(r); R = sum(r); kap = p - 1 - sum(x // 2 for x in l)
    inv2 = (p + 1) // 2
    theta = [(y[(i - 1) % k] - y[i]) % p for i in range(k)]
    u = [(inv2 * th) % p for th in theta]
    def uP(P): return sum(u[i] for i in P) % p
    def window(P):
        m = m_of(P, k); E = sum(r[i] for i in P)
        return -gm(p, kap, m, R - E), gm(p, kap, m, E), m, E
    def hit(P):
        lo, hi, m, E = window(P)
        up = uP(P)
        return any((v - up) % p == 0 for v in range(lo, hi + 1)), lo, hi
    out = {"k": k, "R": R, "kappa": kap}
    # prefix lifts
    V = [0] * (k + 1); V[k] = p
    rho = 0
    for j in range(1, k):
        rho += r[j - 1]
        P = set(range(j))
        lo, hi, m, E = window(P)
        if hi - lo + 1 >= p:
            out["outcome"] = "full_window_prefix"; return out
        h, _, _ = hit(P)
        if h:
            out["outcome"] = "prefix_hit"; return out
        up = uP(P)
        # unique integer in [hi+1, lo+p-1] congruent to up
        cand = [v for v in range(hi + 1, lo + p) if (v - up) % p == 0]
        assert len(cand) == 1
        V[j] = cand[0]
    x = [V[t + 1] - V[t] for t in range(k)]
    bh = [2 * x[t] - r[t] for t in range(k)]
    assert sum(x) == p and sum(bh) == k - 2 * kap
    # Step 1
    step1 = True
    for t in range(k):
        Lt = gm(p, kap, 1, R - r[t]); Ut = gm(p, kap, 1, r[t])
        if x[t] < -Lt: step1 = False
        if bh[t] <= 0:
            if not (x[t] >= r[t] - kap + 1 and -bh[t] <= 2 * kap - 2 - r[t]):
                h, _, _ = hit({t})
                if h:
                    out["outcome"] = "singleton_hit"; return out
                step1 = False
    out["step1_ok"] = step1
    Z = [t for t in range(k) if bh[t] <= 0]
    assert Z and len(Z) < k
    def Phi(P):
        m = m_of(P, k); return sum(r[i] for i in P) + 2 * m - sum(bh[i] for i in P)
    def six(P):
        m = m_of(P, k); rhoP = sum(r[i] for i in P); dP = -sum(bh[i] for i in P)
        return (rhoP + 2 * m - dP <= 2 * p and rhoP + 2 * m + dP >= 2 * kap + 2 and dP >= 0 and
                dP + 2 * m - rhoP <= 2 * p and dP + rhoP - 2 * m <= 2 * R - 2 * kap - 2 and
                dP <= R - ((R - rhoP) % 2))
    PhiZ = Phi(set(Z))
    if PhiZ >= 2 * kap + 2:
        out["case"] = "I"
        P = set()
        for t in Z:
            P.add(t)
            if Phi(P) >= 2 * kap + 2: break
    else:
        out["case"] = "II"
        d = 2 * kap + 2 - PhiZ
        Zs = set(Z)
        adj = set()
        for t in Z:
            adj.add((t - 1) % k); adj.add((t + 1) % k)
        adj -= Zs
        Uset = [t for t in range(k) if t not in Zs and bh[t] == 1 and t not in adj]
        # maximal cyclic intervals of U, every second run
        inU = [t in Uset for t in range(k)]
        F = []
        if Uset:
            starts = [t for t in range(k) if inU[t] and not inU[t - 1]]
            for s0 in starts:
                t = s0; idx = 0
                while inU[t]:
                    if idx % 2 == 0: F.append(t)
                    idx += 1; t = (t + 1) % k
        out["F_size"] = len(F); out["deficit"] = d
        big = [y_ for y_ in F if r[y_] + 1 >= d]
        W = []
        if big:
            W = [big[0]]
        else:
            tot = 0
            for y_ in F:
                W.append(y_); tot += r[y_] + 1
                if tot >= d: break
        P = Zs | set(W)
        out["W"] = len(W)
        # mutation: swap one W item for an adjacent-to-Z bh=1 run
        mut = [t for t in adj if bh[t] == 1]
        if mut and W:
            Pm = (Zs | set(W[1:])) | {mut[0]}
            hm, _, _ = hit(Pm)
            out["mutation_kill"] = bool(hm and six(Pm))
    out["six_ok"] = six(P)
    h, lo, hi = hit(P)
    out["hit_ok"] = bool(h)
    xP = sum(x[i] for i in P)
    out["xP_in_window"] = lo <= xP <= hi
    out["outcome"] = "proof_pattern"
    return out


def lift_sampled(r, l, p):
    k = len(r); R = sum(r); kap = p - 1 - sum(x // 2 for x in l)
    for attempt in range(50):
        V = [0] * (k + 1); V[k] = p; rho = 0; ok = True
        for j in range(1, k):
            rho += r[j - 1]
            lo = -gm(p, kap, 1, R - rho); hi = gm(p, kap, 1, rho)
            if hi - lo + 1 >= p: return None
            V[j] = rng.randint(hi + 1, lo + p - 1)
        u = [(V[t + 1] - V[t]) % p for t in range(k)]
        if any(r[t] == 0 and u[t] == 0 for t in range(k)): continue
        theta = [(2 * ut) % p for ut in u]
        y = [0] * k; prev = 0
        for i in range(k):
            y[i] = (prev - theta[i]) % p; prev = y[i]
        return y
    return None

res = {"tally": {}, "case_by_p": {}, "failures": [], "dp": {"checked": 0, "solvable": 0}, "words": 0}
for p in (5, 7, 11, 13, 17, 19, 23, 29):
    made = 0; tries = 0
    while made < 500 and tries < 20000:
        tries += 1
        kap = rng.randint(1, (p - 1) // 2)
        k = rng.randint(2 * kap + 1, p)
        R = 2 * p - k + 2 * kap
        if R > 2 * p - 1: continue
        g = rng.randint(0, min(k - 1, 2 * kap))
        ne = rng.sample(range(k), k - g)
        if R < len(ne): continue
        rr = [0] * k
        for i in ne: rr[i] = 1
        mode = rng.random()
        for _ in range(R - len(ne)):
            if mode < 0.3: rr[ne[0]] += 1
            else: rr[rng.choice(ne)] += 1
        H = p - 1 - kap
        l = [1] * k; l[rng.randrange(k)] += 2 * H
        yv = lift_sampled(rr, l, p)
        if yv is None: continue
        if any(rr[i] == 0 and yv[i - 1] == yv[i] for i in range(k)): continue
        made += 1; res["words"] += 1
        o = replay(rr, l, yv, p)
        key = o["outcome"] + ("/" + o.get("case", "") if o["outcome"] == "proof_pattern" else "")
        res["tally"][key] = res["tally"].get(key, 0) + 1
        cp = res["case_by_p"].setdefault(str(p), {})
        cp[key] = cp.get(key, 0) + 1
        if o["outcome"] == "proof_pattern" and not (o["six_ok"] and o["hit_ok"] and o["xP_in_window"] and o.get("step1_ok", True)):
            res["failures"].append(dict(p=p, r=rr, l=l, y=yv, o=o))
        if p <= 11:
            res["dp"]["checked"] += 1; res["dp"]["solvable"] += dp.solvable(gwin.word_of(rr, [0] * k, l, yv, p), p)
srcs = {}
for fn in ("dp.py", "gwin.py", "e8_b0s_replay.py", "e8b_lift_sampled.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
for fn in ("plan-E8b.md", "proof-B0S-r1.md"):
    with open(os.path.join(HERE, "..", fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
res["sources_sha256"] = srcs
with open(os.path.join(HERE, "..", "out", "e8b_lift_sampled.json"), "x") as f:
    json.dump(res, f, indent=0)
print(json.dumps({k_: v for k_, v in res.items() if k_ not in ("failures", "sources_sha256")}))
print("failures", len(res["failures"]))

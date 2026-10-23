#!/usr/bin/env python3
"""E10 (plan-E10.md): replay of Theorem MXG (proof-MXG-r2.md).  v2: SPLIT orientation rule fixed by inspection before any run
(v1 e10_mxg_replay.py b133d8d5... never run).  Output out/e10_mxg_replay.json (exclusive create)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
rng = random.Random(1010)

class Fail(Exception):
    pass

def mof(P, k):
    if not P or len(P) == k: return 0
    return sum(1 for j in range(k) if (j in P) and ((j - 1) % k not in P))

def replay(d, l, x, p, stats):
    k = len(d); A = sum(v for v in d if v > 0); B = -sum(v for v in d if v < 0)
    H = sum(v // 2 for v in l); kap = p - 1 - H; g = kap - B; Dt = A - B
    s = k - 1 - 2 * g - B
    assert g >= 1 and B >= 1 and A >= B and s >= 0 and k <= p
    u = [v % p for v in x]
    def G(m, E): return min(p - m, E - g + m - 1, (E + B) // 2)
    def DP_(P): return sum(d[i] for i in P)
    def window(P):
        m = mof(P, k); E = DP_(P); return -G(m, Dt - E), G(m, E), m
    def hit(P):
        lo, hi, m = window(P)
        if hi - lo + 1 >= p: return True
        up = sum(u[i] for i in P) % p
        return any((v - up) % p == 0 for v in range(lo, hi + 1))
    phi = [d[t] - x[t] for t in range(k)]
    bh = [2 * x[t] - d[t] for t in range(k)]
    assert sum(x) == p and sum(bh) == k - 2 * g
    def c(P): return sum(phi[i] for i in P) + mof(P, k)
    def BH(P): return sum(bh[i] for i in P)
    def Phi(P): return DP_(P) - BH(P) + 2 * mof(P, k)
    def KL(S, name):
        S = set(S)
        if not (0 < len(S) < k): raise Fail(name + ": S not proper")
        if any(phi[i] > g - 1 for i in S): raise Fail(name + ": phi > g-1 on S")
        if c(S) < g + 1: raise Fail(name + ": c(S) < g+1")
        if BH(S) > B: raise Fail(name + ": BH(S) > B")
        order = sorted(S, key=lambda i: (bh[i] > 0, i))
        P = set()
        for i in order:
            P.add(i)
            if c(P) >= g + 1: break
        cp = c(P)
        if not (g + 1 <= cp <= 2 * g and BH(P) <= B and DP_(P) >= -B): raise Fail(name + ": KL prefix bounds")
        lo, hi, m = window(P)
        xp = sum(x[i] for i in P)
        if not (lo <= xp <= hi): raise Fail(name + ": x(P) not in I(P)")
        if not hit(P): raise Fail(name + ": no hit")
        stats[name] = stats.get(name, 0) + 1
        return name
    empt = [t for t in range(k) if d[t] == 0]
    al = [t for t in range(k) if d[t] > 0]
    anti = [t for t in range(k) if d[t] < 0]
    for t in empt:
        if x[t] == 0: raise Fail("genuine")
    # GIANT
    T = [t for t in range(k) if d[t] >= 2 * p - 1]
    if T:
        return KL(empt, "GIANT")
    Z0 = [t for t in range(k) if bh[t] <= 0]; Zs = set(Z0)
    Y = [t for t in range(k) if t not in Zs]
    m = mof(Zs, k)
    PhiZ = Phi(Zs)
    for t in Z0:
        if d[t] - bh[t] > 2 * g - 2: raise Fail("defect f > 2g-2")
    for t in al:
        if bh[t] == 1 and d[t] > 2 * g - 1: raise Fail("filler d > 2g-1")
    Yal = [t for t in Y if d[t] > 0]; YE = [t for t in Y if d[t] == 0]; Yan = [t for t in Y if d[t] < 0]
    aZ = sum(d[t] - 1 for t in Z0)
    def lemmaG(F, name):
        Pstar_order = list(Z0) + list(F)
        P = set()
        for i in Pstar_order:
            P.add(i)
            if Phi(P) >= 2 * g + 2: break
        if Phi(P) < 2 * g + 2: raise Fail(name + ": Phi never reached")
        if not (Phi(P) <= 4 * g + 1 and BH(P) <= B and DP_(P) >= -B and 0 < len(P) < k): raise Fail(name + ": G prefix bounds")
        lo, hi, mm = window(P)
        xp = sum(x[i] for i in P)
        if not (lo <= xp <= hi): raise Fail(name + ": x(P) not in I(P)")
        if not hit(P): raise Fail(name + ": no hit")
        stats[name] = stats.get(name, 0) + 1
        return name
    if PhiZ >= 2 * g + 2:
        return lemmaG([], "MIXR_PhiZ")
    if PhiZ % 2: raise Fail("Phi odd")
    j = (2 * g + 2 - PhiZ) // 2
    if len(Yal) + len(YE) + aZ >= 2:
        # gaps and interior fillers
        inZ = [t in Zs for t in range(k)]
        starts = [t for t in range(k) if not inZ[t] and inZ[(t - 1) % k]]
        F = []
        for s0 in starts:
            gap = []; t = s0
            while not inZ[t]:
                gap.append(t); t = (t + 1) % k
            inter = gap[1:-1]
            seg = []
            for t in inter + [None]:
                if t is not None and d[t] > 0 and bh[t] == 1:
                    seg.append(t)
                else:
                    F.extend(seg[0::2]); seg = []
        if len(F) < j: raise Fail("AV: not enough fillers")
        return lemmaG(F[:j], "MIXR_AV")
    stats["R*_G"] = stats.get("R*_G", 0) + 1
    cheap = [t for t in range(k) if phi[t] >= 0 and bh[t] <= 1]
    cheapS = set(cheap)
    for t in cheap:
        if phi[t] > g - 1: raise Fail("cheap phi > g-1")
    def W(P): return sum(phi[i] + 1 for i in P)
    # W
    if B >= g + 1:
        if len(cheap) < k:
            inC = [t in cheapS for t in range(k)]
            st = [t for t in range(k) if inC[t] and not inC[(t - 1) % k]]
            U = []
            for s0 in st:
                blk = []; t = s0
                while inC[t]:
                    blk.append(t); t = (t + 1) % k
                a, b = blk[0::2], blk[1::2]
                U.extend(a if W(a) >= W(b) else b)
        else:
            path = list(range(1, k))
            a, b = path[0::2], path[1::2]
            U = a if W(a) >= W(b) else b
        U.sort(key=lambda i: -(phi[i] + 1))
        S = []
        for i in U:
            S.append(i)
            if W(S) >= g + 1: break
        return KL(S, "W")
    # B1
    T = [t for t in range(k) if d[t] >= 2 * p - B]
    if T:
        T0 = T[0]
        path = [(T0 + i) % k for i in range(1, k)]
        a, b = path[0::2], path[1::2]
        X = a if W(a) >= W(b) else b
        S = [t for t in X if phi[t] >= 0]
        return KL(S, "B1")
    def split(C, name):
        Cs = set(C); E = [t for t in C if d[t] == 0]; Es = set(E)
        Cp = [t for t in C if t not in Es]; Cps = set(Cp)
        if not (0 < len(Cs) < k): raise Fail(name + ": SPLIT C")
        inCp = [t in Cps for t in range(k)]
        st = [t for t in range(k) if inCp[t] and not inCp[(t - 1) % k]]
        blocks = []
        for s0 in st:
            blk = []; t = s0
            while inCp[t]:
                blk.append(t); t = (t + 1) % k
            blocks.append(blk)
        def lam(cls):
            v = len(cls)
            for t in cls:
                v -= ((t - 1) % k in Es) + ((t + 1) % k in Es)
            return v
        Up, Vp = [], []; diff = 0
        for blk in blocks:
            a, b = blk[0::2], blk[1::2]
            da = lam(a) - lam(b)
            if abs(da) > 1: raise Fail(name + ": block difference > 1")
            if abs(diff + da) <= 1:
                Up.extend(a); Vp.extend(b); diff += da
            else:
                Up.extend(b); Vp.extend(a); diff -= da
            if abs(diff) > 1: raise Fail(name + ": orientation")
        Us, Vs = set(Up) | Es, set(Vp) | Es
        need = (len(Cs) + len(Es)) // 2
        if min(c(Us), c(Vs)) < need: raise Fail(name + ": SPLIT c bound")
        if BH(Us) + BH(Vs) != BH(Cs) + BH(Es): raise Fail(name + ": SPLIT BH identity")
        # control: plain alternating split of C (no doubling)
        inC = [t in Cs for t in range(k)]
        st2 = [t for t in range(k) if inC[t] and not inC[(t - 1) % k]]
        U2, V2 = [], []
        for s0 in st2:
            blk = []; t = s0
            while inC[t]:
                blk.append(t); t = (t + 1) % k
            a, b = blk[0::2], blk[1::2]
            if len(U2) <= len(V2): U2.extend(a); V2.extend(b)
            else: U2.extend(b); V2.extend(a)
        ok2 = any(c(set(Q)) >= g + 1 and BH(set(Q)) <= B for Q in (U2, V2) if Q)
        stats["split_uses"] = stats.get("split_uses", 0) + 1
        if not ok2: stats["plain_split_fails"] = stats.get("plain_split_fails", 0) + 1
        for Q in (Us, Vs):
            if BH(Q) <= B and c(Q) >= g + 1:
                return KL(Q, name)
        raise Fail(name + ": neither half")
    Tb = [t for t in range(k) if bh[t] >= B + 1]
    if Tb:
        return split(cheap, "A")
    nEZ = sum(1 for t in Z0 if d[t] == 0)
    if len(cheap) == k:
        if B + s + nEZ >= 2:
            fill = [t for t in range(k) if bh[t] == 1]
            if not fill: raise Fail("AC: no filler")
            return split([t for t in range(k) if t != fill[0]], "AC")
        if k % 2: raise Fail("AC: k odd")
        O = list(range(0, k, 2)); Ev = list(range(1, k, 2))
        return KL(O if BH(O) <= B else Ev, "AC_par")
    free = [t for t in range(k) if phi[t] >= 0 and bh[t] <= 0]
    alpha = sum(1 for t in free if d[t] < 0)
    SZ = sum(d[t] - 1 for t in Z0 if d[t] > 0)
    X = sum(phi[t] for t in free)
    if 2 * X + alpha <= 2 * g + s - 1 + SZ:
        return split(cheap, "KS")
    if c(set(free)) >= g + 1:
        return KL(free, "ZP")
    Tc = [t for t in range(k) if bh[t] >= s + 1]
    if Tc:
        return KL([t for t in range(k) if t != Tc[0]], "C")
    # R4'
    stats["R4"] = stats.get("R4", 0) + 1
    if not all(phi[t] <= g - 1 for t in range(k)): raise Fail("R4 (i)")
    Ys = set(Y)
    inY = [t in Ys for t in range(k)]
    st = [t for t in range(k) if inY[t] and not inY[(t - 1) % k]]
    Q = []
    for s0 in st:
        blk = []; t = s0
        while inY[t]:
            blk.append(t); t = (t + 1) % k
        a, b = blk[0::2], blk[1::2]
        Q.extend(a if BH(a) >= BH(b) else b)
    N = []
    for t in Q:
        N.append(t)
        if BH(N) >= s + 1: break
    if BH(N) < s + 1: raise Fail("R4 N")
    if sum(phi[t] for t in N) <= (p - k + g - 1) + len(N):
        return KL([t for t in range(k) if t not in set(N)], "R4a")
    return KL(set(free) | set(N), "R4b")

def gen(p):
    while True:
        k = rng.randint(4, p)
        B = rng.randint(1, max(1, (k - 3) // 1))
        g = rng.randint(1, max(1, (k - 1 - B) // 2))
        if 2 * g + B > k - 1: continue
        kap = g + B; H = p - 1 - kap
        if H < 0: continue
        Dt = 2 * p - k + 2 * g; A = Dt + B
        if A > 2 * p - 1: continue
        na = rng.randint(1, min(B, k - 1))
        ne = rng.randint(0, k - na - 1)
        nal = k - na - ne
        if nal < 1 or nal > A: continue
        dd = [0] * k
        idx = list(range(k)); rng.shuffle(idx)
        ali, ani = idx[:nal], idx[nal:nal + na]
        for t in ali: dd[t] = 1
        for t in ani: dd[t] = -1
        mode = rng.random()
        for _ in range(A - nal):
            t = ali[0] if mode < 0.25 else rng.choice(ali)
            dd[t] += 1
        for _ in range(B - na):
            dd[rng.choice(ani)] -= 1
        l = [1] * k; l[rng.randrange(k)] += 2 * H
        return dd, l, g, B

def lifts(dd, p, g, B, bias):
    k = len(dd); A = sum(v for v in dd if v > 0); Bt = -sum(v for v in dd if v < 0); Dt = A - Bt
    def G(m, E): return min(p - m, E - g + m - 1, (E + Bt) // 2)
    gaps = []
    for t in range(k):
        lo = G(1, dd[t]) + 1; hi = p - G(1, Dt - dd[t]) - 1
        if lo > hi: return None
        gaps.append((lo, hi))
    for attempt in range(40):
        x = []
        for t in range(k - 1):
            lo, hi = gaps[t]
            if rng.random() < bias:
                tgt = (dd[t] + rng.choice([-2, -1, 0, 1])) // 2 if dd[t] != 0 else rng.choice([-1, -2, 1])
                v = min(max(tgt, lo), hi)
            else:
                v = rng.randint(lo, hi)
            x.append(v)
        xl = p - sum(x)
        lo, hi = gaps[k - 1]
        if not (lo <= xl <= hi): continue
        x.append(xl)
        if any(dd[t] == 0 and x[t] == 0 for t in range(k)): continue
        # interval feasibility
        ok = True
        for a in range(k):
            E = 0; xs = 0
            for L in range(1, k):
                t = (a + L - 1) % k
                E += dd[t]; xs += x[t]
                U = G(1, E); Lq = G(1, Dt - E)
                if U - (-Lq) + 1 >= p or not (U + 1 <= xs <= p - Lq - 1):
                    ok = False; break
            if not ok: break
        if ok: return x
    return None

res = {"kept": 0, "tried": 0, "stats": {}, "failures": [], "dp": {"checked": 0, "solvable": 0}, "by_p": {}}
for p in (7, 11, 13, 17, 19, 23):
    kept = 0; tries = 0
    while kept < 2500 and tries < 400000:
        tries += 1
        dd, l, g, B = gen(p)
        x = lifts(dd, p, g, B, bias=0.7)
        if x is None: continue
        kept += 1
        try:
            name = replay(dd, l, x, p, res["stats"])
        except Fail as e:
            res["failures"].append(dict(p=p, d=dd, l=l, x=x, err=str(e)))
            name = "FAIL"
        bp = res["by_p"].setdefault(str(p), {})
        bp[name] = bp.get(name, 0) + 1
        if p <= 11 and kept % 5 == 0:
            k = len(dd)
            u = [v % p for v in x]
            y = [0] * k; prev = 0
            for i in range(k):
                y[i] = (prev - 2 * u[i]) % p; prev = y[i]
            a_ = [max(v, 0) for v in dd]; b_ = [max(-v, 0) for v in dd]
            res["dp"]["checked"] += 1
            res["dp"]["solvable"] += dp.solvable(gwin.word_of(a_, b_, l, y, p), p)
    res["tried"] += tries; res["kept"] += kept
srcs = {}
for fn in ("dp.py", "gwin.py", "e10_mxg_replay.py", "e10_mxg_replay_v2.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
for fn in ("plan-E10.md", "proof-MXG-r2.md"):
    with open(os.path.join(HERE, "..", fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
res["sources_sha256"] = srcs
res["failures"] = res["failures"][:200]
with open(os.path.join(HERE, "..", "out", "e10_mxg_replay.json"), "x") as f:
    json.dump(res, f, indent=0)
print(json.dumps({k_: v for k_, v in res.items() if k_ not in ("failures", "sources_sha256")}))
print("failures", len(res["failures"]))
for fl in res["failures"][:5]: print(fl)

#!/usr/bin/env python3
"""E5: replays of the new lemmas of proof-RED-r1.md on random instances (aids only):
  K1*  (all-odd, kappa = 1, B = 0, empty runs): single-run BC' certificate (a), (b), (c);
  KB*  (all-odd, B = kappa >= 1, k <= p, uncapped, empty runs allowed): single-run BC certificate;
  CAP  (capped shape with an empty run): the empty-run singleton window is full;
  KBH* (B = kappa >= 1, o_F >= p + 1, any parities, empty runs): KBH greedy theta and the Lemma ZS hypothesis;
  TR   exactness on near-avoiders at shorter lengths (raw DP before/after, both directions).
Raw DP (dp1 + dp2) confirms solvability for p <= 11 in K1*, KB*, CAP, KBH*.  Output: out/e5_red_replay.json (x)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin
rng = random.Random(31337)

def lamQ(Q, a, b, l, p):
    return gwin.lam(sorted(Q), a, b, l, p)

def uQ(Q, y, p):
    k = len(y); inv2 = (p + 1) // 2
    return (inv2 * sum((y[(i - 1) % k] - y[i]) for i in Q)) % p

def lamp(Q, a, b, l, y, p):
    v = lamQ(Q, a, b, l, p)
    if v == 0 and uQ(Q, y, p) != 0:
        return 1
    return v

def bc_single_runs(a, b, l, y, p, boost):
    k = len(a); allr = set(range(k))
    L = (lambda Q: lamp(Q, a, b, l, y, p)) if boost else (lambda Q: lamQ(Q, a, b, l, p))
    parts = [[i] for i in range(k)]
    sa = sum(L(P) for P in parts)
    okb = True
    for t in range(1, k - 1):
        X = set(range(t)); Y = {t}; Z = allr - X - Y
        if L(X | Y) + L(Y | Z) + L(Z | X) < p + 1 or L(X) + L(Y) + L(Z) < 1:
            okb = False
    okc = L({k - 1}) + L(allr - {k - 1}) >= 1
    return sa, sa >= p + 1, okb, okc

def rand_values(k, a, b, p):
    y = [rng.randrange(p) for _ in range(k)]
    for i in range(k):
        if a[i] + b[i] == 0:
            while y[(i - 1) % k] == y[i]:
                y[i] = rng.randrange(p)
    for i in range(k):
        if a[i] + b[i] == 0 and y[(i - 1) % k] == y[i]:
            return None
    return y

def odd_blocks(k, H):
    l = [1] * k
    for _ in range(H):
        l[rng.randrange(k)] += 2
    return l

out = {}
# K1*: kappa = 1, B = 0, all odd
st = dict(n=0, cert_ok=0, dp_checked=0, dp_solvable=0)
for p in (5, 7, 11, 13, 17, 19, 23, 29, 31):
    kap = 1; H = p - 1 - kap
    for trial in range(80):
        k = rng.randint(3, p + 2)
        R = 2 * p - k + 2 * kap
        g = rng.randint(1, 2)
        if k - g > R or g >= k: continue
        ne = rng.sample(range(k), k - g)
        r = [0] * k
        for i in ne: r[i] = 1
        for _ in range(R - (k - g)): r[rng.choice(ne)] += 1
        a = r; b = [0] * k; l = odd_blocks(k, H)
        e_R = sum(1 for x in r if x % 2 == 0)
        if e_R > 2: continue          # (P0) would make it solvable anyway; replay the proof's setting only
        y = rand_values(k, a, b, p)
        if y is None: continue
        st["n"] += 1
        sa, oa, ob, oc = bc_single_runs(a, b, l, y, p, True)
        st["cert_ok"] += (oa and ob and oc)
        if p <= 11:
            st["dp_checked"] += 1; st["dp_solvable"] += dp.solvable(gwin.word_of(a, b, l, y, p), p)
out["K1star"] = st
# KB*: B = kappa >= 1, all odd, k <= p, uncapped, empty runs allowed, runs arbitrary
st = dict(n=0, cert_ok=0, dp_checked=0, dp_solvable=0, capped_skipped=0)
for p in (5, 7, 11, 13, 17, 19, 23):
    for trial in range(120):
        kap = rng.randint(1, p - 2); H = p - 1 - kap; B = kap
        k = rng.randint(kap + 1, p)
        R = 2 * p - k + 2 * kap; A = R - B
        if A < B or A > 2 * p - 1 or R < 1: continue
        g = rng.randint(1, max(1, min(k - 1, 2 * kap)))
        ne = rng.sample(range(k), k - g)
        if R < len(ne): continue
        r = [0] * k
        for i in ne: r[i] = 1
        for _ in range(R - len(ne)): r[rng.choice(ne)] += 1
        # split rotations: total B letters rho_-1
        bb = [0] * k; left = B
        pos = [i for i in ne for _ in range(r[i])]
        rng.shuffle(pos)
        for i in pos[:B]: bb[i] += 1
        a = [r[i] - bb[i] for i in range(k)]; b = bb
        d = [a[i] - b[i] for i in range(k)]
        if max(d) >= 2 * p - 1:
            st["capped_skipped"] += 1; continue
        l = odd_blocks(k, H)
        y = rand_values(k, a, b, p)
        if y is None: continue
        st["n"] += 1
        sa, oa, ob, oc = bc_single_runs(a, b, l, y, p, False)
        st["cert_ok"] += (oa and ob and oc)
        if p <= 11:
            st["dp_checked"] += 1; st["dp_solvable"] += dp.solvable(gwin.word_of(a, b, l, y, p), p)
out["KBstar"] = st
# CAP: one run rho_1^(2p-1), other runs rho_-1^b (sum k-1), at least one empty; B = kappa = k-1; k <= p
st = dict(n=0, full=0, dp_checked=0, dp_solvable=0)
for p in (5, 7, 11, 13, 17, 19, 23):
    for trial in range(60):
        k = rng.randint(2, p); kap = k - 1; H = p - 1 - kap
        if H < 0: continue
        others = list(range(1, k))
        bvals = [0] * k
        for _ in range(k - 1):
            bvals[rng.choice(others)] += 1
        if all(bvals[i] > 0 for i in others):
            j = rng.choice(others); i2 = rng.choice([x for x in others if x != j]) if len(others) > 1 else None
            if i2 is None: continue
            bvals[i2] += bvals[j]; bvals[j] = 0
        a = [2 * p - 1] + [0] * (k - 1); b = bvals
        l = odd_blocks(k, H)
        y = rand_values(k, a, b, p)
        if y is None: continue
        t = [i for i in range(k) if a[i] + b[i] == 0][0]
        st["n"] += 1
        lt = lamQ([t], a, b, l, p); lc = lamQ([i for i in range(k) if i != t], a, b, l, p)
        st["full"] += (lt + lc - 1 >= p)
        if p <= 11:
            st["dp_checked"] += 1; st["dp_solvable"] += dp.solvable(gwin.word_of(a, b, l, y, p), p)
out["CAP"] = st
# KBH*: B = kappa >= 1, o_F >= p + 1, any parities; greedy theta and ZS check
def kbh_check(a, b, l, p):
    k = len(a); A = sum(a); B = sum(b); kap = gwin.kappa_of(l, p); assert B == kap
    odd = [j for j in range(k) if l[j] % 2]
    o = len(odd)
    # segments: runs strictly between consecutive odd blocks; block j lies between run j and run j+1
    segs = []
    for idx in range(o):
        j0 = odd[idx]; j1 = odd[(idx + 1) % o]
        seg = []; r = (j0 + 1) % k
        while True:
            seg.append(r)
            if r == j1: break
            r = (r + 1) % k
        segs.append(seg)
    dG = [sum(a[i] - b[i] for i in s) for s in segs]
    Dt = A - B
    def lo(x): return max(0, -((-(x - B)) // 2), x - p + 1)
    def UQ(x): return min(p - 1, x, (x + B) // 2)
    def LQ(x): return min(p - 1, Dt - x, (Dt - x + B) // 2)
    W = list(range(p))  # first p segments
    theta = []
    for j in range(1, p + 1):
        best = 0
        for i in range(0, j):
            DQ = sum(dG[W[s]] for s in range(i, j))
            prev = sum(theta[i:j - 1])
            best = max(best, lo(DQ) - prev)
        theta.append(max(0, best))
    tau = [dG[W[i]] - theta[i] for i in range(p)]
    ok = True
    for i in range(p):
        for j in range(i + 1, p + 1):
            DQ = sum(dG[W[s]] for s in range(i, j)); ts = sum(tau[i:j])
            if not (-LQ(DQ) <= ts <= UQ(DQ)):
                ok = False
    return ok, o
st = dict(n=0, zs_ok=0, dp_checked=0, dp_solvable=0)
for p in (5, 7, 11, 13):
    for trial in range(150):
        kap = rng.randint(1, p - 2); B = kap; H = p - 1 - kap
        # o_F >= p + 1 odd blocks plus some even blocks; F = 2H + o
        o = rng.randint(p + 1, 2 * p)
        F = 2 * H + o
        R = 4 * p - 2 - F
        A = R - B
        if A < B or A > 2 * p - 1 or R < 1: continue
        ne_ = rng.randint(0, 2)       # number of even blocks
        if 2 * ne_ > 2 * H: ne_ = H
        k = o + ne_
        par = [1] * o + [0] * ne_
        rng.shuffle(par)
        l = [1 if q else 2 for q in par]
        extra = H - ne_
        if extra < 0: continue
        oddidx = [i for i in range(k) if par[i]]
        for _ in range(extra): l[rng.randrange(k)] += 2
        if sum(x // 2 for x in l) != H: continue
        # runs: k runs with R rotations, some empty
        g = rng.randint(1, k - 1)
        ne = rng.sample(range(k), k - g)
        if R < len(ne): continue
        r = [0] * k
        for i in ne: r[i] = 1
        for _ in range(R - len(ne)): r[rng.choice(ne)] += 1
        pos = [i for i in ne for _ in range(r[i])]; rng.shuffle(pos)
        bb = [0] * k
        for i in pos[:B]: bb[i] += 1
        a = [r[i] - bb[i] for i in range(k)]; b = bb
        y = rand_values(k, a, b, p)
        if y is None: continue
        st["n"] += 1
        ok, o_ = kbh_check(a, b, l, p)
        st["zs_ok"] += ok
        if p <= 11:
            st["dp_checked"] += 1; st["dp_solvable"] += dp.solvable(gwin.word_of(a, b, l, y, p), p)
out["KBHstar"] = st
# TR exactness on near-avoiders (shorter lengths)
st = dict(pairs=0, no_before=0, mismatch=0)
for trial in range(4000):
    p = rng.choice((5, 7))
    n = rng.choice((3 * p, 3 * p + 2, 4 * p - 6, 4 * p - 5))
    k = rng.randint(2, 6)
    F = rng.randint(k, n - 2)
    l = [1] * k
    for _ in range(F - k): l[rng.randrange(k)] += 1
    Rr = n - F
    empty = [rng.random() < 0.3 for _ in range(k)]
    if all(empty): continue
    nei = [i for i in range(k) if not empty[i]]
    if Rr < len(nei) + 1: continue
    r = [0] * k
    for i in nei: r[i] = 1
    for _ in range(Rr - len(nei)): r[rng.choice(nei)] += 1
    a = list(r); b = [0] * k
    s = rng.choice(nei)
    if r[s] < 2: continue
    b[s] = rng.randint(1, r[s] - 1); a[s] = r[s] - b[s]
    y = [rng.randrange(min(p, 3)) for _ in range(k)]
    if any(empty[i] and y[i - 1] == y[i] for i in range(k)): continue
    t = rng.choice([i for i in range(k) if i != s])
    w1 = gwin.word_of(a, b, l, y, p)
    a2 = list(a); b2 = list(b); a2[s] -= 1; b2[s] -= 1; a2[t] += 1; b2[t] += 1
    w2 = gwin.word_of(a2, b2, l, y, p)
    x1 = dp.solvable(w1, p); x2 = dp.solvable(w2, p)
    st["pairs"] += 1; st["no_before"] += (not x1); st["mismatch"] += (x1 != x2)
out["TR"] = st
srcs = {}
for fn in ("dp.py", "gwin.py", "e5_red_replay.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
out["sources_sha256"] = srcs
with open(os.path.join(HERE, "..", "out", "e5_red_replay.json"), "x") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=0))

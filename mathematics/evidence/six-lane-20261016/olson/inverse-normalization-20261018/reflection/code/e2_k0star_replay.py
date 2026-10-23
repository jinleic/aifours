#!/usr/bin/env python3
"""E2 (parts A, B, D): replay of Step 5 of Theorem K0* (proof-K0star-r1.md) on random words in the four configurations,
p = 5..31; exact BC' inequalities (a), (b), (c) with Lemma H0 lambdas; GR0-vs-H0 interval algebra on every pattern used;
raw DP (dp1 and dp2) on the explicit word for p <= 11 (must be SOLVABLE); mutation: without the boost, (a) must fail in C1a
and C2a.  Output: out/e2_k0star_replay.json (exclusive create)."""
import json, os, random, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import dp, gwin

rng = random.Random(77)

def blocks_with(p, parities):
    """random block lengths with the given parity list (1 = odd, 0 = even, even blocks >= 2) and sum floor(l/2) = p - 1"""
    k = len(parities)
    base = [1 if q else 2 for q in parities]
    H0 = sum(x // 2 for x in base)
    extra = p - 1 - H0
    if extra < 0:
        return None
    l = list(base)
    for _ in range(extra):
        l[rng.randrange(k)] += 2
    return l

def runs_with(R, parities_nonempty):
    """nonempty run lengths with the given parities summing to R (or None)"""
    n = len(parities_nonempty)
    base = [1 if q else 2 for q in parities_nonempty]
    rest = R - sum(base)
    if rest < 0 or rest % 2:
        return None
    r = list(base)
    for _ in range(rest // 2):
        r[rng.randrange(n)] += 2
    return r

def make(p, conf):
    """returns (a, b, l, y, t, parts) for configuration conf; runs indexed 0..k-1, run i before block i."""
    for attempt in range(200):
        oF = rng.randint(1, p)
        if conf == 'C1a':
            k = oF + 1; t = rng.randrange(k); even_after = rng.random() < 0.5
            par = [1] * k
            if even_after: par[t] = 0
            else: par[(t - 1) % k] = 0
            nonempty = [i for i in range(k) if i != t]; npar = [1] * len(nonempty)
        elif conf == 'C1b':
            k = oF + 2; t = rng.randrange(k)
            par = [1] * k; par[t] = 0; par[(t - 1) % k] = 0
            nonempty = [i for i in range(k) if i != t]; npar = [1] * len(nonempty)
            npar[rng.randrange(len(npar))] = 0
        elif conf in ('C2a', 'C2a_mirror'):
            k = oF + 2; t = rng.randrange(k)
            par = [1] * k; par[t] = 0
            if conf == 'C2a': par[(t + 1) % k] = 0   # a = l_{t-1} odd, c = l_{t+1} even
            else: par[(t - 1) % k] = 0               # a even, c odd
            nonempty = [i for i in range(k) if i not in (t, (t + 1) % k)]; npar = [1] * len(nonempty)
        elif conf == 'C2b':
            k = oF + 3; t = rng.randrange(k)
            par = [1] * k; par[t] = 0; par[(t - 1) % k] = 0; par[(t + 1) % k] = 0
            nonempty = [i for i in range(k) if i not in (t, (t + 1) % k)]; npar = [1] * len(nonempty)
            npar[rng.randrange(len(npar))] = 0
        l = blocks_with(p, par)
        if l is None: continue
        R = 2 * p - oF
        if 4 * p - 2 - sum(l) != R: continue
        r = runs_with(R, npar)
        if r is None: continue
        a = [0] * k; b = [0] * k
        for i, x in zip(nonempty, r): a[i] = x
        y = [rng.randrange(p) for _ in range(k)]
        if conf.startswith('C2'):
            u = rng.randrange(p); v = (u + 1 + rng.randrange(p - 1)) % p
            y[(t - 1) % k] = u; y[t] = v; y[(t + 1) % k] = u
        else:
            while y[(t - 1) % k] == y[t]:
                y[t] = rng.randrange(p)
        # sanity: genuine empty runs, maximal blocks next to empty runs
        for i in range(k):
            if a[i] + b[i] == 0:
                assert y[(i - 1) % k] != y[i]
        assert sum(a) + sum(b) + sum(l) == 4 * p - 2
        assert gwin.kappa_of(l, p) == 0
        # partition (sets of run indices), in cyclic order
        if conf == 'C1a':
            merged = []
        elif conf == 'C1b':
            merged = [[t, (t + 1) % k]]
        elif conf == 'C2a':
            merged = [[(t + 1) % k, (t + 2) % k]]
        elif conf == 'C2a_mirror':
            merged = [[(t - 1) % k, t]]
        else:
            merged = [[(t - 1) % k, t], [(t + 1) % k, (t + 2) % k]]
        inm = {}
        for g in merged:
            for i in g: inm[i] = tuple(g)
        # build cyclic order of parts starting at a part boundary
        start = 0
        while start in inm and inm[start][0] != start:
            start += 1
        parts = []; seen = set(); i = start
        for _ in range(k):
            j = i % k
            if j in seen:
                i += 1; continue
            if j in inm:
                g = inm[j]; parts.append(list(g)); seen.update(g)
            else:
                parts.append([j]); seen.add(j)
            i += 1
        assert sorted(sum(parts, [])) == list(range(k))
        return a, b, l, y, t, parts
    return None

def uQ(Q, y, p):
    inv2 = (p + 1) // 2
    k = len(y)
    return (inv2 * sum((y[(i - 1) % k] - y[i]) for i in Q)) % p

def lamp(Q, a, b, l, y, p, boost=True):
    lq = gwin.lam(Q, a, b, l, p)
    if boost and lq == 0 and uQ(Q, y, p) != 0:
        return 1
    return lq

def gr0_interval(Q, a, b, l, p):
    """[ceil(lo/2), floor(hi/2)] of Lemma GR0 for z = +1 on Q"""
    k = len(a)
    z = [1 if i in Q else -1 for i in range(k)]
    F = sum(l); R = sum(a) + sum(b)
    f = [1 if z[i] != z[(i + 1) % k] else 0 for i in range(k)]
    Phi = sum(f); delta = sum(1 for i in range(k) if (l[i] - f[i]) % 2)
    Cmax = F - delta
    Ep = sum(a[i] if z[i] == 1 else b[i] for i in range(k)); Em = R - Ep
    s0 = 2 * p - Cmax; s1 = 2 * p - Phi
    lo = max(-s1, s0 - 2 * Em, -Em); hi = min(s1, 2 * Ep - s0, Ep)
    return (-((-lo) // 2), hi // 2)

def certificate(a, b, l, y, p, parts, boost=True):
    s = len(parts)
    k = len(a)
    allr = set(range(k))
    used = []
    def L(Q):
        Q = sorted(Q); used.append(tuple(Q))
        return lamp(Q, a, b, l, y, p, boost)
    A_ = sum(L(P) for P in parts)
    ok_a = A_ >= p + 1
    ok_b = True; minb_up = None; minb_lo = None
    for t in range(1, s - 1):
        X = set().union(*parts[:t]); Y = set(parts[t]); Z = allr - X - Y
        up = L(X | Y) + L(Y | Z) + L(Z | X)
        lo = L(X) + L(Y) + L(Z)
        minb_up = up if minb_up is None else min(minb_up, up)
        minb_lo = lo if minb_lo is None else min(minb_lo, lo)
        if up < p + 1 or lo < 1:
            ok_b = False
    Ps = set(parts[-1])
    c = L(Ps) + L(allr - Ps)
    ok_c = c >= 1
    return dict(sum_a=A_, ok_a=ok_a, ok_b=ok_b, ok_c=ok_c, minb_up=minb_up, minb_lo=minb_lo, c=c, used=used)

out = {"configs": {}, "failures": []}
primes = (5, 7, 11, 13, 17, 19, 23, 29, 31)
for conf in ('C1a', 'C1b', 'C2a', 'C2a_mirror', 'C2b'):
    st = dict(n=0, cert_ok=0, sum_a_values={}, noboost_a_fail=0, dp_checked=0, dp_solvable=0, h0_checked=0,
              h0_solvable=0, interval_checks=0, interval_mismatch=0)
    for p in primes:
        for trial in range(60 if p <= 13 else 30):
            m = make(p, conf)
            if m is None:
                continue
            a, b, l, y, t, parts = m
            st["n"] += 1
            cert = certificate(a, b, l, y, p, parts, True)
            st["sum_a_values"][str(cert["sum_a"] - p)] = st["sum_a_values"].get(str(cert["sum_a"] - p), 0) + 1
            if cert["ok_a"] and cert["ok_b"] and cert["ok_c"]:
                st["cert_ok"] += 1
            else:
                out["failures"].append(dict(conf=conf, p=p, a=a, b=b, l=l, y=y, cert={k_: v for k_, v in cert.items() if k_ != 'used'}))
            nb = certificate(a, b, l, y, p, parts, False)
            if not nb["ok_a"]:
                st["noboost_a_fail"] += 1
            # interval algebra on every pattern used
            for Q in set(cert["used"]):
                Qs = set(Q)
                if len(Qs) in (0, len(a)):
                    continue
                lo2, hi2 = gr0_interval(Qs, a, b, l, p)
                lq = gwin.lam(sorted(Qs), a, b, l, p)
                lc = gwin.lam(sorted(set(range(len(a))) - Qs), a, b, l, p)
                st["interval_checks"] += 1
                if (lo2, hi2) != (1 - lc, lq - 1):
                    st["interval_mismatch"] += 1
            if p <= 11:
                w = gwin.word_of(a, b, l, y, p)
                st["dp_checked"] += 1
                sv = dp.solvable(w, p)
                st["dp_solvable"] += sv
                if not sv:
                    out["failures"].append(dict(conf=conf, p=p, a=a, b=b, l=l, y=y, msg="DP says AVOIDS"))
                if p <= 7 and len(a) <= 12:
                    st["h0_checked"] += 1
                    st["h0_solvable"] += gwin.h0_solvable(a, b, l, y, p)
    out["configs"][conf] = st
srcs = {}
for fn in ("dp.py", "gwin.py", "e2_k0star_replay.py"):
    with open(os.path.join(HERE, fn), "rb") as f:
        srcs[fn] = hashlib.sha256(f.read()).hexdigest()
out["sources_sha256"] = srcs
with open(os.path.join(HERE, "..", "out", "e2_k0star_replay.json"), "x") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out["configs"], indent=0))
print("failures", len(out["failures"]))

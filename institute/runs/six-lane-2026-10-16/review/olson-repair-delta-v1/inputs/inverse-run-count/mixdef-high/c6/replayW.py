#!/usr/bin/env python3
"""replayW.py -- [F] literal replay of the constructions of Lemmas C0W and C0B (c6/proof-C0WB.md) on explicit words, task
OlsonRunCount5.  Usage: python3 replayW.py MUT NV
Both constructions use about x only sum_t x_t = p and the singleton lower bounds x_t >= lambda({t}) (plus, for C0B Case A, the bound
(A*)); so they are replayed on integer vectors x with sum p and lambda({t}) <= x_t <= U({t}) (random, and biased to small x), and
the produced pattern must satisfy X_P < lambda(P), checked with c5's independent slow_lambda (c5/cplus_replay.py exec'ed read-only).
C0W: words of random item-(iii) classes with B >= kB + 1 and 3kB + 1 <= p (p = 17, 19, 23, 29; excess words, biased to many even
  aligned runs by c5's generator 'random_word' when possible).  C0B: classes with k >= kB + 3B and 2kB <= p whose word violates
  Theorem C+'s count (n_ev,al > 4 and n_ev,al > 2(k - kB - 2B) + n_pr - 1); the construction is c5's 'procedure' (Theorem C+), whose
  assertion '(B1+) fails' is exactly the count that Lemma C0B proves without the n_ev,al hypothesis; in Case B also n_ev,al <= B + n_an - 2
  is asserted.
MUT 0 real; 1: C0W with target kB in place of kB + 1 ((M) must break); 2: C0W on classes with B >= kB + 1 but 3kB + 1 > p ((P) may
break: counted); 3: kill re-check against lambda - 1 (kills must be lost).
"""
import sys, random, time, json
SRC = open('../c5/cplus_replay.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
RET = "    return kind, XQ < lamQ"
assert SRC.count(GUARD) == 1 and SRC.count(RET) == 1
SRC = SRC.replace(GUARD, "").replace(RET, RET + ", Q")
G = {}
exec(compile(SRC, 'c5/cplus_replay.py', 'exec'), G)
slow_lambda, Wg, procedure, item_iii = G['slow_lambda'], G['Wg'], G['procedure'], G['item_iii']
def lam_set(W, S): return slow_lambda(W.p, W.d, W.l, W.B, W.kappa, sorted(S))
def blocks(W, S): return sum(1 for i in range(W.k) if (i in S) and ((i - 1) % W.k not in S))
def classes(p):
    out = []
    for k in range(p + 1, 2 * p - 1):
        for kappa in range(max(k - p, 1), (k - 3) // 2 + 1):
            R = 2 * p - k + 2 * kappa
            if R < k or R > 2 * p - 3: continue
            for B in range(1, kappa):
                A = R - B
                if B > A or A > 2 * p - 1: continue
                out.append((k, kappa, B))
    return out
def make_word(p, k, kappa, B, rnd, prefer_even=True):
    R = 2 * p - k + 2 * kappa; A = R - B; E = R - k
    for _ in range(3000):
        npr = rnd.randint(0, min(B, E, 2))
        Bp = B - npr
        nan = 0 if Bp == 0 else rnd.randint(max(1, Bp - (E - npr)), Bp)
        nal = k - nan - npr
        Ap = A - npr
        if nal < 1 or Ap < nal: continue
        ca = [1] * nal
        for _ in range(Ap - nal):
            ones = [i for i in range(nal) if ca[i] == 1]
            if prefer_even and ones and rnd.random() < 0.85: ca[rnd.choice(ones)] += 1
            else: ca[rnd.randrange(nal)] += 1
        cb = [1] * nan
        for _ in range(Bp - nan): cb[rnd.randrange(nan)] += 1
        kinds = [0] * nal + [1] * nan + [2] * npr
        rnd.shuffle(kinds)
        a, b = [], []; ia = ib = 0
        for t in range(k):
            if kinds[t] == 0: a.append(ca[ia]); b.append(0); ia += 1
            elif kinds[t] == 1: a.append(0); b.append(cb[ib]); ib += 1
            else: a.append(1); b.append(1)
        l = [1] * k
        for _ in range(p - 1 - kappa): l[rnd.randrange(k)] += 2
        W = Wg(p, a, b, l)
        if item_iii(W) and W.kappa == kappa and W.B == B and W.E == E: return W
    return None
def vectors(W, rnd, NV):
    p, k = W.p, W.k
    lo = W.single_lo; hi = W.single_hi
    out = []
    for i in range(NV):
        mode = i % 3
        x = [rnd.randint(lo[t], hi[t]) if mode == 0 else (lo[t] if mode == 1 else min(max((W.d[t] + 1) // 2, lo[t]), hi[t])) for t in range(k)]
        diff = p - sum(x); guard = 0
        while diff != 0 and guard < 500000:
            guard += 1
            t = rnd.randrange(k)
            if diff > 0 and x[t] < hi[t]: x[t] += 1; diff -= 1
            elif diff < 0 and x[t] > lo[t]: x[t] -= 1; diff += 1
        if diff == 0: out.append(x)
    return out
def c0w(W, x, MUT):
    p, k, kB, B = W.p, W.k, W.kB, W.B
    c = [W.d[t] - x[t] for t in range(k)]; bh = [2 * x[t] - W.d[t] for t in range(k)]
    cheap = [t for t in range(k) if c[t] >= 0 and bh[t] <= 1]
    w = {t: c[t] + 1 for t in cheap}
    for t in cheap: assert 1 <= w[t] <= kB, 'Lemma DF'
    Wc = sum(w.values())
    assert Wc >= 2 * kB + 1, 'step (2)'
    target = kB + 1 if MUT != 1 else kB
    cs = set(cheap)
    if len(cheap) < k:
        U = []
        start = next(t for t in range(k) if t not in cs)
        t = (start + 1) % k; path = []
        for _ in range(k):
            if t in cs: path.append(t)
            else:
                if path:
                    e, o = path[0::2], path[1::2]
                    U += e if sum(w[u] for u in e) >= sum(w[u] for u in o) else o
                path = []
            t = (t + 1) % k
        if path:
            e, o = path[0::2], path[1::2]
            U += e if sum(w[u] for u in e) >= sum(w[u] for u in o) else o
    else:
        t0 = 0; path = [(t0 + 1 + i) % k for i in range(k - 1)]
        e, o = path[0::2], path[1::2]
        U = e if sum(w[u] for u in e) >= sum(w[u] for u in o) else o
    assert sum(w[u] for u in U) >= kB + 1, 'step (3)'
    Us = set(U)
    for u in U: assert ((u - 1) % k not in Us) and ((u + 1) % k not in Us)
    U.sort(key=lambda u: -w[u])
    S = []; tot = 0
    for u in U:
        if tot >= target: break
        S.append(u); tot += w[u]
    S.sort(key=lambda u: 0 if bh[u] <= 0 else 1)
    P = []; tot = 0
    for u in S:
        if tot >= target: break
        P.append(u); tot += w[u]
    PHI = sum(c[u] for u in P) + blocks(W, set(P))
    BHP = sum(bh[u] for u in P); XP = sum(x[u] for u in P)
    okM = PHI >= kB + 1; okFl = BHP <= B; okP = XP + blocks(W, set(P)) <= p
    return set(P), okM, okFl, okP
def main():
    MUT = int(sys.argv[1]); NV = int(sys.argv[2])
    rnd = random.Random(10010 + MUT)
    t0 = time.time()
    print('== replayW.py MUT=%d NV=%d start %s' % (MUT, NV, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    tot = {}; fails = []
    def bump(key):
        tot[key] = tot.get(key, 0) + 1
    for p in (17, 19, 23, 29):
        cl = classes(p)
        if MUT == 2: poolW = [(k, ka, B) for (k, ka, B) in cl if B >= ka - B + 1 and 3 * (ka - B) + 1 > p and 2 * p - k + 2 * ka > k]
        else: poolW = [(k, ka, B) for (k, ka, B) in cl if B >= ka - B + 1 and 3 * (ka - B) + 1 <= p and 2 * p - k + 2 * ka > k]
        poolB = [(k, ka, B) for (k, ka, B) in cl if k >= (ka - B) + 3 * B and 2 * (ka - B) <= p and 2 * p - k + 2 * ka - k >= 6]
        for (k, ka, B) in rnd.sample(poolW, min(6, len(poolW))):
            for _ in range(2):
                W = make_word(p, k, ka, B, rnd)
                if W is None: continue
                for x in vectors(W, rnd, NV):
                    P, okM, okFl, okP = c0w(W, x, MUT)
                    if okM and okFl and okP:
                        lamP = lam_set(W, P) - (1 if MUT == 3 else 0)
                        res = 'C0W-kill' if sum(x[u] for u in P) < lamP else 'C0W-NOKILL'
                    else:
                        res = 'C0W-broken:' + ''.join(n for n, o in (('M', okM), ('Fl', okFl), ('P', okP)) if not o)
                    bump(res)
                    if (res == 'C0W-NOKILL' or (MUT == 0 and res.startswith('C0W-broken'))) and len(fails) < 6: fails.append((p, k, ka, B, res))
        if MUT in (0, 3):
            done = 0
            for (k, ka, B) in rnd.sample(poolB, len(poolB)):
                if done >= 6: break
                W = None
                for _ in range(20):
                    W0 = make_word(p, k, ka, B, rnd, prefer_even=True)
                    if W0 is not None and W0.nev_al > 4 and W0.nev_al > 2 * (W0.k - W0.kB - 2 * W0.B) + W0.npr - 1:
                        W = W0; break
                if W is None: continue
                done += 1
                for x in vectors(W, rnd, NV):
                    stats = {}
                    try:
                        kind, kill, Q = procedure(W, x, 0, stats)
                        if kind == 'B':
                            nan = len(W.anti)
                            assert W.nev_al <= W.B + nan - 2, 'n_ev,al bound'
                        lamQ = lam_set(W, Q) - (1 if MUT == 3 else 0)
                        res = 'C0B-kill-' + kind if sum(x[u] for u in Q) < lamQ else 'C0B-NOKILL-' + kind
                    except AssertionError as e:
                        res = 'C0B-ASSERT:' + str(e)[:40]
                    bump(res)
                    if ('NOKILL' in res or 'ASSERT' in res) and len(fails) < 10: fails.append((p, k, ka, B, res))
        print('  p = %d done %.1f s' % (p, time.time() - t0), flush=True)
    print(json.dumps({'MUT': MUT, 'outcomes': sorted(tot.items()), 'first_failures': fails}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""replayG.py -- [F] literal replay of c6/proof-SEEDG.md on explicit words, with mutation controls (task OlsonRunCount5, c6).
Usage: python3 replayG.py MUT NV
  MUT 0 real; 1: certification steps judged with the CANONICAL singleton ranges instead of the seeds (some steps must fail);
  2: every kill re-checked against lambda - 1 (some kills must be lost); 3: Theorem C+ procedure with |S| = Delta (c5's MUT 1;
  (M) must break in Case B).
Words (explicit, generated here): (RA2) all-single-letter, B = 2, kB = p - 5, p in 13, 17, 19, 23; (RA3) B = 3, kB = p - 6
  (p = 13, 17, 19) and kB = p - 7 (p = 11, 13, 17, 19); anti runs adjacent / spread / random.  (SA, PA) random words with excess
  (multi-letter aligned and anti runs, (1,1)-pairs) of random item-(iii) classes satisfying the region of Corollary SA, resp. PA,
  and C+'s class condition, p in 17, 19, 23, 29.
Per word and vector: singleton arcs (a violation is a kill); canonical lifts; for EVERY run t the explicit configuration of the
  proof is built in the word (pairs of adjacent single-letter aligned runs for RA2/RA3, m isolated aligned runs for SA, m blocks of two
  adjacent aligned runs for PA; existence, isolation and block counts asserted); the four arcs of Q, Q + t are computed by c5's
  independent slow_lambda (generic values asserted for SA/PA, the stated seed values for RA2/RA3); arcs of Q and Q + t checked
  (violation = kill); the seed conclusion x_t in [s_lo, s_hi] asserted.  RA2: then sum x = -2 must be impossible, i.e. every vector
  must have been killed already (asserted).  Otherwise the pin chain of {a}^c is walked with the seed ranges (each member's arc
  checked, each step's (A^s), (B^s) asserted), X_[k] = p asserted, the procedure of Theorem C+ (c5/cplus_replay.py, exec'ed
  read-only, patched in memory to return its final pattern) must return Q with X_Q < lambda(Q), and the removal chain of Q must
  contain an arc violation.  Every kill is re-checked with slow_lambda.
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
def cdiv(a, b): return -((-a) // b)
class Kill(Exception):
    def __init__(self, P, stage): self.P, self.stage = P, stage
def lam_set(W, S): return slow_lambda(W.p, W.d, W.l, W.B, W.kappa, sorted(S))
def lamc_set(W, S): return slow_lambda(W.p, W.d, W.l, W.B, W.kappa, [t for t in range(W.k) if t not in S])
def U_set(W, S): return W.p - lamc_set(W, S)
def in_arc(W, S, u):
    l, lc = lam_set(W, S), lamc_set(W, S)
    if l + lc > W.p: return False
    return (sum(u[t] for t in S) - l) % W.p <= (W.p - lc) - l
def blocks(W, S): return sum(1 for i in range(W.k) if (i in S) and ((i - 1) % W.k not in S))
def verify_kill(W, P, u, MUT):
    l, lc = lam_set(W, P), lamc_set(W, P)
    if MUT == 2: l -= 1
    if l + lc < 2: return False
    return (sum(u[i] for i in P) - (1 - lc)) % W.p <= l + lc - 2
def Delta0(W): return 2 * W.p - W.R
def region_SA(W):
    p, k, B, E, kB, D0 = W.p, W.k, W.B, W.E, W.kB, Delta0(W); bstar = min(B, E + 1)
    lo = max(cdiv(2 * kB + B + max(2, bstar), 3), B + 2 - D0, 1)
    hi = min((2 * p - B - E - 3) // 3, D0 + B - bstar - 2, cdiv(k - B - 3, 2))
    return lo if lo <= hi else None
def region_PA(W):
    p, k, B, E, kB, D0 = W.p, W.k, W.B, W.E, W.kB, Delta0(W); bstar = min(B, E + 1)
    if not (D0 >= B + 1 and bstar <= D0 + B - 1): return None
    lo = max(cdiv(kB + B // 2 + 1, 2), cdiv(kB + bstar + (B - bstar) // 2, 2), 1)
    hi = min((p - (E + B) // 2) // 2, (p - 1 - (E + B + 1) // 2) // 2, cdiv(k - 2 * B - 4, 3))
    return lo if lo <= hi else None
def cplus_ok(W):
    return W.nev_al <= 4 or (2 * W.kB <= W.p and W.nev_al <= 2 * (W.k - W.kB - 2 * W.B) + W.npr - 1)
def build_config(W, t, fam, m):
    """fam: 'P1' pairs of adjacent single-letter aligned runs; 'SA' isolated aligned runs; 'PA' blocks of 2 adjacent aligned runs."""
    k = W.k; Q = set(); need = m
    path = [(t + 2 + i) % k for i in range(k - 3)]
    ok = (lambda r: W.b[r] == 0 and W.a[r] == 1) if fam == 'P1' else (lambda r: W.b[r] == 0)
    i = 0
    while i < len(path) and need > 0:
        if not ok(path[i]): i += 1; continue
        j = i
        while j < len(path) and ok(path[j]): j += 1
        if fam == 'SA':
            for q in range(i, j, 2):
                if need == 0: break
                Q.add(path[q]); need -= 1
        else:
            q = i
            while q + 1 < j and need > 0:
                Q.add(path[q]); Q.add(path[q + 1]); need -= 1; q += 3
        i = j
    assert need == 0, 'configuration does not exist'
    return Q
def removal_chain(W, Q):
    chain = [set(Q)]; S = set(Q); k = W.k
    while len(S) >= 2:
        t = next(i for i in sorted(S) if ((i - 1) % k not in S) or ((i + 1) % k not in S))
        S = set(S); S.discard(t); chain.append(S)
    chain.reverse(); return chain
def certify_chain(W, Q, x, u, rng, stage):
    p = W.p
    ch = removal_chain(W, Q)
    for idx in range(1, len(ch)):
        Qp, Qi = ch[idx - 1], ch[idx]
        t = next(iter(Qi - Qp))
        if not in_arc(W, Qi, u): raise Kill(frozenset(Qi), stage)
        if len(Qp) == 1: lo, hi = rng[next(iter(Qp))]
        else: lo, hi = lam_set(W, Qp), U_set(W, Qp)
        at, bt = rng[t]
        if not (lo + at >= U_set(W, Qi) + 1 - p and hi + bt <= p + lam_set(W, Qi) - 1):
            raise AssertionError('certification step fails (size %d)' % len(Qi))
        assert lam_set(W, Qi) <= sum(x[i] for i in Qi) <= U_set(W, Qi)
def seeds_of(W, kind, m):
    """explicit configuration for every run: returns {t: (Q, s_lo, s_hi)} with all assertions of the proof."""
    p, k = W.p, W.k
    D0 = Delta0(W); out = {}
    fam = 'P1' if kind in ('RA2', 'RA3') else kind
    for t in range(k):
        Q = build_config(W, t, fam, m)
        assert t not in Q and all(((q - 1) % k != t and (q + 1) % k != t) for q in Q)
        assert blocks(W, Q) == m and blocks(W, Q | {t}) == m + 1
        Qt = Q | {t}
        lQ, lQc, lT, lTc = lam_set(W, Q), lamc_set(W, Q), lam_set(W, Qt), lamc_set(W, Qt)
        y = sum(W.d[q] for q in Q); d = W.d[t]
        if kind in ('SA', 'PA'):
            assert lQ == (y + W.B) // 2 + 1 and lQc == (W.A - y) // 2 + 1, 'Q not generic'
            assert lT == (y + d + W.B) // 2 + 1 and lTc == (W.A - y - d) // 2 + 1, 'Q + t not generic'
        slo = lT - (p - lQc); shi = (p - lTc) - lQ
        if kind == 'RA2': assert (slo, shi) == ((0, 0) if d == 1 else (-1, -1))
        if kind == 'RA3': assert (slo, shi) == ((0, 1) if d == 1 else (-1, 0))
        assert 2 * slo >= d - D0 + 2 and 2 * shi <= d + D0 - 2, 'seed not of quality'
        out[t] = (Q, slo, shi)
    return out
def run_vector(W, kind, m, SD, u, MUT, stats):
    p, k = W.p, W.k
    x = [None] * k
    for t in range(k):
        if not in_arc(W, {t}, u): raise Kill(frozenset([t]), 'singleton')
        L1 = lam_set(W, {t}); x[t] = (u[t] - L1) % p + L1
        assert x[t] <= U_set(W, {t})
    rng = {}
    for t in range(k):
        Q, slo, shi = SD[t]
        if not in_arc(W, Q, u): raise Kill(frozenset(Q), 'seed')
        if not in_arc(W, Q | {t}, u): raise Kill(frozenset(Q | {t}), 'seed')
        assert slo <= x[t] <= shi, 'Lemma GS conclusion violated'
        L1, U1 = lam_set(W, {t}), U_set(W, {t})
        rng[t] = (max(L1, slo), min(U1, shi)) if MUT != 1 else (L1, U1)
    if kind == 'RA2':
        raise AssertionError('RA2 vector survived all seeds (sum x = %d)' % sum(x))
    a = 0
    certify_chain(W, set(range(k)) - {a}, x, u, rng, 'pin')
    assert sum(x) == p, 'pin fails'
    kind2, kill, Qf = procedure(W, x, 1 if MUT == 3 else 0, stats)
    if MUT == 3 and not kill: return 'MUT3-M-broken'
    assert kill, 'procedure pattern does not violate (0.2)'
    certify_chain(W, set(Qf), x, u, rng, 'final-' + kind2)
    raise AssertionError('violated pattern certified without a kill')
def make_allsingle(p, kB, B, layout, rnd):
    k = p + kB + B
    if layout == 'block': anti = list(range(B))
    elif layout == 'spread': anti = sorted(set((i * k) // B for i in range(B)))
    else: anti = sorted(rnd.sample(range(k), B))
    a = [0 if t in anti else 1 for t in range(k)]; b = [1 if t in anti else 0 for t in range(k)]
    l = [1] * k; l[rnd.randrange(k)] += 2 * (p - 1 - (kB + B))
    return Wg(p, a, b, l)
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
def make_excess_word(p, k, kappa, B, rnd):
    R = 2 * p - k + 2 * kappa; A = R - B; E = R - k
    for _ in range(2000):
        npr = rnd.randint(0, min(B, E))
        Bp = B - npr
        nan = 0 if Bp == 0 else rnd.randint(1, Bp)
        nal = k - nan - npr
        Ap = A - npr
        if nal < 1 or Ap < nal: continue
        ca = [1] * nal
        for _ in range(Ap - nal): ca[rnd.randrange(nal)] += 1
        cb = [1] * nan
        for _ in range(Bp - nan): cb[rnd.randrange(nan)] += 1
        kinds = [0] * nal + [1] * nan + [2] * npr
        rnd.shuffle(kinds)
        a, b = [], []; ia = ib = 0
        for t in range(k):
            if kinds[t] == 0: a.append(ca[ia]); b.append(0); ia += 1
            elif kinds[t] == 1: a.append(0); b.append(cb[ib]); ib += 1
            else: a.append(1); b.append(1)
        H = p - 1 - kappa
        l = [1] * k
        for _ in range(H): l[rnd.randrange(k)] += 2
        W = Wg(p, a, b, l)
        if item_iii(W) and W.kappa == kappa and W.B == B and W.E == E and cplus_ok(W): return W
    return None
def vectors(W, SD, rnd, NV):
    p, k = W.p, W.k
    box = []
    for t in range(k):
        Q, slo, shi = SD[t]
        box.append((max(W.single_lo[t], slo), min(W.single_hi[t], shi)))
    out = []
    for i in range(NV):
        mode = i % 4
        if mode == 0 or any(lo > hi for lo, hi in box):
            u = [rnd.randrange(p) for _ in range(k)]; u[-1] = (-sum(u[:-1])) % p
            out.append(('uniform', u)); continue
        x = [rnd.randint(lo, hi) if mode == 1 else (lo if mode == 2 else hi) for (lo, hi) in box]
        diff = p - sum(x); guard = 0
        while diff != 0 and guard < 200000:
            guard += 1
            t = rnd.randrange(k); lo, hi = box[t]
            if diff > 0 and x[t] < hi: x[t] += 1; diff -= 1
            elif diff < 0 and x[t] > lo: x[t] -= 1; diff += 1
        if diff != 0:
            u = [rnd.randrange(p) for _ in range(k)]; u[-1] = (-sum(u[:-1])) % p
            out.append(('uniform*', u)); continue
        out.append(('box%d' % mode, [xi % p for xi in x]))
    return out
def main():
    MUT = int(sys.argv[1]); NV = int(sys.argv[2])
    rnd = random.Random(8008 + MUT)
    t0 = time.time()
    print('== replayG.py MUT=%d NV=%d start %s' % (MUT, NV, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    jobs = []
    for p in (13, 17, 19, 23): jobs.append(('RA2', p, p - 5, 2, (p - 3) // 2))
    for p in (13, 17, 19): jobs.append(('RA3', p, p - 6, 3, (p - 3) // 2))
    for p in (11, 13, 17, 19): jobs.append(('RA3', p, p - 7, 3, (p - 5) // 2))
    for p in (17, 19, 23, 29):
        for fam, reg in (('SA', region_SA), ('PA', region_PA)):
            pool = []
            for (k, kappa, B) in classes(p):
                R = 2 * p - k + 2 * kappa
                if R == k: continue
                W0 = make_excess_word(p, k, kappa, B, rnd)
                if W0 is None: continue
                if fam == 'PA' and region_SA(W0) is not None: continue
                if reg(W0) is not None: pool.append((k, kappa, B))
                if len(pool) >= 40: break
            for (k, kappa, B) in rnd.sample(pool, min(3, len(pool))):
                jobs.append((fam, p, k, kappa, B))
    tot = {}; fails = []; nwords = 0
    for job in jobs:
        if job[0] in ('RA2', 'RA3'):
            kind, p, kB, B, m = job
            words = [make_allsingle(p, kB, B, lay, rnd) for lay in ('block', 'spread', 'random')]
        else:
            kind, p, k, kappa, B = job
            words = [w for w in (make_excess_word(p, k, kappa, B, rnd) for _ in range(3)) if w is not None]
        for W in words:
            if kind in ('SA', 'PA'):
                m = region_SA(W) if kind == 'SA' else region_PA(W)
            nwords += 1
            try:
                SD = seeds_of(W, kind, m)
            except AssertionError as e:
                key = '%s:CONFIG-ASSERT:%s' % (kind, str(e)[:40]); tot[key] = tot.get(key, 0) + 1
                if len(fails) < 8: fails.append((job, 'config', str(e)[:60]))
                continue
            for (tag, u) in vectors(W, SD, rnd, NV):
                stats = {}
                try:
                    out = run_vector(W, kind, m, SD, u, MUT, stats)
                except Kill as K:
                    out = K.stage if verify_kill(W, K.P, u, MUT) else 'NOKILL-' + K.stage
                except AssertionError as e:
                    out = 'ASSERT:' + str(e)[:45]
                key = '%s:%s' % (kind, out)
                tot[key] = tot.get(key, 0) + 1
                if (out.startswith('NOKILL') or out.startswith('ASSERT')) and len(fails) < 8:
                    fails.append((job, tag, out))
        print('  job %s done %.1f s' % (str(job), time.time() - t0), flush=True)
    print(json.dumps({'MUT': MUT, 'jobs': jobs, 'words': nwords, 'outcomes': sorted(tot.items()), 'first_failures': fails}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()

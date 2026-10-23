#!/usr/bin/env python3
"""replayB.py -- [F] literal replay of c6/proof-SEEDB.md (Theorem SEED-B) on explicit words, with mutation controls.
Usage: python3 replayB.py MUT NV
  MUT 0 real; 1: certification steps judged with the CANONICAL singleton ranges (no seeds) -> some steps must fail;
  2: kill re-check against lambda - 1 -> some kills must be lost; 3: Theorem C procedure with |S| = Delta (the MUT 1 of
  c5/cplus_replay.py) -> (M) must break in Case B.
Words: all-single-letter, B anti runs placed as one block / spread / random, classes: the four p = 17 priority classes
(kB, B) = (5, 3), (4, 4), (5, 4), (5, 5) and four random region classes (2B + kB <= p - 2) for each p in 19, 23, 29, 37.
Part 1 (full proof): singleton arcs; canonical lifts; for EVERY run t the explicit isolated configuration of Lemma IS is built
  in the word (existence, isolation, type asserted), its arcs and those of Q + t are checked (a violation is a kill), and the
  closed seed bound of Lemma IS is asserted for x_t; pin: the removal chain of {a}^c (a an anti run) is walked, each member's
  arc checked (kill) and each step's (A^s), (B^s) asserted; X_[k] = p asserted; then the procedure of Theorem C
  (c5/cplus_replay.py 'procedure', exec'ed read-only, patched in memory to also return its final pattern Q) must return Q with
  X_Q < lambda(Q); the removal chain of Q is walked and must contain an arc violation (Lemma SL).
Part 2 (deep): vectors drawn inside the closed seed boxes (sum p), the explicit seed arcs are NOT checked (the conclusion of
  Lemma IS is asserted instead), the rest as in Part 1.
Every kill (a pattern P whose half-sum lies in its Lemma H window) is re-checked with c5's independent slow_lambda.
"""
import sys, random, time, json
SRC = open('../c5/cplus_replay.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
RET = "    return kind, XQ < lamQ"
assert SRC.count(GUARD) == 1 and SRC.count(RET) == 1
SRC = SRC.replace(GUARD, "").replace(RET, RET + ", Q")
G = {}
exec(compile(SRC, 'c5/cplus_replay.py', 'exec'), G)
slow_lambda, Wg, procedure = G['slow_lambda'], G['Wg'], G['procedure']
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
def config_rule(p, kB, B):
    if 5 * kB + B + 13 <= 3 * p: return ('S', cdiv(2 * kB + B + 2, 3))
    if 2 * kB + 7 * B + 28 <= 4 * p: return ('P', cdiv(kB + B // 2 + 1, 2))
    return None
def build_config(W, t, kind, m):
    k = W.k; Q = set(); need = m
    path = [(t + 2 + i) % k for i in range(k - 3)]
    i = 0
    while i < len(path) and need > 0:
        if W.b[path[i]] > 0: i += 1; continue
        j = i
        while j < len(path) and W.b[path[j]] == 0: j += 1
        if kind == 'S':
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
def closed_seed(p, kB, B, y, d):
    D = p - kB
    if d == 1:
        return ((B + 1) // 2 + 2 - cdiv(D, 2), D // 2 - B // 2 - 1) if y % 2 == 0 else (B // 2 + 2 - D // 2, cdiv(D, 2) - (B + 1) // 2 - 1)
    return ((B - 1) // 2 + 2 - cdiv(D, 2), D // 2 - B // 2 - 2) if y % 2 == 0 else (B // 2 + 1 - D // 2, cdiv(D, 2) - (B + 1) // 2 - 2)
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
def run_vector(W, kind, m, u, MUT, stats, part):
    p, k, kB, B = W.p, W.k, W.kB, W.B
    x = [None] * k
    for t in range(k):
        if not in_arc(W, {t}, u): raise Kill(frozenset([t]), 'singleton')
        L1 = lam_set(W, {t}); x[t] = (u[t] - L1) % p + L1
        assert x[t] <= U_set(W, {t})
    rng = {}
    y = m if kind == 'S' else 2 * m
    for t in range(k):
        lo, hi = closed_seed(p, kB, B, y, W.d[t])
        if part == 1:
            Q = build_config(W, t, kind, m)
            assert t not in Q and all(((q - 1) % k != t and (q + 1) % k != t) for q in Q)
            assert blocks(W, Q) == m and sum(W.d[q] for q in Q) == y and blocks(W, Q | {t}) == m + 1
            if not in_arc(W, Q, u): raise Kill(frozenset(Q), 'seed')
            if not in_arc(W, Q | {t}, u): raise Kill(frozenset(Q | {t}), 'seed')
        assert lo <= x[t] <= hi, 'Lemma IS conclusion violated'
        L1, U1 = lam_set(W, {t}), U_set(W, {t})
        rng[t] = (max(L1, lo), min(U1, hi)) if MUT != 1 else (L1, U1)
    a = W.anti[0]
    certify_chain(W, set(range(k)) - {a}, x, u, rng, 'pin')
    assert sum(x) == p, 'pin fails'
    kind2, kill, Qf = procedure(W, x, 1 if MUT == 3 else 0, stats)
    if MUT == 3 and not kill: return 'MUT3-M-broken'
    assert kill, 'procedure pattern does not violate (0.2)'
    certify_chain(W, set(Qf), x, u, rng, 'final-' + kind2)
    raise AssertionError('violated pattern certified without a kill')
def verify_kill(W, P, u, MUT):
    l, lc = lam_set(W, P), lamc_set(W, P)
    if MUT == 2: l -= 1
    if l + lc < 2: return False
    return (sum(u[i] for i in P) - (1 - lc)) % W.p <= l + lc - 2
def make_word(p, kB, B, layout, rnd):
    k = p + kB + B
    if layout == 'block': anti = list(range(B))
    elif layout == 'spread': anti = sorted(set((i * k) // B for i in range(B)))
    else: anti = sorted(rnd.sample(range(k), B))
    a = [0 if t in anti else 1 for t in range(k)]; b = [1 if t in anti else 0 for t in range(k)]
    l = [1] * k; l[rnd.randrange(k)] += 2 * (p - 1 - (kB + B))
    return Wg(p, a, b, l)
def vectors(W, kind, m, rnd, NV):
    p, k, kB, B = W.p, W.k, W.kB, W.B
    y = m if kind == 'S' else 2 * m
    al, ah = closed_seed(p, kB, B, y, 1); nl, nh = closed_seed(p, kB, B, y, -1)
    box = [((max(-kB, nl), nh) if W.b[t] > 0 else (max(2 - kB, al), ah)) for t in range(k)]
    out = []
    for i in range(NV):
        mode = i % 5
        if mode == 0:
            u = [rnd.randrange(p) for _ in range(k)]; u[-1] = (-sum(u[:-1])) % p
            out.append(('uniform', u)); continue
        x = [0] * k
        for t in range(k):
            lo, hi = box[t]
            if mode == 1: x[t] = rnd.randint(lo, hi)
            elif mode == 2: x[t] = min(max(1 if W.b[t] == 0 else 0, lo), hi) if rnd.random() < 0.85 else rnd.randint(lo, hi)
            elif mode == 3: x[t] = min(max((1 if W.b[t] == 0 else 0) + rnd.choice([-1, 0, 0, 0, 1]), lo), hi)
            else: x[t] = min(max(1 if W.b[t] == 0 else -1, lo), hi)      # Case-B bias: anti runs as defects with c = 0
        diff = p - sum(x); guard = 0
        while diff != 0 and guard < 100000:
            guard += 1
            t = rnd.randrange(k); lo, hi = box[t]
            if mode == 4 and W.b[t] > 0: continue          # keep the anti runs at -1 in the Case-B mode
            if diff > 0 and x[t] < hi: x[t] += 1; diff -= 1
            elif diff < 0 and x[t] > lo: x[t] -= 1; diff += 1
        if diff != 0: continue
        out.append(('box%d' % mode, [xi % p for xi in x]))
    return out
def main():
    MUT = int(sys.argv[1]); NV = int(sys.argv[2])
    rnd = random.Random(6006 + MUT)
    t0 = time.time()
    print('== replayB.py MUT=%d NV=%d start %s' % (MUT, NV, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    classes = [(17, 5, 3), (17, 4, 4), (17, 5, 4), (17, 5, 5)]
    for p in (19, 23, 29, 37):
        pool = [(p, kB, B) for kB in range(1, p) for B in range(2, p) if 2 * B + kB <= p - 2]
        classes += rnd.sample(pool, 4)
    tot = {}; fails = []
    for (p, kB, B) in classes:
        kind, m = config_rule(p, kB, B)
        for layout in ('block', 'spread', 'random'):
            W = make_word(p, kB, B, layout, rnd)
            assert W.kB == kB and W.B == B
            for part in (1, 2):
                for (tag, u) in vectors(W, kind, m, rnd, NV):
                    if part == 2 and tag == 'uniform': continue
                    stats = {}
                    try:
                        out = run_vector(W, kind, m, u, MUT, stats, part)
                    except Kill as K:
                        out = K.stage if verify_kill(W, K.P, u, MUT) else 'NOKILL-' + K.stage
                    except AssertionError as e:
                        out = 'ASSERT:' + str(e)[:50]
                    key = 'P%d:%s' % (part, out)
                    tot[key] = tot.get(key, 0) + 1
                    if (out.startswith('NOKILL') or out.startswith('ASSERT')) and len(fails) < 6:
                        fails.append((p, kB, B, layout, part, tag, out))
        print('  class (p, kB, B) = %s done %.1f s' % ((p, kB, B), time.time() - t0), flush=True)
    print(json.dumps({'MUT': MUT, 'classes': classes, 'outcomes': sorted(tot.items()), 'first_failures': fails}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()

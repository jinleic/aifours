#!/usr/bin/env python3
"""replay.py -- [F] literal replay of c5/proof-SEED.md (task OlsonRunCount5) on residue vectors, with mutation controls.

Usage: python3 replay.py MUT NV   (MUT = 0 real run; 1, 2, 3 mutation controls; NV vectors per (p, kB, part)).
W(p, kB): run 0 anti (d = -1), runs 1..n aligned (d = +1), k = n + 1 runs on a cycle.  A residue vector u in Z_p^k with
sum 0 is a hypothetical avoider; the replay follows the proof and must end with an explicit proper pattern P whose u_P lies in
its Lemma H window [1 - lambda(P^c), lambda(P) - 1] (mod p) -- a KILL -- re-checked by an independent slow lambda routine
on the explicit run list.  Every intermediate claim of the proof is asserted (seed range of every lift, certified range of
every pattern on every chain, the pin X_[k] = p, the conclusions of Steps 1-3).
Part 1: the full procedure (pair seeds checked on explicit pair configurations).  Part 2: vectors built from the seed
conclusion (x_t in [a, b] for aligned t), testing Lemma SCW, the pin and Steps 1-3.
Mutation controls: MUT = 1: the final kill test uses lambda(P) - 1 (window shrunk by one): some kills must be lost;
MUT = 2: certification steps judged with the plain singleton ranges instead of the seeds: some step conditions must fail;
MUT = 3: Step 3 adjoins a run s ADJACENT to Z (m(Q) = 1): the claim c(Q) > gamma(Q) must fail for some vectors.
"""
import sys, random, time

def fdiv(a, b): return a // b
def cdiv(a, b): return -((-a) // b)

class Word:
    def __init__(self, p, kB):
        self.p, self.kB = p, kB
        self.n = p + kB; self.k = self.n + 1; self.delta = p - kB
        self.d = [-1] + [1] * self.n
        self.full = (1 << self.k) - 1
        self.alignedmask = self.full ^ 1
        self.B, self.kappa = 1, kB + 1
    # fast path (bitmask)
    def Dm(self, Q):
        k = self.k
        D = bin(Q & self.alignedmask).count('1') - (Q & 1)
        rot = ((Q << 1) | (Q >> (k - 1))) & self.full      # bit i of rot = bit i-1 of Q (cyclic)
        m = bin(Q & ~rot & self.full).count('1')
        return D, m
    def lam(self, Q):
        p = self.p; D, m = self.Dm(Q)
        return min(p - m + 1, D + self.B - self.kappa + m, (D + self.B) // 2 + 1)
    def lamc(self, Q): return self.lam(self.full ^ Q)
    def U(self, Q): return self.p - self.lamc(Q)
    def size(self, Q): return bin(Q).count('1')
    def sumx(self, Q, x):
        s = 0; i = 0
        while Q:
            if Q & 1: s += x[i]
            Q >>= 1; i += 1
        return s

# independent slow lambda on the explicit run list (used only for the final kill verification)
def slow_lambda(p, d, B, kappa, members):
    k = len(d)
    inQ = [False] * k
    for i in members: inQ[i] = True
    D = sum(d[i] for i in range(k) if inQ[i])
    blocks = 0
    for i in range(k):
        if inQ[i] and not inQ[i - 1]: blocks += 1
    beta = 0
    return min(p - blocks + 1, D + B - kappa + blocks - beta, (D + B) // 2 + 1)

def verify_kill(W, P, u, MUT):
    k = W.k
    members = [i for i in range(k) if (P >> i) & 1]
    assert 0 < len(members) < k
    comp = [i for i in range(k) if not (P >> i) & 1]
    l = slow_lambda(W.p, W.d, W.B, W.kappa, members)
    lc = slow_lambda(W.p, W.d, W.B, W.kappa, comp)
    if MUT == 1: l -= 1
    if l + lc < 2: return False          # empty window
    uP = sum(u[i] for i in members) % W.p
    return (uP - (1 - lc)) % W.p <= l + lc - 2

class Kill(Exception):
    def __init__(self, P, stage): self.P, self.stage = P, stage

def in_arc(W, Q, uQ):
    l, lc = W.lam(Q), W.lamc(Q)
    if l + lc > W.p: return False        # full window: every residue killed
    return (uQ - l) % W.p <= (W.p - lc) - l

def cw_chain(W, Q):
    """Lemma CW order: remove an aligned END run of a block with >= 2 runs, else an isolated aligned run."""
    chain = [Q]; k = W.k
    while W.size(Q) >= 2:
        t = None
        for i in range(1, k):
            if (Q >> i) & 1:
                prv = (Q >> ((i - 1) % k)) & 1; nxt = (Q >> ((i + 1) % k)) & 1
                if prv != nxt: t = i; break
        if t is None:
            for i in range(1, k):
                if (Q >> i) & 1: t = i; break
        Q = Q & ~(1 << t); chain.append(Q)
    chain.reverse()
    return chain

def certify(W, Q, x, u, seed, stage, stats, MUT):
    """walk the CW chain of Q upwards; kill at the first member whose u is outside its arc; assert the certification."""
    p = W.p
    a, b = seed
    a0, b0 = W.lam(1), W.U(1)              # anti run: canonical range
    ch = cw_chain(W, Q)
    for idx in range(1, len(ch)):
        Qp, Qi = ch[idx - 1], ch[idx]
        t = (Qi ^ Qp).bit_length() - 1
        uQ = sum(u[i] for i in range(W.k) if (Qi >> i) & 1) % p
        if not in_arc(W, Qi, uQ):
            raise Kill(Qi, stage)
        # step condition (A^s), (B^s)
        if W.size(Qp) == 1:
            if Qp == 1: lo, hi = a0, b0
            else: lo, hi = (a, b) if MUT != 2 else (W.lam(Qp), W.U(Qp))
        else:
            lo, hi = W.lam(Qp), W.U(Qp)
        at, bt = (a, b) if MUT != 2 else (W.lam(1 << t), W.U(1 << t))
        okA = lo + at >= W.U(Qi) + 1 - p
        okB = hi + bt <= p + W.lam(Qi) - 1
        if not (okA and okB):
            stats['certfail'] = stats.get('certfail', 0) + 1
            raise AssertionError('certification step fails at size %d' % W.size(Qi))
        X = W.sumx(Qi, x)
        assert W.lam(Qi) <= X <= W.U(Qi), 'certified pattern lifted outside its arc'

def pair_config(W, t):
    n, m = W.n, W.kB // 2 + 1
    Q = 0
    if t <= n - 2:
        Q |= (1 << (t + 1)) | (1 << (t + 2)); ivs = [(1, t - 2), (t + 4, n)]
    else:
        Q |= (1 << (t - 2)) | (1 << (t - 1)); ivs = [(1, t - 4), (t + 2, n)]
    need = m - 1
    for (lo, hi) in ivs:
        s = lo
        while s + 1 <= hi and need > 0:
            Q |= (1 << s) | (1 << (s + 1)); need -= 1; s += 3
    assert need == 0, 'pair configuration does not exist'
    return Q

def gamma(W, Q, x):
    D, m = W.Dm(Q)
    return max(D + m - W.p - 1, W.kB - m, cdiv(D - 1, 2) - 1)

def run_vector(W, u, seed, part, stats, MUT):
    p, k, n, kB, delta = W.p, W.k, W.n, W.kB, W.delta
    a, b = seed
    # singleton arcs and canonical lifts
    x = [None] * k
    for t in range(k):
        S = 1 << t
        if not in_arc(W, S, u[t] % p): raise Kill(S, 'singleton')
        L1 = W.lam(S)
        x[t] = (u[t] - L1) % p + L1
        assert x[t] <= W.U(S)
    # Lemma PS (part 1 only; in part 2 the vectors are built inside the seed range)
    if part == 1:
        for t in range(1, n + 1):
            Q = pair_config(W, t)
            uQ = sum(u[i] for i in range(k) if (Q >> i) & 1) % p
            if not in_arc(W, Q, uQ): raise Kill(Q, 'seed')
            Qt = Q | (1 << t)
            if not in_arc(W, Qt, (uQ + u[t]) % p): raise Kill(Qt, 'seed')
            assert a <= x[t] <= b, 'Lemma PS violated'
    else:
        for t in range(1, n + 1): assert a <= x[t] <= b
    # pin: intervals I_i, i = 2..n (I_n = {0}^c)
    for i in range(2, n + 1):
        I = ((1 << (i + 1)) - 1) ^ 1
        uI = sum(u[1:i + 1]) % p
        if not in_arc(W, I, uI):
            certify(W, I, x, u, seed, 'pin', stats, MUT)    # walks the chain; kills at the first bad member
            raise AssertionError('arc violation not caught by the chain')
    certify(W, W.full ^ 1, x, u, seed, 'pin', stats, MUT)
    assert sum(x) == p, 'pin X_[k] = p fails'
    c = [W.d[t] - x[t] for t in range(k)]
    assert sum(c) == kB - 1
    Zal = [t for t in range(1, k) if c[t] >= 1]
    eZ = 1 if c[0] >= 0 else 0
    # Step 1
    if len(Zal) >= kB:
        Q = 0
        for t in Zal[:kB]: Q |= 1 << t
        cQ = sum(c[t] for t in Zal[:kB])
        assert cQ > gamma(W, Q, x), 'Step 1 claim fails'
        certify(W, Q, x, u, seed, 'step1', stats, MUT)
        raise AssertionError('Step 1 pattern certified but X_Q < lambda(Q) was claimed')
    Z = (1 if eZ else 0)
    for t in Zal: Z |= 1 << t
    cZ = sum(c[t] for t in range(k) if (Z >> t) & 1)
    assert cZ >= kB - eZ, 'Step 2: c(Z) >= kB - e_Z fails'
    if cZ > gamma(W, Z, x):
        certify(W, Z, x, u, seed, 'step2', stats, MUT)
        raise AssertionError('Step 2 pattern certified but X_Z < lambda(Z) was claimed')
    D, mZ = W.Dm(Z)
    assert eZ == 1 and mZ == 1 and cZ == kB - 1, 'Step 2 structure fails'
    assert all(c[t] == 0 for t in range(1, k) if not (Z >> t) & 1)
    # Step 3
    s = None
    for t in range(1, k):
        if (Z >> t) & 1: continue
        if (Z >> ((t - 1) % k)) & 1 or (Z >> ((t + 1) % k)) & 1:
            if MUT == 3: s = t; break
            continue
        if MUT != 3: s = t; break
    assert s is not None
    Q = Z | (1 << s)
    cQ = cZ + c[s]
    if not cQ > gamma(W, Q, x):
        stats['step3claimfail'] = stats.get('step3claimfail', 0) + 1
        raise AssertionError('Step 3 claim c(Q) > gamma(Q) fails')
    certify(W, Q, x, u, seed, 'step3', stats, MUT)
    raise AssertionError('Step 3 pattern certified but X_Q < lambda(Q) was claimed')

def make_vectors(W, rnd, NV, part):
    p, k, n, kB, delta = W.p, W.k, W.n, W.kB, W.delta
    a, b = 3 - cdiv(delta, 2), delta // 2 - 1
    vecs = []
    for i in range(NV):
        mode = i % 5
        if part == 1 and mode == 0:
            u = [rnd.randrange(p) for _ in range(k - 1)]; u.append((-sum(u)) % p); u = [u[-1]] + u[:-1]
            vecs.append(('uniform', u)); continue
        x = [0] * k
        if mode in (0, 1):
            for t in range(1, k): x[t] = rnd.randint(a, b)
            tag = 'seedbox'
        elif mode == 2:
            for t in range(1, k): x[t] = 1
            for _ in range(rnd.randint(0, max(1, kB // 2))): x[rnd.randrange(1, k)] = max(a, 0)
            for _ in range(rnd.randint(0, 3)): x[rnd.randrange(1, k)] = min(b, 2)
            tag = 'ones'
        elif mode == 3:
            for t in range(1, k): x[t] = rnd.choice([max(a, 0), 1, 1, 1, min(b, 2)])
            tag = 'near1'
        else:
            lo = rnd.randint(a, b); hi = rnd.randint(lo, b)
            for t in range(1, k): x[t] = rnd.randint(lo, hi)
            tag = 'band'
        # anti run: choose x_0 with sum = p if inside its canonical range, else the residue (singleton kill or other)
        x0 = p - sum(x[1:])
        x[0] = x0
        u = [xi % p for xi in x]
        vecs.append((tag, u))
    return vecs

def main():
    MUT = int(sys.argv[1]); NV = int(sys.argv[2])
    rnd = random.Random(1017 + MUT)
    t0 = time.time()
    print('== replay.py MUT=%d NV=%d start %s' % (MUT, NV, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    tot = {}
    fails = []
    plist = [11, 13, 17, 19, 23, 37, 41, 43, 47, 53, 59, 61]
    for p in plist:
        kBs = [kB for kB in range(1, p - 3) if 3 * kB >= p + 5]
        if p >= 37:
            lo = kBs[0]; hi = kBs[-1]
            pick = sorted(set([lo, lo + 1, lo + 2, (3 * p + 1 + 6) // 7 - 1, (3 * p) // 5 + 1, (3 * p) // 5 + 3, hi - 3, hi - 2, hi - 1, hi]))
            kBs = [kB for kB in pick if kB in kBs]
        for kB in kBs:
            W = Word(p, kB)
            seed = (3 - cdiv(W.delta, 2), W.delta // 2 - 1)
            for part in (1, 2):
                for (tag, u) in make_vectors(W, rnd, NV, part):
                    stats = {}
                    key = (part, tag)
                    try:
                        run_vector(W, u, seed, part, stats, MUT)
                        out = 'NOKILL-end'
                    except Kill as K:
                        out = K.stage if verify_kill(W, K.P, u, MUT) else 'NOKILL-' + K.stage
                    except AssertionError as e:
                        out = 'ASSERT:' + str(e)
                    tot[out] = tot.get(out, 0) + 1
                    if (out.startswith('NOKILL') or out.startswith('ASSERT')) and len(fails) < 8:
                        fails.append((p, kB, part, tag, out))
        print('  p=%d done (%.1f s) %s' % (p, time.time() - t0, sorted(tot.items())), flush=True)
    print({'MUT': MUT, 'outcomes': sorted(tot.items()), 'first_failures': fails}, flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)

if __name__ == '__main__':
    main()

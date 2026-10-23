# kb0_replay.py -- c4 (T2): literal replay of the kill argument of c4/proof-KB0.md (Theorem KB0) on integer vectors.
# For W(p, K), K = (p+5)/3, p = 1 (mod 6): runs 0 (anti, d = -1), 1..n (aligned, d = 1), n = p + K.
# Claim replayed: for EVERY integer vector x with singleton bounds x_t in [lambda({t}), p - lambda({t}^c)] and
# sum x = p, the case analysis (Steps 1-3 with the exceptions Z = {0}, Z = {0, a}) outputs a pattern Q in the certified
# family CERT = {singletons} u {2 <= |Q| <= K+1, Q not an anti pair} u {P, P^c} with X_Q < lambda(Q).
# lambda is computed here from an explicit block count (independent of certk.cpp / review_check.py).
# Every intermediate claim of the proof is asserted.  Mutation controls: MUT=1 sum x = p + 1; MUT=2 kill test with
# lambda(Q) - 1; MUT=3 in the exception Z = {0} use the uncertified anti pair {0, s} (membership must fail).
# Usage: python3 -B kb0_replay.py SEED TRIALS MUT
import sys, random
SEED, TRIALS, MUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rng = random.Random(SEED)
def run(p):
    K = (p + 5) // 3; n = p + K; k = n + 1
    d = [-1] + [1] * n
    def blocks(Q):
        return sum(1 for t in Q if (t - 1) % k not in Q)
    def lam(Q):
        Q = set(Q); m = blocks(Q); D = sum(d[t] for t in Q)
        return min(p - m + 1, D + m - K, (D + 1) // 2 + 1)
    full = set(range(k))
    P = {0, 2, 4}; Pc = full - P
    def certified(Q):
        Q = set(Q)
        if len(Q) == 1: return True
        if Q == P or Q == Pc: return True
        if 2 <= len(Q) <= K + 1 and not (len(Q) == 2 and 0 in Q): return True
        return False
    lo = {t: lam({t}) for t in range(k)}
    hi = {t: p - lam(full - {t}) for t in range(k)}
    assert lo[0] == -K and all(lo[t] == 2 - K for t in range(1, k))
    def adjacent(a, b): return (a - b) % k in (1, k - 1)
    stats = {'step1': 0, 'step2_Z': 0, 'antipair': 0, 'step3_Z0': 0, 'step3_interval': 0, 'fail': 0, 'mutfail': 0}
    target = p + (1 if MUT == 1 else 0)
    for trial in range(TRIALS):
        # random vector with singleton bounds and sum = target; several shapes
        mode = rng.randrange(4)
        while True:
            x = [0] * k
            for t in range(k):
                if mode == 0: x[t] = rng.randint(lo[t], hi[t])
                elif mode == 1: x[t] = rng.choice([1, 1, 1, 0, rng.randint(lo[t], hi[t])])
                elif mode == 2: x[t] = 1 if t else rng.randint(lo[0], hi[0])
                else: x[t] = rng.choice([1, 1, 1, 1, 1, 0, -1, lo[t]])
                x[t] = max(lo[t], min(hi[t], x[t]))
            # repair the sum by moving single coordinates within bounds
            s = sum(x); tries = 0
            while s != target and tries < 10 * k:
                t = rng.randrange(k); tries += 1
                if s < target and x[t] < hi[t]: x[t] += 1; s += 1
                elif s > target and x[t] > lo[t]: x[t] -= 1; s -= 1
            if s == target: break
        c = [d[t] - x[t] for t in range(k)]
        assert sum(c) == (K - 1) - (1 if MUT == 1 else 0) or MUT == 1
        assert all(ct <= K - 1 for ct in c)
        X = lambda Q: sum(x[t] for t in Q)
        def kill(Q):
            return X(Q) < lam(Q) - (1 if MUT == 2 else 0)
        Zal = [t for t in range(1, k) if c[t] >= 1]
        eZ = 1 if c[0] >= 0 else 0
        Z = set(Zal) | ({0} if eZ else set())
        out = None; tag = None
        if len(Zal) >= K:
            out = set(Zal[:K]); tag = 'step1'
        else:
            # Step 2
            cZ = sum(c[t] for t in Z)
            if MUT != 1: assert cZ >= K - eZ, (cZ, K, eZ)
            if len(Z) == 2 and 0 in Z:
                a = [t for t in Z if t][0]
                zeros = [t for t in range(1, k) if t not in Z and c[t] == 0 and not adjacent(t, 0) and not adjacent(t, a)]
                if MUT != 1: assert len([t for t in range(1, k) if t not in Z and c[t] == 0]) >= p
                if zeros: out = {0, a, zeros[0]}; tag = 'antipair'
            elif certified(Z) and kill(Z):
                out = Z; tag = 'step2_Z'
            else:
                # proof: certified Z with X_Z >= lambda(Z) forces eZ = 1, m(Z) = 1, c(Z) = K - 1, aligned outside c = 0
                ok_struct = (eZ == 1 and blocks(Z) == 1 and cZ == K - 1 and all(c[t] == 0 for t in range(1, k) if t not in Z))
                if MUT == 0: assert ok_struct, ('structure', sorted(Z), cZ)
                if ok_struct:
                    if Z == {0}:
                        if MUT == 3:
                            s1 = [t for t in range(1, k) if not adjacent(t, 0)][0]; out = {0, s1}; tag = 'step3_Z0'
                        else:
                            iso = [t for t in range(1, k) if not adjacent(t, 0)]
                            s1 = iso[0]; s2 = [t for t in iso if not adjacent(t, s1) and t != s1][0]
                            out = {0, s1, s2}; tag = 'step3_Z0'
                    else:
                        far = [t for t in range(1, k) if t not in Z and all(not adjacent(t, z) for z in Z)]
                        if MUT == 0: assert len(far) >= p - 1
                        out = Z | {far[0]}; tag = 'step3_interval'
        if out is not None and certified(out) and kill(out):
            stats[tag] += 1
        else:
            if MUT == 0:
                stats['fail'] += 1
                print('FAIL', p, x, sorted(Z), tag, sorted(out) if out else None)
            else:
                stats['mutfail'] += 1
    return K, stats
for p in (13, 19, 31, 37, 43):
    K, st = run(p)
    print({'p': p, 'K': K, 'MUT': MUT, 'trials': TRIALS, **st}, flush=True)

# ind_replay.py -- c4/proof-IND.md receipts ([F], aids only).  Independent of indep*.cpp, ind_cert*.py, ind_m.py.
# Part A (hypotheses): for every prime 11 <= p <= PMAX and every kB with 3kB >= p + 4, kB <= p - 4: evaluate the
#   hypotheses (S1)-(S3), (C), (L) of Theorem IND exactly as written in proof-IND.md; list the kB that satisfy them;
#   check that the closed-form band (3p+1)/7 <= kB <= (3p-7)/5 of Corollary IND-I satisfies them (p <= PMAX).
# Part B (literal replay, p <= PREP): for random and structured u in Z_p^T follow Steps 1-4 of the proof and output a
#   subset S of T whose half-sum lies in its Lemma H window; the window is recomputed from the explicit pattern
#   (block count, D) by an independent lambda routine.  A "no kill" outcome contradicts the proof.
# Part C (mutation controls): MUT=1 T shrunk by 2 runs; MUT=2 every window shrunk by one (lambda - 1 on both sides);
#   MUT=3 Step 1 skipped (canonical lifts used without the seed range).  Each must produce failures somewhere.
# Usage: python3 -B ind_replay.py PMAX PREP TRIALS SEED MUT
import sys, random
PMAX, PREP, TRIALS, SEED, MUT = (int(v) for v in sys.argv[1:6])
rng = random.Random(SEED)
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def fl(x, y): return x // y
def cl(x, y): return -((-x) // y)
def params(p, kB, N=None):
    d = p - kB
    if N is None: N = cl(p + kB, 2)
    L = lambda j: min(p - j + 1, 2 * j - kB, fl(j + 1, 2) + 1)
    U = lambda j: p - min(p - j + 1, p - 1, fl(p + kB - j, 2) + 1)
    j1 = 1
    while not (2 * j1 - kB >= fl(j1 + 1, 2) + 1): j1 += 1
    s = max(d, j1)
    return d, N, L, U, j1, s
def hypotheses(p, kB, N=None):
    d, N, L, U, j1, s = params(p, kB, N)
    if not (s + 1 <= N): return False, 'S1'
    if not (U(s) == s - 1 and U(s + 1) == s and L(s) == fl(s + 1, 2) + 1 and L(s + 1) == fl(s + 2, 2) + 1): return False, 'S2'
    alpha, omega = 3 - cl(s, 2), fl(s, 2) - 1
    if not (alpha == L(s + 1) - U(s) and omega == U(s + 1) - L(s)): return False, 'A-formula'
    if not (omega <= d + 1 and alpha >= 2 - kB): return False, 'S3'
    h, r = min(omega, fl(d, 2)), -alpha
    if not (-r >= L(1) and h <= U(1)): return False, 'base'
    for j in range(1, N):
        if not (max(L(j), -j * r) - r >= U(j + 1) + 1 - p): return False, 'C1@%d' % j
        if not (min(U(j), j * h) + h <= p + L(j + 1) - 1): return False, 'C2@%d' % j
    if not (j1 <= N and L(j1) == fl(j1 + 1, 2) + 1 and d <= N - 1 and U(d) == d - 1 and U(N) == N - 1): return False, 'L-aux'
    if not (d <= N - fl(j1, 2) + 1): return False, 'L'
    return True, 'ok'
# ---------- Part A
cover = {}; band_fail = []
for p in range(11, PMAX + 1):
    if not isprime(p): continue
    ks = [kB for kB in range(1, p - 3) if 3 * kB >= p + 4]
    ok = [kB for kB in ks if hypotheses(p, kB)[0]]
    cover[p] = ok
    band = [kB for kB in ks if 7 * kB >= 3 * p + 1 and 5 * kB <= 3 * p - 7]
    bf = [kB for kB in band if kB not in ok]
    if bf: band_fail.append((p, bf))
print({'partA_primes': len(cover), 'closed_form_band_failures': band_fail[:10]})
for p in sorted(cover):
    if p <= 113 or p in (199, 499, 997):
        beyond = [kB for kB in range(1, p - 3) if 3 * kB >= p + 5]
        print('p=%d hypotheses hold for kB in %s (beyond-W-ALL %d..%d; not covered: %s)' % (p, cover[p] if len(cover[p]) < 12 else '%d..%d (%d values%s)' % (min(cover[p]), max(cover[p]), len(cover[p]), '' if cover[p] == list(range(min(cover[p]), max(cover[p]) + 1)) else ', with holes'), beyond[0], beyond[-1], [kB for kB in beyond if kB not in cover[p]]))
# ---------- Part B / C
def lam_direct(p, kB, k, Q):
    # Lemma H lambda for an explicit pattern Q of W(p, kB): anti run 0, aligned 1..k-1, B = 1, beta = 0
    Q = set(Q); m = sum(1 for t in Q if (t - 1) % k not in Q)
    D = sum(-1 if t == 0 else 1 for t in Q)
    return min(p - m + 1, D + m - kB, fl(D + 1, 2) + 1) - (1 if MUT == 2 else 0)
def is_kill(p, kB, k, u, S):
    S = set(S); full = set(range(k)); us = sum(u[t] for t in S) % p
    lo, hi = 1 - lam_direct(p, kB, k, full - S), lam_direct(p, kB, k, S) - 1
    return any((y - us) % p == 0 for y in range(lo, hi + 1))
def replay(p, kB, u_T, Tlist):
    # u_T: dict t -> residue for t in T (other runs irrelevant: every pattern used is a subset of T)
    d, N, L, U, j1, s = params(p, kB, len(Tlist))
    k = p + kB + 1
    alpha, omega = 3 - cl(s, 2), fl(s, 2) - 1
    h, r = min(omega, fl(d, 2)), -alpha
    u = [0] * k
    for t in Tlist: u[t] = u_T[t]
    # Step 1 (seed)
    if MUT != 3:
        for t in Tlist:
            if not any((u[t] - y) % p == 0 for y in range(alpha, omega + 1)):
                S = [x for x in Tlist if x != t][:s]
                for cand in (S, S + [t]):
                    if is_kill(p, kB, k, u, cand): return 'step1', cand
                return 'NOKILL-step1', None
    # canonical lifts
    x = {}
    for t in Tlist:
        cands = [y for y in range(L(1), U(1) + 1) if (y - u[t]) % p == 0]
        if not cands:
            if is_kill(p, kB, k, u, [t]): return 'singleton', [t]
            return 'NOKILL-singleton', None
        x[t] = cands[0]
        if MUT != 3 and not (-r <= x[t] <= h): return 'NOKILL-liftrange', None
    order = sorted(Tlist, key=lambda t: (x[t], t))
    # Steps 2-3: bottom chain and top chain
    for chain in (order, order[::-1]):
        X = 0
        for j in range(1, N + 1):
            X += x[chain[j - 1]]
            if not (L(j) <= X <= U(j)):
                S = chain[:j]
                if is_kill(p, kB, k, u, S): return 'chain', S
                return 'NOKILL-chain@%d' % j, None
    return 'NOKILL-final', None
stats = {}; fails = []
for p in range(11, PREP + 1):
    if not isprime(p): continue
    for kB in range(1, p - 3):
        if not hypotheses(p, kB)[0]: continue
        d, N, L, U, j1, s = params(p, kB)
        if MUT == 1: N = N - 2
        Tlist = [2 * i + 1 for i in range(N)]
        for trial in range(TRIALS):
            mode = trial % 5
            if mode == 0: u_T = {t: rng.randrange(p) for t in Tlist}
            elif mode == 1:
                X1 = rng.randrange(1, N); ones = set(rng.sample(Tlist, X1)); u_T = {t: (1 if t in ones else 0) for t in Tlist}
            elif mode == 2:
                c = rng.randrange(p); u_T = {t: (c + (rng.randrange(-1, 2) if rng.random() < 0.2 else 0)) % p for t in Tlist}
            elif mode == 3:
                u_T = {t: rng.choice([0, 1, 1, 1, p - 1, 2]) for t in Tlist}
            else:
                u_T = {t: rng.randrange(-(cl(s, 2) - 3), fl(s, 2)) % p for t in Tlist}
            tag, S = replay(p, kB, u_T, Tlist)
            key = tag.split('@')[0]
            stats[key] = stats.get(key, 0) + 1
            if tag.startswith('NOKILL') and len(fails) < 5: fails.append((p, kB, tag))
print({'partB_MUT': MUT, 'outcomes': stats, 'first_failures': fails})

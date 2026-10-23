# ind_replayB.py -- c4 T4 receipts for proof-INDB.md ([F], aids only).  Theorem IND-B: all-singleton all-odd words with
# k runs, B anti runs at ANY positions, kappa = k - p, kB = k - p - B, item (iii): p + 2 <= k <= 2p - 3, 1 <= B <= k - p - 1.
# T: N := ceil((k - B)/2) pairwise non-adjacent aligned runs.  Arcs for S subset of T, |S| = j:
#   L_j = min(p-j+1, 2j-kB, floor((j+B)/2)+1),  U_j = p - min(p-j+1, p-B, floor((k-B-j)/2)+1),  delta := p - kB.
# j1 := min{j : 2j - kB >= floor((j+B)/2) + 1};  top size jt := min{j : U_j = j - 1 for all j' in [j, N]} (computed);
# seed s := smallest size >= 1 with s + 1 <= N, U_s = s - 1, U_(s+1) = s, L_s = floor((s+B)/2)+1, L_(s+1) = floor((s+1+B)/2)+1;
# A = [alpha, omega] = [L_(s+1) - U_s, U_(s+1) - L_s];  h = min(omega, U_1), r = -alpha.
# Hypotheses: (S1) seed exists; (S3) omega <= p + L_1 - 1, alpha >= L_1;  (C) as in proof-IND-r1.md;
# (L) X-range: 1 <= L_N and U_N = N - 1; top: U_jt = jt - 1 with jt <= N - 1; bottom: j1 <= N, L_j1 = floor((j1+B)/2)+1;
#     contradiction  jt - 1 < N - j1 + L_j1  (i.e. X <= jt - 1 and X >= N - j1 + L_j1 cannot both hold).
# Part A: coverage over all item-(iii) all-singleton classes (p, k, B), primes 11 <= p <= PMAX.
# Part B: literal replay on random words (random anti positions) and random/structured u, p <= PREP; windows recomputed
#   from the explicit pattern with Lemma H (beta = 0): lambda(Q) = min(p-m+1, D_Q + m - kB, floor((D_Q + B)/2) + 1).
# Part C: MUT=1 T shrunk by 2; MUT=2 windows shrunk by 1; MUT=3 seed skipped.
# Usage: python3 -B ind_replayB.py PMAX PREP TRIALS SEED MUT [indepB_receipt]
import sys, random, json
PMAX, PREP, TRIALS, SEED, MUT = (int(v) for v in sys.argv[1:6])
REC = sys.argv[6] if len(sys.argv) > 6 else None
rng = random.Random(SEED)
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
fl = lambda x, y: x // y
cl = lambda x, y: -((-x) // y)
def arcs(p, k, B, N):
    kB = k - p - B
    L = lambda j: min(p - j + 1, 2 * j - kB, fl(j + B, 2) + 1)
    U = lambda j: p - min(p - j + 1, p - B, fl(k - B - j, 2) + 1)
    return kB, L, U
def hyp(p, k, B, N=None):
    if N is None: N = cl(k - B, 2)
    kB, L, U = arcs(p, k, B, N)
    for j in range(1, N + 1):
        if L(j) > U(j): return False, 'window-full@%d' % j, None
    s = None
    for c in range(1, N):
        if U(c) == c - 1 and U(c + 1) == c and L(c) == fl(c + B, 2) + 1 and L(c + 1) == fl(c + 1 + B, 2) + 1:
            s = c; break
    if s is None: return False, 'S1', None
    alpha, omega = L(s + 1) - U(s), U(s + 1) - L(s)
    if omega - alpha + 1 >= p: return False, 'A-wide', None
    if not (omega <= p + L(1) - 1 and alpha >= L(1)): return False, 'S3', None
    h, r = min(omega, U(1)), -alpha
    for j in range(1, N):
        if not (max(L(j), -j * r) - r >= U(j + 1) + 1 - p): return False, 'C1@%d' % j, None
        if not (min(U(j), j * h) + h <= p + L(j + 1) - 1): return False, 'C2@%d' % j, None
    if not (L(N) >= 1 and U(N) == N - 1): return False, 'X-range', None
    jt = None
    for c in range(1, N):
        if all(U(jj) == jj - 1 for jj in range(c, N + 1)): jt = c; break
    if jt is None: return False, 'top', None
    j1 = 1
    while not (2 * j1 - kB >= fl(j1 + B, 2) + 1): j1 += 1
    if not (j1 <= N and L(j1) == fl(j1 + B, 2) + 1): return False, 'bottom', None
    if not (jt - 1 < N - j1 + L(j1)): return False, 'L', None
    return True, 'ok', dict(s=s, alpha=alpha, omega=omega, h=h, r=r, jt=jt, j1=j1, N=N)
# ---------- Part A
cov = {}
for p in range(11, PMAX + 1):
    if not isprime(p): continue
    for k in range(p + 2, 2 * p - 2):
        for B in range(1, k - p):
            ok, why, _ = hyp(p, k, B)
            cov[(p, k, B)] = (ok, why)
tot = len(cov); okc = sum(1 for v in cov.values() if v[0])
print({'partA_classes': tot, 'hypotheses_hold': okc})
for p in sorted(set(q for q, _, _ in cov)):
    cls = [(k, B) for (q, k, B) in cov if q == p]
    good = [(k, B) for (k, B) in cls if cov[(p, k, B)][0]]
    if p <= 31 or p in (43, 61, 101, 199):
        bad = [(k, B, k - p - B) for (k, B) in cls if not cov[(p, k, B)][0]]
        print('p=%d classes %d covered %d | uncovered (k, B, kB): %s' % (p, len(cls), len(good), bad if len(bad) <= 40 else str(bad[:40]) + ' ... (%d)' % len(bad)))
if REC:
    rows = [json.loads(l) for l in open(REC) if l.startswith('{') and 'status' not in l]
    inconsistent = [(r['p'], r['k'], r['B']) for r in rows if (r['p'], r['k'], r['B']) in cov and cov[(r['p'], r['k'], r['B'])][0] and r['feasible_at_N']]
    infeas_not_cov = [(r['p'], r['k'], r['B'], r['k'] - r['p'] - r['B']) for r in rows if (r['p'], r['k'], r['B']) in cov and not cov[(r['p'], r['k'], r['B'])][0] and r['feasible_at_N'] is False]
    feas = [(r['p'], r['k'], r['B'], r['k'] - r['p'] - r['B']) for r in rows if r['feasible_at_N']]
    print({'crosscheck_with': REC, 'covered_but_indepB_feasible': inconsistent, 'indepB_infeasible_not_covered': len(infeas_not_cov),
           'examples_infeasible_not_covered': infeas_not_cov[:12], 'indepB_feasible_classes': len(feas), 'examples_feasible': feas[:12]})
# ---------- Part B / C
def lam_direct(p, kB, B, k, anti, Q):
    Q = set(Q); m = sum(1 for t in Q if (t - 1) % k not in Q)
    D = sum(-1 if t in anti else 1 for t in Q)
    return min(p - m + 1, D + m - kB, fl(D + B, 2) + 1) - (1 if MUT == 2 else 0)
def is_kill(p, kB, B, k, anti, u, S):
    S = set(S); full = set(range(k)); us = sum(u[t] for t in S) % p
    lo, hi = 1 - lam_direct(p, kB, B, k, anti, full - S), lam_direct(p, kB, B, k, anti, S) - 1
    return any((y - us) % p == 0 for y in range(lo, hi + 1))
stats = {}; fails = []
for p in range(11, PREP + 1):
    if not isprime(p): continue
    for k in range(p + 2, 2 * p - 2):
        for B in range(1, k - p):
            ok, why, P = hyp(p, k, B)
            if not ok: continue
            kB, L, U = arcs(p, k, B, P['N'])
            for trial in range(TRIALS):
                anti = set(rng.sample(range(k), B))
                # independent aligned runs: greedy along the cycle starting after an anti run
                start = (min(anti) + 1) % k
                T = []; prev_in = False
                for i in range(k):
                    t = (start + i) % k
                    if t in anti: prev_in = False; continue
                    if not prev_in and (not T or (t - T[0]) % k != k - 1): T.append(t); prev_in = True
                    else: prev_in = False
                N = P['N'] - (2 if MUT == 1 else 0)
                assert len(T) >= P['N'], (p, k, B, len(T), P['N'])
                T = T[:N]
                mode = trial % 5
                if mode == 0: uT = {t: rng.randrange(p) for t in T}
                elif mode == 1:
                    X1 = rng.randrange(1, N); ones = set(rng.sample(T, X1)); uT = {t: (1 if t in ones else 0) for t in T}
                elif mode == 2:
                    c = rng.randrange(p); uT = {t: (c + (rng.randrange(-1, 2) if rng.random() < 0.2 else 0)) % p for t in T}
                elif mode == 3: uT = {t: rng.choice([0, 1, 1, 1, p - 1, 2]) for t in T}
                else: uT = {t: rng.randrange(P['alpha'], P['omega'] + 1) % p for t in T}
                u = [0] * k
                for t in T: u[t] = uT[t]
                tag = None
                if MUT != 3:
                    for t in T:
                        if not any((u[t] - y) % p == 0 for y in range(P['alpha'], P['omega'] + 1)):
                            S = [x for x in T if x != t][:P['s']]
                            for cand in (S, S + [t]):
                                if is_kill(p, kB, B, k, anti, u, cand): tag = 'step1'; break
                            if tag is None: tag = 'NOKILL-step1'
                            break
                if tag is None:
                    x = {}
                    for t in T:
                        cands = [y for y in range(L(1), U(1) + 1) if (y - u[t]) % p == 0]
                        if not cands:
                            tag = 'singleton' if is_kill(p, kB, B, k, anti, u, [t]) else 'NOKILL-singleton'; break
                        x[t] = cands[0]
                    if tag is None:
                        order = sorted(T, key=lambda t: (x[t], t))
                        for chain in (order, order[::-1]):
                            X = 0
                            for j in range(1, N + 1):
                                X += x[chain[j - 1]]
                                if not (L(j) <= X <= U(j)):
                                    tag = 'chain' if is_kill(p, kB, B, k, anti, u, chain[:j]) else 'NOKILL-chain'
                                    break
                            if tag: break
                        if tag is None: tag = 'NOKILL-final'
                stats[tag] = stats.get(tag, 0) + 1
                if tag.startswith('NOKILL') and len(fails) < 5: fails.append((p, k, B, tag))
print({'partB_MUT': MUT, 'outcomes': stats, 'first_failures': fails})

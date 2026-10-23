# ind_star2.py -- c4 T4 receipts for proof-INDstar.md ([F], aids only).  Differs from ind_star.py ONLY in (S):
# the lift range is R := {y in [L_1, U_1] : y = (an element of A_s) mod p for EVERY s in [1, N-1]}, A_s :=
# [L_(s+1) - U_s, U_(s+1) - L_s] (arcs of width >= p impose nothing); alpha := min R, h := max R (R empty: every
# run is killed by a singleton or a seed pair).  Then (C), (L*) as below with these alpha, h.
#  Theorem IND* (general form of Theorem IND):
# all-singleton all-odd words, k runs, B anti runs at ANY positions, kB = k - p - B; item (iii): p+2 <= k <= 2p-3,
# 1 <= B <= k-p-1.  T: N pairwise non-adjacent aligned runs (N <= ceil((k-B)/2) always realisable).  Arcs (S subset T,
# |S| = j): L_j = min(p-j+1, 2j-kB, floor((j+B)/2)+1), U_j = p - min(p-j+1, p-B, floor((k-B-j)/2)+1).
# Hypotheses for a pair (N, s), 1 <= s <= N-1:
#  (W) L_j <= U_j for 1 <= j <= N (no full window; otherwise any j-subset already kills);
#  (S) A := [alpha, omega] = [L_(s+1) - U_s, U_(s+1) - L_s] has omega - alpha + 1 < p, alpha >= L_1, omega <= p + L_1 - 1;
#      put h := min(omega, U_1);
#  (C) for 1 <= j <= N-1: max(L_j, j*alpha) + alpha >= U_(j+1) + 1 - p and min(U_j, j*h) + h <= p + L_(j+1) - 1;
#  (L*) for every integer X with max(L_N, N*alpha) <= X <= min(U_N, N*h), the balanced vector with sum X (values
#      q = floor(X/N), q+1) violates s_j >= L_j or t_j <= U_j for some 1 <= j <= N-1.
# Part A: coverage (first N from ceil((k-B)/2) downwards, all s) over item-(iii) all-singleton classes, primes p <= PMAX,
#   cross-checked against the parity-class DFS receipt (covered => infeasible).  Part B: literal replay (random anti
#   positions, random/structured u) for p <= PREP with independent explicit-pattern windows.  Part C: MUT=1 N-2;
#   MUT=2 windows shrunk by 1; MUT=3 seed skipped.
# Usage: python3 -B ind_star.py PMAX PREP TRIALS SEED MUT [indepB_receipt]
import sys, random, json
PMAX, PREP, TRIALS, SEED, MUT = (int(v) for v in sys.argv[1:6])
REC = sys.argv[6] if len(sys.argv) > 6 else None
rng = random.Random(SEED)
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
fl = lambda x, y: x // y
def arcs(p, k, B):
    kB = k - p - B
    L = [None] + [min(p - j + 1, 2 * j - kB, fl(j + B, 2) + 1) for j in range(1, k + 1)]
    U = [None] + [p - min(p - j + 1, p - B, fl(k - B - j, 2) + 1) for j in range(1, k + 1)]
    return kB, L, U
def lift_range(p, k, B, N, L, U):
    R = []
    for y in range(L[1], U[1] + 1):
        ok = True
        for s in range(1, N):
            lo, hi = L[s + 1] - U[s], U[s + 1] - L[s]
            if hi - lo + 1 >= p: continue
            if (y - lo) % p > hi - lo: ok = False; break
        if ok: R.append(y)
    return R
def check(p, k, B, N, L, U):
    R = lift_range(p, k, B, N, L, U)
    if not R: return ('empty-lifts', None, None, None)
    alpha, h = min(R), max(R)
    for j in range(1, N):
        if max(L[j], j * alpha) + alpha < U[j + 1] + 1 - p: return None
        if min(U[j], j * h) + h > p + L[j + 1] - 1: return None
    Xlo, Xhi = max(L[N], N * alpha), min(U[N], N * h)
    for X in range(Xlo, Xhi + 1):
        q, rho = divmod(X, N)
        good = True
        for j in range(1, N):
            sj = j * q + max(0, j - (N - rho)); tj = j * q + min(j, rho)
            if sj < L[j] or tj > U[j]: good = False; break
        if good: return None
    return ('ok', alpha, h, len(R))
def covered(p, k, B):
    kB, L, U = arcs(p, k, B)
    Nmax = -((-(k - B)) // 2)
    for N in range(Nmax, 1, -1):
        if any(L[j] > U[j] for j in range(1, N + 1)): return (N, 'fullwindow', None)
        r = check(p, k, B, N, L, U)
        if r: return (N, 'seedall', r)
    return None
cov = {}
for p in range(11, PMAX + 1):
    if not isprime(p): continue
    for k in range(p + 2, 2 * p - 2):
        for B in range(1, k - p):
            cov[(p, k, B)] = covered(p, k, B)
print({'partA_classes': len(cov), 'covered': sum(1 for v in cov.values() if v)})
for p in sorted(set(q for q, _, _ in cov)):
    cls = [(k, B) for (q, k, B) in cov if q == p]
    unc = [(k, B, k - p - B) for (k, B) in cls if not cov[(p, k, B)]]
    full = sum(1 for (k, B) in cls if cov[(p, k, B)] and cov[(p, k, B)][1] == 'fullwindow')
    print('p=%d classes %d covered %d (full-window %d) | uncovered (k, B, kB): %s' % (p, len(cls), len(cls) - len(unc), full, unc if len(unc) <= 60 else str(unc[:60]) + ' ... (%d)' % len(unc)))
if REC:
    rows = [json.loads(l) for l in open(REC) if l.startswith('{') and 'status' not in l]
    incons = [(r['p'], r['k'], r['B']) for r in rows if (r['p'], r['k'], r['B']) in cov and cov[(r['p'], r['k'], r['B'])] and r['feasible_at_N']]
    inf_unc = [(r['p'], r['k'], r['B'], r['k'] - r['p'] - r['B']) for r in rows if (r['p'], r['k'], r['B']) in cov and not cov[(r['p'], r['k'], r['B'])] and r['feasible_at_N'] is False]
    print({'crosscheck_with': REC, 'covered_but_parity_DFS_feasible': incons, 'parity_DFS_infeasible_but_uncovered': len(inf_unc), 'examples': inf_unc[:20]})
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
for (p, k, B), c in sorted(cov.items()):
    if p > PREP or not c: continue
    N0, s, r = c
    kB, L, U = arcs(p, k, B)
    for trial in range(TRIALS):
        anti = set(rng.sample(range(k), B))
        start = (min(anti) + 1) % k; T = []; prev = False
        for i in range(k):
            t = (start + i) % k
            if t in anti: prev = False; continue
            if not prev and (not T or (t - T[0]) % k != k - 1): T.append(t); prev = True
            else: prev = False
        assert len(T) >= N0
        N = N0 - (2 if MUT == 1 else 0)
        T = T[:N]
        mode = trial % 5
        if mode == 0: uT = {t: rng.randrange(p) for t in T}
        elif mode == 1:
            X1 = rng.randrange(0, N + 1); ones = set(rng.sample(T, X1)); uT = {t: (1 if t in ones else 0) for t in T}
        elif mode == 2:
            c0 = rng.randrange(p); uT = {t: (c0 + (rng.randrange(-1, 2) if rng.random() < 0.2 else 0)) % p for t in T}
        elif mode == 3: uT = {t: rng.choice([0, 1, 1, 1, p - 1, 2]) for t in T}
        else: uT = {t: (rng.randrange(r[1], r[2] + 1) if (s != 'fullwindow' and r[1] is not None) else rng.randrange(p)) % p for t in T}
        u = [0] * k
        for t in T: u[t] = uT[t]
        tag = None
        if s == 'fullwindow':
            jf = next(j for j in range(1, N0 + 1) if L[j] > U[j])
            tag = 'fullwindow' if is_kill(p, kB, B, k, anti, u, T[:jf]) else 'NOKILL-fullwindow'
        else:
            if MUT != 3:
                for t in T:
                    for s2 in range(1, N0):
                        lo2, hi2 = L[s2 + 1] - U[s2], U[s2 + 1] - L[s2]
                        if hi2 - lo2 + 1 >= p: continue
                        if (u[t] - lo2) % p > hi2 - lo2:
                            S = [x for x in T if x != t][:s2]
                            for cand in (S, S + [t]):
                                if is_kill(p, kB, B, k, anti, u, cand): tag = 'step1'; break
                            if tag is None: tag = 'NOKILL-step1'
                            break
                    if tag: break
                if tag is None and r[1] is None:
                    tag = 'NOKILL-emptyR'
            if tag is None:
                x = {}
                for t in T:
                    cands = [y for y in range(L[1], U[1] + 1) if (y - u[t]) % p == 0]
                    if not cands:
                        tag = 'singleton' if is_kill(p, kB, B, k, anti, u, [t]) else 'NOKILL-singleton'; break
                    x[t] = cands[0]
                if tag is None and MUT != 3 and r[1] is not None and any(not (r[1] <= x[t] <= r[2]) for t in T):
                    tag = 'NOKILL-liftrange'
                if tag is None:
                    order = sorted(T, key=lambda t: (x[t], t))
                    for chain in (order, order[::-1]):
                        X = 0
                        for j in range(1, N + 1):
                            X += x[chain[j - 1]]
                            if not (L[j] <= X <= U[j]):
                                tag = 'chain' if is_kill(p, kB, B, k, anti, u, chain[:j]) else 'NOKILL-chain'
                                break
                        if tag: break
                    if tag is None: tag = 'NOKILL-final'
        stats[tag] = stats.get(tag, 0) + 1
        if tag.startswith('NOKILL') and len(fails) < 5: fails.append((p, k, B, tag))
print({'partB_MUT': MUT, 'outcomes': stats, 'first_failures': fails})

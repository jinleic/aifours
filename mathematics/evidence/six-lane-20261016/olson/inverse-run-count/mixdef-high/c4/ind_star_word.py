# ind_star_word.py -- c4 T4 ([F], aids only): literal replay of Theorem IND* on EXPLICIT random item-(iii) words with
# excess (runs pure or (1,1)-pairs; d_t = a_t - b_t), p <= PMAX.  For each word: T := greedy maximal set of pairwise
# non-adjacent runs with d_t = 1 and r_t = 1 (single rho_1 letters); N := |T| (also checks N >= ceil((k - B - E)/2));
# hypotheses (W), R, (C), (L*) evaluated with the arcs of ind_star_ex.py (D = 2p - k + 2kB); if they hold, TRIALS random
# u in Z_p^T are replayed through Steps 1-4 and every reported kill is re-checked with lambda computed from the explicit
# pattern and the word's d_t (Lemma H, beta = 0).  MUT=2: windows shrunk by one in the kill test (must fail sometimes).
# Usage: python3 -B ind_star_word.py PMAX WORDS TRIALS SEED MUT
import sys, random
PMAX, WORDS, TRIALS, SEED, MUT = (int(v) for v in sys.argv[1:6])
rng = random.Random(SEED)
fl = lambda x, y: x // y
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def random_word(p):
    # item (iii): p+1 <= k <= 2p-3 (k = p+1 only if not ZSI-B; we just require kB >= 1), R <= 2p-3, 1 <= B <= kappa-1
    for _ in range(1000):
        k = rng.randint(p + 2, 2 * p - 3)
        kappa = rng.randint(k - p, (k - 3) // 2)
        R = 2 * p - k + 2 * kappa; E = R - k
        if E < 0: continue
        B = rng.randint(1, kappa - 1) if kappa >= 2 else 0
        if B < 1: continue
        # build runs: start with k single rho_1; distribute B (anti singles or pairs) and the excess E
        d = [1] * k; r = [1] * k
        idx = list(range(k)); rng.shuffle(idx)
        Bleft, Eleft, i = B, E, 0
        while Bleft > 0 and i < k:
            t = idx[i]; i += 1
            if Eleft >= 1 and rng.random() < 0.3:          # (1,1)-pair: d = 0, r = 2 (uses 1 excess, 1 of B)
                d[t] = 0; r[t] = 2; Eleft -= 1; Bleft -= 1
            else:
                bb = 1
                while bb < Bleft and Eleft >= 1 and rng.random() < 0.3: bb += 1; Eleft -= 1
                d[t] = -bb; r[t] = bb; Bleft -= bb
        if Bleft > 0: continue
        al = [t for t in range(k) if d[t] >= 1]
        while Eleft > 0 and al:
            t = rng.choice(al); d[t] += 1; r[t] += 1; Eleft -= 1
        if Eleft > 0: continue
        A = sum(max(dt, 0) for dt in d) + sum(1 for dt in d if dt == 0)
        Bc = sum(-dt for dt in d if dt < 0) + sum(1 for dt in d if dt == 0)
        if Bc != B or A + Bc != R or not (B <= A <= 2 * p - 1): continue
        return k, kappa, B, E, d, r
    return None
def arcs(p, k, kB, B, N):
    D = 2 * p - k + 2 * kB
    L = [None] + [min(p - j + 1, 2 * j - kB, fl(j + B, 2) + 1) for j in range(1, N + 2)]
    U = [None] + [p - min(p - j + 1, D - kB, fl(D - j + B, 2) + 1) for j in range(1, N + 2)]
    return L, U
def hyp(p, k, kB, B, N):
    L, U = arcs(p, k, kB, B, N)
    if any(L[j] > U[j] for j in range(1, N + 1)): return ('fullwindow', L, U, None)
    R = [y for y in range(L[1], U[1] + 1) if all((y - (L[s + 1] - U[s])) % p <= (U[s + 1] - L[s]) - (L[s + 1] - U[s]) for s in range(1, N) if (U[s + 1] - L[s]) - (L[s + 1] - U[s]) + 1 < p)]
    if not R: return ('emptyR', L, U, None)
    a, h = min(R), max(R)
    for j in range(1, N):
        if max(L[j], j * a) + a < U[j + 1] + 1 - p or min(U[j], j * h) + h > p + L[j + 1] - 1: return None
    for X in range(max(L[N], N * a), min(U[N], N * h) + 1):
        q, rho = divmod(X, N)
        if all(j * q + max(0, j - (N - rho)) >= L[j] and j * q + min(j, rho) <= U[j] for j in range(1, N)): return None
    return ('ok', L, U, (a, h))
stats = {}; fails = []; words = 0; covered = 0; badN = 0
for p in range(11, PMAX + 1):
    if not isprime(p): continue
    for w in range(WORDS):
        rw = random_word(p)
        if rw is None: continue
        k, kappa, B, E, d, r = rw; kB = kappa - B; words += 1
        T = []
        for t in range(k):
            if d[t] == 1 and r[t] == 1 and (not T or T[-1] != t - 1) and not (t == k - 1 and T and T[0] == 0):
                T.append(t)
        if len(T) < -((-(k - B - E)) // 2): badN += 1
        N = len(T)
        if N < 2: continue
        res = hyp(p, k, kB, B, N)
        if res is None: continue
        covered += 1
        tag0, L, U, ah = res
        def lam(Q):
            Q = set(Q); m = sum(1 for t in Q if (t - 1) % k not in Q); D = sum(d[t] for t in Q)
            return min(p - m + 1, D + m - kB, fl(D + B, 2) + 1) - (1 if MUT == 2 else 0)
        def kill(u, S):
            S = set(S); us = sum(u[t] for t in S) % p
            lo, hi = 1 - lam(set(range(k)) - S), lam(S) - 1
            return any((y - us) % p == 0 for y in range(lo, hi + 1))
        for trial in range(TRIALS):
            mode = trial % 3
            if mode == 0: uT = {t: rng.randrange(p) for t in T}
            elif mode == 1: X1 = rng.randrange(0, N + 1); ones = set(rng.sample(T, X1)); uT = {t: (1 if t in ones else 0) for t in T}
            else: uT = {t: rng.choice([0, 1, 1, 1, p - 1, 2]) for t in T}
            u = [0] * k
            for t in T: u[t] = uT[t]
            tag = None
            if tag0 == 'fullwindow':
                jf = next(j for j in range(1, N + 1) if L[j] > U[j])
                tag = 'fullwindow' if kill(u, T[:jf]) else 'NOKILL-fullwindow'
            else:
                for t in T:
                    for s in range(1, N):
                        lo, hi = L[s + 1] - U[s], U[s + 1] - L[s]
                        if hi - lo + 1 >= p: continue
                        if (u[t] - lo) % p > hi - lo:
                            S = [x for x in T if x != t][:s]
                            tag = 'step1' if (kill(u, S) or kill(u, S + [t])) else 'NOKILL-step1'
                            break
                    if tag: break
                if tag is None:
                    x = {}
                    for t in T:
                        c = [y for y in range(L[1], U[1] + 1) if (y - u[t]) % p == 0]
                        if not c: tag = 'singleton' if kill(u, [t]) else 'NOKILL-singleton'; break
                        x[t] = c[0]
                    if tag is None and tag0 == 'emptyR': tag = 'NOKILL-emptyR'
                    if tag is None and any(not (ah[0] <= x[t] <= ah[1]) for t in T): tag = 'NOKILL-liftrange'
                    if tag is None:
                        order = sorted(T, key=lambda t: (x[t], t))
                        for chain in (order, order[::-1]):
                            X = 0
                            for j in range(1, N + 1):
                                X += x[chain[j - 1]]
                                if not (L[j] <= X <= U[j]):
                                    tag = 'chain' if kill(u, chain[:j]) else 'NOKILL-chain'; break
                            if tag: break
                        if tag is None: tag = 'NOKILL-final'
            stats[tag] = stats.get(tag, 0) + 1
            if tag.startswith('NOKILL') and len(fails) < 5: fails.append((p, k, B, kB, E, d, tag))
print({'MUT': MUT, 'words': words, 'covered_words': covered, 'words_with_N_below_bound': badN, 'outcomes': stats, 'first_failures': fails[:3]})

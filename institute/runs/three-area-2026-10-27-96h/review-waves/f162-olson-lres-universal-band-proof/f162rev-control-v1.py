#!/usr/bin/env python3
"""f162rev-control-v1.py -- independent reviewer control for review wave
f162-olson-lres-universal-band-proof (Theorem U, D_2p, F=3p-2 reflections, R>=p+1 rotations).

Authored from scratch by reviewer ReviewF162OlsonLRES.  Imports NO author code and reads NO author data.
Encoding: element (a,e), a in F_p, e in {0,1}; code = a + p*e; rho_a=(a,0) rotation, sigma_a=(a,1) reflection;
(a,e)(b,f) = (a + (-1)^e b, e+f mod 2).  Identity = code 0.  A "selector" is a set of 2p original word positions
whose letters, multiplied in increasing ORIGINAL order, give the identity, using at most 2 rotations.

Sections
  A  algebra self-tests (conjugation formulas, transport identity (T), Add/Erase/Swap, cut change, automorphisms)
  B  p=3 exhaustive, method 1: whole-word subset-construction DFS over ALL words (no symmetry reduction)
  C  p=3 exhaustive, method 2: numpy direct product of every 2p-subset, first reflection normalised to sigma_0
  D  p=3 per-reflection-list DFS over the REF-failing projections + explicit counterexamples (brute-force verified)
  E  p=5 exhaustive: per-list DFS over orbit representatives of ALL REF-failing length-13 reflection lists
  F  Lemma A exhaustive checks + hypothesis-violating negatives
  G  Lemma N checks over ALL REF-failing lists (p=3, p=5) and ALL cyclic deletion orders
  H  proof-route constructor (independent re-implementation of sections 4-6 of the candidate), every pair E
  I  harness negative controls (corrupted selectors / wrong order must be rejected)
"""
import sys, os, json, time, math, random, itertools, hashlib, subprocess
from collections import Counter
from multiprocessing import Pool
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT_PATH = os.path.join(HERE, 'f162rev-control-v1-results.json')
NPROC = 10


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


# ----------------------------------------------------------------------------- group
def make_group(p):
    def mul_t(x, y):
        a, e = x
        b, f = y
        return ((a + (b if e == 0 else -b)) % p, (e + f) % 2)
    els = [(a, e) for e in (0, 1) for a in range(p)]
    code = {x: x[0] + p * x[1] for x in els}
    return [[code[mul_t(x, y)] for y in els] for x in els]


class Grp:
    def __init__(self, p):
        self.p = p
        self.MUL = make_group(p)
        n = 2 * p
        self.INV = [next(y for y in range(n) if self.MUL[x][y] == 0) for x in range(n)]

    def prod(self, seq):
        acc = 0
        for g in seq:
            acc = self.MUL[acc][g]
        return acc

    def conj(self, P, x):
        return self.MUL[self.MUL[P][x]][self.INV[P]]


def make_rmul(p):
    FULL = (1 << p) - 1

    def rotl(x, k):
        k %= p
        if k == 0:
            return x
        return ((x << k) | (x >> (p - k))) & FULL

    def rmul(m, g):
        low = m & FULL
        high = m >> p
        if g < p:
            return rotl(low, g) | (rotl(high, -g) << p)
        b = g - p
        return rotl(high, -b) | (rotl(low, b) << p)
    return rmul


def fmt(w, p):
    return " ".join(("r%d" % g) if g < p else ("s%d" % (g - p)) for g in w)


# ----------------------------------------------------------------------------- checkers
def has_selector(word, p, maxrot=2, rmul=None):
    """DP: exists original-order subsequence of exactly 2p letters, <= maxrot rotations, product identity."""
    if rmul is None:
        rmul = make_rmul(p)
    L = 2 * p
    reach = [[0] * (maxrot + 1) for _ in range(L + 1)]
    reach[0][0] = 1
    for g in word:
        isrot = 1 if g < p else 0
        for ln in range(L - 1, -1, -1):
            row = reach[ln]
            nxt = reach[ln + 1]
            for r in range(maxrot - isrot, -1, -1):
                m = row[r]
                if m:
                    nxt[r + isrot] |= rmul(m, g)
    return any(reach[L][r] & 1 for r in range(maxrot + 1))


def brute_selector(word, p, maxrot, G):
    """Direct enumeration of index subsets (original order); returns first selector found or None."""
    L = 2 * p
    rots = [i for i, g in enumerate(word) if g < p]
    refl = [i for i, g in enumerate(word) if g >= p]
    for k in range(0, maxrot + 1):
        if L - k > len(refl) or k > len(rots) or L - k < 0:
            continue
        for rs in itertools.combinations(rots, k):
            for fs in itertools.combinations(refl, L - k):
                idx = sorted(rs + fs)
                if G.prod([word[i] for i in idx]) == 0:
                    return idx
    return None


def verify_selector(word, sel, p, G, maxrot=2):
    """Returns (ok, reason)."""
    if len(sel) != 2 * p:
        return False, 'length'
    if len(set(sel)) != len(sel):
        return False, 'duplicate'
    if any(i < 0 or i >= len(word) for i in sel):
        return False, 'range'
    if sum(1 for i in sel if word[i] < p) > maxrot:
        return False, 'rotations'
    if G.prod([word[i] for i in sorted(sel)]) != 0:
        return False, 'product'
    return True, 'ok'


# ----------------------------------------------------------------------------- A: algebra
def algebra_tests(seed=11):
    out = {}
    rng = random.Random(seed)
    for p in (3, 5, 7, 11, 13):
        G = Grp(p)
        n = 2 * p
        MUL = G.MUL
        ax = all(MUL[MUL[x][y]][z] == MUL[x][MUL[y][z]] for x in range(n) for y in range(n) for z in range(n))
        ax = ax and all(MUL[0][x] == x == MUL[x][0] for x in range(n))
        okc = True
        for a in range(p):
            for e in (0, 1):
                g = a + p * e
                for b in range(p):
                    if G.conj(g, p + b) != p + (2 * a + (b if e == 0 else -b)) % p:
                        okc = False
                    if G.conj(g, b) != ((b if e == 0 else -b) % p):
                        okc = False
        oks = all(MUL[p + a][p + b] == (a - b) % p for a in range(p) for b in range(p))
        oka = True
        for u in range(1, p):
            for v in range(p):
                def phi(x):
                    return ((u * x) % p) if x < p else p + (u * (x - p) + v) % p
                for x in range(n):
                    for y in range(n):
                        if phi(MUL[x][y]) != MUL[phi(x)][phi(y)]:
                            oka = False
        okT = True
        nadd = nerase = nswap = 0
        okCut = True
        for trial in range(400):
            N = rng.randrange(4, 14)
            w = [rng.randrange(n) for _ in range(N)]
            S = set(i for i in range(N) if rng.random() < 0.5)
            T = [i for i in range(N) if i not in S and rng.random() < 0.6]
            P = 0
            tau = {}
            for i in range(N):
                tau[i] = G.conj(P, w[i])
                if i in S:
                    P = MUL[P][w[i]]
            lhs = G.prod([w[i] for i in sorted(S | set(T))])
            acc = 0
            for i in sorted(T):
                acc = MUL[acc][tau[i]]
            if lhs != MUL[acc][G.prod([w[i] for i in sorted(S)])]:
                okT = False
        for trial in range(3000):
            N = rng.randrange(4, 12)
            w = [p + rng.randrange(p) for _ in range(N)]
            S = set(i for i in range(N) if rng.random() < 0.5)
            if G.prod([w[i] for i in sorted(S)]) != 0:
                continue
            P = 0
            tau = {}
            for i in range(N):
                tau[i] = G.conj(P, w[i])
                if i in S:
                    P = MUL[P][w[i]]
            opt = [i for i in range(N) if i not in S]
            sel = sorted(S)
            for h, k in itertools.combinations(opt, 2):
                if tau[h] == tau[k]:
                    nadd += 1
                    if G.prod([w[i] for i in sorted(S | {h, k})]) != 0:
                        okT = False
            for h, k in itertools.combinations(sel, 2):
                if tau[h] == tau[k]:
                    nerase += 1
                    if G.prod([w[i] for i in sorted(S - {h, k})]) != 0:
                        okT = False
            for s in sel:
                for r in opt:
                    if tau[s] == tau[r]:
                        nswap += 1
                        if G.prod([w[i] for i in sorted((S - {s}) | {r})]) != 0:
                            okT = False
            j = rng.randrange(N)
            P2 = 0
            tau2 = {}
            for t in range(N):
                i = (j + t) % N
                tau2[i] = G.conj(P2, w[i])
                if i in S:
                    P2 = MUL[P2][w[i]]
            Q = G.prod([w[i] for i in sorted(S) if i < j])
            if any(tau2[i] != G.conj(G.INV[Q], tau[i]) for i in range(N)):
                okCut = False
        out[str(p)] = {'group_axioms': ax, 'conjugation_formulas': okc, 'sigma_a_sigma_b_eq_rho_a_minus_b': oks,
                       'affine_maps_are_automorphisms': oka, 'T_add_erase_swap_all_ok': okT,
                       'add_instances': nadd, 'erase_instances': nerase, 'swap_instances': nswap,
                       'cut_change_is_common_conjugation': okCut}
    return out


# ----------------------------------------------------------------------------- B: method 1
def method1_dfs(p, F, R, maxrot=2):
    rm = make_rmul(p)
    L = 2 * p
    n = 2 * p
    R1 = maxrot + 1
    BM = (1 << n) - 1

    def blk(ln, r):
        return (ln * R1 + r) * n
    tbits = 0
    for r in range(R1):
        tbits |= 1 << blk(L, r)
    memo = {}

    def step(reach, g):
        isrot = 1 if g < p else 0
        add = 0
        for ln in range(L):
            for r in range(R1 - isrot):
                m = (reach >> blk(ln, r)) & BM
                if m:
                    add |= rm(m, g) << blk(ln + 1, r + isrot)
        return reach | add

    def rec(nf, nr, reach):
        if reach & tbits:
            return 0, math.comb(nf + nr, nr) * p ** (nf + nr)
        if nf == 0 and nr == 0:
            return 1, 1
        key = (nf, nr, reach)
        v = memo.get(key)
        if v is not None:
            return v
        bad = tot = 0
        if nf:
            for b in range(p):
                x, y = rec(nf - 1, nr, step(reach, p + b))
                bad += x
                tot += y
        if nr:
            for b in range(p):
                x, y = rec(nf, nr - 1, step(reach, b))
                bad += x
                tot += y
        memo[key] = (bad, tot)
        return bad, tot
    t0 = time.time()
    bad, tot = rec(F, R, 1 << blk(0, 0))
    return {'p': p, 'F': F, 'R': R, 'maxrot': maxrot, 'bad_words': bad, 'words_covered': tot,
            'expected_words': math.comb(F + R, R) * p ** (F + R), 'memo_states': len(memo),
            'seconds': round(time.time() - t0, 2)}


# ----------------------------------------------------------------------------- C: method 2
def method2_numpy(p, F, R, rotcounts):
    G = Grp(p)
    n = 2 * p
    MULF = np.array([G.MUL[x][y] for x in range(n) for y in range(n)], dtype=np.int64)
    N = F + R
    L = 2 * p
    nvar = F - 1 + R
    grid = np.array(list(itertools.product(range(p), repeat=nvar)), dtype=np.int64).T
    M = grid.shape[1]
    bad_total = 0
    words = 0
    nsubsets = 0
    t0 = time.time()
    for rpos in itertools.combinations(range(N), R):
        rset = set(rpos)
        refl_pos = [i for i in range(N) if i not in rset]
        W = np.empty((N, M), dtype=np.int64)
        W[refl_pos[0]] = p
        k = 0
        for i in refl_pos[1:]:
            W[i] = p + grid[k]
            k += 1
        for i in rpos:
            W[i] = grid[k]
            k += 1
        found = np.zeros(M, dtype=bool)
        for kr in rotcounts:
            if kr > R or L - kr > F or L - kr < 0:
                continue
            for rs in itertools.combinations(rpos, kr):
                for fs in itertools.combinations(refl_pos, L - kr):
                    idx = sorted(rs + fs)
                    nsubsets += 1
                    acc = W[idx[0]].copy()
                    for i in idx[1:]:
                        acc = MULF[acc * n + W[i]]
                    found |= (acc == 0)
        bad_total += int((~found).sum())
        words += M
    return {'p': p, 'F': F, 'R': R, 'rotation_counts_allowed': list(rotcounts),
            'normalised_words': words, 'bad_normalised_words': bad_total,
            'implied_bad_all_words': bad_total * p, 'subset_products_evaluated_per_word_avg': nsubsets / math.comb(N, R),
            'seconds': round(time.time() - t0, 2)}


# ----------------------------------------------------------------------------- REF-failing lists
def ref_fail_lists(p, F):
    rm = make_rmul(p)
    L = 2 * p
    n = 2 * p
    BM = (1 << n) - 1
    tgt = 1 << (L * n)
    out = []
    dead = set()

    def step(reach, b):
        g = p + b
        add = 0
        for ln in range(L):
            m = (reach >> (ln * n)) & BM
            if m:
                add |= rm(m, g) << ((ln + 1) * n)
        return reach | add

    def rec(prefix, reach):
        if reach & tgt:
            return False
        k = F - len(prefix)
        if k == 0:
            out.append(tuple(prefix))
            return True
        key = (k, reach)
        if key in dead:
            return False
        anyok = False
        for b in range(p):
            prefix.append(b)
            if rec(prefix, step(reach, b)):
                anyok = True
            prefix.pop()
        if not anyok:
            dead.add(key)
        return anyok
    rec([], 1)
    return out


def symmetry_images(X, p):
    for u in range(1, p):
        for v in range(p):
            Y = tuple((u * x + v) % p for x in X)
            yield Y
            yield tuple(reversed(Y))


def orbit_reps(Xs, p):
    S = set(Xs)
    reps = {}
    closed = True
    for X in Xs:
        imgs = list(symmetry_images(X, p))
        if not all(Y in S for Y in imgs):
            closed = False
        c = min(imgs)
        reps[c] = reps.get(c, 0) + 1
    return reps, closed


def ref_selector_dp(labels, p, G):
    """labels: reflection codes. Returns index list (into labels) of a 2p identity subsequence, or None."""
    L = 2 * p
    n = 2 * p
    F = len(labels)
    dp = [[0] * (L + 1) for _ in range(F + 1)]
    dp[0][0] = 1
    for k in range(F):
        g = labels[k]
        for ln in range(L + 1):
            dp[k + 1][ln] |= dp[k][ln]
            if ln < L:
                m = dp[k][ln]
                if m:
                    for x in range(n):
                        if m >> x & 1:
                            dp[k + 1][ln + 1] |= 1 << G.MUL[x][g]
    if not (dp[F][L] & 1):
        return None
    sel = []
    ln = L
    target = 0
    for k in range(F, 0, -1):
        if dp[k - 1][ln] >> target & 1:
            continue
        g = labels[k - 1]
        target = G.MUL[target][G.INV[g]]
        sel.append(k - 1)
        ln -= 1
    assert ln == 0 and target == 0
    return sorted(sel)


# ----------------------------------------------------------------------------- per-list DFS (D, E)
def list_dfs(X, p, R, maxrot=2, collect=0):
    """All linear words whose reflection projection is exactly X (labels), R rotations anywhere, any values.
    Returns (bad_count, states, examples)."""
    rm = make_rmul(p)
    L = 2 * p
    n = 2 * p
    R1 = maxrot + 1
    BM = (1 << n) - 1

    def blk(ln, r):
        return (ln * R1 + r) * n
    tbits = 0
    for r in range(R1):
        tbits |= 1 << blk(L, r)
    F = len(X)
    memo = {}

    def step(reach, g):
        isrot = 1 if g < p else 0
        add = 0
        for ln in range(L):
            for r in range(R1 - isrot):
                m = (reach >> blk(ln, r)) & BM
                if m:
                    add |= rm(m, g) << blk(ln + 1, r + isrot)
        return reach | add

    def rec(i, j, reach):
        if reach & tbits:
            return 0
        if i == F and j == R:
            return 1
        key = (i, j, reach)
        v = memo.get(key)
        if v is not None:
            return v
        tot = 0
        if i < F:
            tot += rec(i + 1, j, step(reach, p + X[i]))
        if j < R:
            for b in range(p):
                tot += rec(i, j + 1, step(reach, b))
        memo[key] = tot
        return tot
    bad = rec(0, 0, 1 << blk(0, 0))
    examples = []
    if collect and bad:
        def rec2(i, j, reach, w):
            if len(examples) >= collect:
                return
            if reach & tbits:
                return
            if i == F and j == R:
                examples.append(list(w))
                return
            if memo.get((i, j, reach), 1) == 0:
                return
            if i < F:
                w.append(p + X[i])
                rec2(i + 1, j, step(reach, p + X[i]), w)
                w.pop()
            if j < R:
                for b in range(p):
                    w.append(b)
                    rec2(i, j + 1, step(reach, b), w)
                    w.pop()
        rec2(0, 0, 1 << blk(0, 0), [])
    return bad, len(memo), examples


def task_list_dfs(args):
    X, p, R = args
    t0 = time.time()
    bad, states, _ = list_dfs(X, p, R)
    return X, R, bad, states, round(time.time() - t0, 2)


# ----------------------------------------------------------------------------- F: Lemma A
def lemmaA_chunk(args):
    """Cyclic adjacent-distinct lists of length n=p+2h, first label 0, decoded from step-index range [lo,hi).
    mode 'distinct' (hypothesis lists). Returns histogram of maximal even identity length and violations."""
    p, h, lo, hi = args
    n = p + 2 * h
    FULL = (1 << p) - 1
    idx = np.arange(lo, hi, dtype=np.int64)
    X = np.zeros((n, idx.size), dtype=np.int64)
    rem = idx.copy()
    cur = np.zeros(idx.size, dtype=np.int64)
    for t in range(1, n):
        dgt = rem % (p - 1)
        rem //= (p - 1)
        cur = (cur + dgt + 1) % p
        X[t] = cur
    keep = X[n - 1] != 0
    X = X[:, keep]
    return lemmaA_stats(X, p, h)


def lemmaA_stats(X, p, h):
    n = X.shape[0]
    B = X.shape[1]
    FULL = (1 << p) - 1
    hist = Counter()
    viol_examples = []
    if B == 0:
        return {'lists': 0, 'violations': 0, 'hist': {}, 'violation_examples': []}
    reach = np.zeros((n + 1, B), dtype=np.int64)
    reach[0] = 1
    for t in range(n):
        b = X[t]
        kb = b % p
        kn = (-b) % p
        for ln in range(t, -1, -1):
            m = reach[ln]
            low = m & FULL
            high = m >> p
            sl = ((low << kb) | (low >> ((p - kb) % p))) & FULL
            sh = ((high << kn) | (high >> ((p - kn) % p))) & FULL
            reach[ln + 1] |= sh | (sl << p)
    best = np.zeros(B, dtype=np.int64)
    for ln in range(2, n + 1, 2):
        best = np.where(reach[ln] & 1, ln, best)
    vals, cts = np.unique(best, return_counts=True)
    for v, c in zip(vals, cts):
        hist[int(v)] += int(c)
    bad = np.nonzero(best < 2 * h + 2)[0]
    for k in bad[:3]:
        viol_examples.append([int(x) for x in X[:, k]])
    return {'lists': int(B), 'violations': int(bad.size), 'hist': dict(hist), 'violation_examples': viol_examples}


def merge_lemmaA(parts, p, h):
    tot = {'p': p, 'h': h, 'n': p + 2 * h, 'lists': 0, 'violations': 0, 'max_even_identity_length_histogram': Counter(),
           'violation_examples': []}
    for r in parts:
        tot['lists'] += r['lists']
        tot['violations'] += r['violations']
        for k, v in r['hist'].items():
            tot['max_even_identity_length_histogram'][k] += v
        if len(tot['violation_examples']) < 3:
            tot['violation_examples'] += r['violation_examples'][:3 - len(tot['violation_examples'])]
    tot['max_even_identity_length_histogram'] = {str(k): v for k, v in sorted(tot['max_even_identity_length_histogram'].items())}
    n = p + 2 * h
    tot['expected_lists'] = ((p - 1) ** n + (-1) ** n * (p - 1)) // p
    tot['claimed_lower_bound_2h_plus_2'] = 2 * h + 2
    return tot


def lemmaA_adjacent_equal_negative(p, h):
    """All lists of length p+2h, first label 0, with at least one cyclically adjacent EQUAL pair (hypothesis violated)."""
    n = p + 2 * h
    rows = [t for t in itertools.product(range(p), repeat=n - 1)]
    X = np.array([(0,) + t for t in rows], dtype=np.int64).T
    adj_eq = np.zeros(X.shape[1], dtype=bool)
    for t in range(n):
        adj_eq |= X[t] == X[(t + 1) % n]
    X = X[:, adj_eq]
    r = lemmaA_stats(X, p, h)
    r.update({'p': p, 'h': h, 'n': n, 'note': 'lists violating the cyclic adjacent-distinct hypothesis'})
    return r


# ----------------------------------------------------------------------------- G: Lemma N
def cyclic_reduce(pos, labels, rng=None):
    cur = list(range(len(pos)))
    pairs = []
    while True:
        m = len(cur)
        if m < 2:
            break
        if m == 2:
            cands = [0] if labels[cur[0]] == labels[cur[1]] else []
        else:
            cands = [j for j in range(m) if labels[cur[j]] == labels[cur[(j + 1) % m]]]
        if not cands:
            break
        j = cands[0] if rng is None else rng.choice(cands)
        a, b = cur[j], cur[(j + 1) % m]
        pairs.append((pos[a], pos[b]))
        cur = [x for x in cur if x != a and x != b]
    return [pos[i] for i in cur], pairs


def all_reductions(labels):
    F = len(labels)
    results = set()
    seen = set()

    def rec(cur, pairs):
        key = (tuple(cur), pairs)
        if key in seen:
            return
        seen.add(key)
        m = len(cur)
        cands = []
        if m == 2:
            if labels[cur[0]] == labels[cur[1]]:
                cands = [0]
        elif m > 2:
            cands = [j for j in range(m) if labels[cur[j]] == labels[cur[(j + 1) % m]]]
        if not cands:
            results.add((tuple(cur), pairs))
            return
        for j in cands:
            a, b = cur[j], cur[(j + 1) % m]
            rec([x for x in cur if x != a and x != b], pairs | frozenset([(min(a, b), max(a, b))]))
    rec(list(range(F)), frozenset())
    return results


def lemmaN_check_final(labels, p, surv, pairs, G):
    F = len(labels)
    ok = {'count_p_survivors_p_minus_1_pairs': (len(surv) == p and len(pairs) == p - 1)}
    if not ok['count_p_survivors_p_minus_1_pairs']:
        return ok
    sl = [labels[i] for i in sorted(surv)]
    d = (sl[1] - sl[0]) % p
    ok['survivor_labels_cyclic_AP_nonzero_step'] = d != 0 and all((sl[(k + 1) % p] - sl[k]) % p == d for k in range(p)) and len(set(sl)) == p
    c0 = min(surv)

    def rank(i):
        return (i - c0) % F
    ar = sorted(rank(a) for a in surv)

    def gap(i):
        return sum(1 for x in ar if x < rank(i))
    ok['each_pair_in_one_gap'] = all(gap(u) == gap(v) for u, v in pairs)
    ch = [tuple(sorted((rank(u), rank(v)))) for u, v in pairs]
    nc = True
    for (a1, b1), (a2, b2) in itertools.combinations(ch, 2):
        if a1 < a2 < b1 < b2 or a2 < a1 < b2 < b1:
            nc = False
    ok['pairs_noncrossing'] = nc
    good = True
    for mask in range(1 << len(pairs)):
        keep = set(x for k, pr in enumerate(pairs) if mask >> k & 1 for x in pr)
        for gi in range(1, p + 1):
            gw = sorted([x for x in keep if gap(x) == gi], key=rank)
            if G.prod([p + labels[x] for x in gw]) != 0:
                good = False
    ok['every_subfamily_of_pairs_has_identity_gap_words'] = good
    return ok


def task_lemmaN(args):
    lists, p = args
    G = Grp(p)
    nterm = 0
    fails = Counter()
    for X in lists:
        for surv, pairs in all_reductions(list(X)):
            nterm += 1
            ok = lemmaN_check_final(list(X), p, list(surv), list(pairs), G)
            for k, v in ok.items():
                if not v:
                    fails[k] += 1
    return len(lists), nterm, dict(fails)


# ----------------------------------------------------------------------------- H: proof-route constructor
class RouteFail(Exception):
    pass


def transports(word, S, start, G):
    N = len(word)
    P = 0
    tau = {}
    for t in range(N):
        i = (start + t) % N
        tau[i] = G.conj(P, word[i])
        if i in S:
            P = G.MUL[P][word[i]]
    if P != 0:
        raise RouteFail('S not identity')
    return tau


def construct(word, p, G, rng=None, all_E=True):
    """Independent re-implementation of the candidate's route.  Raises RouteFail on any failed claim."""
    N = len(word)
    refl = [i for i, g in enumerate(word) if g >= p]
    rots = [i for i, g in enumerate(word) if g < p]
    labs = [word[i] for i in refl]
    rs = ref_selector_dp(labs, p, G)
    if rs is not None:
        sel = [refl[k] for k in rs]
        ok, why = verify_selector(word, sel, p, G, 0)
        if not ok:
            raise RouteFail('REF selector ' + why)
        return {'route': 'REF', 'selectors': [sel]}
    surv, pairs = cyclic_reduce(refl, labs, rng)
    if not (len(surv) == p and len(pairs) == p - 1):
        raise RouteFail('Lemma N count')
    sl = [word[i] - p for i in surv]
    d = (sl[1] - sl[0]) % p
    if not (d != 0 and all((sl[(k + 1) % p] - sl[k]) % p == d for k in range(p))):
        raise RouteFail('Lemma N AP')
    c0 = surv[0]

    def rank(i):
        return (i - c0) % N
    anc_rank = sorted(rank(a) for a in surv)

    def gap_of(i):
        return sum(1 for x in anc_rank if x < rank(i))
    for (u, v) in pairs:
        if gap_of(u) != gap_of(v):
            raise RouteFail('pair spans gaps')
    S = set(x for pr in pairs for x in pr)
    tauS = transports(word, S, c0, G)
    for a in surv:
        if tauS[a] != word[a]:
            raise RouteFail('anchor transport != raw label in anchor cut (full S)')
    A = {r: tauS[r] for r in rots}
    for r in rots:
        par = sum(1 for x in S if rank(x) < rank(r)) % 2
        if A[r] != (word[r] if par == 0 else (-word[r]) % p):
            raise RouteFail('A_r parity formula')
    for x, y in itertools.combinations(rots, 2):
        if (A[x] + A[y]) % p == 0:
            sel = sorted(S | {x, y})
            ok, why = verify_selector(word, sel, p, G)
            if not ok or sum(1 for i in sel if word[i] < p) != 2:
                raise RouteFail('fullS selector ' + why)
            return {'route': 'fullS', 'selectors': [sel]}
    Elist = pairs if all_E else pairs[:1]
    kinds = []
    sels = []
    allA_equal = len(set(A.values())) == 1
    for E in Elist:
        SE = S - set(E)
        tauE = transports(word, SE, c0, G)
        for a in surv:
            if tauE[a] != word[a]:
                raise RouteFail('anchor transport != raw label in anchor cut (S_E)')
        e1, e2 = sorted(E, key=rank)
        Ap = {}
        for r in rots:
            chi = 1 if rank(e1) < rank(r) < rank(e2) else 0
            if tauE[r] != (A[r] if chi == 0 else (-A[r]) % p):
                raise RouteFail('flip formula (1)')
            Ap[r] = tauE[r]
        found = None
        rs_sorted = sorted(rots, key=rank)
        for ii in range(len(rs_sorted)):
            for jj in range(ii + 1, len(rs_sorted)):
                r, s = rs_sorted[ii], rs_sorted[jj]
                if gap_of(r) == gap_of(s) and (Ap[r] + Ap[s]) % p != 0:
                    found = ('same', r, s)
                    break
                if gap_of(r) != gap_of(s) and (Ap[r] - Ap[s]) % p != 0:
                    found = ('diff', r, s)
                    break
            if found:
                break
        if found is None:
            raise RouteFail('no completing pair for E=%s (all A equal: %s)' % (E, allA_equal))
        kind, r, s = found
        tau2 = transports(word, SE, r, G)

        def rk2(i):
            return (i - r) % N
        eps = None
        for x in rots:
            if tauE[x] != 0:
                e_ = 1 if tau2[x] == tauE[x] else (-1 if tau2[x] == (-tauE[x]) % p else None)
                if e_ is None or (eps is not None and e_ != eps):
                    raise RouteFail('rotation sign not common under cut change')
                eps = e_
        Q = G.prod([word[i] for i in sorted(SE, key=rank) if rank(i) < rank(r)])
        epsQ = 1 if Q < p else -1
        if eps is not None and eps != epsQ:
            raise RouteFail('eps mismatch')
        lam = {a: tau2[a] - p for a in surv}
        cc = (lam[surv[0]] - epsQ * (word[surv[0]] - p)) % p
        if not all((lam[a] - (epsQ * (word[a] - p) + cc)) % p == 0 for a in surv):
            raise RouteFail('anchors not a common affine image')
        al, be = tau2[r], tau2[s]
        anc = sorted(surv, key=rk2)
        sel = None
        if kind == 'same':
            if not all(rk2(a) > rk2(s) for a in surv):
                raise RouteFail('same-gap cut has an anchor between r and s')
            for xi in range(p):
                for yi in range(xi + 1, p):
                    x, y = anc[xi], anc[yi]
                    if (lam[x] - lam[y] + al + be) % p == 0:
                        sel = sorted(SE | {r, s, x, y})
                        break
                if sel:
                    break
        else:
            first = [a for a in anc if rk2(a) < rk2(s)]
            second = [a for a in anc if rk2(a) > rk2(s)]
            if not (1 <= len(first) <= p - 1 and len(first) + len(second) == p):
                raise RouteFail('arc sizes')
            if set((lam[x] - lam[y]) % p for x in first for y in second) != set(range(1, p)):
                raise RouteFail('cross-difference support')
            for x in first:
                for y in second:
                    if (lam[x] - lam[y] - (be - al)) % p == 0:
                        sel = sorted(SE | {r, x, s, y})
                        break
                if sel:
                    break
        if sel is None:
            raise RouteFail('completion anchors not found')
        ok, why = verify_selector(word, sel, p, G)
        if not ok or sum(1 for i in sel if word[i] < p) != 2:
            raise RouteFail('dropE selector ' + why)
        kinds.append(kind)
        sels.append(sel)
    return {'route': 'dropE:' + ','.join(sorted(set(kinds))), 'selectors': sels, 'allA_equal': allA_equal}


def words_for_list(X, p, R):
    F = len(X)
    N = F + R
    for rpos in itertools.combinations(range(N), R):
        rset = set(rpos)
        for vals in itertools.product(range(p), repeat=R):
            w = []
            it = iter(X)
            iv = iter(vals)
            for i in range(N):
                w.append(next(iv) if i in rset else p + next(it))
            yield w


def task_p3_route(args):
    X, R, seed = args
    G = Grp(3)
    rng = random.Random(seed) if seed is not None else None
    cnt = Counter()
    fails = []
    nw = 0
    for w in words_for_list(X, 3, R):
        nw += 1
        try:
            res = construct(w, 3, G, rng)
            cnt[res['route']] += 1
            if res['route'] == 'REF':
                fails.append(('unexpected REF on REF-failing projection', w))
        except RouteFail as ex:
            fails.append((str(ex), w))
    return X, R, nw, dict(cnt), fails[:5], len(fails)


def lemmaN_list2(p, rng, pL=0.85):
    a = rng.randrange(p)
    d = rng.choice([1, p - 1]) if rng.random() < 0.5 else rng.randrange(1, p)
    toks = [(a + i * d) % p for i in range(p)]
    flag = [True] * p
    for k in range(p - 1):
        pos = rng.randrange(len(toks) + 1)
        left = right = None
        for t in range(pos - 1, pos - 1 - len(toks), -1):
            if flag[t % len(toks)]:
                left = toks[t % len(toks)]
                break
        for t in range(pos, pos + len(toks)):
            if flag[t % len(toks)]:
                right = toks[t % len(toks)]
                break
        u = rng.random()
        x = left if u < pL / 2 else (right if u < pL else rng.randrange(p))
        toks[pos:pos] = [x, x]
        flag[pos:pos] = [False, False]
    off = rng.randrange(len(toks))
    return toks[off:] + toks[:off]


def insert_rotations(X, p, R, rng, mode):
    F = len(X)
    N = F + R
    if mode.startswith('concentrated'):
        j = rng.randrange(F + 1)
        word = [p + x for x in X[:j]] + [None] * R + [p + x for x in X[j:]]
        rpos = list(range(j, j + R))
    else:
        rpos = sorted(rng.sample(range(N), R))
        rs = set(rpos)
        it = iter(X)
        word = [None if i in rs else p + next(it) for i in range(N)]
    if mode in ('random', 'concentrated_random'):
        for i in rpos:
            word[i] = rng.randrange(p)
        return word
    for i in rpos:
        word[i] = 0
    refl = [i for i, g in enumerate(word) if g >= p]
    surv, pairs = cyclic_reduce(refl, [word[i] for i in refl])
    S = set(x for pr in pairs for x in pr)
    c0 = surv[0]
    c = rng.randrange(1, p)
    for r in rpos:
        par = sum(1 for x in S if (x - c0) % N < (r - c0) % N) % 2
        word[r] = c if par == 0 else (-c) % p
    if mode == 'common_onezero':
        word[rpos[0]] = 0
    return word


def onepergap_plus1(X, p, rng):
    """One rotation per anchor gap outside every pair interval plus one extra rotation, common transport c."""
    F = len(X)
    refl = list(range(F))
    surv, pairs = cyclic_reduce(refl, list(X))
    c0 = surv[0]
    order = [(c0 + t) % F for t in range(F)]
    inside = set()
    for (u, v) in pairs:
        a, b = sorted(((u - c0) % F, (v - c0) % F))
        for t in range(a, b):
            inside.add(t)
    # slots: after reflection with rank t (slot t means between rank t and rank t+1)
    anc_rank = sorted((a - c0) % F for a in surv)
    slots = []
    for k in range(p):
        lo = anc_rank[k]
        hi = anc_rank[k + 1] if k + 1 < p else F
        cand = [t for t in range(lo, hi) if t not in inside]
        slots.append(rng.choice(cand))
    extra = rng.randrange(F)
    slots.append(extra)
    slots.sort()
    linear = []
    S = set(x for pr in pairs for x in pr)
    c = rng.randrange(1, p)
    par = 0
    si = 0
    for t in range(F):
        i = order[t]
        linear.append(p + X[i])
        if i in S:
            par ^= 1
        while si < len(slots) and slots[si] == t:
            linear.append(c if par == 0 else (-c) % p)
            si += 1
    return linear


def correction_family(p):
    w = [p + 0, 1, p + 0, 1] + [p + 0] * (2 * p - 3) + [1]
    for j in range(1, p - 1):
        w += [p + j, 1]
    w += [p + (p - 1)]
    return w


def task_adversarial(args):
    p, count, seed = args
    rng = random.Random(seed)
    G = Grp(p)
    rm = make_rmul(p)
    cnt = Counter()
    fails = []
    tried = 0
    tested = 0
    dp_neg = 0
    modes = ['random', 'common', 'common', 'concentrated', 'concentrated_random', 'common_onezero', 'onepergap_plus1']
    t0 = time.time()
    while tested < count:
        tried += 1
        X = lemmaN_list2(p, rng)
        if ref_selector_dp([p + x for x in X], p, G) is not None:
            continue
        mode = modes[tested % len(modes)]
        R = p + 1 + (1 if rng.random() < 0.15 else 0)
        if mode == 'onepergap_plus1':
            w = onepergap_plus1(X, p, rng)
        else:
            w = insert_rotations(X, p, R, rng, mode)
        tested += 1
        if not has_selector(w, p, 2, rm):
            dp_neg += 1
            fails.append(('DP found no selector', w))
        for order in ('leftmost', 'random'):
            try:
                res = construct(w, p, G, None if order == 'leftmost' else rng)
                cnt[(mode, order, res['route'])] += 1
            except RouteFail as ex:
                fails.append((str(ex), w))
    return {'p': p, 'words_tested': tested, 'reflection_lists_tried': tried, 'dp_no_selector': dp_neg,
            'route_counts': {'|'.join(k): v for k, v in sorted(cnt.items())}, 'failures': fails[:5],
            'n_failures': len(fails), 'seconds': round(time.time() - t0, 1)}


def task_random_uniform(args):
    p, F, R, count, seed = args
    rng = random.Random(seed)
    G = Grp(p)
    rm = make_rmul(p)
    cnt = Counter()
    fails = []
    for t in range(count):
        w = [rng.randrange(p) for _ in range(R)] + [p + rng.randrange(p) for _ in range(F)]
        rng.shuffle(w)
        if not has_selector(w, p, 2, rm):
            fails.append(('DP found no selector', w))
        try:
            res = construct(w, p, G, rng)
            cnt[res['route']] += 1
        except RouteFail as ex:
            fails.append((str(ex), w))
    return {'p': p, 'F': F, 'R': R, 'words': count, 'route_counts': dict(cnt), 'failures': fails[:5], 'n_failures': len(fails)}


# ----------------------------------------------------------------------------- main
def main():
    res = {'script': os.path.basename(__file__), 'clock_start': clock()}
    with open(os.path.abspath(__file__), 'rb') as fh:
        res['script_sha256'] = hashlib.sha256(fh.read()).hexdigest()
    res['python'] = sys.version.split()[0]
    res['numpy'] = np.__version__
    T0 = time.time()

    # A
    res['A_algebra'] = algebra_tests()

    # B
    res['B_p3_method1_whole_word_dfs'] = [method1_dfs(3, F, R) for (F, R) in [(7, 4), (7, 5), (7, 6), (6, 4), (7, 3)]]
    res['B_p3_method1_any_rotation_count'] = [method1_dfs(3, F, R, maxrot=6) for (F, R) in [(6, 4), (7, 3)]]

    # C
    res['C_p3_method2_numpy'] = [method2_numpy(3, 7, 4, (0, 2)), method2_numpy(3, 6, 4, (0, 2)),
                                 method2_numpy(3, 6, 4, (0, 2, 4)), method2_numpy(3, 7, 3, (0, 2))]

    # D
    G3 = Grp(3)
    X3 = ref_fail_lists(3, 7)
    X3_6 = ref_fail_lists(3, 6)
    reps3, closed3 = orbit_reps(X3, 3)
    reps3_6, closed3_6 = orbit_reps(X3_6, 3)
    D = {'ref_failing_lists_F7': len(X3), 'orbit_reps_F7': len(reps3), 'closed_F7': closed3,
         'ref_failing_lists_F6': len(X3_6), 'orbit_reps_F6': len(reps3_6), 'closed_F6': closed3_6}
    D['per_list_R4_total_bad'] = sum(list_dfs(X, 3, 4)[0] for X in X3)
    D['per_list_R3_total_bad'] = sum(list_dfs(X, 3, 3)[0] for X in X3)
    D['per_list_F6_R4_total_bad'] = sum(list_dfs(X, 3, 4)[0] for X in X3_6)
    D['orbit_weighted_R3_bad'] = sum(cnt * list_dfs(X, 3, 3)[0] for X, cnt in reps3.items())
    D['orbit_weighted_F6_R4_bad'] = sum(cnt * list_dfs(X, 3, 4)[0] for X, cnt in reps3_6.items())
    ex = []
    for X in X3:
        b, _, e = list_dfs(X, 3, 3, collect=2)
        ex += e
        if len(ex) >= 4:
            break
    ex6 = []
    for X in X3_6:
        b, _, e = list_dfs(X, 3, 4, collect=2)
        ex6 += e
        if len(ex6) >= 6:
            break
    D['neg_R_eq_p_examples'] = [{'word': fmt(w, 3), 'brute_le2': brute_selector(w, 3, 2, G3),
                                 'brute_any': brute_selector(w, 3, 6, G3)} for w in ex]
    D['neg_F_eq_3p_minus_3_examples'] = [{'word': fmt(w, 3), 'brute_le2': brute_selector(w, 3, 2, G3),
                                          'brute_any': brute_selector(w, 3, 6, G3)} for w in ex6]
    res['D_p3_per_list'] = D

    # E + F + G + H heavy parts in a pool
    X5 = ref_fail_lists(5, 13)
    reps5, closed5 = orbit_reps(X5, 5)
    X5_12 = ref_fail_lists(5, 12)
    reps5_12, closed5_12 = orbit_reps(X5_12, 5)
    E = {'ref_failing_lists_F13': len(X5), 'orbit_reps_F13': len(reps5), 'closed_F13': closed5,
         'orbit_size_sum_F13': sum(reps5.values()),
         'ref_failing_lists_F12': len(X5_12), 'orbit_reps_F12': len(reps5_12), 'closed_F12': closed5_12}
    rep_list = sorted(reps5)
    jobs = [(X, 5, 6) for X in rep_list] + [(X, 5, 5) for X in rep_list]
    rngs = random.Random(99)
    nonrep_sample = rngs.sample([X for X in X5 if X not in reps5], 12)
    jobs += [(X, 5, 5) for X in nonrep_sample]
    lemA_jobs = []
    lemA_specs = [(3, 1), (3, 2), (5, 1), (5, 2), (5, 3), (5, 4), (7, 1), (7, 2), (3, 0), (5, 0), (3, 3), (3, 4), (7, 0)]
    for (p, h) in lemA_specs:
        n = p + 2 * h
        tot = (p - 1) ** (n - 1)
        chunk = 1 << 20
        for lo in range(0, tot, chunk):
            lemA_jobs.append((p, h, lo, min(tot, lo + chunk)))
    lemN_jobs = [(X3, 3)] + [(X5[i:i + 400], 5) for i in range(0, len(X5), 400)]
    route_jobs = [(X, 4, None) for X in X3]
    rr = random.Random(5)
    route_jobs_rand = [(X, 4, rr.randrange(10 ** 9)) for X in rr.sample(X3, 24)]
    adv_jobs = [(5, 700, 501), (7, 350, 701), (11, 120, 1101), (13, 80, 1301), (17, 40, 1701)]
    uni_jobs = [(5, 13, 6, 4000, 51), (5, 13, 7, 1500, 52), (7, 19, 8, 800, 71), (3, 7, 4, 4000, 31)]
    with Pool(NPROC) as pool:
        h_dfs = pool.map_async(task_list_dfs, jobs, chunksize=1)
        h_lemA = pool.map_async(lemmaA_chunk, lemA_jobs, chunksize=1)
        h_lemN = pool.map_async(task_lemmaN, lemN_jobs, chunksize=1)
        h_route = pool.map_async(task_p3_route, route_jobs + route_jobs_rand, chunksize=1)
        h_adv = pool.map_async(task_adversarial, adv_jobs, chunksize=1)
        h_uni = pool.map_async(task_random_uniform, uni_jobs, chunksize=1)
        r_dfs = h_dfs.get()
        r_lemA = h_lemA.get()
        r_lemN = h_lemN.get()
        r_route = h_route.get()
        r_adv = h_adv.get()
        r_uni = h_uni.get()

    # E results
    bad6 = {X: b for (X, R, b, s, sec) in r_dfs if R == 6}
    bad5 = {}
    for (X, R, b, s, sec) in r_dfs:
        if R == 5:
            bad5[X] = b
    E['R6_reps_run'] = len(bad6)
    E['R6_reps_with_bad_words'] = sum(1 for b in bad6.values() if b)
    E['R6_orbit_weighted_bad_words_all_F13_R6_words'] = sum(reps5[X] * bad6[X] for X in rep_list)
    E['R6_max_states'] = max(s for (X, R, b, s, sec) in r_dfs if R == 6)
    E['R6_seconds_total'] = round(sum(sec for (X, R, b, s, sec) in r_dfs if R == 6), 1)
    E['R5_orbit_weighted_bad_words'] = sum(reps5[X] * bad5[X] for X in rep_list)
    E['R5_reps_with_bad_words'] = sum(1 for X in rep_list if bad5[X])
    # non-rep consistency
    cons = []
    for X in nonrep_sample:
        rep = min(symmetry_images(X, 5))
        cons.append(bad5[X] == bad5[rep])
    E['R5_nonrep_sample_matches_rep'] = all(cons)
    E['R5_nonrep_sample_size'] = len(cons)
    G5 = Grp(5)
    negs = []
    for X in rep_list:
        if bad5[X]:
            b, _, e = list_dfs(X, 5, 5, collect=1)
            for w in e:
                negs.append({'word': fmt(w, 5), 'brute_le2': brute_selector(w, 5, 2, G5),
                             'brute_any': brute_selector(w, 5, 10, G5)})
        if len(negs) >= 3:
            break
    E['neg_R_eq_p_examples'] = negs
    negs12 = []
    for X in [(0,) * 9 + (1, 2, 3), (0,) * 9 + (1, 2, 4)]:
        assert X in set(X5_12)
        b, _, e = list_dfs(X, 5, 6, collect=2)
        for w in e:
            negs12.append({'word': fmt(w, 5), 'list_bad_words': b, 'brute_le2': brute_selector(w, 5, 2, G5),
                           'brute_any': brute_selector(w, 5, 10, G5)})
    E['neg_F_eq_3p_minus_3_examples'] = negs12
    res['E_p5'] = E

    # F results
    FA = []
    for (p, h) in lemA_specs:
        parts = [r for (job, r) in zip(lemA_jobs, r_lemA) if job[0] == p and job[1] == h]
        FA.append(merge_lemmaA(parts, p, h))
    FA.append(lemmaA_adjacent_equal_negative(5, 1))
    FA.append(lemmaA_adjacent_equal_negative(3, 2))
    res['F_lemmaA'] = FA

    # G results
    GN = {'p3': {'lists': r_lemN[0][0], 'terminal_reductions': r_lemN[0][1], 'failures': r_lemN[0][2]},
          'p5': {'lists': sum(x[0] for x in r_lemN[1:]), 'terminal_reductions': sum(x[1] for x in r_lemN[1:]),
                 'failures': dict(sum((Counter(x[2]) for x in r_lemN[1:]), Counter()))}}
    struct = covered = 0
    for X in itertools.product(range(3), repeat=7):
        surv, pairs = cyclic_reduce(list(range(7)), list(X))
        if len(surv) == 3 and len(pairs) == 2 and len(set(X[i] for i in surv)) == 3:
            struct += 1
            if ref_selector_dp([3 + x for x in X], 3, G3) is not None:
                covered += 1
    GN['p3_lists_with_AP_reduction_structure'] = struct
    GN['p3_of_which_REF_covered'] = covered
    res['G_lemmaN'] = GN

    # H results
    H = {}
    det = r_route[:len(route_jobs)]
    rnd = r_route[len(route_jobs):]
    H['p3_exhaustive_route_deterministic'] = {
        'lists': len(det), 'words': sum(x[2] for x in det),
        'route_counts': dict(sum((Counter(x[3]) for x in det), Counter())),
        'failures': sum(x[5] for x in det), 'failure_examples': [f for x in det for f in x[4]][:5]}
    H['p3_route_random_deletion_order'] = {
        'lists': len(rnd), 'words': sum(x[2] for x in rnd),
        'route_counts': dict(sum((Counter(x[3]) for x in rnd), Counter())),
        'failures': sum(x[5] for x in rnd), 'failure_examples': [f for x in rnd for f in x[4]][:5]}
    H['adversarial'] = r_adv
    H['uniform_random'] = r_uni
    fam = []
    for p in (7, 11, 13, 17):
        G = Grp(p)
        w = correction_family(p)
        refl = [i for i, g in enumerate(w) if g >= p]
        item = {'p': p, 'N': len(w), 'F': len(refl), 'R': len(w) - len(refl),
                'REF_selector_exists': ref_selector_dp([w[i] for i in refl], p, G) is not None,
                'DP_selector_le2': has_selector(w, p, 2)}
        try:
            r = construct(w, p, G, None)
            item['route'] = r['route']
            item['first_selector'] = r['selectors'][0]
        except RouteFail as ex:
            item['route'] = 'FAIL ' + str(ex)
        fam.append(item)
    G11 = Grp(11)
    w11 = correction_family(11)
    sel11 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 23, 24, 25, 27, 29, 31, 33, 35, 37, 38, 39, 41]
    H['correction_family'] = fam
    H['correction_p11_listed_selector'] = {'selector': sel11, 'verify': verify_selector(w11, sel11, 11, G11),
                                           'rotations_used': sum(1 for i in sel11 if w11[i] < 11)}
    res['H_route'] = H

    # I harness negatives
    I = {}
    rng = random.Random(4242)
    G = Grp(5)
    caught = Counter()
    trials = 0
    order_sensitive = 0
    for t in range(400):
        X = lemmaN_list2(5, rng)
        if ref_selector_dp([5 + x for x in X], 5, G) is not None:
            continue
        w = insert_rotations(X, 5, 6, rng, 'common')
        r = construct(w, 5, G, None)
        sel = r['selectors'][0]
        trials += 1
        # (a) duplicate index
        bad = sel[:-1] + [sel[0]]
        caught['duplicate'] += (verify_selector(w, bad, 5, G)[1] == 'duplicate')
        # (b) drop an index
        caught['length'] += (verify_selector(w, sel[:-1], 5, G)[1] == 'length')
        # (c) alter one selected rotation's exponent
        w2 = list(w)
        ri = [i for i in sel if w[i] < 5]
        if ri:
            w2[ri[0]] = (w2[ri[0]] + 1) % 5
            caught['altered_rotation'] += (verify_selector(w2, sel, 5, G)[1] == 'product')
        # (d) replace a selected anchor by an unselected reflection of different label
        unsel = [i for i in range(len(w)) if i not in sel and w[i] >= 5]
        sref = [i for i in sel if w[i] >= 5]
        alt = [(i, j) for i in sref for j in unsel if w[j] != w[i]]
        if alt:
            i, j = alt[0]
            caught['swapped_reflection'] += (not verify_selector(w, sorted([x for x in sel if x != i] + [j]), 5, G)[0])
        # (e) order sensitivity: multiply same letters in a different (non-original) order
        letters = [w[i] for i in sel]
        perm = letters[1:] + letters[:1]  # cyclic rotation keeps identity (conjugate)
        rev = list(reversed(letters))
        if G.prod(perm) != 0:
            caught['cyclic_rotation_broke_identity'] += 1
        if G.prod(rev) != 0:
            order_sensitive += 1
    I['trials'] = trials
    I['caught'] = dict(caught)
    I['reversed_order_product_not_identity'] = order_sensitive
    I['note'] = 'cyclic rotation of an identity selection must stay identity (count should be 0); reversed order generally fails'
    # an intended-reason negative: rotation as anchor / selector with 3 rotations rejected by maxrot
    res['I_harness_negatives'] = I

    res['seconds_total'] = round(time.time() - T0, 1)
    res['clock_end'] = clock()
    with open(RESULT_PATH, 'w') as fh:
        json.dump(res, fh, indent=1, sort_keys=False, default=str)
        fh.write('\n')
    print(json.dumps({'clock_start': res['clock_start'], 'clock_end': res['clock_end'],
                      'seconds_total': res['seconds_total'], 'script_sha256': res['script_sha256']}))


if __name__ == '__main__':
    main()

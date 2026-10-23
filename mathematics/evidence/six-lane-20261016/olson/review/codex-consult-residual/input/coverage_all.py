#!/usr/bin/env python3
"""Which proved sufficient conditions cover a word of length 4p-1 over D_{2p}?

Word: list of ('R', x) / ('F', y), x,y in Z_p.  Left convention
(v,e)(v',e') = (v + e v', e e').  Tools (see proof-dihedral-partial.md):
  EGZ       R >= 3p-1
  P         F + sum floor(n_t/2) >= 3p-1                       (Theorem P)
  DBL       packed-stretch Doubling Lemma, exact subset search
  DAV       Davenport-alpha items >= 3p-1
  RIGID     all letters in {rho_x, rho_-x, sigma_y}
  RPRIME    Corollary R' (<= p-3 merge-free defects)
  LA        Lemma A: some reflection set Phi (even, colouring) with
            sum_g min(k, mu(g)) - k + 1 >= p, k = 2p - |Phi| (searched over
            all Phi with |Phi| <= phimax, or random sample)
Also: exact DP existence check (has_solution) for uncovered words.
Usage: coverage_all.py p nwords seed [mode]
  mode: random | nearrigid:<defects>
"""
import sys, random, json, itertools
from collections import Counter

def gaps_of(word):
    """Rotate so word ends with a reflection; return (ys, gaps) where gaps[t] is the
    list of rotation values before reflection t (cyclic)."""
    idx = [i for i, (c, _) in enumerate(word) if c == 'F']
    if not idx:
        return None, None
    last = idx[-1]
    w = word[last + 1:] + word[:last + 1]
    ys, gaps, cur = [], [], []
    for c, v in w:
        if c == 'R':
            cur.append(v)
        else:
            gaps.append(cur); ys.append(v); cur = []
    return ys, gaps

def has_solution(word, p):
    """Exact DP over the linear word: states (size, sign, value)."""
    n2 = 2 * p
    # state: dict (size, e) -> set of v ; product so far (v, e)
    reach = {(0, 1): {0}}
    for c, val in word:
        new = {k: set(s) for k, s in reach.items()}
        for (sz, e), vs in reach.items():
            if sz >= n2:
                continue
            if c == 'R':
                key = (sz + 1, e)
                tgt = new.setdefault(key, set())
                for v in vs:
                    tgt.add((v + e * val) % p)
            else:
                key = (sz + 1, -e)
                tgt = new.setdefault(key, set())
                for v in vs:
                    tgt.add((v + e * val) % p)
        reach = new
    return 0 in reach.get((n2, 1), set())

def tool_P(ys, gaps, p):
    F = len(ys)
    return F + sum(len(g) // 2 for g in gaps) >= 3 * p - 1

def bracket(ys, gaps, t, p):
    F = len(ys)
    return (ys[(t - 1) % F] - ys[t] - sum(gaps[t])) % p

def subset_sum_exact(pool, need, target, p):
    if need < 0:
        return False
    if need == 0:
        return target % p == 0
    if len(pool) < need:
        return False
    # dp[c] = bitmask set of sums reachable with c elements
    dp = [0] * (need + 1)
    dp[0] = 1
    full = (1 << p) - 1
    for x in pool:
        x %= p
        for c in range(min(need, len(pool)), 0, -1):
            s = dp[c - 1]
            if s:
                rot = ((s << x) | (s >> (p - x))) & full if x else s
                dp[c] |= rot
    return bool((dp[need] >> (target % p)) & 1)

def tool_DBL(ys, gaps, p):
    F = len(ys)
    for t0 in range(F):
        for j in range(0, (F - 1) // 2 + 1):
            if 2 * j + 1 > F:
                break
            Ms = [(t0 + 2 * i - 1) % F for i in range(1, j + 1)]
            Ps = [(t0 + 2 * i) % F for i in range(0, j + 1)]
            need = p - 2 * j - sum(len(gaps[t]) for t in Ms)
            if need < 0:
                break
            bsum = sum(bracket(ys, gaps, t, p) for t in Ms) % p
            pool = [x for t in Ps for x in gaps[t]]
            if subset_sum_exact(pool, need, (-bsum) % p, p):
                return True
    return False

def tool_DAV(ys, gaps, p):
    F = len(ys)
    R = sum(len(g) for g in gaps)
    w = [1 - len(g) for g in gaps]   # gain of putting gap t into I
    # max weight independent set on cycle C_F (F>=1); only positive weights matter
    best = 0
    if F == 1:
        best = max(0, w[0])
    else:
        for first_in in (False, True):
            # linear DP over 0..F-1 with constraint on gap 0 and wraparound
            inc, exc = (w[0] if first_in else -10**9), (0 if not first_in else -10**9)
            for t in range(1, F):
                if t == F - 1 and first_in:
                    inc, exc = -10**9, max(inc, exc)
                else:
                    inc, exc = exc + w[t], max(inc, exc)
            best = max(best, inc, exc)
    return R + best >= 3 * p - 1

def templates(word, p):
    rv = Counter(v for c, v in word if c == 'R')
    fv = Counter(v for c, v in word if c == 'F')
    xs = set()
    for v in rv:
        if v % p:
            xs.add(min(v % p, (-v) % p))
    if not xs:
        xs = {1}
    ys = set(fv) if fv else {0}
    return xs, ys

def is_template(c, v, x, y, p):
    if c == 'R':
        return v % p in (x % p, (-x) % p)
    return v % p == y % p

def tool_RIGID(word, p):
    xs, ys = templates(word, p)
    for x in xs:
        for y in ys:
            if all(is_template(c, v, x, y, p) for c, v in word):
                return True
    return False

def tool_RPRIME(word, p):
    xs, ys = templates(word, p)
    n = len(word)
    for x in xs:
        for y in ys:
            defects = [i for i, (c, v) in enumerate(word) if not is_template(c, v, x, y, p)]
            if len(defects) > p - 3:
                continue
            # refined merge condition: every maximal run of template rotations in
            # w - Delta containing >= p equal letters lies inside one gap of w
            dset = set(defects)
            sub = [(i, word[i]) for i in range(n) if i not in dset]
            ok = True
            if any(c == 'F' for _, (c, _) in sub):
                last = max(k for k, (_, (c, _)) in enumerate(sub) if c == 'F')
                sub = sub[last + 1:] + sub[:last + 1]
                run = []
                for i, (c, v) in sub:
                    if c == 'R':
                        run.append((i, v % p))
                        continue
                    if run:
                        cnt = Counter(val for _, val in run)
                        if max(cnt.values()) >= p:
                            a, b = run[0][0], run[-1][0]
                            span = range(a + 1, b) if a <= b else list(range(a + 1, n)) + list(range(0, b))
                            if any(word[k][0] == 'F' for k in span):
                                ok = False
                                break
                    run = []
            if ok:
                return True
    return False

def lemmaA_bound(signed, k, p):
    mu = Counter(v % p for v in signed)
    return sum(min(k, m) for m in mu.values()) - k + 1

def tool_LA(ys, gaps, p, phimax=None, samples=4000, rng=None):
    """Search reflection subsets Phi (even size) for the Lemma A CD bound."""
    F = len(ys)
    R = sum(len(g) for g in gaps)
    def check(Phi):
        k = 2 * p - len(Phi)
        if k < 1 or k > R:
            return False
        # zones: gap t sign = (-1)^{#Phi among reflections before gap t}, cyclic start at gap 0
        sgn, signed = 1, []
        Phis = set(Phi)
        for t in range(F):
            for x in gaps[t]:
                signed.append(sgn * x)
            if t in Phis:
                sgn = -sgn
        return lemmaA_bound(signed, k, p) >= p
    if phimax is None:
        phimax = F
    # exhaustive for small F, else random
    total = sum(1 for _ in range(0))
    if F <= 16:
        for size in range(2, min(F, phimax, 2 * p) + 1, 2):
            for Phi in itertools.combinations(range(F), size):
                if check(Phi):
                    return True
        return False
    rng = rng or random.Random(0)
    for _ in range(samples):
        size = rng.randrange(2, min(F, 2 * p) + 1, 2)
        Phi = rng.sample(range(F), size)
        if check(Phi):
            return True
    return False

def classify(word, p, la=True):
    R = sum(1 for c, _ in word if c == 'R')
    res = {}
    res['EGZ'] = R >= 3 * p - 1
    ys, gaps = gaps_of(word)
    if ys is None:
        res.update(P=False, DBL=False, DAV=False, LA=False)
    else:
        res['P'] = tool_P(ys, gaps, p)
        res['DBL'] = tool_DBL(ys, gaps, p)
        res['DAV'] = tool_DAV(ys, gaps, p)
        res['LA'] = tool_LA(ys, gaps, p) if la else False
    res['RIGID'] = tool_RIGID(word, p)
    res['RPRIME'] = tool_RPRIME(word, p)
    return res

def wstr(word):
    return ' '.join(('r%d' if c == 'R' else 's%d') % v for c, v in word)

def main():
    p = int(sys.argv[1]); nw = int(sys.argv[2]); seed = int(sys.argv[3])
    mode = sys.argv[4] if len(sys.argv) > 4 else 'random'
    rng = random.Random(seed)
    N = 4 * p - 1
    stats = Counter(); unc = []
    for it in range(nw):
        if mode == 'random':
            pr = rng.random()
            word = [('R', rng.randrange(p)) if rng.random() < pr else ('F', rng.randrange(p)) for _ in range(N)]
        elif mode.startswith('nearrigid'):
            nd = int(mode.split(':')[1])
            pr = rng.random()
            word = [('R', rng.choice([1, p - 1])) if rng.random() < pr else ('F', 0) for _ in range(N)]
            for _ in range(nd):
                i = rng.randrange(N)
                word[i] = ('R', rng.randrange(p)) if rng.random() < 0.5 else ('F', rng.randrange(p))
        elif mode.startswith('lowval'):
            # values from a small set: rotations in {+-1,+-2}, reflections in {0,1}
            pr = rng.random()
            word = [('R', rng.choice([1, p - 1, 2, p - 2])) if rng.random() < pr else ('F', rng.choice([0, 1])) for _ in range(N)]
        elif mode.startswith('rotrigid'):
            pr = rng.uniform(0.25, 0.6)
            word = [('R', rng.choice([1, p - 1])) if rng.random() < pr else ('F', rng.randrange(p)) for _ in range(N)]
        elif mode.startswith('reflrigid'):
            pr = rng.uniform(0.25, 0.75)
            word = [('R', rng.randrange(1, p)) if rng.random() < pr else ('F', 0) for _ in range(N)]
        elif mode.startswith('twoval'):
            c = rng.randrange(1, p)
            pr = rng.uniform(0.25, 0.6)
            word = [('R', rng.choice([1, p - 1])) if rng.random() < pr else ('F', rng.choice([0, c])) for _ in range(N)]
        elif mode.startswith('gr'):
            # generalized rigid: rotations +-1, reflection runs constant with random values
            pr = rng.uniform(0.25, 0.6)
            word, prevF, cur = [], False, rng.randrange(p)
            for _ in range(N):
                if rng.random() < pr:
                    word.append(('R', rng.choice([1, p - 1]))); prevF = False
                else:
                    if not prevF:
                        cur = rng.randrange(p) if rng.random() < 0.5 else 0
                    word.append(('F', cur)); prevF = True
        res = classify(word, p)
        covered = [k for k, v in res.items() if v]
        if covered:
            stats['covered'] += 1
            for k in covered:
                stats['by_' + k] += 1
        else:
            stats['uncovered'] += 1
            sol = has_solution(word, p)
            stats['uncovered_solvable' if sol else 'COUNTEREXAMPLE'] += 1
            if len(unc) < 40:
                unc.append(wstr(word))
    print(json.dumps({'p': p, 'n': nw, 'seed': seed, 'mode': mode, 'stats': dict(stats)}))
    for u in unc[:40]:
        print('UNC', u)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""gc_controls.py -- [F] exact aids for c6/proof-GC.md (task OlsonRunCount5, cycle 6).  NOT hypotheses of any proof.

Part A  Lemma GEN: the closed criterion |4m-(k+2)|+|2v-T| <= E+2*Delta0 versus the definition (lambda and lambda of the complement
        take their floor terms, Lemma H with beta=0), exhaustively for every NMH class with prime p <= PA, every 1<=m<=k-1 and
        -B-2 <= v <= A+2, plus random huge-integer tuples.
Part B  Lemma GC construction, explicit words (several generators incl. concentrated/adjacent long runs), every target run, every
        NMH class with prime 5 <= p <= PMAX (NWORDS words per class): the proof's recipe is followed literally (m, chi0, chi*, the
        two-pass boundary walk, first crossing); every walk invariant and the step/midpoint inequalities are asserted; the final
        X, Y and X+t are re-checked generic by an independent slow lambda computed from the explicit run list, and the Lemma GS
        seed of t from those slow lambdas is checked against (QS) and the no-wrap inequalities.
Part C  Exhaustive explicit words: every run-weight sequence of every NMH class with R <= 2p-3 at p = 5 and p = 7 (sequences, not
        rotation classes), every target, same checks as Part B.
Part D  Mutations (each must be detected), primes <= min(PMAX,23), 2 words per class: D1 window widened by one on each side;
        D2 m := m+2 (with its own correct window); D3 the Y-condition dropped.  In the real mode every failed check raises
        AssertionError and aborts the run, so a printed 'failures': 0 line is only reached when all checks passed.
Usage: python3 -B gc_controls.py PA PMAX NWORDS SEED
"""
import sys, random, json, hashlib, time

def isprime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

def nmh_classes(p):
    """(g, B, E, D0) with E even, D0 = 2p-R >= 3, g, B >= 1, k = 2kappa + D0 >= p + 1."""
    out = []
    for E in range(0, p - 3, 2):
        for kap in range(2, p):
            D0 = p - kap - E // 2
            if D0 < 3: continue
            k = 2 * kap + D0
            if k < p + 1: continue
            for B in range(1, kap):
                out.append((kap - B, B, E, D0))
    return out

def floor_def_generic(p, g, B, E, v, m):
    kap = g + B; A = p + g + E // 2
    lam = min(p - m + 1, v + m - g, (v + B) // 2 + 1)
    lamc = min(p - m + 1, A - kap - v + m, (A - v) // 2 + 1)
    return lam == (v + B) // 2 + 1 and lamc == (A - v) // 2 + 1

def gen_criterion(p, g, B, E, v, m):
    kap = g + B; D0 = p - kap - E // 2; k = 2 * kap + D0; T = 2 * g + E + D0
    return abs(4 * m - (k + 2)) + abs(2 * v - T) <= E + 2 * D0

# ---------- explicit words ----------
def splits(p, g, B, E):
    kap = g + B; D0 = p - kap - E // 2; k = 2 * kap + D0
    res = []
    for e_an in range(E + 1):
        for n_pr in range(E - e_an + 1):
            e_al = E - e_an - n_pr
            n_an = B - e_an - n_pr
            if n_an < 0 or (n_an == 0 and e_an > 0): continue
            n_al = k - n_an - n_pr
            if n_al < 1: continue
            res.append((e_al, e_an, n_pr, n_an, n_al))
    return res

def lengths(n, e, rng, mode):
    L = [1] * n
    if n == 0 or e == 0: return L
    if mode == 'conc':
        L[0] += e
    elif mode == 'two':
        L[0] += (e + 1) // 2; L[min(1, n - 1)] += e // 2
    else:
        for _ in range(e): L[rng.randrange(n)] += 1
    rng.shuffle(L)
    return L

def make_word(p, g, B, E, rng, mode, place):
    sp = splits(p, g, B, E)
    if not sp: return None
    e_al, e_an, n_pr, n_an, n_al = rng.choice(sp)
    al = lengths(n_al, e_al, rng, mode); an = lengths(n_an, e_an, rng, mode)
    runs = [a for a in al] + [-b for b in an] + [0] * n_pr
    if place == 'random':
        rng.shuffle(runs)
    elif place == 'antiblock':
        a_part = [r for r in runs if r > 0]; rng.shuffle(a_part)
        o_part = [r for r in runs if r <= 0]; rng.shuffle(o_part)
        cut = rng.randrange(len(a_part) + 1)
        runs = a_part[:cut] + o_part + a_part[cut:]
    elif place == 'bigclose':
        big = sorted(runs, key=lambda r: -abs(r))[:3]
        rest = list(runs)
        for b in big: rest.remove(b)
        rng.shuffle(rest)
        gap = rng.choice([0, 1, 2])
        pos = rng.randrange(len(rest) + 1)
        seg = [big[0]] + rest[pos:pos + gap] + big[1:]
        runs = rest[:pos] + seg + rest[pos + gap:]
    kap = g + B; D0 = p - kap - E // 2
    assert len(runs) == 2 * kap + D0 and sum(runs) == 2 * g + E + D0
    assert sum(max(r, 0) for r in runs) + sum(1 for r in runs if r == 0) == p + g + E // 2
    assert sum(-min(r, 0) for r in runs) + sum(1 for r in runs if r == 0) == B
    return runs

def excess_of(r):
    return 1 if r == 0 else abs(r) - 1

# ---------- independent slow lambda from the explicit run list ----------
def slow_lam(p, d, g, B, S):
    k = len(d)
    D = sum(d[i] for i in S)
    m = sum(1 for i in S if (i - 1) % k not in S)
    return min(p - m + 1, D + m - g, (D + B) // 2 + 1), D, m

def slow_generic(p, d, g, B, S):
    k = len(d); Sc = set(range(k)) - S
    assert 0 < len(S) < k
    l1, D1, m1 = slow_lam(p, d, g, B, S); l2, D2, m2 = slow_lam(p, d, g, B, Sc)
    assert m1 == m2 and D1 + D2 == sum(d)
    return l1 == (D1 + B) // 2 + 1 and l2 == (D2 + B) // 2 + 1

def U_slow(p, d, g, B, S):
    k = len(d); return p - slow_lam(p, d, g, B, set(range(k)) - S)[0]

# ---------- Lemma GC recipe ----------
def blocks_of(col):
    n = 1
    for i in range(1, len(col)):
        if col[i] != col[i - 1]: n += 1
    return n

def construct(p, g, B, E, d, t, mut=0):
    """mut 0 real; 1 window widened by one each side; 2 m := m + 2; 3 drop the Y-condition."""
    k = len(d); kap = g + B; D0 = p - kap - E // 2; T = 2 * g + E + D0
    assert k == 2 * kap + D0 and sum(d) == T and k >= 7
    L = k - 1; dt = d[t]
    pos = [(t + 1 + i) % k for i in range(L)]
    m = (k + 4) // 4
    if mut == 2: m += 2
    c = abs(4 * m - (k + 2))
    if mut != 2: assert c <= 2 and m >= 2 and 2 * m <= k - 2
    if 2 * m > L - 1: return ('nocls', None)
    Wp = E + 2 * D0 - c
    if mut == 3:
        lo = -((-(T - Wp)) // 2); hi = (T + Wp) // 2
    else:
        lo = -((-(T - Wp)) // 2) + max(0, -dt); hi = (T + Wp) // 2 - max(0, dt)
    if mut == 1: lo -= 1; hi += 1
    if mut == 0:
        S = max(abs(d[a]) for a in range(k) if a != t)
        assert S <= E - excess_of(dt) + 1 <= Wp - abs(dt) <= hi - lo + 1
        Sig = T - dt + d[pos[0]] - d[pos[-1]]
        assert abs(d[pos[0]]) + abs(d[pos[-1]]) + abs(dt) <= E + 3 <= Wp
        assert 2 * lo <= Sig + 1 and 2 * hi >= Sig - 1
    X, Y = 1, 0
    def col_from_b(bb):
        col = []; cur = X; prev = 0
        for b in list(bb) + [L]:
            col += [cur] * (b - prev); prev = b; cur = 1 - cur
        return col
    b0 = list(range(1, 2 * m))                    # unit blocks then the long final Y block
    c0 = col_from_b(b0)
    cs = [1 - x for x in c0]; cs[0] = X; cs[-1] = Y
    bs = [i for i in range(1, L) if cs[i] != cs[i - 1]]
    assert c0[0] == X and c0[-1] == Y and cs[0] == X and cs[-1] == Y
    assert len(bs) == 2 * m - 1 and blocks_of(c0) == 2 * m and blocks_of(cs) == 2 * m
    vX = lambda col: sum(d[pos[i]] for i in range(L) if col[i] == X)
    v0 = vX(c0); vs = vX(cs)
    assert v0 + vs == T - dt + d[pos[0]] - d[pos[-1]]
    b = list(b0); col = list(c0); v = v0; nsteps = 0
    if lo <= v <= hi: return ('ok', (col, pos, nsteps))
    def step(j, delta):
        nonlocal col, v, nsteps
        b[j] += delta
        new = col_from_b(b)
        diff = [i for i in range(L) if new[i] != col[i]]
        assert len(diff) == 1
        i = diff[0]
        dv = (d[pos[i]] if new[i] == X else -d[pos[i]])
        assert new[0] == X and new[-1] == Y and blocks_of(new) == 2 * m
        if mut == 0: assert abs(dv) <= hi - lo + 1
        col = new; v += dv; nsteps += 1
        assert v == vX(col)
        return lo <= v <= hi
    for j in range(2 * m - 2, -1, -1):
        while b[j] < bs[j]:
            if step(j, +1): return ('ok', (col, pos, nsteps))
    for j in range(2 * m - 1):
        while b[j] > bs[j]:
            if step(j, -1): return ('ok', (col, pos, nsteps))
    assert b == bs and col == cs
    return ('nocross', None)

def check_target(p, g, B, E, d, t, mut, stats):
    k = len(d); D0 = p - (g + B) - E // 2
    st, data = construct(p, g, B, E, d, t, mut)
    if st != 'ok':
        stats[st] = stats.get(st, 0) + 1; return False
    col, pos, nsteps = data
    Xs = {pos[i] for i in range(len(pos)) if col[i] == 1}; Ys = {pos[i] for i in range(len(pos)) if col[i] == 0}
    Qt = Xs | {t}
    ok = slow_generic(p, d, g, B, Xs) and slow_generic(p, d, g, B, Ys) and slow_generic(p, d, g, B, Qt)
    if mut == 0:
        assert ok, (p, g, B, E, d, t)
        lam = lambda S: slow_lam(p, d, g, B, S)[0]
        U = lambda S: U_slow(p, d, g, B, S)
        dt = d[t]
        slo = lam(Qt) - U(Xs); shi = U(Qt) - lam(Xs)
        assert 2 * slo >= dt - D0 + 2 and 2 * shi <= dt + D0 - 2           # (QS)
        lt = lam({t}); Ut = U({t})
        assert lt - shi > -p and Ut - slo < p                               # no wrap
        if max(lt, slo) > min(Ut, shi): stats['actual_empty'] = stats.get('actual_empty', 0) + 1
        stats['steps_max'] = max(stats.get('steps_max', 0), nsteps)
        if Qt == Xs | {t} and ((t + 1) % k in Xs or (t - 1) % k in Xs):
            stats['t_adjacent'] = stats.get('t_adjacent', 0) + 1
    else:
        if not ok: stats['detected'] = stats.get('detected', 0) + 1
    return ok

# ---------- exhaustive sequences at small p ----------
def all_sequences(p, g, B, E):
    kap = g + B; D0 = p - kap - E // 2; k = 2 * kap + D0; A = p + g + E // 2
    out = []
    def rec(prefix, al_left, an_left, ex_left):
        if len(prefix) == k:
            if al_left == 0 and an_left == 0 and ex_left == 0: out.append(list(prefix))
            return
        rem = k - len(prefix)
        # aligned run of length a
        for a in range(1, ex_left + 2):
            if a <= al_left: prefix.append(a); rec(prefix, al_left - a, an_left, ex_left - (a - 1)); prefix.pop()
        for bb in range(1, ex_left + 2):
            if bb <= an_left: prefix.append(-bb); rec(prefix, al_left, an_left - bb, ex_left - (bb - 1)); prefix.pop()
        if ex_left >= 1 and al_left >= 1 and an_left >= 1:
            prefix.append(0); rec(prefix, al_left - 1, an_left - 1, ex_left - 1); prefix.pop()
    rec([], A, B, E)
    return out

def main():
    PA, PMAX, NW, SEED = map(int, sys.argv[1:5])
    me = open(__file__, 'rb').read()
    print(json.dumps({'script_sha256': hashlib.sha256(me).hexdigest(), 'args': [PA, PMAX, NW, SEED]}), flush=True)
    rng = random.Random(SEED)
    # Part A
    t0 = time.time(); n = 0; bad = 0
    for p in [q for q in range(5, PA + 1) if isprime(q)]:
        for (g, B, E, D0) in nmh_classes(p):
            k = 2 * (g + B) + D0; A = p + g + E // 2
            for m in range(1, k):
                for v in range(-B - 2, A + 3):
                    n += 1
                    if floor_def_generic(p, g, B, E, v, m) != gen_criterion(p, g, B, E, v, m): bad += 1
    nr = 0; badr = 0
    for _ in range(200000):
        p = rng.choice([rng.randrange(5, 10**6), 2**61 - 1])
        E = 2 * rng.randrange(0, max(1, (p - 4) // 2)) if p < 10**7 else 2 * rng.randrange(0, 10**9)
        D0 = rng.randrange(3, 3 + 10**6)
        kap = p - E // 2 - D0
        if kap < 2: continue
        B = rng.randrange(1, kap); g = kap - B; k = 2 * kap + D0; A = p + g + E // 2
        T = A - B
        m = rng.choice([rng.randrange(1, k), (k + 2) // 4 + rng.randrange(-5, 6)])
        v = rng.choice([rng.randrange(-B, A + 1), T // 2 + rng.randrange(-E - 2 * D0 - 5, E + 2 * D0 + 6)])
        if m < 1: continue
        nr += 1
        if floor_def_generic(p, g, B, E, v, m) != gen_criterion(p, g, B, E, v, m): badr += 1
    print(json.dumps({'part': 'A', 'PA': PA, 'tuples': n, 'mismatch': bad, 'random_huge': nr, 'random_mismatch': badr,
                      'sec': round(time.time() - t0, 1)}), flush=True)
    # Part B
    t0 = time.time(); stats = {}; words = 0; targets = 0; perE = {}
    modes = [('spread', 'random'), ('conc', 'random'), ('conc', 'bigclose'), ('two', 'bigclose'), ('spread', 'antiblock')]
    for p in [q for q in range(5, PMAX + 1) if isprime(q)]:
        for (g, B, E, D0) in nmh_classes(p):
            for w in range(NW):
                mode, place = modes[w % len(modes)]
                d = make_word(p, g, B, E, rng, mode, place)
                if d is None: continue
                words += 1
                for t in range(len(d)):
                    targets += 1
                    check_target(p, g, B, E, d, t, 0, stats)
                key = 'E0' if E == 0 else ('E2' if E == 2 else 'E>=4')
                perE[key] = perE.get(key, 0) + len(d)
    print(json.dumps({'part': 'B', 'PMAX': PMAX, 'NWORDS': NW, 'words': words, 'targets': targets, 'targets_by_E': perE,
                      'failures': 0, 'stats': stats, 'sec': round(time.time() - t0, 1)}), flush=True)
    # Part C
    for p in (5, 7):
        t0 = time.time(); stats = {}; nseq = 0; targets = 0
        for (g, B, E, D0) in nmh_classes(p):
            for d in all_sequences(p, g, B, E):
                nseq += 1
                for t in range(len(d)):
                    targets += 1
                    check_target(p, g, B, E, d, t, 0, stats)
        print(json.dumps({'part': 'C', 'p': p, 'classes': len(nmh_classes(p)), 'sequences': nseq, 'targets': targets,
                          'failures': 0, 'stats': stats, 'sec': round(time.time() - t0, 1)}), flush=True)
    # Part D
    for mut in (1, 2, 3):
        t0 = time.time(); stats = {}; targets = 0; rng2 = random.Random(SEED + mut)
        for p in [q for q in range(5, min(PMAX, 23) + 1) if isprime(q)]:
            for (g, B, E, D0) in nmh_classes(p):
                for w in range(2):
                    mode, place = modes[(w + mut) % len(modes)]
                    d = make_word(p, g, B, E, rng2, mode, place)
                    if d is None: continue
                    for t in range(len(d)):
                        targets += 1
                        check_target(p, g, B, E, d, t, mut, stats)
        print(json.dumps({'part': 'D', 'mut': mut, 'targets': targets, 'stats': stats, 'sec': round(time.time() - t0, 1)}),
              flush=True)
    print(json.dumps({'done': True}), flush=True)

if __name__ == '__main__':
    main()

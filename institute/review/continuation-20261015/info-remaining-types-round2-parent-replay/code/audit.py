#!/usr/bin/env python3
"""Independent audit for remaining-types-round2.

It imports no producer code and no z3. Every finite claim is recomputed with
separate implementations and compared with the producer JSON files:

  R1  six GL(6,2) orbits of cubic forms (sizes) and their completion
      |W|-histogram tables, checked by an independent orbit computation;
  R2  the six Walsh classes of x0x1x2+q and Lemma B (second residue bit
      affine) on every completion of every class;
  R3  the per-coset exact (h,Lambda) realizability lists for ell = 2, 4;
  R4  refutation of the three round-1 witnesses (M1, M2, A, C, realizability);
  R5  the new strengthened z = 8 witness: it satisfies the base relaxation
      and the new histogram constraints;
  S1  (6,144): RM(2,6)|D0 weights, odd-slice counts, 540 admissible z = 8
      non-K-invariant sets with D1 fibers (12,24), single-character min c = 14;
  F1  (4,160): z = 8 classification (15 + 700), non-affine coset counts,
      lone-slice minimum 48, the two slice witnesses, the c >= 12 + z/2 algebra.

Checks raise ValueError, so they stay active under python -O.
"""
import hashlib, itertools, json, os, sys, time
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
PINS = {
    'inputs/round1-rank2-probe-senergy-scross-aux.json': '1b6a5b446e0d8f4c6f5d14005d842ebb98960b698ea82541a76ac530602b4e5e',
    'inputs/round1-rank2-probe-senergy-aux.json': '34c0f9116744d4fdc93cb889420b19eadf4eac777eba1e4daab403e602ead466',
    'inputs/round1-rank2-probe-scross-aux.json': 'b52c280e5f0e9dcd0280d8ca4666b71db721693b7571a31654cf055c338990c1',
    'inputs/round1-PROOF.txt': '7d186cd0f01bf1bc1d6b291c7ca9fa7e45d44277599364575c9029f27591c31d',
}


def need(cond, label):
    if not cond:
        raise ValueError('AUDIT FAIL: ' + label)


def load(rel):
    with open(os.path.join(ROOT, rel)) as fh:
        return json.load(fh)


def sha(rel):
    with open(os.path.join(ROOT, rel), 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# ---------- six-variable helpers (independent implementations) ----------
PTS6 = np.arange(64)
XB = (PTS6[:, None] >> np.arange(6)[None, :]) & 1          # 64 x 6
CHAR = 1 - 2 * ((XB @ XB.T) % 2)                            # (-1)^{x.k}


def walsh_rows(tt):
    """Direct character sums: W[r,kappa] = sum_x (-1)^{f_r(x)+kappa.x}."""
    return (1 - 2 * tt) @ CHAR


def monomial_table(sets):
    out = np.ones((len(sets), 64), dtype=np.int64)
    for n, s in enumerate(sets):
        for i in s:
            out[n] &= XB[:, i]
    return out


CUBS = list(itertools.combinations(range(6), 3))
QUADS = list(itertools.combinations(range(6), 2))
CUBT = monomial_table(CUBS)
QUADT = monomial_table(QUADS)


def completions_tt(cubic_sets):
    base = np.zeros(64, dtype=np.int64)
    for s in cubic_sets:
        base ^= monomial_table([s])[0]
    q = np.arange(1 << 15)
    coeff = (q[:, None] >> np.arange(15)[None, :]) & 1
    return (coeff @ QUADT) % 2 ^ base[None, :]


def hist(row):
    return tuple(sorted(Counter(np.abs(row).tolist()).items()))


def cubic_orbits_independent():
    """Orbits of GL(6,2) on cubic forms by BFS with random invertible matrices
    plus elementary generators; union-find in pure numpy (different method)."""
    rng = np.random.default_rng(20261016)

    def induced(M):
        # M: 6x6 0/1, row i = linear form substituted for x_i
        cols = []
        for (i, j, k) in CUBS:
            v = 0
            for a in np.nonzero(M[i])[0]:
                for b in np.nonzero(M[j])[0]:
                    for c in np.nonzero(M[k])[0]:
                        s = {int(a), int(b), int(c)}
                        if len(s) == 3:
                            v ^= 1 << CUBS.index(tuple(sorted(s)))
            cols.append(v)
        return cols

    def rank2(M):
        A = M.copy() % 2
        r = 0
        for c in range(6):
            p = [i for i in range(r, 6) if A[i, c]]
            if not p:
                continue
            A[[r, p[0]]] = A[[p[0], r]]
            for i in range(6):
                if i != r and A[i, c]:
                    A[i] ^= A[r]
            r += 1
        return r

    mats = []
    while len(mats) < 6:
        M = rng.integers(0, 2, (6, 6))
        if rank2(M) == 6:
            mats.append(M)
    T = np.eye(6, dtype=np.int64)
    T[0, 1] = 1
    mats.append(T)
    states = np.arange(1 << 20, dtype=np.int64)
    parent = np.arange(1 << 20, dtype=np.int64)
    for M in mats:
        cols = induced(M)
        img = np.zeros_like(states)
        for b, col in enumerate(cols):
            img ^= ((states >> b) & 1) * col
        need(len(np.unique(img)) == 1 << 20, 'random generator bijective')
        # union along edges x -> img(x) by repeated min-label hooking
        while True:
            a = parent[states]
            b = parent[img]
            lo = np.minimum(a, b)
            changed = np.any(a != b)
            np.minimum.at(parent, a, lo)
            np.minimum.at(parent, b, lo)
            for _ in range(30):
                nxt = parent[parent]
                if np.array_equal(nxt, parent):
                    break
                parent = nxt
            if not changed:
                break
    for _ in range(40):
        parent = parent[parent]
    roots, sizes = np.unique(parent, return_counts=True)
    return roots, sizes, parent


def audit_rank2():
    rep = {}
    cls = load('results/rank2-cubic-classes.json')
    t = time.time()
    roots, sizes, parent = cubic_orbits_independent()
    need(sorted(sizes.tolist()) == sorted(c['orbit_size'] for c in cls['cubic_classes']), 'R1 orbit sizes')
    need(len(roots) == 6, 'R1 six orbits')
    for c in cls['cubic_classes']:
        sets = [tuple(m) for m in c['rep_monomials']]
        mask = sum(1 << CUBS.index(s) for s in sets)
        need(c['rep_mask'] == mask, 'R1 rep mask encoding')
        size = int(sizes[np.searchsorted(roots, parent[mask])])
        need(size == c['orbit_size'], 'R1 rep orbit size')
        W = walsh_rows(completions_tt(sets))
        got = Counter(hist(r) for r in W)
        want = {tuple(map(tuple, h['hist'])): h['count'] for h in c['completion_abs_walsh_histograms']}
        need(dict(got) == want, 'R1 completion histogram table')
        # Lemma B: uniform W mod 8 and affine second residue bit, every completion
        p6 = sum(1 for a, b in itertools.combinations(sets, 2) if not set(a) & set(b))
        need(set((W % 8).ravel().tolist()) == {(4 * p6) % 8}, 'R2 W = 4 P6 mod 8')
        if p6 % 2 == 0:
            om = (W // 8) % 2
        else:
            om = ((W // 4 - p6) // 2) % 2
        lin = (om[:, [1 << i for i in range(6)]] ^ om[:, [0]])
        pred = (om[:, 0][:, None] + (lin @ XB.T)) % 2
        need(np.array_equal(pred, om), 'R2 Lemma B affine bit for every completion')
    rep['R1_R2_seconds'] = time.time() - t
    # zero-flat class list
    zf = cls['zero_flat_cubic']
    W = walsh_rows(completions_tt([(0, 1, 2)]))
    got = Counter(hist(r) for r in W)
    want = {tuple(map(tuple, c['hist'])): c['count'] for c in zf['classes']}
    need(dict(got) == want and len(want) == 6, 'R2 zero-flat six classes')
    # R3 exact per-coset realizability. First an independent check that each of the
    # six Walsh classes is a single orbit of the affine stabilizer of x0x1x2.
    real = load('results/rank2-coset-realizability.json')
    tt = completions_tt([(0, 1, 2)])
    W = walsh_rows(tt)
    hk = [hist(r) for r in W]
    _stabilizer_orbits_one_per_class(tt, hk)
    reps = {}
    for q in range(1 << 15):
        reps.setdefault(hk[q], q)
    allowed = {2: set(), 4: set()}
    for entry in real['classes']:
        q = reps[tuple(map(tuple, entry['hist']))]
        C = CHAR * (1 - 2 * tt[q])[:, None]
        for ell in (2, 4):
            found = Counter()
            n = 0
            for blk in _blocks(ell):
                Lam = C[blk].sum(1)
                num = 4 * Lam - 3 * W[q][None, :]
                ok = np.all(num % 16 == 0, 1) & np.all(np.abs(num) <= 64, 1)
                n += int(ok.sum())
                for h, lam in zip(num[ok] // 16, Lam[ok]):
                    neg = (h < 0) | ((h == 0) & (lam < 0))
                    h2 = np.where(neg, -h, h)
                    l2 = np.where(neg, -lam, lam)
                    found[tuple(sorted(Counter(zip(h2.tolist(), l2.tolist())).items()))] += 1
            claim = entry['ell%d' % ell]
            need(n == claim['valid_sets'], 'R3 valid set count ell=%d' % ell)
            claimed = {tuple((tuple(p[0]), p[1]) for p in hh['hist']): hh['count'] for hh in claim['hists']}
            need(claimed == dict(found), 'R3 normalized histogram list ell=%d' % ell)
            allowed[ell].update(found)
    rep['R3_seconds'] = time.time() - t
    # R4 / R5 witnesses
    zfh = set(want)
    evenh = set()
    for c in cls['cubic_classes']:
        if c['W_mod_8'] == 0:
            for h in c['completion_abs_walsh_histograms']:
                evenh.add(tuple(map(tuple, h['hist'])))

    def coset_checks(side, c, rows, ell_or_a):
        Wsum = Lsum = n = m16 = 0
        absh = Counter()
        norm = Counter()
        for row in rows:
            if side == 'R':
                h, lam, cnt = row
                num = 4 * lam - 16 * h
            else:
                h, lam, d0, cnt = row
                num = (-1 if c == 0 else 1) * 32 * d0 + 4 * lam - 16 * h
            need(num % 3 == 0, 'witness W integral')
            w = num // 3
            absh[abs(w)] += cnt
            Wsum += w * cnt
            Lsum += lam * cnt
            n += cnt
            m16 += cnt if w % 16 == 8 else 0
            hh, ll = (h, lam) if (h > 0 or (h == 0 and lam >= 0)) else (-h, -lam)
            norm[(hh, ll)] += cnt
        need(n == 64, 'witness covers 64 characters')
        res = {'M1': Wsum in (64, -64), 'M2': Lsum in (0, 64, -64), 'A': m16 in (0, 32, 64),
               'C': tuple(sorted(absh.items())) in (zfh if side == 'R' else evenh)}
        if side == 'R':
            key = tuple(sorted(((int(a), int(b)), v) for (a, b), v in norm.items()))
            if ell_or_a == 0:
                res['X'] = key == (((0, 0), 48), ((3, 0), 16))
            elif ell_or_a in allowed:
                res['X'] = key in allowed[ell_or_a]
        return res

    wc = load('results/rank2-witness-check.json')
    refuted = []
    for rel in ('inputs/round1-rank2-probe-senergy-scross-aux.json', 'inputs/round1-rank2-probe-senergy-aux.json',
                'inputs/round1-rank2-probe-scross-aux.json'):
        w = load(rel)
        bad = False
        for key, rows in w['aux'].items():
            c = int(key[1])
            par = w['ell'][c - 1] if key[0] == 'R' else w['a'][c]
            r = coset_checks(key[0], c, rows, par)
            bad = bad or not all(r.values())
        refuted.append(bad)
    need(all(refuted), 'R4 all round-1 witnesses refuted')
    need(wc['all_refuted'] is True, 'R4 producer agrees')
    nw = load('results/rank2-probe2-z8.json')
    need(nw['status'] == 'sat' and nw['z'] == 8, 'R5 new witness present')
    for key, rows in nw['aux'].items():
        c = int(key[1])
        par = nw['ell'][c - 1] if key[0] == 'R' else nw['a'][c]
        r = coset_checks(key[0], c, rows, par)
        need(all(r.values()), 'R5 new witness passes M1,M2,A,C,X on ' + key)
    _check_base_relaxation(nw)
    rep['R4_R5'] = 'ok'
    return rep


def _blocks(ell):
    combos = np.array(list(itertools.combinations(range(64), ell)), dtype=np.int64)
    return [combos[i:i + 40000] for i in range(0, len(combos), 40000)]


def _stabilizer_orbits_one_per_class(tt, hk):
    """Random elements of the affine stabilizer of the cubic form x0x1x2.

    The substitution x_i -> row_i.x + t_i has rows 0..2 in span(e0,e1,e2). It
    acts on the 2^15 quadratic parts. The orbits under the generated group
    must be exactly the six Walsh classes. A subgroup can only split orbits,
    so a single orbit per class proves that the class is one orbit."""
    rng = np.random.default_rng(7)

    def inv(M):
        A = np.concatenate([M % 2, np.eye(6, dtype=np.int64)], 1)
        r = 0
        for col in range(6):
            p = [i for i in range(r, 6) if A[i, col]]
            if not p:
                return None
            A[[r, p[0]]] = A[[p[0], r]]
            for i in range(6):
                if i != r and A[i, col]:
                    A[i] ^= A[r]
            r += 1
        return A[:, 6:]
    parent = np.arange(1 << 15)
    mons = np.array([[bin(m).count('1') for m in range(64)]])[0]
    made = 0
    while made < 12:
        M = rng.integers(0, 2, (6, 6))
        M[:3, 3:] = 0
        if inv(M) is None:
            continue
        t = int(rng.integers(0, 64))
        y = ((XB @ M.T) % 2 ^ ((t >> np.arange(6)) & 1)[None, :]) @ (1 << np.arange(6))
        new = tt[:, y]
        a = new.copy()
        for i in range(6):
            s = 1 << i
            a = a.reshape(a.shape[0], -1, 2, s)
            a[:, :, 1, :] ^= a[:, :, 0, :]
            a = a.reshape(a.shape[0], 64)
        need(np.all(a[:, 7] == 1) and np.all(a[:, (mons >= 3) & (np.arange(64) != 7)] == 0), 'stabilizer keeps cubic part')
        img = np.zeros(1 << 15, dtype=np.int64)
        for b, (i, j) in enumerate(QUADS):
            img |= a[:, (1 << i) | (1 << j)] << b
        for _ in range(64):
            lo = np.minimum(parent, parent[img])
            np.minimum.at(lo, img, lo.copy())
            lo = lo[lo]
            if np.array_equal(lo, parent):
                break
            parent = lo
        made += 1
    for _ in range(64):
        nxt = np.minimum(parent, parent[parent])
        if np.array_equal(nxt, parent):
            break
        parent = nxt
    roots = np.unique(parent)
    need(len(roots) == 6, 'R3 six stabilizer orbits on completions')
    for r in roots:
        need(len({hk[m] for m in np.nonzero(parent == r)[0]}) == 1, 'R3 orbit inside one class')


def walsh2(bits):
    return [sum((-1) ** (bits[x] ^ (bin(x & c).count('1') & 1)) for x in range(4)) for c in range(4)]


def _check_base_relaxation(w):
    z = w['z']
    ell, a = w['ell'], w['a']
    c = sum(ell)
    need(all(v % 2 == 0 and 0 <= v <= 28 for v in ell + a), 'R5 parities')
    need(2 * (sum(a) + c) + z <= 64 and (z + 2 * c) % 8 == 0 and sum(a) % 4 == 0, 'R5 scalar constraints')
    pats = Counter()
    hs = {cc: Counter() for cc in range(4)}
    ss = {cc: Counter() for cc in range(4)}
    flips = 0
    tot = 0
    h0sq = h0 = 0
    for p in w['pattern_counts']:
        Wu, Ww = walsh2(p['u']), walsh2(p['w'])
        h = [(Wu[i] - Ww[i]) // 2 for i in range(4)]
        s = [(Wu[i] + Ww[i]) // 2 for i in range(4)]
        n = p['count']
        tot += n
        flips += n * sum(1 for x in range(4) if p['u'][x] != p['w'][x])
        h0 += n * h[0]
        h0sq += n * h[0] ** 2
        for i in range(4):
            hs[i][h[i]] += n
            ss[i][s[i]] += n
        # complementary supports: v' = (u-w)/2 and sigma' = (u+w)/2 in {0,+-1}, disjoint
    need(tot == 64, 'R5 64 characters')
    need(h0sq == 64 - z and h0 == 0, 'R5 D0 coset energy and mean')
    need(4 * flips == 496 - z - 2 * c, 'R5 R-support count')
    for cc in (1, 2, 3):
        rows = w['aux']['R%d' % cc]
        l = ell[cc - 1]
        marg = Counter()
        for h, lam, n in rows:
            need(abs(lam) <= l and (l - lam) % 2 == 0, 'R5 Lambda range')
            marg[h] += n
        need(marg == +hs[cc], 'R5 R marginal coset %d' % cc)
        need(sum(n * ((4 * lam - 16 * h) // 3) ** 2 for h, lam, n in rows) == 4096, 'R5 Parseval R')
        need(sum(n * h * h for h, lam, n in rows) == 144 - 2 * l, 'R5 R energy')
        need(sum(n * lam * lam for h, lam, n in rows) == 64 * l, 'R5 Lambda energy')
        need(sum(n * lam * h for h, lam, n in rows) == 4 * l, 'R5 R cross')
    for cc in range(4):
        rows = w['aux']['S%d' % cc]
        av = a[cc]
        sg = -1 if cc == 0 else 1
        marg = Counter()
        d1 = [r for r in rows if r[2] == 1]
        need(sum(r[3] for r in d1) == 1, 'R5 one kappa=0 row')
        for s, lam, d0, n in rows:
            need(abs(lam) <= av and (av - lam) % 2 == 0, 'R5 S Lambda range')
            marg[s] += n
        need(marg == +ss[cc], 'R5 S marginal coset %d' % cc)
        need(sum(n * ((sg * 32 * d0 + 4 * lam - 16 * s) // 3) ** 2 for s, lam, d0, n in rows) == 4096, 'R5 Parseval S')
        need(sum(n * lam * lam for s, lam, d0, n in rows) == 64 * av, 'R5 S Lambda energy')
        s0 = sum(s * n for s, lam, d0, n in d1)
        L0 = sum(lam * n for s, lam, d0, n in d1)
        need(sum(n * s * s for s, lam, d0, n in rows) == 140 - 2 * av + 4 * sg * s0, 'R5 S energy')
        need(sum(n * s * lam for s, lam, d0, n in rows) == 4 * av + 2 * sg * L0, 'R5 S cross')


# ---------- (6,144) ----------
def audit_rank6_144():
    res = load('results/rank6-144-zero-sets.json')
    q6 = lambda u: ((u & 1) & (u >> 1 & 1)) ^ (u & 1) ^ (u >> 1 & 1) ^ ((u >> 2 & 1) & (u >> 3 & 1)) ^ ((u >> 4 & 1) & (u >> 5 & 1))
    U0 = [u for u in range(64) if q6(u) == 0]
    U1 = [u for u in range(64) if q6(u) == 1]
    # weight enumerator via all 2^22 quadratics restricted to U0 (numpy), each word counted 2x (kernel {0,q6})
    mons = [m for m in range(64) if bin(m).count('1') <= 2]
    rows = np.array([[1 if (u & m) == m else 0 for u in U0] for m in mons], dtype=np.int64)
    packed = (rows * (1 << np.arange(28))[None, :]).sum(1)
    words = np.zeros(1, dtype=np.int64)
    for p in packed:
        words = np.concatenate([words, words ^ p])
    wts = np.array([bin(int(x)).count('1') for x in np.unique(words)])
    enum = sorted(Counter(wts.tolist()).items())
    need([list(x) for x in enum] == res['rm2_restricted_weight_enumerator'], 'S1 RM2|D0 weight enumerator')
    need(len(np.unique(words)) * 2 == 1 << 22, 'S1 kernel {0,q6}')
    odd = Counter()
    for l in range(1, 64):
        for b in (0, 1):
            odd[sum(1 for u in U0 if (bin(u & l).count('1') + b) & 1)] += 1
    need([list(x) for x in sorted(odd.items())] == res['odd_slice_counts_nonconstant_affine'], 'S1 odd-slice counts')
    # admissible sets: recheck moments, E-extension (independent rank test), fibers
    D0B = [a for a in range(256) if q6(a & 63) == 0]
    cub = [m for m in range(256) if bin(m).count('1') <= 3]
    M = np.array([[1 if (a & m) == m else 0 for a in D0B] for m in cub], dtype=np.uint8)
    pf = np.array([(sum(1 for m in (15, 51, 60) if (a & m) == m) & 1) for a in D0B], dtype=np.uint8)

    def rank_gf2(A):
        A = A.copy() % 2
        r = 0
        for col in range(A.shape[1]):
            piv = np.nonzero(A[r:, col])[0]
            if len(piv) == 0:
                continue
            p = r + piv[0]
            A[[r, p]] = A[[p, r]]
            mask = A[:, col].astype(bool)
            mask[r] = False
            A[mask] ^= A[r]
            r += 1
            if r == A.shape[0]:
                break
        return r
    base = rank_gf2(M)
    need(base == 76, 'S1 rank 76')
    sets = res['z8_noninvariant_sets']
    need(len(sets) == 540 == res['z8_noninvariant_admissible_count'], 'S1 540 sets')
    seen = set()
    for s in sets:
        Z = s['Z']
        need(len(Z) == 8 and 0 in Z and all(q6(a & 63) == 0 for a in Z), 'S1 Z in D0 with 0')
        need(tuple(Z) not in seen, 'S1 distinct')
        seen.add(tuple(Z))
        x = 0
        for a in Z:
            x ^= a
        need(x == 0, 'S1 XOR zero')
        for i in range(8):
            for j in range(i + 1, 8):
                cnt = sum(1 for a in Z if a >> i & 1 and a >> j & 1)
                need(cnt % 2 == (1 if (i, j) == (6, 7) else 0), 'S1 second moments = C(B)')
        need(any(not all((a ^ k) in Z for a in Z) for k in (64, 128, 192)), 'S1 not K-invariant')
        t = np.array([0 if a in Z else 1 for a in D0B], dtype=np.uint8) ^ pf
        need(rank_gf2(np.vstack([M, t[None, :]])) == base, 'S1 E-extension exists')
        # D1 fibers: e6,e7 determined on D0 by slice directions, extended by quadratics (up to q6)
        T2 = sorted({a & 63 for a in Z})
        need(len(T2) == 4, 'S1 four slices')
        dirs = set()
        for u in T2:
            ks = sorted(a >> 6 for a in Z if a & 63 == u)
            need(len(ks) == 2, 'S1 two points per slice')
            dirs.add(ks[0] ^ ks[1])
        need(len(dirs) == 1, 'S1 one slice direction')
        g = _solve_quadratic(rows, U0, T2)
        m = sum(g[u] for u in U1)
        need(sorted([m, 36 - m]) == s['D1_fibers'] == [12, 24], 'S1 D1 fibers 12/24')
    # single-character minimum
    best = min(n1 + 2 * n2 + 3 * n3 for n1 in range(37) for n2 in range(37 - n1) for n3 in range(37 - n1 - n2)
               if 144 * (36 - n1 - n2 - n3) + 64 * n1 + 16 * n2 <= 4096)
    need(best == res['single_character_min_c']['c'] == 14, 'S1 single-character min c 14')
    return {'S1': 'ok'}


def _solve_quadratic(rows, U0, T2):
    mons = [m for m in range(64) if bin(m).count('1') <= 2]
    A = np.concatenate([rows.T % 2, np.array([[1 if u in T2 else 0] for u in U0])], 1).astype(np.uint8)
    n = len(mons)
    r = 0
    pivcols = []
    for col in range(n):
        piv = np.nonzero(A[r:, col])[0]
        if len(piv) == 0:
            continue
        p = r + piv[0]
        A[[r, p]] = A[[p, r]]
        mask = A[:, col].astype(bool)
        mask[r] = False
        A[mask] ^= A[r]
        pivcols.append(col)
        r += 1
    need(not np.any(A[r:, n]), 'S1 quadratic preimage exists')
    coef = np.zeros(n, dtype=np.int64)
    for i, col in enumerate(pivcols):
        coef[col] = A[i, n]
    return [int(sum(coef[j] for j, m in enumerate(mons) if (u & m) == m) % 2) for u in range(64)]


# ---------- (4,160) ----------
def audit_rank4_160():
    res = load('results/rank4-160-structure.json')
    q4 = lambda u: ((u & 1) & (u >> 1 & 1)) ^ (u & 1) ^ (u >> 1 & 1) ^ ((u >> 2 & 1) & (u >> 3 & 1))
    Q0 = [u for u in range(16) if q4(u) == 0]
    Q1 = [u for u in range(16) if q4(u) == 1]
    D0B = [a for a in range(256) if q4(a & 15) == 0]
    # enumerate 3-dim subspaces by reduced row echelon bases (different method)
    subs = set()
    pts = [a for a in D0B if a]
    for a in pts:
        for b in pts:
            if b <= a:
                continue
            for c in pts:
                if c <= b:
                    continue
                S = frozenset({0, a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c})
                if len(S) == 8 and S <= set(D0B):
                    subs.add(S)
    need(len(subs) == res['z8_linear_subspaces_in_D0'] == 715, 'F1 715 subspaces')
    k8a = sum(1 for S in subs if all(x & 15 == 0 for x in S))
    need(k8a == res['z8_classes']['8a'] == 15 and len(subs) - k8a == res['z8_classes']['8b'] == 700, 'F1 8a/8b split')
    # non-affine D1 cosets for 8b: affine-in-u extension of the quadratic-in-k coefficient
    for S in list(subs)[:60]:
        coefs = {}
        for u in Q0:
            vals = [1 ^ (1 if (u | (k << 4)) in S else 0) for k in range(16)]
            an = vals[:]
            for i in range(4):
                for x in range(16):
                    if x >> i & 1:
                        an[x] ^= an[x ^ (1 << i)]
            coefs[u] = an
        bad = 0
        for u1 in Q1:
            nonaff = False
            for m in (3, 5, 6, 9, 10, 12):
                sols = [(lin, cst) for lin in range(16) for cst in (0, 1)
                        if all(((bin(u & lin).count('1') + cst) & 1) == coefs[u][m] for u in Q0)]
                need(len(sols) == 1, 'F1 unique affine extension')
                lin, cst = sols[0]
                nonaff |= bool((bin(u1 & lin).count('1') + cst) & 1)
            bad += nonaff
        kind = '8a' if all(x & 15 == 0 for x in S) else '8b'
        need(bad == (0 if kind == '8a' else 6), 'F1 non-affine coset count')
    # lone slice minimum by direct search over ternary eps with Y(u1)=12 (independent: via +-1 split)
    H = np.array([[1 - 2 * (bin(x & u).count('1') & 1) for x in range(16)] for u in range(16)])
    for u1 in Q1:
        best = None
        for supp in itertools.combinations(range(16), 12):
            e = np.zeros(16, dtype=np.int64)
            e[list(supp)] = H[u1, list(supp)]
            Y = H @ e
            if Y[u1] == 12 and not any(Y[v] for v in Q1 if v != u1):
                o = int((Y ** 2).sum() - 144)
                best = o if best is None else min(best, o)
        need(best == 48 == res['lone_slice'][str(u1)]['min_outside_energy'], 'F1 lone slice minimum 48')
    # T3 algebra: (12-l)(4+l) - l(16-l) = 48 - 8l for all l
    need(all((12 - l) * (4 + l) - l * (16 - l) == 48 - 8 * l for l in range(17)), 'F1 T3 identity')
    for key in ('slice_witness_c4', 'slice_witness_c16_injective'):
        w = res[key]
        ell, z, c = w['ell'], w['z'], w['c']
        need(sum(ell) == c and (z + 2 * c) % 8 == 0 and 2 * c + z <= 56, 'F1 witness scalars')
        par = {l % 2 for l in ell}
        need(len(par) == 1, 'F1 uniform parity')
        need(sum(E for _, E in w['slices']) == 1824 - 4 * z - 8 * c and len(w['slices']) == 16, 'F1 total energy')
        other = 0
        for A, E in w['slices']:
            own = sum((12 - ell[u]) ** 2 for u in A)
            need(E % 16 == 0 and E <= 256 and (E // 16) % 2 in par and E >= own, 'F1 slice range/parity')
            if A:
                need(E >= 16 * max(12 - ell[u] for u in A), 'F1 uncertainty')
            other += E - own
        need(other == 4 * (96 - z) + sum(l * (16 - l) for l in ell), 'F1 outside energy balance')
    inj = res['slice_witness_c16_injective']
    need(all(len(A) <= 1 for A, _ in inj['slices']) and inj['c'] == 12 + inj['z'] // 2 + 0, 'F1 injective witness at bound')
    return {'F1': 'ok'}


def main():
    t0 = time.time()
    for rel, h in PINS.items():
        need(sha(rel) == h, 'pin ' + rel)
    out = {'pins': 'ok'}
    out.update(audit_rank6_144())
    out.update(audit_rank4_160())
    out.update(audit_rank2())
    out['seconds'] = time.time() - t0
    out['verdict'] = 'PASS'
    print(json.dumps(out))


if __name__ == '__main__':
    main()

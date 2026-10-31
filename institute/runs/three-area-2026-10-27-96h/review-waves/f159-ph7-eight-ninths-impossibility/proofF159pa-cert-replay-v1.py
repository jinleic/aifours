#!/usr/bin/env python3
"""proofF159pa certificate replay (reviewer ReviewF159ProofAttack, wave f159-ph7-eight-ninths-impossibility).

Independently authored, standard library only, exact integer/Fraction arithmetic.
Author code is NOT imported or executed; certificate JSON files are parsed completely here.

1. Hash/bytes/LF-verify and json-parse both certificate files; validate every leaf entry.
2. Rebuild Qpol, Hpol (six rates) and Abar, Dbar, 2(f1-4) (variables y, tau, gam) from their
   written definitions with an own sparse Fraction polynomial engine; compare canonical
   coefficient digests with the certificates and with the residual JSON 'expr' strings
   (parsed by regex, never eval'ed).
3. Exact integer Bernstein replay of every leaf: prefix-free + complete binary cover; girth-4
   leaves: each axis split at least once, every coefficient >= 0 and every open-cube vertex
   coefficient > 0; residual leaves: the labelled selector holds.
4. Engine self-test: exact Bernstein evaluation on leaf boxes equals direct evaluation.
5. An own adaptive cover of the residual 3-parameter statement with a different split rule.
6. Exact random point samples (not proofs) of the residual statement and of case (d).
7. Negative controls that must fail for the stated reason.
"""
import hashlib, json, math, random, re, sys, time
from fractions import Fraction as Fr

PH = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/'
G4P = PH + 'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json'
RESP = PH + 'frontier-20261029-ph7-no-two-cycle-residual-certificate-v1.json'
EXPECT = {G4P: ('b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8', 254486, 10697),
          RESP: ('45256245ecda8aed8ec18150c642fd70c3665cd9af31c49dc59fb25e367ed6be', 76318, 6659)}
OUT = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/'
       'f159-ph7-eight-ninths-impossibility/proofF159pa-cert-replay-v1-result.json')
RESULT = {'script': 'proofF159pa-cert-replay-v1.py', 'started_unix': time.time()}


def load(path):
    raw = open(path, 'rb').read()
    got = (hashlib.sha256(raw).hexdigest(), len(raw), raw.count(b'\n'))
    assert got == EXPECT[path], (path, got)
    return json.loads(raw.decode('utf-8'))


# ---------------- sparse polynomial engine ----------------
def clean(p):
    return {k: v for k, v in p.items() if v != 0}


def padd(*ps):
    o = {}
    for p in ps:
        for k, v in p.items():
            o[k] = o.get(k, 0) + v
    return clean(o)


def psc(p, c):
    return clean({k: v * c for k, v in p.items()})


def pmul(p, q):
    o = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            o[k] = o.get(k, 0) + v1 * v2
    return clean(o)


def var(i, n):
    e = [0] * n
    e[i] = 1
    return {tuple(e): Fr(1)}


def const(c, n):
    return {tuple([0] * n): Fr(c)} if c else {}


def esym(vs, k, n):
    # elementary symmetric polynomial via the recursion prod (1 + t v_i)
    E = [const(1, n)] + [{} for _ in range(k)]
    for v in vs:
        for j in range(k, 0, -1):
            E[j] = padd(E[j], pmul(E[j - 1], v))
    return E[k]


def peval(p, pt):
    s = Fr(0)
    for k, v in p.items():
        t = Fr(v)
        for e, x in zip(k, pt):
            if e:
                t *= Fr(x) ** e
        s += t
    return s


def digest(P):
    assert all(Fr(v).denominator == 1 for v in P.values())
    rows = [[list(k), str(int(v))] for k, v in sorted(P.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


def degs(P, n):
    return [max(k[i] for k in P) for i in range(n)]


# ---------------- generic exact Bernstein tensors ----------------
class Tensor:
    """Integer Bernstein coefficients on a box, flat storage with strides."""

    def __init__(self, shape, data):
        self.shape = tuple(shape)
        self.data = data
        st = []
        acc = 1
        for s in reversed(self.shape):
            st.append(acc)
            acc *= s
        self.strides = tuple(reversed(st))

    def idx(self, multi):
        return sum(a * b for a, b in zip(multi, self.strides))


def multi_indices(shape):
    if not shape:
        yield ()
        return
    for i in range(shape[0]):
        for rest in multi_indices(shape[1:]):
            yield (i,) + rest


_FIBER_CACHE = {}


def fibers(shape, ax):
    key = (shape, ax)
    if key not in _FIBER_CACHE:
        T = Tensor(shape, None)
        bases = []
        for m in multi_indices(shape):
            if m[ax] == 0:
                bases.append(T.idx(m))
        _FIBER_CACHE[key] = (bases, T.strides[ax])
    return _FIBER_CACHE[key]


def split(T, ax):
    """Exact midpoint de Casteljau; both halves scaled by 2^d (d = degree along ax)."""
    d = T.shape[ax] - 1
    if d == 0:
        return T, T
    bases, st = fibers(T.shape, ax)
    L = list(T.data)
    R = list(T.data)
    src = T.data
    for b in bases:
        row = [src[b + j * st] for j in range(d + 1)]
        levels = [row]
        for _ in range(d):
            prev = levels[-1]
            levels.append([prev[i] + prev[i + 1] for i in range(len(prev) - 1)])
        for j in range(d + 1):
            L[b + j * st] = levels[j][0] << (d - j)
            R[b + j * st] = levels[d - j][j] << j
    return Tensor(T.shape, L), Tensor(T.shape, R)


def bern_comb(m, d):
    return math.comb(d, m)


def initial_tensor(P, nv, compact_axes):
    """Bernstein coefficients on [0,1]^nv of the compactified polynomial.
    compact axes: x=s/(1-s) times (1-s)^deg; other axes: plain [0,1]."""
    dg = degs(P, nv)
    shape = tuple(d + 1 for d in dg)
    vals = {}
    for m in multi_indices(shape):
        # sum over power exponents j <= m on plain axes; j == m on compact axes
        ranges = []
        for ax in range(nv):
            if ax in compact_axes:
                ranges.append([m[ax]])
            else:
                ranges.append(list(range(m[ax] + 1)))
        tot = Fr(0)
        for j in _product(ranges):
            c = P.get(tuple(j), 0)
            if not c:
                continue
            w = Fr(c)
            for ax in range(nv):
                if ax in compact_axes:
                    w /= math.comb(dg[ax], j[ax])
                else:
                    w *= Fr(math.comb(m[ax], j[ax]), math.comb(dg[ax], j[ax]))
            tot += w
        vals[m] = tot
    L = 1
    for v in vals.values():
        L = math.lcm(L, v.denominator)
    T = Tensor(shape, [0] * math.prod(shape))
    for m, v in vals.items():
        T.data[T.idx(m)] = int(v * L)
    return T, L


def _product(ranges):
    if not ranges:
        yield ()
        return
    for a in ranges[0]:
        for rest in _product(ranges[1:]):
            yield (a,) + rest


def compact_value(P, nv, compact_axes, x):
    """Value of the compactified polynomial at a point x of [0,1)^nv (exact)."""
    dg = degs(P, nv)
    pt = []
    fac = Fr(1)
    for ax in range(nv):
        if ax in compact_axes:
            pt.append(Fr(x[ax]) / (1 - Fr(x[ax])))
            fac *= (1 - Fr(x[ax])) ** dg[ax]
        else:
            pt.append(Fr(x[ax]))
    return fac * peval(P, pt)


def bernstein_value(T, box, x):
    """Evaluate sum b_m prod C(d,m) t^m (1-t)^(d-m) on the box at x (exact)."""
    tot = Fr(0)
    ts = [(Fr(x[a]) - lo) / (hi - lo) for a, (lo, hi) in enumerate(box)]
    for m in multi_indices(T.shape):
        w = Fr(T.data[T.idx(m)])
        if not w:
            continue
        for a, mi in enumerate(m):
            d = T.shape[a] - 1
            w *= math.comb(d, mi) * ts[a] ** mi * (1 - ts[a]) ** (d - mi)
        tot += w
    return tot


def check_cover_structure(paths):
    s = set(paths)
    assert len(s) == len(paths), 'duplicate leaf'
    assert all(p and set(p) <= {'0', '1'} for p in paths) or all(set(p) <= {'0', '1'} for p in paths)
    prefixes = set()
    for p in s:
        for i in range(len(p)):
            prefixes.add(p[:i])
    clash = sorted(p for p in s if p in prefixes)
    assert not clash, ('not prefix-free', clash[:3])
    return s, prefixes


def replay(start, leafset, prefixes, nax, leaf_check):
    """DFS over the binary tree; axis = depth mod nax; bit 0 lower half, 1 upper half.
    start: dict name->Tensor. leaf_check(path, tensors, box_ints) must return True/raise."""
    stack = [('', start, tuple((0, 0) for _ in range(nax)))]
    seen = 0
    while stack:
        path, Ts, box = stack.pop()
        if path in leafset:
            leaf_check(path, Ts, box)
            seen += 1
            continue
        if path not in prefixes:
            raise AssertionError(('uncovered', path))
        ax = len(path) % nax
        Ls, Rs = {}, {}
        for k, T in Ts.items():
            Ls[k], Rs[k] = split(T, ax)
        k_, m_ = box[ax]
        bl = list(box)
        bl[ax] = (2 * k_ + 1, m_ + 1)
        stack.append((path + '1', Rs, tuple(bl)))
        bl = list(box)
        bl[ax] = (2 * k_, m_ + 1)
        stack.append((path + '0', Ls, tuple(bl)))
    assert seen == len(leafset), (seen, len(leafset))
    return seen


def box_fr(box):
    return [(Fr(k, 2 ** m), Fr(k + 1, 2 ** m)) for k, m in box]


def main():
    t0 = time.time()
    G4 = load(G4P)
    RS = load(RESP)
    RESULT['inputs_verified'] = {p: EXPECT[p][0] for p in EXPECT}

    # ============ girth-four certificate ============
    assert set(G4) == {'H_coefficients_sha256', 'H_positive_compactified_binary_leaf_paths', 'H_terms',
                       'H_variable_degrees', 'Q_coefficients_sha256', 'Q_positive_compactified_binary_leaf_paths',
                       'Q_terms', 'Q_variable_degrees', 'compactification', 'identity', 'scope', 'split_axis', 'z'}
    n = 6
    u = [var(i, n) for i in range(n)]
    f = [esym(u, k, n) for k in range(5)]
    c6 = lambda a: const(a, n)
    A = padd(f[2], psc(f[1], -4), c6(Fr(74, 9)))
    B = padd(f[3], psc(f[2], -4), psc(f[1], Fr(74, 9)), c6(Fr(-28, 3)))
    h0 = padd(f[4], psc(f[2], Fr(-70, 9)), psc(f[1], Fr(212, 9)), c6(Fr(-1007, 27)))
    h1 = padd(f[3], psc(f[1], Fr(-70, 9)), c6(Fr(212, 9)))
    Qp = psc(padd(pmul(A, A), psc(pmul(padd(f[1], c6(-4)), B), -1)), 81)
    Hp = psc(padd(pmul(h0, A), psc(pmul(h1, B), -1)), -243)
    g4 = {
        'Q_terms_own': len(Qp), 'H_terms_own': len(Hp),
        'Q_degrees_own': degs(Qp, n), 'H_degrees_own': degs(Hp, n),
        'Q_digest_own': digest(Qp), 'H_digest_own': digest(Hp),
    }
    g4['Q_digest_match'] = g4['Q_digest_own'] == G4['Q_coefficients_sha256']
    g4['H_digest_match'] = g4['H_digest_own'] == G4['H_coefficients_sha256']
    g4['terms_match'] = (len(Qp), len(Hp)) == (G4['Q_terms'], G4['H_terms'])
    g4['degrees_match'] = (degs(Qp, n), degs(Hp, n)) == (G4['Q_variable_degrees'], G4['H_variable_degrees'])
    assert g4['Q_digest_match'] and g4['H_digest_match'] and g4['terms_match'] and g4['degrees_match']
    assert G4['z'] == '8/9'

    allax = set(range(6))
    CORNERS = [(c, Tensor((3,) * 6, None).idx(tuple(2 * x for x in c))) for c in multi_indices((2,) * 6)]

    def g4_leaf_checker(stats):
        def chk(path, Ts, box):
            T = Ts['P']
            assert all(m >= 1 for _, m in box), ('axis never split', path)
            mn = min(T.data)
            assert mn >= 0, ('negative coefficient', path, mn)
            for corner, vidx in CORNERS:
                open_ = all((k > 0) if c == 0 else (k + 1 < 2 ** m) for c, (k, m) in zip(corner, box))
                if open_:
                    v = T.data[vidx]
                    assert v > 0, ('open-cube vertex not positive', path, corner)
                    stats['open_vertices'] += 1
            stats['coefficients'] += len(T.data)
            stats['zero_coefficients'] += sum(1 for v in T.data if v == 0)
            stats['maxdepth'] = max(stats['maxdepth'], len(path))
            return True
        return chk

    for name, P, key in (('Q', Qp, 'Q_positive_compactified_binary_leaf_paths'),
                         ('H', Hp, 'H_positive_compactified_binary_leaf_paths')):
        paths = G4[key]
        assert isinstance(paths, list) and all(isinstance(p, str) and p and set(p) <= {'0', '1'} for p in paths)
        leafset, prefixes = check_cover_structure(paths)
        T0, scale0 = initial_tensor(P, 6, allax)
        assert T0.shape == (3,) * 6
        stats = {'open_vertices': 0, 'coefficients': 0, 'zero_coefficients': 0, 'maxdepth': 0}
        ts = time.time()
        nleaf = replay({'P': T0}, leafset, prefixes, 6, g4_leaf_checker(stats))
        stats.update({'leaves': nleaf, 'initial_integer_scale': scale0, 'seconds': round(time.time() - ts, 2)})
        g4[name + '_replay'] = stats
        print(name, 'girth-four replay PASS', stats, flush=True)

    # engine self-test on a few girth-four leaves: Bernstein value == direct compactified value
    rng = random.Random(159)

    def descend(P, path, nax, compact_axes):
        T, sc = initial_tensor(P, nax, compact_axes)
        box = [(0, 0)] * nax
        scale = Fr(sc)
        for i, bit in enumerate(path):
            ax = i % nax
            Lt, Rt = split(T, ax)
            T = Rt if bit == '1' else Lt
            scale *= 2 ** (T.shape[ax] - 1)
            k_, m_ = box[ax]
            box[ax] = (2 * k_ + (bit == '1'), m_ + 1)
        return T, scale, box_fr(box)

    selftests = 0
    for name, P, key in (('Q', Qp, 'Q_positive_compactified_binary_leaf_paths'),
                         ('H', Hp, 'H_positive_compactified_binary_leaf_paths')):
        for path in rng.sample(G4[key], 3):
            T, scale, bx = descend(P, path, 6, allax)
            x = [lo + (hi - lo) * Fr(rng.randint(1, 99), 100) for lo, hi in bx]
            assert bernstein_value(T, bx, x) == scale * compact_value(P, 6, allax, x), (name, path)
            selftests += 1
    g4['engine_selftests_exact'] = selftests
    RESULT['girth4'] = g4

    # ============ residual certificate ============
    assert set(RS) == {'compactification', 'imported', 'leaf_counts', 'leaves', 'polynomials', 'selectors',
                       'split_axis', 'variables', 'z'}
    assert RS['z'] == '8/9'
    assert RS['imported'] == {'girth4_certificate_sha256_Q': G4['Q_coefficients_sha256'],
                              'girth4_certificate_sha256_H': G4['H_coefficients_sha256']}
    t3 = 3
    Y, Tt, Gm = var(0, t3), var(1, t3), var(2, t3)
    c3 = lambda a: const(a, t3)
    b1 = padd(psc(Y, Fr(1, 2)), Gm)
    al2 = psc(pmul(Tt, pmul(Y, Y)), Fr(3, 8))
    Abar = psc(padd(al2, psc(Y, -4), c3(Fr(74, 9)), pmul(b1, padd(Y, c3(-4))), psc(pmul(b1, b1), Fr(1, 4))), 144)
    Dbar = psc(padd(psc(pmul(Y, Y), 4), psc(Y, -16), c3(Fr(212, 9)), psc(pmul(Y, al2), Fr(-5, 6)),
                    pmul(b1, padd(al2, psc(pmul(Y, Y), -1), psc(Y, 4), c3(Fr(-70, 9))))), 144)
    F2 = psc(padd(Y, b1, c3(-4)), 2)
    polys = {'Abar': Abar, 'Dbar': Dbar, 'f1minus4': F2}
    varname = {'y': 0, 'tau': 1, 'gam': 2}

    def parse_expr(s):
        s = s.replace(' - ', ' + -')
        out = {}
        for term in s.split(' + '):
            term = term.strip()
            sign = -1 if term.startswith('-') else 1
            term = term.lstrip('-')
            coef = 1
            e = [0, 0, 0]
            for tok, pw in re.findall(r'(\d+|[a-z]+)(?:\*\*(\d+))?', term):
                if tok.isdigit():
                    coef *= int(tok)
                else:
                    e[varname[tok]] += int(pw) if pw else 1
            k = tuple(e)
            out[k] = out.get(k, 0) + sign * coef
        return clean({k: Fr(v) for k, v in out.items()})

    res = {}
    for k, P in polys.items():
        meta = RS['polynomials'][k]
        res[k] = {'digest_own': digest(P), 'digest_match': digest(P) == meta['sha256'],
                  'expr_parse_match': parse_expr(meta['expr']) == P,
                  'degrees_match': degs(P, 3) == meta['degrees'], 'degrees_own': degs(P, 3)}
        assert res[k]['digest_match'] and res[k]['expr_parse_match'] and res[k]['degrees_match'], (k, res[k])
    leaves = RS['leaves']
    assert isinstance(leaves, list) and all(isinstance(e, list) and len(e) == 2 and isinstance(e[0], str)
                                            and e[1] in ('Abar<=0', 'Dbar<=0', 'f1-4<0') for e in leaves)
    labels = {}
    for p, lab in leaves:
        assert p not in labels
        labels[p] = lab
    counts = {lab: sum(1 for _, l in leaves if l == lab) for lab in ('Abar<=0', 'Dbar<=0', 'f1-4<0')}
    assert counts == RS['leaf_counts'], counts
    compact3 = {0, 2}
    start = {k: initial_tensor(P, 3, compact3)[0] for k, P in polys.items()}
    rule = {'Abar<=0': ('Abar', 'le'), 'Dbar<=0': ('Dbar', 'le'), 'f1-4<0': ('f1minus4', 'lt')}

    def res_checker(lbl, stats):
        def chk(path, Ts, box):
            name, r = rule[lbl[path]]
            mx = max(Ts[name].data)
            ok = (mx <= 0) if r == 'le' else (mx < 0)
            assert ok, ('selector fails', path, lbl[path], mx)
            stats[lbl[path]] = stats.get(lbl[path], 0) + 1
            stats['maxdepth'] = max(stats['maxdepth'], len(path))
            return True
        return chk

    leafset, prefixes = check_cover_structure([p for p, _ in leaves])
    st = {'maxdepth': 0}
    nres = replay(start, leafset, prefixes, 3, res_checker(labels, st))
    res['replay'] = {'leaves': nres, **st}
    print('residual replay PASS', res['replay'], flush=True)
    # engine self-test on residual leaves
    stc = 0
    for path in rng.sample(sorted(labels), 6):
        for k, P in polys.items():
            T, scale, bx = descend(P, path, 3, compact3)
            x = [lo + (hi - lo) * Fr(rng.randint(1, 99), 100) for lo, hi in bx]
            if any(xx >= 1 for i, xx in enumerate(x) if i in compact3):
                continue
            assert bernstein_value(T, bx, x) == scale * compact_value(P, 3, compact3, x), (k, path)
            stc += 1
    res['engine_selftests_exact'] = stc

    # own adaptive cover with a different split rule (widest box side; ties s, g, tau)
    def own_cover(maxdepth=60):
        stack = [(start, ((0, 0), (0, 0), (0, 0)), 0)]
        nleaf = 0
        lab = {'Abar<=0': 0, 'Dbar<=0': 0, 'f1-4<0': 0}
        deepest = 0
        while stack:
            Ts, box, dep = stack.pop()
            if max(Ts['f1minus4'].data) < 0:
                lab['f1-4<0'] += 1
            elif max(Ts['Dbar'].data) <= 0:
                lab['Dbar<=0'] += 1
            elif max(Ts['Abar'].data) <= 0:
                lab['Abar<=0'] += 1
            else:
                assert dep < maxdepth, ('own cover did not terminate', box)
                order = [0, 2, 1]
                ax = max(order, key=lambda a: (-box[a][1], -order.index(a)))
                Ls, Rs = {}, {}
                for k, T in Ts.items():
                    Ls[k], Rs[k] = split(T, ax)
                k_, m_ = box[ax]
                bl = list(box)
                bl[ax] = (2 * k_, m_ + 1)
                br = list(box)
                br[ax] = (2 * k_ + 1, m_ + 1)
                stack.append((Ls, tuple(bl), dep + 1))
                stack.append((Rs, tuple(br), dep + 1))
                continue
            nleaf += 1
            deepest = max(deepest, dep)
        return nleaf, lab, deepest

    nown, labown, deepown = own_cover()
    res['own_cover'] = {'leaves': nown, 'labels': labown, 'max_depth': deepown,
                        'rule': 'split widest side, ties s,g,tau; selector order f1-4<0, Dbar<=0, Abar<=0'}
    print('own independent residual cover PASS', res['own_cover'], flush=True)

    # exact random samples (not proofs)
    def esy(v, k):
        E = [Fr(1)] + [Fr(0)] * k
        for x in v:
            for j in range(k, 0, -1):
                E[j] += E[j - 1] * x
        return E[k]

    samp = {'points': 0, 'case_d_hits': 0, 'relax_violations': 0, 'residual_statement_violations': 0}
    for _ in range(4000):
        v = sorted(Fr(rng.randint(1, 4000), rng.randint(1, 1500)) for _ in range(6))
        a4, r5, r6 = v[:4], v[4], v[5]
        f1_, f2_, f3_, f4_ = (esy(v, k) for k in (1, 2, 3, 4))
        Ar = f2_ - 4 * f1_ + Fr(74, 9)
        h1r = f3_ - Fr(70, 9) * f1_ + Fr(212, 9)
        Dr = h1r - Ar * sum(a4)
        y_ = sum(a4)
        al2_ = esy(a4, 2)
        tau_ = al2_ / (Fr(3, 8) * y_ * y_)
        gam_ = r5 + r6 - y_ / 2
        assert 0 < tau_ <= 1 and gam_ >= 0
        pa = peval(Abar, (y_, tau_, gam_)) / 144
        pd = peval(Dbar, (y_, tau_, gam_)) / 144
        pf = peval(F2, (y_, tau_, gam_)) / 2
        assert pf == f1_ - 4
        if not (Ar <= pa and Dr <= pd):
            samp['relax_violations'] += 1
        if Ar > 0 and Dr > 0 and f1_ >= 4:
            samp['case_d_hits'] += 1
        if pa > 0 and pd > 0 and pf >= 0:
            samp['residual_statement_violations'] += 1
        samp['points'] += 1
    for _ in range(20000):
        y_ = Fr(rng.randint(1, 3000), rng.randint(1, 300))
        tau_ = Fr(rng.randint(1, 1000), 1000)
        gam_ = Fr(rng.randint(0, 3000), rng.randint(1, 300))
        pa, pd, pf = (peval(P, (y_, tau_, gam_)) for P in (Abar, Dbar, F2))
        if pa > 0 and pd > 0 and pf >= 0:
            samp['residual_statement_violations'] += 1
        samp['points'] += 1
    assert samp['relax_violations'] == 0 and samp['case_d_hits'] == 0 and samp['residual_statement_violations'] == 0
    res['exact_samples'] = samp
    RESULT['residual'] = res

    # ============ negative controls ============
    neg = {}
    # NC1: delete one residual leaf -> completeness must fail at exactly that path
    drop = sorted(labels)[len(labels) // 2]
    ls2 = set(leafset) - {drop}
    pf2 = set()
    for p in ls2:
        for i in range(len(p)):
            pf2.add(p[:i])
    try:
        replay(start, ls2, pf2, 3, lambda *a: True)
        neg['NC1_drop_residual_leaf'] = 'NOT DETECTED'
    except AssertionError as e:
        neg['NC1_drop_residual_leaf'] = {'dropped': drop, 'error': repr(e.args[0])[:120],
                                         'intended': e.args[0][0] == 'uncovered' and e.args[0][1] == drop}
    # NC2: relabel one leaf whose other selector is false
    victim = None
    for p in sorted(labels):
        if labels[p] == 'Abar<=0':
            T, _, _ = descend(Dbar, p, 3, compact3)
            if max(T.data) > 0:
                victim = p
                break
    lab2 = dict(labels)
    lab2[victim] = 'Dbar<=0'
    try:
        replay(start, leafset, prefixes, 3, res_checker(lab2, {'maxdepth': 0}))
        neg['NC2_relabel_leaf'] = 'NOT DETECTED'
    except AssertionError as e:
        neg['NC2_relabel_leaf'] = {'victim': victim, 'error': repr(e.args[0])[:120],
                                   'intended': e.args[0][0] == 'selector fails' and e.args[0][1] == victim}
    # NC3: weakened threshold 2(f1-4)+1 (i.e. f1<3.5 claimed) must break some f1-4<0 leaf
    F2w = padd(F2, c3(1))
    start_w = dict(start)
    start_w['f1minus4'] = initial_tensor(F2w, 3, compact3)[0]
    try:
        replay(start_w, leafset, prefixes, 3, res_checker(labels, {'maxdepth': 0}))
        neg['NC3_shifted_threshold'] = 'NOT DETECTED'
    except AssertionError as e:
        neg['NC3_shifted_threshold'] = {'error': repr(e.args[0])[:120],
                                        'intended': e.args[0][0] == 'selector fails' and e.args[0][2] == 'f1-4<0'}
    # NC4: delete one girth-four Q leaf -> uncovered
    qpaths = G4['Q_positive_compactified_binary_leaf_paths']
    dq = qpaths[len(qpaths) // 3]
    qs = set(qpaths) - {dq}
    qpre = set()
    for p in qs:
        for i in range(len(p)):
            qpre.add(p[:i])
    T0q = initial_tensor(Qp, 6, allax)[0]
    try:
        replay({'P': T0q}, qs, qpre, 6, lambda *a: True)
        neg['NC4_drop_girth4_leaf'] = 'NOT DETECTED'
    except AssertionError as e:
        neg['NC4_drop_girth4_leaf'] = {'dropped': dq, 'error': repr(e.args[0])[:120],
                                       'intended': e.args[0][0] == 'uncovered' and e.args[0][1] == dq}
    # NC5: Q' = Q - (floor(Q(p0))+2) with p0 = all rates 9/10, so Q'(p0) < 0; the leaf containing x0 = 9/19 must fail
    p0 = [Fr(9, 10)] * 6
    qv = peval(Qp, p0)
    shift = math.floor(qv) + 2
    Qm = padd(Qp, c6(-shift))
    assert peval(Qm, p0) < 0
    x0 = [Fr(9, 19)] * 6
    hit = None
    # locate leaf box containing x0 without subdividing every leaf
    for p in qpaths:
        bx = [[Fr(0), Fr(1)] for _ in range(6)]
        for i, bit in enumerate(p):
            ax = i % 6
            lo, hi = bx[ax]
            mid = (lo + hi) / 2
            bx[ax] = [mid, hi] if bit == '1' else [lo, mid]
        if all(lo <= xx <= hi for (lo, hi), xx in zip(bx, x0)):
            hit = p
            break
    Tm, scm, bxm = descend(Qm, hit, 6, allax)
    detected = min(Tm.data) < 0
    neg['NC5_shifted_Q_negative_at_equal_rates'] = {'Q(9/10,...)': str(qv), 'shift': shift, 'leaf': hit,
                                                    'digest_changed': digest(Qm) != G4['Q_coefficients_sha256'],
                                                    'leaf_has_negative_coefficient': min(Tm.data) < 0,
                                                    'intended': detected}
    RESULT['negative_controls'] = neg
    for k, v in neg.items():
        assert isinstance(v, dict) and v['intended'], (k, v)
    print('negative controls all detected for intended reasons', json.dumps(neg)[:600], flush=True)
    RESULT['seconds_total'] = round(time.time() - t0, 2)
    RESULT['verdict'] = 'PASS'
    with open(OUT, 'w') as fh:
        fh.write(json.dumps(RESULT, indent=1, sort_keys=True, default=str) + '\n')
    print('PASS; wrote', OUT)


if __name__ == '__main__':
    main()

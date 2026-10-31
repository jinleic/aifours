#!/usr/bin/env python3
"""proofF159pa lemma controls (reviewer ReviewF159ProofAttack, wave f159-ph7-eight-ninths-impossibility).

Independently authored; standard library exact Fraction arithmetic for every PASS/FAIL decision.
NumPy is used ONLY for clearly labelled floating diagnostics (Ky Fan slack, nonreal spectrum).
No author code is imported or executed.

L0  characteristic matching of D_z(y)(y^2+py+q), z=8/9 and general z (k=1+z)
L1  Lemma C algebra (seventh-rate split, SPLIT identities, beta2 cancellation, relaxations,
    sum-of-squares identities, case (a) bound) by own sparse polynomial expansion
L2  Lemma C case logic on exact random samples at z=8/9 (sanity, not proof)
L3  Lemma 2 cover identity + Lemma 3 coefficients, exact, random rational 7x7 Metzler matrices
    with one-way and bidirected edges (bidirected pairs (s t, s/t) so S is rational); negative
    controls: drop virtual cycles / use w+ + w- / drop one-way cycles must break the identity
L4  Lemma 1 exact (Sylvester) on zero-row-sum irreducible G; negative control: reversible G
    (equality case, real spectrum) gives singular -S
L5  exact end-to-end chain on actual matrices: Z7 circulants with a triple complex pair,
    z=9/175 and z=16/175: char poly, S spectrum, E4_z(ut)=W, K_z>=0 (z-dependent constants)
"""
import itertools, json, math, random, time
from fractions import Fraction as Fr
import numpy as np

OUT = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/'
       'f159-ph7-eight-ninths-impossibility/proofF159pa-lemma-controls-v1-result.json')
R = {'script': 'proofF159pa-lemma-controls-v1.py', 'started_unix': time.time()}


# ---------- sparse multivariate polynomials ----------
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


def psub(p, q):
    return padd(p, psc(q, -1))


def pmul(*ps):
    o = ps[0]
    for q in ps[1:]:
        r = {}
        for k1, v1 in o.items():
            for k2, v2 in q.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                r[k] = r.get(k, 0) + v1 * v2
        o = clean(r)
    return o


def var(i, n):
    e = [0] * n
    e[i] = 1
    return {tuple(e): Fr(1)}


def const(c, n):
    return {tuple([0] * n): Fr(c)} if c else {}


def esym(vs, k, n):
    E = [const(1, n)] + [{} for _ in range(k)]
    for v in vs:
        for j in range(k, 0, -1):
            E[j] = padd(E[j], pmul(E[j - 1], v))
    return E[k]


def iszero(p):
    return not clean(p)


# ---------- L0 characteristic matching ----------
def umul(a, b):
    o = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return o


def matching(z):
    """Return linear forms (dicts over '1','e1'..'e4') for p, q, W(=E4), E3 at ratio z."""
    k = 1 + Fr(z)
    quad = [k, Fr(2), Fr(1)]
    D = umul([Fr(0), Fr(1)], umul(quad, quad))  # ascending, degree 5
    Dg = lambda j: D[j] if 0 <= j < len(D) else Fr(0)
    assert Dg(5) == 1
    p = {'1': -Dg(4), 'e1': Fr(1)}
    q = {'1': -Dg(3), 'e2': Fr(1)}
    for key, v in p.items():
        q[key] = q.get(key, 0) - Dg(4) * v
    def lin(c0, cp, cq):
        o = {'1': c0}
        for key, v in p.items():
            o[key] = o.get(key, 0) + cp * v
        for key, v in q.items():
            o[key] = o.get(key, 0) + cq * v
        return o
    rhs4 = lin(Dg(2), Dg(3), Dg(4))
    rhs3 = lin(Dg(1), Dg(2), Dg(3))
    E4 = {'e3': Fr(1)}
    for key, v in rhs4.items():
        E4[key] = E4.get(key, 0) - v
    E3 = {'e4': Fr(1)}
    for key, v in rhs3.items():
        E3[key] = E3.get(key, 0) - v
    cl = lambda d: {a: b for a, b in d.items() if b != 0}
    return cl(p), cl(q), cl(E4), cl(E3)


def closed_forms(z):
    k = 1 + Fr(z)
    return ({'1': Fr(-4), 'e1': Fr(1)},
            {'1': 12 - 2 * k, 'e1': Fr(-4), 'e2': Fr(1)},
            {'1': 12 * k - 32, 'e1': 12 - 2 * k, 'e2': Fr(-4), 'e3': Fr(1)},
            {'1': 3 * k * k - 48, 'e1': 16 + 4 * k, 'e2': -(4 + 2 * k), 'e4': Fr(1)})


def L0():
    out = {}
    p, q, E4, E3 = matching(Fr(8, 9))
    cand = ({'1': Fr(-4), 'e1': Fr(1)},
            {'1': Fr(74, 9), 'e1': Fr(-4), 'e2': Fr(1)},
            {'1': Fr(-28, 3), 'e1': Fr(74, 9), 'e2': Fr(-4), 'e3': Fr(1)},
            {'1': Fr(-1007, 27), 'e1': Fr(212, 9), 'e2': Fr(-70, 9), 'e4': Fr(1)})
    out['z=8/9 matches candidate constants'] = (p, q, E4, E3) == cand
    ok = True
    for z in (Fr(0), Fr(1, 2), Fr(9, 175), Fr(78, 100), Fr(87, 100), Fr(8, 9), Fr(3, 2)):
        ok &= matching(z) == closed_forms(z)
    out['general-z closed forms (7 rational z)'] = ok
    # negative: z=87/100 constants differ from the 8/9 constants
    out['NEG z=87/100 constants differ from 8/9 (intended detection)'] = matching(Fr(87, 100)) != cand
    assert all(out.values()), out
    return out


# ---------- L1 Lemma C algebra ----------
def L1():
    n = 7
    r = [var(i, n) for i in range(6)]
    x = var(6, n)
    c = lambda a: const(a, n)
    f = [esym(r, k, n) for k in range(5)]
    e = [esym(r + [x], k, n) for k in range(5)]
    chk = {}
    chk['e_k = f_k + x f_{k-1}'] = all(iszero(psub(e[k], padd(f[k], pmul(x, f[k - 1])))) for k in range(1, 5))
    p7 = padd(e[1], c(-4))
    q7 = padd(e[2], psc(e[1], -4), c(Fr(74, 9)))
    E4 = padd(e[3], psc(e[2], -4), psc(e[1], Fr(74, 9)), c(Fr(-28, 3)))
    E3 = padd(e[4], psc(e[2], Fr(-70, 9)), psc(e[1], Fr(212, 9)), c(Fr(-1007, 27)))
    A = padd(f[2], psc(f[1], -4), c(Fr(74, 9)))
    B = padd(f[3], psc(f[2], -4), psc(f[1], Fr(74, 9)), c(Fr(-28, 3)))
    h0 = padd(f[4], psc(f[2], Fr(-70, 9)), psc(f[1], Fr(212, 9)), c(Fr(-1007, 27)))
    h1 = padd(f[3], psc(f[1], Fr(-70, 9)), c(Fr(212, 9)))
    S4 = padd(*r[:4])
    chk['p = f1 + x - 4'] = iszero(psub(p7, padd(f[1], x, c(-4))))
    chk['q = A + x(f1-4)'] = iszero(psub(q7, padd(A, pmul(x, padd(f[1], c(-4))))))
    chk['E4 = A x + B'] = iszero(psub(E4, padd(pmul(A, x), B)))
    chk['E3 = h0 + x h1'] = iszero(psub(E3, padd(h0, pmul(x, h1))))
    D = psub(h1, pmul(A, S4))
    E = psub(h0, pmul(B, S4))
    K = psub(E3, pmul(E4, S4))
    chk['K = E + x D'] = iszero(psub(K, padd(E, pmul(x, D))))
    chk['E A - B D = h0 A - h1 B'] = iszero(psub(psub(pmul(E, A), pmul(B, D)), psub(pmul(h0, A), pmul(h1, B))))
    a = r[:4]
    al = [esym(a, k, n) for k in range(5)]
    b1 = padd(r[4], r[5])
    b2 = pmul(r[4], r[5])
    K1 = padd(al[3], psc(pmul(al[1], al[2]), -1), psc(pmul(al[1], al[1]), 4), psc(al[1], -16), c(Fr(212, 9)))
    K2 = padd(al[2], psc(pmul(al[1], al[1]), -1), psc(al[1], 4), c(Fr(-70, 9)))
    chk['D = K1 + beta1 K2 (beta2 cancels)'] = iszero(psub(D, padd(K1, pmul(b1, K2))))
    chk['A = (al2-4al1+74/9) + beta1(al1-4) + beta2'] = iszero(
        psub(A, padd(al[2], psc(al[1], -4), c(Fr(74, 9)), pmul(b1, padd(al[1], c(-4))), b2)))
    Abar = padd(al[2], psc(al[1], -4), c(Fr(74, 9)), pmul(b1, padd(al[1], c(-4))), psc(pmul(b1, b1), Fr(1, 4)))
    Dbar = padd(psc(pmul(al[1], al[1]), 4), psc(al[1], -16), c(Fr(212, 9)), psc(pmul(al[1], al[2]), Fr(-5, 6)),
                pmul(b1, K2))
    d56 = psub(r[4], r[5])
    chk['Abar - A = (r5-r6)^2/4'] = iszero(psub(psub(Abar, A), psc(pmul(d56, d56), Fr(1, 4))))
    chk['Dbar - D = al1 al2/6 - al3'] = iszero(psub(psub(Dbar, D), psub(psc(pmul(al[1], al[2]), Fr(1, 6)), al[3])))
    sos3 = {}
    for i in range(4):
        for j in range(4):
            for k in range(j + 1, 4):
                if i in (j, k):
                    continue
                dd = psub(a[j], a[k])
                sos3 = padd(sos3, psc(pmul(a[i], dd, dd), Fr(1, 2)))
    chk['al1 al2 - 6 al3 = (1/2) sum a_i (a_j-a_k)^2'] = iszero(psub(psub(pmul(al[1], al[2]), psc(al[3], 6)), sos3))
    sos2 = {}
    for i in range(4):
        for j in range(i + 1, 4):
            dd = psub(a[i], a[j])
            sos2 = padd(sos2, pmul(dd, dd))
    chk['3 al1^2 - 8 al2 = sum (a_i-a_j)^2'] = iszero(psub(psub(psc(pmul(al[1], al[1]), 3), psc(al[2], 8)), sos2))
    sos6 = {}
    for i in range(6):
        for j in range(i + 1, 6):
            dd = psub(r[i], r[j])
            sos6 = padd(sos6, pmul(dd, dd))
    chk['5 f1^2 - 12 f2 = sum (r_i-r_j)^2'] = iszero(psub(psub(psc(pmul(f[1], f[1]), 5), psc(f[2], 12)), sos6))
    four = padd(c(4), psc(f[1], -1))
    chk['A - (4-f1)^2 = f2 + 4 f1 - f1^2 - 70/9'] = iszero(
        psub(psub(A, pmul(four, four)), padd(f[2], psc(f[1], 4), psc(pmul(f[1], f[1]), -1), c(Fr(-70, 9)))))
    s = var(0, 1)
    lhs = padd(psc(pmul(s, s), Fr(-7, 12)), psc(s, 4), {(0,): Fr(-70, 9)})
    sh = padd(s, {(0,): Fr(-24, 7)})
    chk['-(7/12)s^2+4s-70/9 = -58/63-(7/12)(s-24/7)^2'] = iszero(
        psub(lhs, padd({(0,): Fr(-58, 63)}, psc(pmul(sh, sh), Fr(-7, 12)))))
    # residual parametrisation: substitute al1=y, al2=(3/8)tau y^2, beta1=gam+y/2 (3 vars) and
    # compare with the displayed 144*Abar, 144*Dbar, 2(f1-4)
    Y, T, G = var(0, 3), var(1, 3), var(2, 3)
    c3 = lambda v: const(v, 3)
    al2 = psc(pmul(T, Y, Y), Fr(3, 8))
    be1 = padd(G, psc(Y, Fr(1, 2)))
    K2s = padd(al2, psc(pmul(Y, Y), -1), psc(Y, 4), c3(Fr(-70, 9)))
    Abs = psc(padd(al2, psc(Y, -4), c3(Fr(74, 9)), pmul(be1, padd(Y, c3(-4))), psc(pmul(be1, be1), Fr(1, 4))), 144)
    Dbs = psc(padd(psc(pmul(Y, Y), 4), psc(Y, -16), c3(Fr(212, 9)), psc(pmul(Y, al2), Fr(-5, 6)), pmul(be1, K2s)), 144)
    shown_A = {(0, 0, 2): 36, (1, 0, 1): 180, (0, 0, 1): -576, (2, 1, 0): 54, (2, 0, 0): 81, (1, 0, 0): -864, (0, 0, 0): 1184}
    shown_D = {(2, 1, 1): 54, (2, 0, 1): -144, (1, 0, 1): 576, (0, 0, 1): -1120, (3, 1, 0): -18, (3, 0, 0): -72,
               (2, 0, 0): 864, (1, 0, 0): -2864, (0, 0, 0): 3392}
    chk['144 Abar(y,tau,gam) equals displayed polynomial'] = Abs == {k: Fr(v) for k, v in shown_A.items()}
    chk['144 Dbar(y,tau,gam) equals displayed polynomial'] = Dbs == {k: Fr(v) for k, v in shown_D.items()}
    # negative control: a deliberately wrong coefficient (Dbar with -(4/6) instead of -(5/6)) must not match
    Dwrong = psc(padd(psc(pmul(Y, Y), 4), psc(Y, -16), c3(Fr(212, 9)), psc(pmul(Y, al2), Fr(-4, 6)), pmul(be1, K2s)), 144)
    chk['NEG altered Dbar coefficient detected'] = Dwrong != {k: Fr(v) for k, v in shown_D.items()}
    assert all(chk.values()), {k: v for k, v in chk.items() if not v}
    return chk


# ---------- L2 Lemma C case logic on exact samples ----------
def esy_num(v, k):
    E = [Fr(1)] + [Fr(0)] * k
    for x in v:
        for j in range(k, 0, -1):
            E[j] += E[j - 1] * x
    return E[k]


def crude(v, z=Fr(8, 9)):
    """Return p, q, E4, K for sorted positive v (len 7) with z-dependent constants."""
    e = [Fr(1)] + [esy_num(v, k) for k in range(1, 5)]
    P, Q, E4, E3 = closed_forms(z)
    ev = lambda form: sum(cf * (Fr(1) if key == '1' else e[int(key[1])]) for key, cf in form.items())
    p, q, w, e3 = ev(P), ev(Q), ev(E4), ev(E3)
    S4 = sum(sorted(v)[:4])
    return p, q, w, e3 - w * S4


def L2(rng):
    stats = {'samples': 0, 'all_four_hold': 0, 'case': {'a': 0, 'b': 0, 'c': 0, 'd': 0},
             'case_logic_violations': 0, 'closest_min_slack': None}
    best = None
    pts = []
    for _ in range(6000):
        v = sorted(Fr(rng.randint(1, 3000), rng.randint(1, 1000)) for _ in range(7))
        pts.append(v)
    for _ in range(6000):  # near the equal-rate danger zone
        t = Fr(rng.randint(850, 950), 1000)
        v = sorted(t + Fr(rng.randint(-60, 60), 1000) for _ in range(7))
        if v[0] > 0:
            pts.append(v)
    for v in pts:
        p, q, E4v, Kv = crude(v)
        stats['samples'] += 1
        if p > 0 and q > 0 and E4v >= 0 and Kv >= 0:
            stats['all_four_hold'] += 1
        six, x = v[:6], v[6]
        f1, f2, f3, f4 = (esy_num(six, k) for k in (1, 2, 3, 4))
        A = f2 - 4 * f1 + Fr(74, 9)
        B = f3 - 4 * f2 + Fr(74, 9) * f1 - Fr(28, 3)
        h0 = f4 - Fr(70, 9) * f2 + Fr(212, 9) * f1 - Fr(1007, 27)
        h1 = f3 - Fr(70, 9) * f1 + Fr(212, 9)
        S4 = sum(six[:4])
        D = h1 - A * S4
        Qpol = 81 * (A * A - (f1 - 4) * B)
        Hpol = -243 * (h0 * A - h1 * B)
        bad = False
        if Qpol <= 0 or Hpol <= 0:
            bad = True  # would contradict the girth-four certificate
        if f1 < 4:
            stats['case']['a'] += 1
            if p > 0 and q > 0:
                bad = True  # case (a) claims p>0 and q>0 are incompatible
        elif A <= 0:
            stats['case']['b'] += 1
            if q > 0 and E4v >= 0:
                bad = True
        elif D <= 0:
            stats['case']['c'] += 1
            if E4v >= 0 and Kv >= 0:
                bad = True
        else:
            stats['case']['d'] += 1
            bad = True  # case (d) claimed empty
        stats['case_logic_violations'] += bad
        m = min(p, q, E4v, Kv)
        if best is None or m > best:
            best = m
    stats['closest_min_slack'] = float(best)
    assert stats['all_four_hold'] == 0 and stats['case_logic_violations'] == 0, stats
    return stats


# ---------- exact linear algebra ----------
def det(M):
    M = [list(r) for r in M]
    n = len(M)
    d = Fr(1)
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            d = -d
        d *= M[col][col]
        inv = 1 / M[col][col]
        for r in range(col + 1, n):
            if M[r][col] != 0:
                fct = M[r][col] * inv
                for k in range(col, n):
                    M[r][k] -= fct * M[col][k]
    return d


def charpoly(M):
    """Faddeev-LeVerrier, exact: returns ascending coefficients of det(yI-M)."""
    n = len(M)
    c = [Fr(0)] * (n + 1)
    c[n] = Fr(1)
    Mk = [[Fr(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        AM = [[sum(M[i][l] * Mk[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        Mk = [[AM[i][j] + (c[n - k + 1] if i == j else 0) for j in range(n)] for i in range(n)]
        AMk = [[sum(M[i][l] * Mk[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
        c[n - k] = -Fr(sum(AMk[i][i] for i in range(n)), k)
    return c


def sub(M, idx):
    return [[M[i][j] for j in idx] for i in idx]


def shifted(M, y0, idx):
    return [[(y0 if i == j else 0) - M[i][j] for j in idx] for i in idx]


def strongly_connected(G):
    n = len(G)
    def reach(adj):
        seen = {0}
        st = [0]
        while st:
            i = st.pop()
            for j in range(n):
                if j not in seen and adj(i, j):
                    seen.add(j)
                    st.append(j)
        return len(seen) == n
    return reach(lambda i, j: i != j and G[i][j] != 0) and reach(lambda i, j: i != j and G[j][i] != 0)


# ---------- L3 Lemma 2 / Lemma 3 ----------
def rand_metzler(rng, n, p_bi, p_one, zero_rowsum):
    G = [[Fr(0)] * n for _ in range(n)]
    S = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            r = rng.random()
            if r < p_bi:
                s = Fr(rng.randint(1, 7), rng.randint(1, 4))
                t = Fr(rng.randint(1, 6), rng.randint(1, 6))
                G[i][j], G[j][i] = s * t, s / t
                S[i][j] = S[j][i] = s
            elif r < p_bi + p_one:
                w = Fr(rng.randint(1, 9), rng.randint(1, 4))
                if rng.random() < 0.5:
                    G[i][j] = w
                else:
                    G[j][i] = w
    for i in range(n):
        off = sum(G[i][j] for j in range(n) if j != i)
        G[i][i] = -(off + (0 if zero_rowsum else Fr(rng.randint(0, 4), 3)))
        S[i][i] = G[i][i]
    return G, S


def extra_cycles(G, S):
    n = len(G)
    one_way, groups = [], {}
    for k in range(3, n + 1):
        for verts in itertools.combinations(range(n), k):
            for rest in itertools.permutations(verts[1:]):
                seq = (verts[0],) + rest
                edges = [(seq[i], seq[(i + 1) % k]) for i in range(k)]
                w = Fr(1)
                for i, j in edges:
                    w *= G[i][j]
                    if w == 0:
                        break
                if w == 0:
                    continue
                if all(G[j][i] != 0 for i, j in edges):
                    key = frozenset(frozenset(e) for e in edges)
                    groups.setdefault(key, []).append((seq, w, edges))
                else:
                    one_way.append((frozenset(verts), w))
    virtual = []
    for key, lst in groups.items():
        assert len(lst) == 2, 'both orientations must be present'
        (s1, w1, ed1), (s2, w2, _) = lst
        sg = Fr(1)
        for i, j in ed1:
            sg *= S[i][j]
        assert sg * sg == w1 * w2
        virtual.append((frozenset(s1), w1 + w2 - 2 * sg, w1, w2, sg))
    return one_way, virtual


def rhs_values(S, extras, n, ys):
    """Right side of Lemma 2 evaluated exactly at every y0 in ys."""
    assert n < 9  # three pairwise disjoint extra cycles (>=3 states each) would need >= 9 states
    V = frozenset(range(n))
    # group the L-terms by the uncovered vertex set: coefficient of det((y0 I - S)_U)
    terms = {tuple(range(n)): Fr(1)}
    for vs, om in extras:
        U = tuple(sorted(V - vs))
        terms[U] = terms.get(U, Fr(0)) - om
    for (v1, o1), (v2, o2) in itertools.combinations(extras, 2):
        if v1 & v2:
            continue
        U = tuple(sorted(V - v1 - v2))
        terms[U] = terms.get(U, Fr(0)) + o1 * o2
    out = []
    for y0 in ys:
        tot = Fr(0)
        for U, cf in terms.items():
            if cf:
                tot += cf * (det(shifted(S, y0, U)) if U else Fr(1))
        out.append(tot)
    return out


def L3(rng):
    n = 7
    res = {'instances': 0, 'identity_pass': 0, 'lemma3_pass': 0, 'neg_drop_virtual_detected': 0,
           'neg_drop_virtual_applicable': 0, 'neg_sum_weight_detected': 0, 'neg_sum_weight_applicable': 0,
           'neg_drop_oneway_detected': 0, 'neg_drop_oneway_applicable': 0, 'virtual_cycles_total': 0,
           'oneway_cycles_total': 0, 'kyfan_min_slack_float': None, 'modes': {}}
    kmin = None
    modes = [('mixed', 0.35, 0.35), ('mixed-dense', 0.5, 0.4), ('all-bidirected', 1.0, 0.0),
             ('one-way-only', 0.0, 0.7), ('sparse', 0.2, 0.3)]
    for trial in range(15):
        name, pb, po = modes[trial % len(modes)]
        G, S = rand_metzler(rng, n, pb, po, zero_rowsum=(trial % 2 == 0))
        ow, vi = extra_cycles(G, S)
        extras = [(vs, om) for vs, om in ow] + [(v[0], v[1]) for v in vi]
        lhs = [det(shifted(G, Fr(y0), range(n))) for y0 in range(n + 1)]
        rhs = rhs_values(S, extras, n, [Fr(y0) for y0 in range(n + 1)])
        ok = lhs == rhs
        # coefficient-level cross-check by Faddeev-LeVerrier
        cG = charpoly(G)
        cS = charpoly(S)
        A = [[-S[i][j] for j in range(n)] for i in range(n)]
        W = sum(om for vs, om in extras if len(vs) == 3)
        C4 = sum(om for vs, om in extras if len(vs) == 4)
        T3 = sum(om * sum(A[i][i] for i in range(n) if i not in vs) for vs, om in extras if len(vs) == 3)
        # e_k(ut) as sums of principal minors of A=-S (independent of cS)
        ek = [sum(det(sub(A, J)) for J in itertools.combinations(range(n), k)) for k in range(5)]
        lem3 = (cS[6] == ek[1] and cS[5] == ek[2] and cS[4] == ek[3] and cS[3] == ek[4] and
                cG[6] == ek[1] and cG[5] == ek[2] and cG[4] == ek[3] - W and cG[3] == ek[4] - T3 - C4)
        res['instances'] += 1
        res['identity_pass'] += ok
        res['lemma3_pass'] += lem3
        res['virtual_cycles_total'] += len(vi)
        res['oneway_cycles_total'] += len(ow)
        res['modes'][name] = res['modes'].get(name, 0) + 1
        # negative controls
        if any(v[1] != 0 for v in vi):
            res['neg_drop_virtual_applicable'] += 1
            ex2 = [(vs, om) for vs, om in ow]
            res['neg_drop_virtual_detected'] += lhs != rhs_values(S, ex2, n, [Fr(y0) for y0 in range(n + 1)])
        if vi:
            res['neg_sum_weight_applicable'] += 1
            ex3 = [(vs, om) for vs, om in ow] + [(v[0], v[2] + v[3]) for v in vi]
            res['neg_sum_weight_detected'] += lhs != rhs_values(S, ex3, n, [Fr(y0) for y0 in range(n + 1)])
        if ow:
            res['neg_drop_oneway_applicable'] += 1
            ex4 = [(v[0], v[1]) for v in vi]
            res['neg_drop_oneway_detected'] += lhs != rhs_values(S, ex4, n, [Fr(y0) for y0 in range(n + 1)])
        # Ky Fan floating diagnostic
        Af = np.array([[float(x) for x in row] for row in A])
        ev = np.sort(np.linalg.eigvalsh(Af))
        kf = min(sum(Af[i][i] for i in J) - ev[:4].sum() for J in itertools.combinations(range(n), 4))
        kmin = kf if kmin is None else min(kmin, kf)
    res['kyfan_min_slack_float'] = kmin
    assert res['identity_pass'] == res['instances'] and res['lemma3_pass'] == res['instances'], res
    assert res['neg_drop_virtual_detected'] == res['neg_drop_virtual_applicable'] > 0, res
    assert res['neg_sum_weight_detected'] == res['neg_sum_weight_applicable'] > 0, res
    assert res['neg_drop_oneway_detected'] == res['neg_drop_oneway_applicable'] > 0, res
    assert kmin > -1e-9
    return res


# ---------- L4 Lemma 1 ----------
def leading_minors(M):
    return [det([row[:k] for row in M[:k]]) for k in range(1, len(M) + 1)]


def L4(rng):
    n = 7
    out = {'positive_instances': 0, 'all_negS_positive_definite': True, 'nonreal_spectrum_float': 0, 'sG_float_max_abs': 0.0,
           'lambda_max_S_float_max': None}
    lm = None
    tries = 0
    while out['positive_instances'] < 12:
        tries += 1
        G, S = rand_metzler(rng, n, 0.35, 0.35, zero_rowsum=True)
        if not strongly_connected(G):
            continue
        negS = [[-x for x in row] for row in S]
        pd = all(m > 0 for m in leading_minors(negS))
        Gf = np.array([[float(x) for x in row] for row in G])
        evG = np.linalg.eigvals(Gf)
        nonreal = bool(np.any(np.abs(evG.imag) > 1e-9))
        out['nonreal_spectrum_float'] += nonreal
        out['sG_float_max_abs'] = max(out['sG_float_max_abs'], float(abs(max(evG.real))))
        lmax = float(max(np.linalg.eigvalsh(np.array([[float(x) for x in row] for row in S]))))
        lm = lmax if lm is None else max(lm, lmax)
        if nonreal:
            out['all_negS_positive_definite'] &= pd
            out['positive_instances'] += 1
    out['lambda_max_S_float_max'] = lm
    out['tries'] = tries
    # negative control (equality case): reversible G with pi = squares, real spectrum
    pi = [Fr((i + 1) ** 2) for i in range(n)]
    Kc = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if rng.random() < 0.7 or j == i + 1:
                Kc[i][j] = Kc[j][i] = Fr(rng.randint(1, 9))
    G = [[(Kc[i][j] / pi[i] if i != j else 0) for j in range(n)] for i in range(n)]
    for i in range(n):
        G[i][i] = -sum(G[i][j] for j in range(n) if j != i)
    Sx = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                Sx[i][j] = G[i][i]
            elif G[i][j] != 0:
                Sx[i][j] = Kc[i][j] / ((i + 1) * (j + 1))  # = sqrt(G_ij G_ji) exactly
                assert Sx[i][j] ** 2 == G[i][j] * G[j][i]
    negS = [[-x for x in row] for row in Sx]
    lmn = leading_minors(negS)
    out['NEG reversible: det(-S)'] = str(lmn[-1])
    out['NEG reversible: -S positive definite'] = all(m > 0 for m in lmn)
    out['NEG reversible: strongly connected'] = strongly_connected(G)
    out['NEG reversible: intended (det(-S)=0, s(S)=s(G)=0)'] = lmn[-1] == 0 and all(m > 0 for m in lmn[:-1])
    assert out['all_negS_positive_definite'] and out['NEG reversible: intended (det(-S)=0, s(S)=s(G)=0)']
    return out


# ---------- L5 exact end-to-end chain on circulant matrices ----------
def L5():
    n = 7
    out = {}
    for a, b, sq in ((4, 1, 2), (9, 1, 3)):
        cvec = {1: a, 2: a, 4: a, 3: b, 5: b, 6: b}
        scale = Fr(2, 7 * (a + b))
        G = [[(scale * cvec[(j - i) % n] if i != j else -scale * 3 * (a + b)) for j in range(n)] for i in range(n)]
        z = Fr((a - b) ** 2, 7 * (a + b) ** 2)
        k = 1 + z
        cp = charpoly(G)
        quad = [k, Fr(2), Fr(1)]
        target = umul([Fr(0), Fr(1)], umul(quad, umul(quad, quad)))
        S = [[(scale * sq if i != j else G[i][i]) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j:
                    assert S[i][j] ** 2 == G[i][j] * G[j][i]
        A = [[-x for x in row] for row in S]
        # exact spectrum of A = scale*((3(a+b)+sq) I - sq J): eigenvalue on 1 and on 1-perp
        lam1 = scale * (3 * (a + b) + sq - n * sq)
        lam2 = scale * (3 * (a + b) + sq)
        one = [Fr(1)] * n
        assert all(sum(A[i][j] * one[j] for j in range(n)) == lam1 for i in range(n))
        v = [Fr(1), Fr(-1)] + [Fr(0)] * (n - 2)
        assert all(sum(A[i][j] * v[j] for j in range(n)) == lam2 * v[i] for i in range(n))
        ut = sorted([lam1] + [lam2] * 6)
        ek = [Fr(1)] + [esy_num(ut, kk) for kk in range(1, 5)]
        ek_minors = [sum(det(sub(A, J)) for J in itertools.combinations(range(n), kk)) for kk in range(5)]
        ow, vi = extra_cycles(G, S)
        extras = [(vs, om) for vs, om in ow] + [(x[0], x[1]) for x in vi]
        W = sum(om for vs, om in extras if len(vs) == 3)
        C4 = sum(om for vs, om in extras if len(vs) == 4)
        T3 = sum(om * sum(A[i][i] for i in range(n) if i not in vs) for vs, om in extras if len(vs) == 3)
        P, Q, E4f, E3f = closed_forms(z)
        ev = lambda form: sum(cf * (Fr(1) if key == '1' else ek[int(key[1])]) for key, cf in form.items())
        p, q, E4v, E3v = ev(P), ev(Q), ev(E4f), ev(E3f)
        S4 = sum(ut[:4])
        Kv = E3v - E4v * S4
        kyfan_exact = min(sum(A[i][i] for i in J) for J in itertools.combinations(range(n), 4)) >= S4
        rec = {'z': str(z), 'charpoly == y((y+1)^2+z)^3': cp == target, 'one_way_cycles': len(ow),
               'virtual_cycles': len(vi), 'ut': [str(x) for x in ut], 'ek(ut) == principal-minor sums': ek == ek_minors,
               'p': str(p), 'q': str(q), 'E4_z(ut)': str(E4v), 'W': str(W), 'E4_z(ut) == W': E4v == W,
               'E3_z(ut) == sum omega tr + C4': E3v == T3 + C4, 'K_z': str(Kv), 'K_z >= 0': Kv >= 0,
               'p>0,q>0': p > 0 and q > 0, 'kyfan_exact': kyfan_exact, 's(S)<0': lam1 > 0 and lam2 > 0,
               'K_z float': float(Kv), 'E4 float': float(E4v)}
        rec['p == 2 and q == 1+z (hidden quadratic is (y+1)^2+z)'] = p == 2 and q == 1 + z
        # negative controls. (i) The 8/9 constants are z-specific: applied to this matrix the [y^5] and
        # [y^3] matchings must fail. (E4 itself is z-insensitive here because e1(ut)=6, i.e. p=2:
        # E4_z - E4_{8/9} = 2(k_{8/9}-k_z)(e1-6); recorded, not used as a control.)
        P8, Q8, E48, E38 = closed_forms(Fr(8, 9))
        rec['NEG 8/9 constants: q != 1+z (intended)'] = ev(Q8) != 1 + z
        rec['NEG 8/9 constants: E3 != sum omega tr + C4 (intended)'] = ev(E38) != T3 + C4
        rec['note: e1(ut)'] = str(ek[1])
        # (ii) a no-virtual-cycle bookkeeping (only one-way cycles, none here) must break E4 = W
        W_naive = sum(om for vs, om in ow if len(vs) == 3)
        rec['NEG virtual cycles omitted: E4_z(ut) != W_naive (intended)'] = E4v != W_naive
        out['a=%d,b=%d' % (a, b)] = rec
        assert all(v for kk, v in rec.items() if isinstance(v, bool)), rec
    return out


def main():
    rng = random.Random(15901)
    t = time.time()
    R['L0_matching'] = L0(); print('L0 PASS', flush=True)
    R['L1_lemmaC_algebra'] = L1(); print('L1 PASS', flush=True)
    R['L2_lemmaC_case_logic_samples'] = L2(rng); print('L2 PASS', R['L2_lemmaC_case_logic_samples'], flush=True)
    R['L3_cover_identity'] = L3(rng); print('L3 PASS', R['L3_cover_identity'], flush=True)
    R['L4_lemma1'] = L4(rng); print('L4 PASS', R['L4_lemma1'], flush=True)
    R['L5_circulant_chain'] = L5(); print('L5 PASS', json.dumps(R['L5_circulant_chain'])[:900], flush=True)
    R['seconds'] = round(time.time() - t, 2)
    R['verdict'] = 'PASS'
    with open(OUT, 'w') as fh:
        fh.write(json.dumps(R, indent=1, sort_keys=True, default=str) + '\n')
    print('PASS; wrote', OUT)


if __name__ == '__main__':
    main()

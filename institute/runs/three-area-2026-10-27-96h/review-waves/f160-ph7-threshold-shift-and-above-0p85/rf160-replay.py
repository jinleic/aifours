#!/usr/bin/env python3
"""rf160-replay.py -- reviewer ReviewF160Threshold, review wave
f160-ph7-threshold-shift-and-above-0p85.

Independently authored exact replay.  It does not import, execute or copy any
author code.  Every polynomial is rebuilt from the WRITTEN definitions in the
packets (z1 packet section 2, z2 packet sections 3-4), the z-symbolic
identities are checked by exact sparse expansion with z as a polynomial
variable, and every certificate leaf is replayed by a DIRECT per-leaf method:
for each leaf box the Bernstein coefficients are computed from the monomial form
by an exact integer Taylor shift followed by the monomial->Bernstein conversion
(no subdivision tree, no de Casteljau recursion).  Leaf-list coverage is checked
separately (alphabet, prefix-freeness, Kraft sum exactly 1).  Only Python ints
and Fractions are used in any decision (numpy is used only as an object-dtype
container for exact Python ints/Fractions).

Usage:  python3 rf160-replay.py all   (identities + both certificates)
        python3 rf160-replay.py neg   (negative controls; each must FAIL for the
                                       intended reason)
A log is written next to this script as rf160-replay-<mode>-log.txt.
"""
import sys, json, hashlib, itertools, math, time, random
from fractions import Fraction as Fr
import numpy as np

PT = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/'
RD = '/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f160-ph7-threshold-shift-and-above-0p85/'
CERTS = {
    'z1': (PT + 'frontier-20261029-ph7-threshold-z1-certificate-v1.json',
           '62b279a132f0f7663dfefa2c0b2fd05591884f2a47928800decc58f39f6ba9af', 523925, 22880),
    'z2': (PT + 'frontier-20261029-ph7-threshold-z2-certificate-v1.json',
           '3824b33dffd55abb03e5174c65fec1d9a353c72c1403c7b3356e9f20603fc6df', 1593287, 144650),
}
Z1 = Fr(1753, 2000)
Z2 = Fr(17, 20)
LINES = []


def log(*a):
    s = ' '.join(str(t) for t in a)
    print(s, flush=True)
    LINES.append(s)


def check(cond, msg):
    if not cond:
        log('FAIL:', msg)
        flush_log()
        raise SystemExit(1)


MODE = sys.argv[1] if len(sys.argv) > 1 else 'all'


def flush_log():
    with open(RD + 'rf160-replay-%s-log.txt' % MODE, 'w') as fh:
        fh.write('\n'.join(LINES) + '\n')


# ---------------------------------------------------------------- sparse polynomials
def clean(p):
    return {k: v for k, v in p.items() if v != 0}


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def pscale(p, c):
    return clean({k: v * c for k, v in p.items()})


def psub(a, b):
    return padd(a, pscale(b, -1))


def pmul(a, b):
    out = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            k = tuple(i + j for i, j in zip(k1, k2))
            out[k] = out.get(k, 0) + v1 * v2
    return clean(out)


def pprod(*ps):
    r = ps[0]
    for p in ps[1:]:
        r = pmul(r, p)
    return r


class Ring:
    def __init__(self, names):
        self.names = list(names)
        self.n = len(names)

    def c(self, v):
        v = Fr(v)
        return {(0,) * self.n: v} if v != 0 else {}

    def v(self, name):
        e = [0] * self.n
        e[self.names.index(name)] = 1
        return {tuple(e): Fr(1)}


def esym(vs, kmax, R):
    """e_0..e_kmax of the polynomials vs via e_k <- e_k + v*e_{k-1}."""
    e = [R.c(1)] + [{} for _ in range(kmax)]
    for v in vs:
        for k in range(kmax, 0, -1):
            e[k] = padd(e[k], pmul(v, e[k - 1]))
    return e


def is_zero(p):
    return len(clean(p)) == 0


def coeff(p, i, d):
    """coefficient of (variable i)^d, variable i's slot set to 0."""
    return clean({k[:i] + (0,) + k[i + 1:]: v for k, v in p.items() if k[i] == d})


def degree(p, i):
    return max((k[i] for k in p), default=-1)


def subst(p, images, R):
    """substitute variable j of p by the polynomial images[j] of ring R."""
    cache = {}

    def power(j, e):
        if (j, e) not in cache:
            cache[(j, e)] = R.c(1) if e == 0 else pmul(power(j, e - 1), images[j])
        return cache[(j, e)]
    out = {}
    for k, v in p.items():
        t = R.c(v)
        for j, e in enumerate(k):
            if e:
                t = pmul(t, power(j, e))
        out = padd(out, t)
    return out


def integerize(p):
    L = 1
    for v in p.values():
        L = math.lcm(L, Fr(v).denominator)
    q = {}
    for k, v in p.items():
        w = Fr(v) * L
        assert w.denominator == 1
        q[k] = int(w)
    return q, L


def digest(pint):
    """SHA-256 of the JSON rows [[exponents],"integer"] sorted by exponent tuple
    (the digest convention stated in the certificates' generator; format only)."""
    rows = [[list(k), str(int(v))] for k, v in sorted(pint.items())]
    return hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()


def peval(p, point):
    tot = Fr(0)
    for k, v in p.items():
        t = Fr(v)
        for xi, e in zip(point, k):
            if e:
                t *= Fr(xi) ** e
        tot += t
    return tot


# ---------------------------------------------------------------- A. identities
def part_identities():
    log('== A. z-symbolic identities (exact sparse expansion, z a polynomial variable) ==')
    Ry = Ring(['y', 'z', 'p', 'q'])
    y, z, p, q = (Ry.v(s) for s in Ry.names)
    c = Ry.c
    quad = padd(pmul(padd(y, c(1)), padd(y, c(1))), z)
    T = pprod(y, quad, quad, padd(pmul(y, y), pmul(p, y), q))
    check(degree(T, 0) == 7 and is_zero(psub(coeff(T, 0, 7), c(1))), 'target monic of degree 7')
    zp1 = padd(c(1), z)
    claims = {
        6: padd(p, c(4)),
        5: padd(q, pscale(p, 4), c(6), pscale(z, 2)),
        4: padd(pscale(q, 4), pmul(padd(c(6), pscale(z, 2)), p), c(4), pscale(z, 4)),
        3: padd(pmul(padd(c(6), pscale(z, 2)), q), pmul(padd(c(4), pscale(z, 4)), p), pmul(zp1, zp1)),
        2: padd(pmul(padd(c(4), pscale(z, 4)), q), pmul(pmul(zp1, zp1), p)),
    }
    for d, cl in claims.items():
        check(is_zero(psub(coeff(T, 0, d), cl)), 'target coefficient of y^%d' % d)
    log('A1 target y((y+1)^2+z)^2(y^2+py+q): coefficients of y^7..y^2 exactly as used in Lemma 3 / Lemma 5: PASS')

    Re = Ring(['e1', 'e2', 'e3', 'e4', 'e5', 'z'])
    e1, e2, e3, e4, e5, zz = (Re.v(s) for s in Re.names)
    ce = Re.c
    pe = padd(e1, ce(-4))
    qe = padd(e2, pscale(e1, -4), ce(10), pscale(zz, -2))
    img = [ce(0), zz, pe, qe]
    co = {d: subst(coeff(T, 0, d), img, Re) for d in (6, 5, 4, 3, 2)}
    check(is_zero(psub(co[6], e1)) and is_zero(psub(co[5], e2)), 'p=e1-4, q=e2-4e1+10-2z solve [y^6]=e1, [y^5]=e2')
    W = psub(e3, co[4])
    E4w = padd(e3, pscale(e2, -4), pmul(padd(ce(10), pscale(zz, -2)), e1), pscale(zz, 12), ce(-20))
    check(is_zero(psub(W, E4w)), 'W = e3-[y^4] equals the written E4(z)')
    T3C4 = psub(e4, co[3])
    E3w = padd(e4, pmul(padd(ce(-6), pscale(zz, -2)), e2), pmul(padd(ce(20), pscale(zz, 4)), e1),
               pscale(pmul(zz, zz), 3), pscale(zz, 6), ce(-45))
    check(is_zero(psub(T3C4, E3w)), 'T3+C4 = e4-[y^3] equals the written E3(z)')
    zp1e = padd(ce(1), zz)
    E2w = psub(e5, padd(pmul(pmul(zp1e, zp1e), pe), pmul(padd(ce(4), pscale(zz, 4)), qe)))
    check(is_zero(psub(psub(e5, co[2]), E2w)), 'e5-[y^2] equals the written E2')
    log('A2 matching: p=e1-4, q=e2-4e1+10-2z, W=E4(z)=e3-4e2+(10-2z)e1+12z-20, '
        'T3+C4=E3(z)=e4-(6+2z)e2+(20+4z)e1+3z^2+6z-45, E2=e5-[(1+z)^2p+(4+4z)q]: PASS')
    # z = 8/9 specialisation reproduces the constants of the 8/9 candidate
    Rz = Ring(['e1', 'e2', 'e3', 'e4', 'e5', 'z'])
    s89 = [Rz.v('e1'), Rz.v('e2'), Rz.v('e3'), Rz.v('e4'), Rz.v('e5'), Rz.c(Fr(8, 9))]
    q89 = subst(qe, s89, Rz)
    E4_89 = subst(E4w, s89, Rz)
    E3_89 = subst(E3w, s89, Rz)
    check(is_zero(psub(q89, padd(Rz.v('e2'), pscale(Rz.v('e1'), -4), Rz.c(Fr(74, 9))))), 'q at 8/9')
    check(is_zero(psub(E4_89, padd(Rz.v('e3'), pscale(Rz.v('e2'), -4), pscale(Rz.v('e1'), Fr(74, 9)), Rz.c(Fr(-28, 3))))), 'E4 at 8/9')
    check(is_zero(psub(E3_89, padd(Rz.v('e4'), pscale(Rz.v('e2'), Fr(-70, 9)), pscale(Rz.v('e1'), Fr(212, 9)), Rz.c(Fr(-1007, 27))))), 'E3 at 8/9')
    log('A2b at z=8/9 the general formulas reduce to the 8/9 candidate constants 74/9, -28/3, -70/9, 212/9, -1007/27: PASS')

    R8 = Ring(['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'x', 'z'])
    c8 = R8.c
    r = [R8.v('r%d' % i) for i in range(1, 7)]
    x = R8.v('x')
    z8 = R8.v('z')

    def zl(a, b):
        return padd(c8(a), pscale(z8, b))
    f = esym(r, 5, R8)
    e7 = esym(r + [x], 5, R8)
    p7 = padd(e7[1], c8(-4))
    q7 = padd(e7[2], pscale(e7[1], -4), zl(10, -2))
    E4 = padd(e7[3], pscale(e7[2], -4), pmul(zl(10, -2), e7[1]), zl(-20, 12))
    E3 = padd(e7[4], pmul(zl(-6, -2), e7[2]), pmul(zl(20, 4), e7[1]), pscale(pmul(z8, z8), 3), zl(-45, 6))
    E2 = psub(e7[5], padd(pmul(pmul(zl(1, 1), zl(1, 1)), p7), pmul(zl(4, 4), q7)))
    A = padd(f[2], pscale(f[1], -4), zl(10, -2))
    B = padd(f[3], pscale(f[2], -4), pmul(zl(10, -2), f[1]), zl(-20, 12))
    h1 = padd(f[3], pmul(zl(-6, -2), f[1]), zl(20, 4))
    h0 = padd(f[4], pmul(zl(-6, -2), f[2]), pmul(zl(20, 4), f[1]), pscale(pmul(z8, z8), 3), zl(-45, 6))
    check(is_zero(psub(q7, padd(A, pmul(x, padd(f[1], c8(-4)))))), 'q = A + x(f1-4)')
    check(is_zero(psub(E4, padd(pmul(A, x), B))), 'E4 = A x + B')
    check(is_zero(psub(E3, padd(h0, pmul(x, h1)))), 'E3 = h0 + x h1')
    S4 = padd(*r[:4])
    D = psub(h1, pmul(A, S4))
    E = psub(h0, pmul(B, S4))
    check(is_zero(psub(psub(E3, pmul(E4, S4)), padd(E, pmul(x, D)))), 'E3 - E4*S4 = E + x D')
    check(is_zero(psub(psub(pmul(E, A), pmul(B, D)), psub(pmul(h0, A), pmul(h1, B)))), 'EA - BD = h0 A - h1 B')
    log('A3 seventh-rate splitting (x largest, f_k of the other six): q=A+x(f1-4), E4=Ax+B, E3=h0+xh1, '
        'E3-E4*S4=E+xD, EA-BD=h0A-h1B: PASS')

    al = esym(r[:4], 4, R8)
    be1 = padd(r[4], r[5])
    be2 = pmul(r[4], r[5])
    check(is_zero(psub(f[1], padd(al[1], be1))) and is_zero(psub(f[2], padd(al[2], pmul(al[1], be1), be2)))
          and is_zero(psub(f[3], padd(al[3], pmul(al[2], be1), pmul(al[1], be2)))), 'f_k in alpha/beta sums')
    K1 = padd(al[3], pscale(pmul(al[1], al[2]), -1), pscale(pmul(al[1], al[1]), 4), pscale(al[1], -16), zl(20, 4))
    K2 = padd(al[2], pscale(pmul(al[1], al[1]), -1), pscale(al[1], 4), zl(-6, -2))
    check(is_zero(psub(D, padd(K1, pmul(be1, K2)))), 'D = K1 + beta1*K2 (beta2 cancels)')
    Abar = padd(al[2], pmul(al[1], be1), pscale(pmul(be1, be1), Fr(1, 4)), pscale(padd(al[1], be1), -4), zl(10, -2))
    K1bar = padd(pscale(pmul(al[1], al[2]), Fr(1, 6) - 1), pscale(pmul(al[1], al[1]), 4), pscale(al[1], -16), zl(20, 4))
    Dbar = padd(K1bar, pmul(be1, K2))
    d56 = psub(r[4], r[5])
    check(is_zero(psub(psub(Abar, A), pscale(pmul(d56, d56), Fr(1, 4)))), 'Abar - A = (r5-r6)^2/4')
    check(is_zero(psub(psub(Dbar, D), psub(pscale(pmul(al[1], al[2]), Fr(1, 6)), al[3]))), 'Dbar - D = a1 a2/6 - a3')
    sos3 = {}
    for (a_, b_, c_) in itertools.combinations(r[:4], 3):
        sos3 = padd(sos3, pmul(a_, pmul(psub(b_, c_), psub(b_, c_))), pmul(b_, pmul(psub(a_, c_), psub(a_, c_))),
                    pmul(c_, pmul(psub(a_, b_), psub(a_, b_))))
    check(is_zero(psub(psub(pscale(pmul(al[1], al[2]), Fr(1, 6)), al[3]), pscale(sos3, Fr(1, 12)))),
          'a1a2/6 - a3 = (1/12) sum_triples [a(b-c)^2+b(a-c)^2+c(a-b)^2]')
    sq4 = {}
    for a_, b_ in itertools.combinations(r[:4], 2):
        sq4 = padd(sq4, pmul(psub(a_, b_), psub(a_, b_)))
    check(is_zero(psub(psub(pscale(pmul(al[1], al[1]), Fr(3, 8)), al[2]), pscale(sq4, Fr(1, 8)))),
          '(3/8)a1^2 - a2 = (1/8) sum (ri-rj)^2')
    sq6 = {}
    for a_, b_ in itertools.combinations(r, 2):
        sq6 = padd(sq6, pmul(psub(a_, b_), psub(a_, b_)))
    check(is_zero(psub(psub(pscale(pmul(f[1], f[1]), Fr(5, 12)), f[2]), pscale(sq6, Fr(1, 12)))),
          '(5/12)f1^2 - f2 = (1/12) sum (ri-rj)^2')
    gap = {}
    for i in range(4):
        gap = padd(gap, psub(r[4], r[i]), psub(r[5], r[i]))
    check(is_zero(psub(psub(be1, pscale(al[1], Fr(1, 2))), pscale(gap, Fr(1, 4)))),
          'beta1 - a1/2 = (1/4) sum_{i<=4} [(r5-ri)+(r6-ri)]')
    check(is_zero(psub(psub(pscale(pmul(be1, be1), Fr(1, 4)), be2), pscale(pmul(d56, d56), Fr(1, 4)))),
          'beta1^2/4 - beta2 = (r5-r6)^2/4')
    log('A4 case (d): D=K1+beta1*K2, Abar-A=(r5-r6)^2/4>=0, Dbar-D=a1a2/6-a3>=0, and exact nonnegative forms of '
        'beta2<=beta1^2/4, a3<=a1a2/6, a2<=(3/8)a1^2, beta1>=a1/2 (sorted), f2<=(5/12)f1^2: PASS')

    four = psub(c8(4), f[1])
    check(is_zero(psub(psub(A, pmul(four, four)), padd(f[2], pscale(f[1], 4), pscale(pmul(f[1], f[1]), -1), zl(-6, -2)))),
          'case (a) identity')
    R1 = Ring(['s', 'z'])
    s1 = R1.v('s')
    zr = R1.v('z')
    lhs = padd(pscale(pmul(s1, s1), Fr(-7, 12)), pscale(s1, 4), R1.c(-6), pscale(zr, -2))
    sh = padd(s1, R1.c(Fr(-24, 7)))
    rhs = padd(R1.c(Fr(6, 7)), pscale(zr, -2), pscale(pmul(sh, sh), Fr(-7, 12)))
    check(is_zero(psub(lhs, rhs)), 'case (a) completed square')
    check(Fr(6, 7) - 2 * Z1 < 0 and Fr(6, 7) - 2 * Z2 < 0, 'case (a) sign at z1 and z2')
    log('A5 case (a): A-(4-f1)^2=f2+4f1-f1^2-6-2z<=6/7-2z-(7/12)(f1-24/7)^2<0 for z>3/7; z1,z2>3/7: PASS')

    S3 = padd(*r[:3])
    m2 = esym(r[:4], 2, R8)[2]
    L4 = padd(r[3], r[4], r[5], x)
    Y2b = psub(psub(E2, pmul(E4, m2)), pmul(S3, psub(E3, pmul(E4, L4))))
    check(degree(Y2b, 6) == 2, 'Y2b quadratic in x')
    check(is_zero(psub(coeff(Y2b, 6, 2), pmul(S3, A))), 'c2 = S3*A')
    log('A6 Lemma 5 quadratic: Y2b=E2-E4*m2-S3*(E3-E4*L4) has degree exactly 2 in x=v7 and c2=S3*A: PASS')


# ---------------------------------------------------------------- B. polynomials at a fixed ratio
def six_polys(z0):
    R6 = Ring(['u%d' % i for i in range(6)])
    u = [R6.v(nm) for nm in R6.names]
    c = R6.c
    g = esym(u, 4, R6)
    A = padd(g[2], pscale(g[1], -4), c(10 - 2 * z0))
    B = padd(g[3], pscale(g[2], -4), pscale(g[1], 10 - 2 * z0), c(12 * z0 - 20))
    h1 = padd(g[3], pscale(g[1], -(6 + 2 * z0)), c(20 + 4 * z0))
    h0 = padd(g[4], pscale(g[2], -(6 + 2 * z0)), pscale(g[1], 20 + 4 * z0), c(3 * z0 * z0 + 6 * z0 - 45))
    Qr = psub(pmul(A, A), pmul(padd(g[1], c(-4)), B))
    Hr = pscale(psub(pmul(h0, A), pmul(h1, B)), -1)
    return Qr, Hr


def n_polys(z0):
    R7 = Ring(['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'x'])
    w = [R7.v('v%d' % i) for i in range(1, 7)]
    x = R7.v('x')
    c = R7.c
    e = esym(w + [x], 5, R7)
    f = esym(w, 4, R7)
    p7 = padd(e[1], c(-4))
    q7 = padd(e[2], pscale(e[1], -4), c(10 - 2 * z0))
    E4 = padd(e[3], pscale(e[2], -4), pscale(e[1], 10 - 2 * z0), c(12 * z0 - 20))
    E3 = padd(e[4], pscale(e[2], -(6 + 2 * z0)), pscale(e[1], 20 + 4 * z0), c(3 * z0 * z0 + 6 * z0 - 45))
    E2 = psub(e[5], padd(pscale(p7, (1 + z0) ** 2), pscale(q7, 4 + 4 * z0)))
    S3 = padd(*w[:3])
    m2 = esym(w[:4], 2, R7)[2]
    L4 = padd(w[3], w[4], w[5], x)
    Y2b = psub(psub(E2, pmul(E4, m2)), pmul(S3, psub(E3, pmul(E4, L4))))
    check(degree(Y2b, 6) == 2, 'Y2b degree 2 in x at fixed z')
    c0, c1, c2 = (coeff(Y2b, 6, d) for d in range(3))
    A = padd(f[2], pscale(f[1], -4), c(10 - 2 * z0))
    B = padd(f[3], pscale(f[2], -4), pscale(f[1], 10 - 2 * z0), c(12 * z0 - 20))
    check(is_zero(psub(c2, pmul(S3, A))), 'c2 = S3*A at fixed z')
    v6 = w[5]
    at_v6 = w + [v6]                     # x -> v6
    E4v6 = subst(E4, at_v6, R7)
    Y2v6 = subst(Y2b, at_v6, R7)
    check(is_zero(psub(E4v6, padd(pmul(A, v6), B))), 'E4(x=v6) = A v6 + B')
    check(is_zero(psub(Y2v6, padd(pmul(c2, pmul(v6, v6)), pmul(c1, v6), c0))), 'Y2b(v6) = c2 v6^2 + c1 v6 + c0')
    dY = padd(pscale(pmul(c2, v6), 2), c1)
    polys = {
        'F': psub(c(4), f[1]),
        'A': A,
        'Q': psub(pmul(A, A), pmul(padd(f[1], c(-4)), B)),
        'mA': pscale(A, -1),
        'mE46': pscale(E4v6, -1),
        'mG6': pscale(Y2v6, -1),
        'mD6': pscale(dY, -1),
        'mDl': pscale(psub(pmul(c1, c1), pscale(pmul(c2, c0), 4)), -1),
    }
    out = {}
    for k, P in polys.items():
        check(all(kk[6] == 0 for kk in P), 'no x in N polynomial ' + k)
        out[k] = {kk[:6]: vv for kk, vv in P.items()}
    return out


def residual_polys(z0):
    """Case (d) chart reconstructed from the packet's bounds: y=alpha1 (sum of the four
    smallest of the six), gam=beta1-alpha1/2>=0, alpha2=(3/8)*tau*y^2, tau in [0,1];
    Abar uses beta2<=beta1^2/4, Dbar uses alpha3<=alpha1*alpha2/6."""
    Rr = Ring(['y', 'tau', 'gam'])
    y = Rr.v('y')
    tau = Rr.v('tau')
    gam = Rr.v('gam')
    c = Rr.c
    a1 = y
    b1 = padd(pscale(y, Fr(1, 2)), gam)
    a2 = pscale(pmul(tau, pmul(y, y)), Fr(3, 8))
    Abar = padd(a2, pmul(a1, b1), pscale(pmul(b1, b1), Fr(1, 4)), pscale(padd(a1, b1), -4), c(10 - 2 * z0))
    K2 = padd(a2, pscale(pmul(a1, a1), -1), pscale(a1, 4), c(-6 - 2 * z0))
    Dbar = padd(pscale(pmul(a1, a2), Fr(1, 6) - 1), pscale(pmul(a1, a1), 4), pscale(a1, -16), c(20 + 4 * z0), pmul(b1, K2))
    F = padd(a1, b1, c(-4))
    return {'Abar': Abar, 'Dbar': Dbar, 'f1minus4': F}


def parse_expr(s, names):
    s = s.replace(' ', '')
    terms, cur = [], ''
    for i, ch in enumerate(s):
        if ch in '+-' and i > 0 and s[i - 1] != '*':
            terms.append(cur)
            cur = ch
        else:
            cur += ch
    terms.append(cur)
    poly = {}
    for t in terms:
        sign = 1
        if t[0] in '+-':
            sign = -1 if t[0] == '-' else 1
            t = t[1:]
        coef, ex = 1, [0] * len(names)
        for fac in t.replace('**', '^').split('*'):
            if fac[0].isdigit():
                coef *= int(fac)
            else:
                nm, e = (fac.split('^') + ['1'])[:2]
                ex[names.index(nm)] += int(e)
        poly[tuple(ex)] = poly.get(tuple(ex), 0) + sign * coef
    return clean(poly)


# ---------------------------------------------------------------- C. direct per-leaf Bernstein machinery
_MAT = {}


def leaf_matrix(d, a, k):
    """Integer matrix taking monomial coefficients (c_0..c_d) of c(x) to
    L_d*2^(k*d) times the degree-d Bernstein coefficients of c on [a/2^k,(a+1)/2^k]."""
    key = (d, a, k)
    M = _MAT.get(key)
    if M is None:
        T = [[(math.comb(i, m) * a ** (i - m) * (1 << (k * (d - i)))) if i >= m else 0 for i in range(d + 1)]
             for m in range(d + 1)]
        L = math.lcm(*[math.comb(d, j) for j in range(d + 1)])
        Bm = [[(L // math.comb(d, m)) * math.comb(j, m) if m <= j else 0 for m in range(d + 1)] for j in range(d + 1)]
        M = np.array([[sum(Bm[j][m] * T[m][i] for m in range(d + 1)) for i in range(d + 1)] for j in range(d + 1)],
                     dtype=object)
        _MAT[key] = M
    return M


def leaf_scale(degs, boxes):
    s = 1
    for d, (a, k) in zip(degs, boxes):
        if d > 0:
            s *= math.lcm(*[math.comb(d, j) for j in range(d + 1)]) * (1 << (k * d))
    return s


def box_bernstein(arr, boxes):
    out = arr
    for ax, (a, k) in enumerate(boxes):
        d = out.shape[ax] - 1
        if d > 0:
            out = np.moveaxis(np.tensordot(leaf_matrix(d, a, k), out, axes=([1], [ax])), 0, ax)
    return out


def path_box(path, naxes):
    a, k = [0] * naxes, [0] * naxes
    for i, ch in enumerate(path):
        j = i % naxes
        a[j] = 2 * a[j] + (1 if ch == '1' else 0)
        k[j] += 1
    return list(zip(a, k))


def dense(p, nv, as_fraction=False):
    degs = [max((kk[j] for kk in p), default=0) for j in range(nv)]
    arr = np.empty([d + 1 for d in degs], dtype=object)
    for idx in itertools.product(*[range(d + 1) for d in degs]):
        arr[idx] = Fr(0) if as_fraction else 0
    for kk, v in p.items():
        arr[kk] = Fr(v) if as_fraction else int(v)
    return arr


def compactify(arr, axes):
    """monomial coefficients in x of prod_{j in axes}(1-x_j)^{d_j} P(.., x_j/(1-x_j), ..)."""
    out = arr
    for ax in axes:
        d = out.shape[ax] - 1
        K = np.array([[((-1) ** (m - a)) * math.comb(d - a, m - a) if m >= a else 0 for a in range(d + 1)]
                      for m in range(d + 1)], dtype=object)
        out = np.moveaxis(np.tensordot(K, out, axes=([1], [ax])), 0, ax)
    return out


def affine(arr, lo, w):
    """monomial coefficients in s of P(lo + w*s) along every axis (exact Fractions)."""
    out = arr
    for ax in range(out.ndim):
        d = out.shape[ax] - 1
        M = np.array([[Fr(math.comb(i, m)) * lo ** (i - m) * w ** m if i >= m else Fr(0) for i in range(d + 1)]
                      for m in range(d + 1)], dtype=object)
        out = np.moveaxis(np.tensordot(M, out, axes=([1], [ax])), 0, ax)
    return out


def int_array(arr):
    L = 1
    for v in arr.flat:
        L = math.lcm(L, Fr(v).denominator)
    out = np.empty(arr.shape, dtype=object)
    for idx in itertools.product(*[range(s) for s in arr.shape]):
        w = Fr(arr[idx]) * L
        assert w.denominator == 1
        out[idx] = int(w)
    return out, L


def bern_eval(B, boxes, tloc):
    """value of the scaled Bernstein form at box-local point tloc, divided by the scale."""
    out = B
    degs = [s - 1 for s in B.shape]
    for ax in range(B.ndim - 1, -1, -1):
        d = degs[ax]
        t = Fr(tloc[ax])
        vec = np.array([Fr(math.comb(d, j)) * t ** j * (1 - t) ** (d - j) for j in range(d + 1)], dtype=object)
        out = np.tensordot(out, vec, axes=([ax], [0]))
    val = out.item() if hasattr(out, 'item') else out
    return Fr(val) / leaf_scale(degs, boxes)


def coverage(paths):
    if not all(set(p) <= {'0', '1'} for p in paths):
        return False, 'alphabet'
    sp = sorted(paths)
    for a_, b_ in zip(sp, sp[1:]):
        if b_.startswith(a_):
            return False, 'prefix or duplicate: %r is a prefix of %r' % (a_, b_)
    Lm = max(len(p) for p in paths)
    tot = sum(1 << (Lm - len(p)) for p in paths)
    if tot != (1 << Lm):
        return False, 'Kraft sum %d/2^%d != 1' % (tot, Lm)
    return True, 'alphabet {0,1}, prefix-free, Kraft sum exactly 1 (complete partition), %d leaves, max depth %d' % (len(paths), Lm)


def pos_leaf(B, boxes, depth):
    if depth < 6:
        return 'depth<6'
    if min(B.flat) < 0:
        return 'negative Bernstein coefficient'
    nint = 0
    for corner in itertools.product((0, 1), repeat=B.ndim):
        idx, interior = [], True
        for j, cb in enumerate(corner):
            a, k = boxes[j]
            if cb == 0:
                interior = interior and a > 0
                idx.append(0)
            else:
                interior = interior and (a + 1) < (1 << k)
                idx.append(B.shape[j] - 1)
        if interior:
            nint += 1
            if B[tuple(idx)] <= 0:
                return 'interior-domain vertex coefficient <= 0'
    if nint == 0:
        return 'no interior-domain vertex'
    return None


def in_ncube(boxes):
    """compactified box inside [3/8, 9/16]^6"""
    return all(8 * a >= 3 * (1 << k) and 16 * (a + 1) <= 9 * (1 << k) for a, k in boxes)


def unsorted_box(boxes):
    return any(boxes[i][0] * (1 << boxes[j][1]) > (boxes[j][0] + 1) * (1 << boxes[i][1])
               for i in range(6) for j in range(i + 1, 6))


def replay_compact(arr, leaves, allow_n=False, stop_at_first=True):
    counts, fails = {}, []
    for path, lab in leaves:
        boxes = path_box(path, 6)
        if lab == 'N' and allow_n:
            err = None if in_ncube(boxes) else 'N leaf not inside [3/8,9/16]^6'
        elif lab == 'pos':
            err = pos_leaf(box_bernstein(arr, boxes), boxes, len(path))
        else:
            err = 'unknown label ' + lab
        if err:
            fails.append((path, lab, err))
            if stop_at_first:
                break
        counts[lab] = counts.get(lab, 0) + 1
    return counts, fails


RES_RULE = {'Abar<=0': ('Abar', 'le'), 'Dbar<=0': ('Dbar', 'le'), 'f1-4<0': ('f1minus4', 'lt')}


def replay_residual(arrs, leaves, stop_at_first=True):
    counts, fails = {}, []
    for path, lab in leaves:
        if lab not in RES_RULE:
            fails.append((path, lab, 'unknown label'))
            break
        nm, kind = RES_RULE[lab]
        mx = max(box_bernstein(arrs[nm], path_box(path, 3)).flat)
        ok = (mx <= 0) if kind == 'le' else (mx < 0)
        if not ok:
            fails.append((path, lab, 'sign condition fails (max coefficient %s)' % ('>0' if mx > 0 else '=0')))
            if stop_at_first:
                break
        counts[lab] = counts.get(lab, 0) + 1
    return counts, fails


NEED = {'unsorted': (), 'F': ('F',), 'A': ('A',), 'Q': ('Q',), 'E4v6': ('mA', 'mE46'),
        'Y2v6': ('mA', 'mG6', 'mD6'), 'Disc': ('mA', 'mDl')}


def n_label_ok(lab, mins, boxes):
    if lab == 'unsorted':
        return unsorted_box(boxes)
    if lab in ('F', 'A', 'Q'):
        return mins[lab] > 0
    if lab == 'E4v6':
        return mins['mA'] > 0 and mins['mE46'] > 0
    if lab == 'Y2v6':
        return mins['mA'] > 0 and mins['mG6'] > 0 and mins['mD6'] >= 0
    if lab == 'Disc':
        return mins['mA'] > 0 and mins['mDl'] > 0
    return False


def replay_n(arrs, leaves, stop_at_first=True):
    counts, fails = {}, []
    for path, lab in leaves:
        boxes = path_box(path, 6)
        if lab not in NEED:
            fails.append((path, lab, 'unknown label'))
            break
        mins = {nm: min(box_bernstein(arrs[nm], boxes).flat) for nm in NEED[lab]}
        if not n_label_ok(lab, mins, boxes):
            fails.append((path, lab, 'label condition fails'))
            if stop_at_first:
                break
        counts[lab] = counts.get(lab, 0) + 1
    return counts, fails


def load_cert(tag):
    path, sha, nbytes, nlf = CERTS[tag]
    raw = open(path, 'rb').read()
    h = hashlib.sha256(raw).hexdigest()
    check(h == sha and len(raw) == nbytes and raw.count(b'\n') == nlf, 'certificate %s hash/bytes/LF' % tag)
    log('%s certificate %s: sha256 %s, %d bytes, %d LF (matches manifest)' % (tag, path.rsplit('/', 1)[1], h, len(raw), raw.count(b'\n')))
    return json.loads(raw.decode('utf-8'))


def sample_machinery(arr, leaves, nax, target, nsamp, rng, label):
    """positive control of the per-leaf machinery: vertex coefficients and the Bernstein form at a
    random interior rational point must equal exact direct evaluation of the target function."""
    chosen = rng.sample(leaves, min(nsamp, len(leaves)))
    degs = [s - 1 for s in arr.shape]
    nvert = 0
    for path in chosen:
        boxes = path_box(path, nax)
        B = box_bernstein(arr, boxes)
        sc = leaf_scale(degs, boxes)
        lo = [Fr(a, 1 << k) for a, k in boxes]
        wd = [Fr(1, 1 << k) for a, k in boxes]
        for corner in rng.sample(list(itertools.product((0, 1), repeat=nax)), min(8, 2 ** nax)):
            pt = [lo[j] + wd[j] * corner[j] for j in range(nax)]
            tv = target(pt)
            if tv is None:          # vertex on a compactified face x_j=1 (u_j infinite): skipped
                continue
            idx = tuple(0 if corner[j] == 0 else degs[j] for j in range(nax))
            check(Fr(B[idx]) / sc == tv, 'vertex coefficient = exact value (%s)' % label)
            nvert += 1
        tl = [Fr(rng.randint(1, 999), 1000) for _ in range(nax)]
        pt = [lo[j] + wd[j] * tl[j] for j in range(nax)]
        check(bern_eval(B, boxes, tl) == target(pt), 'Bernstein form = exact value at interior point (%s)' % label)
    log('   machinery control %s: %d random leaves (%d vertices, %d interior points): vertex coefficients and interior '
        'Bernstein values equal exact direct evaluation: PASS' % (label, len(chosen), nvert, len(chosen)))


def compact_target(P, degs):
    def t(xpt):
        u = [xi / (1 - xi) if xi != 1 else None for xi in xpt]
        if any(v is None for v in u):
            # value at x_j=1 is the leading coefficient limit; avoid by construction (skip)
            return None
        s = peval(P, u)
        for xi, d in zip(xpt, degs):
            s *= (1 - xi) ** d
        return s
    return t


# ---------------------------------------------------------------- main replay
def run_all(rng):
    part_identities()

    # ---------------- z1
    log('== B1. z1 = 1753/2000 certificate ==')
    C1 = load_cert('z1')
    check(C1['z1'] == '1753/2000', 'z1 value string')
    Q1, H1 = six_polys(Z1)
    Q1i, LQ1 = integerize(Q1)
    H1i, LH1 = integerize(H1)
    for nm, P in (('Q', Q1i), ('H', H1i)):
        check([degree(P, j) for j in range(6)] == [2] * 6, nm + ' individual degree 2')
    check(LQ1 == C1['Q']['scale_lcm'] and LH1 == C1['H']['scale_lcm'], 'z1 scale lcms')
    check(len(Q1i) == C1['Q']['terms'] and len(H1i) == C1['H']['terms'], 'z1 term counts')
    check(digest(Q1i) == C1['Q']['sha256'] and digest(H1i) == C1['H']['sha256'], 'z1 Q/H digests')
    log('B1.1 Qpol(z1)=10^6[A^2-(f1-4)B] (168 terms), Hpol(z1)=-4*10^9[h0A-h1B] (435 terms) rebuilt from the written '
        'definitions; individual degree 2; scale lcms and coefficient digests equal the certificate: PASS')
    for nm, P, key in (('Qpol(z1)', Q1i, 'Q'), ('Hpol(z1)', H1i, 'H')):
        leaves = C1[key]['leaves']
        ok, msg = coverage(leaves)
        check(ok, nm + ' coverage: ' + msg)
        arr = compactify(dense(P, 6), range(6))
        t0 = time.time()
        cnt, fails = replay_compact(arr, [(p, 'pos') for p in leaves])
        check(not fails, '%s leaf failure %r' % (nm, fails[:1]))
        log('B1.2 %s: %s; every leaf (depth>=6, all coefficients>=0, every interior-domain vertex coefficient>0) '
            'verified by direct per-leaf Bernstein conversion: %d/%d PASS (%.1fs)' % (nm, msg, cnt['pos'], len(leaves), time.time() - t0))
        sample_machinery(arr, leaves, 6, compact_target(P, [2] * 6), 40, rng, nm)
    res1 = residual_polys(Z1)
    R1i = {}
    for nm, P in res1.items():
        jp = parse_expr(C1['residual']['polynomials'][nm]['expr'], ['y', 'tau', 'gam'])
        Pi, _ = integerize(P)
        check(set(jp) == set(P), 'residual %s monomial support equals JSON expr' % nm)
        kk = next(iter(jp))
        ratio = Fr(jp[kk]) / Fr(P[kk])
        check(ratio > 0 and pscale(P, ratio) == {k2: Fr(v) for k2, v in jp.items()}, 'residual %s = positive multiple of JSON expr' % nm)
        check(digest(jp) == C1['residual']['polynomials'][nm]['sha256'], 'residual %s digest (y,tau,gam order)' % nm)
        R1i[nm] = {k2: int(v) for k2, v in pscale(P, ratio).items()}
    log('B1.3 residual chart reconstructed (y=alpha1, gam=beta1-alpha1/2, alpha2=(3/8)tau*y^2): Abar, Dbar, f1-4 from the '
        'written bounds are positive multiples of the certificate expressions; digests in (y,tau,gam) order match: PASS')
    leaves3 = [tuple(t) for t in C1['residual']['leaves']]
    ok, msg = coverage([p for p, _ in leaves3])
    check(ok, 'z1 residual coverage: ' + msg)
    arrs3 = {nm: compactify(dense(P, 3), [0, 2]) for nm, P in R1i.items()}
    cnt, fails = replay_residual(arrs3, leaves3)
    check(not fails, 'z1 residual leaf failure %r' % (fails[:1],))
    check(cnt == C1['residual']['leaf_counts'], 'z1 residual counts')
    log('B1.4 z1 residual cover: %s; every leaf label verified (<=0 for Abar/Dbar, <0 for f1-4): %s PASS' % (msg, cnt))
    for nm in arrs3:
        lv = [p for p, lab in leaves3 if RES_RULE[lab][0] == nm]
        degs = [s - 1 for s in dense(R1i[nm], 3).shape]

        def tgt(pt, P=R1i[nm], degs=degs):
            s_, ta, g_ = pt
            if s_ == 1 or g_ == 1:
                return None
            return peval(P, [s_ / (1 - s_), ta, g_ / (1 - g_)]) * (1 - s_) ** degs[0] * (1 - g_) ** degs[2]
        sample_machinery_res(arrs3[nm], lv, tgt, rng, 'z1 residual ' + nm)

    # ---------------- z2
    log('== B2. z2 = 17/20 certificate ==')
    C2 = load_cert('z2')
    check(C2['z2'] == '17/20', 'z2 value string')
    Q2, H2 = six_polys(Z2)
    Q2i, LQ2 = integerize(Q2)
    H2i, LH2 = integerize(H2)
    check(LQ2 == C2['outer']['Q_scale_lcm'] and LH2 == C2['H']['scale_lcm'], 'z2 scale lcms')
    check(digest(Q2i) == C2['outer']['Q_sha256'] and digest(H2i) == C2['H']['sha256'], 'z2 Q/H digests')
    check(C2['outer']['N_cube'] == ['3/8', '9/16'] and C2['N']['box'] == ['3/5', '9/7'], 'N boxes')
    check(Fr(3, 8) / (1 - Fr(3, 8)) == Fr(3, 5) and Fr(9, 16) / (1 - Fr(9, 16)) == Fr(9, 7), 'N = image of [3/8,9/16]')
    log('B2.1 Qpol(z2)=100[A^2-(f1-4)B], Hpol(z2)=-4000[h0A-h1B] rebuilt; digests match; u=x/(1-x) maps [3/8,9/16] onto N=[3/5,9/7]: PASS')
    Hl = C2['H']['leaves']
    ok, msg = coverage(Hl)
    check(ok, 'z2 H coverage: ' + msg)
    arrH = compactify(dense(H2i, 6), range(6))
    t0 = time.time()
    cnt, fails = replay_compact(arrH, [(p, 'pos') for p in Hl])
    check(not fails, 'z2 H leaf failure %r' % (fails[:1],))
    log('B2.2 Hpol(z2): %s; all %d leaves verified: PASS (%.1fs)' % (msg, cnt['pos'], time.time() - t0))
    sample_machinery(arrH, Hl, 6, compact_target(H2i, [2] * 6), 40, rng, 'Hpol(z2)')
    Ol = [tuple(t) for t in C2['outer']['leaves']]
    ok, msg = coverage([p for p, _ in Ol])
    check(ok, 'z2 outer coverage: ' + msg)
    arrQ = compactify(dense(Q2i, 6), range(6))
    t0 = time.time()
    cnt, fails = replay_compact(arrQ, Ol, allow_n=True)
    check(not fails, 'z2 outer leaf failure %r' % (fails[:1],))
    check(cnt == {'pos': 9470, 'N': 312}, 'outer counts')
    log('B2.3 outer Q/N cover: %s; pos leaves Qpol(z2)>0 and N leaves inside [3/8,9/16]^6 verified: %s PASS (%.1fs)' % (msg, cnt, time.time() - t0))
    sample_machinery(arrQ, [p for p, lab in Ol if lab == 'pos'], 6, compact_target(Q2i, [2] * 6), 30, rng, 'Qpol(z2) outer')
    NPr = n_polys(Z2)
    NPi = {}
    for k, P in NPr.items():
        Pi, L = integerize(P)
        meta = C2['N']['polynomials'][k]
        check(L == meta['scale_lcm'] and digest(Pi) == meta['sha256'], 'N polynomial %s scale/digest' % k)
        NPi[k] = Pi
    check(NPi['Q'] == Q2i and digest(NPi['Q']) == C2['outer']['Q_sha256'], 'N Q equals outer Q')
    log('B2.4 N-cover polynomials F=4-f1, A, Q, mA=-A, mE46=-E4(v6), mG6=-Y2b(v6), mD6=-Y2b\'(v6), '
        'mDl=-(c1^2-4c2c0) rebuilt from the written Lemma 5 / Lemma C2 definitions (Y2b from e1..e5 of seven '
        'variables); scale lcms and digests match: PASS; degrees %s' % {k: [degree(P, j) for j in range(6)] for k, P in NPi.items()})
    lo, wdt = Fr(3, 5), Fr(9, 7) - Fr(3, 5)
    arrN, scN = {}, {}
    for k, P in NPi.items():
        arrN[k], scN[k] = int_array(affine(dense(P, 6, as_fraction=True), lo, wdt))
    Nl = [tuple(t) for t in C2['N']['leaves']]
    ok, msg = coverage([p for p, _ in Nl])
    check(ok, 'z2 N coverage: ' + msg)
    t0 = time.time()
    cnt, fails = replay_n(arrN, Nl)
    check(not fails, 'z2 N leaf failure %r' % (fails[:1],))
    check(cnt == C2['N']['leaf_counts'], 'N counts')
    log('B2.5 sorted affine N cover (v=3/5+(24/35)s): %s; every label verified (strict >0 except mD6>=0; '
        'unsorted: some i<j with lo_i>hi_j): %s PASS (%.1fs)' % (msg, cnt, time.time() - t0))
    for k in ('Q', 'mG6', 'mDl', 'mE46'):
        lv = [p for p, lab in Nl if k in NEED[lab]]
        P = NPi[k]
        Lk = scN[k]

        def tgtN(spt, P=P, Lk=Lk):
            return Lk * peval(P, [lo + wdt * si for si in spt])
        sample_machinery(arrN[k], lv, 6, tgtN, 15, rng, 'N ' + k)
    res2 = residual_polys(Z2)
    R2i = {}
    for nm, P in res2.items():
        jp = parse_expr(C2['residual']['polynomials'][nm]['expr'], ['y', 'tau', 'gam'])
        check(set(jp) == set(P), 'z2 residual %s monomial support equals JSON expr' % nm)
        kk = next(iter(jp))
        ratio = Fr(jp[kk]) / Fr(P[kk])
        check(ratio > 0 and pscale(P, ratio) == {k2: Fr(v) for k2, v in jp.items()}, 'z2 residual %s multiple' % nm)
        check(digest(jp) == C2['residual']['polynomials'][nm]['sha256'], 'z2 residual %s digest' % nm)
        R2i[nm] = {k2: int(v) for k2, v in pscale(P, ratio).items()}
    leaves3 = [tuple(t) for t in C2['residual']['leaves']]
    ok, msg = coverage([p for p, _ in leaves3])
    check(ok, 'z2 residual coverage: ' + msg)
    arrs3 = {nm: compactify(dense(P, 3), [0, 2]) for nm, P in R2i.items()}
    cnt, fails = replay_residual(arrs3, leaves3)
    check(not fails, 'z2 residual leaf failure %r' % (fails[:1],))
    check(cnt == C2['residual']['leaf_counts'], 'z2 residual counts')
    log('B2.6 z2 residual cover: %s; labels verified: %s PASS' % (msg, cnt))
    # diagnostics (not premises): Qpol(z2) negative inside N^6, so the N cover is genuinely needed
    a = Fr(447, 500)
    val = peval(Q2i, [a] * 6)
    log('D1 diagnostic: Qpol(z2) at six equal rates 447/500 = %s (%s); exact value sign confirms Qpol(z2) is not '
        'positive on the orthant, hence the outer/N split is necessary' % (float(val), 'NEGATIVE' if val < 0 else 'nonnegative'))


def sample_machinery_res(arr, leaves, target, rng, label):
    chosen = rng.sample(leaves, min(25, len(leaves)))
    degs = [s - 1 for s in arr.shape]
    nchk = 0
    for path in chosen:
        boxes = path_box(path, 3)
        B = box_bernstein(arr, boxes)
        sc = leaf_scale(degs, boxes)
        lo = [Fr(a, 1 << k) for a, k in boxes]
        wd = [Fr(1, 1 << k) for a, k in boxes]
        tl = [Fr(rng.randint(1, 999), 1000) for _ in range(3)]
        pt = [lo[j] + wd[j] * tl[j] for j in range(3)]
        tv = target(pt)
        if tv is None:
            continue
        check(bern_eval(B, boxes, tl) == tv, 'residual Bernstein form = exact value (%s)' % label)
        nchk += 1
    log('   machinery control %s: %d random leaves, interior Bernstein value equals exact direct evaluation: PASS' % (label, nchk))


# ---------------------------------------------------------------- negative controls
def run_neg(rng):
    log('== N. negative controls (each must FAIL for the intended reason) ==')
    C1 = load_cert('z1')
    C2 = load_cert('z2')
    # N1: the z1 Q cover applied to Qpol at z=7/8 < z_Q must fail
    Q78, _ = six_polys(Fr(7, 8))
    Q78i, _ = integerize(Q78)
    a = Fr(447, 500)
    v78 = peval(Q78i, [a] * 6)
    arr = compactify(dense(Q78i, 6), range(6))
    cnt, fails = replay_compact(arr, [(p, 'pos') for p in C1['Q']['leaves']], stop_at_first=False)
    xa = a / (1 + a)
    hit = None
    for p in C1['Q']['leaves']:
        bx = path_box(p, 6)
        if all(Fr(aa, 1 << k) <= xa <= Fr(aa + 1, 1 << k) for aa, k in bx):
            hit = p
            break
    hit_failed = any(fp == hit for fp, _, _ in fails)
    check(v78 < 0 and len(fails) > 0 and hit_failed, 'N1 expected failure not observed')
    log('N1 PASS(as negative): Qpol(7/8) at six equal rates 447/500 = %.6g < 0 exactly; the z1 Q leaves applied to Qpol(7/8) '
        'fail at %d of %d leaves, including the leaf %s containing the equal-rate point (reason: %s)'
        % (float(v78), len(fails), len(C1['Q']['leaves']), hit, [e for fp, _, e in fails if fp == hit][0]))
    # N2: coverage negatives
    L = list(C1['Q']['leaves'])
    ok1, m1 = coverage(L[:-1])
    ok2, m2 = coverage(L + [L[5] + '0'])
    ok3, m3 = coverage(L[:7] + [L[7][:-1]] + L[8:])
    check((not ok1) and (not ok2) and (not ok3), 'N2 coverage negatives')
    log('N2 PASS(as negative): dropping one leaf -> %s; adding a child of a leaf -> %s; truncating a leaf -> %s' % (m1, m2, m3))
    # N3: residual relabel
    R1 = residual_polys(Z1)
    R1i = {nm: integerize(P)[0] for nm, P in R1.items()}
    arrs3 = {nm: compactify(dense(P, 3), [0, 2]) for nm, P in R1i.items()}
    leaves3 = [tuple(t) for t in C1['residual']['leaves']]
    swapped = None
    for p, lab in leaves3:
        if lab == 'Dbar<=0':
            cnt, fails = replay_residual(arrs3, [(p, 'Abar<=0')])
            if fails:
                swapped = (p, fails[0][2])
                break
    check(swapped is not None, 'N3 expected relabel failure')
    log('N3 PASS(as negative): relabelling the Dbar<=0 leaf %s as Abar<=0 fails: %s' % swapped)
    # N4: z2 N cover replayed against the polynomials at z=21/25 (=0.84) must fail somewhere
    NP84 = n_polys(Fr(21, 25))
    lo, wdt = Fr(3, 5), Fr(9, 7) - Fr(3, 5)
    arrN = {k: int_array(affine(dense(integerize(P)[0], 6, as_fraction=True), lo, wdt))[0] for k, P in NP84.items()}
    Nl = [tuple(t) for t in C2['N']['leaves']]
    t0 = time.time()
    cnt, fails = replay_n(arrN, Nl, stop_at_first=False)
    bylab = {}
    for _, lab, _ in fails:
        bylab[lab] = bylab.get(lab, 0) + 1
    check(len(fails) > 0, 'N4 expected failures at z=0.84')
    log('N4 PASS(as negative): the z2 N leaves replayed against the N polynomials rebuilt at z=21/25 fail at %d of %d '
        'leaves (by label %s; %.1fs); the cover is specific to z2' % (len(fails), len(Nl), bylab, time.time() - t0))
    # N5: wrong sign of the H polynomial must fail at the first leaf checked
    _, H2 = six_polys(Z2)
    H2i, _ = integerize(H2)
    arrm = compactify(dense(pscale(H2i, -1), 6), range(6))
    cnt, fails = replay_compact(arrm, [(p, 'pos') for p in C2['H']['leaves'][:50]], stop_at_first=True)
    check(len(fails) == 1, 'N5 expected failure')
    log('N5 PASS(as negative): +(h0A-h1B) (wrong sign) fails the H leaf rule at leaf %s: %s' % (fails[0][0], fails[0][2]))


if __name__ == '__main__':
    t_start = time.time()
    rng = random.Random(20261029)
    log('rf160-replay mode=%s python=%s numpy=%s' % (MODE, sys.version.split()[0], np.__version__))
    if MODE == 'all':
        run_all(rng)
        log('RESULT: ALL POSITIVE REPLAYS PASS (%.1fs)' % (time.time() - t_start))
    elif MODE == 'neg':
        run_neg(rng)
        log('RESULT: ALL NEGATIVE CONTROLS FAILED FOR THE INTENDED REASON (%.1fs)' % (time.time() - t_start))
    else:
        raise SystemExit('mode must be all or neg')
    flush_log()

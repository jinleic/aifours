#!/usr/bin/env python3
"""Reviewer-written, standard-library-only replay for review wave
f90-ph7-equal-outer-all-common-rates (manifest-v1).  Version 3.
History (all earlier files kept, exclusive-create): v1 (review-replay.py)
stopped in its own helper self-test (too-strict disjointness assertion on
touching bisection isolators) and had a None+2 slip for the reviewer sample in
the unbounded last base interval; v2 (review-replay-v2.py) passed Parts A-C
but hung in Part D because its Sturm chain normalised every remainder to a
POSITIVE leading coefficient, which multiplies chain elements by -1 and
destroys the sign-variation property (23 phantom positive roots for the
degree-40 factor, non-separating clusters).  v3 normalises chain elements by
their positive content only (sign preserved), adds self-tests with known real
root counts that detect the v2 defect, and guards against non-separating
clusters.  Parts A-C are byte-identical in mathematics to v2.

Independent of the author's checker and replay: no author code is imported or
executed.  The certificate JSON is read ONLY as data (factor table, isolating
intervals, section samples) so that the recorded census can be checked; every
projection polynomial, factorization identity, root count, section and sign is
recomputed here from the elimination upward with exact Fraction arithmetic.

Parts
  A  spectral coefficient elimination (p,q,s3,s4,s2 via y^1 equation, LONG)
  B  the six constraint polynomials; comparison with certificate strings;
     Newton identities, Hankel = sum of squared 3x3 Vandermondes (Cauchy-Binet)
  C  23 projection polynomials by own Bareiss Sylvester determinants; exact
     identity with certificate factorization (scale * prod factor^mult)
  D  own Sturm chains: positive roots of the 17 factors (25), isolators, order
  E  own section census at the certificate V samples AND at reviewer-chosen V
     samples: s-roots > 4 isolated by own bisection, cells, full negative sets
Receipt written exclusive-create to review-replay-v3-receipt.json.
"""
import ast, json, random, time
from fractions import Fraction as Fr
from itertools import combinations
from math import gcd, lcm
from pathlib import Path

CERT = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/'
            'phase-type/frontier-20261028-ph7-equal-outer-open-cad-certificate.json')
OUT = Path(__file__).resolve().parent / 'review-replay-v3-receipt.json'
T0 = time.monotonic()
R = {'parts': {}}

# ---------------------------------------------------------------- multivariate
class MP:
    """Sparse multivariate polynomial over Q; monomial = exponent tuple."""
    __slots__ = ('n', 'c')
    def __init__(self, n, c=None):
        self.n = n
        self.c = {k: v for k, v in (c or {}).items() if v}
    @staticmethod
    def const(n, x):
        x = Fr(x)
        return MP(n, {(0,) * n: x} if x else {})
    @staticmethod
    def var(n, i):
        e = [0] * n; e[i] = 1
        return MP(n, {tuple(e): Fr(1)})
    def _co(self, b):
        return b if isinstance(b, MP) else MP.const(self.n, b)
    def __add__(self, b):
        b = self._co(b); c = dict(self.c)
        for k, v in b.c.items():
            c[k] = c.get(k, Fr(0)) + v
        return MP(self.n, c)
    __radd__ = __add__
    def __neg__(self):
        return MP(self.n, {k: -v for k, v in self.c.items()})
    def __sub__(self, b):
        return self + (-self._co(b))
    def __rsub__(self, b):
        return (-self) + b
    def __mul__(self, b):
        b = self._co(b); c = {}
        for k1, v1 in self.c.items():
            for k2, v2 in b.c.items():
                k = tuple(x + y for x, y in zip(k1, k2))
                c[k] = c.get(k, Fr(0)) + v1 * v2
        return MP(self.n, c)
    __rmul__ = __mul__
    def __pow__(self, e):
        r = MP.const(self.n, 1)
        for _ in range(e):
            r = r * self
        return r
    def __eq__(self, b):
        return self.c == self._co(b).c
    def iszero(self):
        return not self.c
    def deg(self, i):
        return max((k[i] for k in self.c), default=-1)
    def coeff(self, i, e):
        """coefficient of var_i^e (var_i exponent set to 0 in result)."""
        return MP(self.n, {k[:i] + (0,) + k[i + 1:]: v for k, v in self.c.items() if k[i] == e})
    def subs(self, i, val):
        """substitute var_i := val (MP of same arity) by Horner."""
        d = self.deg(i)
        r = MP.const(self.n, 0)
        for e in range(d, -1, -1):
            r = r * val + self.coeff(i, e)
        return r
    def ev(self, point):
        tot = Fr(0)
        for k, v in self.c.items():
            t = v
            for x, e in zip(point, k):
                if e:
                    t *= x ** e
            tot += t
        return tot

def plist_mul(a, b, n):
    """multiply two polynomials in y given as lists of MP coefficients."""
    out = [MP.const(n, 0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, yv in enumerate(b):
            out[i + j] = out[i + j] + x * yv
    return out

# ----------------------------------------------------------- univariate over Q
def utrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p
def uadd(a, b):
    n = max(len(a), len(b)); out = [Fr(0)] * n
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return utrim(out)
def uneg(a): return [-x for x in a]
def usub(a, b): return uadd(a, uneg(b))
def uiszero(a): return len(a) == 1 and a[0] == 0
def umul(a, b):
    if uiszero(utrim(a)) or uiszero(utrim(b)):
        return [Fr(0)]
    out = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, yv in enumerate(b):
                out[i + j] += x * yv
    return utrim(out)
def uscale(a, c): return utrim([x * c for x in a])
def udivmod(a, b):
    a = utrim(a); b = utrim(b)
    assert not uiszero(b)
    q = [Fr(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while len(r) >= len(b) and not uiszero(r):
        c = r[-1] / b[-1]; k = len(r) - len(b)
        q[k] = c
        for i, x in enumerate(b):
            r[i + k] -= c * x
        r = utrim(r)
        if len(r) < len(b):
            break
    return utrim(q), utrim(r)
def udiv_exact(a, b):
    q, r = udivmod(a, b)
    assert uiszero(r), 'inexact division'
    return q
def ueval(p, x):
    r = Fr(0)
    for c in reversed(p):
        r = r * x + c
    return r
def uderiv(p):
    return utrim([i * p[i] for i in range(1, len(p))]) if len(p) > 1 else [Fr(0)]
def udeg(p):
    p = utrim(p)
    return -1 if uiszero(p) else len(p) - 1
def ucontent(p):
    """divide by the positive content: integer coefficients, SIGN PRESERVED (for Sturm chains)."""
    p = utrim(p)
    if uiszero(p):
        return p
    den = 1
    for x in p: den = lcm(den, x.denominator)
    ints = [int(x * den) for x in p]
    g = 0
    for x in ints: g = gcd(g, abs(x))
    return [Fr(x // g) for x in ints]
def uprimitive(p):
    """integer primitive part with positive leading coefficient (factor-table comparison only)."""
    p = utrim(p)
    if uiszero(p):
        return p
    den = 1
    for x in p: den = lcm(den, x.denominator)
    ints = [int(x * den) for x in p]
    g = 0
    for x in ints: g = gcd(g, abs(x))
    ints = [x // g for x in ints]
    if ints[-1] < 0: ints = [-x for x in ints]
    return [Fr(x) for x in ints]

def sturm(p):
    """Sturm chain p0=p, p1=p', p_{i+1} = -rem(p_{i-1}, p_i); only POSITIVE rescaling allowed."""
    a = ucontent(p); assert udeg(a) >= 1
    seq = [a, ucontent(uderiv(a))]
    while udeg(seq[-1]) >= 1:
        _, r = udivmod(seq[-2], seq[-1])
        if uiszero(r):
            break
        seq.append(ucontent(uneg(r)))
    return seq
def variations(seq, x):
    vals = [(p[-1] if x is None else ueval(p, x)) for p in seq]  # None = +infinity
    sg = [1 if v > 0 else -1 for v in vals if v != 0]
    return sum(sg[i] != sg[i - 1] for i in range(1, len(sg)))
def nroots(seq, lo, hi):
    """distinct real roots in (lo, hi]; hi=None means +infinity. Requires p(lo)!=0."""
    return variations(seq, lo) - variations(seq, hi)
def cauchy_bound(p):
    p = utrim(p)
    return 1 + max(abs(c / p[-1]) for c in p[:-1]) if len(p) > 1 else Fr(1)
def isolate_above(p, lo):
    """own isolation of all distinct real roots of p in (lo, inf): sorted list of (a,b)
    with exactly one root in each open (a,b), a<b, p(a),p(b)!=0; intervals may touch."""
    p = utrim(p); seq = sturm(p)
    assert ueval(p, lo) != 0
    hi = max(cauchy_bound(p), lo + 1)
    while ueval(p, hi) == 0:
        hi += 1
    total = nroots(seq, lo, hi)
    assert total == nroots(seq, lo, None)
    work = [(lo, hi, total)]; out = []
    while work:
        a, b, k = work.pop()
        if k == 0:
            continue
        if k == 1:
            out.append((a, b)); continue
        assert b - a > Fr(1, 10 ** 60), 'non-separating root cluster: Sturm chain or multiple-root defect'
        m = (a + b) / 2
        if ueval(p, m) == 0:  # rational root hit exactly: nudge
            m = a + (b - a) * Fr(1, 3)
            assert ueval(p, m) != 0
        ka = nroots(seq, a, m)
        work.append((a, m, ka)); work.append((m, b, k - ka))
    out.sort()
    return out, seq
def refine(p, seq, a, b):
    """halve an isolating interval (a,b) of p keeping exactly one root."""
    m = (a + b) / 2
    if ueval(p, m) == 0:
        m = a + (b - a) * Fr(1, 3); assert ueval(p, m) != 0
    return (a, m) if nroots(seq, a, m) == 1 else (m, b)

# -------------------------------------------------- Q[V] matrices (Bareiss det)
def bareiss_det(M):
    """determinant of a square matrix with entries in Q[V] (lists), fraction-free."""
    M = [[utrim(list(x)) for x in row] for row in M]
    n = len(M); sign = 1; prev = [Fr(1)]
    for k in range(n - 1):
        if uiszero(M[k][k]):
            sw = next((i for i in range(k + 1, n) if not uiszero(M[i][k])), None)
            if sw is None:
                return [Fr(0)]
            M[k], M[sw] = M[sw], M[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = usub(umul(M[i][j], M[k][k]), umul(M[i][k], M[k][j]))
                M[i][j] = udiv_exact(num, prev)
            M[i][k] = [Fr(0)]
        prev = M[k][k]
    return uscale(M[n - 1][n - 1], sign)

def sylvester(f, g):
    """f,g: lists of Q[V] coefficients indexed by s-power. Standard Sylvester matrix."""
    m = len(f) - 1; n = len(g) - 1
    N = m + n
    M = [[[Fr(0)] for _ in range(N)] for _ in range(N)]
    for i in range(n):
        for j, c in enumerate(reversed(f)):
            M[i][i + j] = c
    for i in range(m):
        for j, c in enumerate(reversed(g)):
            M[n + i][i + j] = c
    return M
def resultant_s(f, g):
    return bareiss_det(sylvester(f, g))
def discriminant_s(f):
    n = len(f) - 1
    fd = [uscale(f[i], i) for i in range(1, len(f))]
    res = resultant_s(f, fd)
    sgn = -1 if (n * (n - 1) // 2) % 2 else 1
    return uscale(udiv_exact(res, f[-1]), sgn)

# unit tests of helpers on tiny known cases
assert udiv_exact(umul([Fr(1), Fr(2)], [Fr(3), Fr(4)]), [Fr(3), Fr(4)]) == [Fr(1), Fr(2)]
# Res_s(s^2-2, s-1) = 1^2-2 = -1 (constant coefficients in Q[V])
assert resultant_s([[Fr(-2)], [Fr(0)], [Fr(1)]], [[Fr(-1)], [Fr(1)]]) == [Fr(-1)]
# disc(s^2 + V s + 1) = V^2 - 4
assert discriminant_s([[Fr(1)], [Fr(0), Fr(1)], [Fr(1)]]) == [Fr(-4), Fr(0), Fr(1)]
# disc(s^4 - 1) = -256 ; Res(s^2-1, s^2-4) = 9
assert discriminant_s([[Fr(-1)], [Fr(0)], [Fr(0)], [Fr(0)], [Fr(1)]]) == [Fr(-256)]
assert resultant_s([[Fr(-1)], [Fr(0)], [Fr(1)]], [[Fr(-4)], [Fr(0)], [Fr(1)]]) == [Fr(9)]
_s = sturm([Fr(-2), Fr(0), Fr(1)])  # s^2-2
assert nroots(_s, Fr(0), None) == 1 and nroots(_s, Fr(-3), None) == 2
def _prod(rts):
    out = [Fr(1)]
    for r in rts: out = umul(out, [Fr(-r), Fr(1)])
    return out
# known real-root counts (these detect a sign-normalised, i.e. invalid, chain)
_p6 = _prod([1, 2, 3, 4, 5, 6]); assert nroots(sturm(_p6), Fr(0), None) == 6 and nroots(sturm(_p6), Fr(Fr(7, 2)), None) == 3
_pc = umul(umul([Fr(1), Fr(0), Fr(1)], [Fr(2), Fr(0), Fr(1)]), [Fr(3), Fr(0), Fr(1)]); assert nroots(sturm(_pc), Fr(-100), None) == 0
_pm = umul(_prod([1, 2]), [Fr(1), Fr(0), Fr(1)]); assert nroots(sturm(_pm), Fr(-100), None) == 2
_p5 = umul(_prod([0, 1, -1, 2, -2]), [Fr(1)]); assert nroots(sturm(_p5), Fr(-100), None) == 5 and nroots(sturm(_p5), Fr(Fr(1, 2)), None) == 2
_pr = _prod([Fr(1, 3), Fr(2, 7), Fr(5, 11), 3, 7, 10, 20]); assert nroots(sturm(_pr), Fr(0), None) == 7 and nroots(sturm(_pr), Fr(Fr(2, 5)), Fr(8)) == 3
_pd = umul(_prod([1, 1, 2]), [Fr(1)]); assert nroots(sturm(_pd), Fr(0), None) == 2   # distinct roots counted once
_iso, _ = isolate_above([Fr(6), Fr(-5), Fr(1)], Fr(0))  # (s-2)(s-3)
assert len(_iso) == 2 and _iso[0][0] < 2 < _iso[0][1] <= _iso[1][0] < 3 < _iso[1][1]

# ================================================================= PART A
# variables: 0=s(=s1), 1=s2, 2=V, 3=s5
NA = 4
s, s2, V, s5 = (MP.var(NA, i) for i in range(4))
one = MP.const(NA, 1)
quad = [MP.const(NA, Fr(17, 9)), MP.const(NA, 2), one]          # y^2 + 2y + 17/9 = (y+1)^2 + 8/9
Dy = plist_mul([MP.const(NA, 0), one], plist_mul(quad, quad, NA), NA)   # D(y) = y*quad^2
assert [c.ev((0, 0, 0, 0)) for c in Dy] == [0, Fr(289, 81), Fr(68, 9), Fr(70, 9), 4, 1]
p = s + 2 * V - 4
q = s2 + 2 * V * s + V * V - 4 * p - Fr(70, 9)
Qy = [q, p, one]
T = plist_mul(Dy, Qy, NA)        # T[j] = [y^j](D Q), j=0..7
assert len(T) == 8 and T[7] == one and T[0].iszero()
# P(y) = A(y)(y+V)^2 - D1 (y+V)^2 - D3 ; A monic deg 5 with e.s.f. s,s2,s3,s4,s5
assert T[6] == s + 2 * V and T[5] == s2 + 2 * V * s + V * V          # y^6, y^5 define p, q
r3 = T[4] - 2 * V * s2 - V * V * s                 # s3   (COEF, y^4)
r4 = T[3] - 2 * V * r3 - V * V * s2                # s4   (COEF, y^3)
D1 = s5 + 2 * V * r4 + V * V * r3 - T[2]           # y^2
E1 = 2 * V * s5 + V * V * r4 - 2 * V * D1 - T[1]   # y^1 residual
assert E1.deg(3) <= 0, 's5 must cancel from the y^1 equation'
assert E1 == -3 * V * V * r4 - 2 * V ** 3 * r3 + 2 * V * T[2] - T[1]
F1 = 9 * V * V - 18 * V + 17
L = (324 * s * V ** 3 - 1944 * s * V ** 2 + 1944 * s * V - 612 * s
     + (405 * V * V - 486 * V + 153) * s2 - 1296 * V ** 3 + 4626 * V ** 2 - 3996 * V + 1258)
prod = F1 * L
k0 = next(iter(prod.c)); ratio = E1.c.get(k0, Fr(0)) / prod.c[k0]
assert ratio != 0 and E1 == ratio * prod, 'y^1 equation factorization'
A_e1_ratio = str(ratio)
assert F1 == 9 * (V - 1) ** 2 + 8
d = 45 * V * V - 54 * V + 17
assert 405 * V * V - 486 * V + 153 == 9 * d
assert d == 45 * (V - Fr(3, 5)) ** 2 + Fr(4, 5)
L0 = L.subs(1, MP.const(NA, 0))
A2 = -L0                                            # A2 := 9 d s2
A2_cand = -2 * ((162 * V ** 3 - 972 * V ** 2 + 972 * V - 306) * s - 648 * V ** 3 + 2313 * V ** 2 - 1998 * V + 629)
assert A2 == A2_cand, 'A2 display'
def lin_sub(expr, num, den):
    """expr linear in var1 (s2): return den*expr with s2 := num/den, as a polynomial."""
    assert expr.deg(1) <= 1
    return den * expr.subs(1, MP.const(NA, 0)) + expr.coeff(1, 1) * num
A3 = lin_sub(r3, A2, 9 * d)                         # 9 d s3
A4 = 9 * lin_sub(r4, A2, 9 * d)                     # 81 d s4
LONG = 9 * lin_sub(T[2] - 2 * V * r4 - V * V * r3, A2, 9 * d)     # 81 d * (D3/V^2)
assert LONG == (s - 4) * (9 * (V - 1) ** 2 + 8) ** 3, 'LONG identity'
D3_num = 9 * lin_sub(V * V * (s5 - D1), A2, 9 * d)  # 81 d * D3 from the y^0 equation
assert D3_num == V * V * LONG
R['parts']['A_elimination'] = {
    'p': 's+2V-4', 'q_from_y5': True, 'COEF_s3_s4_from_y4_y3': True,
    'y1_residual_independent_of_s5_and_D1': True,
    'y1_residual_equals_ratio_times_(9V^2-18V+17)*L_ratio': A_e1_ratio,
    'd_positive_form': '45(V-3/5)^2+4/5', 'A2_display_matches': True,
    'LONG_identity_81d*(T2-2Vs4-V^2s3)==(s-4)(9(V-1)^2+8)^3': True,
}
print('A: elimination reconstructed; y^1 residual = %s * (9V^2-18V+17) * L; LONG holds' % A_e1_ratio)

# ================================================================= PART B
def to2(P):
    assert P.deg(1) <= 0 and P.deg(3) <= 0
    return MP(2, {(k[0], k[2]): v for k, v in P.c.items()})
S, W = MP.var(2, 0), MP.var(2, 1)      # S = s, W = V
f0 = S - 4
f1, f2, f3 = to2(A2), to2(A3), to2(A4)
d2 = 45 * W * W - 54 * W + 17; D0 = 9 * d2
f4 = 9 * f2 * f2 - 2 * f1 * f3                                   # Newton numerator
P2 = D0 * S ** 2 - 2 * f1
P3 = D0 * S ** 3 - 3 * S * f1 + 3 * f2
P4 = D0 ** 2 * S ** 4 - 4 * D0 * S ** 2 * f1 + 2 * f1 ** 2 + 4 * D0 * S * f2 - 4 * d2 * f3
f5 = 5 * P2 * P4 - 5 * D0 * P3 ** 2 - S ** 2 * D0 * P4 + 2 * S * D0 * P2 * P3 - P2 ** 3
polys = [f0, f1, f2, f3, f4, f5]
labels = ['s-4', 's2', 's3', 's4', 'newton3', 'hankel3']
degs = [(P.deg(0), P.deg(1)) for P in polys]
assert degs == [(1, 0), (1, 3), (1, 4), (1, 5), (2, 8), (4, 10)], degs

# Hankel/Newton derivations in (s, V, e2, e3, e4): S2=D0 e2, S3=D0 e3, S4=9 D0 e4
N5 = 5
x1, xV, e2, e3, e4 = (MP.var(N5, i) for i in range(5))
dd = 45 * xV * xV - 54 * xV + 17; DD = 9 * dd
S2, S3, S4 = DD * e2, DD * e3, 9 * DD * e4
pp2 = x1 ** 2 - 2 * e2
pp3 = x1 ** 3 - 3 * x1 * e2 + 3 * e3
pp4 = x1 ** 4 - 4 * x1 ** 2 * e2 + 2 * e2 ** 2 + 4 * x1 * e3 - 4 * e4
PP2 = DD * x1 ** 2 - 2 * S2
PP3 = DD * x1 ** 3 - 3 * x1 * S2 + 3 * S3
PP4 = DD ** 2 * x1 ** 4 - 4 * DD * x1 ** 2 * S2 + 2 * S2 ** 2 + 4 * DD * x1 * S3 - 4 * dd * S4
assert PP2 == DD * pp2 and PP3 == DD * pp3 and PP4 == DD ** 2 * pp4
hdet = 5 * pp2 * pp4 - 5 * pp3 ** 2 - x1 ** 2 * pp4 + 2 * x1 * pp2 * pp3 - pp2 ** 3
HH = 5 * PP2 * PP4 - 5 * DD * PP3 ** 2 - x1 ** 2 * DD * PP4 + 2 * x1 * DD * PP2 * PP3 - PP2 ** 3
assert HH == DD ** 3 * hdet, 'H = (9d)^3 * Hankel determinant'
assert 9 * S3 ** 2 - 2 * S2 * S4 == 9 * DD ** 2 * (e3 ** 2 - 2 * e2 * e4), 'N = 9(9d)^2 (s3^2 - 2 s2 s4)'
# Newton identities, 3x3 Hankel determinant expansion and Cauchy-Binet for u1..u5
u = [MP.var(5, i) for i in range(5)]
def esym(k):
    tot = MP.const(5, 0)
    for c in combinations(range(5), k):
        t = MP.const(5, 1)
        for i in c: t = t * u[i]
        tot = tot + t
    return tot
E = [MP.const(5, 1)] + [esym(k) for k in range(1, 6)]
def psum(k):
    tot = MP.const(5, 0)
    for i in range(5): tot = tot + u[i] ** k
    return tot
Pw = [MP.const(5, 5)] + [psum(k) for k in range(1, 5)]
assert Pw[2] == E[1] ** 2 - 2 * E[2]
assert Pw[3] == E[1] ** 3 - 3 * E[1] * E[2] + 3 * E[3]
assert Pw[4] == E[1] ** 4 - 4 * E[1] ** 2 * E[2] + 2 * E[2] ** 2 + 4 * E[1] * E[3] - 4 * E[4]
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
hank = det3([[Pw[0], Pw[1], Pw[2]], [Pw[1], Pw[2], Pw[3]], [Pw[2], Pw[3], Pw[4]]])
assert hank == 5 * Pw[2] * Pw[4] - 5 * Pw[3] ** 2 - Pw[1] ** 2 * Pw[4] + 2 * Pw[1] * Pw[2] * Pw[3] - Pw[2] ** 3
cb = MP.const(5, 0)
for i, j, k in combinations(range(5), 3):
    vdm = (u[j] - u[i]) * (u[k] - u[i]) * (u[k] - u[j])
    cb = cb + vdm * vdm
assert hank == cb, 'Hankel det = sum over triples of squared Vandermonde'
# Newton inequality normalisation for n=5,k=3: e3^2 >= e2 e4 with e_k = s_k/C(5,k) <=> s3^2 >= 2 s2 s4
assert Fr(1, 10) ** 2 * 100 == 1 and Fr(1, 10) * Fr(1, 5) * 100 == 2
# exact random sanity (the rigorous strictness argument is in the review text)
rng = random.Random(20261028)
newton_ok = True; hank_rank_ok = True; trials = 0
for trial in range(400):
    kdist = rng.choice([2, 3, 4, 5])
    vals = [Fr(rng.randint(1, 60), rng.randint(1, 30)) for _ in range(kdist)]
    while len(set(vals)) < kdist:
        vals = [Fr(rng.randint(1, 60), rng.randint(1, 30)) for _ in range(kdist)]
    pt = [rng.choice(vals) for _ in range(5)]
    for i in range(kdist): pt[i] = vals[i]
    rng.shuffle(pt); pt = tuple(pt); trials += 1
    newton_ok &= (E[3].ev(pt) ** 2 - 2 * E[2].ev(pt) * E[4].ev(pt)) > 0
    hv = hank.ev(pt)
    hank_rank_ok &= (hv > 0) if len(set(pt)) >= 3 else (hv == 0)
assert newton_ok and hank_rank_ok
pt = (Fr(3),) * 5
assert E[3].ev(pt) ** 2 - 2 * E[2].ev(pt) * E[4].ev(pt) == 0 and hank.ev(pt) == 0

C = json.loads(CERT.read_text())
def parse2(txt):
    def walk(n):
        if isinstance(n, ast.Constant) and isinstance(n.value, int):
            return MP.const(2, n.value)
        if isinstance(n, ast.Name):
            return {'s': S, 'v': W}[n.id]
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -walk(n.operand)
        if isinstance(n, ast.BinOp):
            if isinstance(n.op, ast.Pow):
                assert isinstance(n.right, ast.Constant) and isinstance(n.right.value, int) and n.right.value >= 0
                return walk(n.left) ** n.right.value
            a, b = walk(n.left), walk(n.right)
            if isinstance(n.op, ast.Add): return a + b
            if isinstance(n.op, ast.Sub): return a - b
            if isinstance(n.op, ast.Mult): return a * b
        raise ValueError(ast.dump(n))
    return walk(ast.parse(txt, mode='eval').body)
cert_polys = [parse2(t) for t in C['polynomials']]
assert len(cert_polys) == 6 and all(a == b for a, b in zip(cert_polys, polys)), 'certificate polynomial strings'
R['parts']['B_polynomials'] = {
    'degrees_(s,V)': degs, 'certificate_polynomial_strings_match_reconstruction': True,
    'H_equals_(9d)^3_times_Hankel_det': True, 'N_equals_9(9d)^2(s3^2-2s2s4)': True,
    'Newton_identities_p2_p3_p4_verified_symbolically_n=5': True,
    'Hankel_det_equals_sum_of_squared_3x3_Vandermondes_(Cauchy-Binet)_verified_symbolically': True,
    'random_exact_sanity_trials': trials,
}
print('B: six polynomials match certificate; Hankel/Newton identities verified symbolically')

# ================================================================= PART C
def as_s_poly(P):
    """MP(2) -> list over s-power of Q[V] coefficient lists."""
    out = []
    for i in range(P.deg(0) + 1):
        ci = P.coeff(0, i)
        out.append(utrim([ci.c.get((0, j), Fr(0)) for j in range(max(ci.deg(1), 0) + 1)]))
    return out
spolys = [as_s_poly(P) for P in polys]
project = []
for lab, sp in zip(labels, spolys):
    project.append((lab + ':lead', sp[-1]))
    if len(sp) - 1 > 1:
        project.append((lab + ':disc', discriminant_s(sp)))
for i, j in combinations(range(6), 2):
    project.append((labels[i] + ':' + labels[j], resultant_s(spolys[i], spolys[j])))
assert len(project) == 23 and all(not uiszero(P) for _, P in project)
def uni_from_mp(P):
    assert P.deg(0) <= 0
    return utrim([P.c.get((0, j), Fr(0)) for j in range(P.deg(1) + 1)])
factors = [uni_from_mp(parse2(r['polynomial'])) for r in C['projection_factor_records']]
assert len(factors) == 17 and all(udeg(f) >= 1 for f in factors)
assert len({tuple(f) for f in factors}) == 17, 'factors pairwise distinct'
assert all(f == uprimitive(f) for f in factors), 'factors primitive with positive lc'
recs = C['projection_records']; assert len(recs) == 23
assert [n for n, _ in project] == [r['name'] for r in recs], 'projection naming/order'
proj_degrees = {}
factor_use = [0] * 17
for (name, P), rec in zip(project, recs):
    prodp = [Fr(rec['scale'])]
    for idx, m in rec['factors']:
        for _ in range(m):
            prodp = umul(prodp, factors[idx])
        factor_use[idx] += 1
    assert utrim(P) == prodp, 'projection factorization identity fails for ' + name
    assert udeg(P) == rec['degree']
    proj_degrees[name] = udeg(P)
assert all(factor_use), 'every listed factor is used'
R['parts']['C_projection'] = {
    'projection_polynomials': 23, 'all_nonzero': True, 'degrees_in_V': proj_degrees,
    'max_degree': max(proj_degrees.values()),
    'exact_identity_scale*prod(factor^mult)_for_all_23': True,
    'distinct_factors': 17, 'factor_degrees': [udeg(f) for f in factors],
    'own_Bareiss_Sylvester_resultants': True,
}
print('C: 23 projection polynomials recomputed (own Bareiss); all 23 factorization identities exact; 17 factors')

# ================================================================= PART D
own_roots = []      # (lo, hi, factor_index) from my own isolation
cert_roots = []
fseq = []
for i, f in enumerate(factors):
    if f == [Fr(0), Fr(1)]:        # the factor 'v': only root 0, not positive
        fseq.append(None)
        assert C['projection_factor_records'][i]['positive_root_intervals'] == []
        continue
    assert ueval(f, Fr(0)) != 0
    iso, seq = isolate_above(f, Fr(0))
    fseq.append(seq)
    npos = nroots(seq, Fr(0), None)
    assert npos == len(iso)
    for a, b in iso:
        own_roots.append((a, b, i))
    ivs = C['projection_factor_records'][i]['positive_root_intervals']
    assert len(ivs) == npos, (i, npos, len(ivs))
    for a, b in ivs:
        a, b = Fr(a), Fr(b)
        assert 0 < a < b and ueval(f, a) != 0 and ueval(f, b) != 0 and nroots(seq, a, b) == 1
        cert_roots.append((a, b, i))
assert len(own_roots) == 25 and len(cert_roots) == 25
cert_roots.sort()
assert all(cert_roots[k][1] < cert_roots[k + 1][0] for k in range(24)), 'certificate isolators disjoint'
given = [(Fr(a), Fr(b), i) for a, b, i in C['ordered_positive_projection_roots']]
assert given == cert_roots, 'ordered root table consistent with factor tables'
changed = True
while changed:
    changed = False
    own_roots.sort()
    for k in range(24):
        a1, b1, i1 = own_roots[k]; a2, b2, i2 = own_roots[k + 1]
        if not b1 < a2:
            own_roots[k] = refine(factors[i1], fseq[i1], a1, b1) + (i1,)
            own_roots[k + 1] = refine(factors[i2], fseq[i2], a2, b2) + (i2,)
            changed = True
for k in range(25):
    (a, b, i), (c, e, j) = own_roots[k], cert_roots[k]
    assert i == j and max(a, c) < min(b, e), 'root order disagreement at %d' % k
R['parts']['D_projection_roots'] = {
    'positive_roots_total_own_Sturm': 25, 'own_isolators_disjoint_and_aligned_with_certificate': True,
    'certificate_isolators_each_contain_exactly_one_root': True,
    'roots_per_factor': [sum(1 for r in own_roots if r[2] == i) for i in range(17)],
    'own_isolators_sorted': [[str(a), str(b), i] for a, b, i in own_roots],
    'base_intervals': 26,
}
print('D: 25 positive projection roots (own Sturm), isolators verified, 26 base intervals')

# ================================================================= PART E
def specialize(P, vv):
    return utrim([P.coeff(0, i).ev((Fr(0), vv)) for i in range(P.deg(0) + 1)])
def census_at(vv, record=None):
    """full own census at base point vv; returns (cells, roots). cells: (lo,hi,sample,negatives)."""
    for f in factors:
        assert ueval(f, vv) != 0, 'sample hits a projection root'
    ps = [specialize(P, vv) for P in polys]
    assert [udeg(x) for x in ps] == [1, 1, 1, 1, 2, 4], 'degree drop at sample'
    roots = []; seqs = {}
    for j in range(1, 6):
        assert ueval(ps[j], Fr(4)) != 0
        iso, seq = isolate_above(ps[j], Fr(4)); seqs[j] = seq
        for a, b in iso: roots.append((a, b, j))
        if record is not None:
            listed = [(Fr(a), Fr(b)) for a, b, jj in record['s_roots'] if jj == j]
            assert len(listed) == len(iso), ('section root count', vv, j)
            for a, b in listed:
                assert 4 < a < b and ueval(ps[j], a) != 0 and ueval(ps[j], b) != 0 and nroots(seq, a, b) == 1
    changed = True
    while changed:
        changed = False; roots.sort()
        for k in range(len(roots) - 1):
            a1, b1, j1 = roots[k]; a2, b2, j2 = roots[k + 1]
            if not b1 < a2:
                roots[k] = refine(ps[j1], seqs[j1], a1, b1) + (j1,)
                roots[k + 1] = refine(ps[j2], seqs[j2], a2, b2) + (j2,)
                changed = True
    cells = []
    for k in range(len(roots) + 1):
        lo = Fr(4) if k == 0 else roots[k - 1][1]
        hi = None if k == len(roots) else roots[k][0]
        ss = (lo + 1) if hi is None else (lo + hi) / 2
        vals = [ueval(x, ss) for x in ps]
        assert all(x != 0 for x in vals)
        neg = [i for i, x in enumerate(vals) if x < 0]
        assert neg, ('feasible cell found', vv, ss)
        cells.append((str(lo), 'inf' if hi is None else str(hi), str(ss), neg))
    if record is not None:
        sm = record['samples']; assert len(sm) == len(roots) + 1
        listed = sorted((Fr(a), Fr(b), jj) for a, b, jj in record['s_roots'])
        for k, entry in enumerate(sm):
            ss = Fr(entry['s'])
            lo = Fr(4) if k == 0 else listed[k - 1][1]
            hi = None if k == len(listed) else listed[k][0]
            assert ss > lo and (hi is None or ss < hi)
            vals = [ueval(x, ss) for x in ps]
            assert all(x != 0 for x in vals) and vals[int(entry['negative_constraint_index'])] < 0
    return cells, [(str(a), str(b), j) for a, b, j in roots]

sections = C['sections']; assert len(sections) == 26
cert_cells = 0; own_cells = 0
per_section = []; neg_histogram = {}; only_newton = []; only_hankel = []
for k in range(26):
    lo = Fr(0) if k == 0 else cert_roots[k - 1][1]
    hi = None if k == 25 else cert_roots[k][0]
    vc = Fr(sections[k]['v'])
    assert vc > lo and (hi is None or vc < hi), 'certificate sample V outside base interval'
    cells_c, roots_c = census_at(vc, sections[k])
    cert_cells += len(cells_c)
    # reviewer-chosen second sample in the same base interval, distinct from the author's
    if k == 0:
        vo = hi / 3
    elif hi is None:
        vo = lo + 2
    else:
        vo = lo + (hi - lo) / 3
    assert vo > lo and (hi is None or vo < hi) and vo != vc
    cells_o, roots_o = census_at(vo)
    own_cells += len(cells_o)
    assert len(cells_o) == len(cells_c), 'cell count differs between two samples of one base interval'
    assert [c[3] for c in cells_o] == [c[3] for c in cells_c], 'negative sets differ within base interval'
    assert [r[2] for r in roots_o] == [r[2] for r in roots_c], 'root-curve order differs within base interval'
    for c in cells_o:
        key = ','.join(labels[i] for i in c[3]); neg_histogram[key] = neg_histogram.get(key, 0) + 1
        if c[3] == [4]: only_newton.append((k, c[0], c[1]))
        if c[3] == [5]: only_hankel.append((k, c[0], c[1]))
    per_section.append({'base_interval': k, 'V_lo': str(lo), 'V_hi': 'inf' if hi is None else str(hi),
                        'V_cert_sample': str(vc), 'V_own_sample': str(vo),
                        's_root_curve_order_above_4': [r[2] for r in roots_o],
                        's_roots_above_4_own_sample': roots_o, 'cells_own_sample': cells_o})
assert cert_cells == 82 and own_cells == 82
R['parts']['E_sections'] = {
    'base_intervals': 26, 'cells_at_certificate_samples': cert_cells, 'cells_at_reviewer_samples': own_cells,
    'every_cell_has_a_strictly_negative_constraint': True,
    'certificate_recorded_s_roots_samples_and_negative_indices_all_verified': True,
    'negative_constraint_set_histogram': neg_histogram,
    'cells_where_only_newton3_negative': only_newton, 'cells_where_only_hankel3_negative': only_hankel,
    'sections': per_section,
}
print('E: 26 sections x 2 samples; 82 cells each; negative-set histogram', neg_histogram)
print('   cells with ONLY newton3 negative: %d ; ONLY hankel3 negative: %d' % (len(only_newton), len(only_hankel)))

R['elapsed_seconds'] = round(time.monotonic() - T0, 2)
R['replay_result'] = ('PASS: elimination, six polynomials, 23 projections (own Bareiss), 17-factor identities, '
                      '25 positive roots (own Sturm), 26 base intervals, 82 strict-sign cells at two independent '
                      'base samples per interval; no feasible open cell')
with open(OUT, 'x') as fh:
    json.dump(R, fh, indent=1); fh.write('\n')
print('receipt:', OUT, 'elapsed', R['elapsed_seconds'], 's')

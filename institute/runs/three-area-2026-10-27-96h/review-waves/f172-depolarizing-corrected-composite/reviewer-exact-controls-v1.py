#!/usr/bin/env python3
"""f172 reviewer-authored exact controls (ReviewF172DepolFresh).

Independently written; imports no author code and reads no author files.
Standard library only; every check uses exact Fraction / Gaussian-rational
arithmetic.  Instance checks and univariate polynomial identities checked at
more points than their degree; multivariate statements are instance checks
only and are NOT proofs of universal claims.

Kinds: "positive" = a claimed identity/inequality is expected to hold;
"negative" = a deliberate mutation is expected to be DETECTED (fail) for the
stated intended reason.  expected_outcome_observed=True means the expected
outcome occurred.  Exit status 0 iff every check observed its expected outcome.
"""
import itertools
import json
import sys
from fractions import Fraction as Fr

RESULTS = []


def record(cid, kind, claim, ok, detail=""):
    RESULTS.append({"id": cid, "kind": kind, "claim": claim,
                    "expected_outcome_observed": bool(ok), "detail": str(detail)})


# ----------------------------------------------------------------- Gaussian rationals
class G:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = g(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = g(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        o = g(o)
        return G(o.re - self.re, o.im - self.im)

    def __mul__(self, o):
        o = g(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __neg__(self):
        return G(-self.re, -self.im)

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def __truediv__(self, o):
        o = g(o)
        d = o.abs2()
        n = self * o.conj()
        return G(n.re / d, n.im / d)

    def __eq__(self, o):
        o = g(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        return "(%s%+si)" % (self.re, self.im) if self.im != 0 else "%s" % self.re


def g(x):
    return x if isinstance(x, G) else G(x, 0)


I_ = G(0, 1)
Z0 = G(0)
ONE = G(1)

# ----------------------------------------------------------------- matrices
def zeros(n, m=None):
    m = n if m is None else m
    return [[Z0] * m for _ in range(n)]


def eye(n):
    return [[ONE if i == j else Z0 for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    c = g(c)
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        Ai = A[i]
        row = []
        for j in range(m):
            re = Fr(0)
            im = Fr(0)
            for l in range(k):
                a = Ai[l]
                if a.re == 0 and a.im == 0:
                    continue
                b = B[l][j]
                if b.re == 0 and b.im == 0:
                    continue
                re += a.re * b.re - a.im * b.im
                im += a.re * b.im + a.im * b.re
            row.append(G(re, im))
        out.append(row)
    return out


def dag(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def tr_(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def trace(A):
    s = G(0)
    for i in range(len(A)):
        s = s + A[i][i]
    return s


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def fro2(A):
    return sum((A[i][j].abs2() for i in range(len(A)) for j in range(len(A[0]))), Fr(0))


def is_herm(A):
    return meq(A, dag(A))


def comm(A, B):
    return msub(mmul(A, B), mmul(B, A))


def inverse(A):
    n = len(A)
    M = [list(A[i]) + [ONE if i == j else Z0 for j in range(n)] for i in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if not M[r][col].iszero())
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x / pv for x in M[col]]
        for r in range(n):
            if r != col and not M[r][col].iszero():
                f = M[r][col]
                M[r] = [M[r][j] - f * M[col][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def charpoly(A):
    """Faddeev-LeVerrier: returns c with det(xI-A)=sum_j c[j] x^j."""
    n = len(A)
    c = [None] * (n + 1)
    c[n] = ONE
    Mk = zeros(n)
    I = eye(n)
    for k in range(1, n + 1):
        Mk = madd(mmul(A, Mk), mscale(c[n - k + 1], I))
        t = trace(mmul(A, Mk))
        c[n - k] = G(-t.re / k, -t.im / k)
    return c


def inertia(A):
    """Exact (pos, neg, zero) for Hermitian A via real-rooted Descartes rule."""
    assert is_herm(A)
    c = charpoly(A)
    assert all(x.im == 0 for x in c)
    r = [x.re for x in c]
    n = len(A)
    z = 0
    while r[z] == 0:
        z += 1
    q = r[z:]

    def changes(seq):
        s = [x for x in seq if x != 0]
        return sum(1 for i in range(len(s) - 1) if (s[i] > 0) != (s[i + 1] > 0))

    pos = changes(q)
    neg = changes([q[j] * (-1) ** j for j in range(len(q))])
    assert pos + neg + z == n
    return pos, neg, z


# ----------------------------------------------------------------- four-qubit helpers
N = 16


def bit(x, i):
    return (x >> (3 - i)) & 1


def setbit(x, i, c):
    return (x & ~(1 << (3 - i))) | (c << (3 - i))


def wt(x):
    return bin(x).count("1")


def W(s):
    return int(s, 2)


E1 = [1 << (3 - i) for i in range(4)]          # weight-one word e_i (site i = 1)
BAR = [15 ^ (1 << (3 - i)) for i in range(4)]   # weight-three word missing site i
PAIRS = list(itertools.combinations(range(4), 2))


def pair_word(i, j):
    return (1 << (3 - i)) | (1 << (3 - j))


def E_site(i, X):
    """E_i(X) = I_i (x) Tr_i(X) / 2, factor order restored."""
    out = zeros(N)
    for x in range(N):
        for y in range(N):
            if bit(x, i) != bit(y, i):
                continue
            acc = X[setbit(x, i, 0)][setbit(y, i, 0)] + X[setbit(x, i, 1)][setbit(y, i, 1)]
            out[x][y] = G(acc.re / 2, acc.im / 2)
    return out


def Lam(p, X):
    """Phi_p^{(x)4}, Phi_p(X)=(1-p)X+(p/2)Tr(X)I, site by site (definition route)."""
    p = Fr(p)
    for i in range(4):
        Ei = E_site(i, X)
        X = [[(1 - p) * X[a][b] + p * Ei[a][b] for b in range(N)] for a in range(N)]
    return X


def marginal(i, X):
    m = [[Z0, Z0], [Z0, Z0]]
    for x in range(N):
        c = bit(x, i)
        for d in (0, 1):
            m[c][d] = m[c][d] + X[x][setbit(x, i, d)]
    return m


def embed(i, A2):
    out = zeros(N)
    mask = ~(1 << (3 - i)) & 15
    for x in range(N):
        for y in range(N):
            if (x & mask) == (y & mask):
                out[x][y] = g(A2[bit(x, i)][bit(y, i)])
    return out


def H1(X):
    out = zeros(N)
    for i in range(4):
        out = madd(out, embed(i, marginal(i, X)))
    return out


PX = [[Z0, ONE], [ONE, Z0]]
PY = [[Z0, -I_], [I_, Z0]]
PZ = [[ONE, Z0], [Z0, -ONE]]
P1 = [[ONE, Z0], [Z0, ONE]]
PAULI1 = [P1, PX, PY, PZ]


def kron4(mats):
    out = zeros(N)
    for x in range(N):
        for y in range(N):
            v = ONE
            for i in range(4):
                v = v * mats[i][bit(x, i)][bit(y, i)]
                if v.iszero():
                    break
            out[x][y] = v
    return out


Y4 = kron4([PY] * 4)
SITE_PAULI = [[embed(i, P) for P in (PX, PY, PZ)] for i in range(4)]


def Ffr(X):
    out = zeros(N)
    for i in range(4):
        for P in SITE_PAULI[i]:
            out = madd(out, mmul(mmul(P, X), P))
    return out


def tilde(X):
    return mmul(mmul(Y4, tr_(X)), Y4)


def T_layer(m, X):
    out = zeros(N)
    for A in itertools.combinations(range(4), m):
        Y = X
        for i in A:
            Y = E_site(i, Y)
        out = madd(out, Y)
    return out


def ket(x):
    v = [Z0] * N
    v[x] = ONE
    return v


def outer(u, v):
    return [[u[x] * v[y].conj() for y in range(N)] for x in range(N)]


def all_paulis():
    for s in itertools.product(range(4), repeat=4):
        yield s, sum(1 for k in s if k), kron4([PAULI1[k] for k in s])


def expval(X, P):
    """Tr(XP) using the sparsity of the Pauli/product matrix P."""
    re = Fr(0)
    im = Fr(0)
    for y in range(N):
        Py = P[y]
        for x in range(N):
            b = Py[x]
            if b.re == 0 and b.im == 0:
                continue
            a = X[x][y]
            re += a.re * b.re - a.im * b.im
            im += a.re * b.im + a.im * b.re
    return G(re, im)


def bloch(i, X):
    return [expval(X, SITE_PAULI[i][a]).re for a in range(3)]


def normalized_state(base):
    """Gaussian-integer list; append last amplitude so the norm^2 is a square."""
    s = sum((G(*z).abs2() for z in base), Fr(0))
    for r in range(0, 40):
        for a in range(-12, 13):
            for b in range(-12, 13):
                tot = s + a * a + b * b
                n = int(tot ** 0.5 + 0.5) if tot >= 0 else 0
                if n * n == tot and n > 0 and (a, b) != (0, 0):
                    amps = [G(*z) for z in base] + [G(a, b)]
                    return [G(z.re / n, z.im / n) for z in amps]
    raise RuntimeError("no square completion")


# ----------------------------------------------------------------- T1 univariate identities
def poly_identities():
    pts = [Fr(k, 13) for k in range(1, 12)]   # 11 distinct points > all degrees used (<= 8)
    ok1 = ok2 = ok3 = ok4 = ok5 = True
    mut = False
    for t in pts:
        a, b = (1 + t) / 2, (1 - t) / 2
        R3 = a ** 4 + 2 * a ** 3 * b
        ok1 &= 16 * R3 == 3 + 8 * t + 6 * t ** 2 - t ** 4
        p = 1 - t
        ref = sum(c * (1 - p) ** (4 - m) * p ** m
                  for m, c in enumerate([1, 3, 3, Fr(5, 4), Fr(3, 16)]))
        ok2 &= ref == R3
        d = [((1 + t) ** (4 - h) * (1 - t) ** h - 1) / t for h in range(5)]
        ok3 &= (d[0] - d[1] == 2 * (1 + t) ** 3) and (d[1] - d[2] == 2 * (1 + t) ** 2 * (1 - t))
        ok3 &= d == [4 + 6 * t + 4 * t ** 2 + t ** 3, 2 - 2 * t ** 2 - t ** 3, -2 * t + t ** 3,
                     -2 + 2 * t ** 2 - t ** 3, -4 + 6 * t - 4 * t ** 2 + t ** 3]
        D3 = 1 - a * b
        ok4 &= D3 == (3 + t ** 2) / 4
        lhs = -a * t * D3 + a * t ** 5 / D3 - 2 * a * a * b * t + t * t * b * b + t ** 5 * b / D3
        rhs = -t * (1 - t) * (15 + 24 * t + 38 * t ** 2 + 32 * t ** 3 + 3 * t ** 4) / (32 * D3)
        ok4 &= lhs == rhs
        rhs_mut = -t * (1 - t) * (15 + 24 * t + 37 * t ** 2 + 32 * t ** 3 + 3 * t ** 4) / (32 * D3)
        mut |= lhs != rhs_mut
        D4 = a * a + b * b
        ok5 &= D4 == (1 + t * t) / 2 and (-t * D4 + t ** 7 / D4 - 2 * a * b * t == -t + t ** 7 / D4)
    record("T1.R3", "positive", "(1) 16R3=3+8t+6t^2-t^4 (degree-4 identity, 11 points)", ok1)
    record("T1.layers", "positive", "sum_m (1-p)^(4-m)p^m (1,3,3,5/4,3/16) = R3 for p<=1", ok2)
    record("T1.gaps", "positive", "d_h closed forms; d0-d1=2(1+t)^3, d1-d2=2(1+t)^2(1-t)", ok3)
    record("T1.eq19", "positive", "(19) closed form equals -atD3+at^5/D3-2a^2bt+t^2b^2+t^5b/D3", ok4)
    record("T1.eq19.mut", "negative", "coefficient 38->37 in (19) is detected", mut,
           "intended reason: altered polynomial coefficient")
    record("T1.eq20", "positive", "(20) A4+K2(M4) = -t + t^7/D4 with D4=(1+t^2)/2", ok5)


# ----------------------------------------------------------------- T2 local rules + reference
def local_rules():
    t = Fr(1, 200)
    a, b = (1 + t) / 2, (1 - t) / 2
    ok = True
    mut = False
    for (c, d) in itertools.product((0, 1), repeat=2):
        X = zeros(N)
        X[c << 3][d << 3] = ONE        # site 1 matrix unit |c><d| (x) |000><000|
        Y = Lam(1 - t, X)
        # read the site-1 2x2 action on top of the site-2..4 |000><000| diag(a,b)^3 factor
        loc = [[Y[(u << 3)][(v << 3)] / (a ** 3) for v in (0, 1)] for u in (0, 1)]
        if c == d == 0:
            exp = [[g(a), Z0], [Z0, g(b)]]
        elif c == d == 1:
            exp = [[g(b), Z0], [Z0, g(a)]]
        elif (c, d) == (0, 1):
            exp = [[Z0, g(t)], [Z0, Z0]]
            mut |= not meq(loc, [[Z0, Z0], [g(t), Z0]])
        else:
            exp = [[Z0, Z0], [g(t), Z0]]
        ok &= meq(loc, exp)
    record("T2.units", "positive", "local rules |0><0|->diag(a,b), |1><1|->diag(b,a), |0><1|->t|0><1|", ok)
    record("T2.units.mut", "negative", "orientation mutation |0><1|->t|1><0| is detected", mut,
           "intended reason: wrong matrix-unit orientation")
    rho0 = outer(ket(0), ket(0))
    Q0 = zeros(N)
    for x in (W("0000"), W("1000"), W("0100")):
        Q0[x][x] = ONE
    layers = [trace(mmul(Q0, T_layer(m, rho0))) for m in range(5)]
    record("T2.refLayers", "positive", "product-reference layer traces (1,3,3,5/4,3/16)",
           layers == [g(1), g(3), g(3), g(Fr(5, 4)), g(Fr(3, 16))], layers)
    # erratum 127 witness at p=0
    Qe = zeros(N)
    for x in (W("0001"), W("0010"), W("0100")):
        Qe[x][x] = ONE
    val = trace(mmul(Qe, Lam(0, rho0)))
    record("T2.err127", "positive", "p=0, rho=|0000>, Q=span{0001,0010,0100}: Tr=0 < R3(0)=1 (strict)",
           val == g(0), val)
    val2 = trace(mmul(Q0, Lam(0, rho0)))
    record("T2.err127.eq", "positive", "p=0 equality for Q containing supp(rho)", val2 == g(1), val2)


# ----------------------------------------------------------------- shared complex objects
def make_state():
    base = [(3, 1), (1, -2), (0, 1), (2, 2), (-1, 1), (1, 0), (0, -2), (2, -1),
            (1, 1), (-2, 0), (1, 3), (0, 1), (1, -1), (2, 0), (-1, -1)]
    return normalized_state(base)


def make_projector():
    K = zeros(N)
    for x in range(N):
        K[x][x] = G(0, Fr((x % 3) - 1, 5))
        for y in range(x + 1, N):
            val = G(Fr(((x + 2 * y) % 5) - 2, 7), Fr(((3 * x + y) % 3) - 1, 7))
            K[x][y] = val
            K[y][x] = -val.conj()
    I = eye(N)
    U = mmul(msub(I, K), inverse(madd(I, K)))
    P3 = zeros(N)
    for x in range(3):
        P3[x][x] = ONE
    return U, mmul(mmul(U, P3), dag(U))


# ----------------------------------------------------------------- T3 spin flip / frame identities
def identities(psi):
    rho = outer(psi, psi)
    T1 = T_layer(1, rho)
    T2 = T_layer(2, rho)
    T3 = T_layer(3, rho)
    T4 = T_layer(4, rho)
    F = Ffr(rho)
    rt = tilde(rho)
    I = eye(N)
    record("T3.T1", "positive", "(4) T1 = rho + F(rho)/4 (complex pure input)",
           meq(T1, madd(rho, mscale(Fr(1, 4), F))))
    rhs = msub(madd(madd(madd(H1(rho), rho), rt), mscale(Fr(1, 2), F)), I)
    record("T3.T2", "positive", "(4) 4T2 = H1 + rho + tilde rho + F/2 - I", meq(mscale(4, T2), rhs))
    exp_ = madd(madd(msub(rho, mscale(2, T1)), mscale(4, T2)), msub(mscale(16, T4), mscale(8, T3)))
    record("T3.flip", "positive", "tilde rho = rho -2T1 +4T2 -8T3 +16T4 and 8T3=H1",
           meq(rt, exp_) and meq(mscale(8, T3), H1(rho)))
    rt_mut = mmul(mmul(Y4, rho), Y4)
    record("T3.flip.mut", "negative", "spin flip without transpose violates (4) for complex input",
           not meq(mscale(4, T2), msub(madd(madd(madd(H1(rho), rho), rt_mut), mscale(Fr(1, 2), F)), I)),
           "intended reason: phase-sensitive transpose omitted")
    sigma = rt
    M = msub(H1(sigma), sigma)
    record("T3.eq7", "positive", "(7) H1(rho)+tilde rho = 4I - M(sigma)",
           meq(madd(H1(rho), rt), msub(mscale(4, I), M)))
    pos, neg, z = inertia(msub(M, sigma))
    record("T3.Mgeq", "positive", "M(sigma) - sigma >= 0 (pure complex sigma), exact inertia",
           neg == 0, (pos, neg, z))
    # frame moment
    S = sum((sum(c * c for c in bloch(i, rho)) for i in range(4)), Fr(0))
    yb = [y.conj() for y in psi]
    Y4psibar = [sum((Y4[x][y] * yb[y] for y in range(N)), G(0)) for x in range(N)]
    ov = sum((psi[x].conj() * Y4psibar[x] for x in range(N)), G(0))
    C = ov.abs2()
    A = [Fr(0)] * 5
    for s, w, P in all_paulis():
        e = expval(rho, P)
        assert e.im == 0
        A[w] += e.re * e.re
    ok = (A[0] == 1 and A[1] == S and A[3] == 12 + S - 2 * A[2] and A[4] == 3 - 2 * S + A[2]
          and 16 * C == 1 - S + A[2] - A[3] + A[4] and A[2] == 2 + S + 4 * C)
    record("T3.moments", "positive", "A3=12+S-2A2, A4=3-2S+A2, 16C=sum(-1)^jA_j, A2=2+S+4C", ok,
           {"S": str(S), "C": str(C)})
    trF2 = trace(mmul(F, F))
    record("T3.eq11", "positive", "(11) Tr F^2 = 16+4S+8C and Tr F = 12", trF2 == g(16 + 4 * S + 8 * C)
           and trace(F) == g(12), trF2)
    return rho


# ----------------------------------------------------------------- T4 reflection (6)
def reflection(rho, Q):
    ok = True
    mut1 = mut2 = True
    for p in (Fr(201, 200), Fr(4, 3), Fr(7, 6)):
        pp = 2 - p
        L = Lam(p, rho)
        Lp = Lam(pp, rho)
        ok &= meq(L, mmul(mmul(Y4, tr_(Lp)), Y4))
        Qr = mmul(mmul(Y4, tr_(Q)), Y4)
        ok &= meq(mmul(Qr, Qr), Qr) and trace(Qr) == g(3) and is_herm(Qr)
        ok &= trace(mmul(Q, L)) == trace(mmul(Qr, Lp))
        ok &= abs(1 - p) == abs(1 - pp)
        Qm = mmul(mmul(Y4, Q), Y4)
        mut1 &= trace(mmul(Q, L)) != trace(mmul(Qm, Lp))
        mut2 &= not meq(L, mmul(mmul(Y4, Lp), Y4))
    record("T4.refl", "positive",
           "(6) Lam_p = Y^4 Lam_{2-p}(.)^T Y^4 and Tr[Q Lam_p rho]=Tr[Y^4 Q^T Y^4 Lam_{2-p} rho]; t preserved",
           ok, "p in {201/200, 7/6, 4/3}")
    record("T4.refl.mutQ", "negative", "projector map without transpose is detected (complex Q)", mut1,
           "intended reason: actual complex projector requires Q^T")
    record("T4.refl.mutL", "negative", "output map without transpose is detected (complex rho)", mut2,
           "intended reason: transpose needed")
    tmax = Fr(1, 200)
    ok_int = (abs(1 - Fr(201, 200)) <= tmax and abs(1 - (2 - Fr(201, 200))) <= tmax
              and abs(1 - Fr(4, 3)) > tmax and abs(1 - Fr(202, 200)) > tmax)
    record("T4.interval", "positive",
           "reflection maps t->t: all-density antecedent t<=1/200 covers only 199/200<=p<=201/200; p=4/3 has t=1/3",
           ok_int)
    par = sum(trace(mmul(Q, P)).re ** 2 for s, w, P in all_paulis() if w > 0)
    record("T4.parseval", "positive", "sum_{P!=I} Tr(QP)^2 = 16TrQ^2-(TrQ)^2 = 39 (complex Q)", par == 39, par)


# ----------------------------------------------------------------- T5/T6 Hessian blocks
def blocks_A_M(v, t):
    a, b = (1 + t) / 2, (1 - t) / 2
    lam = [a ** (4 - h) * b ** h for h in range(5)]
    e0 = ket(0)
    V = Lam(1 - t, madd(outer(v, e0), outer(e0, v)))
    Wm = Lam(1 - t, msub(outer(v, v), outer(e0, e0)))
    A = Wm[0][0]
    for k in range(N):
        if wt(k) >= 2:
            A = A + G(V[k][0].abs2() / (lam[0] - lam[wt(k)]))
    M = [[Wm[E1[i]][E1[j]] for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            for k in range(N):
                if wt(k) >= 2:
                    M[i][j] = M[i][j] + V[E1[i]][k] * V[k][E1[j]] / (lam[1] - lam[wt(k)])
    return V, Wm, A, M


def closed_parts(v, t, orient="conj", gamma="TTdag"):
    a, b = (1 + t) / 2, (1 - t) / 2
    D3 = 1 - a * b
    D4 = a * a + b * b
    c = {(i, j): v[pair_word(i, j)] for (i, j) in PAIRS}
    T = [[Z0] * 4 for _ in range(4)]
    for (i, j), val in c.items():
        T[i][j] = val
        T[j][i] = val
    Gam = mmul(T, dag(T)) if gamma == "TTdag" else mmul(dag(T), T)
    w2 = sum((val.abs2() for val in c.values()), Fr(0))
    gv = [v[BAR[i]] for i in range(4)]
    w3 = sum((z.abs2() for z in gv), Fr(0))
    u4 = v[15]
    w4 = u4.abs2()
    A = (-a * a * t * (1 - t * t)) * w2 + (-a * t * D3 + a * t ** 5 / D3) * w3 + (-t * D4 + t ** 7 / D4) * w4
    M = [[Z0] * 4 for _ in range(4)]
    c3 = t * t * b * b + t ** 5 * b / D3
    for i in range(4):
        for j in range(4):
            val = Z0
            if i == j:
                val = val + G(-a * b * t * (1 - t * t)) * (G(w2) - Gam[i][i])
                val = val + G(-a * a * b * t * w3 - b * b * t * (1 + t) * gv[i].abs2())
                val = val + G(-a * b * t * w4)
            else:
                val = val + G(a * b * t * t * (1 + t)) * Gam[i][j]
            rk1 = gv[i].conj() * gv[j] if orient == "conj" else gv[i] * gv[j].conj()
            val = val + G(c3) * rk1
            M[i][j] = val
    return G(A), M, Gam


def hessian_checks():
    results = {}
    for t in (Fr(1, 200), Fr(2, 7)):
        tag = "t=%s" % t
        a, b = (1 + t) / 2, (1 - t) / 2
        # weight three, complex phases, normalized: g=(2+i,1+2i,-2+i,1+3i)/5
        g3 = [G(2, 1), G(1, 2), G(-2, 1), G(1, 3)]
        v = [Z0] * N
        for i in range(4):
            v[BAR[i]] = G(g3[i].re / 5, g3[i].im / 5)
        V, Wm, A, M = blocks_A_M(v, t)
        Ac, Mc, _ = closed_parts(v, t)
        record("T5.w3.%s" % tag, "positive", "(18) A3,M3 closed form with conj(g)conj(g)^dagger", A == Ac and meq(M, Mc))
        _, Mm, _ = closed_parts(v, t, orient="plain")
        record("T5.w3.mut.%s" % tag, "negative", "(18) with g g^dagger orientation is detected", not meq(M, Mm),
               "intended reason: complex conjugation orientation in the rank-one term")
        ok_ent = all(V[E1[i]][15] == G(b * t ** 3) * v[BAR[i]].conj() and
                     V[15][E1[i]] == G(b * t ** 3) * v[BAR[i]] and
                     V[BAR[i]][0] == G(a * t ** 3) * v[BAR[i]] for i in range(4))
        record("T5.w3.entries.%s" % tag, "positive",
               "V_(i,1111)=bt^3 conj(g_i), V_(1111,i)=bt^3 g_i, V_(bar i,0)=at^3 g_i (erratum 133)", ok_ent)
        mut_ent = any(V[E1[i]][15] != G(b * t ** 3) * v[BAR[i]] for i in range(4))
        record("T5.w3.entries.mut.%s" % tag, "negative", "unconjugated V_(i,1111)=bt^3 g_i is detected", mut_ent,
               "intended reason: complex g_i non-real")
        # coupling selection: weight-three direction couples weight one only to virtual weight four
        sel = all(V[E1[i]][k].iszero() for i in range(4) for k in range(N) if wt(k) != 4)
        record("T5.w3.select.%s" % tag, "positive", "weight-3 direction couples weight-one block only to weight 4", sel)
        # weight two, complex normalized
        cw = {(0, 1): G(1, 2), (0, 2): G(2, -1), (0, 3): G(0, 1), (1, 2): G(-1, 1), (1, 3): G(1, 0), (2, 3): G(0, -3)}
        s = sum((z.abs2() for z in cw.values()), Fr(0))   # 5+5+1+2+1+9 = 23 -> rescale via square search
        assert s == 23
        # complete to a square norm with the (2,3) entry adjusted: use (0,-3)->(1,-4): 5+5+1+2+1+17=31 no; search
        found = None
        for ar in range(-6, 7):
            for ai in range(-6, 7):
                tot = 14 + ar * ar + ai * ai
                n = int(tot ** 0.5 + 0.5)
                if n * n == tot and (ar, ai) != (0, 0) and ai != 0:
                    found = (ar, ai, n)
                    break
            if found:
                break
        ar, ai, n = found
        cw[(2, 3)] = G(ar, ai)
        v = [Z0] * N
        for (i, j), z in cw.items():
            v[pair_word(i, j)] = G(z.re / n, z.im / n)
        V, Wm, A, M = blocks_A_M(v, t)
        Ac, Mc, Gam = closed_parts(v, t)
        record("T5.w2.%s" % tag, "positive", "(17) A2, M2 closed form with Gamma=TT^dagger", A == Ac and meq(M, Mc),
               "c_23=(%d%+di)/%d" % (ar, ai, n))
        _, Mm, Gm = closed_parts(v, t, gamma="TdagT")
        record("T5.w2.mut.%s" % tag, "negative", "Gamma replaced by T^dagger T (=conj Gamma) is detected",
               (not meq(M, Mm)) and not meq(Gam, Gm), "intended reason: Gamma non-real for complex c")
        if t == Fr(1, 200):
            Kmat = [[G(t) * Gam[i][j] + (G((1 - 2 * t)) * Gam[i][i] if i == j else Z0) for j in range(4)] for i in range(4)]
            pos, neg, z = inertia(Kmat)
            record("T5.w2.K", "positive", "K=t Gamma+(1-2t)diag(n) >= 0 and Tr K = 2(1-t)",
                   neg == 0 and trace(Kmat) == g(2 * (1 - t)), (pos, neg, z))
        # weight four with a phase
        v = [Z0] * N
        v[15] = G(Fr(3, 5), Fr(4, 5))
        V, Wm, A, M = blocks_A_M(v, t)
        Ac, Mc, _ = closed_parts(v, t)
        record("T5.w4.%s" % tag, "positive", "(20) A4=-tD4+t^7/D4, M4=-abtI", A == Ac and meq(M, Mc))
    return results


def mixed_vector():
    amps = {W("1100"): (1, 2), W("1010"): (2, -1), W("0011"): (0, 3), W("1001"): (1, 1),
            W("0111"): (1, 1), W("1101"): (2, 3), W("1111"): (2, -3)}
    tot = sum(a * a + b * b for a, b in amps.values())
    assert tot == 49
    v = [Z0] * N
    for x, (a, b) in amps.items():
        v[x] = G(Fr(a, 7), Fr(b, 7))
    return v


def mixed_checks(v):
    for t in (Fr(1, 200), Fr(2, 7)):
        V, Wm, A, M = blocks_A_M(v, t)
        Ac, Mc, _ = closed_parts(v, t)
        record("T6.mixed.t=%s" % t, "positive",
               "mixed weights 2,3,4: cross-weight terms vanish, A=sum A_h, M=sum M_h (exact)", A == Ac and meq(M, Mc))
        _, Mm, _ = closed_parts(v, t, orient="plain")
        record("T6.mixed.mut.t=%s" % t, "negative", "mixed sum with g g^dagger orientation is detected",
               not meq(M, Mm), "intended reason: phase orientation")
        blk = all(V[x][y].iszero() for x in range(N) for y in range(N) if wt(x) <= 1 and wt(y) <= 1)
        record("T6.Vblocks.t=%s" % t, "positive", "V vanishes on weight-0/1 x weight-0/1 blocks", blk)


# ----------------------------------------------------------------- T7 normalized block conjugation
def block_of(x):
    return 0 if wt(x) == 0 else (1 if wt(x) == 1 else 2)


def conjugation_checks(v):
    t = Fr(1, 200)
    e0 = ket(0)

    def Ht(X):
        L = Lam(1 - t, X)
        trX = trace(X)
        return [[(G(16) * L[i][j] - (trX if i == j else Z0)) / t for j in range(N)] for i in range(N)]

    D = Ht(outer(e0, e0))
    VH = Ht(madd(outer(v, e0), outer(e0, v)))
    WH = Ht(msub(outer(v, v), outer(e0, e0)))
    V, Wm, A, M = blocks_A_M(v, t)
    a, b = (1 + t) / 2, (1 - t) / 2
    dh = [((1 + t) ** (4 - h) * (1 - t) ** h - 1) / t for h in range(5)]
    diag_ok = all(D[x][y] == (g(dh[wt(x)]) if x == y else Z0) for x in range(N) for y in range(N))
    record("T7.D", "positive", "D=H_t(|0><0|) diagonal with d_h", diag_ok)
    record("T7.rescale", "positive", "V_H=16V/t and W_H=16W/t (traceless)",
           meq(VH, mscale(Fr(16) / t, V)) and meq(WH, mscale(Fr(16) / t, Wm)))
    S1 = zeros(N)
    Voff = zeros(N)
    for x in range(N):
        for y in range(N):
            if block_of(x) != block_of(y):
                S1[x][y] = -VH[x][y] / (D[x][x] - D[y][y])
                Voff[x][y] = VH[x][y]
    record("T7.S1", "positive", "S1 anti-Hermitian, zero within blocks, V_off+[D,S1]=0",
           meq(dag(S1), mscale(-1, S1)) and meq(madd(Voff, comm(D, S1)), zeros(N)))
    B = madd(comm(VH, S1), mscale(Fr(1, 2), comm(comm(D, S1), S1)))
    Qs = madd(WH, B)
    q00 = Qs[0][0] == G(16 / t) * A
    q11 = all(Qs[E1[i]][E1[j]] == G(16 / t) * M[i][j] for i in range(4) for j in range(4))
    record("T7.Qblocks", "positive", "Q_00=(16/t)A and Q_(wt1,wt1)=(16/t)M exactly (bridge 7->8)", q00 and q11)
    Bm = comm(VH, S1)
    Qm = madd(WH, Bm)
    record("T7.Qblocks.mut", "negative", "dropping (1/2)[[D,S1],S1] breaks Q_00=(16/t)A",
           Qm[0][0] != G(16 / t) * A, "intended reason: second-order Schrieffer-Wolff term omitted")
    n_VH = fro2(VH)
    n_S1 = fro2(S1)
    n_B = fro2(B)
    # W0 and transverse part
    rv = [bloch(i, outer(v, v)) for i in range(4)]
    W0 = zeros(N)
    Gt = zeros(N)
    for i in range(4):
        W0 = madd(W0, madd(madd(mscale(rv[i][0], SITE_PAULI[i][0]), mscale(rv[i][1], SITE_PAULI[i][1])),
                           mscale(rv[i][2] - 1, SITE_PAULI[i][2])))
        Gt = madd(Gt, madd(mscale(rv[i][0], SITE_PAULI[i][0]), mscale(rv[i][1], SITE_PAULI[i][1])))
    dW = msub(WH, W0)
    wt1zero = all(expval(dW, SITE_PAULI[i][a]).iszero() for i in range(4) for a in range(3))
    ok_norms = (n_VH <= 512 * t * t < Fr(23, 200) ** 2 and n_S1 <= n_VH / 4 and n_S1 < Fr(23, 400) ** 2
                and n_B < Fr(47, 1000) ** 2 and fro2(dW) <= 512 * t * t and wt1zero)
    record("T7.norms", "positive",
           "instance: ||V_H||_F^2<=512t^2<(23/200)^2, ||S1||_F<=||V_H||_F/2<23/400, ||B||_F<47/1000, W_H-W0 has no wt-1 part",
           ok_norms, {"VH2": float(n_VH), "S12": float(n_S1), "B2": float(n_B), "dW2": float(fro2(dW))})
    offW0 = [[W0[x][y] if block_of(x) != block_of(y) else Z0 for y in range(N)] for x in range(N)]
    compG = [[Gt[x][y] if (wt(x) <= 2 and wt(y) <= 2) else Z0 for y in range(N)] for x in range(N)]
    record("T7.offW0", "positive", "off-block part of W0 equals compression of transverse G to weights<=2",
           meq(offW0, compG))
    # (22) with eta=9/41, sqrt(1-eta^2)=40/41
    eta = Fr(9, 41)
    h = eta * Fr(40, 41)
    psi = [G(Fr(40, 41)) * e0[x] + G(eta) * v[x] for x in range(N)]
    Hrho = Ht(outer(psi, psi))
    record("T7.eq22", "positive", "(22) H_t(rho)=D+hV_H+eta^2W_H at eta=9/41 (exact)",
           meq(Hrho, madd(madd(D, mscale(h, VH)), mscale(eta * eta, WH))))
    return {"VH_F2": str(n_VH), "S1_F2": str(n_S1), "B_F2": str(n_B)}


# ----------------------------------------------------------------- T8 constants and interval
def constants():
    t = Fr(1, 200)
    s1 = Fr(23, 400)
    c = Fr(103, 100) * (5 * (2 * s1) ** 3 / 6 + Fr(23, 200) * (2 * s1) ** 2 / 2 + Fr(163, 20) * (2 * s1))
    ok = c == Fr(580473701, 600000000) and c < 1
    x = 2 * Fr(9, 40) * s1
    ok &= 1 / (1 - x) < Fr(103, 100)          # exp(x) <= 1/(1-x) for 0<x<1
    ok &= Fr(9, 40) * Fr(23, 200) + Fr(9, 40) ** 2 * Fr(41, 5) == Fr(441, 1000)
    ok &= 2 - 2 * Fr(441, 1000) > Fr(11, 10)
    e = 3 * Fr(9, 40) + 3 * Fr(47, 1000) * Fr(9, 40) ** 2 + 3 * Fr(21, 5) ** 2 / Fr(11, 10) * Fr(9, 40) ** 2
    ok &= e == Fr(54870831, 17600000) and e < Fr(13, 4)
    ok &= Fr(15, 4) - Fr(13, 4) == Fr(1, 2)
    ok &= 8 + Fr(23, 200) < Fr(163, 20) and Fr(163, 20) + Fr(47, 1000) < Fr(41, 5)
    ok &= 4 + Fr(23, 200) + Fr(47, 1000) < Fr(21, 5)
    ok &= 2 * Fr(23, 200) * s1 + 2 * 5 * s1 * s1 < Fr(47, 1000)  # crude ||B||_F bound
    ok &= 3 * Fr(23, 200) * s1 < Fr(47, 1000)                      # reviewer bound
    a = (1 + t) / 2
    ok &= a * a * (1 - t * t) > Fr(15, 64) and Fr(15, 32) * (1 - t) > Fr(15, 64) and 1 - 2 * t ** 6 > Fr(15, 64)
    ok &= 512 * t * t < Fr(23, 200) ** 2
    ok &= 4 + 6 * t + 4 * t * t + t ** 3 < 5 and 4 - 6 * t + 4 * t * t - t ** 3 < 5
    ok &= (1 + t) ** 2 * (1 - t) >= 1
    ok &= 39 * 15 < 25 ** 2 and 20 * t <= Fr(1, 10) < Fr(81, 800) and 2 * Fr(9, 40) ** 2 == Fr(81, 800)
    record("T8.constants", "positive", "all displayed §7-§9 rational constants and interval inequalities at t<=1/200", ok,
           {"cubic": str(c), "err": str(e)})
    # monotone in t: each used inequality only gets easier as t decreases; endpoint suffices
    t2 = Fr(1, 196)
    record("T8.edge.VH", "negative", "Frobenius constant 23/200 fails at t=1/196 (antecedent t<=1/200 is used)",
           not (512 * t2 * t2 < Fr(23, 200) ** 2), "intended reason: interval endpoint")
    t3 = Fr(1, 190)
    record("T8.edge.far", "negative", "far-region margin 20t<81/800 fails at t=1/190", not (20 * t3 < Fr(81, 800)),
           "intended reason: tube/far boundary at eta=9/40 needs t<=1/200-scale noise")
    # far chain algebra: delta - sum(1-r_i) = 4-2r3-2r4 >= 0 on sorted samples
    okf = True
    for r in itertools.product([Fr(0), Fr(1, 3), Fr(3, 4), Fr(1)], repeat=4):
        r = sorted(r)
        L = r[0] + r[1] + 3 * r[2] + 3 * r[3]
        okf &= (8 - L) - sum(1 - x for x in r) == 4 - 2 * r[2] - 2 * r[3] >= 0
        # T3 top-three sum (12+L)/16 via all sign patterns
        vals = sorted((4 + sum(e * x for e, x in zip(sg, r)) for sg in itertools.product((1, -1), repeat=4)),
                      reverse=True)
        okf &= sum(vals[:3]) == 12 + L
    record("T8.farchain", "positive", "sum(1-r_i) <= delta and top-three of T3 = (12+L)/16 on a sorted grid", okf)


# ----------------------------------------------------------------- T9 spin-flip criterion (9)
def schur_criterion(phi, dvec, xstar):
    """dvec: diagonal of D (=H1 sigma); returns (crit_holds, W, q4, s) for criterion (9)."""
    s = dvec[xstar]
    q4 = phi[xstar].abs2()
    Wv = Fr(0)
    for x in range(len(phi)):
        if x == xstar:
            continue
        ax = dvec[x] - 1
        assert ax >= 0
        if ax > 0:
            Wv += phi[x].abs2() / ax
    return Wv <= 1 + q4 / (1 - s), Wv, q4, s


def spin_flip_checks():
    def state(amps):
        tot = sum((G(*z).abs2() for z in amps.values()), Fr(0))
        n = int(tot ** 0.5 + 0.5)
        assert n * n == tot
        v = [Z0] * N
        for x, z in amps.items():
            v[x] = G(Fr(z[0], n), Fr(z[1], n))
        return v

    cases = {
        # even-weight support => diagonal one-site marginals; majority |0>; norm^2 = 90+10 = 100
        "even": {W("0000"): (9, 3), W("1100"): (1, 1), W("0011"): (0, 1), W("1010"): (1, -1),
                 W("0101"): (0, 1), W("1111"): (1, 0), W("0110"): (1, 1), W("1001"): (0, 1)},
        # {0000} + weight three, equal moduli, phases 1,i,-1,-i => equal radii; norm^2 = 45+4 = 49
        "eq": {W("0000"): (6, 3), W("0111"): (1, 0), W("1011"): (0, 1), W("1101"): (-1, 0), W("1110"): (0, -1)},
        # {0000} + weight three with unequal moduli; norm^2 = 41+8 = 49
        "uneq": {W("0000"): (5, 4), W("0111"): (2, 1), W("1011"): (0, 1), W("1101"): (1, 1)},
    }
    for name, amps in cases.items():
        sig = state(amps)
        sigma = outer(sig, sig)
        marg = [marginal(i, sigma) for i in range(4)]
        diag_marg = all(m[0][1].iszero() for m in marg)
        pmin = [m[1][1].re for m in marg]
        s = sum(pmin, Fr(0))
        majority = all(p <= Fr(1, 2) for p in pmin) and 0 < s < 1
        Dm = H1(sigma)
        dvec = [Dm[x][x].re for x in range(N)]
        diagD = all(Dm[x][y].iszero() for x in range(N) for y in range(N) if x != y)
        ax_ok = all(dvec[x] - 1 == 3 - s - sum((1 - 2 * pmin[i]) for i in range(4) if bit(x, i)) for x in range(15))
        polygon = all(pmin[i] <= s - pmin[i] for i in range(4))
        crit, Wv, q4, s_ = schur_criterion(sig, dvec, 15)
        Mm = msub(Dm, sigma)
        pos, neg, z = inertia(msub(Mm, eye(N)))
        equiv = (crit == (neg <= 1))
        rho = tilde(sigma)                     # then tilde(rho) = sigma (involution)
        eq7 = meq(tilde(rho), sigma) and meq(madd(H1(rho), sigma), msub(mscale(4, eye(N)), Mm))
        record("T9.%s" % name, "positive",
               "diag marginals, a_x formula, polygon, (7), and (9) <=> lambda_2(M)>=1 (exact inertia of M-I)",
               diag_marg and majority and diagD and ax_ok and polygon and equiv and eq7,
               {"s": str(s), "W": str(Wv), "q4": str(q4), "crit": crit, "inertia(M-I)": (pos, neg, z)})
        if name == "eq":
            record("T9.eq.equality", "positive", "equal radii {0000}+wt3: W=1 equality, zero Schur eigenvalue allowed",
                   Wv == 1 + q4 / (1 - s_) and neg == 1 and z >= 1, (pos, neg, z))
    # abstract lemma instances (16-dim): violating and support-condition mutation
    dvec = [Fr(1) + Fr(k + 1, 10) for k in range(15)] + [Fr(1, 2)]
    dvec[3] = Fr(1) + Fr(1, 20)
    phi = [Z0] * N
    phi[3] = G(Fr(3, 5))
    phi[15] = G(0, Fr(4, 5))
    crit, Wv, q4, s_ = schur_criterion(phi, dvec, 15)
    Dmat = [[G(dvec[x]) if x == y else Z0 for y in range(N)] for x in range(N)]
    pos, neg, z = inertia(msub(msub(Dmat, eye(N)), outer(phi, phi)))
    record("T9.abstract.violate", "negative", "abstract instance violating (9) has two negative eigenvalues",
           (not crit) and neg == 2, {"W": str(Wv), "inertia": (pos, neg, z)})
    dvec2 = list(dvec)
    dvec2[3] = Fr(1)            # a_x = 0 but amplitude nonzero: support condition violated
    Dmat2 = [[G(dvec2[x]) if x == y else Z0 for y in range(N)] for x in range(N)]
    phi2 = [Z0] * N
    phi2[3] = G(Fr(3, 13))
    phi2[15] = G(0, Fr(4, 13))
    phi2[7] = G(Fr(12, 13))      # 9+16+144=169
    crit2, W2, q42, s2 = schur_criterion(phi2, dvec2, 15)   # skips the a_x=0 entry, as the lemma would
    pos2, neg2, z2 = inertia(msub(msub(Dmat2, eye(N)), outer(phi2, phi2)))
    record("T9.abstract.support", "negative",
           "with a_x=0 but P_x!=0 the W-test (zero entry skipped) passes yet >=2 negative eigenvalues occur",
           crit2 and neg2 >= 2,
           {"W": str(W2), "inertia": (pos2, neg2, z2), "reason": "intended: P_x=0 at a_x=0 is load-bearing"})


# ----------------------------------------------------------------- T10 equal radii identity (10)
def equal_radii():
    ok = True
    mut = True
    samples = [(Fr(1, 3), Fr(1, 20), Fr(1, 30), Fr(1, 100)), (Fr(3, 5), Fr(1, 10), Fr(1, 25), Fr(1, 50)),
               (Fr(9, 10), Fr(1, 7), Fr(1, 11), Fr(1, 40)), (Fr(1, 8), Fr(1, 64), Fr(1, 80), Fr(1, 500))]
    for s, P1v, P2v, P4v in samples:
        P3v = (s - P1v - 2 * P2v - 4 * P4v) / 3
        P0v = 1 - P1v - P2v - P3v - P4v
        assert P3v >= 0 and P0v >= 0
        K = (2 - s) / (s * (3 - s))
        a1 = 1 / (2 - s / 2) - 1 / (3 - s)
        a2 = 1 - 1 / (3 - s)
        lhs = P0v / (3 - s) + P1v / (2 - s / 2) + P2v + 2 * P3v / s - 1 - P4v / (1 - s)
        red = (a1 - K) * P1v + (a2 - 2 * K) * P2v - (1 / (3 - s) + 1 / (1 - s) + 4 * K) * P4v
        ok &= lhs == red and a1 == K * s / (4 - s) and a2 == s * K and red <= 0
        Km = (2 - s) / (s * (4 - s))
        redm = (a1 - Km) * P1v + (a2 - 2 * Km) * P2v - (1 / (3 - s) + 1 / (1 - s) + 4 * Km) * P4v
        mut &= lhs != redm
    record("T10.eq10", "positive", "(10) reduction identity, a1=Ks/(4-s)<=K, a2=sK<=2K, LHS-RHS<=0", ok)
    record("T10.eq10.mut", "negative", "K replaced by (2-s)/(s(4-s)) is detected", mut, "intended reason: wrong K")


def erratum133_witness():
    t = Fr(1, 200)
    v = [Z0] * N
    v[BAR[0]] = I_                                   # v = i|bar 1>, g_1 = i
    V = Lam(1 - t, madd(outer(v, ket(0)), outer(ket(0), v)))
    val = V[E1[0]][15]
    record("T5.err133.witness", "positive", "t=1/200, v=i|bar1>: V_(1,1111) = -199i/3200000000 exactly",
           val == G(0, Fr(-199, 3200000000)) and V[15][E1[0]] == G(0, Fr(199, 3200000000)), val)
    record("T5.err133.witness.mut", "negative", "the unconjugated sign +199i/3200000000 is detected",
           val != G(0, Fr(199, 3200000000)), "intended reason: conj(g_1)=-i")


def main():
    poly_identities()
    erratum133_witness()
    local_rules()
    psi = make_state()
    rho = identities(psi)
    U, Q = make_projector()
    record("T4.projector", "positive", "Cayley-built complex Q is an exact rank-3 orthogonal projector",
           meq(mmul(Q, Q), Q) and is_herm(Q) and trace(Q) == g(3) and
           any(Q[x][y].im != 0 for x in range(N) for y in range(N)))
    reflection(rho, Q)
    hessian_checks()
    v = mixed_vector()
    mixed_checks(v)
    conjugation_checks(v)
    constants()
    spin_flip_checks()
    equal_radii()
    allok = all(r["expected_outcome_observed"] for r in RESULTS)
    out = {"tool": "reviewer-exact-controls-v1.py", "python": sys.version.split()[0],
           "n_checks": len(RESULTS), "all_expected_outcomes_observed": allok, "results": RESULTS}
    text = json.dumps(out, indent=1) + "\n"
    if len(sys.argv) > 1:
        with open(sys.argv[1], "x", encoding="utf-8") as fh:   # exclusive creation, never overwrite
            fh.write(text)
    for r in RESULTS:
        print(("OK  " if r["expected_outcome_observed"] else "BAD ") + r["kind"][:3] + " " + r["id"])
    print("n_checks=%d all_expected_outcomes_observed=%s" % (len(RESULTS), allok))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())

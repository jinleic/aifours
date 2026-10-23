"""Checker A (python-flint arb + exact fmpq) for the central box: local dual concavity (LDC).

Notation: eta = (n00,n01,n10,n11) - 1/9 in B0 = [-r0, r0]^4; n^u = 1/9 + (A eta)_u (A integer);
multipliers y = Y eta, Y = exact rational optimal linear response at n*; z^u = K_u eta, K_u = C_u Y.
  (W)  ln F(n) <= U(eta) = sum_u [n^u Psi*(z^u) + (3/2) n^u ln n^u]  (weak pairing duality, any Y).
  (Q)  For every z whose c = B3^T z lies in the box [-gamma, gamma]^3 (this box contains c for all
       z^u, u, eta in B0, and is convex with 0 inside):  R(z) := Hess Psi*(z) <= Rbar := R(0) + eps P,
       P = I - J/4.  Since R = B3 X^{-1} B3^T with X = -B3^T Hess psi(mhat(z)) B3 > 0 (slice
       concavity), this is equivalent to X(z) >= Xmin := (X0^{-1} + eps (B3^T B3)^{-1})^{-1}.
       Taylor: Psi*(z) <= Psi*(0) + (5/4) 1.z + z^T Rbar z / 2.
       Rigorous check per c-sub-box: parametric Krawczyk for the inner maximiser in unnormalised
       mu-coordinates (mu4 = 1; m(mu), dm/dmu, S2 and dS2/dmu have nonnegative coefficients, so
       their ranges over positive boxes are corner evaluations), then a mean-value enclosure of X
       over the mu-box (S2^{-1} by a Loewner bound) and congruence+Gershgorin for X - Xmin > 0.
  (C)  Ubar(eta) = sum_u [n^u (Psi*(0) + l_u.eta + eta^T Q_u eta/2) + (3/2) n^u ln n^u],
       l_u = (5/4) K_u^T 1, Q_u = K_u^T Rbar K_u, satisfies Ubar(0) = L*, grad Ubar(0) = 0 (exact),
       and Hess Ubar < 0 on each of M^4 sub-boxes of B0 (rigorous) => ln F(n) < L* on B0 \\ {0}.
Usage: cert_ldc3.py R0 EPS NC M     e.g. 1/1000 1/10 6 8
"""
import sys, json, time, itertools
from fractions import Fraction
import numpy as np
import flint
from flint import arb, fmpq, arb_mat, fmpq_mat

flint.ctx.prec = 128
# r2 (2026-10-17): byte copy of the parent's guarded file review/colour-centralA-guarded-v2/cert_ldc3.py
# (sha256 2aa71de6...0d1cd: NC/M > 0 guard, PASS only if all NC^3 + M^4 boxes were checked, exit code),
# plus: refuse python -O, and every certificate-critical assert replaced by require() (explicit FAIL, exit 1).
if sys.flags.optimize:
    raise SystemExit('refusing to run under python -O: certificate checks must not be stripped')


def require(cond, msg):
    """Explicit certificate check; unlike assert it is active under every interpreter flag."""
    if not cond:
        print(json.dumps({'verdict': 'FAIL', 'reason': 'certificate check failed: ' + msg}))
        raise SystemExit(1)


r0 = Fraction(sys.argv[1]); eps = Fraction(sys.argv[2]); NC = int(sys.argv[3]); M = int(sys.argv[4])
if NC <= 0 or M <= 0:
    raise SystemExit("NC and M must be positive integers")
require(r0 > 0 and eps >= 0, 'r0 > 0 and eps >= 0 required')
fq = lambda f: fmpq(f.numerator, f.denominator)
toF = lambda q: Fraction(int(q.p), int(q.q))

S = [(a, b, c, 5 - a - b - c) for a, b, c in itertools.product(range(6), repeat=3)
     if a + b + c <= 5 and min(a + b, 5 - a - b) >= 1 and min(a + c, 5 - a - c) >= 1]
require(len(S) == 36, 'spectrum count != 36')
FACT = [1, 1, 2, 6, 24, 120]
W = [120 // (FACT[a] * FACT[b] * FACT[c] * FACT[d]) for (a, b, c, d) in S]
OFF = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
EDGES, seen = [], set()
for u in range(9):
    i, j = divmod(u, 3)
    for k, (r, t) in enumerate(OFF):
        v = 3 * ((i + r) % 3) + (j + t) % 3
        kv = OFF.index((-r, -t))
        if (u, k) in seen:
            continue
        seen.add((u, k)); seen.add((v, kv))
        EDGES.append((u, k, v, kv))
Cmat = [[[0] * 18 for _ in range(4)] for _ in range(9)]
for e, (u, k, v, kv) in enumerate(EDGES):
    Cmat[u][k][e] += 1
    Cmat[v][kv][e] -= 1
A = [[1, 0, 0, 0], [0, 1, 0, 0], [-1, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, -1, -1],
     [-1, 0, -1, 0], [0, -1, 0, -1], [1, 1, 1, 1]]
B3 = [[1, 0, 0], [-1, 1, 0], [0, -1, 1], [0, 0, -1]]
B3q = fmpq_mat(B3)
B3a = arb_mat(B3)


def _dy(a):
    m, e = a.man_exp()
    return Fraction(int(m)) * Fraction(2) ** int(e)


def rat_upper(x):
    return _dy(x.mid()) + _dy(x.rad())


def rat_lower(x):
    return _dy(x.mid()) - _dy(x.rad())


def sqrt_up(q):
    x = Fraction(float(q) ** 0.5) * Fraction(1000001, 1000000)
    require(x * x >= q, 'sqrt_up upper bound')
    return x


def interval(lo, hi):
    return arb(lo).union(arb(hi))


# ---------------- exact data at n* ----------------
Zc = sum(W)
mh0 = [fmpq(sum(W[i] * S[i][k] for i in range(36)), Zc) for k in range(4)]
require(all(x == fmpq(5, 4) for x in mh0), 'centre mean (5/4)1')
E2 = [[fmpq(sum(W[i] * S[i][k] * S[i][l] for i in range(36)), Zc) for l in range(4)] for k in range(4)]
V0 = fmpq_mat([[E2[k][l] - mh0[k] * mh0[l] for l in range(4)] for k in range(4)])
I4q = fmpq_mat([[1 if k == l else 0 for l in range(4)] for k in range(4)])
J0 = B3q.transpose() * (fmpq(2, 5) * V0 - I4q) * B3q          # (1/2) D^{-1} V - I at mhat* = 5/4
R0 = -(V0 * B3q * J0.inv() * B3q.transpose())
# X0 = -B3^T Hess psi(mhat*) B3 with Hess psi(mhat*) = Hess psi(5/36)/9 (homogeneity)
S2s = fmpq_mat([[fmpq(sum(W[i] * S[i][k] * S[i][l] for i in range(36)), 8100) for l in range(4)] for k in range(4)])
Hstar = fmpq_mat([[fmpq(18, 5) if k == l else 0 for l in range(4)] for k in range(4)]) - S2s.inv()
X0 = -(B3q.transpose() * Hstar * B3q) * fmpq(1, 9)
require(B3q * X0.inv() * B3q.transpose() == R0, 'R(0) = B3 X0^{-1} B3^T identity')
BtB = B3q.transpose() * B3q
Xmin = (X0.inv() + fq(eps) * BtB.inv()).inv()
Pperp = fmpq_mat([[fmpq(3, 4) if k == l else fmpq(-1, 4) for l in range(4)] for k in range(4)])
require(B3q * BtB.inv() * B3q.transpose() == Pperp, 'B3 (B3^T B3)^{-1} B3^T = I - J/4')
Rbar = R0 + fq(eps) * Pperp
Cq = [fmpq_mat(Cmat[u]) for u in range(9)]
G = Cq[0].transpose() * R0 * Cq[0]
for u in range(1, 9):
    G += Cq[u].transpose() * R0 * Cq[u]
ones = fmpq_mat([[1]] * 4)
bm = Cq[0].transpose() * ones * fmpq_mat([A[0]])
for u in range(1, 9):
    bm += Cq[u].transpose() * ones * fmpq_mat([A[u]])
Y = fmpq(-45, 4) * G.solve(bm)
Kq = [Cq[u] * Y for u in range(9)]
lq = [fmpq(5, 4) * (Kq[u].transpose() * ones) for u in range(9)]
Qq = [Kq[u].transpose() * Rbar * Kq[u] for u in range(9)]
require(all(sum(A[u][c] for u in range(9)) == 0 for c in range(4)), 'sum_u A_u = 0')
lsum = lq[0]
for u in range(1, 9):
    lsum += lq[u]
require(all(lsum[i, 0] == 0 for i in range(4)), 'sum_u l_u = 0')


# ---------------- polynomial maps in unnormalised mu (nonnegative coefficients) ----------------
def prod_pow(mu, s):
    t = arb(1)
    for k in range(4):
        if s[k]:
            t *= mu[k] ** s[k]
    return t


def m_of(mu):
    return [sum((arb(W[i] * S[i][k]) * prod_pow(mu, S[i]) for i in range(36) if S[i][k]), arb(0)) for k in range(4)]


def S2_of(mu):
    out = [[arb(0)] * 4 for _ in range(4)]
    for i in range(36):
        pw = arb(W[i]) * prod_pow(mu, S[i])
        for k in range(4):
            for l in range(4):
                if S[i][k] and S[i][l]:
                    out[k][l] = out[k][l] + pw * (S[i][k] * S[i][l])
    return out


def Jm_of(mu):        # d m_k / d mu_j
    out = [[arb(0)] * 4 for _ in range(4)]
    for i in range(36):
        for j in range(4):
            if not S[i][j]:
                continue
            e = list(S[i]); e[j] -= 1
            pw = arb(W[i] * S[i][j]) * prod_pow(mu, e)
            for k in range(4):
                if S[i][k]:
                    out[k][j] = out[k][j] + pw * S[i][k]
    return out


def dS2_of(mu, j):    # d S2 / d mu_j
    out = [[arb(0)] * 4 for _ in range(4)]
    for i in range(36):
        if not S[i][j]:
            continue
        e = list(S[i]); e[j] -= 1
        pw = arb(W[i] * S[i][j]) * prod_pow(mu, e)
        for k in range(4):
            for l in range(4):
                if S[i][k] and S[i][l]:
                    out[k][l] = out[k][l] + pw * (S[i][k] * S[i][l])
    return out


def corner(fun, lo, hi, *args):
    a, b = fun(lo, *args), fun(hi, *args)
    if isinstance(a[0], list):
        return [[a[k][l].union(b[k][l]) for l in range(len(a[0]))] for k in range(len(a))]
    return [a[k].union(b[k]) for k in range(len(a))]


def float_inner_mu(c):
    """mu (mu4 = 1) with B3^T(ln m(mu)/2 - ln mu) + c = 0 (float Newton in log mu)."""
    Sf = np.array(S, float); w = np.array(W, float); Bf = np.array(B3, float)
    th = np.zeros(4)
    for _ in range(100):
        d = w * np.exp(Sf @ th); m = Sf.T @ d; S2 = (Sf.T * d) @ Sf
        F = Bf.T @ (0.5 * np.log(m) - th) + c
        if np.max(np.abs(F)) < 1e-15:
            break
        Jt = Bf.T @ (0.5 * S2 / m[:, None] - np.eye(4))[:, :3]
        th[:3] -= np.linalg.solve(Jt, F)
    return np.exp(th)


def gersh_pos(Hs):
    n = Hs.nrows()
    Hm = np.array([[float(Hs[i, j].mid()) for j in range(n)] for i in range(n)])
    _, P = np.linalg.eigh(0.5 * (Hm + Hm.T))
    Pq = fmpq_mat([[fmpq(*Fraction(float(P[i, j])).as_integer_ratio()) for j in range(n)] for i in range(n)])
    require(Pq.det() != 0, 'congruence nonsingular (gersh_pos)')
    Pa = arb_mat([[arb(Pq[i, j]) for j in range(n)] for i in range(n)])
    Mx = Pa.transpose() * Hs * Pa
    worst = None
    for i in range(n):
        g = Mx[i, i] - sum((abs(Mx[i, j]) for j in range(n) if j != i), arb(0))
        if not (g > 0):
            return False, g
        worst = g if worst is None else worst.min(g)
    return True, worst


def check_Q(clo, chi):
    cbox = [interval(fq(l), fq(h)) for l, h in zip(clo, chi)]
    cmid = np.array([float((l + h) / 2) for l, h in zip(clo, chi)])
    mut = float_inner_mu(cmid)
    one = arb(1)

    def Gf(mu):
        m = m_of(mu)
        lm = [m[k].log() / 2 - mu[k].log() for k in range(4)]
        return [sum((lm[k] * B3[k][c] for k in range(4)), arb(0)) for c in range(3)]

    def dG(mu_lo, mu_hi):
        mB = corner(m_of, mu_lo, mu_hi)
        JB = corner(Jm_of, mu_lo, mu_hi)
        muB = [mu_lo[k].union(mu_hi[k]) for k in range(4)]
        T = [[JB[k][j] / mB[k] / 2 - (1 / muB[k] if k == j else 0) for j in range(3)] for k in range(4)]
        return arb_mat([[sum((B3[k][c] * T[k][j] for k in range(4)), arb(0)) for j in range(3)] for c in range(3)])

    mupt = [arb(float(x)) for x in mut[:3]] + [one]
    Jp = dG(mupt, mupt)
    Ym = np.linalg.inv(np.array([[float(Jp[i, j].mid()) for j in range(3)] for i in range(3)]))
    Ya = arb_mat([[arb(float(Ym[i, j])) for j in range(3)] for i in range(3)])
    G0 = [g + cb for g, cb in zip(Gf(mupt), cbox)]
    est = np.abs(Ym) @ np.array([abs(float(x.mid())) + float(x.rad()) for x in G0])
    rad = np.maximum(1.5 * est, 1e-14)
    for attempt in range(25):
        lo = [arb(float(mut[k] - rad[k])) for k in range(3)] + [one]
        hi = [arb(float(mut[k] + rad[k])) for k in range(3)] + [one]
        if not all(x > 0 for x in lo):
            return False, 'nonpositive'
        JB = dG(lo, hi)
        I3 = arb_mat([[1 if i == j else 0 for j in range(3)] for i in range(3)])
        Mres = I3 - Ya * JB
        dv = arb_mat([[lo[k].union(hi[k]) - arb(float(mut[k]))] for k in range(3)])
        Kv = arb_mat([[arb(float(mut[k]))] for k in range(3)]) - Ya * arb_mat([[x] for x in G0]) + Mres * dv
        if all(((Kv[k, 0] - lo[k]) > 0) and ((hi[k] - Kv[k, 0]) > 0) for k in range(3)):
            klo = [rat_lower(Kv[k, 0]) for k in range(3)] + [Fraction(1)]
            khi = [rat_upper(Kv[k, 0]) for k in range(3)] + [Fraction(1)]
            return check_X(mut, klo, khi)
        rad = rad * 2
    return False, 'krawczyk_fail'


def check_X(mut, klo, khi):
    """X(mu) = -(sum m/5) B3^T H(m(mu)) B3 >= Xmin for all mu in the box (mean-value form)."""
    muc = [Fraction(round(float(mut[k]) * 2 ** 60), 2 ** 60) for k in range(3)] + [Fraction(1)]
    require(all(klo[k] <= muc[k] <= khi[k] for k in range(4)), 'rational centre mu_c inside the Krawczyk box')
    # exact centre value
    dc = []
    for s, w in zip(S, W):
        t = Fraction(w)
        for k in range(4):
            t *= muc[k] ** s[k]
        dc.append(t)
    mc = [sum(dc[i] * S[i][k] for i in range(36)) for k in range(4)]
    S2c = fmpq_mat([[fq(sum(dc[i] * S[i][k] * S[i][l] for i in range(36))) for l in range(4)] for k in range(4)])
    S2ci = S2c.inv()
    Hc = fmpq_mat([[fq(Fraction(1, 2) / mc[k]) if k == l else 0 for l in range(4)] for k in range(4)]) - S2ci
    Xc = -(B3q.transpose() * Hc * B3q) * fq(sum(mc) / 5)
    # Loewner bound for S2^{-1} over the box
    rr = [max(muc[k] - klo[k], khi[k] - muc[k]) / muc[k] for k in range(4)]
    epsL = Fraction(0)
    for s in S:
        up, dn = Fraction(1), Fraction(1)
        for k in range(4):
            up *= (1 + rr[k]) ** s[k]; dn *= (1 - rr[k]) ** s[k]
        epsL = max(epsL, up - 1, 1 - dn)
    require(epsL < Fraction(1, 2), 'Loewner ratio eps_L < 1/2 (hence < 1)')
    e2 = epsL / (1 - epsL) * sqrt_up(sum(toF(S2ci[k, l]) ** 2 for k in range(4) for l in range(4)))
    Sinv = arb_mat([[arb(S2ci[k, l]) + arb(0, fq(e2)) for l in range(4)] for k in range(4)])
    lo_a = [arb(fq(x)) for x in klo]; hi_a = [arb(fq(x)) for x in khi]
    mB = corner(m_of, lo_a, hi_a)
    JB = corner(Jm_of, lo_a, hi_a)
    Hbox = arb_mat([[(1 / mB[k]) / 2 if k == l else arb(0) for l in range(4)] for k in range(4)]) - Sinv
    summ = sum(mB, arb(0)) / 5
    # congruence by a rational matrix P (float eigenvectors of Xc - Xmin, rounded) applied BEFORE the
    # mean-value terms, so that directional cancellations are kept: P^T (X - Xmin) P is enclosed by
    # P^T (Xc - Xmin) P + sum_j (P^T dX_j P) [dmu_j]; P nonsingular => inertia preserved (Sylvester).
    D0 = Xc - Xmin
    Dm = np.array([[float(toF(D0[i, j])) for j in range(3)] for i in range(3)])
    _, Pf = np.linalg.eigh(0.5 * (Dm + Dm.T))
    Pq = fmpq_mat([[fmpq(*Fraction(float(Pf[i, j])).as_integer_ratio()) for j in range(3)] for i in range(3)])
    require(Pq.det() != 0, 'congruence nonsingular (check_X)')
    Pa = arb_mat([[arb(Pq[i, j]) for j in range(3)] for i in range(3)])
    Mx = arb_mat([[arb(x) for x in row] for row in (Pq.transpose() * D0 * Pq).tolist()])
    for j in range(3):
        dS2 = arb_mat(corner(dS2_of, lo_a, hi_a, j))
        dH = Sinv * dS2 * Sinv - arb_mat([[JB[k][j] / (mB[k] * mB[k]) / 2 if k == l else arb(0) for l in range(4)] for k in range(4)])
        dsum = sum((JB[k][j] for k in range(4)), arb(0)) / 5
        dX = -(B3a.transpose() * Hbox * B3a) * dsum - (B3a.transpose() * dH * B3a) * summ
        dmu = arb(fq(klo[j] - muc[j])).union(arb(fq(khi[j] - muc[j])))
        Mx = Mx + (Pa.transpose() * dX * Pa) * dmu
    worst = None
    for i in range(3):
        g = (Mx[i, i] + Mx[i, i]) / 2 - sum((abs((Mx[i, j] + Mx[j, i]) / 2) for j in range(3) if j != i), arb(0))
        if not (g > 0):
            return False, g
        worst = g if worst is None else worst.min(g)
    return True, worst


# ---------------- (C): explicit Hessian of Ubar on sub-boxes of B0 ----------------
# Hess Ubar(eta) = Haff(0) + sum_c eta_c Dc + sum_u (3/2) a_u a_u^T / n^u(eta), with the affine part
# Haff(eta) = sum_u [a_u (l_u + Q_u eta)^T + (l_u + Q_u eta) a_u^T + (1/9 + a_u.eta) Q_u] computed
# exactly (rational Haff(0), Dc), so cancellations across u are exact.
_aq = [fmpq_mat([[A[u][c]] for c in range(4)]) for u in range(9)]
HAFF0 = fmpq_mat(4, 4)
DC = [fmpq_mat(4, 4) for _ in range(4)]
for u in range(9):
    HAFF0 += _aq[u] * lq[u].transpose() + lq[u] * _aq[u].transpose() + fmpq(1, 9) * Qq[u]
    for c in range(4):
        ec = fmpq_mat([[1 if i == c else 0] for i in range(4)])
        Qe = Qq[u] * ec
        DC[c] += _aq[u] * Qe.transpose() + Qe * _aq[u].transpose() + fmpq(A[u][c]) * Qq[u]


def check_C(lo, hi):
    eta = [interval(fq(l), fq(h)) for l, h in zip(lo, hi)]
    Hm = np.array([[float(toF(HAFF0[i, j])) for j in range(4)] for i in range(4)])
    for u in range(9):
        Hm += 1.5 * 9 * np.outer(A[u], A[u])
    _, Pf = np.linalg.eigh(-(Hm + Hm.T) / 2)
    Pq = fmpq_mat([[fmpq(*Fraction(float(Pf[i, j])).as_integer_ratio()) for j in range(4)] for i in range(4)])
    require(Pq.det() != 0, 'congruence nonsingular (check_C)')
    Pa = arb_mat([[arb(Pq[i, j]) for j in range(4)] for i in range(4)])
    Mx = arb_mat([[arb(x) for x in row] for row in (-(Pq.transpose() * HAFF0 * Pq)).tolist()])
    for c in range(4):
        Dp = arb_mat([[arb(x) for x in row] for row in (-(Pq.transpose() * DC[c] * Pq)).tolist()])
        Mx = Mx + Dp * eta[c]
    for u in range(9):
        nu = arb(fmpq(1, 9)) + sum((eta[c] * A[u][c] for c in range(4)), arb(0))
        if not (nu > 0):
            return False, None
        pa = Pq.transpose() * _aq[u]
        Ma = arb_mat([[arb(x) for x in row] for row in (-(pa * pa.transpose())).tolist()])
        Mx = Mx + Ma * (arb(fmpq(3, 2)) / nu)
    worst = None
    for i in range(4):
        g = Mx[i, i] - sum((abs((Mx[i, j] + Mx[j, i]) / 2) for j in range(4) if j != i), arb(0))
        if not (g > 0):
            return False, g
        worst = g if worst is None else worst.min(g)
    return True, worst


if __name__ == '__main__':
    t0 = time.time()
    gam = [Fraction(0)] * 3
    for u in range(9):
        BK = B3q.transpose() * Kq[u]
        for c in range(3):
            gam[c] = max(gam[c], sum(abs(toF(BK[c, k])) for k in range(4)) * r0)
    res_Q = {'boxes': 0, 'failed': 0, 'fails': [], 'min_margin': None}
    grid = [[-gam[c] + Fraction(2 * i, NC) * gam[c] for i in range(NC + 1)] for c in range(3)]
    for idx in itertools.product(range(NC), repeat=3):
        clo = [grid[c][idx[c]] for c in range(3)]; chi = [grid[c][idx[c] + 1] for c in range(3)]
        ok, info = check_Q(clo, chi)
        res_Q['boxes'] += 1
        if not ok:
            res_Q['failed'] += 1
            res_Q['fails'].append([[str(x) for x in clo], str(info)])
        else:
            res_Q['min_margin'] = info if res_Q['min_margin'] is None else res_Q['min_margin'].min(info)
    res_Q['min_margin_lower_bound'] = None if res_Q['min_margin'] is None else float(rat_lower(res_Q['min_margin']))
    res_Q['min_margin'] = str(res_Q['min_margin'])
    res_Q['runtime_s'] = round(time.time() - t0, 1)
    t1 = time.time()
    res_C = {'boxes': 0, 'failed': 0, 'min_margin': None}
    eg = [-r0 + Fraction(2 * i, M) * r0 for i in range(M + 1)]
    for idx in itertools.product(range(M), repeat=4):
        lo = [eg[i] for i in idx]; hi = [eg[i + 1] for i in idx]
        ok, g = check_C(lo, hi)
        res_C['boxes'] += 1
        if not ok:
            res_C['failed'] += 1
        else:
            res_C['min_margin'] = g if res_C['min_margin'] is None else res_C['min_margin'].min(g)
    res_C['min_margin_lower_bound'] = None if res_C['min_margin'] is None else float(rat_lower(res_C['min_margin']))
    res_C['min_margin'] = str(res_C['min_margin'])
    res_C['runtime_s'] = round(time.time() - t1, 1)
    out = {'r0': str(r0), 'eps': str(eps), 'NC': NC, 'M': M, 'c_halfwidths': [str(g) for g in gam],
           'Q_check': res_Q, 'C_check': res_C,
           'verdict': 'PASS' if (res_Q['boxes'] == NC ** 3 and res_C['boxes'] == M ** 4
                                 and res_Q['failed'] == 0 and res_C['failed'] == 0) else 'FAIL'}
    print(json.dumps(out, default=str))
    raise SystemExit(0 if out['verdict'] == 'PASS' else 1)

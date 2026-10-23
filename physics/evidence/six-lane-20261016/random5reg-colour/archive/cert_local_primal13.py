"""Checker A (python-flint arb + exact fmpq) for the central box (primal local argument).

Claim: for every n with eta = (n00,n01,n10,n11) - 1/9, 0 < |eta|_inf <= r1:  F(n) < F(n*).
Proof skeleton (each numbered quantity is computed rigorously below):
 (1) E_hull: an interval 4x4 matrix containing Hess psi(m) = D(m)^{-1}/2 - S2(mu(m))^{-1} for all m
     in the box B = [5/36 - delta, 5/36 + delta]^4.  Per sub-box: parametric Krawczyk for mu(m)
     (m(mu) = sum_s w_s s mu^s and dm/dmu have nonnegative coefficients, so their ranges over
     positive mu-boxes are given exactly by the two corner evaluations), then ball arithmetic.
 (2) On C = {x in M : |x_e - 5/36| <= delta}: Hess L|_T <= -kappa (T = tangent of M, 13-dim) and
     Hess L|_Tf <= -kappa_f (Tf = fibre tangent, 9-dim), via exact rational Cholesky of
     -Qr^T [E^T blockdiag(Hc) E + 2 rho I] Qr - kappa Qr^T Qr, rho >= ||H - Hc||_F over E_hull.
     => L strictly concave on C, grad L(m*) is normal to M, so m* is the unique max of L on C.
 (3) Exact rational lift Lf: eta -> x with correct vertex sums and Pf^T Hess L(m*) Lf = 0.
     Fibre gradient at m~ = x* + Lf eta: |g| <= 2 rho' |Lf eta|, rho' >= ||H - H(m*)||_F.
     Fibre maximiser within 3|g|/kappa_f of m~ (strong concavity on C + global fibre concavity,
     which follows from the exact slice-concavity certificate).  If |Lf eta|_inf + 3|g|/kappa_f
     <= delta, the fibre maximiser lies in C, hence F(n) = max_{M(n) cap C} e^L < e^{L(m*)}.
Usage: cert_local.py DELTA K R1     e.g. 3/1000 4 1/2200
"""
import sys, json, time, itertools
from fractions import Fraction
import numpy as np
import flint
from flint import arb, fmpq, arb_mat, fmpq_mat

flint.ctx.prec = 128
delta = Fraction(sys.argv[1]); K = int(sys.argv[2]); r1 = Fraction(sys.argv[3])
fq = lambda f: fmpq(f.numerator, f.denominator)
toF = lambda q: Fraction(int(q.p), int(q.q))

S = [(a, b, c, 5 - a - b - c) for a, b, c in itertools.product(range(6), repeat=3)
     if a + b + c <= 5 and min(a + b, 5 - a - b) >= 1 and min(a + c, 5 - a - c) >= 1]
assert len(S) == 36
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
Emat = [[0] * 18 for _ in range(36)]          # m (36) = E x (18)
for e, (u, k, v, kv) in enumerate(EDGES):
    Emat[4 * u + k][e] = 1
    Emat[4 * v + kv][e] = 1
A = [[1, 0, 0, 0], [0, 1, 0, 0], [-1, -1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, -1, -1],
     [-1, 0, -1, 0], [0, -1, 0, -1], [1, 1, 1, 1]]


def mpoly(mu, k):          # m_k(mu) = sum_s w_s s_k mu^s   (arb, mu list of arb)
    return sum((arb(W[i] * S[i][k]) * prod_pow(mu, S[i]) for i in range(36) if S[i][k]), arb(0))


def prod_pow(mu, s):
    t = arb(1)
    for k in range(4):
        if s[k]:
            t *= mu[k] ** s[k]
    return t


def S2poly(mu):
    out = [[arb(0)] * 4 for _ in range(4)]
    for i in range(36):
        pw = arb(W[i]) * prod_pow(mu, S[i])
        for k in range(4):
            for l in range(4):
                if S[i][k] and S[i][l]:
                    out[k][l] = out[k][l] + pw * (S[i][k] * S[i][l])
    return out


def Jpoly(mu):             # J_kl = d m_k / d mu_l = sum_s w s_k s_l mu^{s - e_l}
    out = [[arb(0)] * 4 for _ in range(4)]
    for i in range(36):
        for l in range(4):
            if not S[i][l]:
                continue
            e = list(S[i]); e[l] -= 1
            pw = arb(W[i] * S[i][l]) * prod_pow(mu, e)
            for k in range(4):
                if S[i][k]:
                    out[k][l] = out[k][l] + pw * S[i][k]
    return out


def corner_range(fun, lo, hi):
    """range of a nonnegative-coefficient polynomial map over the positive box [lo, hi]."""
    a, b = fun(lo), fun(hi)
    if isinstance(a[0], list):
        return [[a[k][l].union(b[k][l]) for l in range(4)] for k in range(4)]
    return [a[k].union(b[k]) for k in range(4)]


def float_mu(m):
    Sf = np.array(S, float); w = np.array(W, float)
    th = np.full(4, np.log(m.sum() / 5 / w.sum()) / 5)
    for _ in range(200):
        d = w * np.exp(Sf @ th); mm = Sf.T @ d
        F = mm - m
        if np.max(np.abs(F / m)) < 1e-15:
            break
        th = th - np.linalg.solve((Sf.T * d) @ Sf, F)
    return np.exp(th)


def hess_enclosure(mlo, mhi):
    mb = [arb(fq(l)).union(arb(fq(h))) for l, h in zip(mlo, mhi)]
    mmid = np.array([float((l + h) / 2) for l, h in zip(mlo, mhi)])
    mut = float_mu(mmid)
    Jt = Jpoly([arb(float(x)) for x in mut])
    Ym = np.linalg.inv(np.array([[float(Jt[k][l].mid()) for l in range(4)] for k in range(4)]))
    Ya = arb_mat([[arb(float(Ym[k][l])) for l in range(4)] for k in range(4)])
    Fm = [mpoly([arb(float(x)) for x in mut], k) - mb[k] for k in range(4)]
    est = np.abs(Ym) @ np.array([abs(float(x.mid())) + float(x.rad()) for x in Fm])
    rad = np.maximum(1.5 * est, 1e-14)
    for attempt in range(30):
        lo = [arb(float(mut[k] - rad[k])) for k in range(4)]
        hi = [arb(float(mut[k] + rad[k])) for k in range(4)]
        if not all(x > 0 for x in lo):
            return None
        JB = corner_range(Jpoly, lo, hi)
        I4 = arb_mat([[1 if k == l else 0 for l in range(4)] for k in range(4)])
        Mres = I4 - Ya * arb_mat(JB)
        box = [lo[k].union(hi[k]) for k in range(4)]
        dv = arb_mat([[box[k] - arb(float(mut[k]))] for k in range(4)])
        Kv = arb_mat([[arb(float(mut[k]))] for k in range(4)]) - Ya * arb_mat([[x] for x in Fm]) + Mres * dv
        if all(((Kv[k, 0] - lo[k]) > 0) and ((hi[k] - Kv[k, 0]) > 0) for k in range(4)):
            return centred_hessian(mlo, mhi, mut, [rat_lower(Kv[k, 0]) for k in range(4)],
                                   [rat_upper(Kv[k, 0]) for k in range(4)])
        rad = rad * 2
    return None


def centred_hessian(mlo, mhi, mut, klo, khi):
    """Mean-value enclosure of H(m) over the m sub-box, given mu(m) in [klo, khi] for all of it.
    H(m) = H(mc) + sum_j dH/dm_j(xi) (m - mc)_j along the segment [mc, m] (inside the sub-box),
    dH/dm_j = -(1/2) e_j e_j^T / m_j^2 + S2^{-1} T3(S2^{-1} e_j) S2^{-1},  T3(v) = sum_l v_l T3_l,
    T3_l = sum_s w_s mu^s s_l s s^T (nonnegative coefficients: range = corner evaluations).
    S2^{-1} over the mu-box: Loewner bound (1-eps) S2c <= S2 <= (1+eps) S2c (all d_s ratios in
    [1-eps, 1+eps]), so |S2^{-1} - S2c^{-1}|_entry <= eps/(1-eps) ||S2c^{-1}||_F."""
    muc = [Fraction(round(float(mut[k]) * 2 ** 60), 2 ** 60) for k in range(4)]
    assert all(klo[k] < muc[k] < khi[k] for k in range(4))
    dc = [W[i] * prod_frac(muc, S[i]) for i in range(36)]
    mc = [sum(dc[i] * S[i][k] for i in range(36)) for k in range(4)]
    assert all(mlo[k] <= mc[k] <= mhi[k] for k in range(4)), 'centre outside sub-box'
    S2c = fmpq_mat([[fq(sum(dc[i] * S[i][k] * S[i][l] for i in range(36))) for l in range(4)] for k in range(4)])
    S2ci = S2c.inv()
    Hc = [[(Fraction(1, 2) / mc[k] if k == l else 0) - toF(S2ci[k, l]) for l in range(4)] for k in range(4)]
    rr = [max(muc[k] - klo[k], khi[k] - muc[k]) / muc[k] for k in range(4)]
    eps = Fraction(0)
    for s in S:
        up, dn = Fraction(1), Fraction(1)
        for k in range(4):
            up *= (1 + rr[k]) ** s[k]; dn *= (1 - rr[k]) ** s[k]
        eps = max(eps, up - 1, 1 - dn)
    assert eps < Fraction(1, 2)
    e2 = eps / (1 - eps) * sqrt_up(sum(toF(S2ci[k, l]) ** 2 for k in range(4) for l in range(4)))
    Sinv = arb_mat([[arb(S2ci[k, l]) + arb(0, fq(e2)) for l in range(4)] for k in range(4)])
    klo_a = [arb(fq(x)) for x in klo]; khi_a = [arb(fq(x)) for x in khi]
    T3 = []
    for l in range(4):
        def T3l(mu, l=l):
            out = [[arb(0)] * 4 for _ in range(4)]
            for i in range(36):
                if not S[i][l]:
                    continue
                pw = arb(W[i] * S[i][l]) * prod_pow(mu, S[i])
                for a in range(4):
                    for b in range(4):
                        if S[i][a] and S[i][b]:
                            out[a][b] = out[a][b] + pw * (S[i][a] * S[i][b])
            return out
        A_, B_ = T3l(klo_a), T3l(khi_a)
        T3.append(arb_mat([[A_[a][b].union(B_[a][b]) for b in range(4)] for a in range(4)]))
    mbox = [arb(fq(l_)).union(arb(fq(h_))) for l_, h_ in zip(mlo, mhi)]
    Henc = arb_mat([[arb(fq(Hc[k][l])) for l in range(4)] for k in range(4)])
    for j in range(4):
        v = [Sinv[l, j] for l in range(4)]
        Tv = T3[0] * v[0] + T3[1] * v[1] + T3[2] * v[2] + T3[3] * v[3]
        dH = Sinv * Tv * Sinv
        dH = dH - arb_mat([[(1 / (mbox[j] * mbox[j])) / 2 if (a == j and b == j) else arb(0) for b in range(4)] for a in range(4)])
        dm = arb(fq(mlo[j] - mc[j])).union(arb(fq(mhi[j] - mc[j])))
        Henc = Henc + dH * dm
    return ([[rat_lower(Henc[k, l]) for l in range(4)] for k in range(4)],
            [[rat_upper(Henc[k, l]) for l in range(4)] for k in range(4)])


def prod_frac(mu, s):
    t = Fraction(1)
    for k in range(4):
        if s[k]:
            t *= mu[k] ** s[k]
    return t


def sqrt_up(q):
    x = Fraction(float(q) ** 0.5) * Fraction(1000001, 1000000)
    assert x * x >= q
    return x


def _dy(a):               # exact Fraction of an exact (radius-0) arb such as mid() or rad()
    m, e = a.man_exp()
    return Fraction(int(m)) * Fraction(2) ** int(e)


def rat_upper(x):          # rational >= every point of ball x (exact: mid + rad)
    return _dy(x.mid()) + _dy(x.rad())


def rat_lower(x):
    return _dy(x.mid()) - _dy(x.rad())


def chol_pos(Mq):
    """exact: Mq (fmpq_mat, symmetric) positive definite iff all LDL^T pivots > 0."""
    n = Mq.nrows()
    a = [[Mq[i, j] for j in range(n)] for i in range(n)]
    for k in range(n):
        if not a[k][k] > 0:
            return False
        for i in range(k + 1, n):
            f = a[i][k] / a[k][k]
            for j in range(k + 1, n):
                a[i][j] -= f * a[k][j]
    return True


if __name__ == '__main__':
    t0 = time.time()
    c = Fraction(5, 36)
    grid = [c - delta + Fraction(2 * i, K) * delta for i in range(K + 1)]
    lo_h = [[None] * 4 for _ in range(4)]; hi_h = [[None] * 4 for _ in range(4)]
    nbox, nfail = 0, 0
    for idx in itertools.product(range(K), repeat=4):
        mlo = [grid[i] for i in idx]; mhi = [grid[i + 1] for i in idx]
        H = hess_enclosure(mlo, mhi)
        nbox += 1
        if H is None:
            nfail += 1
            continue
        Hlo, Hhi = H
        for k in range(4):
            for l in range(4):
                lo_h[k][l] = Hlo[k][l] if lo_h[k][l] is None else min(lo_h[k][l], Hlo[k][l])
                hi_h[k][l] = Hhi[k][l] if hi_h[k][l] is None else max(hi_h[k][l], Hhi[k][l])
    t1 = time.time()
    out = {'delta': str(delta), 'K': K, 'r1': str(r1), 'subboxes': nbox, 'krawczyk_failed': nfail,
           'hull_runtime_s': round(t1 - t0, 1)}
    if nfail:
        out['verdict'] = 'FAIL'; print(json.dumps(out)); sys.exit(0)
    Hc = [[(lo_h[k][l] + hi_h[k][l]) / 2 for l in range(4)] for k in range(4)]
    rad2 = sum(((hi_h[k][l] - lo_h[k][l]) / 2) ** 2 for k in range(4) for l in range(4))
    # exact H(m*) = D^{-1}/2 - S2*^{-1}, S2* = sum_s (w_s/8100) s s^T
    S2s = fmpq_mat([[fmpq(sum(W[i] * S[i][k] * S[i][l] for i in range(36)), 8100) for l in range(4)] for k in range(4)])
    Hs = fmpq_mat([[fmpq(18, 5) if k == l else 0 for l in range(4)] for k in range(4)]) - S2s.inv()
    Hsf = [[toF(Hs[k, l]) for l in range(4)] for k in range(4)]
    assert all(lo_h[k][l] <= Hsf[k][l] <= hi_h[k][l] for k in range(4) for l in range(4))
    radp2 = sum(max(abs(hi_h[k][l] - Hsf[k][l]), abs(Hsf[k][l] - lo_h[k][l])) ** 2 for k in range(4) for l in range(4))
    # rational upper bounds on Frobenius norms via squares: rho^2 <= rad2 (sqrt_up defined above)
    rho = sqrt_up(rad2); rhop = sqrt_up(radp2)
    E = fmpq_mat(Emat)
    blk = [[fmpq(0)] * 36 for _ in range(36)]
    for u in range(9):
        for k in range(4):
            for l in range(4):
                blk[4 * u + k][4 * u + l] = fq(Hc[k][l])
    Hx = E.transpose() * fmpq_mat(blk) * E          # 18x18 rational
    # rational bases of T (13-dim) and Tf (9-dim)
    Vx = fmpq_mat([[sum(Emat[4 * u + k][e] for k in range(4)) for e in range(18)] for u in range(9)])
    rowcol = []
    for i in range(3):
        rowcol.append([sum(Vx[3 * i + j, e] for j in range(3)) for e in range(18)])
    for j in range(3):
        rowcol.append([sum(Vx[3 * i + j, e] for i in range(3)) for e in range(18)])
    def kernel_basis(Mq):
        R = Mq.rref()[0]; n = Mq.ncols(); piv = []
        rr = 0
        for col in range(n):
            if rr < R.nrows() and R[rr, col] != 0:
                piv.append(col); rr += 1
        free = [cc for cc in range(n) if cc not in piv]
        B = []
        for f in free:
            v = [fmpq(0)] * n; v[f] = fmpq(1)
            for r_, p in enumerate(piv):
                v[p] = -R[r_, f]
            B.append(v)
        return fmpq_mat([[B[j][i] for j in range(len(B))] for i in range(n)])
    QT = kernel_basis(fmpq_mat(rowcol)); QF = kernel_basis(Vx)
    assert QT.ncols() == 13 and QF.ncols() == 9
    I18 = fmpq_mat([[1 if i == j else 0 for j in range(18)] for i in range(18)])
    def best_kappa(Qr):
        G = Qr.transpose() * Qr
        base = Qr.transpose() * (Hx + fq(2 * rho) * I18) * Qr
        lo_k, hi_k = Fraction(0), Fraction(20)
        if not chol_pos(-base):
            return None
        for _ in range(30):
            mid = (lo_k + hi_k) / 2
            if chol_pos(-base - fq(mid) * G):
                lo_k = mid
            else:
                hi_k = mid
        return lo_k
    kappa = best_kappa(QT); kappa_f = best_kappa(QF)
    out.update({'rho_frobenius_radius': float(rho), 'rho_prime': float(rhop),
                'kappa_T': None if kappa is None else float(kappa), 'kappa_fibre': None if kappa_f is None else float(kappa_f)})
    if not kappa or not kappa_f:
        out['verdict'] = 'FAIL'; print(json.dumps(out)); sys.exit(0)
    # exact optimal lift: Vx Lf = 5 A, QF^T H* Lf = 0  (H* exact)
    blk2 = [[fmpq(0)] * 36 for _ in range(36)]
    for u in range(9):
        for k in range(4):
            for l in range(4):
                blk2[4 * u + k][4 * u + l] = Hs[k, l]
    Hstar = E.transpose() * fmpq_mat(blk2) * E
    Mbig = fmpq_mat([[Vx[i, j] for j in range(18)] for i in range(9)] + [[x for x in row] for row in (QF.transpose() * Hstar).tolist()])
    rhs = fmpq_mat([[5 * A[i][c] for c in range(4)] for i in range(9)] + [[0] * 4 for _ in range(9)])
    # least-squares-free exact solve: Mbig has full column rank 18 (checked via rank)
    assert Mbig.rank() == 18
    Lf = (Mbig.transpose() * Mbig).solve(Mbig.transpose() * rhs)
    assert Mbig * Lf == rhs, 'lift system inconsistent'
    # worst case over the eta-box corners (norms are convex)
    worst_inf, worst_2sq = Fraction(0), Fraction(0)
    for sgn in itertools.product([-1, 1], repeat=4):
        v = [sum(toF(Lf[e, cc]) * sgn[cc] for cc in range(4)) * r1 for e in range(18)]
        worst_inf = max(worst_inf, max(abs(x) for x in v))
        worst_2sq = max(worst_2sq, sum(x * x for x in v))
    L2 = sqrt_up(worst_2sq)
    gbound = 2 * rhop * L2
    radius = 3 * gbound / kappa_f
    ok = worst_inf + radius <= delta
    out.update({'lift_inf': float(worst_inf), 'lift_2': float(L2), 'fibre_grad_bound': float(gbound),
                'fibre_ball_radius': float(radius), 'containment': bool(ok),
                'runtime_s': round(time.time() - t0, 1), 'verdict': 'PASS' if ok else 'FAIL'})
    print(json.dumps(out))

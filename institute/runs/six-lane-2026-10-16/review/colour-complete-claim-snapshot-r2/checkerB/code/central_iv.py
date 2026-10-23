#!/usr/bin/env python3
r"""Checker B, CENTRAL BOX (mpmath.iv + fractions).

Claim: ln F(n) < L* := (5/2) ln 5 + ln(25/24) for every n with 0 < max_k |n_k - 1/9| <= r0
(default r0 = 1/10000; n = (n00, n01, n10, n11), nine values n^u by (7.2)).

Independence: written from README section 1, the "FROZEN: outer cell certificate scheme" and
"central box certified by checker A" log entries, and the primary preprint text only.  No file
under code/ or outer/code/ (or archive/) was read or imported.

Derivations used (all re-derived here; u = class, k = matrix entry, see cb_common.py)
------------------------------------------------------------------------------------
D1 (Gibbs / max-entropy).  For c > 0, d >= 0 with sum_s d_s = c, m = sum_s d_s s, and any
    mu > 0, with q_s(mu) := w_s mu^s / Phi(mu) (a probability vector on S):
      sum_s d_s ln(w_s/d_s) = c ln Phi(mu) - c ln c - <ln mu, m> - c KL(d/c || q(mu))
    so H(m) := max_d sum_s d_s ln(w_s/d_s) <= c ln Phi(mu) - c ln c - <ln mu, m>, with equality
    iff d = c q(mu), i.e. iff m = c mhat(mu), mhat(mu) := sum_s q_s s = mu*grad Phi(mu)/Phi(mu)
    (0-homogeneous in mu; |mhat| = 5 by Euler).
D2 (scaling).  psi(m) := H(m) + (1/2) sum_k m_k ln m_k satisfies psi(c mh) = c psi(mh) + (3/2) c ln c
    (H(c mh) = c H(mh) - c ln c; (1/2) sum c mh ln(c mh) = c (1/2) sum mh ln mh + (5/2) c ln c).
D3 (weak pairing duality, (W)).  For a fibre point d of n and ANY y in R^18, z^u := C_u y:
    sum_u <z^u, m^u> = sum_e y_e (m^u_k - m^v_k') = 0 by (7.5), hence
      ln Fhat(d) = sum_u [sum_s d^u_s ln(w_s/d^u_s) + (1/2) sum_k m^u_k ln m^u_k + <z^u, m^u>]
                <= sum_u [n^u (psi(mh^u) + <z^u, mh^u>) + (3/2) n^u ln n^u]      (D2, mh^u in conv S)
                <= U := sum_u [n^u Psi*(z^u) + (3/2) n^u ln n^u],  Psi*(z) := max_{conv S} psi + <z,.>.
    Max over the fibre: ln F(n) <= U.  We take y = Y eta (Y rational 18x4), z^u = K_u eta.
D4 (Psi* near 0).  INPUT LEMMA (README sec. 2, "exact slice-concavity lemma", not re-proved
    here; the same lemma is rule 1 of the frozen outer scheme): psi is concave on conv(S).
    Gradient on the open cone (paper (5.18)-(5.19)): with mu(m) solving (7.8) (so Phi(mu)=|m|/5),
    d psi/dm_j = (1/2) ln m_j + 1/2 - ln mu_j - sum_k m_k d ln mu_k/dm_j and
    sum_k m_k d ln mu_k/dm_j = d Phi(mu(m))/dm_j = 1/5, so grad psi = (1/2) ln m - ln mu + 3/10.
    m -> ln mu(m) inverts theta -> grad_theta Phi(e^theta) whose Jacobian is
    S2 = sum_s w_s mu^s s s^T, so Hess psi = (1/2) diag(m)^-1 - S2(mu(m))^-1; on |m| = 5,
    S2(mu(m)) = N(mu') := sum_s q_s(mu') s s^T for any positive rescaling mu' of mu(m).
    Hadamard basis B (columns: row contrast r, column contrast t, product rt; B^T B = 4 I,
    B^T 1 = 0).  Interior stationarity of psi + <z,.> on the slice <=> B^T(grad psi + z) = 0;
    writing ln mu = B phi (scaling fixed so that sum ln mu = 0) and c := B^T z this reads
      h(phi) = -c,   h(phi) := (1/2) B^T ln mhat(e^{B phi}) - 4 phi,
    with Jacobian J_h = (1/2) B^T diag(1/mhat) Cov_q(s) B - 4 I (d mhat/d theta = Cov_q(s)).
    Implicit differentiation: Hess Psi*(z) = R(z) := B X(z)^-1 B^T,
      X(z) := -B^T Hess psi(mh(z)) B = B^T [N(mu)^-1 - (1/2) diag(mhat(mu))^-1] B,
    grad Psi*(z) = mh(z) (envelope).  At z = 0: mu = 1, q_s = w_s/900, mh* = (5/4) 1,
    N(1) = W2/900 with W2 := sum_s w_s s s^T, X0 = B^T [900 W2^-1 - (2/5) I] B and
    R(0) = B X0^-1 B^T (exact rationals), Psi*(0) = psi(mh*) = (5/2) ln(5/4) + ln 900
    (D1 equality at mu = 1; mh* is stationary since grad psi(mh*) is parallel to 1).
    If phi in a box solves h(phi) = -c and X > 0 there, lemma L makes mhat(e^{B phi}) a strict
    local, hence the unique global, maximiser; the branch is smooth (IFT).
D5 ((Q) quadratic bound).  Xmin := (X0^-1 + eps (B^T B)^-1)^-1, Rbar := B Xmin^-1 B^T
    = R(0) + eps (I - J/4) (asserted exactly; I - J/4 = B (B^T B)^-1 B^T).  If X >= Xmin on
    the segment [0, z] then R <= Rbar there (inversion reverses Loewner order; congruence by B
    preserves it) and Taylor with integral remainder for t -> Psi*(t z) gives
      Psi*(z) <= Psi*(0) + (5/4) 1.z + (1/2) z^T Rbar z.
    Region: c = B^T K_u (t eta) lies in Cbox = prod_i [-gamma_i, gamma_i],
    gamma_i := r0 max_u sum_j |(B^T K_u)_ij|, for all u, t in [0,1], eta in B0 = [-r0,r0]^4.
    Verification of X >= Xmin on Cbox, per sub-box Csub of an NC^3 grid:
     (i) parametric Krawczyk: K = phic - Yk (h(phic) + Csub) + (I - Yk J_h(Xb)) (Xb - phic)
         inside int(Xb) and Yk nonsingular  =>  for every c in Csub some phi in Xb solves
         h(phi) = -c (mean value theorem row-wise + Brouwer for phi -> phi - Yk (h(phi) + c));
    (ii) Loewner sandwich on Xb: interval enclosures give qlo_s <= q_s <= qhi_s; since
         N = sum_s q_s s s^T with PSD rank-one terms, N <= Nhi := sum_s qhi_s s s^T, so
         N^-1 >= Nhi^-1; mhat_k >= mlo_k := sum_s qlo_s s_k; hence
         X >= Xlb := B^T Nhi^-1 B - (1/2) B^T diag(1/mlo) B;
   (iii) Gershgorin lower bound of lambda_min(Xlb - Xmin) > 0 (and Sylvester minors > 0).
D6 ((C)).  l_u := (5/4) K_u^T 1, Q_u := K_u^T Rbar K_u, n^u = 1/9 + a_u.eta (a_u = AROWS[u]):
      U(eta) <= Ubar(eta) := sum_u [n^u (Psi*(0) + l_u.eta + (1/2) eta^T Q_u eta) + (3/2) n^u ln n^u].
    Ubar(0) = Psi*(0) + (3/2) ln(1/9) = L*  (exact identity: both = -3 ln2 - ln3 + (9/2) ln5).
    grad Ubar(0) = (Psi*(0) + (3/2)(1 - ln 9)) sum_u a_u + (1/9) sum_u l_u = 0 (both sums are 0
    exactly; sum_u C_u^T 1 = 0 for any Y).
    Hess Ubar(eta) = Haff + sum_c eta_c D_c + sum_u (3/2) a_u a_u^T / n^u with
      Haff := sum_u [a_u l_u^T + l_u a_u^T + Q_u/9],
      D_c  := sum_u [a_u (Q_u e_c)^T + (Q_u e_c) a_u^T + a_{u,c} Q_u].
    On B0, n^u >= nlo_u := 1/9 - r0 |a_u|_1 > 0, so Hess Ubar(eta) <= Tm(eta) :=
    Haff + sum_c eta_c D_c + sum_u (3/2) a_u a_u^T/nlo_u, affine in eta.  Tm(v) + delta I < 0 at the
    16 vertices v (exact Sylvester) => on all of B0 (convexity of the negative-definite cone).
    Conclusion: for eta in B0 \ {0},
      ln F(n) <= U(eta) <= Ubar(eta) = L* + int_0^1 (1-t) eta^T Hess Ubar(t eta) eta dt
              <= L* - (delta/2) |eta|_2^2 < L*.
"""
import argparse
import hashlib
import itertools
import json
import os
import platform
import resource
import sys
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cb_common as cb  # noqa: E402
import mpmath  # noqa: E402
from mpmath import iv, mp, mpf  # noqa: E402

S, W = cb.SPECTRA, cb.WEIGHT
NS = len(S)


# ---------------------------------------------------------------------------- iv helpers
def lo(x):
    return mp.make_mpf(x._mpi_[0])


def hi(x):
    return mp.make_mpf(x._mpi_[1])


def mid(x):
    return (lo(x) + hi(x)) / 2


def ivq(x):
    x = Fr(x)
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def ivsum(xs):
    acc = iv.mpf(0)
    for x in xs:
        acc += x
    return acc


def ivabs_hi(x):
    return iv.mpf(max(abs(lo(x)), abs(hi(x))))


def iv_inverse(M):
    """Gauss-Jordan without pivoting on an interval matrix (encloses the inverse of every
    member); fails if a pivot interval contains 0."""
    n = len(M)
    aug = [[M[i][j] for j in range(n)] + [iv.mpf(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        p = aug[col][col]
        if lo(p) <= 0 <= hi(p):
            raise ArithmeticError("pivot interval contains 0")
        aug[col] = [x / p for x in aug[col]]
        for r in range(n):
            if r != col:
                f = aug[r][col]
                aug[r] = [x - f * y for x, y in zip(aug[r], aug[col])]
    return [row[n:] for row in aug]


def iv_det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def fr_str(x):
    return f"{x.numerator}/{x.denominator}"


# ---------------------------------------------------------------------------- exact part
def exact_objects(r0, eps):
    ex = {}
    assert cb.check_spectra() and cb.check_arows()
    B = [[r, t, r * t] for (r, t) in cb.KRT]          # Hadamard basis (4x3)
    Bf = [[Fr(x) for x in row] for row in B]
    assert cb.mm(cb.T(Bf), Bf) == cb.msc(Fr(4), cb.eye(3))
    assert all(sum(row[i] for row in B) == 0 for i in range(3))
    W2 = [[Fr(sum(w * s[a] * s[b] for s, w in zip(S, W))) for b in range(4)] for a in range(4)]
    phi1 = sum(W)
    assert phi1 == 900 == cb.phi_closed_form(1, 1, 1, 1)
    mstar = [Fr(sum(w * s[a] for s, w in zip(S, W)), phi1) for a in range(4)]
    assert mstar == [Fr(5, 4)] * 4
    # W2 is diagonal in the orthogonal basis {1, r, t, rt} (row/column-swap characters);
    # record the eigenvalues (only for the report: every later formula uses W2 itself).
    w2eig = []
    for v in ([1, 1, 1, 1], [row[0] for row in B], [row[1] for row in B], [row[2] for row in B]):
        Wv = [sum(W2[a][b] * v[b] for b in range(4)) for a in range(4)]
        lam = Wv[0] / v[0]
        assert Wv == [lam * x for x in v]
        w2eig.append(lam)
    ex["W2_eigs_1_r_t_rt"] = [fr_str(x) for x in w2eig]
    # Hess psi(m*) = (1/2) diag(m*)^-1 - N(1)^-1 = (2/5) I - 900 W2^-1
    hpsi0 = cb.madd(cb.msc(Fr(2, 5), cb.eye(4)), cb.msc(Fr(-phi1), cb.inv(W2)))
    X0 = cb.msc(Fr(-1), cb.mm(cb.T(Bf), cb.mm(hpsi0, Bf)))
    assert cb.is_pos_def_exact(X0)
    R0 = cb.mm(Bf, cb.mm(cb.inv(X0), cb.T(Bf)))
    assert all(sum(row) == 0 for row in R0)
    # Y: optimal linear dual response at n* (any rational Y is valid for (W))
    Cf = [[[Fr(x) for x in row] for row in cb.CMAT[u]] for u in range(9)]
    Af = [[Fr(x) for x in a] for a in cb.AROWS]
    assert [sum(Af[u][c] for u in range(9)) for c in range(4)] == [0] * 4
    G = [[Fr(0)] * 18 for _ in range(18)]
    for u in range(9):
        G = cb.madd(G, cb.mm(cb.T(Cf[u]), cb.mm(R0, Cf[u])))
    msum = [[Fr(0)] * 4 for _ in range(18)]
    for u in range(9):
        ct1 = [sum(Cf[u][k][e] for k in range(4)) for e in range(18)]
        for e in range(18):
            for c in range(4):
                msum[e][c] += ct1[e] * Af[u][c]
    Y = cb.msc(Fr(-45, 4), cb.mm(cb.inv(G), msum))
    Ku = [cb.mm(Cf[u], Y) for u in range(9)]
    BtK = [cb.mm(cb.T(Bf), Ku[u]) for u in range(9)]
    gamma = [r0 * max(sum(abs(x) for x in BtK[u][i]) for u in range(9)) for i in range(3)]
    # (Q) objects
    BtB_inv = cb.inv(cb.mm(cb.T(Bf), Bf))
    Xmin = cb.inv(cb.madd(cb.inv(X0), cb.msc(eps, BtB_inv)))
    Rbar = cb.madd(R0, cb.msc(eps, cb.madd(cb.eye(4), cb.msc(Fr(-1, 4), [[Fr(1)] * 4 for _ in range(4)]))))
    assert Rbar == cb.mm(Bf, cb.mm(cb.inv(Xmin), cb.T(Bf)))
    # (C) objects
    Qu = [cb.mm(cb.T(Ku[u]), cb.mm(Rbar, Ku[u])) for u in range(9)]
    lu = [[Fr(5, 4) * sum(Ku[u][k][c] for k in range(4)) for c in range(4)] for u in range(9)]
    assert [sum(lu[u][c] for u in range(9)) for c in range(4)] == [0] * 4
    Haff = [[Fr(0)] * 4 for _ in range(4)]
    for u in range(9):
        Haff = cb.madd(Haff, cb.madd(cb.madd(cb.outer(Af[u], lu[u]), cb.outer(lu[u], Af[u])),
                                     cb.msc(Fr(1, 9), Qu[u])))
    Dc = []
    for c in range(4):
        D = [[Fr(0)] * 4 for _ in range(4)]
        for u in range(9):
            qc = [Qu[u][k][c] for k in range(4)]
            D = cb.madd(D, cb.madd(cb.madd(cb.outer(Af[u], qc), cb.outer(qc, Af[u])),
                                   cb.msc(Af[u][c], Qu[u])))
        Dc.append(D)
    nlo = [Fr(1, 9) - r0 * sum(abs(x) for x in Af[u]) for u in range(9)]
    assert all(x > 0 for x in nlo)
    ex.update(B=B, Bf=Bf, W2=W2, X0=X0, R0=R0, Y=Y, Ku=Ku, gamma=gamma, Xmin=Xmin, Rbar=Rbar,
              Qu=Qu, lu=lu, Haff=Haff, Dc=Dc, nlo=nlo, Af=Af)
    return ex


def log_coeffs_identity():
    """Ubar(0) = Psi*(0) - 3 ln 3 with Psi*(0) = (5/2) ln(5/4) + ln 900, versus
    L* = (5/2) ln 5 + ln(25/24); compare exact coefficient vectors over (ln 2, ln 3, ln 5)."""
    def v(fr, mult):
        fr = Fr(fr)
        out = {2: Fr(0), 3: Fr(0), 5: Fr(0)}
        for part, sgn in ((fr.numerator, 1), (fr.denominator, -1)):
            for p in (2, 3, 5):
                while part % p == 0:
                    part //= p
                    out[p] += sgn * Fr(mult)
            assert part == 1
        return out

    def add(*vs):
        out = {2: Fr(0), 3: Fr(0), 5: Fr(0)}
        for d in vs:
            for p in out:
                out[p] += d[p]
        return out
    ubar0 = add(v(Fr(5, 4), Fr(5, 2)), v(900, 1), v(Fr(1, 9), Fr(3, 2)))
    lstar = add(v(5, Fr(5, 2)), v(Fr(25, 24), 1))
    assert ubar0 == lstar
    return {str(p): fr_str(c) for p, c in lstar.items()}


# ---------------------------------------------------------------------------- (C): exact
def check_C(ex, r0):
    Haff, Dc, nlo, Af = ex["Haff"], ex["Dc"], ex["nlo"], ex["Af"]
    hlog = [[Fr(0)] * 4 for _ in range(4)]
    for u in range(9):
        hlog = cb.madd(hlog, cb.msc(Fr(3, 2) / nlo[u], cb.outer(Af[u], Af[u])))
    base = cb.madd(Haff, hlog)
    verts = []
    for sg in itertools.product([-1, 1], repeat=4):
        Tm = base
        for c in range(4):
            Tm = cb.madd(Tm, cb.msc(sg[c] * r0, Dc[c]))
        verts.append((sg, Tm))
    # non-rigorous eigenvalue estimate only to choose delta; the decision is exact below
    mp.prec = 128
    lam = [max(mp.eigsy(mpmath.matrix([[mpf(x.numerator) / x.denominator for x in row]
                                         for row in Tm]))[0]) for _, Tm in verts]
    lam_max = max(lam)
    delta = Fr(int(-lam_max * 10 ** 6) - 1, 10 ** 6)        # rational, just below -max lambda_max
    ok_neg = all(cb.is_pos_def_exact(cb.msc(Fr(-1), Tm)) for _, Tm in verts)
    ok_delta = all(cb.is_pos_def_exact(cb.msc(Fr(-1), cb.madd(Tm, cb.msc(delta, cb.eye(4)))))
                   for _, Tm in verts)
    # Hess Ubar(0) = Haff + sum_u (3/2) * 9 a_u a_u^T (exact; eigenvalues printed for information)
    h0 = Haff
    for u in range(9):
        h0 = cb.madd(h0, cb.msc(Fr(27, 2), cb.outer(Af[u], Af[u])))
    lam0 = mp.eigsy(mpmath.matrix([[mpf(x.numerator) / x.denominator for x in row] for row in h0]))[0]
    return {
        "vertices": len(verts),
        "all_vertex_matrices_negative_definite_exact": ok_neg,
        "delta_rigorous": fr_str(delta), "delta_float": float(delta),
        "Tm_plus_delta_I_negative_definite_at_all_vertices_exact": ok_delta,
        "max_vertex_lambda_max_float": float(lam_max),
        "HessUbar_at_0_eigs_float": sorted(float(x) for x in lam0),
        "Dc_max_abs_entry_float": max(float(abs(x)) for D in Dc for row in D for x in row),
        "pass": ok_neg and ok_delta and delta > 0,
    }


# ---------------------------------------------------------------------------- (Q): intervals
class QCheck:
    def __init__(self, ex):
        self.B = ex["B"]
        self.BtS = [[sum(self.B[k][i] * s[k] for k in range(4)) for i in range(3)] for s in S]
        self.Xmin_iv = [[ivq(x) for x in row] for row in ex["Xmin"]]
        self.c54 = iv.mpf(5) / 4

    def q_box(self, Xb):
        """Interval enclosure of q_s(e^{B phi}) for phi in the box Xb."""
        t = [ivsum(self.BtS[a][i] * Xb[i] for i in range(3)) for a in range(NS)]
        E = [W[a] * iv.exp(t[a]) for a in range(NS)]
        Z = ivsum(E)
        return [e / Z for e in E]

    def mhat(self, q):
        return [ivsum(q[a] * S[a][k] for a in range(NS) if S[a][k]) for k in range(4)]

    def h_point(self, phic):
        Xp = [iv.mpf(x) for x in phic]
        m = self.mhat(self.q_box(Xp))
        lm = [iv.log(x) for x in m]
        return [ivsum(self.B[k][i] * lm[k] for k in range(4)) / 2 - 4 * Xp[i] for i in range(3)]

    def jac_box(self, Xb):
        """J_h over the box: (1/2) B^T diag(1/mhat) Cov B - 4 I, Cov written about the
        exact point 5/4 (Cov = sum q (s-a)(s-a)^T - (mhat-a)(mhat-a)^T) to limit cancellation."""
        q = self.q_box(Xb)
        m = self.mhat(q)
        cov = [[iv.mpf(0)] * 4 for _ in range(4)]
        for a in range(NS):
            d = [S[a][k] - self.c54 for k in range(4)]
            for k in range(4):
                for l in range(k, 4):
                    cov[k][l] += q[a] * d[k] * d[l]
        dm = [m[k] - self.c54 for k in range(4)]
        for k in range(4):
            for l in range(k, 4):
                cov[k][l] -= dm[k] * dm[l]
                cov[l][k] = cov[k][l]
        J = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                acc = ivsum(self.B[k][i] * cov[k][l] * self.B[l][j] / m[k]
                            for k in range(4) for l in range(4))
                J[i][j] = acc / 2 - (4 if i == j else 0)
        return J

    def newton_center(self, cc):
        """Non-rigorous: approximate phi with h(phi) = -cc (only used as Krawczyk centre)."""
        phi = [mpf(0)] * 3
        for _ in range(4):
            hv = [mid(x) for x in self.h_point(phi)]
            J = self.jac_box([iv.mpf(x) for x in phi])
            Jm = mpmath.matrix([[mid(J[i][j]) for j in range(3)] for i in range(3)])
            d = mp.lu_solve(Jm, mpmath.matrix([hv[i] + cc[i] for i in range(3)]))
            phi = [phi[i] - d[i] for i in range(3)]
        Jm = self.jac_box([iv.mpf(x) for x in phi])
        return phi, mpmath.matrix([[mid(Jm[i][j]) for j in range(3)] for i in range(3)])

    def check_subbox(self, clo, chi):
        cc = [(a + b) / 2 for a, b in zip(clo, chi)]
        hw = [(b - a) / 2 for a, b in zip(clo, chi)]
        phic, Jc = self.newton_center([mpf(x.numerator) / x.denominator for x in cc])
        Yk = Jc ** -1
        Yk_iv = [[iv.mpf(Yk[i, j]) for j in range(3)] for i in range(3)]
        detY = iv_det3(Yk_iv)
        if lo(detY) <= 0 <= hi(detY):
            return {"ok": False, "why": "Yk singular?"}
        Csub = [iv.mpf([lo(ivq(a)), hi(ivq(b))]) for a, b in zip(clo, chi)]
        hc = self.h_point(phic)
        rho = [mpf(5) / 4 * sum(abs(Yk[i, j]) * mpf(hw[j].numerator) / hw[j].denominator
                                for j in range(3)) + mpf(2) ** -100 for i in range(3)]
        for attempt in range(10):
            Xb = [iv.mpf([phic[i] - rho[i], phic[i] + rho[i]]) for i in range(3)]
            J = self.jac_box(Xb)
            K, contr = [], mpf(0)
            for i in range(3):
                v = iv.mpf(phic[i]) - ivsum(Yk_iv[i][j] * (hc[j] + Csub[j]) for j in range(3))
                row = 0
                for j in range(3):
                    IJ = iv.mpf(int(i == j)) - ivsum(Yk_iv[i][l] * J[l][j] for l in range(3))
                    v += IJ * (Xb[j] - iv.mpf(phic[j]))
                    row += hi(ivabs_hi(IJ))
                contr = max(contr, row)
                K.append(v)
            if all(lo(K[i]) > lo(Xb[i]) and hi(K[i]) < hi(Xb[i]) for i in range(3)):
                break
            rho = [2 * max(rho[i], abs(lo(K[i]) - phic[i]), abs(hi(K[i]) - phic[i])) for i in range(3)]
        else:
            return {"ok": False, "why": "Krawczyk did not verify"}
        # Loewner sandwich on Xb
        q = self.q_box(Xb)
        qhi = [hi(x) for x in q]
        qlo = [lo(x) for x in q]
        Nhi = [[ivsum(iv.mpf(qhi[a]) * (S[a][k] * S[a][l]) for a in range(NS) if S[a][k] * S[a][l])
                for l in range(4)] for k in range(4)]
        mlo = [lo(ivsum(iv.mpf(qlo[a]) * S[a][k] for a in range(NS) if S[a][k])) for k in range(4)]
        if min(mlo) <= 0:
            return {"ok": False, "why": "mhat lower bound <= 0"}
        Ninv = iv_inverse(Nhi)
        M = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                acc = ivsum(self.B[k][i] * Ninv[k][l] * self.B[l][j] for k in range(4) for l in range(4))
                acc -= ivsum(iv.mpf(self.B[k][i] * self.B[k][j]) / (2 * iv.mpf(mlo[k])) for k in range(4))
                M[i][j] = acc - self.Xmin_iv[i][j]
        gersh = min(lo(M[i][i] - ivsum(ivabs_hi(M[i][j]) for j in range(3) if j != i)) for i in range(3))
        minors = [lo(M[0][0]), lo(M[0][0] * M[1][1] - M[0][1] * M[1][0]), lo(iv_det3(M))]
        tau = max(sum(abs(self.BtS[a][i]) * rho[i] for i in range(3)) for a in range(NS))
        return {"ok": gersh > 0 and min(minors) > 0, "gersh": gersh, "minors": minors,
                "rho": rho, "contraction": contr, "tau": tau,
                "phi_abs_max": max(max(abs(lo(x)), abs(hi(x))) for x in Xb)}


def check_Q(ex, nc):
    qc = QCheck(ex)
    gamma = ex["gamma"]
    res = {"subboxes": nc ** 3, "failed": 0, "min_gershgorin": None, "min_sylvester_minor": None,
           "max_krawczyk_rho": [0.0] * 3, "max_contraction": 0.0, "max_tau": 0.0, "max_abs_phi": 0.0}
    for idx in itertools.product(range(nc), repeat=3):
        clo = [-gamma[i] + 2 * gamma[i] * Fr(idx[i], nc) for i in range(3)]
        chi = [-gamma[i] + 2 * gamma[i] * Fr(idx[i] + 1, nc) for i in range(3)]
        r = qc.check_subbox(clo, chi)
        if not r["ok"]:
            res["failed"] += 1
            res.setdefault("failures", []).append({"idx": idx, **{k: str(v) for k, v in r.items()}})
            continue
        g, mn = r["gersh"], min(r["minors"])
        res["min_gershgorin"] = g if res["min_gershgorin"] is None else min(res["min_gershgorin"], g)
        res["min_sylvester_minor"] = mn if res["min_sylvester_minor"] is None else min(res["min_sylvester_minor"], mn)
        res["max_krawczyk_rho"] = [max(a, float(b)) for a, b in zip(res["max_krawczyk_rho"], r["rho"])]
        res["max_contraction"] = max(res["max_contraction"], float(r["contraction"]))
        res["max_tau"] = max(res["max_tau"], float(r["tau"]))
        res["max_abs_phi"] = max(res["max_abs_phi"], float(r["phi_abs_max"]))
    res["pass"] = res["failed"] == 0 and res["min_gershgorin"] is not None and res["min_gershgorin"] > 0
    for key in ("min_gershgorin", "min_sylvester_minor"):
        if res[key] is not None:   # rigorous lower bounds, rounded DOWN to 1e-9 for printing
            res[key] = floor_str(res[key])
    return res


def floor_str(x, digits=9):
    n = int(mpmath.floor(x * 10 ** digits))
    return f"{n // 10 ** digits}.{n % 10 ** digits:0{digits}d}" if n >= 0 else f"-{(-n) / 10 ** digits:.{digits}f}"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--r0", default="1/10000")
    ap.add_argument("--eps", default="3/20")
    ap.add_argument("--nc", type=int, default=8)
    ap.add_argument("--prec", type=int, default=128)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    assert a.prec >= 128
    iv.prec = a.prec
    mp.prec = a.prec
    r0, eps = Fr(a.r0), Fr(a.eps)
    t0 = time.time()
    ex = exact_objects(r0, eps)
    ident = log_coeffs_identity()
    t1 = time.time()
    resC = check_C(ex, r0)
    t2 = time.time()
    mp.prec = a.prec
    resQ = check_Q(ex, a.nc)
    t3 = time.time()
    Yvals = sorted({x for row in ex["Y"] for x in row})
    out = {
        "checker": "B (mpmath.iv + fractions), central box",
        "params": {"r0": fr_str(r0), "eps": fr_str(eps), "NC": a.nc, "iv_prec_bits": a.prec},
        "identities": {
            "Ubar0_equals_Lstar_coeffs_ln2_ln3_ln5": ident,
            "sum_u_a_u_zero": True, "sum_u_l_u_zero": True, "Rbar_equals_B_Xmin_inv_Bt": True,
            "R0_rows_sum_zero": True, "Phi_sum_equals_closed_form_7_7": True, "num_spectra": NS},
        "exact_objects": {
            "W2_eigs_on_1_r_t_rt": ex["W2_eigs_1_r_t_rt"],
            "X0_diag": [fr_str(ex["X0"][i][i]) for i in range(3)],
            "X0_offdiag_zero": all(ex["X0"][i][j] == 0 for i in range(3) for j in range(3) if i != j),
            "Xmin_diag": [fr_str(ex["Xmin"][i][i]) for i in range(3)],
            "R0_row0": [fr_str(x) for x in ex["R0"][0]],
            "Y_distinct_entries": [fr_str(x) for x in Yvals],
            "gamma": [fr_str(g) for g in ex["gamma"]],
            "gamma_float": [float(g) for g in ex["gamma"]],
            "nlo_min": fr_str(min(ex["nlo"])),
        },
        "C": resC,
        "Q": resQ,
        "PASS": bool(resC["pass"] and resQ["pass"]),
        "margin_statement": (f"ln F(n) <= L* - (delta/2)|eta|_2^2 on B0 with delta = {resC['delta_rigorous']}"),
        "runtime_s": {"exact": round(t1 - t0, 3), "C": round(t2 - t1, 3), "Q": round(t3 - t2, 3),
                      "total": round(t3 - t0, 3)},
        "max_rss_MiB": round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20, 1),
        "versions": {"python": sys.version.split()[0], "mpmath": mpmath.__version__,
                     "mpmath_backend": mpmath.libmp.BACKEND, "platform": platform.platform()},
        "script_sha256": {os.path.basename(p): sha256(p) for p in
                          (os.path.abspath(__file__),
                           os.path.join(os.path.dirname(os.path.abspath(__file__)), "cb_common.py"))},
    }
    txt = json.dumps(out, indent=1)
    print(txt)
    if a.out:
        with open(a.out, "w") as f:
            f.write(txt + "\n")
    return 0 if out["PASS"] else 1


if __name__ == "__main__":
    sys.exit(main())

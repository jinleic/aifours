#!/usr/bin/env python3
"""reviewer-f126-impulse-chain-repair-exact-diagnostics-v1.py

Same-harness reviewer diagnostics for review wave
f126-hinf-impulse-chain-repair-gate (author addendum repair gate for the
stochastic impulse-chain necessary gain bound).

Own code, written for this review. No author code is imported or executed.
No Monte Carlo. Exact Fractions / free-algebra checks where the object is
algebraic; mpmath 30-digit deterministic quadrature where a Gaussian
expectation is needed. Diagnostics illustrate and cross-check the written
arguments; they are NOT proofs of the theorem.

Sections
  D1  free-algebra (noncommutative) check of the Ito variation-of-constants
      identity with the -Qg correction, of the inverse-flow SDE, and of the
      Doss-Sussmann dt/dW coefficient identity; no commutation rule exists
      in the free algebra, so none can be used.
  D2  control: the naive "commuting" closed form exp(QW_t+(P-Q^2/2)t) gives
      the WRONG mean for noncommuting P,Q (exact rational series) while the
      Ito flow mean is exactly exp(Pt).
  D3  exact window covariance bookkeeping (|Cov(xi_j^eps,W_t)|<=sqrt(eps),
      zero covariance with the deleted-increment Brownian motion, paused
      clock values, admissibility of the last window).
  D4  h=0 scalar example: L(1)=E sqrt(1+xi^2) by three deterministic
      routes; exact finite-eps second-moment identities for P=Q=0 and for
      Q=q!=0 (closed form vs high-precision ODE); exact in-window state
      increment error E|x_eps(eps)-xi^eps|^2.
  D5  Q=0 impulse functionals with exact Gram matrices (Fractions) and the
      1-D s-integral; includes the candidate's hypothesis-failing/weakened-
      condition-holding instances, a negative control with alpha_j=0, and an
      h>0 chain with Gh!=0 (endpoint impulse at t_n<T).
  D6  genuinely noncommuting P,Q with Q!=0 (3x3 strictly upper triangular):
      exact polynomial Lyapunov second moments via the nilpotent Kronecker
      generator, cross-checked against the explicit Ito solution and against
      the Doss-Sussmann representation evaluated formally; RMS/Jensen
      sandwich for L.
  D7  exact endpoint geometry: n=ceil(S/h), t_n<T, admissible eps range,
      disjointness, paused horizon.
"""
import sys, json, hashlib, platform, math
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 30
OUT = {"schema": 1, "review_id": "f126-hinf-impulse-chain-repair-gate",
       "python": platform.python_version(), "mpmath": mp.__version__,
       "platform": platform.platform(), "monte_carlo_used": False,
       "author_code_used": False}
with open(__file__, 'rb') as fh:
    OUT["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()


def S(x, d=25):
    """string of an mpf with d significant digits"""
    return mp.nstr(x, d)


# ----------------------------------------------------------------------------
# tiny exact linear algebra over Fractions
# ----------------------------------------------------------------------------
def mat(rows):
    return [[Fr(v) for v in r] for r in rows]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m):
    return [[Fr(0)] * m for _ in range(n)]


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][l] * B[l][j] for l in range(k)) for j in range(m)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    return [[Fr(c) * v for v in r] for r in A]


def mT(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def is_zero(A):
    return all(v == 0 for r in A for v in r)


def kron(A, B):
    n, m = len(A), len(A[0])
    p, q = len(B), len(B[0])
    K = zeros(n * p, m * q)
    for i in range(n):
        for j in range(m):
            for k in range(p):
                for l in range(q):
                    K[i * p + k][j * q + l] = A[i][j] * B[k][l]
    return K


def mstr(A):
    return [[str(v) for v in r] for r in A]


# ----------------------------------------------------------------------------
# D1: free algebra check of the Ito identities (no commutation possible)
# ----------------------------------------------------------------------------
class NC:
    """noncommutative polynomial with Fraction coefficients; words are tuples"""

    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def sym(s):
        return NC({(s,): Fr(1)})

    @staticmethod
    def one():
        return NC({(): Fr(1)})

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, Fr(0)) + v
        return NC(d)

    def __neg__(self):
        return NC({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

    def scale(self, c):
        return NC({k: v * Fr(c) for k, v in self.d.items()})

    def __mul__(self, o):
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                k = k1 + k2
                d[k] = d.get(k, Fr(0)) + v1 * v2
        return NC(d)

    def is_zero(self):
        return len(self.d) == 0

    def cancel(self, a, ainv):
        """rewrite with a*ainv = ainv*a = 1 (adjacent pairs only)"""
        d = dict(self.d)
        changed = True
        while changed:
            changed = False
            nd = {}
            for k, v in d.items():
                kk = list(k)
                i = 0
                while i < len(kk) - 1:
                    if (kk[i], kk[i + 1]) in ((a, ainv), (ainv, a)):
                        del kk[i:i + 2]
                        changed = True
                        i = max(i - 1, 0)
                    else:
                        i += 1
                kk = tuple(kk)
                nd[kk] = nd.get(kk, Fr(0)) + v
            d = {k: v for k, v in nd.items() if v != 0}
        return NC(d)

    def __repr__(self):
        if not self.d:
            return "0"
        return " + ".join(f"({v})*{'.'.join(k) if k else '1'}" for k, v in sorted(self.d.items()))


def D1():
    P, Q, Psi, F, x, f, g, Z, E, Einv = [NC.sym(s) for s in
                                          ['P', 'Q', 'Psi', 'F', 'x', 'f', 'g', 'Z', 'E', 'Einv']]
    # postulated inverse-flow SDE: dPsi = Psi((QQ-P)dt - Q dW)
    dPsi_dt = Psi * (Q * Q - P)
    dPsi_dW = -(Psi * Q)
    # state SDE: dx = (Px+f)dt + (Qx+g)dW
    dx_dt, dx_dW = P * x + f, Q * x + g
    # flow SDE: dF = PF dt + QF dW
    dF_dt, dF_dW = P * F, Q * F
    # Ito product rule: d(AB) = dA B + A dB + dA_dW dB_dW dt
    prod_dt = dPsi_dt * x + Psi * dx_dt + dPsi_dW * dx_dW
    prod_dW = dPsi_dW * x + Psi * dx_dW
    target_dt = Psi * f - Psi * Q * g      # addendum (1): Psi (f - Q g)
    target_dW = Psi * g
    inv_dt = dPsi_dt * F + Psi * dF_dt + dPsi_dW * dF_dW
    inv_dW = dPsi_dW * F + Psi * dF_dW
    # Doss-Sussmann: F = E Z with E = exp(QW): dE = QE dW + (1/2)QQE dt (one-parameter group),
    # dZ = Einv (P - QQ/2) E Z dt. dt-coefficient of dF must be P E Z, dW-coefficient Q E Z.
    ds_dt = (Q * Q * E * Z).scale(Fr(1, 2)) + E * (Einv * (P - (Q * Q).scale(Fr(1, 2))) * E * Z)
    ds_dW = Q * E * Z
    res = {
        "d(Psi x)_dt_equals_Psi(f-Qg)": (prod_dt - target_dt).is_zero(),
        "d(Psi x)_dW_equals_Psi_g": (prod_dW - target_dW).is_zero(),
        "residual_if_-Qg_dropped": repr(prod_dt - Psi * f),
        "d(Psi F)_dt_zero": inv_dt.is_zero(),
        "d(Psi F)_dW_zero": inv_dW.is_zero(),
        "DS_dt_coefficient_equals_P_E_Z_after_EEinv_cancel": (ds_dt - P * E * Z).cancel('E', 'Einv').is_zero(),
        "DS_dt_coefficient_without_cancel_is_nonzero(as expected)": not (ds_dt - P * E * Z).is_zero(),
        "DS_dW_coefficient_equals_Q_E_Z": (ds_dW - Q * E * Z).is_zero(),
        "PQ_minus_QP_is_nonzero_word_in_free_algebra": not (P * Q - Q * P).is_zero(),
        "note": "free algebra has no commutation rule; the identities hold word-by-word, so no P,Q commutation is used anywhere",
    }
    # concrete noncommuting rational matrices: same identities coefficientwise
    Pm = mat([[0, 1], [0, 0]])
    Qm = mat([[0, 0], [1, 0]])
    comm = msub(mmul(Pm, Qm), mmul(Qm, Pm))
    res["concrete_P=E12_Q=E21_commutator"] = mstr(comm)
    res["concrete_commutator_nonzero"] = not is_zero(comm)
    # with concrete numbers the dt identity reduces to Psi[(QQ-P)x + Px + f - Q(Qx+g)] = Psi(f-Qg): check
    Psim = mat([[3, Fr(-1, 2)], [Fr(2, 7), 5]])
    xv, fv, gv = mat([[2], [-3]]), mat([[Fr(1, 3)], [4]]), mat([[-5], [Fr(7, 2)]])
    lhs = mmul(Psim, madd(madd(mmul(msub(mmul(Qm, Qm), Pm), xv), madd(mmul(Pm, xv), fv)),
                          mscale(-1, mmul(Qm, madd(mmul(Qm, xv), gv)))))
    rhs = mmul(Psim, msub(fv, mmul(Qm, gv)))
    res["concrete_dt_identity_holds"] = is_zero(msub(lhs, rhs))
    return res


OUT["D1_free_algebra_variation_of_constants"] = D1()


# ----------------------------------------------------------------------------
# D2: naive commuting formula fails for noncommuting P,Q (exact series)
# ----------------------------------------------------------------------------
def D2():
    # P=E12, Q=E21 (2x2), Q^2=0. Ito flow: E F_t = exp(Pt) = I + Pt (exact).
    # naive: F_naive = exp(Q W_t + (P - Q^2/2) t) = exp(N), N = [[0,t],[W,0]], N^2 = tW I.
    # (1,1) entry of E F_naive(t) = sum_k (2k-1)!! t^{3k} / (4k)!   (exact rational partial sums)
    # (1,2) entry = sum_k (2k-1)!! t^{3k+1} / (4k+1)!
    def dfact(m):  # (m)!! for odd m, with (-1)!! = 1
        r = 1
        while m > 1:
            r *= m
            m -= 2
        return r
    t = Fr(1)
    s11 = [Fr(dfact(2 * k - 1) * t ** (3 * k), math.factorial(4 * k)) for k in range(0, 8)]
    s12 = [Fr(dfact(2 * k - 1) * t ** (3 * k + 1), math.factorial(4 * k + 1)) for k in range(0, 8)]
    p11 = sum(s11)
    p12 = sum(s12)
    # tail bound: terms for k>=8 are < term_8 * sum of geometric ratio <= 2*term_8
    tail11 = 2 * Fr(dfact(15) * t ** 24, math.factorial(32))
    return {
        "t": str(t),
        "Ito_mean_exp(Pt)_entries_(11,12)": ["1", str(t)],
        "naive_mean_(11)_partial_sum_k<=7": str(p11),
        "naive_mean_(11)_float": float(p11),
        "naive_mean_(11)_tail_upper_bound": float(tail11),
        "naive_mean_(12)_partial_sum_k<=7": str(p12),
        "naive_mean_(12)_float": float(p12),
        "naive_(11)_minus_Ito_(11)_lower_bound": float(p11 - 1),
        "first_correction_term_(11)": str(s11[1]),
        "conclusion": "exp(QW+(P-Q^2/2)t) is NOT the Ito flow when PQ!=QP; the Doss-Sussmann ODE form Z'=e^{-QW}(P-Q^2/2)e^{QW}Z (addendum section 3) is the device that avoids commutation",
    }


OUT["D2_naive_commuting_formula_control"] = D2()


# ----------------------------------------------------------------------------
# D3: exact window covariance bookkeeping
# ----------------------------------------------------------------------------
def D3():
    h, T, eps = Fr(1), Fr(5, 2), Fr(1, 10)
    Sh = T - h
    n = -(-Sh // h)  # ceil
    n = int(n)
    tj = [j * h for j in range(n + 1)]
    wins = [(t, t + eps) for t in tj]

    def meas_cap(a, b, c, d):  # |[a,b] cap [c,d]|
        lo, hi = max(a, c), min(b, d)
        return max(Fr(0), hi - lo)

    grid = [Fr(k, 40) * T for k in range(41)]
    maxcov_scaled = Fr(0)   # sqrt(eps)*Cov(xi_j, W_t) = |[0,t] cap I_j| / eps ... we report |[0,t] cap I_j| <= eps
    for t in grid:
        for (a, b) in wins:
            maxcov_scaled = max(maxcov_scaled, meas_cap(Fr(0), t, a, b))
    # deleted-increment BM: Cov(V_t, xi_j^eps) * sqrt(eps) = |[0,t] cap Off cap I_j|, with Off = union of the
    # explicit off-window intervals J_k = [t_k+eps, t_{k+1}) (k<n), J_n = [t_n+eps, T]
    offs = [(tj[k] + eps, tj[k + 1]) for k in range(n)] + [(tj[n] + eps, T)]
    off_cap = Fr(0)
    partition_ok = True
    for t in grid:
        for (a, b) in wins:
            for (c_, d_) in offs:
                lo, hi = max(a, c_, Fr(0)), min(b, d_, t)
                off_cap = max(off_cap, max(Fr(0), hi - lo))
        tot = sum(meas_cap(Fr(0), t, a, b) for (a, b) in wins) + sum(meas_cap(Fr(0), t, a, b) for (a, b) in offs)
        partition_ok = partition_ok and (tot == t)
    # paused clock c(t) = t - |[0,t] cap Win|
    def c(t):
        return t - sum(meas_cap(Fr(0), t, a, b) for (a, b) in wins)
    rj = [c(t) for t in tj]
    rj_end = [c(t + eps) for t in tj]
    Tbar = c(T)
    return {
        "h": str(h), "T": str(T), "S": str(Sh), "n": n, "eps": str(eps),
        "windows": [[str(a), str(b)] for a, b in wins],
        "max_over_grid_|[0,t] cap I_j| (=sqrt(eps)*|Cov(xi_j^eps,W_t)|)": str(maxcov_scaled),
        "bound_eps": str(eps), "addendum_bound_holds_|Cov|<=sqrt(eps)": maxcov_scaled <= eps,
        "off_window_intervals_J_k": [[str(a), str(b)] for a, b in offs],
        "max_over_grid_|[0,t] cap I_j cap J_k| (=sqrt(eps)*|Cov(V_t,xi_j^eps)|, f120 Step 4)": str(off_cap),
        "windows_and_off_intervals_partition_[0,t]_on_grid": partition_ok,
        "paused_clock_c(t_j)": [str(v) for v in rj],
        "paused_clock_c(t_j+eps)": [str(v) for v in rj_end],
        "formula_jh-j*eps": [str(j * h - j * eps) for j in range(n + 1)],
        "c(t_j)==c(t_j+eps)==jh-j*eps": all(rj[j] == rj_end[j] == j * h - j * eps for j in range(n + 1)),
        "Tbar=T-(n+1)eps": str(Tbar), "Tbar_check": Tbar == T - (n + 1) * eps,
        "r_n<=Tbar iff nh+eps<=T": (rj[n] <= Tbar) == (n * h + eps <= T),
        "r_n<=Tbar": rj[n] <= Tbar,
    }


OUT["D3_window_covariance_and_clock"] = D3()


# ----------------------------------------------------------------------------
# Gaussian expectation helpers (deterministic, high precision)
# ----------------------------------------------------------------------------
def E_sqrt_c2_plus_lam_xi2_direct(c, lam):
    """E sqrt(c^2 + lam xi^2), xi~N(0,1), direct Gaussian quadrature"""
    f = lambda x: mp.sqrt(c * c + lam * x * x) * mp.exp(-x * x / 2) / mp.sqrt(2 * mp.pi)
    return mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf])


def E_sqrt_c2_plus_lam_xi2_bessel(c, lam):
    """closed form (own derivation, x = k sinh u): sqrt(lam) k^2 e^{k^2/4}[K0(k^2/4)+K1(k^2/4)]/(2 sqrt(2 pi)), k^2=c^2/lam"""
    k2 = c * c / lam
    z = k2 / 4
    return mp.sqrt(lam) * k2 * mp.exp(z) * (mp.besselk(0, z) + mp.besselk(1, z)) / (2 * mp.sqrt(2 * mp.pi))


def E_sqrt_quadform(c2, M):
    """E sqrt(c2 + xi^T M xi), M symmetric PSD (list of Fractions), via
    sqrt(y) = (2 sqrt(pi))^{-1} int_0^inf s^{-3/2} (1 - e^{-s y}) ds and the Gaussian mgf
    E e^{-s xi^T M xi} = det(I+2sM)^{-1/2}."""
    n = len(M)
    # det(I + 2sM) = sum_k e_k (2s)^k with e_k = sum of kxk principal minors, computed EXACTLY in Fractions
    def det_exact(A):
        m = len(A)
        if m == 0:
            return Fr(1)
        if m == 1:
            return A[0][0]
        tot = Fr(0)
        for j in range(m):
            minor = [[A[i][l] for l in range(m) if l != j] for i in range(1, m)]
            tot += (-1) ** j * A[0][j] * det_exact(minor)
        return tot
    from itertools import combinations
    e = [Fr(0)] * (n + 1)
    for k in range(n + 1):
        for idx in combinations(range(n), k):
            e[k] += det_exact([[M[i][j] for j in idx] for i in idx])
    assert e[0] == 1
    em = [mp.mpf(v.numerator) / v.denominator for v in e]
    c2m = mp.mpf(c2.numerator) / c2.denominator
    trM = em[1]

    def rest(u):
        # e^{-s c^2} det(I+2sM)^{-1/2} with s=u^2
        s = u * u
        det = sum(em[k] * (2 * s) ** k for k in range(n + 1))
        return mp.exp(-s * c2m) / mp.sqrt(det)

    def integrand_u(u):
        # s = u^2, ds = 2u du, s^{-3/2} ds = 2 u^{-2} du; integrand is bounded at u=0
        if u == 0:
            return 2 * (c2m + trM)
        return 2 * (1 - rest(u)) / (u * u)
    U = mp.mpf(32)
    with mp.workdps(45):
        head = mp.quad(integrand_u, [0, mp.mpf(1) / 8, mp.mpf(1) / 2, 1, 2, 4, 8, 16, U])
        tail_main = 2 / U                      # int_U^inf 2/u^2 du exactly
        tail_rest = mp.quad(lambda u: 2 * rest(u) / (u * u), [U, 2 * U, mp.inf])
        val = head + tail_main - tail_rest
    return +val / (2 * mp.sqrt(mp.pi))


def trace(M):
    return sum(M[i][i] for i in range(len(M)))


# ----------------------------------------------------------------------------
# D4: h=0 scalar example, exact finite-eps identities
# ----------------------------------------------------------------------------
def D4():
    one = mp.mpf(1)
    L_direct = E_sqrt_c2_plus_lam_xi2_direct(one, one)
    L_bessel = E_sqrt_c2_plus_lam_xi2_bessel(one, one)
    L_sint = E_sqrt_quadform(Fr(1), [[Fr(1)]])
    simple_lb = 1 + (mp.sqrt(2) - 1) * mp.erfc(1 / mp.sqrt(2))   # author LF61: 1+(sqrt2-1)P(|xi|>=1)
    res = {
        "L(1)=E sqrt(1+xi^2)_direct_quadrature": S(L_direct),
        "L(1)_bessel_closed_form": S(L_bessel),
        "L(1)_s_integral": S(L_sint),
        "max_pairwise_abs_diff": S(max(abs(L_direct - L_bessel), abs(L_direct - L_sint), abs(L_bessel - L_sint)), 5),
        "author_simple_lower_bound_1+(sqrt2-1)P(|xi|>=1)": S(simple_lb),
        "RMS_proxy_sqrt(E(1+xi^2))=sqrt2": S(mp.sqrt(2)),
        "strict_L>1": L_direct > 1, "strict_L<RMS(Jensen, nonconstant energy)": L_direct < mp.sqrt(2),
        "direct_atom_threshold_delta": "1",
    }
    # finite-eps, P=Q=0: x_eps(t) = eps^{-1/2} W_{t wedge eps}; exact E||z_eps||^2 = 2 - eps/2
    def Ez2_PQ0(eps):
        # E int_0^eps (eps^{-1/2}(1+W_t))^2 dt + E int_eps^1 eps^{-1} W_eps^2 dt
        return (1 + eps / 2) + (1 - eps)
    res["finite_eps_P=Q=0_E||z_eps||^2_exact"] = {str(e): str(Ez2_PQ0(e)) for e in [Fr(1, 10), Fr(1, 25), Fr(1, 100)]}
    res["finite_eps_P=Q=0_formula"] = "2 - eps/2 -> 2 = c^2 + G^2 T (RMS^2 of the limit)"
    # independent route: moment ODE with q=0 (u' = 1/eps on [0,eps], u'=0 after; y' = u + 1/eps, then u)
    def Ez2_q0_ode(eps):
        f1 = lambda t, Y: [1 / eps, Y[0] + 1 / eps]
        u_e, y_e = mp.odefun(f1, 0, [mp.mpf(0), mp.mpf(0)])(eps)
        f2 = lambda t, Y: [mp.mpf(0), Y[0]]
        return mp.odefun(f2, eps, [u_e, y_e])(1)[1]
    res["finite_eps_P=Q=0_ode_cross_check"] = {str(e): {"ode": S(Ez2_q0_ode(mp.mpf(e.numerator) / e.denominator), 20),
                                                       "exact": str(Ez2_PQ0(e)),
                                                       "abs_diff": S(abs(Ez2_q0_ode(mp.mpf(e.numerator) / e.denominator) - mp.mpf(Ez2_PQ0(e).numerator) / Ez2_PQ0(e).denominator), 5)}
                                               for e in [Fr(1, 10), Fr(1, 25), Fr(1, 100)]}

    # finite-eps with Q=q (dx = q x dW + w dW, z = x + w, h=0, T=1, pulse eps^{-1/2} on [0,eps])
    def Ez2_q_closed(eps, q):
        q2 = q * q
        return 1 + (mp.exp(q2 * eps) - 1 - q2 * eps) / (q2 * q2 * eps) \
            + (mp.exp(q2 * eps) - 1) * (mp.exp(q2 * (1 - eps)) - 1) / (q2 * q2 * eps)

    def Ez2_q_ode(eps, q):
        # u=E x^2: u' = q^2 u + 1/eps on [0,eps], u' = q^2 u on [eps,1]; y' = E z^2 = u + 1/eps on [0,eps], u on [eps,1]
        q2 = q * q
        f1 = lambda t, Y: [q2 * Y[0] + 1 / eps, Y[0] + 1 / eps]
        sol1 = mp.odefun(f1, 0, [mp.mpf(0), mp.mpf(0)])
        u_e, y_e = sol1(eps)
        f2 = lambda t, Y: [q2 * Y[0], Y[0]]
        sol2 = mp.odefun(f2, eps, [u_e, y_e])
        return sol2(1)[1]

    q = mp.mpf(1)
    tab = {}
    for e in [mp.mpf(1) / 10, mp.mpf(1) / 25, mp.mpf(1) / 100]:
        a, b = Ez2_q_closed(e, q), Ez2_q_ode(e, q)
        # addendum (3) remainder, scalar inverse flow Psi_s = exp(-qW_s + q^2 s/2):
        # E|error|^2 = eps^{-1} int_0^eps E(Psi_s - 1)^2 ds, E(Psi_s-1)^2 = e^{3q^2 s} - 2e^{q^2 s} + 1 (exact Gaussian mgf)
        q2 = q * q
        err3_closed = ((mp.exp(3 * q2 * e) - 1) / (3 * q2) - 2 * (mp.exp(q2 * e) - 1) / q2 + e) / e
        err3_quad = mp.quad(lambda t: mp.exp(3 * q2 * t) - 2 * mp.exp(q2 * t) + 1, [0, e]) / e
        tab[S(e, 6)] = {"closed_form": S(a, 20), "ode_cross_check": S(b, 20), "abs_diff": S(abs(a - b), 5),
                        "in_window_increment_error_E|x_eps(eps)-xi^eps|^2=(e^{q^2 eps}-1)/(q^2 eps)-1": S((mp.exp(q * q * e) - 1) / (q * q * e) - 1, 12),
                        "q^2 eps/2 (leading order)": S(q * q * e / 2, 12),
                        "addendum_(3)_E|error_0|^2_closed": S(err3_closed, 12), "addendum_(3)_E|error_0|^2_quad": S(err3_quad, 12),
                        "ratio_to_eps": S(err3_closed / e, 8)}
    res["finite_eps_Q=1_P=0"] = tab
    res["finite_eps_Q=1_P=0_note"] = "E|error_0|^2/eps -> q^2/2 = 1/2: the inverse-flow stochastic-integral remainder of addendum (3) is O(eps) in this exact scalar instance"
    limit_rms2 = 1 + (mp.exp(q * q) - 1) / (q * q)
    EA = (mp.exp(q * q) - 1) / (q * q)
    phi_EA = E_sqrt_c2_plus_lam_xi2_bessel(one, EA)
    res["finite_eps_Q=1_limit_E||z||^2 -> 1+(e^{q^2}-1)/q^2"] = S(limit_rms2)
    res["Q=1_limit_L_sandwich"] = {
        "lower_strict": "1 (A=int_0^1 e^{2qW-q^2 t}dt>0 a.s. => P(alpha>0)=1 => L>1)",
        "upper_Jensen_in_A: E_xi sqrt(1+xi^2 E A)": S(phi_EA),
        "upper_RMS: sqrt(1+E A)": S(mp.sqrt(limit_rms2)),
        "ordering_holds": bool(1 < phi_EA < mp.sqrt(limit_rms2)),
        "note": "L itself for q!=0 needs the law of int e^{2qW-q^2t}dt (no elementary closed form); not computed, not claimed",
    }
    return res


OUT["D4_h0_scalar_example_exact"] = D4()


# ----------------------------------------------------------------------------
# D5: Q=0 impulse functionals with exact Gram matrices
# ----------------------------------------------------------------------------
def poly_mul(p, q):
    r = {}
    for i, a in p.items():
        for j, b in q.items():
            r[i + j] = r.get(i + j, Fr(0)) + a * b
    return r


def poly_add(p, q):
    r = dict(p)
    for j, b in q.items():
        r[j] = r.get(j, Fr(0)) + b
    return r


def poly_shift_pow(k, tj):
    """(t - tj)^k as polynomial in t"""
    r = {0: Fr(1)}
    base = {0: -Fr(tj), 1: Fr(1)}
    for _ in range(k):
        r = poly_mul(r, base)
    return r


def poly_int(p, lo, hi):
    return sum(c * (Fr(hi) ** (k + 1) - Fr(lo) ** (k + 1)) / (k + 1) for k, c in p.items())


def nilpotent_index(P):
    n = len(P)
    A = eye(n)
    for k in range(n + 1):
        if is_zero(A):
            return k
        A = mmul(A, P)
    return None


def impulse_gram(P, O, Gs, ts, T):
    """Q=0: M_jk = int_{max(tj,tk)}^T <O e^{P(t-tj)} G_j, O e^{P(t-tk)} G_k> dt exactly (P nilpotent)"""
    d = len(P)
    nil = nilpotent_index(P)
    assert nil is not None, "P must be nilpotent for exact polynomial flow"
    # v_j(t) = sum_k (O P^k G_j)/k! (t-tj)^k  (vector of polynomials)
    def vj(G, tj):
        comps = [dict() for _ in range(len(O))]
        Pk = eye(d)
        for k in range(nil):
            OPkG = mmul(O, mmul(Pk, G))  # p x 1
            sh = poly_shift_pow(k, tj)
            for i in range(len(O)):
                comps[i] = poly_add(comps[i], {e: c * OPkG[i][0] / math.factorial(k) for e, c in sh.items()})
            Pk = mmul(Pk, P)
        return comps
    V = [vj(G, tj) for G, tj in zip(Gs, ts)]
    m = len(Gs)
    M = zeros(m, m)
    for j in range(m):
        for k in range(m):
            lo = max(ts[j], ts[k])
            tot = Fr(0)
            for i in range(len(O)):
                tot += poly_int(poly_mul(V[j][i], V[k][i]), lo, T)
            M[j][k] = tot
    return M


def D5():
    res = {}
    # S1: candidate h=0 example: P=0 (1x1), O=1, G=1, c=1, T=1
    M = impulse_gram(mat([[0]]), mat([[1]]), [mat([[1]])], [Fr(0)], Fr(1))
    res["S1_candidate_example"] = {"M": mstr(M), "L": S(E_sqrt_quadform(Fr(1), M))}
    # NC3-type: O=[1,0], P=[[0,1],[0,0]], G=(0,1), c=1, T=1: OG=0 but O e^{Pt} G = t, alpha=1/3
    P = mat([[0, 1], [0, 0]]); O = mat([[1, 0]]); G = mat([[0], [1]])
    M = impulse_gram(P, O, [G], [Fr(0)], Fr(1))
    L = E_sqrt_quadform(Fr(1), M)
    Lb = E_sqrt_c2_plus_lam_xi2_bessel(mp.mpf(1), mp.mpf(1) / 3)
    res["N3_OG=0_but_OPG!=0"] = {"OG": mstr(mmul(O, G)), "OPG": mstr(mmul(O, mmul(P, G))), "M=alpha": mstr(M),
                                 "L_s_integral": S(L), "L_bessel": S(Lb), "abs_diff": S(abs(L - Lb), 5),
                                 "gap_L>c=1": L > 1}
    # NEW N1: 3-dim shift, OG=OPG=0, OP^2G!=0: O e^{Pt}G = t^2/2, alpha = 1/20
    P3 = mat([[0, 1, 0], [0, 0, 1], [0, 0, 0]]); O3 = mat([[1, 0, 0]]); G3 = mat([[0], [0], [1]])
    M = impulse_gram(P3, O3, [G3], [Fr(0)], Fr(1))
    L = E_sqrt_quadform(Fr(1), M)
    Lb = E_sqrt_c2_plus_lam_xi2_bessel(mp.mpf(1), mp.mpf(1) / 20)
    res["N1_OG=OPG=0_OP2G!=0"] = {"OG": mstr(mmul(O3, G3)), "OPG": mstr(mmul(O3, mmul(P3, G3))),
                                 "OP2G": mstr(mmul(O3, mmul(P3, mmul(P3, G3)))), "M=alpha": mstr(M),
                                 "L_s_integral": S(L), "L_bessel": S(Lb), "abs_diff": S(abs(L - Lb), 5), "gap_L>c=1": L > 1}
    # NEW N0 negative control: G in the unobservable subspace: P=[[0,0],[1,0]], O=[1,0], G=(0,1): O P^k G = 0 for all k
    P0 = mat([[0, 0], [1, 0]]); O0 = mat([[1, 0]]); G0 = mat([[0], [1]])
    M = impulse_gram(P0, O0, [G0], [Fr(0)], Fr(1))
    L = E_sqrt_quadform(Fr(1), M)
    res["N0_negative_control_alpha=0"] = {"OG": mstr(mmul(O0, G0)), "OPG": mstr(mmul(O0, mmul(P0, G0))), "M=alpha": mstr(M),
                                          "L": S(L), "L_equals_c=1_to_1e-22": abs(L - 1) < mp.mpf(10) ** -22,
                                          "note": "weakened condition P(alpha>0)>0 fails; impulse functional gives NO gap, consistent with Prop 5.2 being sufficient only"}
    # f120 instance S2 (independent recomputation): h=1,T=5/2,n=2,E0=1,Eh=-1,O=1,G0=1,Gh=0,P=Q=0 (1-dim state), a=(1,-1)
    a = [Fr(1), Fr(-1)]
    D = [a[0], a[1] - a[0], -a[1]]  # E0 a_j + Eh a_{j-1}
    c2 = sum(v * v for v in D)
    Gs = [mat([[a[0]]]), mat([[a[1]]]), mat([[0]])]
    ts = [Fr(0), Fr(1), Fr(2)]
    M = impulse_gram(mat([[0]]), mat([[1]]), Gs, ts, Fr(5, 2))
    L = E_sqrt_quadform(c2, M)
    na = mp.sqrt(sum(v * v for v in a))
    res["S2_f120_instance_recomputed"] = {"D": [str(v) for v in D], "c^2": str(c2), "M": mstr(M),
                                          "L(a)/||a||": S(L / na), "delta=sqrt3": S(mp.sqrt(3)),
                                          "Jensen_RMS/||a||": S(mp.sqrt(c2 + trace(M)) / na),
                                          "c/||a||<=L/||a||<=RMS/||a||": bool(mp.sqrt(c2) / na <= L / na <= mp.sqrt(c2 + trace(M)) / na),
                                          "f120_reported": "2.18410369310628"}
    # NEW chain C1: h=1, T=5/2, n=2, state dim 2, P=[[0,1],[0,0]], O=[1,0], E0=1, Eh=-1, G0=(0,1), Gh=(0,1/2)
    # => OG_j=0 for all j (candidate (3) hypothesis fails) but alpha_j>0 (weakened condition); endpoint impulse at t_2=2<T with G_2=Gh a_1 != 0
    P = mat([[0, 1], [0, 0]]); O = mat([[1, 0]])
    G0v = mat([[0], [1]]); Ghv = mat([[0], [Fr(1, 2)]])
    a = [Fr(1), Fr(-1)]  # top singular direction of B_2 (delta = sqrt 3)
    am1 = [Fr(0)] + a + [Fr(0)]  # a_{-1}, a_0, a_1, a_2=0
    D = [am1[j + 1] - am1[j] for j in range(3)]  # E0 a_j + Eh a_{j-1} with E0=1, Eh=-1
    c2 = sum(v * v for v in D)
    Gs = [madd(mscale(am1[j + 1], G0v), mscale(am1[j], Ghv)) for j in range(3)]
    ts = [Fr(0), Fr(1), Fr(2)]
    M = impulse_gram(P, O, Gs, ts, Fr(5, 2))
    L = E_sqrt_quadform(c2, M)
    alphas = [str(M[j][j]) for j in range(3)]
    res["C1_new_chain_OGj=0_all_j_alpha_j>0_endpoint_G2!=0"] = {
        "D": [str(v) for v in D], "c^2": str(c2), "G_j": [mstr(mT(G))[0] for G in Gs],
        "OG_j": [mstr(mmul(O, G))[0] for G in Gs], "t_j": [str(t) for t in ts], "T": "5/2", "t_n<T": ts[-1] < Fr(5, 2),
        "M": mstr(M), "alpha_j=M_jj": alphas, "all_alpha_j>0": all(M[j][j] > 0 for j in range(3)),
        "L(a)/||a||": S(L / na), "delta=sqrt3": S(mp.sqrt(3)), "strict_gap_holds": L / na > mp.sqrt(3),
        "Jensen_RMS/||a||": S(mp.sqrt(c2 + trace(M)) / na), "L<RMS": L < mp.sqrt(c2 + trace(M)),
        "last_impulse_energy_share_alpha_2/(sum alpha)": str(M[2][2] / sum(M[j][j] for j in range(3))),
    }
    # C1 with the last impulse's visible horizon shrunk: T = 2 + 1/100 (S/h = 1.01, n=2, T-nh = 1/100)
    Tt = Fr(201, 100)
    M2 = impulse_gram(P, O, Gs, ts, Tt)
    L2 = E_sqrt_quadform(c2, M2)
    res["C1_short_endpoint_horizon_T=2.01"] = {"T": str(Tt), "S": str(Tt - 1), "n": 2, "T-nh": str(Tt - 2),
                                                 "admissible_eps_max=T-nh": str(Tt - 2), "M": mstr(M2),
                                                 "alpha_2": str(M2[2][2]), "L(a)/||a||": S(L2 / na), "strict_gap_holds": L2 / na > mp.sqrt(3),
                                                 "atom_c^2_unchanged": str(c2)}
    return res


OUT["D5_Q0_impulse_functionals_exact"] = D5()


# ----------------------------------------------------------------------------
# D6: noncommuting P,Q with Q != 0: exact Lyapunov second moments
# ----------------------------------------------------------------------------
def D6():
    P = mat([[0, 1, 0], [0, 0, 0], [0, 0, 0]])   # E12
    Q = mat([[0, 0, 0], [0, 0, 1], [0, 0, 0]])   # E23
    O = mat([[1, 0, 0]])
    G = mat([[0], [0], [1]])
    comm = msub(mmul(P, Q), mmul(Q, P))
    I3 = eye(3)
    K = madd(madd(kron(I3, P), kron(P, I3)), kron(Q, Q))   # vec(PM + MP^T + QMQ^T) = K vec(M)
    nil = nilpotent_index(K)
    # M(t) = exp(tK) vec(G G^T) as polynomial in t: sum_k t^k K^k/k! vec(GG^T)
    v0 = [[Fr(0)] for _ in range(9)]
    GG = mmul(G, mT(G))
    for i in range(3):
        for j in range(3):
            v0[j * 3 + i][0] = GG[i][j]   # column-major vec
    polys = [dict() for _ in range(9)]
    Kk = eye(9)
    for k in range(nil):
        vk = mmul(Kk, v0)
        for r in range(9):
            if vk[r][0] != 0:
                polys[r][k] = polys[r].get(k, Fr(0)) + vk[r][0] / math.factorial(k)
        Kk = mmul(Kk, K)
    def Mij(i, j):
        return polys[j * 3 + i]
    # hand solution: X3=xi, X2=xi W_t, X1=xi int_0^t W: M11=t^3/3, M12=t^2/2, M22=t, M33=1, others 0
    hand = {(0, 0): {3: Fr(1, 3)}, (0, 1): {2: Fr(1, 2)}, (1, 0): {2: Fr(1, 2)}, (1, 1): {1: Fr(1)}, (2, 2): {0: Fr(1)}}
    match = True
    for i in range(3):
        for j in range(3):
            p = {k: v for k, v in Mij(i, j).items() if v != 0}
            if p != hand.get((i, j), {}):
                match = False
    T = Fr(1)
    OMO = Mij(0, 0)  # O M O^T = M11
    EJ = poly_int(OMO, 0, T)   # E int_0^T ||O X||^2 dt = E J
    c2 = Fr(1)
    rms = mp.sqrt(mp.mpf(c2.numerator) / c2.denominator + mp.mpf(EJ.numerator) / EJ.denominator)
    phi = E_sqrt_c2_plus_lam_xi2_bessel(mp.mpf(1), mp.mpf(EJ.numerator) / EJ.denominator)
    # Doss-Sussmann formal check: e^{QW} = I + W Q (Q^2=0); Z' = (I - WQ) P (I + WQ) Z = (E12 + W E13) Z;
    # generators at different times commute (product zero) so Z_t = I + t E12 + J_t E13, J_t = int_0^t W.
    # F = (I + W_t Q) Z_t. Represent entries as polynomials in formal (t, W, J) -> dict{(a,b,c): Fr}
    def fp_mul(p, q):
        r = {}
        for (a1, b1, c1), v1 in p.items():
            for (a2, b2, c2_), v2 in q.items():
                key = (a1 + a2, b1 + b2, c1 + c2_)
                r[key] = r.get(key, Fr(0)) + v1 * v2
        return {k: v for k, v in r.items() if v != 0}
    def fp_add(p, q):
        r = dict(p)
        for k, v in q.items():
            r[k] = r.get(k, Fr(0)) + v
        return {k: v for k, v in r.items() if v != 0}
    def fmat_const(A):
        return [[({(0, 0, 0): A[i][j]} if A[i][j] != 0 else {}) for j in range(3)] for i in range(3)]
    def fmat_mul(A, B):
        return [[(lambda i, j: (lambda acc: acc)(
            __import__('functools').reduce(fp_add, [fp_mul(A[i][l], B[l][j]) for l in range(3)], {})))(i, j)
            for j in range(3)] for i in range(3)]
    tW = {(0, 1, 0): Fr(1)}; tt = {(1, 0, 0): Fr(1)}; tJ = {(0, 0, 1): Fr(1)}
    E = fmat_const(I3); E[1][2] = fp_add(E[1][2], tW)              # I + W E23
    Z = fmat_const(I3); Z[0][1] = fp_add(Z[0][1], tt); Z[0][2] = fp_add(Z[0][2], tJ)   # I + t E12 + J E13
    F_DS = fmat_mul(E, Z)
    F_ITO = fmat_const(I3); F_ITO[0][1] = tt; F_ITO[0][2] = tJ; F_ITO[1][2] = tW   # direct Ito solution
    ds_match = all(F_DS[i][j] == F_ITO[i][j] for i in range(3) for j in range(3))
    # Ito check of F_ITO: dF = (E12 + W E13) dt + E23 dW must equal PF dt + QF dW
    PF = fmat_mul(fmat_const(P), F_ITO); QF = fmat_mul(fmat_const(Q), F_ITO)
    dF_dt = fmat_const(zeros(3, 3)); dF_dt[0][1] = {(0, 0, 0): Fr(1)}; dF_dt[0][2] = tW
    dF_dW = fmat_const(zeros(3, 3)); dF_dW[1][2] = {(0, 0, 0): Fr(1)}
    ito_ok = all(PF[i][j] == dF_dt[i][j] and QF[i][j] == dF_dW[i][j] for i in range(3) for j in range(3))
    # DS ODE generator check: (I - WQ) P (I + WQ) == E12 + W E13 formally
    Em = fmat_const(I3); Em[1][2] = {(0, 1, 0): Fr(-1)}
    gen = fmat_mul(fmat_mul(Em, fmat_const(P)), E)
    gen_expected = fmat_const(zeros(3, 3)); gen_expected[0][1] = {(0, 0, 0): Fr(1)}; gen_expected[0][2] = tW
    gen_ok = all(gen[i][j] == gen_expected[i][j] for i in range(3) for j in range(3))
    return {
        "P": mstr(P), "Q": mstr(Q), "O": mstr(O), "G": mstr(mT(G)), "[P,Q]": mstr(comm), "noncommuting": not is_zero(comm),
        "Kronecker_generator_nilpotent_index": nil,
        "M(t)_polynomials": {f"M{i+1}{j+1}": {str(k): str(v) for k, v in sorted(Mij(i, j).items()) if v != 0} for i in range(3) for j in range(3) if any(v != 0 for v in Mij(i, j).values())},
        "matches_hand_solution_M11=t^3/3,M12=t^2/2,M22=t,M33=1": match,
        "E int_0^1 ||O X||^2 = E J": str(EJ),
        "RMS=sqrt(c^2+EJ)": S(rms), "Jensen_in_J_upper: E_xi sqrt(1+xi^2 EJ)": S(phi),
        "L_sandwich": "1 < L <= " + S(phi, 12) + " <= " + S(rms, 12) + " (strict lower: J=int_0^1(int_0^t W)^2 dt>0 a.s.)",
        "ordering_holds": bool(1 < phi < rms),
        "DS_generator_(I-WQ)P(I+WQ)=E12+W*E13": gen_ok,
        "DS_F=(I+WQ)(I+tE12+JE13)_equals_direct_Ito_flow": ds_match,
        "direct_flow_satisfies_dF=PFdt+QFdW_formally": ito_ok,
        "note": "exact noncommuting Q!=0 instance: Doss-Sussmann representation reproduces the Ito flow word-for-word; L not computed (law of J non-elementary), only the proved sandwich",
    }


OUT["D6_noncommuting_PQ_Qnonzero_exact"] = D6()


# ----------------------------------------------------------------------------
# D7: endpoint geometry
# ----------------------------------------------------------------------------
def D7():
    rows = []
    for (T, h) in [(Fr(5, 2), Fr(1)), (Fr(3), Fr(1)), (Fr(201, 100), Fr(1)), (Fr(1), Fr(1, 3)), (Fr(7, 3), Fr(2, 5)), (Fr(1), Fr(0))]:
        if h == 0:
            rows.append({"T": str(T), "h": "0", "n": "n/a (one window [0,eps], eps<S=T)", "S": str(T),
                         "impulse_time": "0", "0<T": T > 0, "eps_max": str(T)})
            continue
        Sh = T - h
        n = int(-(-Sh // h))
        tn = n * h
        eps_max = min(h / 2, Sh - (n - 1) * h)  # strict bounds in the source; this is the sup
        # eps grid: check (a) nh+eps<=T <=> eps<=S-(n-1)h, (b) output windows [jh,jh+eps], j=0..n, pairwise disjoint <=> eps<h
        grid_ok_a = grid_ok_b = True
        for k in range(1, 41):
            e = k * h / 20
            a_lhs = (n * h + e <= T); a_rhs = (e <= Sh - (n - 1) * h)
            grid_ok_a = grid_ok_a and (a_lhs == a_rhs)
            w = [(j * h, j * h + e) for j in range(n + 1)]
            disjoint = all(w[j][1] < w[j + 1][0] for j in range(n))
            grid_ok_b = grid_ok_b and (disjoint == (e < h))
        rows.append({"T": str(T), "h": str(h), "S": str(Sh), "n=ceil(S/h)": n, "t_n=nh": str(tn), "t_n<T": tn < T,
                     "T-t_n=S-(n-1)h": str(T - tn), "T-t_n>0": T - tn > 0, "T-t_n<=h": T - tn <= h,
                     "sup_eps=min(h/2,S-(n-1)h)": str(eps_max), "binding": "h/2" if h / 2 <= Sh - (n - 1) * h else "S-(n-1)h",
                     "eps_grid_(k h/20, k=1..40)_windows_disjoint_iff_eps<h": grid_ok_b,
                     "eps_grid_nh+eps<=T_iff_eps<=S-(n-1)h": grid_ok_a})
    return rows


OUT["D7_endpoint_geometry"] = D7()

# ----------------------------------------------------------------------------
if __name__ == "__main__":
    outpath = sys.argv[1]
    with open(outpath, 'x') as fh:
        json.dump(OUT, fh, indent=1, default=str)
    print("wrote", outpath)
    print(json.dumps({k: (v if not isinstance(v, (dict, list)) else "...") for k, v in OUT.items()}, indent=1))

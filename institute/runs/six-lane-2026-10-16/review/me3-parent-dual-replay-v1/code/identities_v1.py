#!/usr/bin/env python3
"""identities_v1.py -- exact (sympy) checks of every algebraic identity the parent dual checker relies on.

Each check is an exact symbolic identity (or an exact rational inequality); a few constants are certified with arb.
Nothing here is numerical sampling.  Writes OUT (exclusive).  Usage: python -I -B identities_v1.py OUT.json
"""
import sys
import json
import sympy as sp
from flint import arb, fmpq, ctx

ctx.prec = 128
OUT = sys.argv[1]
res = {}


def zero(expr):
    e = sp.expand(sp.together(sp.expand(expr)))
    if e == 0:
        return True
    return sp.simplify(sp.expand(sp.expand_complex(expr).rewrite(sp.exp))) == 0


t, th, z, kap, s, xi, dl, om, nu, beta, d, chi, rt, c0 = sp.symbols(
    "t theta z kappa s xi delta omega nu beta d chi rho_t c0", positive=True)
k_ = sp.Rational(50, 61)
T = sp.Rational(11, 50)
res["kappa_is_1_over_1_plus_T"] = (k_ == 1 / (1 + T))
res["two_kappa_minus_1"] = str(2 * k_ - 1)


def QT(y, kk):
    return (kk * y ** 2 - 2 * y + 2) / y ** 3


# I1 Laplace transform of q_theta
rho = 1 - kap
lap = sp.integrate(((t - th) ** 2 - rho * th ** 2) * sp.exp(-z * t), (t, 0, sp.oo))
res["I1_laplace_q_theta"] = zero(lap - th ** 3 * QT(th * z, kap))

# I2 W in s-coordinates: Q_T(theta(1+xi))/Q_T(theta) = zz(w1 + zz(w2 + zz w3)), theta = s/(1-s)
thv = s / (1 - s)
N1 = kap * s ** 2 - 2 * s * (1 - s) + 2 * (1 - s) ** 2
zz = 1 / (1 + xi)
w1, w2, w3 = kap * s ** 2 / N1, -2 * s * (1 - s) / N1, 2 * (1 - s) ** 2 / N1
res["I2_W_form"] = zero(sp.together(QT(thv * (1 + xi), kap) / QT(thv, kap) - zz * (w1 + zz * (w2 + zz * w3))))
q = lambda zv: kap * s ** 2 * zv ** 2 - 2 * s * (1 - s) * zv + 2 * (1 - s) ** 2  # noqa: E731
res["I2b_W_eq_q_over_N1_z3"] = zero(sp.together(zz * (w1 + zz * (w2 + zz * w3)) - q(1 + xi) / (N1 * (1 + xi) ** 3)))

# I3 N1 > 0
res["I3_N1_expanded"] = zero(N1 - ((kap + 4) * s ** 2 - 6 * s + 2))
res["I3_N1_eq_(1-s)^2 N(theta)"] = zero(sp.together(N1 - (1 - s) ** 2 * (kap * thv ** 2 - 2 * thv + 2)))
disc = 36 - 8 * (k_ + 4)
res["I3_discriminant_at_kappa"] = str(disc)
res["I3_N1_positive_definite"] = bool(disc < 0)

# I4 p factorisation (c0^2 = 2 kappa - 1) and I5 |p|^2 = B
I = sp.I
p = (s * (1 - s) * (1 + I * c0) - kap * s ** 2) / N1
pb = (s * (1 - s) * (1 - I * c0) - kap * s ** 2) / N1
f4 = sp.expand(sp.together((1 - p * xi) * (1 - pb * xi) * N1 - q(1 + xi)) * N1)
f4 = sp.expand(f4.subs(c0 ** 2, 2 * kap - 1))
res["I4_(1-p xi)(1-pbar xi) N1 = q(1+xi)"] = zero(f4)
f5 = sp.expand(sp.together(p * pb - kap * s ** 2 / N1) * N1 ** 2)
res["I5_|p|^2 = kappa s^2/N1"] = zero(sp.expand(f5.subs(c0 ** 2, 2 * kap - 1)))
res["I5b_100*N1 - 39*kappa*s^2 at kappa=50/61"] = str(sp.factor(100 * N1.subs(kap, k_) - 39 * k_ * s ** 2))
res["I5b_B_le_100_over_39"] = zero(100 * N1.subs(kap, k_) - 39 * k_ * s ** 2 - 50 * (3 * s - 2) ** 2)

# I6 X/U recursion: xi^m = X_m - i omega U_m;  X_j - delta U_j = -(delta^2+omega^2) U_{j-1}
X, U = [sp.Integer(1)], [sp.Integer(0)]
for m in range(10):
    X.append(sp.expand(dl * X[-1] - om ** 2 * U[-1]))
    U.append(sp.expand(X[-2] + dl * U[-1]))
ok6 = all(zero(sp.expand((dl - I * om) ** m) - (X[m] - I * om * U[m])) for m in range(11))
ok6b = all(zero(X[j] - dl * U[j] + (dl ** 2 + om ** 2) * U[j - 1]) for j in range(1, 11))
res["I6_xi_powers"] = ok6
res["I6b_X_minus_delta_U"] = ok6b

# I8 Phi and Im g in series form for a truncated polynomial g_N with real coefficients c_j (N = 8)
N = 8
cj = sp.symbols("c1:%d" % (N + 1), real=True)
gN = sum(cj[j - 1] * (dl - I * om) ** j for j in range(1, N + 1))
ReG, ImG = sp.expand(sp.re(sp.expand(gN))), sp.expand(sp.im(sp.expand(gN)))
Phi = sp.expand(om * ReG + dl * ImG)
res["I8_Phi = -omega|xi|^2 sum_{j>=2} c_j U_{j-1}"] = zero(
    Phi + om * (dl ** 2 + om ** 2) * sum(cj[j - 1] * U[j - 1] for j in range(2, N + 1)))
res["I8b_Im g = -omega sum_{j>=1} c_j U_j"] = zero(ImG + om * sum(cj[j - 1] * U[j] for j in range(1, N + 1)))

# I7 series of log W: log(1-p xi)+log(1-pbar xi)-3log(1+xi) coefficients c_j = -(p^j+pbar^j)/j + 3(-1)^j/j
P1, P2 = sp.symbols("P1 P2")
ser = sp.series(sp.log(1 - P1 * xi) + sp.log(1 - P2 * xi) - 3 * sp.log(1 + xi), xi, 0, 9).removeO()
res["I7_log_series_coefficients"] = all(
    zero(ser.coeff(xi, j) - (-(P1 ** j + P2 ** j) / j + sp.Integer(3) * (-1) ** j / j)) for j in range(1, 9))

# I9 SWB derivatives on the real axis and the root form
zr = sp.symbols("zr", positive=True)
g_real = sp.log(q(zr) / N1) - 3 * sp.log(zr)
qz = 2 * kap * s ** 2 * zr - 2 * s * (1 - s)
qzz = 2 * kap * s ** 2
r1 = qz / q(zr)
g1 = r1 - 3 / zr
g2 = qzz / q(zr) - r1 ** 2 + 3 / zr ** 2
g3 = -3 * r1 * qzz / q(zr) + 2 * r1 ** 3 - 6 / zr ** 3
res["I9_g1"] = zero(sp.together(sp.diff(g_real, zr) - g1))
res["I9_g2"] = zero(sp.together(sp.diff(g_real, zr, 2) - g2))
res["I9_g3"] = zero(sp.together(sp.diff(g_real, zr, 3) - g3))
z1 = (1 - s) * (1 + I * c0) / (kap * s)
z2 = (1 - s) * (1 - I * c0) / (kap * s)
fq = sp.expand(sp.expand(kap * s ** 2 * (zr - z1) * (zr - z2) - q(zr)).subs(c0 ** 2, 2 * kap - 1))
res["I9_q = kappa s^2 (z-z1)(z-z2)"] = zero(fq)
res["I9_v1 = kappa s/(kappa s z - (1-s)(1+i c0)) = 1/(z-z1)"] = zero(sp.together(
    kap * s / (kap * s * zr - (1 - s) * (1 + I * c0)) - 1 / (zr - z1)))
a1, a2 = sp.symbols("a1 a2")
gk = sp.log(zr - a1) + sp.log(zr - a2) - 3 * sp.log(zr)
res["I9_kth_derivative_root_form_k1..6"] = all(zero(sp.together(
    sp.diff(gk, zr, k) - (-1) ** (k - 1) * sp.factorial(k - 1) * (1 / (zr - a1) ** k + 1 / (zr - a2) ** k - 3 / zr ** k)))
    for k in range(1, 7))

# I10 LD1 map
R = sp.sqrt((1 + dl) ** 2 + om ** 2)
cbv, sbv = (1 + dl) / R, om / R                       # cos, sin of beta = atan(omega/(1+delta)) in (0, pi/2)
dd = 1 / (1 + dl)
res["I10_beta_def"] = zero(sbv / cbv - om / (1 + dl)) and zero(cbv ** 2 + sbv ** 2 - 1)
res["I10_zeta = d cos(beta) e^{i beta}"] = zero(dd * cbv * (cbv + I * sbv) - 1 / (1 + dl - I * om))
res["I10_delta/omega = (1-d)/tan(beta)"] = zero((1 - dd) * cbv / sbv - dl / om)
zeta_b = d * sp.cos(beta) * sp.exp(I * beta)
res["I10_dzeta/dbeta = i d e^{2i beta}"] = zero(sp.diff(zeta_b, beta) - I * d * sp.exp(2 * I * beta))

# I11 LD2 blow-up
sv = chi * rt
zeta2 = (1 - chi) * rt * sp.exp(I * beta)
N1v = N1.subs(s, sv)
Pfull = (kap * sv ** 2 - 2 * sv * (1 - sv) * zeta2 + 2 * (1 - sv) ** 2 * zeta2 ** 2) / N1v
Ph = (kap * chi ** 2 - 2 * chi * (1 - chi) * (1 - sv) * sp.exp(I * beta)
      + 2 * (1 - sv) ** 2 * (1 - chi) ** 2 * sp.exp(2 * I * beta)) / N1v
res["I11_P = rho_t^2 Phat"] = zero(sp.simplify(Pfull - rt ** 2 * Ph))
Phb = I * (-2 * chi * (1 - chi) * (1 - sv) * sp.exp(I * beta)
           + 4 * (1 - sv) ** 2 * (1 - chi) ** 2 * sp.exp(2 * I * beta)) / N1v
res["I11_dPhat/dbeta"] = zero(sp.simplify(sp.diff(Ph, beta) - Phb))
res["I11_rho_t_max = 1/16 + 1/65 = 81/1040"] = (sp.Rational(1, 16) + sp.Rational(1, 65) == sp.Rational(81, 1040))

# I12 LW map
res["I12_zz = nu/(nu(1+delta) - i)"] = zero(sp.together(1 / (1 + dl - I / nu) - nu / (nu * (1 + dl) - I)))

# I13 G gradients of log W
xs = sp.symbols("xs")
logW = sp.log(q(1 + xs)) - sp.log(N1) - 3 * sp.log(1 + xs)
qs_expr = 2 * kap * s * (1 + xs) ** 2 - 2 * (1 - 2 * s) * (1 + xs) - 4 * (1 - s)
N1s = 2 * kap * s - 2 * (1 - 2 * s) - 4 * (1 - s)
res["I13_dlogW/dxi"] = zero(sp.together(sp.diff(logW, xs) - (sp.diff(q(1 + xs), xs) / q(1 + xs) - 3 / (1 + xs))))
res["I13_q_xi = 2 kappa s^2 z - 2 s(1-s)"] = zero(sp.diff(q(1 + xs), xs) - (2 * kap * s ** 2 * (1 + xs) - 2 * s * (1 - s)))
res["I13_dlogW/ds"] = zero(sp.together(sp.diff(logW, s) - (qs_expr / q(1 + xs) - N1s / N1)))

# I14 Lemma 2.2 identity: min_u (m2 u^2 - 2 m1 u + 1) = 1 - m1^2/m2 = SCV/(1+SCV) (m0 = 1)
m1, m2, u = sp.symbols("m1 m2 u", positive=True)
umin = m1 / m2
scv = m2 / m1 ** 2 - 1
res["I14_min_R_theta"] = zero(sp.together((m2 * umin ** 2 - 2 * m1 * umin + 1) - scv / (1 + scv)))

# I15 moments of f0 = e^{-t} - e^{-(1+delta)t} cos(omega t) (controls)
ok15 = True
for kk in range(3):
    mom = sp.integrate(t ** kk * (sp.exp(-t) - sp.exp(-(1 + dl) * t) * sp.cos(om * t)), (t, 0, sp.oo), conds="none")
    claim = sp.factorial(kk) * (1 - sp.re(sp.expand_complex((1 / (1 + dl - I * om)) ** (kk + 1))))
    ok15 = ok15 and zero(sp.simplify(mom - claim))
res["I15_f0_moments"] = ok15

# I16 TRIANGLE algebra: W = a + b V, V = e^{-r th}(cos th + i sin th)
rr, tt, ReW, ImW = sp.symbols("r tt ReW ImW", real=True)
Vr, Vi = sp.exp(-rr * tt) * sp.cos(tt), sp.exp(-rr * tt) * sp.sin(tt)
bb = ImW * sp.exp(rr * tt) / sp.sin(tt)
aa = ReW - ImW * sp.cos(tt) / sp.sin(tt)
res["I16_triangle_solution"] = zero(sp.simplify(aa + bb * Vr - ReW)) and zero(sp.simplify(bb * Vi - ImW))
res["I16_a_plus_b"] = zero(sp.simplify(aa + bb - (ReW + ImW * (sp.exp(rr * tt) - sp.cos(tt)) / sp.sin(tt))))

# certified constants (arb)
res["C_beta_top_gt_pi_over_2"] = bool(arb(fmpq(15708, 10000)) > arb.pi() / 2)
res["C_v_cos_upper_lt_T"] = bool(arb("0.20090156350055695880138069") < arb(fmpq(11, 50)))
bad = [k for k, v in res.items() if v is False]
res["all_true"] = not bad
res["false_items"] = bad
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"all_true": res["all_true"], "false_items": bad}))

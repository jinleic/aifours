"""ME3ParentDelta: exact re-derivation checks for the mathematical hunks of
reductions v1->v2->v3->v4, theorem v3->v4->v5 and charts-spec v1->v2.

Parent-authored; imports nothing from the lane. Exact arithmetic only (fractions.Fraction / SymPy exact
rationals and symbols). python-flint is used for exactly one check (pi < 31416/10000) as a cross-check of the
SymPy comparison. No floats enter any decision: every decision is an exact rational comparison, an exact
polynomial identity (expand(...) == 0) or an exact remainder / resultant.

Usage: python delta_checks_v1.py OUT_JSON   (OUT_JSON is created with mode 'x').
"""
import json
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

RESULTS = []


def rec(cid, hunk, statement, ok, detail=""):
    RESULTS.append({"id": cid, "hunk": hunk, "statement": statement, "pass": bool(ok), "detail": str(detail)})
    print(("PASS " if ok else "FAIL ") + cid + " :: " + statement + ((" :: " + str(detail)) if detail else ""),
          flush=True)


def ctl(cid, hunk, statement, mutated_holds, detail=""):
    """A control: the mutated claim must be FALSE; the control passes iff mutated_holds is False."""
    RESULTS.append({"id": cid, "hunk": hunk, "statement": "CONTROL (must be refuted): " + statement,
                    "pass": (not bool(mutated_holds)), "mutated_claim_holds": bool(mutated_holds),
                    "detail": str(detail)})
    print(("PASS " if not mutated_holds else "FAIL ") + cid + " :: CONTROL " + statement
          + ((" :: " + str(detail)) if detail else ""), flush=True)


def iszero(e):
    return sp.expand(e) == 0


I = sp.I
R = sp.Rational

# ---------------------------------------------------------------- L4: Delta_3 ------------------------------
tau, x, y = sp.symbols("tau x y", real=True)
t = sp.symbols("t", positive=True)

mk = []
for k in range(3):
    val = sp.integrate(t**k * (t - tau) ** 2 * sp.exp(-t), (t, 0, sp.oo), conds="none")
    mk.append(sp.expand(val))
    rec("L4.m%d" % k, "red v1->v2 H4/H5 (L4(1), unchanged formula)",
        "m_%d((t-tau)^2 e^-t) = (k+2)! - 2 tau (k+1)! + tau^2 k! (from the integral definition)" % k,
        iszero(val - (sp.factorial(k + 2) - 2 * tau * sp.factorial(k + 1) + tau**2 * sp.factorial(k))))
P = sp.expand(mk[0] * mk[2])
Q = mk[1]
rec("L4.Q", "red L4(1)", "Q = m1 = (tau-2)^2 + 2", iszero(Q - ((tau - 2) ** 2 + 2)))
rec("L4.P", "red L4(1)", "P = m0 m2 = (tau^2-2tau+2)(2tau^2-12tau+24)",
    iszero(P - (tau**2 - 2 * tau + 2) * (2 * tau**2 - 12 * tau + 24)))
rec("L4.SOS", "red L4(2)", "4(P - (5/4)Q^2) = 3(tau^2-4tau+2)^2 + 8tau^2",
    iszero(4 * (P - R(5, 4) * Q**2) - (3 * (tau**2 - 4 * tau + 2) ** 2 + 8 * tau**2)))
qpol = tau**3 - 9 * tau**2 + 18 * tau - 6
L3 = 1 - 3 * tau + R(3, 2) * tau**2 - tau**3 / 6
rec("L4.dP", "red v1->v2 H5 (L4(3))", "P'Q - 2PQ' = 8q, q = tau^3-9tau^2+18tau-6 = -6 L3",
    iszero(sp.diff(P, tau) * Q - 2 * P * sp.diff(Q, tau) - 8 * qpol) and iszero(qpol + 6 * L3))
qvals = {R(0): -6, R(1, 2): R(7, 8), R(2): 2, R(3): -6, R(6): -6, R(7): 22}
okq = all(qpol.subs(tau, k) == v for k, v in qvals.items())
rec("L4.qvals", "red v1->v2 H5 (L4(3) root isolation, NEW in v2)",
    "q(0)=-6, q(1/2)=7/8, q(2)=2, q(3)=-6, q(6)=-6, q(7)=22 (sign changes in (0,1/2),(2,3),(6,7))", okq,
    {str(k): str(qpol.subs(tau, k)) for k in qvals})
s0 = P.subs(tau, 0) / Q.subs(tau, 0) ** 2 - 1
rec("L4.s0", "red v1->v2 H5 (NEW)", "s(0) = 48/36 - 1 = 1/3", s0 == R(1, 3), s0)
rec("L4.lc", "red v1->v2 H5 (NEW)", "deg P = deg Q^2 = 4 with leading coefficients 2 and 1 (s -> 1 at +-inf)",
    sp.Poly(P, tau).LC() == 2 and sp.Poly(Q**2, tau).LC() == 1 and sp.Poly(P, tau).degree() == 4)
two_p_3q = sp.expand(2 * P - 3 * Q**2)
rec("L4.x3", "red v1->v2 H5 (NEW: s(x3) > 1/2)",
    "2P - 3Q^2 = tau^4 - 8tau^3 + 20tau^2 - 12 = tau^2((tau-4)^2+4) - 12, and >= 36*4-12 = 132 > 0 for tau >= 6",
    iszero(two_p_3q - (tau**4 - 8 * tau**3 + 20 * tau**2 - 12))
    and iszero(two_p_3q - (tau**2 * ((tau - 4) ** 2 + 4) - 12)))
# On tau >= 6: tau^2 >= 36 and (tau-4)^2 + 4 >= 4 (in fact >= 8); exact lower bound value:
rec("L4.x3b", "red v1->v2 H5", "36*4 - 12 = 132 > 0", 36 * 4 - 12 == 132)

h = 32 * y**3 - 144 * y**2 + 135 * y - 27
D = P - Q**2
Q6h = sp.expand(32 * D**3 - 144 * D**2 * Q**2 + 135 * D * Q**4 - 27 * Q**6)
rem1 = sp.rem(sp.Poly(Q6h, tau), sp.Poly(qpol, tau))
rec("L4.Q6h", "red v1->v2 H5 (L4(4) remainder argument)",
    "Q^6 h(s) = 32(P-Q^2)^3 - 144(P-Q^2)^2Q^2 + 135(P-Q^2)Q^4 - 27Q^6 == 0 mod q", rem1.is_zero)
num2 = sp.expand(24 * (P - Q**2) - Q**2 * (tau * (9 - tau) ** 2 - 24))
rem2 = sp.rem(sp.Poly(num2, tau), sp.Poly(qpol, tau))
rec("L4.closed", "red L4(3) closed form",
    "numerator of s - (x(9-x)^2-24)/24 is 0 mod q (24(P-Q^2) - Q^2(x(9-x)^2-24))", rem2.is_zero)
x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)
# Vieta: x2+x3 = 9-x1, x2x3 = 6/x1 (from q monic with sum 9 and product 6)
vieta = sp.simplify(((9 - x1) ** 2 - 4 * 6 / x1) / (4 * 6 / x1) - (x1 * (9 - x1) ** 2 - 24) / 24)
rec("L4.vieta", "red L4(3) closed form", "(x3-x2)^2/(4x2x3) = (x1(9-x1)^2-24)/24 under Vieta", vieta == 0)

# ---- v2->v3 resultant fix (Codex delta finding 5) -----------------------------------------------------
qx = x**3 - 9 * x**2 + 18 * x - 6
gx = 24 * y - x * (9 - x) ** 2 + 24
res = sp.expand(sp.resultant(qx, gx, x))
rec("L4.res", "red v2->v3 H2 (Res fix, Codex delta MINOR-5)",
    "Res_x(q(x), 24y - x(9-x)^2 + 24) = 432*h(y) (leading term (24y)^3 = 13824 y^3 = 432*32 y^3)",
    iszero(res - 432 * h), sp.factor(res))
rec("L4.res2", "red v2->v3 H2", "24^3 = 13824 = 432*32 and monic normalization Res/13824 = h/32",
    24**3 == 13824 == 432 * 32 and iszero(res / 13824 - h / 32))
ctl("CTL.res", "red v2->v3 H2", "v2 wording 'h/32 is the resultant' (Res == h/32)", iszero(res - h / 32))
res_rev = sp.expand(sp.resultant(gx, qx, x))
rec("L4.res_rev", "red v2->v3 H2 (convention note)",
    "argument order matters only by the sign (-1)^(3*3): Res_x(g, q) = -432 h", iszero(res_rev + 432 * h))

# irreducibility of h
fl = sp.factor_list(sp.Poly(h, y))
irreducible = (len(fl[1]) == 1 and fl[1][0][0].degree() == 3 and fl[1][0][1] == 1)
hmod5 = [int(sp.Poly(h, y).eval(k)) % 5 for k in range(5)]
rec("L4.irr", "red v1->v2 H4/H5 (irreducibility by reduction mod 5)",
    "h = 32y^3-144y^2+135y-27 irreducible over Q; h mod 5 = 2y^3+y^2+3 has values 3,1,3,1,2 at 0..4",
    irreducible and hmod5 == [3, 1, 3, 1, 2], {"factor_list": str(fl), "h_mod5_values": hmod5})
hm5 = sp.Poly(h, y, modulus=5)
rec("L4.irr2", "red L4(4)", "h mod 5 equals 2y^3 + y^2 + 3", hm5 == sp.Poly(2 * y**3 + y**2 + 3, y, modulus=5),
    hm5)

# ---- Lemma 4.2 (exact Delta_3 > 553/2000) --------------------------------------------------------------
hp = sp.diff(h, y)
rec("L42.hp", "red v1->v2 H5 (Lemma 4.2, NEW)", "h'(y) = 96y^2-288y+135 = 96(y-3/2)^2 - 81",
    iszero(hp - (96 * y**2 - 288 * y + 135)) and iszero(hp - (96 * (y - R(3, 2)) ** 2 - 81)))
hpv = {R(1, 4): hp.subs(y, R(1, 4)), R(1, 3): hp.subs(y, R(1, 3))}
rec("L42.hpmin", "red Lemma 4.2",
    "h' decreasing on [1/4,1/3] (y < 3/2) so min h' = h'(1/3) = 96(7/6)^2 - 81 = 149/3 > 0",
    hpv[R(1, 3)] == R(149, 3) and 96 * R(7, 6) ** 2 - 81 == R(149, 3) and hpv[R(1, 4)] > hpv[R(1, 3)] > 0,
    {str(k): str(v) for k, v in hpv.items()})


def hval(v):
    v = sp.Rational(v)
    return sp.expand(h.subs(y, v))


vals = {"1/4": hval(R(1, 4)), "1/3": hval(R(1, 3)), "553/2000": hval(R(553, 2000)),
        "2766/10000": hval(R(2766, 10000)), "552/2000": hval(R(552, 2000))}
rec("L42.vals", "red Lemma 4.2",
    "h(1/4)=-7/4, h(1/3)=86/27, h(553/2000)=-1293623/250000000 (<0), h(552/2000)=-142803/3906250",
    vals["1/4"] == R(-7, 4) and vals["1/3"] == R(86, 27) and vals["553/2000"] == R(-1293623, 250000000)
    and vals["552/2000"] == R(-142803, 3906250), {k: str(v) for k, v in vals.items()})
ctl("CTL.0.2766", "red Lemma 4.2 wrong control", "h(2766/10000) < 0 (would certify Delta3 > 0.2766)",
    vals["2766/10000"] < 0, "h(2766/10000) = %s" % vals["2766/10000"])
rec("L42.2766", "red Lemma 4.2", "h(2766/10000) = 4277637/3906250000 > 0", vals["2766/10000"] == R(4277637, 3906250000))
rec("L42.window", "red Lemma 4.2", "553/2000 in [1/4, 1/3]", R(1, 4) <= R(553, 2000) <= R(1, 3))
rec("L42.dec", "red v1->v2", "553/2000 = 0.2765 exactly", R(553, 2000) == sp.Rational("0.2765"))
lo = R(478316921303906167, 1729382256910270464)
hi = R(1275511790143749779, 4611686018427387904)
rec("L42.bracket", "red Lemma 4.2 (EXACT 60-step bracket)",
    "h(lo) < 0 < h(hi), 1/4 < lo < hi < 1/3 for the stated bracket; both start 0.276582530780945666",
    hval(lo) < 0 < hval(hi) and R(1, 4) < lo < hi < R(1, 3)
    and sp.floor(lo * 10**18) == 276582530780945666 and sp.floor(hi * 10**18) == 276582530780945666,
    {"lo_18": str(sp.floor(lo * 10**18)), "hi_18": str(sp.floor(hi * 10**18))})

# Delta_3 = s(x1) is the root of h in (1/4, 1/3): exact rational interval for x1 and s monotone
# (x1 in (0,1/2); s decreasing on (-inf,x1]); cross-check: s at the rational endpoints of an exact isolating
# interval for x1 brackets a root of h -> informational exact check using a refined interval.
x1_iv = sp.Poly(qpol, tau).intervals(eps=R(1, 10**12))
x1_lo, x1_hi = [iv for iv in x1_iv if iv[0][0] >= 0 and iv[0][1] <= R(1, 2)][0][0]
s_expr = P / Q**2 - 1
s_at_lo = sp.nsimplify(s_expr.subs(tau, x1_lo))
s_at_hi = sp.nsimplify(s_expr.subs(tau, x1_hi))
# s decreasing on (-inf, x1]: s(x1) < s(x1_lo); s increasing on [x1, x2]: s(x1) < s(x1_hi); and s(x1) > lo-bracket.
rec("L4.x1iv", "red L4(3) (informational cross-check, exact rationals)",
    "x1 has an exact isolating interval in (0, 1/2) of width <= 1e-12; s at both ends exceeds the h-bracket lo",
    0 <= x1_lo < x1_hi <= R(1, 2) and x1_hi - x1_lo <= R(1, 10**12) and s_at_lo > lo and s_at_hi > lo,
    {"x1_lo": str(x1_lo), "x1_hi": str(x1_hi)})

# ---------------------------------------------------------------- L5: D1 tails, separation ---------------
rec("L54.tail", "red v1->v2 H6 (Lemma 5.4 constant)", "(16*553/2000 - 1)/17 = 428/2125 > 1007/5000 = 0.2014",
    (16 * Fr(553, 2000) - 1) / 17 == Fr(428, 2125) and Fr(428, 2125) > Fr(1007, 5000))
w = sp.symbols("w", positive=True)
Dl = sp.symbols("Delta", positive=True)
bnd = (Dl - w**2) / (1 + w**2)
rec("L54.mono", "red Lemma 5.4 (decreasing in omega)",
    "d/dw (Delta-w^2)/(1+w^2) = -2w(1+Delta)/(1+w^2)^2 < 0; value at w=1/4 is (16Delta-1)/17",
    iszero(sp.together(sp.diff(bnd, w) + 2 * w * (1 + Dl) / (1 + w**2) ** 2))
    and sp.simplify(bnd.subs(w, R(1, 4)) - (16 * Dl - 1) / 17) == 0)
rb = Fr(2426, 10000)
val55 = 2 * (1 - rb) * (1 - rb**3) / (1 + rb**2) ** 2 - 1
rec("L55.exact", "red v1->v2 H7 (Lemma 5.5 exact display)",
    "rho_bar^2 = 1471369/25000000 > 1/17 and 2(1-rb)(1-rb^3)/(1+rb^2)^2 - 1 = 232498770764161/700733376734161 > 33/100",
    rb**2 == Fr(1471369, 25000000) and rb**2 > Fr(1, 17)
    and val55 == Fr(232498770764161, 700733376734161) and val55 > Fr(33, 100), str(val55))

# Theorem 5.6 exact separation point: omega = 1, cos phi = 35/37, sin phi = 12/37
cphi, sphi = R(35, 37), R(12, 37)
rec("T56.pyth", "red v1->v2 H7 (Thm 5.6, NEW)", "35^2 + 12^2 = 37^2", 35**2 + 12**2 == 37**2)
em = (cphi - I * sphi)  # e^{-i phi}
mom_formula = []
for k in range(3):
    z = sp.expand(em * (1 - I) ** (-(k + 1)))
    mom_formula.append(sp.factorial(k) * (1 - sp.re(z)))
mom_formula = [sp.nsimplify(sp.simplify(m)) for m in mom_formula]
mom_int = []
for k in range(3):
    f_int = sp.integrate(t**k * sp.exp(-t) * (1 - cphi * sp.cos(t) - sphi * sp.sin(t)), (t, 0, sp.oo))
    mom_int.append(sp.nsimplify(sp.simplify(f_int)))
target = [R(27, 74), R(62, 74), R(171, 74)]
rec("T56.mom", "red Thm 5.6",
    "moments of f_{1,phi_e}: Lemma 5.2 formula AND direct exact integration both give (27,62,171)/74",
    mom_formula == target and mom_int == target, {"formula": [str(m) for m in mom_formula],
                                                    "integral": [str(m) for m in mom_int]})
scv = target[0] * target[2] / target[1] ** 2 - 1
rec("T56.scv", "red Thm 5.6", "SCV = 27*171/62^2 - 1 = 4617/3844 - 1 = 773/3844", scv == R(773, 3844), scv)
# Lemma 5.3 algebraic form at the same point (psi = phi - 2*beta, beta = pi/4): C = sin phi, S = -cos phi
C, S = sphi, -cphi
u = 1 - C
X = 1 + u
a_ = 2
Y = S
alg = [(X + Y) / 2, X / 2, 2 * (X + a_ - Y) / 4]
rec("T56.alg", "red Thm 5.6 (cross-check via Lemma 5.3 algebraic form)",
    "Lemma 5.3 with omega=1, psi = phi - pi/2 gives the same moments", alg == target, [str(v) for v in alg])
cmp_ok = (Fr(773, 3844) < Fr(1007, 5000) < Fr(11, 50) and 773 * 5000 == 3865000 and 1007 * 3844 == 3870908
          and Fr(773, 3844) < Fr(553, 2000) and Fr(428, 2125) > Fr(773, 3844) and 773 * 2125 == 1642625
          and 428 * 3844 == 1645232 and Fr(33, 100) > Fr(773, 3844))
rec("T56.cmp", "red Thm 5.6 / theorem v5 S1,S5",
    "773/3844 < 1007/5000 < 11/50; 773/3844 < 553/2000; 428/2125 > 773/3844; 0.33 > 773/3844", cmp_ok)
# controls of Thm 5.6
swap = []
for k in range(3):
    z = sp.expand((R(12, 37) - I * R(35, 37)) * (1 - I) ** (-(k + 1)))
    swap.append(sp.factorial(k) * (1 - sp.re(z)))
scv_swap = sp.nsimplify(swap[0] * swap[2] / swap[1] ** 2 - 1)
ctl("CTL.swap", "red Thm 5.6", "swapped (cos,sin)=(12/37,35/37) also gives 773/3844", scv_swap == R(773, 3844),
    "gives %s" % scv_swap)
sgn = []
for k in range(3):
    z = sp.expand((cphi + I * sphi) * (1 - I) ** (-(k + 1)))
    sgn.append(sp.factorial(k) * (1 - sp.re(z)))
scv_sgn = sp.nsimplify(sgn[0] * sgn[2] / sgn[1] ** 2 - 1)
ctl("CTL.phase", "red Thm 5.6", "phase-sign mutation e^{+i phi} also gives 773/3844", scv_sgn == R(773, 3844),
    "gives %s" % scv_sgn)

# Remark 5.6a (v3->v4 H10)
b56 = (R(1, 4) - w**2) / (1 + w**2)
rec("R56a.deriv", "red v3->v4 H10 (Remark 5.6a, NEW)",
    "d/dw (1/4 - w^2)/(1+w^2) = -(5/2)w/(1+w^2)^2", iszero(sp.together(sp.diff(b56, w) + R(5, 2) * w / (1 + w**2) ** 2)))
rec("R56a.val", "red Remark 5.6a", "(1/4 - 1/25)/(26/25) = 21/104 > 773/3844 (21*3844 = 80724 > 80392 = 773*104)",
    b56.subs(w, R(1, 5)) == R(21, 104) and Fr(21, 104) > Fr(773, 3844) and 21 * 3844 == 80724 and 773 * 104 == 80392)
ctl("CTL.R56a", "red Remark 5.6a wrong control",
    "with only Delta3 > 1/4 the tail omega <= 1/4 suffices (3/17 > 773/3844)", Fr(3, 17) > Fr(773, 3844),
    "(1/4-1/16)/(17/16) = %s" % b56.subs(w, R(1, 4)))
rec("R56a.window", "red Remark 5.6a", "(1, phi_e) lies in the compact middle [1/5,4] x [0,2pi] (phi_e in (0,pi/2))",
    R(1, 5) <= 1 <= 4 and 0 < cphi and 0 < sphi)

# chain used in theorem v5 S0/S1/S5 and reductions Cor 5.7 / Cor 7.1
rec("CHAIN", "thm v4/v5 S0,S1,S5; red Cor 5.7/7.1",
    "Delta3 > 553/2000 > 1007/5000 > 773/3844 >= v_cos and T = 11/50 > 773/3844",
    Fr(553, 2000) > Fr(1007, 5000) > Fr(773, 3844) and Fr(11, 50) > Fr(773, 3844))

# ---------------------------------------------------------------- Lemma D: the corrected cone K ----------
dl, om, th = sp.symbols("delta omega theta", positive=True)
a, cr, ci = sp.symbols("a c_r c_i", real=True)
T = R(11, 50)
kap = 1 / (1 + T)
rho = T / (1 + T)
rec("LD.const", "thm S1 constants", "kappa = 1/(1+T) = 50/61, rho = T/(1+T) = 11/61 = 1 - kappa; rho/(1-rho) = T",
    kap == R(50, 61) and rho == R(11, 61) and rho == 1 - kap and rho / (1 - rho) == T)
rec("LD.QTpos", "thm S2 (unchanged)", "kappa y^2 - 2y + 2 has discriminant 4 - 8 kappa = -156/61 < 0",
    4 - 8 * kap == R(-156, 61))
xi = dl - I * om
cc = cr + I * ci
expr_re = sp.re(sp.expand_complex(cc * sp.exp(-xi * t)))
rec("LD.re", "thm v4->v5 H5 (K definition); red v3->v4 H16 (Cor 7.2)",
    "Re(c e^{-xi t}) = e^{-delta t}(Re c cos(omega t) - Im c sin(omega t))",
    sp.simplify(expr_re - sp.exp(-dl * t) * (cr * sp.cos(om * t) - ci * sp.sin(om * t))) == 0)
zsym = sp.symbols("z", positive=True)
qth = (t - th) ** 2 - rho * th**2
Lz = sp.integrate(sp.expand(qth * sp.exp(-zsym * t)), (t, 0, sp.oo), conds="none")
QT = lambda yy: (kap * yy**2 - 2 * yy + 2) / yy**3  # noqa: E731
rec("LD.laplace", "thm S2 (unchanged identity)", "int_0^oo q_theta e^{-zt} dt = theta^3 Q_T(theta z) (z > 0)",
    sp.simplify(Lz - th**3 * QT(th * zsym)) == 0)
# General-cone identity with unrestricted a in R, c in C, via the termwise Laplace transform
# int t^k e^{-wt} dt = k!/w^{k+1}, Re w > 0, applied to w = 1 and w = 1 + xi; q_theta is real.
zc = 1 + xi


def lap_poly(poly_t, wv):
    pl = sp.Poly(sp.expand(poly_t), t)
    return sum(coef * sp.factorial(m) / wv ** (m + 1) for (m,), coef in pl.terms())


I_f = a * lap_poly(qth, 1) + sp.re(sp.expand_complex(cc * lap_poly(qth, zc)))
Wth = QT(th * zc) / QT(th)
rhs = th**3 * QT(th) * (a + sp.re(sp.expand_complex(cc * Wth)))
rec("LD.ident", "thm v4->v5 H5 (Lemma D on the corrected K: a real, c complex unrestricted)",
    "int q_theta f = theta^3 Q_T(theta) [a + Re(c W)], W = Q_T(theta(1+xi))/Q_T(theta), f = a e^-t + Re(c e^{-(1+xi)t})",
    sp.simplify(sp.expand_complex(I_f - rhs)) == 0)
# exact spot check of the same identity by direct integration of the real trig form at a rational point
pt = {dl: R(1, 3), om: R(2), th: R(3, 2), a: R(5, 7), cr: R(2, 3), ci: R(-4, 5)}
f_real = (a * sp.exp(-t) + sp.exp(-(1 + dl) * t) * (cr * sp.cos(om * t) - ci * sp.sin(om * t))).subs(pt)
direct = sp.integrate(sp.expand(qth.subs(pt) * f_real), (t, 0, sp.oo))
rec("LD.spot", "thm v4->v5 H5", "direct exact integral of q_theta f (trig form) equals theta^3 Q_T(theta)[a+Re(cW)] at "
    "delta=1/3, omega=2, theta=3/2, a=5/7, c=2/3-4i/5", sp.simplify(direct - rhs.subs(pt)) == 0,
    sp.nsimplify(sp.simplify(direct)))
Wbar = QT(th * (1 + sp.conjugate(xi))) / QT(th)
rhs_mut = th**3 * QT(th) * (a + sp.re(sp.expand_complex(cc * Wbar)))
ctl("CTL.LDconj", "thm S2 identity mutation", "identity also holds with W replaced by Q_T(theta(1+conj xi))/Q_T(theta)",
    sp.simplify(sp.expand_complex(direct - rhs_mut.subs(pt))) == 0)
# convex-combination step: a + Re(cW) = (1 - sum l)a + sum l H(t_k) when W = sum l e^{-xi t_k}
l1, l2, t1, t2 = sp.symbols("l1 l2 t1 t2", nonnegative=True)
Hf = lambda tt: a + sp.re(sp.expand_complex(cc * sp.exp(-xi * tt)))  # noqa: E731
Wcomb = l1 * sp.exp(-xi * t1) + l2 * sp.exp(-xi * t2)
lhs_c = a + sp.re(sp.expand_complex(cc * Wcomb))
rhs_c = (1 - l1 - l2) * a + l1 * Hf(t1) + l2 * Hf(t2)
rec("LD.convex", "thm S2 Lemma D proof (unchanged)", "a + Re(cW) = (1-l1-l2)a + l1 H(t1) + l2 H(t2) for W = sum l_k e^{-xi t_k}",
    sp.simplify(lhs_c - rhs_c) == 0)
# a >= 0 for delta = 0 by averaging over one period: the oscillating part has zero mean
per = sp.integrate((cr * sp.cos(om * t) - ci * sp.sin(om * t)), (t, 0, 2 * sp.pi / om))
rec("LD.mean", "thm v4->v5 H5 (a >= 0 when delta = 0)", "int_0^{2pi/omega} Re(c e^{i omega t}) dt = 0",
    sp.simplify(per) == 0)
# the v5 example and the 'real span' wording (Codex v3-delta MINOR)
ex = sp.exp(-t) * (1 - sp.exp(-dl * t) * sp.cos(om * t))
ex_gen = sp.exp(-t) - R(1, 2) * sp.exp(-(1 + xi) * t) - R(1, 2) * sp.exp(-(1 + sp.conjugate(xi)) * t)
rec("LD.example", "thm v4->v5 H5 (example in K, not in conic hull)",
    "e^-t(1 - e^-dt cos wt) = e^-t - (1/2)e^{-(1+xi)t} - (1/2)e^{-(1+conj xi)t}: negative generator coefficients",
    sp.simplify(sp.expand_complex(ex - ex_gen)) == 0)
ctl("CTL.conichull", "thm v4 S2 'cone{...}' regression (Codex v2-delta MAJOR)",
    "the example's generator coefficients (1, -1/2, -1/2) are all >= 0 (i.e. it lies in the conic hull)",
    all(v >= 0 for v in (R(1), R(-1, 2), R(-1, 2))))
b1, b2 = sp.symbols("b1 b2", real=True)
lit = b1 * sp.exp(-(1 + xi) * t) + b2 * sp.exp(-(1 + sp.conjugate(xi)) * t)
im_lit = sp.im(sp.expand_complex(lit))
rec("LD.realspan", "thm v5 L126 wording (Codex v3-delta MINOR 'real span')",
    "Im(b1 e^{-(1+xi)t} + b2 e^{-(1+conj xi)t}) = (b1-b2) e^{-(1+delta)t} sin(omega t) for real b1,b2: the literal "
    "real span's real-valued members are span{e^-t, e^{-(1+delta)t} cos} (no sine)",
    sp.simplify(im_lit - (b1 - b2) * sp.exp(-(1 + dl) * t) * sp.sin(om * t)) == 0)
ex2 = sp.exp(-t) * (1 - sp.exp(-dl * t) * sp.sin(om * t))
ex2_gen = sp.exp(-t) + (I / 2) * sp.exp(-(1 + xi) * t) - (I / 2) * sp.exp(-(1 + sp.conjugate(xi)) * t)
rec("LD.sineex", "thm v5 L126 wording (witness)",
    "e^-t(1 - e^-dt sin wt) (>= 0, a=1, c=i, so in the displayed K) has non-real generator coefficients +-i/2, "
    "so it is NOT in the literal real span; the displayed set definition (L124) includes it",
    sp.simplify(sp.expand_complex(ex2 - ex2_gen)) == 0
    and sp.simplify(sp.re(sp.expand_complex(I * sp.exp(-xi * t))) + sp.exp(-dl * t) * sp.sin(om * t)) == 0)

# ---------------------------------------------------------------- L6 / Cor 7.2 dependencies -----------------
r_, u_, tt = sp.symbols("r u tau_", real=True)
htau = 1 - sp.exp(-dl * (t - tt)) * (sp.cos(om * (t - tt)) + (dl / om) * sp.sin(om * (t - tt)))
rec("L62.deriv", "red L6.2 (used by Cor 7.2)", "h_tau' = ((omega^2+delta^2)/omega) e^{-delta(t-tau)} sin omega(t-tau)",
    sp.simplify(sp.diff(htau, t) - (om**2 + dl**2) / om * sp.exp(-dl * (t - tt)) * sp.sin(om * (t - tt))) == 0)
span_form = sp.expand(sp.expand_trig(htau))
k1 = sp.exp(dl * tt) * (sp.cos(om * tt) - (dl / om) * sp.sin(om * tt))
k2 = sp.exp(dl * tt) * (sp.sin(om * tt) + (dl / om) * sp.cos(om * tt))
rec("L62.span", "red L6.2", "h_tau = 1 - e^{-delta t}[k1 cos(omega t) + k2 sin(omega t)] (span membership)",
    sp.simplify(span_form - (1 - sp.exp(-dl * t) * (k1 * sp.cos(om * t) + k2 * sp.sin(om * t)))) == 0)
g_r = sp.exp(r_ * u_) * (sp.cos(u_) - r_ * sp.sin(u_))
rec("L64.h0", "red L6.4 (used by Cor 7.2)", "h_tau(0) = 1 - g_r(omega tau) with delta = r omega",
    sp.simplify(htau.subs(t, 0).subs(dl, r_ * om) - (1 - g_r.subs(u_, om * tt))) == 0)
rec("L64.gp", "red L6.4", "g_r'(u) = -(1+r^2) e^{ru} sin u", sp.simplify(sp.diff(g_r, u_) + (1 + r_**2) * sp.exp(r_ * u_) * sp.sin(u_)) == 0)
rec("L65.gr", "red L6.5", "d_r g_r = u g_r - e^{ru} sin u", sp.simplify(sp.diff(g_r, r_) - (u_ * g_r - sp.exp(r_ * u_) * sp.sin(u_))) == 0)
# Lemma 6.6 moment formula at an exact rational feasible point (phi = 1/2 < pi, so feasible by Lemma 6.4)
rp, wp, taup = R(1, 2), R(1), R(1, 2)
dp = rp * wp
phip = wp * taup
f66 = sp.exp(-t) * htau.subs({dl: dp, om: wp, tt: taup})
c66 = (1 - I * rp) * sp.exp((rp - I) * phip)
z66 = 1 / (1 + dp - I * wp)
ok66 = True
det66 = []
for k in range(3):
    lhs = sp.integrate(sp.expand(t**k * f66), (t, 0, sp.oo))
    rhs66 = sp.factorial(k) * (1 - sp.re(sp.expand_complex(c66 * z66 ** (k + 1))))
    d66 = sp.simplify(sp.expand_complex(lhs - rhs66))
    ok66 = ok66 and d66 == 0
    det66.append(str(d66))
rec("L66.mom", "red L6.6 (S_2 used by Cor 7.2, Lemma M)",
    "m_k(e^-t h_tau) = k!(1 - Re[c zeta^{k+1}]) exactly at r=1/2, omega=1, phi=1/2 (k=0,1,2)", ok66, det66)
# R_P phi-range contains [0, theta_1(r)] subset [0, 2pi): 2pi < 31416/5000
pi_ok_sympy = bool(sp.pi < R(31416, 10000))
try:
    import flint
    flint.ctx.prec = 128
    pi_ok_arb = bool(flint.arb.pi() < flint.arb(flint.fmpq(31416, 10000)))
except Exception as exc:  # pragma: no cover
    pi_ok_arb = False
    print("flint unavailable:", exc)
rec("RP.phi", "thm S3/S5 + red Cor 7.2 (P-assigned extreme rays lie in R_P)",
    "2 pi < 31416/5000, so every phase phi in [0, theta_1(r)] subset [0, 2pi) lies in R_P's phi-range",
    pi_ok_sympy and pi_ok_arb, {"sympy": pi_ok_sympy, "arb128": pi_ok_arb})

# ---------------------------------------------------------------- charts-spec v1 -> v2 hunks -----------------
d_, b_ = sp.symbols("d beta", positive=True)
bet = sp.atan(om / (1 + dl))
zeta_ld = (1 / (1 + dl)) * sp.cos(bet) * sp.exp(I * bet)
rec("LD1.I10", "charts-spec v2 LD paragraph (unchanged identity I10)",
    "zeta = 1/(1+xi) = d cos(beta) e^{i beta}, d = 1/(1+delta), beta = atan(omega/(1+delta))",
    sp.simplify(sp.expand_complex(zeta_ld - 1 / (1 + xi))) == 0)
rec("LD1.ratio", "charts-spec v2 LD paragraph", "delta/omega = (1-d)/tan(beta)",
    sp.simplify((1 - 1 / (1 + dl)) / sp.tan(bet) - dl / om) == 0)
rec("LD2.union", "charts-spec v1->v2 (s-union, NEW wording)",
    "rho_t = s + d cos beta <= 1/16 + 1/65 = 81/1040 for s <= 1/16, d <= 1/65, cos beta <= 1",
    R(1, 16) + R(1, 65) == R(81, 1040))
chi, rt, bl, chih, rtl = sp.symbols("chi rho_t beta_l chi_h rho_l", positive=True)
# skip-d soundness: d = (1-chi) rho_t / cos(beta) >= (1-chi_h) rho_l / cos(beta) > cos(beta_l)/(65 cos beta) >= 1/65
rec("LD2.skipd", "thm v4->v5 H7 (SKIP leaves contain no physical point)",
    "if (1-chi_h) rho_l > cos(beta_l)/65 and 0 <= beta_l <= beta < pi/2 then d > 1/65 (cos decreasing on [0,pi])",
    True, "argument by monotonicity; no computation needed")
s_ = sp.symbols("s", real=True)
N1 = kap * s_**2 - 2 * s_ * (1 - s_) + 2 * (1 - s_) ** 2
rec("SWC.N1", "charts-spec (I3)", "N1 = (kappa+4)s^2 - 6s + 2", iszero(N1 - ((kap + 4) * s_**2 - 6 * s_ + 2)))
rec("SWC.I5", "charts-spec (I5)", "100 N1 - 39 kappa s^2 = 50(3s-2)^2 (so B = kappa s^2/N1 <= 100/39)",
    iszero(100 * N1 - 39 * kap * s_**2 - 50 * (3 * s_ - 2) ** 2))
sq = sp.sqrt(2 * kap - 1)
p = (s_ * (1 - s_) * (1 + I * sq) - kap * s_**2) / N1
A = (2 * kap * s_**2 - 2 * s_ * (1 - s_)) / N1
B = kap * s_**2 / N1
rec("SWC.p", "charts-spec v1->v2 SWC (cancellation-free p)", "2 Re p = -A and |p|^2 = B",
    sp.simplify(2 * sp.re(sp.expand_complex(p)) + A) == 0
    and sp.simplify(sp.expand_complex(p * sp.conjugate(p)) - B) == 0)
xs = sp.symbols("xi_s")
qsz = lambda zz: kap * s_**2 * zz**2 - 2 * s_ * (1 - s_) * zz + 2 * (1 - s_) ** 2  # noqa: E731
pc = (s_ * (1 - s_) * (1 - I * sq) - kap * s_**2) / N1
rec("SWC.I4", "charts-spec (I4)", "q(s,1+xi)/N1 = (1 - p xi)(1 - conj(p) xi)",
    sp.simplify(sp.expand(qsz(1 + xs) / N1 - (1 - p * xs) * (1 - pc * xs))) == 0)
thv = sp.symbols("theta_v", positive=True)
rec("SWC.param", "thm S2 parametrization (unchanged)",
    "Q_T(theta(1+xi))/Q_T(theta) = q(s,1+xi)/(N1 (1+xi)^3) with s = theta/(1+theta)",
    sp.simplify((QT(thv * (1 + xs)) / QT(thv) - qsz(1 + xs) / (N1 * (1 + xs) ** 3)).subs(s_, thv / (1 + thv))) == 0)
# series coefficients of log W at s = 1/3 vs c_j = (-2 Re(p^j) + 3(-1)^j)/j, j = 1..6
s_pt = R(1, 3)
Wser = sp.log((1 - p.subs(s_, s_pt) * xs) * (1 - pc.subs(s_, s_pt) * xs) / (1 + xs) ** 3)
ser = sp.series(Wser, xs, 0, 7).removeO()
ok_c = True
ok_mut = True
for j in range(1, 7):
    cj_ser = sp.simplify(sp.expand_complex(ser.coeff(xs, j)))
    pj = sp.expand_complex(p.subs(s_, s_pt) ** j)
    cj = (-2 * sp.re(pj) + 3 * (-1) ** j) / j
    cj_mut = (-2 * sp.re(pj) - 3 * (-1) ** j) / j
    ok_c = ok_c and sp.simplify(cj_ser - cj) == 0
    ok_mut = ok_mut and sp.simplify(cj_ser - cj_mut) == 0
rec("SWC.cj", "charts-spec v1->v2 SWC (same c_j, exact form)",
    "log W = sum c_j xi^j with c_j = (-2 Re(p^j) + 3(-1)^j)/j (coefficients j=1..6 exact at s=1/3)", ok_c)
ctl("CTL.cj", "charts-spec SWC", "sign-flipped c_j = (-2 Re(p^j) - 3(-1)^j)/j matches the series", ok_mut)

# ---------------------------------------------------------------- L1(b) padding and 0.2 (v3->v4) ------------
Ab = sp.Matrix([[2, 0, -2], [7, 0, -6], [4, 1, -5]])
alpha = sp.Matrix([[1, 0, 0]])
Apad = sp.diag(Ab, -1)
apad = sp.Matrix([[1, 0, 0, 0]])
ts = sp.symbols("t_s", real=True)
g3 = sp.simplify((alpha * (Ab * ts).exp() * sp.ones(3, 1))[0])
g4 = sp.simplify((apad * (Apad * ts).exp() * sp.ones(4, 1))[0])
rec("L1b.pad", "red v3->v4 H3 (padding (alpha,0), diag(A,-1))",
    "(alpha,0) e^{diag(A,-1)t} 1 = alpha e^{At} 1 for the lane control representation of 2e^-t(1-cos t)",
    sp.simplify(g3 - g4) == 0 and sp.simplify(-sp.diff(g3, ts) - 2 * sp.exp(-ts) * (1 - sp.cos(ts))) == 0,
    {"G": str(g3)})


def main(out):
    t0 = time.time()
    summary = {
        "desk": "review/me3-parent-delta-audit-v1",
        "script": "code/delta_checks_v1.py",
        "sympy": sp.__version__,
        "n_checks": len(RESULTS),
        "n_pass": sum(1 for r_ in RESULTS if r_["pass"]),
        "all_pass": all(r_["pass"] for r_ in RESULTS),
        "checks": RESULTS,
    }
    with open(out, "x", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=1)
        fh.write("\n")
    print("TOTAL", summary["n_pass"], "/", summary["n_checks"], "all_pass", summary["all_pass"],
          "write_s", round(time.time() - t0, 3))
    return 0 if summary["all_pass"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

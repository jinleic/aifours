"""ME3 parent desk (ME3ParentPrimal): independent exact checks for reductions L3-L6 and the essential v_cos bounds.

Usage: red_checks_v1.py RUN_DIR
Arithmetic: sympy exact rationals/polynomials (Sturm-based root counting via Poly.count_roots, exact root isolation
via Poly.intervals / refine_root) and python-flint Arb balls built only from exact rationals (fmpq) and integers.
No Python floats, float literals or math.* enter any certified quantity. mpmath is not used.
Parts (results in RUN_DIR/RESULT.json, exclusive create):
  R1  L4: moments of (t - tau)^2 e^{-t} from the definition; P, Q; SOS for Delta3 > 1/4; derivative numerator
      = 8(tau^3 - 9 tau^2 + 18 tau - 6) = -48 L3(tau); exact isolation of the three real critical points; Arb values
      of s at them; Delta3 = s(x1); remainder identity s(x) = (x(9-x)^2 - 24)/24 mod the cubic; minimal polynomial by
      resultant and its irreducibility; Sturm certificates Delta3 > 2765/10000 and Delta3 > lo; exact upper bracket.
  R2  L3: face-ray SCVs and the Hermite-Genocchi kernel identity on four node triples (incl. confluent nodes).
  R3  L5: D1 algebraic forms (Lemma 5.3), the Lemma 5.4 identities, the tail constants (omega <= 1/4, omega >= 4)
      as exact rationals, and the ESSENTIAL upper bound v_cos <= SCV(omega0, phi0) < U < T (Arb, 320 bits).
  R4  L6: g_r', d_r g_r, h_tau', h_tau(0) = 1 - g_r(phi), span membership, double-zero determinant (exact sympy);
      theta1 brackets and an infeasible-ray control (Arb).
  R5  mutation controls (each must be rejected at the intended check).
"""
import sys
import os
import json
import time
from fractions import Fraction
import sympy as sp
import flint
from flint import arb, acb, fmpq

RUN = sys.argv[1]
res = {"script": "red_checks_v1.py", "started_epoch": time.time()}
allok = True


def rec(key, value, ok):
    global allok
    res[key] = {"value": value, "ok": bool(ok)}
    if not ok:
        allok = False


def qa(x):
    x = Fraction(x)
    return arb(fmpq(x.numerator, x.denominator))


def R(s):
    """Exact sympy rational from a decimal/fraction string."""
    return sp.Rational(s)


tau = sp.symbols("tau", real=True)
t = sp.symbols("t", positive=True)

# ===================================== R1: Delta3 ===================================================================
m = [sp.integrate(t ** k * (t - tau) ** 2 * sp.exp(-t), (t, 0, sp.oo)) for k in range(3)]
m_ok = all(sp.expand(m[k] - (sp.factorial(k + 2) - 2 * tau * sp.factorial(k + 1) + tau ** 2 * sp.factorial(k))) == 0
           for k in range(3))
P = sp.expand(m[0] * m[2])
Q = sp.expand(m[1])
P_ok = sp.expand(P - (tau ** 2 - 2 * tau + 2) * (2 * tau ** 2 - 12 * tau + 24)) == 0
Q_ok = sp.expand(Q - (tau ** 2 - 4 * tau + 6)) == 0 and sp.expand(Q - ((tau - 2) ** 2 + 2)) == 0
sos = sp.expand(4 * (P - sp.Rational(5, 4) * Q ** 2) - (3 * (tau ** 2 - 4 * tau + 2) ** 2 + 8 * tau ** 2))
Nnum = sp.expand(sp.diff(P, tau) * Q - 2 * P * sp.diff(Q, tau))
cub = tau ** 3 - 9 * tau ** 2 + 18 * tau - 6
L3 = 1 - 3 * tau + sp.Rational(3, 2) * tau ** 2 - sp.Rational(1, 6) * tau ** 3
der_ok = (sp.expand(Nnum - 8 * cub) == 0 and sp.expand(8 * cub + 48 * L3) == 0
          and sp.simplify(sp.diff(P / Q ** 2, tau) - Nnum / Q ** 3) == 0)
lim_ok = sp.limit(P / Q ** 2, tau, sp.oo) == 2 and sp.limit(P / Q ** 2, tau, -sp.oo) == 2
rec("R1a_moments_P_Q_SOS_derivative", {"moments_from_definition": m_ok, "P": P_ok, "Q": Q_ok,
                                       "SOS_residual": str(sos), "derivative_numerator": der_ok,
                                       "limits_1_plus_s_to_2": lim_ok},
    m_ok and P_ok and Q_ok and sos == 0 and der_ok and lim_ok)

flint.ctx.prec = 256
cpoly = sp.Poly(cub, tau)
ivs = cpoly.intervals()
roots_ok = len(ivs) == 3 and all(mult == 1 for (_, mult) in ivs)
eps = sp.Rational(1, 10 ** 40)
ref = [cpoly.refine_root(a, b, eps=eps) for ((a, b), _) in ivs]
ref = sorted(ref, key=lambda ab: ab[0])


def ball_of(a, b):
    return qa(Fraction(int(sp.numer(a)), int(sp.denom(a)))).union(qa(Fraction(int(sp.numer(b)), int(sp.denom(b)))))


def poly_arb(expr, x):
    pl = sp.Poly(expr, tau)
    acc = arb(0)
    for c in pl.all_coeffs():
        c = sp.Rational(c)
        acc = acc * x + qa(Fraction(int(c.p), int(c.q)))
    return acc


svals = []
for (a, b) in ref:
    x = ball_of(a, b)
    s = poly_arb(P, x) / (poly_arb(Q, x) ** 2) - 1
    svals.append(s)
order_ok = (svals[0] < svals[2]) and (svals[0] < 1) and (svals[0] < svals[1])
signs_ok = cpoly.eval(sp.Integer(-1000)) < 0 and sp.LC(cpoly) > 0
rem = sp.rem(sp.expand(24 * (P - Q ** 2) - Q ** 2 * (tau * (9 - tau) ** 2 - 24)), cub, tau)
y = sp.symbols("y")
resl = sp.resultant(cub, 24 * y - (tau * (9 - tau) ** 2 - 24), tau)
fl = sp.factor_list(resl)
minpoly = 32 * y ** 3 - 144 * y ** 2 + 135 * y - 27
minpoly_ok = len(fl[1]) == 1 and fl[1][0][1] == 1 and sp.expand(fl[1][0][0] * sp.Rational(32, sp.LC(fl[1][0][0], y))
                                                                   - minpoly) == 0
irreducible_ok = len(sp.factor_list(minpoly)[1]) == 1
d3ball = svals[0]
mp_at = minpoly.subs(y, 0)
lo27 = Fraction(2765, 10000)
lo = Fraction("0.2765825307809456")
hi = Fraction("0.2765825307809457")


def sturm_no_real_root(bound):
    pol = sp.Poly(sp.expand(P - (1 + sp.Rational(bound.numerator, bound.denominator)) * Q ** 2), tau)
    return pol.count_roots() == 0 and sp.LC(pol) > 0, pol.count_roots()


s27, n27 = sturm_no_real_root(lo27)
slo, nlo = sturm_no_real_root(lo)
a1, b1 = ref[0]
tau0 = (a1 + b1) / 2
Fhi = (P - (1 + sp.Rational(hi.numerator, hi.denominator)) * Q ** 2).subs(tau, tau0)
upper_ok = Fhi < 0
x1ball = ball_of(a1, b1)
rec("R1b_Delta3_isolation_value_minpoly_brackets", {
    "three_simple_real_critical_points": roots_ok,
    "critical_point_enclosures": [[str(sp.N(a, 25)), str(sp.N(b, 25))] for (a, b) in ref],
    "s_at_critical_points": [v.str(30) for v in svals],
    "s(x1)<s(x2),s(x3),1 (so Delta3=s(x1); s decreasing on (-inf,x1])": order_ok and signs_ok,
    "remainder_identity_residual": str(rem),
    "resultant_factor": str(fl), "minimal_polynomial_32y3-144y2+135y-27": minpoly_ok,
    "irreducible_over_Q": irreducible_ok,
    "Delta3_ball_256bit": d3ball.str(60, radius=True),
    "x1_ball": x1ball.str(40, radius=True),
    "x1_positive_so_attained_ray_tau=x1>=0": bool(x1ball > 0),
    "sturm_Delta3_gt_2765/10000": [s27, n27],
    "sturm_Delta3_gt_lo=0.2765825307809456": [slo, nlo],
    "exact_upper_bracket_at_rational_tau0_lt_hi=0.2765825307809457": bool(upper_ok),
    "tau0": str(tau0)},
    roots_ok and order_ok and signs_ok and rem == 0 and minpoly_ok and irreducible_ok and s27 and slo and upper_ok
    and bool(x1ball > 0) and bool(d3ball > qa(lo)) and bool(d3ball < qa(hi)))

# ===================================== R2: L3 face rays, Hermite-Genocchi ==========================================
k1, k2, kap = sp.symbols("kappa1 kappa2 kappa", positive=True)


def scv_of(f):
    mm = [sp.integrate(t ** k * f, (t, 0, sp.oo)) for k in range(3)]
    return sp.simplify(mm[0] * mm[2] / mm[1] ** 2 - 1)


s_exp = scv_of(sp.exp(-kap * t))
s_texp = scv_of(t * sp.exp(-kap * t))
s_diff = scv_of(sp.exp(-k1 * t) - sp.exp(-k2 * t))
face_ok = (sp.simplify(s_exp - 1) == 0 and sp.simplify(s_texp - sp.Rational(1, 2)) == 0
           and sp.simplify(s_diff - (k1 ** 2 + k2 ** 2) / (k1 + k2) ** 2) == 0
           and sp.expand(2 * (k1 ** 2 + k2 ** 2) - (k1 + k2) ** 2 - (k1 - k2) ** 2) == 0)
sv, u2, u3 = sp.symbols("s u2 u3", positive=True)
xv = sp.symbols("xv")
hg = []
for lam in ((1, 2, 3), (1, 1, 2), (1, 2, 2), (1, 1, 1)):
    integrand = sp.exp(-sv * ((1 - u2 - u3) * lam[0] + u2 * lam[1] + u3 * lam[2]))
    I2 = sp.integrate(sp.integrate(integrand, (u3, 0, 1 - u2)), (u2, 0, 1))
    phi = sp.exp(-sv * xv)
    # confluent divided difference by the standard recursion / derivative formula
    nodes = list(lam)

    def dd(ns):
        if len(ns) == 1:
            return phi.subs(xv, ns[0])
        if all(n_ == ns[0] for n_ in ns):
            return sp.diff(phi, xv, len(ns) - 1).subs(xv, ns[0]) / sp.factorial(len(ns) - 1)
        lo_, hi_ = ns[0], ns[-1]
        return (dd(ns[1:]) - dd(ns[:-1])) / (hi_ - lo_)

    resid = sp.simplify(sv ** 2 * I2 - dd(sorted(nodes)))
    hg.append({"nodes": lam, "residual": str(resid)})
rec("R2_face_rays_and_Hermite_Genocchi", {"face_scv_formulas": face_ok, "HG": hg},
    face_ok and all(h["residual"] == "0" for h in hg))

# ===================================== R3: D1 algebra, tails, essential U ===========================================
w = sp.symbols("omega", positive=True)
Cc, Ss = sp.symbols("C S", real=True)
q = 1 / (1 + w ** 2)
forms = []
for k in range(3):
    expr = (Cc - sp.I * Ss) * (1 - sp.I * w) ** 2 / (1 + w ** 2) * (1 - sp.I * w) ** (-(k + 1))
    re_ = sp.simplify(sp.re(sp.expand_complex(expr)))
    target = [q * (Cc - w * Ss), q * Cc, q ** 2 * (Cc + w * Ss)][k]
    forms.append(str(sp.simplify(re_ - target)))
# e^{-2 i beta} = (1 - i w)^2/(1 + w^2), beta = atan(w): checked through cos 2beta and sin 2beta (real identities)
beta_c = sp.simplify(sp.expand_trig(sp.cos(2 * sp.atan(w))) - (1 - w ** 2) / (1 + w ** 2))
beta_s = sp.simplify(sp.expand_trig(sp.sin(2 * sp.atan(w))) - 2 * w / (1 + w ** 2))
beta_t = sp.expand(((1 - w ** 2) - sp.I * 2 * w) - (1 - sp.I * w) ** 2)
beta_id = "0" if (beta_c == 0 and beta_s == 0 and beta_t == 0) else f"{beta_c}|{beta_s}|{beta_t}"
u = 1 - Cc
X = w ** 2 + u
Y = w * Ss
aa = w ** 2 * (1 + w ** 2)
a0 = 1 - q * (Cc - w * Ss)
a1_ = 1 - q * Cc
a2 = 1 - q ** 2 * (Cc + w * Ss)
alg = [sp.simplify(a0 - q * (X + Y)), sp.simplify(a1_ - q * X), sp.simplify(a2 - q ** 2 * (X + aa - Y)),
       sp.simplify(2 * a0 * a2 / a1_ ** 2 - 2 * (X + Y) * (X + aa - Y) / ((1 + w ** 2) * X ** 2))]
v, sm, sg = sp.symbols("v s_m sigma", nonnegative=True)
# step 2: u = w^2 v, Y_m = w^2 s_m with s_m^2 = v(2 - w^2 v)
Xv = w ** 2 * (1 + v)
lhs = Xv ** 2 + aa * Xv - aa * w ** 2 * sm - (w ** 2 * sm) ** 2
Nfun = (1 + v) ** 2 + (1 + w ** 2) * (1 + v - sm) - sm ** 2
step2 = sp.expand(lhs - w ** 4 * Nfun)
N0 = (1 + v) ** 2 + 1 + v - sg - 2 * v
step4 = sp.simplify((2 * N0 / (1 + v) ** 2).subs(v, sg ** 2 / 2)
                    - (P / Q ** 2).subs(tau, 2 - sg))
step4b = sp.expand(P.subs(tau, 2 - sg) - 2 * (sg ** 4 + 2 * sg ** 2 - 4 * sg + 8))
tail_low = (16 * lo27 - 1) / 17
rho_bar = Fraction(2426, 10000)
rho_sq_ok = rho_bar ** 2 > Fraction(1, 17)
Bbar = 2 * (1 - rho_bar) * (1 - rho_bar ** 3) / (1 + rho_bar ** 2) ** 2 - 1
Bclaim = Fraction(232498770764161, 700733376734161)
U = Fraction("0.2009015635005569588013806824561593216569")
Tq = Fraction(11, 50)
rec("R3a_D1_algebra_and_tail_constants", {
    "Re_forms_residuals": forms, "e^{-2i beta} identity": str(beta_id), "Lemma5.3_residuals": [str(x) for x in alg],
    "Lemma5.4_step2_residual": str(step2), "Lemma5.4_step4_residual": str(step4), "P(2-sigma)_residual": str(step4b),
    "tail_omega<=1/4_bound_(16*0.2765-1)/17": str(tail_low), "tail_low>2014/10000": tail_low > Fraction(2014, 10000),
    "rho_bar^2>1/17": rho_sq_ok, "B(rho_bar)": str(Bbar), "B==worker_claim": Bbar == Bclaim,
    "B>33/100": Bbar > Fraction(33, 100)},
    all(f == "0" for f in forms) and str(beta_id) == "0" and all(str(x) == "0" for x in alg) and step2 == 0
    and str(step4) == "0" and step4b == 0 and tail_low > Fraction(2014, 10000) and rho_sq_ok and Bbar == Bclaim
    and Bbar > Fraction(33, 100))

flint.ctx.prec = 320
w0 = Fraction(517966477543, 500000000000)
p0 = Fraction(674076484769, 2000000000000)
W0, P0 = qa(w0), qa(p0)


def d1_scv(Wb, Pb):
    e = acb(0, -1) * Pb
    E = e.exp()                                   # e^{-i phi}
    zinv = 1 / acb(1, -Wb)                        # (1 - i w)^{-1}
    a = []
    zz = zinv
    for k in range(3):
        a.append(1 - (E * zz).real)              # m_k / k!
        zz = zz * zinv
    return 2 * a[0] * a[2] / (a[1] * a[1]) - 1, a


S0, a_0 = d1_scv(W0, P0)
PI = arb.pi()
inbox = (w0 >= Fraction(1, 4)) and (w0 <= 4) and (p0 >= 0) and bool(qa(p0) < 2 * PI)
ess = {
    "SCV(omega0,phi0)_ball_320bit": S0.str(50, radius=True),
    "moments_positive": all(bool(x > 0) for x in a_0),
    "SCV<U": bool(S0 < qa(U)),
    "point_in_[1/4,4]x[0,2pi)": inbox,
    "U<2014/10000 (below both tail bounds)": U < Fraction(2014, 10000),
    "U<T=11/50": U < Tq,
    "U<1/4": U < Fraction(1, 4),
    "U<2765/10000<Delta3": U < lo27,
    "U<0.20090185 (contract band upper edge)": U < Fraction("0.20090185"),
}
# cross-check through the parent primal evaluator at r = 0 (same Arb library, different formula path)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p_core_v1 as PC  # noqa: E402
evp = PC.Evaluator(Tq, 320)
Pp0, Pp1, Pp2, _ = evp.base(qa(0), W0, P0)
b_ = [1 - Pp0.real, 1 - Pp1.real, 1 - Pp2.real]
S0b = 2 * b_[0] * b_[2] / (b_[1] * b_[1]) - 1
ess["cross_check_primal_evaluator_r=0_agrees_to_1e-80"] = bool(abs(S0b - S0) < qa(Fraction(1, 10 ** 80)))
rec("R3b_ESSENTIAL_vcos_upper_bound_U_lt_T", ess, all(v for k, v in ess.items() if not k.startswith("SCV(")))

# ===================================== R4: L6 feasibility (exact) ==================================================
rr, uu, ww, tt, ta = sp.symbols("r u w t tau_", real=True)
g = sp.exp(rr * uu) * (sp.cos(uu) - rr * sp.sin(uu))
g1 = sp.simplify(sp.diff(g, uu) + (1 + rr ** 2) * sp.exp(rr * uu) * sp.sin(uu))
g2 = sp.simplify(sp.diff(g, rr) - (uu * g - sp.exp(rr * uu) * sp.sin(uu)))
dl = rr * ww
hfun = 1 - sp.exp(-dl * (tt - ta)) * (sp.cos(ww * (tt - ta)) + rr * sp.sin(ww * (tt - ta)))
h1 = sp.simplify(sp.diff(hfun, tt) - ((ww ** 2 + dl ** 2) / ww) * sp.exp(-dl * (tt - ta)) * sp.sin(ww * (tt - ta)))
h0 = sp.simplify(hfun.subs(tt, 0) - (1 - g.subs(uu, ww * ta)))
htau = sp.simplify(hfun.subs(tt, ta))
span = sp.simplify(sp.expand(sp.expand_trig(hfun - (1 - sp.exp(dl * ta) * (
    (sp.cos(ww * ta) - rr * sp.sin(ww * ta)) * sp.exp(-dl * tt) * sp.cos(ww * tt)
    + (sp.sin(ww * ta) + rr * sp.cos(ww * ta)) * sp.exp(-dl * tt) * sp.sin(ww * tt))))))
bb, cc, de = sp.symbols("b c delta", real=True)
detm = sp.Matrix([[-de, ww], [-ww, -de]]).det()
rec("R4a_L6_exact_identities", {"g_r'": str(g1), "d_r g": str(g2), "h'": str(h1), "h(0)=1-g_r(phi)": str(h0),
                                "h(tau)": str(htau), "span": str(span), "det": str(sp.expand(detm))},
    all(str(x) == "0" for x in (g1, g2, h1, h0, htau, span)) and sp.expand(detm - (de ** 2 + ww ** 2)) == 0)

flint.ctx.prec = 256


def g_arb(r_, u_):
    return (r_ * u_).exp() * (u_.cos() - r_ * u_.sin())


brackets = []
br_ok = True
for (rv, lo_s, hi_s) in ((Fraction(3, 10), "4.65987805685937", "4.65987805685938"),
                         (Fraction(1), "3.94073313569291", "3.94073313569292"),
                         (Fraction(3), "3.46335292772992", "3.46335292772993")):
    gl = g_arb(qa(rv), qa(Fraction(lo_s))) - 1
    gh = g_arb(qa(rv), qa(Fraction(hi_s))) - 1
    okb = bool(gl < 0) and bool(gh > 0) and bool(qa(Fraction(lo_s)) > PI)
    br_ok = br_ok and okb
    brackets.append({"r": str(rv), "theta1_in": [lo_s, hi_s], "ok": okb})
# infeasible ray control: r = 3/10, w = 1, phi = theta1_hi + 1/100 gives h(0) = 1 - g < 0 (certified)
phi_bad = Fraction("4.65987805685938") + Fraction(1, 100)
h0bad = 1 - g_arb(qa(Fraction(3, 10)), qa(phi_bad))
rec("R4b_theta1_brackets_and_infeasible_ray", {"brackets": brackets, "h0_at_theta1+1/100": h0bad.str(20),
                                                 "negative": bool(h0bad < 0)}, br_ok and bool(h0bad < 0))

# ===================================== R5: mutation controls =======================================================
mut = {}
s_bad, n_bad = sturm_no_real_root(Fraction(2766, 10000))
mut["Delta3>0.2766_claim"] = {"sturm_no_root": s_bad, "real_roots": n_bad, "rejected": not s_bad}
sos7 = sp.expand(4 * (P - sp.Rational(5, 4) * Q ** 2) - (3 * (tau ** 2 - 4 * tau + 2) ** 2 + 7 * tau ** 2))
mut["SOS_coefficient_8_to_7"] = {"residual": str(sos7), "rejected": sos7 != 0}
flint.ctx.prec = 320
S0 = d1_scv(W0, P0)[0]
lowS = S0.lower()
# exact rational strictly below the certified ball: decimal of the lower endpoint (50 digits) minus 1e-45
Ubad = Fraction(lowS.str(50, radius=False)) - Fraction(1, 10 ** 45)
mut["U_below_value_at_point"] = {"U_bad": str(Ubad), "SCV<U_bad_certified": bool(S0 < qa(Ubad)),
                                 "rejected": not bool(S0 < qa(Ubad))}
tail_half = (lo27 - Fraction(1, 4)) / (1 + Fraction(1, 4))
mut["tail_at_omega<=1/2"] = {"bound": str(tail_half), "rejected": not (tail_half > U)}
rho_b2 = Fraction(2425, 10000)
mut["rho_bar=0.2425"] = {"rho^2>1/17": rho_b2 ** 2 > Fraction(1, 17), "rejected": not (rho_b2 ** 2 > Fraction(1, 17))}
flint.ctx.prec = 256
hfeas = 1 - g_arb(qa(Fraction(3, 10)), qa(Fraction("4.65987805685937") - Fraction(1, 100)))
mut["feasible_ray_claimed_infeasible"] = {"h0": hfeas.str(20), "rejected": not bool(hfeas < 0)}
rec("R5_mutation_controls", mut, all(x["rejected"] for x in mut.values()))

res["all_ok"] = allok
res["elapsed_seconds"] = round(time.time() - res["started_epoch"], 2)
with open(os.path.join(RUN, "RESULT.json"), "x") as fh:
    json.dump(res, fh, indent=1, default=str)
print("RESULT", "PASS" if allok else "FAIL", json.dumps({k: v["ok"] for k, v in res.items() if isinstance(v, dict)}))
sys.exit(0 if allok else 1)

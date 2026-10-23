"""Control (b) for reduction L4: Delta3 := inf_{tau real} SCV(e^{-t}(t - tau)^2).

CERTIFIED parts use exact sympy rational arithmetic (Sturm real-root counts, polynomial identities, remainders) and
python-flint arb balls on exact rational root-isolating intervals.  Nothing here is a float-only claim.

(b1) moments m0 = tau^2-2tau+2, m1 = tau^2-4tau+6, m2 = 2tau^2-12tau+24 (two independent exact computations).
(b2) SOS certificate: 4*(P - (5/4) Q^2) = 3 (tau^2 - 4 tau + 2)^2 + 8 tau^2 with P = m0 m2, Q = m1  => s(tau) > 1/4.
(b3) s'(tau) = N/Q^3 with N = P'Q - 2PQ' = 8 (tau^3 - 9 tau^2 + 18 tau - 6) = -48 L_3(tau) (Laguerre); the three real
     roots x1 < x2 < x3 of the cubic are isolated exactly; Delta3 = s(x1) (sign pattern of s').
(b4) Exact identity s(x) = (x (9 - x)^2 - 24)/24 modulo the cubic; Vieta => s(x1) = (x3 - x2)^2/(4 x2 x3)
     (Battagliola-Peralta "relative gap" form); minimal polynomial of Delta3 via a resultant.
(b5) arb enclosure of Delta3 (>= 60 digits) and an exact 16-digit rational bracket lo < Delta3 < hi:
     lo by "P - (1+lo) Q^2 has no real root and positive leading coefficient", hi by exact evaluation at a rational tau0.
(b6) Mutation controls: each mutated certificate must be rejected for the intended reason.
"""
import os
import sys
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import sympy as sp  # noqa: E402
from flint import arb, fmpq, ctx  # noqa: E402

RUN = sys.argv[1]
T0 = time.time()
ctx.prec = 512
out = {"script": "ctl_b_delta3_v1.py", "label_default": "CERTIFIED (exact sympy / arb balls, prec=512 bits)"}
checks = {}


def record(name, ok, detail=None):
    checks[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        print("FAIL", name, detail)


def to_fmpq(q):
    q = sp.Rational(q)
    return fmpq(int(q.p), int(q.q))


tau = sp.Symbol("tau", real=True)
t = sp.Symbol("t", positive=True)


# ---------------- (b1) moments, two ways
def mom_factorial(k):
    poly = sp.Poly(sp.expand(t ** k * (t - tau) ** 2), t)
    return sp.expand(sum(c * sp.factorial(mon[0]) for mon, c in zip(poly.monoms(), poly.coeffs())))


m_fact = [mom_factorial(k) for k in range(3)]
m_int = [sp.expand(sp.integrate(sp.expand(t ** k * (t - tau) ** 2) * sp.exp(-t), (t, 0, sp.oo))) for k in range(3)]
m_claim = [tau ** 2 - 2 * tau + 2, tau ** 2 - 4 * tau + 6, 2 * tau ** 2 - 12 * tau + 24]
record("b1_moments_factorial", all(sp.expand(a - b) == 0 for a, b in zip(m_fact, m_claim)), [str(x) for x in m_fact])
record("b1_moments_integrate", all(sp.expand(a - b) == 0 for a, b in zip(m_int, m_claim)), [str(x) for x in m_int])
P = sp.expand(m_claim[0] * m_claim[2])
Q = m_claim[1]
record("b1_Q_eq_(tau-2)^2+2", sp.expand(Q - ((tau - 2) ** 2 + 2)) == 0)
s_expr = P / Q ** 2 - 1
record("b1_s(0)_eq_1/3", sp.nsimplify(s_expr.subs(tau, 0)) == sp.Rational(1, 3))
record("b1_s_to_1_at_+-inf", sp.limit(s_expr, tau, sp.oo) == 1 and sp.limit(s_expr, tau, -sp.oo) == 1)

# ---------------- (b2) SOS certificate for s > 1/4
quart = sp.expand(4 * (P - sp.Rational(5, 4) * Q ** 2))
sos = 3 * (tau ** 2 - 4 * tau + 2) ** 2 + 8 * tau ** 2
record("b2_SOS_identity", sp.expand(quart - sos) == 0, {"quartic": str(quart), "sos": str(sos)})
record("b2_SOS_strict(no common zero: tau=0 gives 12)", sos.subs(tau, 0) == 12)
record("b2_quartic_no_real_root(Sturm)", sp.Poly(quart, tau).count_roots() == 0)

# ---------------- (b3) critical points = zeros of Laguerre L3
Nn = sp.expand(sp.diff(P, tau) * Q - 2 * P * sp.diff(Q, tau))
cubic = tau ** 3 - 9 * tau ** 2 + 18 * tau - 6
L3 = sp.expand(sp.laguerre(3, tau))
record("b3_N_eq_8cubic", sp.expand(Nn - 8 * cubic) == 0, str(Nn))
record("b3_N_eq_-48L3", sp.expand(Nn + 48 * L3) == 0, str(L3))
record("b3_ds_eq_N_over_Q3", sp.simplify(sp.diff(P / Q ** 2, tau) - Nn / Q ** 3) == 0)
cpoly = sp.Poly(cubic, tau)
ivs = cpoly.intervals(eps=sp.Rational(1, 10 ** 80))
ivs = sorted(ivs, key=lambda iv: iv[0][0])
record("b3_three_simple_real_roots", len(ivs) == 3 and all(m == 1 for (_, m) in ivs))
X = []
for (a, b), _ in ivs:
    X.append(arb(to_fmpq(a)).union(arb(to_fmpq(b))))


def s_arb(x):
    Pn = (x * x - 2 * x + 2) * (2 * x * x - 12 * x + 24)
    Qn = x * x - 4 * x + 6
    return Pn / (Qn * Qn) - 1


sv = [s_arb(x) for x in X]
D3 = sv[0]
record("b3_s(x1)<s(x3)", bool(D3 < sv[2]), [v.str(20) for v in sv])
record("b3_s(x1)<s(x2)", bool(D3 < sv[1]))
out["b3"] = {"roots_x1_x2_x3": [x.str(40) for x in X], "s_at_roots": [v.str(40) for v in sv],
             "sign_argument": "leading coeff of cubic > 0: s' < 0 on (-inf,x1), > 0 on (x1,x2), < 0 on (x2,x3), > 0 on "
                              "(x3,inf); s -> 1 at +-inf; so min_R s = min(s(x1), s(x3)) = s(x1)"}

# ---------------- (b4) Laguerre-gap identity and minimal polynomial
Eexpr = (tau * (9 - tau) ** 2 - 24) / 24
num = sp.numer(sp.together(s_expr - Eexpr))
record("b4_s_eq_E_mod_cubic", sp.rem(sp.expand(num), cubic, tau) == 0)
x = sp.Symbol("x", positive=True)
vieta = sp.simplify(((9 - x) ** 2 - 24 / x) / (24 / x) - (x * (9 - x) ** 2 - 24) / 24)
record("b4_vieta_form", vieta == 0)
gap = (X[2] - X[1]) ** 2 / (4 * X[1] * X[2])
record("b4_BP_gap_overlaps_Delta3", bool(gap.overlaps(D3)), gap.str(40))
y = sp.Symbol("y")
res = sp.Poly(sp.resultant(sp.Poly(cubic, tau).as_expr(), 24 * y - tau * (9 - tau) ** 2 + 24, tau), y)
res_monic = sp.Poly(res.monic(), y)
record("b4_minpoly_irreducible", res_monic.is_irreducible, str(res_monic.as_expr()))
coeffs = [to_fmpq(c) for c in res_monic.all_coeffs()]
valD = arb(0)
for c in coeffs:
    valD = valD * D3 + arb(c)
record("b4_Delta3_root_of_minpoly", bool(valD.contains(0)), valD.str(5))
out["b4"] = {"BP_gap_(x3-x2)^2/(4x2x3)": gap.str(40), "minimal_polynomial_of_Delta3": str(res_monic.as_expr())}

# ---------------- (b5) enclosure and exact rational bracket
mid40 = D3.mid().str(45, radius=False)
Dq = sp.Rational(mid40)
lo = sp.floor(Dq * 10 ** 16) / sp.Integer(10) ** 16
hi = sp.ceiling(Dq * 10 ** 16) / sp.Integer(10) ** 16
qlo = sp.Poly(sp.expand(P - (1 + lo) * Q ** 2), tau)
lo_ok = (qlo.LC() > 0) and (qlo.count_roots() == 0)
record("b5_lower_bracket_lo_lt_Delta3", lo_ok, {"lo": str(lo), "LC": str(qlo.LC())})
tau0 = (ivs[0][0][0] + ivs[0][0][1]) / 2
val_hi = sp.expand(P - (1 + hi) * Q ** 2).subs(tau, tau0)
record("b5_upper_bracket_Delta3_lt_hi", val_hi < 0, {"hi": str(hi), "tau0_float": str(sp.N(tau0, 30))})
q2765 = sp.Poly(sp.expand(P - (1 + sp.Rational(2765, 10000)) * Q ** 2), tau)
record("b5_Delta3_gt_0.2765", q2765.LC() > 0 and q2765.count_roots() == 0)
out["b5"] = {"Delta3_arb_enclosure": D3.str(70), "Delta3_mid_45_digits": mid40, "lo": str(lo), "hi": str(hi),
             "lo_decimal": str(sp.N(lo, 20)), "hi_decimal": str(sp.N(hi, 20)),
             "x1_minimizer": X[0].str(40), "1/Delta3": (1 / D3).str(30)}

# ---------------- (b6) mutation controls (each must FAIL its certificate check)
mut = {}
qbad = sp.Poly(sp.expand(P - (1 + sp.Rational(2766, 10000)) * Q ** 2), tau)
wit = sp.Rational(21, 50)
mut["M1_claim_s_gt_0.2766_everywhere"] = {
    "real_root_count": int(qbad.count_roots()), "rejected": qbad.count_roots() > 0,
    "witness_tau": str(wit), "s(witness)_exact": str(sp.nsimplify(s_expr.subs(tau, wit))),
    "s(witness)<0.2766": bool(s_expr.subs(tau, wit) < sp.Rational(2766, 10000))}
sos_bad = 3 * (tau ** 2 - 4 * tau + 2) ** 2 + 7 * tau ** 2
mut["M2_SOS_coefficient_8_to_7"] = {"identity_residual": str(sp.expand(quart - sos_bad)),
                                    "rejected": sp.expand(quart - sos_bad) != 0}
hi_bad = lo - sp.Rational(1, 10 ** 16)
val_bad = sp.expand(P - (1 + hi_bad) * Q ** 2).subs(tau, tau0)
qhb = sp.Poly(sp.expand(P - (1 + hi_bad) * Q ** 2), tau)
mut["M3_claim_Delta3_lt_lo-1e-16"] = {"value_at_tau0_sign_positive": bool(val_bad > 0),
                                      "no_real_root_so_s_gt_claim_everywhere": qhb.count_roots() == 0,
                                      "rejected": bool(val_bad > 0)}
mut["M4_wrong_root_box_x2_instead_of_x1"] = {"s(x2)": sv[1].str(20), "outside_bracket": bool(sv[1] > arb(to_fmpq(hi))),
                                             "rejected": bool(sv[1] > arb(to_fmpq(hi)))}
record("b6_all_mutations_rejected", all(v["rejected"] for v in mut.values()))
record("b6_M1_witness_below_0.2766", mut["M1_claim_s_gt_0.2766_everywhere"]["s(witness)<0.2766"])
out["b6_mutations"] = mut

out["checks"] = checks
out["all_pass"] = all(v["pass"] for v in checks.values())
out["elapsed_s"] = round(time.time() - T0, 2)
with lane_guard.xopen(os.path.join(RUN, "ctl_b.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "n_checks": len(checks),
                  "failed": [k for k, v in checks.items() if not v["pass"]],
                  "Delta3": D3.str(30), "lo": str(sp.N(lo, 20)), "hi": str(sp.N(hi, 20)),
                  "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if out["all_pass"] else 1)

"""Control (d): HSTZ 2016 eq.(4)/Table 2 convention (order 3: omega = 1.03593, phi = 0.337037).

CERTIFIED: python-flint acb/arb (prec 256) closed-form moments at the exact rational parameters.
EXPLORATORY: independent mpmath quadrature (50 digits) of the same moments (an independent evaluator).

(d1) literal reading  f = e^{-t} cos^2(1.03593 t - 0.337037) = e^{-t}(1 + cos(2 omega t - 2 phi))/2  -> SCV ~ 1.5757,
     inconsistent with HSTZ Table 1 (cv = 0.20090, 1/cv = 4.9776): REJECTED as a convention error.
(d2) reading f = e^{-t}(1 - cos(omega t - phi)) -> SCV ~ 0.2009015635, matching Table 1 and the contract constant.
(d3) half-frequency cos^2 form e^{-t} cos^2((omega/2) t - (phi/2 + pi/2)) = (1/2) e^{-t}(1 - cos(omega t - phi)):
     exact sympy identity and an arb evaluation with its own formula reproduce the same SCV.
(d4) the '+' variant e^{-t}(1 + cos(omega t - phi)) = 2 e^{-t} cos^2(omega t/2 - phi/2) for comparison.
"""
import os
import sys
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from flint import arb, acb, fmpq, ctx  # noqa: E402

RUN = sys.argv[1]
T0 = time.time()
ctx.prec = 256
out = {"script": "ctl_d_hstz_v1.py"}
checks = {}


def record(name, ok, detail=None):
    checks[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        print("FAIL", name, detail)


W = arb(fmpq(103593, 100000))
PH = arb(fmpq(337037, 1000000))
PI = arb.pi()


def scv_from_m(m):
    return m[0] * m[2] / (m[1] * m[1]) - 1


def moments_1_sign_cos(sign, Om, Ph):
    """m_k of e^{-t}(1 + sign*cos(Om t - Ph)): k!(1 + sign*Re[e^{-i Ph}(1 - i Om)^{-(k+1)}])."""
    z = 1 / acb(1, -Om)
    e = acb(Ph.cos(), -Ph.sin())
    m = []
    zk = z
    fact = [1, 1, 2]
    for k in range(3):
        m.append(fact[k] * (1 + sign * (e * zk).real))
        zk = zk * z
    return m


def moments_cos2(Om, Ph):
    """m_k of e^{-t} cos^2(Om t - Ph) = e^{-t}(1 + cos(2 Om t - 2 Ph))/2."""
    m = moments_1_sign_cos(+1, 2 * Om, 2 * Ph)
    return [x / 2 for x in m]


m_lit = moments_cos2(W, PH)
S_lit = scv_from_m(m_lit)
m_ok = moments_1_sign_cos(-1, W, PH)
S_ok = scv_from_m(m_ok)
m_half = moments_cos2(W / 2, PH / 2 + PI / 2)
S_half = scv_from_m(m_half)
m_plus = moments_1_sign_cos(+1, W, PH)
S_plus = scv_from_m(m_plus)
record("d1_literal_SCV_in_[1.575,1.576]", bool(S_lit > arb("1.575")) and bool(S_lit < arb("1.576")), S_lit.str(20))
record("d1_literal_rejected_vs_Table1_cv_0.20090", bool(abs(S_lit - arb("0.20090")) > arb("1")))
record("d2_1-cos_SCV_matches_0.2009015635", bool(abs(S_ok - arb("0.2009015635")) < arb("1e-10")), S_ok.str(20))
record("d2_1/SCV_matches_Table1_4.9776", bool(abs(1 / S_ok - arb("4.9776")) < arb("1e-4")), (1 / S_ok).str(15))
record("d3_half_frequency_cos2_same_SCV", bool((S_half - S_ok).contains(0)) and S_half.rad() < arb("1e-60"),
       S_half.str(30))
record("d3_half_frequency_moments_are_half", all(bool((2 * a - b).contains(0)) for a, b in zip(m_half, m_ok)))
x = sp.Symbol("x", real=True)
ident = sp.simplify(1 - sp.cos(x) - 2 * sp.cos(x / 2 - sp.pi / 2) ** 2)
record("d3_sympy_identity_1-cos(x)=2cos^2(x/2-pi/2)", ident == 0, str(ident))
ident2 = sp.simplify(sp.cos(x) ** 2 - (1 + sp.cos(2 * x)) / 2)
record("d3_sympy_identity_cos^2", ident2 == 0, str(ident2))
record("d4_plus_variant_differs", bool(abs(S_plus - S_ok) > arb("0.1")), S_plus.str(20))

# EXPLORATORY independent evaluator: mpmath quadrature of the moments
mp.mp.dps = 50
w_ = mp.mpf(103593) / 100000
p_ = mp.mpf(337037) / 1000000
cuts = [0, 2, 5, 10, 20, 40, 80, 160, mp.inf]


def quad_scv(fn):
    m = [mp.quad(lambda tt: tt ** k * fn(tt), cuts) for k in range(3)]
    return m[0] * m[2] / m[1] ** 2 - 1


q_lit = quad_scv(lambda tt: mp.exp(-tt) * mp.cos(w_ * tt - p_) ** 2)
q_ok = quad_scv(lambda tt: mp.exp(-tt) * (1 - mp.cos(w_ * tt - p_)))
q_half = quad_scv(lambda tt: mp.exp(-tt) * mp.cos(w_ / 2 * tt - (p_ / 2 + mp.pi / 2)) ** 2)
record("dq_quadrature_literal_agrees_EXPLORATORY", abs(q_lit - mp.mpf(S_lit.mid().str(40, radius=False))) < mp.mpf("1e-30"),
       mp.nstr(q_lit, 25))
record("dq_quadrature_1-cos_agrees_EXPLORATORY", abs(q_ok - mp.mpf(S_ok.mid().str(40, radius=False))) < mp.mpf("1e-30"),
       mp.nstr(q_ok, 25))
record("dq_quadrature_half_agrees_EXPLORATORY", abs(q_half - q_ok) < mp.mpf("1e-30"), mp.nstr(q_half, 25))

out["values"] = {
    "params": {"omega": "103593/100000", "phi": "337037/1000000"},
    "literal_e^{-t}cos^2(omega t - phi)": {"SCV": S_lit.str(30), "moments": [v.str(25) for v in m_lit],
                                          "quadrature_EXPLORATORY": mp.nstr(q_lit, 30)},
    "e^{-t}(1-cos(omega t - phi))": {"SCV": S_ok.str(30), "1/SCV": (1 / S_ok).str(25), "moments": [v.str(25) for v in m_ok],
                                    "quadrature_EXPLORATORY": mp.nstr(q_ok, 30)},
    "half_freq_e^{-t}cos^2((omega/2)t-(phi/2+pi/2))": {"SCV": S_half.str(30), "quadrature_EXPLORATORY": mp.nstr(q_half, 30)},
    "plus_variant_e^{-t}(1+cos(omega t - phi))": {"SCV": S_plus.str(30)},
    "HSTZ_Table1_order3": {"cv": "0.20090", "1/cv": "4.9776"},
    "verdict": "literal eq.(4) reading with Table 2 numbers gives SCV ~1.5757, inconsistent with Table 1: convention "
               "error, rejected. Table 2 numbers are the (omega, phi) of e^{-t}(1 - cos(omega t - phi)), i.e. of the "
               "cos^2 form with half frequency omega/2 and phase phi/2 + pi/2."}
out["checks"] = checks
out["all_pass"] = all(v["pass"] for v in checks.values())
out["elapsed_s"] = round(time.time() - T0, 2)
with lane_guard.xopen(os.path.join(RUN, "ctl_d.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "n_checks": len(checks),
                  "failed": [k for k, v in checks.items() if not v["pass"]],
                  "SCV_literal": S_lit.str(12), "SCV_1-cos": S_ok.str(15), "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if out["all_pass"] else 1)

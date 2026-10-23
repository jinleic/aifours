"""Exact certificates for reductions-v2 (fix (3) of review me3-reductions-codex-v1.note.md, sha256 a6d34ecb...1328).

Every decision uses Python fractions.Fraction (stdlib) on exact rationals / Gaussian rationals.  sympy is used only for
independent EXACT cross-checks (Rational, Poly, rem, integrate).  No floats: a start-up AST self-scan rejects float or
complex literals, calls to float()/complex(), and the numeric evaluators evalf/N/nsimplify; decimal displays are
produced by exact integer division (truncation).

C1  Upper separation (reductions-v2 Theorem 5.6).  omega = 1, cos phi = 35/37, sin phi = 12/37 (a real phi exists since
    c^2 + s^2 = 1).  Lemma 5.2: m_k = k! (1 - Re[e^{-i phi} (1 - i omega)^{-(k+1)}]), computed in exact Gaussian
    rationals -> (m0, m1, m2) = (27, 62, 171)/74 and SCV = m0 m2/m1^2 - 1 = 773/3844.
    Cross-checks: Lemma 5.3 algebraic form (cos/sin of 2 atan(omega) are rational in omega); sympy exact integration of
    int_0^oo t^k e^{-t} (1 - cos(t - phi)) dt with cos(t - phi) = c cos t + s sin t.
    Comparisons (exact): 773/3844 < 1007/5000 (= 0.2014) < 11/50 = T; 773/3844 < 428/2125 (Lemma 5.4 tail bound at
    omega <= 1/4 given Delta3 > 553/2000); 773/3844 < Lemma 5.5 tail constant (rho_bar = 1213/5000, rho_bar^2 > 1/17);
    773/3844 < 553/2000 < Delta3.
C2  Delta3 > 553/2000 (reductions-v2 Lemma 4.2), Delta3 := inf_tau s(tau), s(tau) = SCV((t - tau)^2 e^{-t}).
    (a) m_k((t-tau)^2 e^{-t}) = (k+2)! - 2 tau (k+1)! + tau^2 k!  ->  P = m0 m2, Q = m1;  s = P/Q^2 - 1.
    (b) Q = (tau - 2)^2 + 2 > 0;  4 (P - 5/4 Q^2) = 3 (tau^2 - 4 tau + 2)^2 + 8 tau^2 (no common zero) -> s > 1/4.
    (c) P'Q - 2 P Q' = 8 q, q = tau^3 - 9 tau^2 + 18 tau - 6;  exact signs of q at 0, 1/2, 2, 3, 6, 7 isolate the three
        roots x1 in (0, 1/2), x2 in (2, 3), x3 in (6, 7);  LC(P) = 2, LC(Q^2) = 1 -> s -> 1 at +-oo.
    (d) s(0) = 1/3; 2P - 3Q^2 = tau^4 - 8 tau^3 + 20 tau^2 - 12 = tau^2((tau - 4)^2 + 4) - 12 > 0 for tau >= 6, so
        s(x3) > 1/2;  s decreasing on (-oo, x1] gives s(x1) < s(0) = 1/3;  hence Delta3 = s(x1) in (1/4, 1/3).
    (e) Q^6 h(s) = 32 (P - Q^2)^3 - 144 (P - Q^2)^2 Q^2 + 135 (P - Q^2) Q^4 - 27 Q^6 has remainder 0 mod q, so
        h(Delta3) = 0 with h(y) = 32 y^3 - 144 y^2 + 135 y - 27 (cross-check through E(x) = (x (9 - x)^2 - 24)/24).
    (f) h'(y) = 96 (y - 3/2)^2 - 81 >= 96 (7/6)^2 - 81 = 149/3 > 0 on [1/4, 1/3] (= h'(1/3), the minimum there);
        h(1/4) = -7/4 < 0 < 86/27 = h(1/3);  Delta3 is the unique root of h in [1/4, 1/3].
    (g) h(553/2000) = -1293623/250000000 < 0 with 553/2000 in [1/4, 1/3]  ->  Delta3 > 553/2000.
Wrong controls (each MUST fail): W1 swapped cos/sin; W2 h(2766/10000) > 0 (wrong sign: does not certify
Delta3 > 2766/10000); W4 point 1/5 outside the monotonicity window; W5 a pair with c^2 + s^2 != 1; W6 phase-sign
mutation e^{+i phi} in Lemma 5.2.  Reported, not a control: h(552/2000) < 0 only certifies the weaker Delta3 > 0.276.
"""
import os
import sys
import ast
import json
import time
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import sympy as sp  # noqa: E402

RUN = sys.argv[1]
T0 = time.monotonic_ns()

# ---------------- no-float self-scan
with open(os.path.abspath(__file__), "r") as fh:
    _tree = ast.parse(fh.read())
_bad = []
_ALLOWED_CONST = (bool, int, str, bytes, type(None))
for node in ast.walk(_tree):
    if isinstance(node, ast.Constant) and not isinstance(node.value, _ALLOWED_CONST):
        _bad.append(("non-exact literal", node.lineno))
    if isinstance(node, ast.Name) and node.id in ("fl" + "oat", "com" + "plex"):
        _bad.append(("name " + node.id, node.lineno))
    if isinstance(node, ast.Attribute) and node.attr in ("evalf", "N", "nsimplify", "nroots", "Float", "time"):
        _bad.append(("attribute " + node.attr, node.lineno))
assert not _bad, _bad

out = {"script": "exact_certs_v1.py", "label": "EXACT (fractions.Fraction decisions; sympy exact cross-checks)",
       "no_float_self_scan": "passed"}
checks = {}


def record(name, ok, detail=None):
    checks[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        print("FAIL", name, detail)


def dec(x, n=15):
    """Exact truncated decimal display of a Fraction (no floats)."""
    sgn = "-" if x < 0 else ""
    x = abs(x)
    ip = x.numerator // x.denominator
    fp = (x - ip) * 10 ** n
    return "%s%d.%0*d" % (sgn, ip, n, fp.numerator // fp.denominator)


def fs(x):
    return str(x)


# ---------------- Gaussian rationals
def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cinv(a):
    d = a[0] * a[0] + a[1] * a[1]
    return (a[0] / d, -a[1] / d)


FACT = [Fr(1), Fr(1), Fr(2)]
T = Fr(11, 50)
B2014 = Fr(1007, 5000)
D3_LO = Fr(553, 2000)


def d1_moments(omega, c, s, phase_sign=-1):
    """Lemma 5.2 with e^{phase_sign * i phi} (correct formula: phase_sign = -1)."""
    e = (c, phase_sign * s)
    z = cinv((Fr(1), -omega))
    zk = z
    m = []
    for k in range(3):
        m.append(FACT[k] * (1 - cmul(e, zk)[0]))
        zk = cmul(zk, z)
    return m


def d1_moments_lemma53(omega, c, s):
    """Lemma 5.3: psi = phi - 2 beta, tan beta = omega; cos 2beta = (1-w^2)/(1+w^2), sin 2beta = 2w/(1+w^2)."""
    w2 = omega * omega
    c2b, s2b = (1 - w2) / (1 + w2), 2 * omega / (1 + w2)
    C = c * c2b + s * s2b
    S = s * c2b - c * s2b
    u = 1 - C
    X = w2 + u
    a = w2 * (1 + w2)
    Y = omega * S
    return [(X + Y) / (1 + w2), X / (1 + w2), 2 * (X + a - Y) / (1 + w2) ** 2]


def scv(m):
    return m[0] * m[2] / (m[1] * m[1]) - 1


def upper_certificate(omega, c, s, phase_sign=-1):
    """Returns (certified?, details): certified iff c^2 + s^2 = 1, m1 > 0 and SCV < 1007/5000."""
    if c * c + s * s != 1:
        return False, {"reason": "c^2 + s^2 != 1", "c2+s2": fs(c * c + s * s)}
    m = d1_moments(omega, c, s, phase_sign)
    if m[1] <= 0:
        return False, {"reason": "m1 <= 0"}
    v = scv(m)
    return v < B2014, {"moments": [fs(x) for x in m], "SCV": fs(v), "SCV_decimal": dec(v),
                       "SCV<1007/5000": v < B2014}


# ======================= C1 upper separation
c0, s0 = Fr(35, 37), Fr(12, 37)
record("C1_pythagoras_35/37_12/37", c0 * c0 + s0 * s0 == 1, fs(c0 * c0 + s0 * s0))
m = d1_moments(Fr(1), c0, s0)
record("C1_moments_eq_(27,62,171)/74", m == [Fr(27, 74), Fr(62, 74), Fr(171, 74)], [fs(x) for x in m])
V = scv(m)
record("C1_SCV_eq_773/3844", V == Fr(773, 3844), fs(V))
m53 = d1_moments_lemma53(Fr(1), c0, s0)
record("C1_lemma5.3_form_agrees", m53 == m, [fs(x) for x in m53])
# sympy exact integration (independent of Lemmas 5.2/5.3)
t = sp.Symbol("t", positive=True)
fsym = sp.exp(-t) * (1 - sp.Rational(35, 37) * sp.cos(t) - sp.Rational(12, 37) * sp.sin(t))
mi = [sp.simplify(sp.integrate(t ** k * fsym, (t, 0, sp.oo))) for k in range(3)]
mi_ok = all(isinstance(x, sp.Rational) for x in mi) and [Fr(int(x.p), int(x.q)) for x in mi] == m
record("C1_sympy_integrate_agrees", mi_ok, [str(x) for x in mi])
ok_cert, det = upper_certificate(Fr(1), c0, s0)
record("C1_upper_certificate", ok_cert, det)
record("C1_773/3844_lt_1007/5000", V < B2014)
record("C1_1007/5000_lt_11/50", B2014 < T)
tail54 = (16 * D3_LO - 1) / 17
record("C1_Lemma5.4_tail_bound_eq_428/2125", tail54 == Fr(428, 2125), fs(tail54))
record("C1_773/3844_lt_428/2125", V < tail54)
rho = Fr(1213, 5000)
record("C1_rho_bar^2_gt_1/17", rho * rho > Fr(1, 17), fs(rho * rho))
tail55 = 2 * (1 - rho) * (1 - rho ** 3) / (1 + rho ** 2) ** 2 - 1
record("C1_Lemma5.5_tail_eq_v1_value", tail55 == Fr(232498770764161, 700733376734161), fs(tail55))
record("C1_773/3844_lt_Lemma5.5_tail", V < tail55)
record("C1_773/3844_lt_553/2000", V < D3_LO)
out["C1"] = {"omega": "1", "cos_phi": fs(c0), "sin_phi": fs(s0), "moments": [fs(x) for x in m],
             "SCV": fs(V), "SCV_decimal_truncated": dec(V), "T": fs(T), "0.2014": fs(B2014),
             "Lemma5.4_tail_omega<=1/4": fs(tail54), "Lemma5.4_tail_decimal": dec(tail54),
             "Lemma5.5_tail_omega>=4": fs(tail55), "Lemma5.5_tail_decimal": dec(tail55),
             "chain": "v_cos <= 773/3844 < 1007/5000 < 428/2125 <= inf_{omega<=1/4} SCV; 773/3844 < 11/50 = T; "
                      "773/3844 < Lemma5.5 tail <= inf_{omega>=4} SCV; 773/3844 < 553/2000 < Delta3"}


# ======================= C2 Delta3 > 553/2000 : exact polynomial arithmetic on Fraction lists (index = degree)
def trim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)])


def pscale(a, c):
    return trim([c * x for x in a])


def psub(a, b):
    return padd(a, pscale(b, Fr(-1)))


def pmul(a, b):
    if not a or not b:
        return []
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return trim(r)


def ppow(a, k):
    r = [Fr(1)]
    for _ in range(k):
        r = pmul(r, a)
    return r


def pder(a):
    return trim([i * a[i] for i in range(1, len(a))])


def pev(a, x):
    v = Fr(0)
    for coef in reversed(a):
        v = v * x + coef
    return v


def prem(a, b):
    a = trim(a)
    b = trim(b)
    while len(a) >= len(b):
        c = a[-1] / b[-1]
        sh = len(a) - len(b)
        a = psub(a, [Fr(0)] * sh + pscale(b, c))
    return a


def P_(*cs):
    return trim([Fr(c) for c in cs])


X1 = P_(0, 1)  # tau
fact = [1, 1, 2, 6, 24]
mk = [P_(fact[k + 2], -2 * fact[k + 1], fact[k]) for k in range(3)]  # (k+2)! - 2 tau (k+1)! + tau^2 k!
record("C2a_m0=tau^2-2tau+2", mk[0] == P_(2, -2, 1), [fs(x) for x in mk[0]])
record("C2a_m1=tau^2-4tau+6", mk[1] == P_(6, -4, 1), [fs(x) for x in mk[1]])
record("C2a_m2=2tau^2-12tau+24", mk[2] == P_(24, -12, 2), [fs(x) for x in mk[2]])
P = pmul(mk[0], mk[2])
Q = mk[1]
Q2 = pmul(Q, Q)
record("C2b_Q=(tau-2)^2+2", Q == padd(ppow(P_(-2, 1), 2), P_(2)))
sos = padd(pscale(ppow(P_(2, -4, 1), 2), Fr(3)), P_(0, 0, 8))
record("C2b_SOS_4(P-5/4Q^2)=3(tau^2-4tau+2)^2+8tau^2", pscale(psub(P, pscale(Q2, Fr(5, 4))), Fr(4)) == sos)
record("C2b_SOS_no_common_zero(tau=0_gives_12)", pev(sos, Fr(0)) == 12)
q = P_(-6, 18, -9, 1)
record("C2c_P'Q-2PQ'=8q", psub(pmul(pder(P), Q), pscale(pmul(P, pder(Q)), Fr(2))) == pscale(q, Fr(8)))
qv = {x: pev(q, x) for x in (Fr(0), Fr(1, 2), Fr(2), Fr(3), Fr(6), Fr(7))}
sign_ok = qv[Fr(0)] < 0 < qv[Fr(1, 2)] and qv[Fr(2)] > 0 > qv[Fr(3)] and qv[Fr(6)] < 0 < qv[Fr(7)]
record("C2c_q_sign_changes_isolate_(0,1/2),(2,3),(6,7)", sign_ok, {fs(k): fs(v) for k, v in qv.items()})
record("C2c_LC(P)=2_LC(Q^2)=1_deg4", len(P) == 5 and len(Q2) == 5 and P[-1] == 2 and Q2[-1] == 1)
s0v = pev(P, Fr(0)) / pev(Q, Fr(0)) ** 2 - 1
record("C2d_s(0)=1/3", s0v == Fr(1, 3), fs(s0v))
d_half = psub(pscale(P, Fr(2)), pscale(Q2, Fr(3)))
record("C2d_2P-3Q^2=tau^4-8tau^3+20tau^2-12", d_half == P_(-12, 0, 20, -8, 1))
record("C2d_=tau^2((tau-4)^2+4)-12", d_half == psub(pmul(P_(0, 0, 1), padd(ppow(P_(-4, 1), 2), P_(4))), P_(12)))
record("C2d_bound_for_tau>=6:_36*4-12>0", 36 * 4 - 12 > 0)
Pm = psub(P, Q2)  # numerator of s, s = Pm / Q^2
h = P_(-27, 135, -144, 32)
Nh = padd(padd(pscale(ppow(Pm, 3), Fr(32)), pscale(pmul(ppow(Pm, 2), Q2), Fr(-144))),
          padd(pscale(pmul(Pm, ppow(Q2, 2)), Fr(135)), pscale(ppow(Q2, 3), Fr(-27))))
rem_h = prem(Nh, q)
record("C2e_Q^6*h(s)_rem_q=0", rem_h == [], [fs(x) for x in rem_h])
E24 = psub(pmul(X1, ppow(P_(9, -1), 2)), P_(24))  # 24 E(x) = x (9 - x)^2 - 24
rem_E = prem(psub(pscale(Pm, Fr(24)), pmul(E24, Q2)), q)
record("C2e_s=E_mod_q", rem_E == [])
NhE = padd(padd(pscale(ppow(E24, 3), Fr(32)), pscale(ppow(E24, 2), Fr(-144 * 24))),
           padd(pscale(E24, Fr(135 * 24 * 24)), P_(-27 * 24 ** 3)))
record("C2e_h(E)=0_mod_q", prem(NhE, q) == [])
hp = pder(h)
record("C2f_h'=96y^2-288y+135", hp == P_(135, -288, 96))
record("C2f_h'=96(y-3/2)^2-81", hp == padd(pscale(ppow(P_(Fr(-3, 2), 1), 2), Fr(96)), P_(-81)))
hp_lb = 96 * Fr(7, 6) ** 2 - 81
record("C2f_lower_bound_96(7/6)^2-81=149/3>0", hp_lb == Fr(149, 3) and hp_lb > 0, fs(hp_lb))
record("C2f_3/2-1/3=7/6_(window_left_of_vertex)", Fr(3, 2) - Fr(1, 3) == Fr(7, 6))
record("C2f_h'(1/3)=149/3_is_the_min_on_window", pev(hp, Fr(1, 3)) == Fr(149, 3) and pev(hp, Fr(1, 4)) == 69)
record("C2f_h(1/4)=-7/4<0<h(1/3)=86/27", pev(h, Fr(1, 4)) == Fr(-7, 4) and pev(h, Fr(1, 3)) == Fr(86, 27))


def delta3_lower_certificate(y0):
    """Certifies Delta3 > y0 iff y0 in [1/4, 1/3] (window where h' >= 149/3) and h(y0) < 0."""
    if not (Fr(1, 4) <= y0 <= Fr(1, 3)):
        return False, {"reason": "y0 outside [1/4, 1/3]", "h(y0)": fs(pev(h, y0))}
    hv = pev(h, y0)
    return hv < 0, {"h(y0)": fs(hv), "h(y0)<0": hv < 0}


hv553 = pev(h, D3_LO)
record("C2g_h(553/2000)=-1293623/250000000", hv553 == Fr(-1293623, 250000000), fs(hv553))
ok2, det2 = delta3_lower_certificate(D3_LO)
record("C2g_Delta3_gt_553/2000", ok2, det2)
# exact rational bracket of the root by bisection (Fractions only)
lo_b, hi_b = Fr(1, 4), Fr(1, 3)
for _ in range(60):
    mid = (lo_b + hi_b) / 2
    if pev(h, mid) < 0:
        lo_b = mid
    else:
        hi_b = mid
record("C2g_bisection_bracket_consistent", lo_b > D3_LO and pev(h, lo_b) < 0 < pev(h, hi_b))
out["C2"] = {"h": "32y^3 - 144y^2 + 135y - 27", "h(553/2000)": fs(hv553), "h(553/2000)_decimal": dec(hv553, 12),
             "h'_min_on_[1/4,1/3]": "149/3", "h(1/4)": "-7/4", "h(1/3)": "86/27",
             "Delta3_bracket_exact_bisection_60_steps": [fs(lo_b), fs(hi_b)],
             "Delta3_bracket_decimal": [dec(lo_b, 18), dec(hi_b, 18)],
             "q_values": {fs(k): fs(v) for k, v in qv.items()},
             "chain": "Delta3 = min s = s(x1) in (1/4, 1/3), h(Delta3) = 0, h' >= 149/3 on [1/4,1/3], "
                      "h(553/2000) < 0  =>  Delta3 > 553/2000"}

# sympy exact cross-checks of the polynomial identities
y_, x_ = sp.symbols("y x")
Ps = sp.expand((x_ ** 2 - 2 * x_ + 2) * (2 * x_ ** 2 - 12 * x_ + 24))
Qs = x_ ** 2 - 4 * x_ + 6
qs = x_ ** 3 - 9 * x_ ** 2 + 18 * x_ - 6
hs = 32 * y_ ** 3 - 144 * y_ ** 2 + 135 * y_ - 27
Nhs = sp.expand(sp.numer(sp.together(hs.subs(y_, Ps / Qs ** 2 - 1))))
record("X_sympy_rem(numer(h(s)),q)=0", sp.rem(Nhs, qs, x_) == 0)
record("X_sympy_h(553/2000)", hs.subs(y_, sp.Rational(553, 2000)) == sp.Rational(-1293623, 250000000))
mres = sp.Poly(sp.resultant(qs, 24 * y_ - x_ * (9 - x_) ** 2 + 24, x_), y_).monic()
record("X_sympy_resultant_monic_eq_h/32", sp.expand(mres.as_expr() - hs / 32) == 0, str(mres.as_expr()))

# ======================= wrong controls (each must FAIL)
ctl = {}
w1, d1 = upper_certificate(Fr(1), s0, c0)
ctl["W1_swapped_cos_sin_(12/37,35/37)"] = {"certified": w1, "detail": d1, "failed_as_expected": not w1}
w2, d2_ = delta3_lower_certificate(Fr(2766, 10000))
ctl["W2_h(2766/10000)_wrong_sign"] = {"certified": w2, "detail": d2_, "failed_as_expected": not w2,
                                      "note": "h(2766/10000) > 0, so 'Delta3 > 2766/10000' is not certified "
                                              "(the same sign certifies Delta3 < 2766/10000)"}
w4, d4 = delta3_lower_certificate(Fr(1, 5))
ctl["W4_point_1/5_outside_window"] = {"certified": w4, "detail": d4, "failed_as_expected": not w4}
w5, d5 = upper_certificate(Fr(1), Fr(35, 37), Fr(13, 37))
ctl["W5_pythagoras_violated_(35/37,13/37)"] = {"certified": w5, "detail": d5, "failed_as_expected": not w5}
w6, d6 = upper_certificate(Fr(1), c0, s0, phase_sign=+1)
ctl["W6_phase_sign_e^{+i phi}"] = {"certified": w6, "detail": d6, "failed_as_expected": not w6}
for k_, v_ in ctl.items():
    record("CTL_" + k_ + "_must_fail", v_["failed_as_expected"], v_["detail"])
info552, d552 = delta3_lower_certificate(Fr(552, 2000))
out["info_h(552/2000)_not_a_failing_control"] = {"certified_weaker_bound_Delta3>552/2000": info552, "detail": d552}
out["controls"] = ctl

out["checks"] = checks
out["all_pass"] = all(v["pass"] for v in checks.values())
out["n_checks"] = len(checks)
out["elapsed_s"] = str(Fr(time.monotonic_ns() - T0, 10 ** 9))
with lane_guard.xopen(os.path.join(RUN, "exact_certs.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "n_checks": len(checks),
                  "failed": [k for k, v in checks.items() if not v["pass"]], "SCV_C1": fs(V),
                  "h(553/2000)": fs(hv553), "controls_all_failed_as_expected": all(v["failed_as_expected"]
                                                                                  for v in ctl.values())}))
sys.exit(0 if out["all_pass"] else 1)

"""Control (a) for reductions L1/L3.  Labels: CERTIFIED = exact sympy arithmetic; EXPLORATORY = mpmath floats.

(a1) Erlang-3 via an explicit order-3 ME representation (alpha, A) (HSTZ Def. 1): E(t) = e^{-t}(I + N t + N^2 t^2/2)
     is verified to BE e^{At} (E(0) = I, E' = A E); density f = -alpha A e^{At} 1; alpha 1 = 1; moments; SCV = 1/3.
(a2) Real-pole kernel formula 1 + s(tau) = (tau^2-2tau+2)(2tau^2-12tau+24)/(tau^2-4tau+6)^2 at tau = 0 gives 1/3.
(a3) Hermite-Genocchi: s^2 * (simplex integral of e^{-s<u,lambda>}) equals the (confluent) divided difference of
     x -> e^{-s x} at the nodes, for nodes (1,2,3), (1,1,2), (1,2,2), (1,1,1); the quotient by s^2 tends to 1/2 at s=0.
     Sample SCV(F_tau) values (EXPLORATORY numerics) compared with the Laguerre value of Delta3.
(a4) L1 converse realization for f = 2 e^{-t}(1 - cos t) (omega = 1, phi = 0): companion matrix C, S with S e1 = 1,
     A = S C^T S^{-1}, alpha = x0^T S^{-1}; exact checks alpha 1 = 1, charpoly(A) = (s+1)(s^2+2s+2),
     alpha A^k 1 = G^{(k)}(0) (k = 0,1,2), -alpha A^{k+1} 1 = f^{(k)}(0) consistency; mpmath expm spot check (EXPLORATORY).
"""
import os
import sys
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
T0 = time.time()
out = {"script": "ctl_a_erlang3_v1.py", "label_default": "CERTIFIED (exact sympy)"}
checks = {}


def record(name, ok, detail=None):
    checks[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        print("FAIL", name, detail)


t = sp.Symbol("t", nonnegative=True)

# ---------------- (a1) Erlang-3 through (alpha, A)
alpha = sp.Matrix([[1, 0, 0]])
A = sp.Matrix([[-1, 1, 0], [0, -1, 1], [0, 0, -1]])
one = sp.ones(3, 1)
Nn = A + sp.eye(3)
record("a1_N_nilpotent", Nn ** 3 == sp.zeros(3, 3))
Et = sp.exp(-t) * (sp.eye(3) + Nn * t + Nn ** 2 * t ** 2 / 2)
record("a1_E0_is_I", sp.simplify(Et.subs(t, 0) - sp.eye(3)) == sp.zeros(3, 3))
record("a1_Eprime_eq_AE", sp.simplify(Et.diff(t) - A * Et) == sp.zeros(3, 3))
G = sp.simplify((alpha * Et * one)[0])
f = sp.simplify((-alpha * A * Et * one)[0])
record("a1_alpha1_eq_1", (alpha * one)[0] == 1)
record("a1_G0_eq_1", sp.simplify(G.subs(t, 0) - 1) == 0)
record("a1_G_to_0", sp.limit(G, t, sp.oo) == 0)
record("a1_f_eq_t2e-t/2", sp.simplify(f - t ** 2 * sp.exp(-t) / 2) == 0, str(f))
record("a1_f_eq_minus_Gprime", sp.simplify(f + G.diff(t)) == 0)
m = [sp.integrate(t ** k * f, (t, 0, sp.oo)) for k in range(3)]
scv = sp.nsimplify(m[0] * m[2] / m[1] ** 2 - 1)
record("a1_moments", m == [1, 3, 12], [str(x) for x in m])
record("a1_SCV_eq_1/3", scv == sp.Rational(1, 3), str(scv))
out["a1"] = {"alpha": str(alpha.tolist()), "A": str(A.tolist()), "G": str(G), "f": str(f),
             "moments": [str(x) for x in m], "SCV": str(scv)}

# ---------------- (a2) real-pole kernel formula at tau = 0
tau = sp.Symbol("tau", real=True)
P = (tau ** 2 - 2 * tau + 2) * (2 * tau ** 2 - 12 * tau + 24)
Q = tau ** 2 - 4 * tau + 6
s0 = sp.nsimplify(P.subs(tau, 0) / Q.subs(tau, 0) ** 2 - 1)
record("a2_s(0)_eq_1/3", s0 == sp.Rational(1, 3), str(s0))
out["a2"] = {"s(0)": str(s0)}

# ---------------- (a3) Hermite-Genocchi kernels
s = sp.Symbol("s", positive=True)
u2, u3 = sp.symbols("u2 u3", nonnegative=True)


def hg(l1, l2, l3):
    integrand = sp.exp(-s * ((1 - u2 - u3) * l1 + u2 * l2 + u3 * l3))
    inner = sp.integrate(integrand, (u3, 0, 1 - u2))
    return sp.simplify(s ** 2 * sp.integrate(sp.expand(inner), (u2, 0, 1)))


def phi(x):
    return sp.exp(-s * x)


def dphi(x):
    return -s * sp.exp(-s * x)


dd = {
    (1, 2, 3): phi(1) / ((1 - 2) * (1 - 3)) + phi(2) / ((2 - 1) * (2 - 3)) + phi(3) / ((3 - 1) * (3 - 2)),
    (1, 1, 2): ((phi(2) - phi(1)) / (2 - 1) - dphi(1)) / (2 - 1),
    (1, 2, 2): (dphi(2) - (phi(2) - phi(1)) / (2 - 1)) / (2 - 1),
    (1, 1, 1): s ** 2 * sp.exp(-s) / 2,
}
a3 = {}
for nodes, ddexpr in dd.items():
    h = hg(*nodes)
    diff0 = sp.simplify(sp.expand(h - ddexpr))
    if diff0 != 0:  # second exact attempt: clear exponentials and expand
        diff0 = sp.simplify(sp.expand(sp.powsimp(sp.expand((h - ddexpr) * sp.exp(4 * s)))))
    lim = sp.limit(ddexpr / s ** 2, s, 0)
    # numeric spot check of the identity at s = 0.37, 2.9 (50 digits) in addition to simplify
    spot = [sp.N((h - ddexpr).subs(s, sp.Rational(37, 100)), 50), sp.N((h - ddexpr).subs(s, sp.Rational(29, 10)), 50)]
    ok = (diff0 == 0) and all(abs(v) < sp.Float("1e-45") for v in spot) and lim == sp.Rational(1, 2)
    record("a3_HG_eq_DD_%s" % (nodes,), ok, {"simplified_difference": str(diff0), "limit_DD_over_s2": str(lim),
                                            "spot_differences": [str(v) for v in spot]})
    a3[str(nodes)] = {"HG": str(h), "DD": str(ddexpr), "limit_DD/s^2_at_0": str(lim)}
out["a3_HG"] = a3

# Sample SCV(F_tau) for nodes (1,2,3) (exact moment expressions, evaluated at 40 digits; EXPLORATORY comparison)
# F_tau(t) = sum_i c_i e^{-l_i (t - tau)}, c = (1/2, -1, 1/2); m_k = sum_i c_i e^{l_i tau} k!/l_i^{k+1}
mp.mp.dps = 40
x = sp.Symbol("x")
cub = sp.Poly(x ** 3 - 9 * x ** 2 + 18 * x - 6, x)
x1 = min(sp.Poly(cub).nroots(n=40))
delta3_lag = (x1 * (9 - x1) ** 2 - 24) / 24
samples = []
for tv in ["0", "0.2", "0.41577", "0.5", "1", "2", "5"]:
    tq = sp.Rational(tv)
    lam = [1, 2, 3]
    c = [sp.Rational(1, 2), -1, sp.Rational(1, 2)]
    mk = [sum(c[i] * sp.exp(lam[i] * tq) * sp.factorial(k) / sp.Integer(lam[i]) ** (k + 1) for i in range(3))
          for k in range(3)]
    sv = sp.N(mk[0] * mk[2] / mk[1] ** 2 - 1, 30)
    samples.append({"tau": tv, "SCV": str(sv), "ge_Delta3": bool(sv >= delta3_lag)})
record("a3_sample_SCV_Ftau_ge_Delta3_EXPLORATORY", all(d["ge_Delta3"] for d in samples))
out["a3_sample_SCV_F_tau_nodes123_EXPLORATORY"] = {"Delta3_laguerre_numeric": str(sp.N(delta3_lag, 30)),
                                                   "samples": samples}

# ---------------- (a4) L1 converse realization
Gt = 2 * sp.exp(-t) - sp.exp(-t) * (sp.cos(t) - sp.sin(t))  # = int_t^inf 2 e^{-s}(1 - cos s) ds
fn = 2 * sp.exp(-t) * (1 - sp.cos(t))
record("a4_G_is_tail_integral", sp.simplify(Gt.diff(t) + fn) == 0 and sp.limit(Gt, t, sp.oo) == 0)
record("a4_G0_eq_1", sp.simplify(Gt.subs(t, 0)) == 1)
record("a4_int_f_eq_1", sp.simplify(sp.integrate(fn, (t, 0, sp.oo)) - 1) == 0)
sv_ = sp.Symbol("sv")
chi = sp.expand((sv_ + 1) * (sv_ ** 2 + 2 * sv_ + 2))
coef = sp.Poly(chi, sv_).all_coeffs()  # [1, 3, 4, 2]
C = sp.Matrix([[0, 1, 0], [0, 0, 1], [-coef[3], -coef[2], -coef[1]]])
record("a4_chi_annihilates_G", sp.simplify(Gt.diff(t, 3) + coef[1] * Gt.diff(t, 2) + coef[2] * Gt.diff(t) + coef[3] * Gt) == 0)
x0 = sp.Matrix([sp.simplify(Gt.diff(t, k).subs(t, 0)) for k in range(3)])
S = sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 0, 1]])
record("a4_S_e1_eq_1", S * sp.Matrix([1, 0, 0]) == one and S.det() == 1)
Ar = S * C.T * S.inv()
alr = x0.T * S.inv()
record("a4_alpha1_eq_1", sp.simplify((alr * one)[0]) == 1)
cp = sp.expand(Ar.charpoly(sv_).as_expr())
record("a4_charpoly", sp.expand(cp - chi) == 0, str(cp))
dm = [sp.simplify((alr * Ar ** k * one)[0] - x0[k]) for k in range(3)]
record("a4_alpha_A^k_1_eq_G^(k)(0)", all(v == 0 for v in dm), [str(v) for v in dm])
fd = [sp.simplify((-alr * Ar ** (k + 1) * one)[0] - fn.diff(t, k).subs(t, 0)) for k in range(3)]
record("a4_minus_alpha_A^(k+1)_1_eq_f^(k)(0)", all(v == 0 for v in fd), [str(v) for v in fd])
# EXPLORATORY numeric spot check with mpmath expm
mp.mp.dps = 30
An = mp.matrix([[mp.mpf(sp.Rational(Ar[i, j]).p) / sp.Rational(Ar[i, j]).q for j in range(3)] for i in range(3)])
aln = mp.matrix([[mp.mpf(sp.Rational(alr[0, j]).p) / sp.Rational(alr[0, j]).q for j in range(3)]])
spot = []
for tv in [mp.mpf("0.7"), mp.mpf("2.3"), mp.mpf("6.1")]:
    val = (aln * mp.expm(An * tv) * mp.matrix([1, 1, 1]))[0]
    exact = 2 * mp.exp(-tv) - mp.exp(-tv) * (mp.cos(tv) - mp.sin(tv))
    spot.append({"t": str(tv), "alpha_expAt_1": mp.nstr(val, 25), "G": mp.nstr(exact, 25),
                 "absdiff": mp.nstr(abs(val - exact), 5)})
record("a4_expm_spot_EXPLORATORY", all(mp.mpf(d["absdiff"]) < mp.mpf("1e-20") for d in spot))
out["a4"] = {"C": str(C.tolist()), "S": str(S.tolist()), "A": str(Ar.tolist()), "alpha": str(alr.tolist()),
             "x0": str(x0.T.tolist()), "charpoly": str(cp), "expm_spot_EXPLORATORY": spot}

out["checks"] = checks
out["all_pass"] = all(v["pass"] for v in checks.values())
out["elapsed_s"] = round(time.time() - T0, 2)
with lane_guard.xopen(os.path.join(RUN, "ctl_a.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "n_checks": len(checks),
                  "failed": [k for k, v in checks.items() if not v["pass"]], "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if out["all_pass"] else 1)

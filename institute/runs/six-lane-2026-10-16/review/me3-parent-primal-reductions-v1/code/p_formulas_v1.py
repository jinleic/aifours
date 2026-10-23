"""ME3 parent desk (ME3ParentPrimal): exact and diagnostic checks of the primal-chart formulas and of p_core_v1.

Usage: p_formulas_v1.py RUN_DIR
Parts (results in RUN_DIR/RESULT.json, exclusive create):
  F1 (exact, sympy): d_x log P_k = Lam_{k,x} and d_x L_k as used by p_core_v1, k = 0, 1, 2, x in (r, w, phi);
     (r - i)/(1 + r^2) = -i/(1 - i r).
  F2 (exact, sympy): d_r log(2 A0 A2/A1^2) = D/(A0 A1 A2) for arbitrary functions A_k(r).
  F3 (exact, sympy): h_tau(t) = 1 - Re[(1 - i r) e^{(r - i) phi} e^{(-delta + i w) t}], delta = r w, tau = phi/w;
     int_0^inf t^k e^{-z t} dt = k!/z^{k+1} (z > 0, extended to Re z > 0 by analytic continuation).
  F4 (diagnostic, mpmath 40 digits): direct quadrature of m_k = int_0^inf t^k e^{-t} h_tau(t) dt vs k! a_k.
  F5 (code check): p_core_v1 point-ball values of a_k, a_k', D, grad G, grad D, d_x a_k' vs sympy derivatives of the
     definition-level expressions evaluated at 60 digits (agreement required to 1e-30).
  F6 (diagnostic): enclosure soundness smoke test of p_core_v1 naive and mean-value forms on random boxes against
     mpmath point values (G closed form; D by mpmath numerical r-derivative of a_k, not by the closed form).
"""
import sys
import os
import json
import random
import time
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402
from flint import arb  # noqa: E402
import p_core_v1 as C  # noqa: E402

RUN = sys.argv[1]
T = Fraction(11, 50)
res = {"script": "p_formulas_v1.py", "started_epoch": time.time()}
ok_all = True


def rec(key, value, ok):
    global ok_all
    res[key] = {"value": value, "ok": bool(ok)}
    if not ok:
        ok_all = False


# ---------------- F1 ----------------------------------------------------------------------------------------------
r, w, p = sp.symbols("r w p", real=True)
Isym = sp.I
zeta = 1 / (1 + r * w - Isym * w)
Pk = []
f1 = []
for k in range(3):
    kk = k + 1
    P = (1 - Isym * r) * sp.exp((r - Isym) * p) * zeta ** kk
    Pk.append(P)
    L = p + (r - Isym) / (1 + r ** 2) - kk * w * zeta
    lam = {r: L, w: -kk * (r - Isym) * zeta, p: (r - Isym)}
    dL = {r: (1 - Isym * r) ** (-2) + kk * w ** 2 * zeta ** 2, w: -kk * zeta ** 2, p: sp.Integer(1)}
    for x in (r, w, p):
        e1 = sp.simplify(sp.diff(P, x) / P - lam[x])
        e2 = sp.simplify(sp.diff(L, x) - dL[x])
        f1.append({"k": k, "x": str(x), "dlogP_residual": str(e1), "dL_residual": str(e2)})
e3 = sp.simplify((r - Isym) / (1 + r ** 2) + Isym / (1 - Isym * r))
rec("F1_derivative_identities", {"items": f1, "K_identity_residual": str(e3)},
    all(it["dlogP_residual"] == "0" and it["dL_residual"] == "0" for it in f1) and str(e3) == "0")

# ---------------- F2 ----------------------------------------------------------------------------------------------
A = [sp.Function(f"A{k}")(r) for k in range(3)]
lhs = sp.diff(sp.log(2 * A[0] * A[2] / A[1] ** 2), r)
Dabs = sp.diff(A[0], r) * A[1] * A[2] + A[0] * A[1] * sp.diff(A[2], r) - 2 * A[0] * sp.diff(A[1], r) * A[2]
e4 = sp.simplify(lhs - Dabs / (A[0] * A[1] * A[2]))
rec("F2_dlog_identity", str(e4), str(e4) == "0")

# ---------------- F3 ----------------------------------------------------------------------------------------------
# Stepwise exact identities of the derivation (gating), plus one full simplify (informational only):
#  (i)  Re[(1 - i r)(cos x + i sin x)] = cos x + r sin x  (polynomial identity in cos x, sin x);
#  (ii) (-delta + i w)(t - tau) = (-delta + i w) t + (r - i) phi  with delta = r w, tau = phi/w;
#  so e^{-delta s}(cos ws + r sin ws) = Re[(1 - i r) e^{(-delta + i w) s}] = Re[c e^{(-delta + i w) t}], s = t - tau.
t = sp.symbols("t", real=True)
wp = sp.symbols("wp", positive=True)
delta = r * wp
tau = p / wp
cs, sn = sp.symbols("cs sn", real=True)
e5a = sp.expand(sp.re(sp.expand((1 - Isym * r) * (cs + Isym * sn))) - (cs + r * sn))
e5b = sp.expand((-delta + Isym * wp) * (t - tau) - ((-delta + Isym * wp) * t + (r - Isym) * p))
h_def = 1 - sp.exp(-delta * (t - tau)) * (sp.cos(wp * (t - tau)) + r * sp.sin(wp * (t - tau)))
zc = (1 - Isym * r) * sp.exp((r - Isym) * p) * sp.exp((-delta + Isym * wp) * t)
h_cx = 1 - sp.re(sp.expand_complex(zc))
e5 = sp.simplify(sp.expand_trig(sp.expand(h_cx - h_def)))
zp = sp.symbols("zp", positive=True)
lap = [sp.simplify(sp.integrate(t ** k * sp.exp(-zp * t), (t, 0, sp.oo)) - sp.factorial(k) / zp ** (k + 1))
       for k in range(3)]
rec("F3_h_representation_and_laplace", {"step_i_residual": str(e5a), "step_ii_residual": str(e5b),
                                         "full_simplify_residual_informational": str(e5),
                                         "laplace_residuals": [str(x) for x in lap]},
    str(e5a) == "0" and str(e5b) == "0" and all(str(x) == "0" for x in lap))

# ---------------- F4 (diagnostic) ---------------------------------------------------------------------------------
mp.mp.dps = 40
f4 = []
pts4 = [(Fraction(3, 10), Fraction(1), Fraction(2)), (Fraction(1, 10), Fraction(259, 250), Fraction(337, 1000)),
        (Fraction(2), Fraction(5), Fraction(33, 10)), (Fraction(0), Fraction(1, 5), Fraction(6)),
        (Fraction(1, 4), Fraction(12), Fraction(1, 7))]
for (rv, wv, pv) in pts4:
    R, W, PH = mp.mpf(rv.numerator) / rv.denominator, mp.mpf(wv.numerator) / wv.denominator, \
        mp.mpf(pv.numerator) / pv.denominator
    dl, ta = R * W, PH / W

    def h(tt):
        s = tt - ta
        return 1 - mp.exp(-dl * s) * (mp.cos(W * s) + R * mp.sin(W * s))

    c = (1 - 1j * R) * mp.exp((R - 1j) * PH)
    z = 1 / (1 + R * W - 1j * W)
    period = 2 * mp.pi / W
    nodes = [mp.mpf(0)] + [period * j / 4 for j in range(1, int(4 * 120 / period) + 2)]
    nodes = [x for x in nodes if x < 120] + [mp.mpf(120), mp.inf]
    row = []
    for k in range(3):
        quad = mp.quad(lambda tt: tt ** k * mp.exp(-tt) * h(tt), nodes)
        closed = mp.factorial(k) * (1 - mp.re(c * z ** (k + 1)))
        row.append(mp.nstr(abs(quad - closed), 5))
    f4.append({"point": [str(rv), str(wv), str(pv)], "abs_diff_k012": row})
rec("F4_quadrature_diagnostic", f4, all(mp.mpf(x) < mp.mpf("1e-25") for it in f4 for x in it["abs_diff_k012"]))

# ---------------- F5 (code check) ---------------------------------------------------------------------------------
ev = C.Evaluator(T, 128)
a_ex = [1 - sp.re(P) for P in Pk]
ap_ex = [-sp.re(sp.diff(P, r)) for P in Pk]
G_ex = 2 * a_ex[0] * a_ex[2] - sp.Rational(61, 50) * a_ex[1] ** 2
D_ex = ap_ex[0] * a_ex[1] * a_ex[2] + a_ex[0] * a_ex[1] * ap_ex[2] - 2 * a_ex[0] * ap_ex[1] * a_ex[2]
dG_ex = [sp.diff(G_ex, x) for x in (r, w, p)]
dD_ex = [sp.diff(D_ex, x) for x in (r, w, p)]
dd_ex = [[-sp.re(sp.diff(P, r, x)) for x in (r, w, p)] for P in Pk]
rng = random.Random(20261018)
pts5 = [(Fraction(0), Fraction(1, 5), Fraction(0)), (Fraction(3), Fraction(40), Fraction(31416, 5000)),
        (Fraction(0), Fraction(259, 250), Fraction(337, 1000))]
for _ in range(5):
    pts5.append((Fraction(rng.randint(0, 3000), 1000), Fraction(rng.randint(200, 40000), 1000),
                 Fraction(rng.randint(0, 6283), 1000)))
tol = arb("1e-30")
f5 = []
f5ok = True


def agree(ball, ex, subs):
    v = sp.N(ex.subs(subs), 60)
    diff = ball - arb(str(sp.re(v)))
    good = abs(diff) < tol * (1 + abs(ball))
    return bool(good), float(abs(diff).mid())


for (rv, wv, pv) in pts5:
    subs = {r: sp.Rational(rv.numerator, rv.denominator), w: sp.Rational(wv.numerator, wv.denominator),
            p: sp.Rational(pv.numerator, pv.denominator)}
    balls = ev.point((rv, wv, pv))
    a, d, D, P, z = ev.D_val(*balls)
    G = ev.G_of(*a)
    dG, da = ev.grad_G(balls, P, z, a)
    dD, dd, da2 = ev.grad_D(balls, a, d, P, z)
    worst = 0.0
    good = True
    for ball, ex in ([(a[k], a_ex[k]) for k in range(3)] + [(d[k], ap_ex[k]) for k in range(3)]
                     + [(G, G_ex), (D, D_ex)] + [(dG[j], dG_ex[j]) for j in range(3)]
                     + [(dD[j], dD_ex[j]) for j in range(3)]
                     + [(dd[k][j], dd_ex[k][j]) for k in range(3) for j in range(3)]):
        g, e = agree(ball, ex, subs)
        good = good and g
        worst = max(worst, e)
    f5.append({"point": [str(rv), str(wv), str(pv)], "ok": good, "worst_abs_diff": worst})
    f5ok = f5ok and good
rec("F5_code_vs_sympy", f5, f5ok)

# ---------------- F6 (diagnostic) ---------------------------------------------------------------------------------
mp.mp.dps = 50


def mp_a(R, W, PH):
    c = (1 - 1j * R) * mp.exp((R - 1j) * PH)
    z = 1 / (1 + R * W - 1j * W)
    return [1 - mp.re(c * z ** (k + 1)) for k in range(3)]


def mp_GD(R, W, PH):
    a = mp_a(R, W, PH)
    G = 2 * a[0] * a[2] - mp.mpf(61) / 50 * a[1] ** 2
    ap = [mp.diff(lambda rr, k=k: mp_a(rr, W, PH)[k], R) for k in range(3)]
    D = ap[0] * a[1] * a[2] + a[0] * a[1] * ap[2] - 2 * a[0] * ap[1] * a[2]
    return G, D


def q2mp(x):
    return mp.mpf(x.numerator) / x.denominator


f6 = {"boxes": 0, "points": 0, "violations": [], "naive_G_wider_than_mvf": 0}
for bi in range(40):
    size = [Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000), Fraction(1, 10000)][bi % 4]
    rl = Fraction(rng.randint(0, 2900), 1000)
    wl = Fraction(rng.randint(200, 39000), 1000)
    pl = Fraction(rng.randint(0, 6100), 1000)
    box = ((rl, rl + size), (wl, wl + 3 * size), (pl, pl + 2 * size))
    balls, P, z, a, Gn = ev.G_naive(box)
    Gm, a1m = ev.G_mvf(box, balls, P, z, a)
    ballsD, aD, dD_, Dn, PD, zD = ev.D_naive(box)
    Dm, amv = ev.D_mvf(box, ballsD, aD, dD_, PD, zD)
    f6["boxes"] += 1
    if Gn.rad() > Gm.rad():
        f6["naive_G_wider_than_mvf"] += 1
    for _ in range(12):
        pt = tuple(lo + (hi - lo) * Fraction(rng.randint(0, 10 ** 6), 10 ** 6) for lo, hi in box)
        Gv, Dv = mp_GD(*(q2mp(x) for x in pt))
        av = mp_a(*(q2mp(x) for x in pt))
        f6["points"] += 1
        for name, ball, val in (("Gnaive", Gn, Gv), ("Gmvf", Gm, Gv), ("Dnaive", Dn, Dv), ("Dmvf", Dm, Dv),
                                ("a1naive", a[1], av[1]), ("a1mvf", a1m, av[1])):
            vb = arb(mp.nstr(val, 45))
            if not (ball.contains(vb) or ball.overlaps(vb)):
                f6["violations"].append({"box": [[str(x) for x in iv] for iv in box], "pt": [str(x) for x in pt],
                                         "what": name})
rec("F6_enclosure_smoke_diagnostic", f6, not f6["violations"])

res["all_ok"] = ok_all
res["elapsed_seconds"] = round(time.time() - res["started_epoch"], 2)
with open(os.path.join(RUN, "RESULT.json"), "x") as fh:
    json.dump(res, fh, indent=1)
print("RESULT", "PASS" if ok_all else "FAIL", json.dumps({k: v["ok"] for k, v in res.items() if isinstance(v, dict)}))
sys.exit(0 if ok_all else 1)

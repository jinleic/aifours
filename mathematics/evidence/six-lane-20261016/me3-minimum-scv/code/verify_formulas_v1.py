"""Formula checks for the ME3 lane (exact sympy identities + 40-digit mpmath quadrature smoke).

1. EXACT (sympy): dP_k/dr = P_k [phi + (r - i)/(1 + r^2) - (k+1) w zeta] for P_k = (1 - i r) e^{(r - i) phi} zeta^{k+1},
   zeta = 1/(1 + r w - i w), k = 0, 1, 2.
2. EXACT (sympy): h(t) = 1 - Re[(1 - i r) e^{(-r + i) w (t - tau)}] equals 1 - e^{-delta s}(cos w s + r sin w s),
   s = t - tau, delta = r w; h(tau) = h'(tau) = 0; h'(t) = (1 + r^2) w e^{-delta s} sin(w s).
3. SMOKE (mpmath quad, 40 digits): a_k = (1/k!) int t^k e^{-t} h(t) dt equals 1 - Re[c zeta^{k+1}],
   c = (1 - i r) e^{(r - i) phi}, at seeded random feasible (r, w, phi).
4. SMOKE: the integral representation Psi_r(w s) = (delta^2 + w^2) s^2 int_0^1 x e^{-delta x s} sinc(w x s) dx
   at random points (used only as an explanatory identity).
5. SMOKE (dual): for (delta, w) configurations and T = 11/50, min over a fine phi-grid of G = 2 a0 a2 - (1+T) a1^2
   has the same sign as the dual test min over a fine mu-grid of [-(log|W| + r arg W)] (spiral branch), where
   W = Q_T(mu (1 + delta - i w)) / Q_T(mu), Q_T(s) = (2 - 2 s + s^2/(1+T)) / s^3.
argv[1] = run directory; writes verify.json (exclusive create).
"""
import sys
import json
import random
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
out = {}
r, w, phi, t, tau = sp.symbols("r w phi t tau", real=True)
I = sp.I
zeta = 1 / (1 + r * w - I * w)
c = (1 - I * r) * sp.exp((r - I) * phi)
ok1 = []
for k in range(3):
    P = c * zeta ** (k + 1)
    lhs = sp.diff(P, r)
    rhs = P * (phi + (r - I) / (1 + r ** 2) - (k + 1) * w * zeta)
    ok1.append(bool(sp.simplify(sp.expand(sp.simplify((lhs - rhs) / P))) == 0))
out["1_dPdr_identity_k012"] = ok1

s = t - tau
h_complex = 1 - (1 - I * r) * sp.exp((-r + I) * w * s)
h_real_claim = 1 - sp.exp(-r * w * s) * (sp.cos(w * s) + r * sp.sin(w * s))
re_part = sp.re(sp.expand_complex(h_complex))
ok2a = bool(sp.simplify(re_part - h_real_claim) == 0)
dh = sp.diff(h_real_claim, t)
ok2b = bool(sp.simplify(dh - (1 + r ** 2) * w * sp.exp(-r * w * s) * sp.sin(w * s)) == 0)
ok2c = bool(sp.simplify(h_real_claim.subs(t, tau)) == 0 and sp.simplify(dh.subs(t, tau)) == 0)
out["2_h_real_form"] = ok2a
out["2_h_derivative"] = ok2b
out["2_double_zero_at_tau"] = ok2c

mp.mp.dps = 40
rng = random.Random(20261018)


def theta1(rv):
    if rv == 0:
        return 2 * mp.pi
    g = lambda u: mp.cos(u) - rv * mp.sin(u) - mp.exp(-rv * u)  # noqa: E731
    return mp.findroot(g, (mp.pi + mp.mpf("1e-30"), 2 * mp.pi), solver="bisect")


res3 = []
for _ in range(12):
    rv = mp.mpf(rng.choice([0, rng.uniform(0, 0.5), rng.uniform(0.5, 3)]))
    wv = mp.mpf(10) ** rng.uniform(-1, 0.7)
    th = theta1(rv)
    pv = th * mp.mpf(rng.uniform(0, 1))
    tv = pv / wv
    cv = (1 - 1j * rv) * mp.exp((rv - 1j) * pv)
    zv = 1 / (1 + rv * wv - 1j * wv)

    def h(tt):
        ss = tt - tv
        return 1 - mp.exp(-rv * wv * ss) * (mp.cos(wv * ss) + rv * mp.sin(wv * ss))
    errs = []
    for k in range(3):
        quad = mp.quad(lambda tt: tt ** k * mp.exp(-tt) * h(tt), [0, tv, tv + 20, mp.inf]) / mp.factorial(k)
        closed = 1 - mp.re(cv * zv ** (k + 1))
        errs.append(float(abs(quad - closed) / max(abs(closed), mp.mpf(1e-30))))
    hmin = min(h(mp.mpf(x) * tv / 50) for x in range(0, 51)) if tv > 0 else h(0)
    res3.append({"r": float(rv), "w": float(wv), "phi": float(pv), "rel_err_k012": errs, "h_min_on_[0,tau]_grid": float(hmin)})
out["3_moment_closed_form_vs_quad"] = res3
out["3_max_rel_err"] = max(max(x["rel_err_k012"]) for x in res3)

res4 = []
for _ in range(8):
    rv = mp.mpf(rng.uniform(0, 3))
    wv = mp.mpf(10) ** rng.uniform(-1, 0.7)
    dv = rv * wv
    sv = mp.mpf(rng.uniform(-3, 6))
    lhs = 1 - mp.exp(-dv * sv) * (mp.cos(wv * sv) + rv * mp.sin(wv * sv))
    rhs = (dv ** 2 + wv ** 2) * sv ** 2 * mp.quad(lambda x: x * mp.exp(-dv * x * sv) * mp.sinc(wv * x * sv), [0, 1])
    res4.append(float(abs(lhs - rhs)))
out["4_sinc_representation_abs_err"] = res4

T = mp.mpf(11) / 50
kap = 1 / (1 + T)


def QT(z):
    return (2 - 2 * z + kap * z * z) / z ** 3


res5 = []
for (dv, wv) in [(0.0, 1.0359), (0.02, 1.0), (0.05, 1.0), (0.2, 0.9), (0.5, 0.6), (1.0, 2.0), (0.0, 0.3), (2.0, 0.2), (0.3, 3.0)]:
    dv, wv = mp.mpf(dv), mp.mpf(wv)
    rv = dv / wv
    th = theta1(rv)
    Gmin = mp.inf
    for j in range(2001):
        pv = th * j / 2000
        cv = (1 - 1j * rv) * mp.exp((rv - 1j) * pv)
        zv = 1 / (1 + dv - 1j * wv)
        a0, a1, a2 = [1 - mp.re(cv * zv ** (k + 1)) for k in range(3)]
        Gmin = min(Gmin, 2 * a0 * a2 - (1 + T) * a1 ** 2)
    defect = -mp.inf
    for j in range(4001):
        mu = mp.mpf(10) ** (-3 + 6 * mp.mpf(j) / 4000)
        Wv = QT(mu * (1 + dv - 1j * wv)) / QT(mu)
        ang = mp.arg(Wv)
        if ang < 0:
            ang += 2 * mp.pi
        if ang <= th:
            dfc = mp.log(abs(Wv)) + rv * ang
        else:
            dfc = mp.nan
        if dfc == dfc:
            defect = max(defect, dfc)
    res5.append({"delta": float(dv), "w": float(wv), "primal_min_G": float(Gmin), "dual_max_defect": float(defect),
                 "signs_agree": bool((Gmin >= 0) == (defect <= 0))})
out["5_primal_dual_agreement"] = res5
out["ALL_EXACT_OK"] = bool(all(ok1) and ok2a and ok2b and ok2c)
with lane_guard.xopen(RUN + "/verify.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1)[:4000])

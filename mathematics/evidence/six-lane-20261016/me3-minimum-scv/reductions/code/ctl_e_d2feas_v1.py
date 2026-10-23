"""Control (e) for reduction L6 (D2 extreme rays and feasibility).

Real pole -1, pair -(1+delta) +- i omega, delta > 0, r = delta/omega, phi = omega tau.
h_tau(t) = 1 - e^{-delta (t - tau)} (cos omega (t - tau) + r sin omega (t - tau));  g(u) = e^{r u}(cos u - r sin u);
h_tau(0) = 1 - g(phi); feasibility (L6) <=> phi in [0, theta1(r)], theta1(r) the root of g = 1 in (pi, 2 pi).

CERTIFIED: exact sympy identities (h(tau) = 0, h' formula, h(0) = 1 - g(phi), g', dg/dr, span membership, the 2x2
           determinant); python-flint arb (prec 256) bisection enclosures of theta1(r) (signs of g - 1 certified at
           rational endpoints, monotonicity of g on [pi, 2pi] from the exact g' formula), certified dg/dr > 0 and
           dg/du > 0 on the enclosure, strict decrease of theta1 across r samples, certified h(0) < 0 on infeasible
           rays (phi slightly > theta1, and tau >= 2 pi/omega), certified h > 0 at every point of a grid on [0, 40]
           for a feasible ray with phi = theta1 - 1/100 (the all-t statement is the analytic L6 argument).
EXPLORATORY: mpmath quadrature of the moments vs the closed form m_k = k!(1 - Re[c zeta^{k+1}]).
Mutation controls: a shifted theta1 enclosure and a 'feasible' claim for an infeasible ray are rejected.
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
PI = arb.pi()
out = {"script": "ctl_e_d2feas_v1.py"}
checks = {}


def record(name, ok, detail=None):
    checks[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        print("FAIL", name, detail)


def to_fmpq(q):
    q = sp.Rational(q)
    return fmpq(int(q.p), int(q.q))


# ---------------- exact symbolic identities
t, tau_s, de, om, u, r_s = sp.symbols("t tau delta omega u r", positive=True)
s_ = t - tau_s
h = 1 - sp.exp(-de * s_) * (sp.cos(om * s_) + (de / om) * sp.sin(om * s_))
record("e0_h(tau)=0", sp.simplify(h.subs(t, tau_s)) == 0)
hp_claim = (om ** 2 + de ** 2) / om * sp.exp(-de * s_) * sp.sin(om * s_)
record("e0_h'_formula", sp.simplify(sp.diff(h, t) - hp_claim) == 0)
record("e0_h'(tau)=0", sp.simplify(hp_claim.subs(t, tau_s)) == 0)
g = sp.exp(r_s * u) * (sp.cos(u) - r_s * sp.sin(u))
h0 = sp.simplify(h.subs(t, 0))
g_at = g.subs({r_s: de / om, u: om * tau_s})
record("e0_h(0)=1-g(omega tau)", sp.simplify(sp.expand_trig(h0 - (1 - g_at))) == 0)
record("e0_g'_formula", sp.simplify(sp.diff(g, u) + (1 + r_s ** 2) * sp.exp(r_s * u) * sp.sin(u)) == 0)
record("e0_dg/dr_formula", sp.simplify(sp.diff(g, r_s) - (u * g - sp.exp(r_s * u) * sp.sin(u))) == 0)
# span membership: h = 1 - e^{-delta t}(A cos(omega t) + B sin(omega t))
Acoef = sp.exp(de * tau_s) * (sp.cos(om * tau_s) - (de / om) * sp.sin(om * tau_s))
Bcoef = sp.exp(de * tau_s) * (sp.sin(om * tau_s) + (de / om) * sp.cos(om * tau_s))
span_res = sp.simplify(sp.expand(sp.expand_trig(sp.expand(
    h - (1 - sp.exp(-de * t) * (Acoef * sp.cos(om * t) + Bcoef * sp.sin(om * t)))))))
record("e0_h_in_span{1, e^{-dt}cos, e^{-dt}sin}", span_res == 0, str(span_res))
Mdet = sp.Matrix([[-de, om], [-om, -de]]).det()
record("e0_derivative_map_det=delta^2+omega^2", sp.simplify(Mdet - (de ** 2 + om ** 2)) == 0)


# ---------------- arb helpers
def g_arb(uu, r):
    return (r * uu).exp() * (uu.cos() - r * uu.sin())


def h_arb(tt, tau, delta, omega):
    ss = tt - tau
    return 1 - (-delta * ss).exp() * ((omega * ss).cos() + (delta / omega) * (omega * ss).sin())


def theta1_enclosure(rq, nbis=110):
    r = arb(to_fmpq(rq))
    lo, hi = fmpq(31416, 10000), fmpq(62831, 10000)
    pre = {"lo>pi": bool(arb(lo) > PI), "hi<2pi": bool(arb(hi) < 2 * PI),
           "g(lo)<1": bool(g_arb(arb(lo), r) - 1 < 0), "g(hi)>1": bool(g_arb(arb(hi), r) - 1 > 0)}
    if not all(pre.values()):
        return None, None, pre
    for _ in range(nbis):
        mid = (lo + hi) / 2
        v = g_arb(arb(mid), r) - 1
        if v > 0:
            hi = mid
        elif v < 0:
            lo = mid
        else:
            break
    return lo, hi, pre


r_list = ["1/100000", "1/1000", "1/100", "1/10", "3/10", "1", "3", "10", "100"]
th = {}
encl_ok = True
deriv_ok = True
for rq in r_list:
    lo, hi, pre = theta1_enclosure(rq)
    if lo is None:
        encl_ok = False
        th[rq] = {"pre": pre}
        continue
    r = arb(to_fmpq(rq))
    U = arb(lo).union(arb(hi))
    dgr = U - (r * U).exp() * U.sin()
    dgu = -(1 + r * r) * (r * U).exp() * U.sin()
    sinneg = bool(U.sin() < 0)
    if not (dgr > 0 and dgu > 0 and sinneg):
        deriv_ok = False
    th[rq] = {"lo": arb(lo).str(35), "hi": arb(hi).str(35), "width": arb(hi - lo).str(3),
              "dg/dr_at_root(>0)": dgr.str(10), "dg/du_at_root(>0)": dgu.str(10), "pre": pre,
              "theta1-pi": (U - PI).str(12), "2pi-theta1": (2 * PI - U).str(12)}
    th[rq]["_lo"], th[rq]["_hi"] = lo, hi
record("e1_theta1_enclosures_certified", encl_ok)
record("e1_dg/dr>0_and_dg/du>0_on_enclosures", deriv_ok)
dec = encl_ok and all(th[r_list[k + 1]]["_hi"] < th[r_list[k]]["_lo"] for k in range(len(r_list) - 1))
record("e1_theta1_strictly_decreasing_on_samples", dec)
# small r: theta1(r) ~ 2 pi - sqrt(4 pi r) (heuristic size; the limit theta1 -> 2 pi is the analytic L6 argument)
record("e1_theta1(1/1000)_in_(2pi-0.12,2pi)", encl_ok and bool(2 * PI - arb(th["1/1000"]["_lo"]) < arb("0.12")),
       th["1/1000"].get("2pi-theta1"))
record("e1_theta1(1/100000)_in_(2pi-0.012,2pi)", encl_ok and bool(2 * PI - arb(th["1/100000"]["_lo"]) < arb("0.012")),
       th["1/100000"].get("2pi-theta1"))
record("e1_theta1(100)_in_(pi,pi+0.011)", encl_ok and bool(arb(th["100"]["_hi"]) - PI < arb("0.011")),
       th["100"].get("theta1-pi"))
out["e1_theta1"] = {k: {kk: vv for kk, vv in v.items() if not kk.startswith("_")} for k, v in th.items()}

# ---------------- rays at r = 3/10, omega = 1 (delta = 3/10)
rq = sp.Rational(3, 10)
r = arb(to_fmpq(rq))
omega = arb(1)
delta = r * omega
lo, hi = th["3/10"]["_lo"], th["3/10"]["_hi"]
phi_bad = hi + fmpq(1, 100)
tau_bad = arb(phi_bad) / omega
h0_bad = h_arb(arb(0), tau_bad, delta, omega)
record("e2_infeasible_phi=theta1+1/100_has_h(0)<0", bool(h0_bad < 0), h0_bad.str(15))
record("e2_h(0)=1-g(phi)_numeric_consistency", bool((h0_bad - (1 - g_arb(arb(phi_bad), r))).contains(0)))
phi_bad2 = 2 * PI + arb(fmpq(1, 10))
tau_bad2 = phi_bad2 / omega
hb2 = h_arb(arb(fmpq(1, 10)), tau_bad2, delta, omega)
record("e2_infeasible_tau>=2pi/omega_negative_at_t=tau-2pi/omega", bool(hb2 < 0), hb2.str(15))
record("e2_value_equals_1-e^{2 pi r}", bool((hb2 - (1 - (2 * PI * r).exp())).contains(0)))
# second infeasible example: r = 1, omega = 2 (delta = 2)
lo1, hi1 = th["1"]["_lo"], th["1"]["_hi"]
om2 = arb(2)
h0_bad3 = h_arb(arb(0), arb(hi1 + fmpq(1, 1000)) / om2, arb(2), om2)  # delta = r*omega = 1*2 = 2
record("e2_infeasible_r=1_omega=2_h(0)<0", bool(h0_bad3 < 0), h0_bad3.str(15))

phi_ok = lo - fmpq(1, 100)
tau_ok = arb(phi_ok) / omega
h0_ok = h_arb(arb(0), tau_ok, delta, omega)
record("e3_feasible_phi=theta1-1/100_has_h(0)>0", bool(h0_ok > 0), h0_ok.str(15))
grid_ok = True
gmin = None
ncontain = 0
for jj in range(0, 64 * 40 + 1):
    tt = arb(fmpq(jj, 64))
    hv = h_arb(tt, tau_ok, delta, omega)
    if hv.contains(0):
        ncontain += 1
    if not hv > 0:
        grid_ok = False
    if gmin is None or hv.mid() < gmin[0].mid():
        gmin = (hv, jj)
record("e3_feasible_ray_h>0_on_grid_j/64_j=0..2560", grid_ok and ncontain == 0,
       {"min": gmin[0].str(12), "at_t": "%d/64" % gmin[1]})
# other feasible phases at r = 3/10: h(0) >= 0 (phi = 0 gives the double zero at 0)
ph_samples = {"0": fmpq(0), "157/100": fmpq(157, 100), "3": fmpq(3), "4": fmpq(4)}
phs = {}
ph_ok = True
for name, phq in ph_samples.items():
    v = h_arb(arb(0), arb(phq) / omega, delta, omega)
    phs[name] = v.str(15)
    if name == "0":
        ph_ok = ph_ok and v.contains(0) and v.rad() < arb("1e-60")
    else:
        ph_ok = ph_ok and bool(v > 0)
record("e3_h(0)_at_feasible_phases(phi=0:exact_zero;_others>0)", ph_ok, phs)

# ---------------- closed-form moments vs quadrature (EXPLORATORY)
mp.mp.dps = 40
phi_m = mp.mpf(arb(phi_ok).mid().str(40, radius=False))
r_m = mp.mpf(3) / 10
om_m = mp.mpf(1)
de_m = r_m * om_m
tau_m = phi_m / om_m


def hm(tt):
    ss = tt - tau_m
    return 1 - mp.exp(-de_m * ss) * (mp.cos(om_m * ss) + r_m * mp.sin(om_m * ss))


cuts = [0, 1, 2, 4, float(tau_m), 6, 10, 20, 40, 80, mp.inf]
mq = [mp.quad(lambda tt: tt ** k * mp.exp(-tt) * hm(tt), cuts) for k in range(3)]
c = (1 - 1j * r_m) * mp.exp((r_m - 1j) * phi_m)
zeta = 1 / (1 + de_m - 1j * om_m)
mc = [mp.factorial(k) * (1 - mp.re(c * zeta ** (k + 1))) for k in range(3)]
record("e4_closed_form_moments_vs_quadrature_EXPLORATORY", max(abs(a - b) for a, b in zip(mq, mc)) < mp.mpf("1e-25"),
       [mp.nstr(a - b, 5) for a, b in zip(mq, mc)])
# the same with arb (certified evaluation of the closed form)
cb = acb(1, -r) * acb((r * arb(phi_ok)).exp() * arb(phi_ok).cos(), -(r * arb(phi_ok)).exp() * arb(phi_ok).sin())
zb = 1 / acb(1 + delta, -omega)
mb = []
zk = zb
for k in range(3):
    mb.append([1, 1, 2][k] * (1 - (cb * zk).real))
    zk = zk * zb
Sb = mb[0] * mb[2] / (mb[1] * mb[1]) - 1
out["e4_feasible_ray_moments"] = {"phi": arb(phi_ok).str(30), "closed_form_arb": [x.str(25) for x in mb],
                                  "quadrature_EXPLORATORY": [mp.nstr(x, 25) for x in mq], "SCV_arb": Sb.str(25)}

# ---------------- mutation controls
mut = {}
lo_m, hi_m = lo + fmpq(1, 100), hi + fmpq(1, 100)
g_lo_m = g_arb(arb(lo_m), r) - 1
mut["M1_theta1_enclosure_shifted_by_+1/100"] = {"g(lo')-1": g_lo_m.str(10), "rejected": bool(g_lo_m > 0)}
mut["M2_claim_phi=theta1+1/100_feasible"] = {"h(0)": h0_bad.str(10), "rejected": bool(h0_bad < 0)}
record("e5_all_mutations_rejected", all(v["rejected"] for v in mut.values()))
out["e5_mutations"] = mut
out["rays"] = {"r": "3/10", "omega": "1", "delta": "3/10", "theta1_lo": arb(lo).str(30), "theta1_hi": arb(hi).str(30),
               "phi_infeasible": arb(phi_bad).str(30), "h0_infeasible": h0_bad.str(20),
               "phi_feasible": arb(phi_ok).str(30), "h0_feasible": h0_ok.str(20), "h_tau>=2pi_example": hb2.str(20),
               "grid_min_feasible": gmin[0].str(15), "grid_min_at_t": "%d/64" % gmin[1]}

out["checks"] = checks
out["all_pass"] = all(v["pass"] for v in checks.values())
out["elapsed_s"] = round(time.time() - T0, 2)
with lane_guard.xopen(os.path.join(RUN, "ctl_e.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "n_checks": len(checks),
                  "failed": [k for k, v in checks.items() if not v["pass"]], "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if out["all_pass"] else 1)

"""Control (c) for reduction L5: v_cos := min_{omega>0, phi} SCV(e^{-t}(1 - cos(omega t - phi))).

v2 (2026-10-18): identical to v1 except mutation M3.  In v1 the "too-strong Lemma 5.5 constant" was 0.5, which is
BELOW the true minimum of SCV at omega = 4 (~0.547, v1 grid), so v1's M3 was correctly NOT violated and v1 exited 1
on c6_all_mutations_rejected (a control-design error, not a mathematical failure; v1 stays as a failed attempt).
v2 uses the constant 0.6 (above the sampled omega = 4 minimum) and records the sampled minimum.

Closed form (L5.2): m_k = k! (1 - Re[e^{-i phi} (1 - i omega)^{-(k+1)}]),  SCV = m0 m2 / m1^2 - 1.

EXPLORATORY (labelled): mpmath (80 digits) Newton iteration on the analytic gradient from the parent point; Hessian;
                        float64 numpy grid scans (global landscape on [1/4,4] x [0,2pi) and the tails).
CERTIFIED: python-flint acb/arb (prec 320) evaluation at an explicit rational point => v_cos <= U (exact decimal U);
           exact sympy Sturm certificate Delta3 > 2765/10000 (re-done here) and the exact tail constants of
           Lemma 5.4 (omega <= 1/4) and Lemma 5.5 (omega >= 4); arb sample checks of Lemma 5.3 (algebraic form),
           5.4 and 5.5 at rational sample points; band check 0.20090144 <= v_cos <= 0.20090185 (STOP otherwise).
Mutation controls: a too-small U, a strengthened Lemma 5.4 constant and a too-strong Lemma 5.5 constant are rejected.
"""
import os
import sys
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import numpy as np  # noqa: E402
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from flint import arb, acb, fmpq, ctx  # noqa: E402

RUN = sys.argv[1]
T0 = time.time()
out = {"script": "ctl_c_vcos_v2.py"}
checks = {}


def record(name, ok, detail=None):
    checks[name] = {"pass": bool(ok), "detail": detail}
    if not ok:
        print("FAIL", name, detail)


def to_fmpq(q):
    q = sp.Rational(q)
    return fmpq(int(q.p), int(q.q))


# ======================= EXPLORATORY: high-precision local optimization
mp.mp.dps = 80


def mp_A(w, p):
    z = 1 / mp.mpc(1, -w)
    e = mp.expj(-p)
    return [1 - mp.re(e * z ** (k + 1)) for k in range(3)], z, e


def mp_S(w, p):
    A, _, _ = mp_A(w, p)
    return 2 * A[0] * A[2] / A[1] ** 2 - 1


def mp_grad(w, p):
    A, z, e = mp_A(w, p)
    Aw = [(k + 1) * mp.im(e * z ** (k + 2)) for k in range(3)]
    Ap = [-mp.im(e * z ** (k + 1)) for k in range(3)]

    def dS(dA):
        return 2 * (dA[0] * A[2] / A[1] ** 2 + A[0] * dA[2] / A[1] ** 2 - 2 * A[0] * A[2] * dA[1] / A[1] ** 3)
    return [dS(Aw), dS(Ap)]


w, p = mp.mpf("1.0359329551"), mp.mpf("0.3370382424")
# gradient sanity check vs finite differences (EXPLORATORY)
g_an = mp_grad(w, p)
g_fd = [mp.diff(lambda x: mp_S(x, p), w), mp.diff(lambda y: mp_S(w, y), p)]
record("c0_gradient_formula_vs_mp.diff_EXPLORATORY", max(abs(g_an[0] - g_fd[0]), abs(g_an[1] - g_fd[1])) < mp.mpf("1e-50"),
       [mp.nstr(g_an[0] - g_fd[0], 5), mp.nstr(g_an[1] - g_fd[1], 5)])
hist = []
for it in range(80):
    g = mp_grad(w, p)
    Hww = mp.diff(lambda x: mp_grad(x, p)[0], w)
    Hwp = mp.diff(lambda y: mp_grad(w, y)[0], p)
    Hpw = mp.diff(lambda x: mp_grad(x, p)[1], w)
    Hpp = mp.diff(lambda y: mp_grad(w, y)[1], p)
    det = Hww * Hpp - Hwp * Hpw
    dw = (Hpp * g[0] - Hwp * g[1]) / det
    dp = (-Hpw * g[0] + Hww * g[1]) / det
    w, p = w - dw, p - dp
    step = max(abs(dw), abs(dp))
    hist.append(mp.nstr(step, 5))
    if step < mp.mpf("1e-72"):
        break
vS = mp_S(w, p)
g = mp_grad(w, p)
H = mp.matrix([[mp.diff(lambda x: mp_grad(x, p)[0], w), mp.diff(lambda y: mp_grad(w, y)[0], p)],
               [mp.diff(lambda x: mp_grad(x, p)[1], w), mp.diff(lambda y: mp_grad(w, y)[1], p)]])
ev = mp.eig(H)[0]
ev = sorted([mp.re(x) for x in ev])
record("c1_newton_converged_EXPLORATORY", len(hist) < 80 and max(abs(g[0]), abs(g[1])) < mp.mpf("1e-60"),
       {"steps": hist, "grad": [mp.nstr(g[0], 5), mp.nstr(g[1], 5)]})
record("c1_hessian_positive_definite_EXPLORATORY", ev[0] > 0, [mp.nstr(x, 20) for x in ev])
band_ok = mp.mpf("0.20090144") <= vS <= mp.mpf("0.20090185")
record("c1_v_cos_in_contract_band_[0.20090144,0.20090185]", band_ok, mp.nstr(vS, 30))
beta = mp.atan(w)
psi = p - 2 * beta
u_star = 1 - mp.cos(psi)
S_star = mp.sin(psi)
out["c1_local_min_EXPLORATORY"] = {
    "v_cos": mp.nstr(vS, 60), "1/v_cos": mp.nstr(1 / vS, 40), "omega*": mp.nstr(w, 50), "phi*": mp.nstr(p, 50),
    "psi*=phi*-2atan(omega*)": mp.nstr(psi, 40), "u*=1-cos(psi*)": mp.nstr(u_star, 40), "sin(psi*)": mp.nstr(S_star, 30),
    "hessian_eigenvalues": [mp.nstr(x, 20) for x in ev], "newton_steps": hist,
    "label": "EXPLORATORY: stationary point found by Newton at 80 digits; local minimality from the Hessian; "
             "global minimality is NOT established by this computation"}


# (w,u) reduced form of Lemma 5.3/5.4 (minimizing sign S = -sqrt(u(2-u))), EXPLORATORY consistency
def mp_F(wv, uv, sign=-1):
    X = wv ** 2 + uv
    a = wv ** 2 * (1 + wv ** 2)
    Y = sign * wv * mp.sqrt(uv * (2 - uv))
    return 2 * (X * X + a * X + a * Y - Y * Y) / ((1 + wv ** 2) * X * X) - 1


record("c1_reduced_form_matches_EXPLORATORY", abs(mp_F(w, u_star, -1 if S_star < 0 else 1) - vS) < mp.mpf("1e-70")
       and S_star < 0, mp.nstr(mp_F(w, u_star) - vS, 5))
if not band_ok:
    print("STOP: v_cos outside contract band -> convention error")


# ======================= EXPLORATORY: float64 landscape scans
def np_S(W, Pp):
    z = 1.0 / (1.0 - 1j * W)
    e = np.exp(-1j * Pp)
    A = [1 - np.real(e * z ** (k + 1)) for k in range(3)]
    return 2 * A[0] * A[2] / A[1] ** 2 - 1


Wg = np.linspace(0.25, 4.0, 1501)
Pg = np.linspace(0.0, 2 * np.pi, 2400, endpoint=False)
WW, PP = np.meshgrid(Wg, Pg, indexing="ij")
SS = np_S(WW, PP)
i, j = np.unravel_index(np.argmin(SS), SS.shape)
far = (np.abs(WW - float(w)) > 0.05) | (np.minimum(np.abs(PP - float(p)), 2 * np.pi - np.abs(PP - float(p))) > 0.05)
out["c2_grid_middle_EXPLORATORY"] = {"grid_min": float(SS[i, j]), "at_omega": float(Wg[i]), "at_phi": float(Pg[j]),
                                     "min_outside_0.05_nbhd_of_local_min": float(SS[far].min()),
                                     "grid": "omega in linspace(0.25,4,1501), phi in [0,2pi) 2400 pts"}
record("c2_grid_min_near_local_min_EXPLORATORY", abs(Wg[i] - float(w)) < 0.01 and SS[far].min() > float(vS) + 1e-4)
tails = {}
for lo_, hi_ in [(0.001, 0.25), (4.0, 1000.0)]:
    Wt = np.exp(np.linspace(np.log(lo_), np.log(hi_), 801))
    Pt = np.linspace(0.0, 2 * np.pi, 4000, endpoint=False)
    A_, B_ = np.meshgrid(Wt, Pt, indexing="ij")
    St = np_S(A_, B_)
    tails["omega in [%g,%g]" % (lo_, hi_)] = float(St.min())
out["c2_grid_tails_EXPLORATORY"] = tails

# ======================= CERTIFIED: upper bound U at an explicit rational point
ctx.prec = 320


def arb_S(wb, pb):
    z = 1 / acb(1, -wb)
    e = acb(pb.cos(), -pb.sin())
    A = []
    zk = z
    for k in range(3):
        A.append(1 - (e * zk).real)
        zk = zk * z
    return 2 * A[0] * A[2] / (A[1] * A[1]) - 1, A


w0q = sp.Rational(mp.nstr(w, 13, strip_zeros=False))  # 13 significant digits
p0q = sp.Rational(mp.nstr(p, 13, strip_zeros=False))
Sb, Ab = arb_S(arb(to_fmpq(w0q)), arb(to_fmpq(p0q)))
U = sp.Rational(Sb.mid().str(40, radius=False)) + sp.Rational(1, 10 ** 30)
U_cert = bool(arb(to_fmpq(U)) > Sb)
record("c3_v_cos_le_SCV(w0,p0)_lt_U", U_cert, {"U": str(sp.N(U, 40))})
record("c3_U_lt_0.2010", U < sp.Rational(2010, 10000))
record("c3_m1_positive", bool(Ab[1] > 0))
out["c3_certified_upper_bound"] = {
    "omega0": str(w0q), "phi0": str(p0q), "SCV_ball": Sb.str(45), "1/SCV_ball": (1 / Sb).str(30),
    "U_exact_decimal": str(U), "label": "CERTIFIED: arb ball; v_cos <= SCV(omega0,phi0) < U by definition of v_cos"}

# ======================= CERTIFIED: tail constants
tau = sp.Symbol("tau", real=True)
Pp_ = sp.expand((tau ** 2 - 2 * tau + 2) * (2 * tau ** 2 - 12 * tau + 24))
Qq_ = tau ** 2 - 4 * tau + 6
D3lo = sp.Rational(2765, 10000)
qq = sp.Poly(sp.expand(Pp_ - (1 + D3lo) * Qq_ ** 2), tau)
d3cert = qq.LC() > 0 and qq.count_roots() == 0
record("c4_Delta3_gt_0.2765_Sturm", d3cert)
small_const = (D3lo - sp.Rational(1, 16)) / (1 + sp.Rational(1, 16))  # (Delta3 - w^2)/(1+w^2) at w = 1/4
record("c4_Lemma5.4_const_omega<=1/4_gt_0.2014", small_const > sp.Rational(2014, 10000), str(sp.N(small_const, 20)))
rho_bar = sp.Rational(2426, 10000)
record("c4_rho_bar_sq_gt_1/17", rho_bar ** 2 > sp.Rational(1, 17))
big_const = 2 * (1 - rho_bar) * (1 - rho_bar ** 3) / (1 + rho_bar ** 2) ** 2 - 1
record("c4_Lemma5.5_const_omega>=4_gt_0.33", big_const > sp.Rational(33, 100), str(sp.N(big_const, 20)))
record("c4_U_lt_both_tail_constants", U < small_const and U < big_const)
out["c4_tail_constants"] = {"Delta3_lower_used": str(D3lo), "Lemma5.4_bound_at_omega=1/4": str(small_const),
                            "Lemma5.4_bound_decimal": str(sp.N(small_const, 20)), "rho_bar": str(rho_bar),
                            "Lemma5.5_bound_rho_bar": str(big_const), "Lemma5.5_bound_decimal": str(sp.N(big_const, 20))}

# ======================= CERTIFIED sample checks of Lemma 5.3 / 5.4 / 5.5 at rational points (arb)
lo_arb = arb(to_fmpq(D3lo))


def arb_reduced(wb, pb):
    beta = wb.atan()
    psi_ = pb - 2 * beta
    C = psi_.cos()
    S_ = psi_.sin()
    u = 1 - C
    X = wb * wb + u
    a = wb * wb * (1 + wb * wb)
    Y = wb * S_
    return 2 * (X * X + a * X + a * Y - Y * Y) / ((1 + wb * wb) * X * X) - 1


ws_s = ["1/100", "1/20", "1/10", "1/5", "1/4", "1/2", "1", "2", "4", "10", "100"]
nphi = 96
worst54 = None
worst55 = None
max_id_rad = arb(0)
id_ok = True
ineq54_ok = True
ineq55_ok = True
for ws in ws_s:
    wq = sp.Rational(ws)
    wb = arb(to_fmpq(wq))
    for jj in range(nphi):
        pq = sp.Rational(2 * 314159265358979, 100000000000000) * jj / nphi
        pb = arb(to_fmpq(pq))
        S1, _ = arb_S(wb, pb)
        S2 = arb_reduced(wb, pb)
        if not (S1 - S2).contains(0):
            id_ok = False
        max_id_rad = max_id_rad.max((S1 - S2).rad())
        # Lemma 5.4: 1 + SCV >= (1 + Delta3)/(1 + w^2); certified with Delta3 > 0.2765
        gap54 = (1 + S1) - (1 + lo_arb) / (1 + wb * wb)
        if not gap54 > 0:
            ineq54_ok = False
        if worst54 is None or gap54.mid() < worst54[0].mid():
            worst54 = (gap54, ws, str(pq))
        if wq >= 4:
            rho = 1 / (1 + wb * wb).sqrt()
            b55 = 2 * (1 - rho) * (1 - rho ** 3) / ((1 + rho * rho) ** 2) - 1
            gap55 = S1 - b55
            if not gap55 >= 0:
                ineq55_ok = False
            if worst55 is None or gap55.mid() < worst55[0].mid():
                worst55 = (gap55, ws, str(pq))
record("c5_Lemma5.3_identity_at_samples", id_ok, max_id_rad.str(5))
record("c5_Lemma5.4_at_samples", ineq54_ok, {"min_gap": worst54[0].str(10), "omega": worst54[1], "phi": worst54[2]})
record("c5_Lemma5.5_at_samples", ineq55_ok, {"min_gap": worst55[0].str(10), "omega": worst55[1], "phi": worst55[2]})

# EXPLORATORY: tightness of Lemma 5.4 as omega -> 0 (min over phi of SCV vs Delta3)
tight = []
for wv in ["0.001", "0.01", "0.1"]:
    Pt = np.linspace(0.0, 2 * np.pi, 200001)
    St = np_S(float(wv) * np.ones_like(Pt), Pt)
    tight.append({"omega": wv, "min_phi_SCV_float": float(St.min()),
                  "Lemma5.4_bound": float((0.27658253078 - float(wv) ** 2) / (1 + float(wv) ** 2))})
out["c5_tightness_EXPLORATORY"] = tight

# ======================= mutation controls (must be rejected)
mut = {}
U_bad = sp.Rational(Sb.lower().str(40, radius=False)) - sp.Rational(1, 10 ** 25)
mut["M1_U_below_ball"] = {"U_bad": str(sp.N(U_bad, 35)), "certified": bool(arb(to_fmpq(U_bad)) > Sb),
                          "rejected": not bool(arb(to_fmpq(U_bad)) > Sb)}
# strengthened Lemma 5.4: 1+SCV >= (1 + Delta3 + 0.01)/(1+w^2) must fail at some sample (omega = 1/100)
wb = arb(to_fmpq(sp.Rational(1, 100)))
viol = None
for jj in range(20000):
    pq = sp.Rational(jj, 10000) * sp.Rational(1, 50)  # phi in [0, 0.04): near 2*omega for omega = 0.01
    pb = arb(to_fmpq(pq))
    S1, _ = arb_S(wb, pb)
    if bool((1 + S1) < (1 + lo_arb + arb("0.01")) / (1 + wb * wb)):
        viol = {"omega": "1/100", "phi": str(pq), "SCV": S1.str(15)}
        break
mut["M2_Lemma5.4_plus_0.01"] = {"violation": viol, "rejected": viol is not None}
# v2: too-strong Lemma 5.5 constant 0.6 at omega = 4 (v1 used 0.5 < true minimum ~0.547: not violated)
wb = arb(4)
viol = None
min_s4 = None
for jj in range(4000):
    pq = sp.Rational(2 * 314159265358979, 100000000000000) * jj / 4000
    pb = arb(to_fmpq(pq))
    S1, _ = arb_S(wb, pb)
    if min_s4 is None or S1.mid() < min_s4[0].mid():
        min_s4 = (S1, str(sp.N(pq, 15)))
    if viol is None and bool(S1 < arb("0.6")):
        viol = {"omega": "4", "phi": str(sp.N(pq, 15)), "SCV": S1.str(15)}
mut["M3_Lemma5.5_const_0.6"] = {"violation": viol, "rejected": viol is not None,
                                "sampled_min_SCV_at_omega=4": min_s4[0].str(15), "at_phi": min_s4[1]}
record("c6_all_mutations_rejected", all(v["rejected"] for v in mut.values()))
out["c6_mutations"] = mut

out["checks"] = checks
out["all_pass"] = all(v["pass"] for v in checks.values())
out["elapsed_s"] = round(time.time() - T0, 2)
with lane_guard.xopen(os.path.join(RUN, "ctl_c.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"all_pass": out["all_pass"], "n_checks": len(checks),
                  "failed": [k for k, v in checks.items() if not v["pass"]],
                  "v_cos_local_EXPLORATORY": mp.nstr(vS, 25), "U": str(sp.N(U, 30)), "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if out["all_pass"] else 1)

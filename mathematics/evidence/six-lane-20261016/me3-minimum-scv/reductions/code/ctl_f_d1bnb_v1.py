"""Control (f) (optional): CERTIFIED lower bound v_cos >= L by interval branch-and-bound + written tail lemmas.

Reduction (reductions-v1 Lemma 5.3 / proof of 5.4): for omega > 0 and any phi,
  SCV(omega, phi) >= F(w, u) := 2 (X^2 + a X - a Y - Y^2) / ((1 + w^2) X^2) - 1,
  w = omega, u = 1 - cos(phi - 2 atan omega) in [0, 2], X = w^2 + u, a = w^2 (1 + w^2), Y = w sqrt(u (2 - u)) >= 0,
with equality for the phase with sin(phi - 2 atan omega) <= 0.  Hence v_cos = inf_{w > 0, 0 <= u <= 2} F(w, u).
Cover of (0, inf) x [0, 2]:
  * w <= w_lo : Lemma 5.4 (F >= (Delta3 - w^2)/(1 + w^2), decreasing in w), Delta3 > 2765/10000 re-certified (Sturm);
  * w >= w_hi : Lemma 5.5 (SCV >= 2(1-rho)(1-rho^3)/(1+rho^2)^2 - 1, rho = (1+w^2)^{-1/2} <= rho_bar, exact rational);
  * [w_lo, w_hi] x [0, 2]: python-flint arb (prec 128) branch-and-bound on dyadic boxes.  A box is certified if the
    natural interval extension of F, or the mean-value (centered) form F(c) - sup|F_w| h_w - sup|F_u| h_u (only on
    boxes with 0 < u_lo, u_hi < 2, where F is C^1), exceeds L.  Rounding is outward (arb balls).  A box is never
    discarded otherwise; if the center has a certified F(c) < L, the claimed bound is refuted and the run stops.
Usage: ctl_f_d1bnb_v1.py RUN L W_LO W_HI EXPECT MAX_BOXES   (EXPECT = certify | reject; exit 0 iff outcome == EXPECT)
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
L_str, wlo_str, whi_str, EXPECT, MAXB = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6])
T0 = time.time()
ctx.prec = 128
out = {"script": "ctl_f_d1bnb_v1.py", "argv": sys.argv[2:], "label": "CERTIFIED (arb balls, exact rationals)"}


def to_fmpq(q):
    q = sp.Rational(q)
    return fmpq(int(q.p), int(q.q))


Lq = sp.Rational(L_str)
Lf = to_fmpq(Lq)
La = arb(Lf)
w_lo = sp.Rational(wlo_str)
w_hi = sp.Rational(whi_str)

# ---------------- tails (exact)
tau = sp.Symbol("tau", real=True)
P = sp.expand((tau ** 2 - 2 * tau + 2) * (2 * tau ** 2 - 12 * tau + 24))
Q = tau ** 2 - 4 * tau + 6
D3lo = sp.Rational(2765, 10000)
qq = sp.Poly(sp.expand(P - (1 + D3lo) * Q ** 2), tau)
d3_ok = bool(qq.LC() > 0 and qq.count_roots() == 0)
small_tail = (D3lo - w_lo ** 2) / (1 + w_lo ** 2)
# rho_bar >= (1 + w_hi^2)^{-1/2}: smallest 10-digit decimal whose square is >= 1/(1 + w_hi^2)
rb = (arb(1) / (arb(to_fmpq(1 + w_hi ** 2))).sqrt()).upper()
rho_bar = sp.ceiling(sp.Rational(rb.str(30, radius=False)) * 10 ** 10) / sp.Integer(10) ** 10
rho_ok = rho_bar ** 2 >= 1 / (1 + w_hi ** 2) and rho_bar < 1
big_tail = 2 * (1 - rho_bar) * (1 - rho_bar ** 3) / (1 + rho_bar ** 2) ** 2 - 1
tails_ok = d3_ok and rho_ok and small_tail > Lq and big_tail > Lq
out["tails"] = {"Delta3_gt_2765/10000_Sturm": d3_ok, "w_lo": str(w_lo), "Lemma5.4_bound_at_w_lo": str(sp.N(small_tail, 20)),
                "w_hi": str(w_hi), "rho_bar": str(rho_bar), "rho_bar_ok": bool(rho_ok),
                "Lemma5.5_bound": str(sp.N(big_tail, 20)), "both_tails_exceed_L": bool(tails_ok)}


# ---------------- F and its gradient on arb balls
def F_ball(w, u):
    w2 = w * w
    X = w2 + u
    a = w2 * (1 + w2)
    g = (u * (2 - u)).nonnegative_part()
    Y = w * g.sqrt()
    YY = w2 * g
    Phi = 1 + a / X - (a * Y + YY) / (X * X)
    return 2 * Phi / (1 + w2) - 1


def grad_ball(w, u):
    w2 = w * w
    X = w2 + u
    a = w2 * (1 + w2)
    g = u * (2 - u)
    R = g.sqrt()
    Y = w * R
    YY = w2 * g
    X2 = X * X
    X3 = X2 * X
    aw = 2 * w + 4 * w * w2
    Yu = w * (1 - u) / R
    Yw = R
    YYu = w2 * (2 - 2 * u)
    YYw = 2 * w * g
    Phi = 1 + a / X - (a * Y + YY) / X2
    Phi_u = -a / X2 - (a * Yu + YYu) / X2 + 2 * (a * Y + YY) / X3
    Phi_w = aw / X - a * 2 * w / X2 - (aw * Y + a * Yw + YYw) / X2 + 2 * (a * Y + YY) * 2 * w / X3
    opw = 1 + w2
    return 2 * Phi_w / opw - 4 * w * Phi / (opw * opw), 2 * Phi_u / opw


# gradient sanity check (finite differences at points, 1e-20 steps at prec 128; EXPLORATORY)
gchk = []
for (wq, uq) in [("1.0359329550858568", "0.7028149519884834"), ("0.5", "1.3"), ("3", "0.2")]:
    wb, ub = arb(to_fmpq(sp.Rational(wq))), arb(to_fmpq(sp.Rational(uq)))
    hh = arb(fmpq(1, 10 ** 15))
    fdw = (F_ball(wb + hh, ub) - F_ball(wb - hh, ub)) / (2 * hh)
    fdu = (F_ball(wb, ub + hh) - F_ball(wb, ub - hh)) / (2 * hh)
    gw, gu = grad_ball(wb, ub)
    gchk.append({"w": wq, "u": uq, "Fw": gw.str(12), "fd_w": fdw.str(12), "Fu": gu.str(12), "fd_u": fdu.str(12),
                 "agree_1e-12": bool(abs(gw - fdw) < arb("1e-12") and abs(gu - fdu) < arb("1e-12"))})
out["gradient_check_EXPLORATORY"] = gchk
Fstar = F_ball(arb(to_fmpq(sp.Rational("1.0359329550858567909065869278226347339723"))),
               arb(to_fmpq(sp.Rational("0.7028149519884833734825198194904334286242"))))
out["F_at_EXPLORATORY_minimizer"] = Fstar.str(30)


def iv(lo, hi):
    return arb(lo).union(arb(hi))


# ---------------- branch and bound on [w_lo, w_hi] x [0, 2]
stack = [(to_fmpq(w_lo), to_fmpq(w_hi), fmpq(0), fmpq(2), 0)]
n_boxes = 0
n_nat = 0
n_cen = 0
max_depth = 0
min_center = None
refuted = None
aborted = False
while stack:
    wl, wh, ul, uh, dep = stack.pop()
    n_boxes += 1
    if n_boxes > MAXB:
        aborted = True
        break
    max_depth = max(max_depth, dep)
    W = iv(wl, wh)
    U = iv(ul, uh)
    if F_ball(W, U) > La:
        n_nat += 1
        continue
    wc = (wl + wh) / 2
    uc = (ul + uh) / 2
    Fc = F_ball(arb(wc), arb(uc))
    if min_center is None or Fc.mid() < min_center[0].mid():
        min_center = (Fc, wc, uc)
    if Fc < La:
        refuted = {"w": str(wc), "u": str(uc), "F(center)": Fc.str(25)}
        break
    if ul > 0 and uh < 2:
        gw, gu = grad_ball(W, U)
        err = gw.abs_upper() * arb((wh - wl) / 2) + gu.abs_upper() * arb((uh - ul) / 2)
        if (Fc - err) > La:
            n_cen += 1
            continue
    if dep >= 200:
        aborted = True
        refuted = refuted or {"depth_limit_box": [str(wl), str(wh), str(ul), str(uh)]}
        break
    if (wh - wl) >= (uh - ul):
        wm = (wl + wh) / 2
        stack.append((wl, wm, ul, uh, dep + 1))
        stack.append((wm, wh, ul, uh, dep + 1))
    else:
        um = (ul + uh) / 2
        stack.append((wl, wh, ul, um, dep + 1))
        stack.append((wl, wh, um, uh, dep + 1))

middle_certified = (not aborted) and (refuted is None) and not stack
certified = bool(middle_certified and tails_ok)
outcome = "certify" if certified else "reject"
out["bnb"] = {"boxes_processed": n_boxes, "certified_by_natural_extension": n_nat, "certified_by_centered_form": n_cen,
              "max_depth": max_depth, "aborted_box_limit_or_depth": aborted, "refutation": refuted,
              "remaining_stack": len(stack),
              "min_F_at_box_centers": None if min_center is None else
              {"F": min_center[0].str(25), "w": str(min_center[1]), "u": str(min_center[2])}}
out["result"] = {"L": L_str, "certified_v_cos_ge_L": certified, "outcome": outcome, "expected": EXPECT,
                 "outcome_matches_expectation": outcome == EXPECT,
                 "statement": ("v_cos >= %s (tails: Lemmas 5.4/5.5; middle: B&B)" % L_str) if certified else
                 "claimed lower bound NOT certified (see refutation / tails / abort flags)"}
out["elapsed_s"] = round(time.time() - T0, 2)
with lane_guard.xopen(os.path.join(RUN, "ctl_f.json")) as fh:
    json.dump(out, fh, indent=1, default=str)
print(json.dumps({"outcome": outcome, "expected": EXPECT, "boxes": n_boxes, "natural": n_nat, "centered": n_cen,
                  "max_depth": max_depth, "tails_ok": bool(tails_ok), "refuted": refuted,
                  "elapsed_s": out["elapsed_s"]}))
sys.exit(0 if outcome == EXPECT else 1)

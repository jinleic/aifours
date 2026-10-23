"""INDEPENDENT point-evaluation replay of dual-chart certificate leaves (Lemma D membership; smoke test, NOT a
certificate).  Written by MathPhaseType3.ME3Reductions from the definitions in the task message and in
proof/charts-spec-v1.md (read-only); imports nothing from the lane's code/ directory.

Lemma D test at a physical point (s, delta, omega), s in [0, 1], delta >= 0, omega > 0 finite:
  xi = delta - i omega, mu = s/(1 - s), Q(y) = (kappa y^2 - 2 y + 2)/y^3, kappa = 50/61,
  W = Q(mu (1 + xi)) / Q(mu) for 0 < s < 1;  limits W = (1 + xi)^{-3} (s = 0) and W = (1 + xi)^{-1} (s = 1)
  (from Q(y) ~ 2/y^3 as y -> 0 and Q(y) ~ kappa/y as y -> oo).
  H = conv({0} u {e^{-xi t} : t >= 0}); spiral in polar form rho = e^{-r theta}, r = delta/omega.
  EXACT membership (own derivation; the chord through 1 and P1 = e^{(-r+i) theta1} is tangent to the spiral at P1 iff
  g_r(theta1) = e^{r theta1}(cos theta1 - r sin theta1) = 1, theta1 in (pi, 2 pi)):
    r = 0: |W| <= 1.  r > 0: alpha = smallest nonnegative argument of W in [0, 2 pi);
    alpha <= theta1: RADIAL |W| <= e^{-r alpha};  alpha > theta1: CHORD, W on the 0-side of the line through 1 and P1.
  CROSS-CHECK (independent): support function sigma(psi) = max(0, cos psi, cos(gamma) e^{-r ((psi - gamma) mod 2 pi)}),
    gamma = arctan r, i.e. the exact max over t >= 0 of Re(e^{-i psi} e^{-xi t}) together with 0; W in H iff
    Re(e^{-i psi} W) <= sigma(psi) for all psi; checked on a 2880-direction grid in float64.
Chart variables -> (s, delta, omega) (charts-spec-v1.md):
  SWC, SWB, G: (s, delta, omega).   LW: (s, delta, nu), omega = 1/nu.
  LD1: (s, d, beta), delta = 1/d - 1, omega = tan(beta)/d.
  LD2: (chi, rho_t, beta), s = chi rho_t, d = (1 - chi) rho_t / cos(beta), then as LD1.
  Non-physical points (omega = 0 or infinite, d = 0, beta >= pi/2, beta = 0, cos(beta) <= 0) are skipped and counted.
Points per box: PRIMARY = midpoint + 8 corners; EXTRA = other 18 points of the 3x3x3 grid + 8 corners moved 1/64 of the
  way to the midpoint.  Outcomes starting with "SKIP" are not tested (their geometric rule is checked at the box for
  G and LD2); any other non-CERT outcome is reported.
Usage: replay_dual_v1.py RUN CHART SAMPLE_PATH
"""
import os
import sys
import json
import time
import hashlib
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import mpmath as mp  # noqa: E402
import numpy as np  # noqa: E402

RUN, CHART, SAMPLE = sys.argv[1], sys.argv[2], sys.argv[3]
assert CHART in ("SWC", "SWB", "G", "LW", "LD1", "LD2")
T0 = time.time()
mp.mp.dps = 50
KAPPA = mp.mpf(50) / 61
PI = mp.pi
TINY = mp.mpf(10) ** -40


def mpq(q):
    return mp.mpf(q.numerator) / q.denominator


def to_physical(chart, v):
    """v = exact chart point (Fractions) -> (s, delta, omega) as mpf, or (None, reason)."""
    a, b, c = v
    if chart in ("SWC", "SWB", "G"):
        if c <= 0:
            return None, "omega<=0"
        return (mpq(a), mpq(b), mpq(c)), None
    if chart == "LW":
        if c <= 0:
            return None, "nu=0 (omega=inf)"
        return (mpq(a), mpq(b), 1 / mpq(c)), None
    if chart == "LD1":
        s, d, be = mpq(a), b, mpq(c)
        if d <= 0:
            return None, "d=0 (delta=inf)"
        if be <= 0 or be >= PI / 2:
            return None, "beta not in (0, pi/2)"
        dm = mpq(d)
        return (s, 1 / dm - 1, mp.tan(be) / dm), None
    chi, rt, be = a, b, mpq(c)  # LD2
    if be <= 0 or be >= PI / 2:
        return None, "beta not in (0, pi/2)"
    s = mpq(chi * rt)
    dnum = (1 - chi) * rt
    if dnum <= 0:
        return None, "d=0 (delta=inf)"
    dm = mpq(dnum) / mp.cos(be)
    return (s, 1 / dm - 1, mp.tan(be) / dm), None


def Q(y):
    return (KAPPA * y * y - 2 * y + 2) / y ** 3


def W_of(s, de, om):
    one_xi = mp.mpc(1 + de, -om)
    if s == 0:
        return 1 / one_xi ** 3
    if s == 1:
        return 1 / one_xi
    mu = s / (1 - s)
    return Q(mu * one_xi) / Q(mu)


def g(r, u):
    return mp.exp(r * u) * (mp.cos(u) - r * mp.sin(u))


_th = {}


def theta1(r):
    """Root of g_r = 1 in (pi, 2pi): 60 bisection steps, then a bracketed solve, accepted only if g - 1 changes sign
    across th -+ 1e-45 th; otherwise bisection continues to full precision (robust for huge r, theta1 - pi ~ 1/r)."""
    key = mp.nstr(r, 45)
    if key in _th:
        return _th[key]
    lo, hi = PI, 2 * PI
    assert g(r, lo) - 1 < 0 and g(r, hi) - 1 > 0
    for _ in range(60):
        mid = (lo + hi) / 2
        if g(r, mid) - 1 > 0:
            hi = mid
        else:
            lo = mid
    th = None
    try:
        cand = mp.findroot(lambda u: g(r, u) - 1, (lo, hi), solver="anderson")
        eps = mp.mpf(10) ** -45 * cand
        if lo <= cand <= hi and g(r, cand - eps) - 1 < 0 and g(r, cand + eps) - 1 > 0:
            th = cand
    except (ValueError, ZeroDivisionError):
        th = None
    if th is None:
        for _ in range(200):
            mid = (lo + hi) / 2
            if g(r, mid) - 1 > 0:
                hi = mid
            else:
                lo = mid
            if hi - lo < mp.mpf(10) ** -48 * hi:
                break
        th = (lo + hi) / 2
    _th[key] = th
    return th


def member(W, de, om):
    """Exact test: (inside?, margin, mode, alpha, theta1); margin > 0 strictly inside."""
    absW = abs(W)
    if absW == 0:
        return True, mp.mpf(0), "zero", None, None
    alpha = mp.arg(W)
    if alpha < 0:
        alpha += 2 * PI
    r = de / om
    if r == 0:
        return absW <= 1, 1 - absW, "disk", alpha, None
    if alpha <= PI:  # theta1 > pi, so the ray at alpha meets the boundary on the spiral arc
        bound = mp.exp(-r * alpha)
        return absW <= bound, bound - absW, "radial", alpha, None
    th = theta1(r)
    if alpha <= th:
        bound = mp.exp(-r * alpha)
        return absW <= bound, bound - absW, "radial", alpha, th
    P1 = mp.exp(mp.mpc(-r, 1) * th)
    d1 = P1 - 1
    # signed area cross(P1 - 1, W - 1) has the sign of cross(P1 - 1, 0 - 1) on 0's side; distance normalized by |P1-1|
    cr_W = mp.im(mp.conj(d1) * (W - 1))
    cr_0 = mp.im(mp.conj(d1) * (-1))
    marg = cr_W * mp.sign(cr_0) / abs(d1)
    return marg >= 0, marg, "chord", alpha, th


PSI = np.linspace(0.0, 2 * np.pi, 2880, endpoint=False)


def support_check(W, de, om):
    """max over the psi grid of Re(e^{-i psi} W) - sigma(psi) (float64); <= 0 is consistent with membership."""
    w = complex(W)
    r = float(de / om)
    gam = np.arctan(r)
    proj = np.real(np.exp(-1j * PSI) * w)
    sig = np.maximum(0.0, np.maximum(np.cos(PSI), np.cos(gam) * np.exp(-r * np.mod(PSI - gam, 2 * np.pi))))
    return float(np.max(proj - sig))


def box_points(b):
    mids = [(lo + hi) / 2 for lo, hi in b]
    prim = [tuple(mids)]
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                prim.append((b[0][i], b[1][j], b[2][k]))
    extra = []
    for x in (b[0][0], mids[0], b[0][1]):
        for y in (b[1][0], mids[1], b[1][1]):
            for z in (b[2][0], mids[2], b[2][1]):
                if (x, y, z) not in prim:
                    extra.append((x, y, z))
    for cnr in prim[1:]:
        extra.append(tuple(cv + (mv - cv) / 64 for cv, mv in zip(cnr, mids)))
    return prim, extra


def skip_rule_ok(chart, b):
    if chart == "G":
        (sl, sh), (dl, dh), (wl, wh) = b
        return wh <= 40 and wl >= Fr(1, 5) and dh <= 3 * wl
    if chart == "LD2":
        (cl, ch), (tl, th_), (bl, bh) = b
        return cl * tl > Fr(1, 16) or mpq((1 - ch) * tl) > mp.cos(mpq(bl)) / 65
    return False


def assigned(chart, s, de, om):
    """Point lies in the chart's assigned (delta, omega, s) set (charts-spec-v1.md table)."""
    if chart == "SWC":
        return de <= mp.mpf(3) / 10 and om <= mp.mpf(1) / 5
    if chart == "SWB":
        return mp.mpf(3) / 10 <= de <= 64 and om <= mp.mpf(1) / 5
    if chart == "G":
        inP = (mp.mpf(1) / 5 <= om <= 40) and de <= 3 * om
        return de <= 64 and mp.mpf(1) / 5 <= om <= 640 and not inP
    if chart == "LW":
        return de <= 64 and om >= 640
    if chart == "LD1":
        return de >= 64 and s >= mp.mpf(1) / 16
    return de >= 64 and s <= mp.mpf(1) / 16  # LD2


with open(SAMPLE, "rb") as fh:
    raw = fh.read()
sample_sha = hashlib.sha256(raw).hexdigest()
lines = [ln.split() for ln in raw.decode().splitlines() if ln.strip()]

counts = {"boxes": len(lines), "cert_boxes": 0, "skip_boxes": 0, "other_boxes": 0, "points_primary": 0,
          "points_extra": 0, "nonphysical_skipped": {}, "tested_primary": 0, "tested_extra": 0,
          "outside_assigned_set_tested_anyway": 0, "mode_counts": {}, "outcomes": {}}
violations = []
other = []
skip_rule_fail = []
support_disagree = []
support_amb = 0
minm = {"primary": None, "extra": None}
argm = {"primary": None, "extra": None}
per_box = []

for bi, parts in enumerate(lines):
    out = parts[0]
    counts["outcomes"][out] = counts["outcomes"].get(out, 0) + 1
    q = [Fr(x) for x in parts[1:7]]
    box = [(q[0], q[1]), (q[2], q[3]), (q[4], q[5])]
    if out.startswith("SKIP"):
        counts["skip_boxes"] += 1
        if not skip_rule_ok(CHART, box):
            skip_rule_fail.append({"box": bi, "line": " ".join(parts)})
        continue
    if not out.startswith("CERT"):
        counts["other_boxes"] += 1
        other.append({"box": bi, "line": " ".join(parts)})
        continue
    counts["cert_boxes"] += 1
    prim, extra = box_points(box)
    bmin = None
    for kind, pts in (("primary", prim), ("extra", extra)):
        for v in pts:
            counts["points_" + kind] += 1
            phys, why = to_physical(CHART, v)
            if phys is None:
                counts["nonphysical_skipped"][why] = counts["nonphysical_skipped"].get(why, 0) + 1
                continue
            s, de, om = phys
            counts["tested_" + kind] += 1
            if not assigned(CHART, s, de, om):
                counts["outside_assigned_set_tested_anyway"] += 1
            W = W_of(s, de, om)
            ins, marg, mode, alpha, th = member(W, de, om)
            counts["mode_counts"][mode] = counts["mode_counts"].get(mode, 0) + 1
            where = {"box": bi, "kind": kind, "chart_point": [str(x) for x in v],
                     "s_delta_omega": [mp.nstr(s, 20), mp.nstr(de, 20), mp.nstr(om, 20)]}
            if minm[kind] is None or marg < minm[kind]:
                minm[kind] = marg
                argm[kind] = dict(where, mode=mode, margin=mp.nstr(marg, 15))
            if bmin is None or marg < bmin:
                bmin = marg
            if (not ins) or marg <= TINY:
                violations.append(dict(where, outcome=out, mode=mode, margin=mp.nstr(marg, 25),
                                       W=mp.nstr(W, 25), alpha=None if alpha is None else mp.nstr(alpha, 20),
                                       theta1=None if th is None else mp.nstr(th, 20),
                                       ambiguous=bool(abs(marg) <= TINY), line=" ".join(parts)))
            sc = support_check(W, de, om)
            if abs(sc) < 1e-12 or abs(float(marg)) < 1e-12:
                support_amb += 1
            elif (sc > 0) == bool(ins):
                support_disagree.append(dict(where, exact_inside=bool(ins), support_max=sc, margin=mp.nstr(marg, 15)))
    per_box.append("%d %s %s" % (bi, out, "NA" if bmin is None else mp.nstr(bmin, 12)))

# ---------------- Q_T is the Laplace transform of q(t) = (t - 1)^2 - 11/61: quadrature check at complex y
mp.mp.dps = 30
qchk = []
for yv in [mp.mpc("0.7", "-0.3"), mp.mpc("2.5", "4"), mp.mpc("1", "0")]:
    lap = mp.quad(lambda t: mp.exp(-yv * t) * ((t - 1) ** 2 - mp.mpf(11) / 61), [0, 5, 20, 60, mp.inf])
    qchk.append({"y": mp.nstr(yv, 5), "abs_diff": mp.nstr(abs(lap - Q(yv)), 5),
                 "ok": bool(abs(lap - Q(yv)) < mp.mpf(10) ** -20)})
mp.mp.dps = 50

res = {"script": "replay_dual_v1.py", "label": "EXPLORATORY point replay (mpmath 50 digits); smoke test, not a certificate",
       "chart": CHART, "sample_path": SAMPLE, "sample_sha256": sample_sha, "counts": counts,
       "min_margin_primary": None if minm["primary"] is None else mp.nstr(minm["primary"], 20),
       "argmin_primary": argm["primary"],
       "min_margin_extra": None if minm["extra"] is None else mp.nstr(minm["extra"], 20), "argmin_extra": argm["extra"],
       "violations_count": len(violations), "violations_first100": violations[:100],
       "non_cert_non_skip_boxes": other[:100], "skip_rule_failures": skip_rule_fail[:100],
       "support_cross_check": {"disagreements": len(support_disagree), "first50": support_disagree[:50],
                               "ambiguous_|value|<1e-12": support_amb},
       "theta1_values_computed": len(_th), "QT_laplace_check": qchk,
       "elapsed_s": round(time.time() - T0, 2)}
ok = (not violations and not other and not skip_rule_fail and not support_disagree and all(x["ok"] for x in qchk))
res["verdict"] = "NO VIOLATION at any sampled physical point" if ok else "ISSUES FOUND (see fields)"
with lane_guard.xopen(os.path.join(RUN, "replay_dual_%s.json" % CHART)) as fh:
    json.dump(res, fh, indent=1)
with lane_guard.xopen(os.path.join(RUN, "per_box_min_margin_%s.txt" % CHART)) as fh:
    fh.write("# box outcome min_margin_over_tested_points\n" + "\n".join(per_box) + "\n")
print(json.dumps({"chart": CHART, "counts": counts, "violations": len(violations), "other": len(other),
                  "skip_rule_failures": len(skip_rule_fail), "support_disagreements": len(support_disagree),
                  "min_margin_primary": res["min_margin_primary"], "verdict": res["verdict"],
                  "elapsed_s": res["elapsed_s"]}))
sys.exit(0 if ok else 1)

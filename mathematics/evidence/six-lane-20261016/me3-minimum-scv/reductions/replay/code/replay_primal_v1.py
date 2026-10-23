"""INDEPENDENT point-evaluation replay of the primal chart-P certificate leaves (smoke test, NOT a certificate).

Written by MathPhaseType3.ME3Reductions from the definitions (reductions-v1.md Lemma 6.4-6.6); imports nothing from
the lane's code/ directory (lane_guard here is the lane's no-deletion guard, copied unchanged).

Input: SAMPLE file with lines "OUTCOME rl rh wl wh pl ph" (exact rationals; r = delta/omega, w = omega, p = phi).
Evaluation (mpmath, mp.dps = 50):
  a_k = 1 - Re[c zeta^{k+1}],  c = (1 - i r) e^{(r - i) phi},  zeta = 1/(1 + r w - i w)   (L6.6; r = 0 is D1),
  S = m0 m2/m1^2 - 1 = 2 a0 a2 / a1^2 - 1,
  dS/dr at fixed (w, phi): analytic, with dc/dr = e^{(r-i)phi}(phi(1 - i r) - i), dzeta/dr = -w zeta^2;
  cross-checked by mpmath central differences (mp.diff).
Feasibility (L6.4): r = 0: every phi feasible (D1: h = 1 - cos(w(t - tau)) >= 0); r > 0: phi <= theta1(r), theta1 the root
  in (pi, 2pi) of g_r(u) = e^{ru}(cos u - r sin u) = 1 (bracketed root finding, verified by sign change), cross-checked
  by the sign of h_tau(0) = 1 - g_r(phi) when phi in (pi, 2pi).
Points per box: PRIMARY = midpoint + 8 corners (as specified); EXTRA = the other 18 points of the 3x3x3 grid and the
  8 corners moved 1/64 of the way to the midpoint.  All points are exact rationals.
Checks: SGE: S > 11/50 at every feasible point; DPOS: dS/dr > 0 at every point; INFEAS: phi > theta1(r) (r > 0) at
  every point.  Also reported (information about the certificate's whole-box claims): S <= T or a1 <= 0 at infeasible
  points of SGE boxes; a_k <= 0 at points of DPOS boxes.
Moment cross-check: direct mpmath quadrature of int t^k e^{-t} h_tau(t) dt at a subset of points.
Usage: replay_primal_v1.py RUN SAMPLE_PATH
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

RUN, SAMPLE = sys.argv[1], sys.argv[2]
T0 = time.time()
mp.mp.dps = 50
T = mp.mpf(11) / 50
TINY = mp.mpf(10) ** -40
PI = mp.pi


def mpq(q):
    return mp.mpf(q.numerator) / q.denominator


def moments(r, w, p):
    E = mp.exp(mp.mpc(r, -1) * p)
    c = mp.mpc(1, -r) * E
    zeta = 1 / mp.mpc(1 + r * w, -w)
    a = [1 - mp.re(c * zeta ** (k + 1)) for k in range(3)]
    dc = E * (p * mp.mpc(1, -r) - mp.mpc(0, 1))
    da = [-mp.re(dc * zeta ** (k + 1) - (k + 1) * w * c * zeta ** (k + 2)) for k in range(3)]
    return a, da


def S_of(r, w, p):
    a, _ = moments(r, w, p)
    return 2 * a[0] * a[2] / a[1] ** 2 - 1


def S_and_dS(r, w, p):
    a, da = moments(r, w, p)
    S = 2 * a[0] * a[2] / a[1] ** 2 - 1
    dS = 2 * (da[0] * a[2] + a[0] * da[2]) / a[1] ** 2 - 4 * a[0] * a[2] * da[1] / a[1] ** 3
    return S, dS, a


def g(r, u):
    return mp.exp(r * u) * (mp.cos(u) - r * mp.sin(u))


_th = {}


def theta1(rq):
    """theta1(r) for exact rational r > 0; bracketed in (pi, 2pi); verified by a sign change of g - 1."""
    if rq in _th:
        return _th[rq]
    r = mpq(rq)
    lo, hi = PI, 2 * PI
    assert g(r, lo) - 1 < 0 and g(r, hi) - 1 > 0
    for _ in range(25):  # bisection to a safe bracket, then a bracketed secant solve
        mid = (lo + hi) / 2
        if g(r, mid) - 1 > 0:
            hi = mid
        else:
            lo = mid
    th = mp.findroot(lambda u: g(r, u) - 1, (lo, hi), solver="anderson")
    eps = mp.mpf(10) ** -45
    assert lo <= th <= hi and g(r, th - eps) - 1 < 0 and g(r, th + eps) - 1 > 0, "theta1 sign check failed"
    _th[rq] = th
    return th


def feasible(rq, p):
    """(feasible?, phi - theta1 or None, consistency flag with the h_tau(0) sign test)."""
    if rq == 0:
        return True, None, True
    th = theta1(rq)
    marg = p - th
    feas = marg <= 0
    cons = True
    if PI < p < 2 * PI:
        h0 = 1 - g(mpq(rq), p)
        cons = (h0 >= 0) == feas or abs(marg) < TINY
    return feas, marg, cons


def box_points(b):
    (rl, rh), (wl, wh), (pl, ph) = b
    mids = [(lo + hi) / 2 for lo, hi in b]
    prim = [tuple(mids)]
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                prim.append((b[0][i], b[1][j], b[2][k]))
    grid3 = []
    for x in (rl, mids[0], rh):
        for y in (wl, mids[1], wh):
            for z in (pl, mids[2], ph):
                if (x, y, z) not in prim:
                    grid3.append((x, y, z))
    inset = []
    for cnr in prim[1:]:
        inset.append(tuple(cv + (mv - cv) / 64 for cv, mv in zip(cnr, mids)))
    return prim, grid3 + inset


with open(SAMPLE, "rb") as fh:
    raw = fh.read()
sample_sha = hashlib.sha256(raw).hexdigest()
lines = [ln.split() for ln in raw.decode().splitlines() if ln.strip()]

stats = {o: {"boxes": 0, "points_primary": 0, "points_extra": 0, "feasible_points": 0, "min_margin_primary": None,
             "min_margin_extra": None, "argmin_primary": None, "argmin_extra": None} for o in ("SGE", "DPOS", "INFEAS")}
violations = []
cert_claim_issues = []
fd_disagree = []
feas_inconsistent = []
per_box = []
unknown = []


def upd(st, key, val, where):
    if val is None:
        return
    if st[key] is None or val < st[key]:
        st[key] = val
        st[key.replace("min_margin", "argmin")] = where


for bi, parts in enumerate(lines):
    out = parts[0]
    if out not in stats:
        unknown.append({"box": bi, "line": " ".join(parts)})
        continue
    q = [Fr(x) for x in parts[1:7]]
    box = [(q[0], q[1]), (q[2], q[3]), (q[4], q[5])]
    prim, extra = box_points(box)
    st = stats[out]
    st["boxes"] += 1
    bmin = {"primary": None, "extra": None}
    for kind, pts in (("primary", prim), ("extra", extra)):
        for (rq, wq, pq) in pts:
            st["points_" + kind] += 1
            r, w, p = mpq(rq), mpq(wq), mpq(pq)
            feas, fmarg, cons = feasible(rq, p)
            if not cons:
                feas_inconsistent.append({"box": bi, "point": [str(rq), str(wq), str(pq)]})
            where = {"box": bi, "kind": kind, "point": [str(rq), str(wq), str(pq)]}
            if out == "SGE":
                a = moments(r, w, p)[0]
                S = 2 * a[0] * a[2] / a[1] ** 2 - 1
                if feas:
                    st["feasible_points"] += 1
                    m = S - T
                    upd(st, "min_margin_" + kind, m, where)
                    if bmin[kind] is None or m < bmin[kind]:
                        bmin[kind] = m
                    if m <= TINY:
                        violations.append(dict(where, outcome=out, test="S > 11/50", S=mp.nstr(S, 30),
                                               ambiguous=bool(abs(m) <= TINY), line=" ".join(parts)))
                elif a[1] <= 0 or S - T <= 0:
                    cert_claim_issues.append(dict(where, outcome=out, note="infeasible point with a1 <= 0 or S <= T",
                                                  a1=mp.nstr(a[1], 20), S=mp.nstr(S, 20)))
            elif out == "DPOS":
                S, dS, a = S_and_dS(r, w, p)
                fd = mp.diff(lambda rr: S_of(rr, w, p), r)
                if abs(fd - dS) > mp.mpf(10) ** -30 * (1 + abs(dS)):
                    fd_disagree.append(dict(where, analytic=mp.nstr(dS, 25), central=mp.nstr(fd, 25)))
                if feas:
                    st["feasible_points"] += 1
                upd(st, "min_margin_" + kind, dS, where)
                if bmin[kind] is None or dS < bmin[kind]:
                    bmin[kind] = dS
                if dS <= TINY:
                    violations.append(dict(where, outcome=out, test="dS/dr > 0", dSdr=mp.nstr(dS, 30),
                                           S=mp.nstr(S, 20), feasible=bool(feas), ambiguous=bool(abs(dS) <= TINY),
                                           line=" ".join(parts)))
                if min(a) <= 0:
                    cert_claim_issues.append(dict(where, outcome=out, note="a_k <= 0 at a DPOS point",
                                                  a=[mp.nstr(x, 15) for x in a]))
            else:  # INFEAS
                if rq == 0:
                    m = None
                    violations.append(dict(where, outcome=out, test="phi > theta1(r)", note="r = 0 (D1): feasible",
                                           line=" ".join(parts)))
                else:
                    m = fmarg
                    upd(st, "min_margin_" + kind, m, where)
                    if bmin[kind] is None or m < bmin[kind]:
                        bmin[kind] = m
                    if m <= TINY:
                        violations.append(dict(where, outcome=out, test="phi > theta1(r)",
                                               phi_minus_theta1=mp.nstr(m, 30), ambiguous=bool(abs(m) <= TINY),
                                               line=" ".join(parts)))
                if feas:
                    st["feasible_points"] += 1
    per_box.append("%d %s %s %s" % (bi, out, "NA" if bmin["primary"] is None else mp.nstr(bmin["primary"], 12),
                                     "NA" if bmin["extra"] is None else mp.nstr(bmin["extra"], 12)))

# ---------------- direct quadrature cross-check of the closed-form moments (independent of L6.6's algebra)
mp.mp.dps = 30
quad_rows = []
picked = {}
for bi, parts in enumerate(lines):
    o = parts[0]
    if o in stats and picked.get(o, 0) < 8:
        picked[o] = picked.get(o, 0) + 1
        q = [Fr(x) for x in parts[1:7]]
        rq, wq, pq = (q[0] + q[1]) / 2, (q[2] + q[3]) / 2, (q[4] + q[5]) / 2
        r, w, p = mpq(rq), mpq(wq), mpq(pq)
        de, tau = r * w, p / w

        def h(t):
            s_ = t - tau
            return 1 - mp.exp(-de * s_) * (mp.cos(w * s_) + r * mp.sin(w * s_))

        n_osc = int(min(240, max(4, mp.ceil(60 * w / PI))))
        cuts = [mp.mpf(0)] + [mp.mpf(60) * j / n_osc for j in range(1, n_osc + 1)] + [mp.inf]
        mq = [mp.quad(lambda t: t ** k * mp.exp(-t) * h(t), cuts) for k in range(3)]
        a, _ = moments(r, w, p)
        mc = [a[0], a[1], 2 * a[2]]
        err = max(abs(x - y) for x, y in zip(mq, mc))
        quad_rows.append({"box": bi, "outcome": o, "point": [str(rq), str(wq), str(pq)],
                          "max_abs_diff": mp.nstr(err, 5), "ok": bool(err < mp.mpf(10) ** -20)})
mp.mp.dps = 50


def fmt(st):
    d = dict(st)
    for k in ("min_margin_primary", "min_margin_extra"):
        d[k] = None if d[k] is None else mp.nstr(d[k], 20)
    return d


real_viol = [v for v in violations if not v.get("ambiguous")]
res = {
    "script": "replay_primal_v1.py", "label": "EXPLORATORY point replay (mpmath 50 digits); smoke test, not a certificate",
    "sample_path": SAMPLE, "sample_sha256": sample_sha, "boxes_read": len(lines),
    "outcome_counts": {o: stats[o]["boxes"] for o in stats}, "unknown_outcome_lines": unknown,
    "margins": "SGE: min(S - 11/50) over feasible points; DPOS: min dS/dr; INFEAS: min(phi - theta1(r))",
    "stats": {o: fmt(stats[o]) for o in stats},
    "violations_count": len(violations), "violations_nonambiguous_count": len(real_viol),
    "violations_first100": violations[:100],
    "certificate_whole_box_claim_issues_count": len(cert_claim_issues),
    "certificate_whole_box_claim_issues_first50": cert_claim_issues[:50],
    "dSdr_analytic_vs_central_difference_disagreements": fd_disagree[:50],
    "feasibility_theta1_vs_h0_inconsistencies": feas_inconsistent[:50],
    "theta1_values_computed": len(_th),
    "quadrature_cross_check": quad_rows, "quadrature_all_ok": all(rw["ok"] for rw in quad_rows),
    "elapsed_s": round(time.time() - T0, 2)}
res["verdict"] = ("NO VIOLATION at any sampled point" if not violations and not unknown else
                  "VIOLATIONS FOUND (see violations_first100)")
with lane_guard.xopen(os.path.join(RUN, "replay_primal.json")) as fh:
    json.dump(res, fh, indent=1)
with lane_guard.xopen(os.path.join(RUN, "per_box_min_margin.txt")) as fh:
    fh.write("# box outcome min_margin_primary min_margin_extra\n" + "\n".join(per_box) + "\n")
print(json.dumps({k: res[k] for k in ("boxes_read", "outcome_counts", "violations_count", "violations_nonambiguous_count",
                                       "certificate_whole_box_claim_issues_count", "quadrature_all_ok", "verdict",
                                       "elapsed_s")}))
print(json.dumps({o: fmt(stats[o]) for o in stats}))
sys.exit(0 if (not violations and not unknown and res["quadrature_all_ok"] and not fd_disagree
               and not feas_inconsistent) else 1)

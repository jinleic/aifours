"""EXPLORATORY (mpmath 30 digits on a grid; not a certificate). Landscape of the dual sufficient test.

For (delta, w) on log grids and s in a fine grid of (0,1): W = Nt(s,1+xi)/(Nt(s,1)(1+xi)^3), xi = delta - i w,
Arg_+ in [0, 2pi), Phi = w log|W| + delta Arg_+. Reports, outside the primal valley V = {w in [0.45,1.9], delta <= 0.3 w}:
  * points with max_s Phi > 0 (sufficient test fails) and whether Im W < 0 there;
  * normalized margins: max_s Phi/(w |xi|^2) near the corner, max_s Phi/w near the B-edge;
  * the minimum over s of Re g'(xi) along the segment to probe the corner chart's g1sign condition.
argv[1] = run directory; writes explore_dual.json (exclusive create).
"""
import sys
import json
import math
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import mpmath as mp  # noqa: E402

RUN = sys.argv[1]
mp.mp.dps = 30
kap = mp.mpf(50) / 61


def Nt(s, z):
    return kap * s * s * z * z - 2 * s * (1 - s) * z + 2 * (1 - s) ** 2


def Wf(s, xi):
    z = 1 + xi
    return Nt(s, z) / (Nt(s, 1) * z ** 3)


def argp(W):
    a = mp.arg(W)
    return a + 2 * mp.pi if a < 0 else a


ss = [mp.mpf(k) / 400 for k in range(1, 400)]
ds = [0.0] + [10 ** (-3 + 6 * k / 60) for k in range(61)]
ws = [10 ** (-3 + 6 * k / 60) for k in range(61)]
bad = []
neg_im = []
corner = []
bedge = []
for d in ds:
    for w in ws:
        inV = (0.45 <= w <= 1.9) and (d <= 0.3 * w)
        xi = mp.mpf(d) - 1j * mp.mpf(w)
        worst = -mp.inf
        worst_s = None
        anyneg = False
        for s in ss:
            W = Wf(s, xi)
            if W.imag < 0:
                anyneg = True
            Phi = w * mp.log(abs(W)) + d * argp(W)
            if Phi > worst:
                worst, worst_s = Phi, s
        rec = {"delta": d, "w": w, "max_Phi": float(worst), "s_at": float(worst_s), "inV": inV, "any_ImW_neg": anyneg}
        if worst > 0 and not inV:
            bad.append(rec)
        if anyneg and not inV:
            neg_im.append(rec)
        if d <= 0.3 and w <= 0.3:
            corner.append({"delta": d, "w": w, "max_Phi_over_w_xi2": float(worst / (w * (d * d + w * w)))})
        if w <= 0.3 and d >= 0.25:
            bedge.append({"delta": d, "w": w, "max_Phi_over_w": float(worst / w)})
out = {"bad_outside_V": bad[:200], "n_bad_outside_V": len(bad), "imW_negative_outside_V": neg_im[:100],
       "n_imW_negative_outside_V": len(neg_im),
       "corner_max": max(corner, key=lambda x: x["max_Phi_over_w_xi2"]) if corner else None,
       "bedge_max": max(bedge, key=lambda x: x["max_Phi_over_w"]) if bedge else None}
# Re g' scan in the corner rectangle
gp = []
for R in [0.05, 0.1, 0.15, 0.2, 0.3]:
    worst = -mp.inf
    for s in ss[::4]:
        for a in range(11):
            for b in range(11):
                xi = mp.mpf(R) * a / 10 - 1j * mp.mpf(R) * b / 10
                z = 1 + xi
                g1 = (2 * kap * s * s * z - 2 * s * (1 - s)) / Nt(s, z) - 3 / z
                worst = max(worst, g1.real)
    gp.append({"rect_side": R, "max_Re_g1": float(worst)})
out["corner_Re_g1_scan"] = gp
with lane_guard.xopen(RUN + "/explore_dual.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: out[k] for k in ("n_bad_outside_V", "n_imW_negative_outside_V", "corner_max", "bedge_max",
                                      "corner_Re_g1_scan")}, indent=1))
print("bad sample", bad[:15])
print("negIm sample", neg_im[:10])

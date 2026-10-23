"""Designed negative controls for the certificates (each must FAIL for the stated reason). Bounded, small regions.

M1 primal without DPOS: region r in [0, 1/20], w in [1, 107/100], phi in [3/10, 37/100] (around the D1 optimum
   (1.0359, 0.3370)); outcomes {INFEAS, SGE} only, max depth 10 -> must leave FAIL boxes (S < T there since v_cos < T).
M2 primal with the derivative sign flipped (-D > 0 required): same region -> must FAIL.
M3 dual GENERAL test (me3dual_v8.test_general) at T = 11/50 on delta in [0, 1/20], w in [1, 107/100], s in [0,1] (inside
   the primal valley, where S < T for some extreme rays) -> no box at max depth 10 may pass everywhere: the chart must FAIL.
M4 dual CORNER test with T' = 3/10 > Delta_3 on delta, w in [0, 1/20] (near the C-limit, where S -> Delta_3 < T') -> FAIL.
M5 INFEAS predicate on boxes that contain feasible points (phi_lo below theta1(r_lo)) -> must not classify INFEAS.
M6 positive control: the same small primal region WITH DPOS -> certified (no FAIL).
argv[1] = run directory; writes controls.json (exclusive create).
"""
import sys
import json
import time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402
import me3lib_v1 as L  # noqa: E402
from me3jet_v1 import EXP, RE, mvf  # noqa: E402
import me3dual_v8 as D8  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 128
I = acb(0, 1)
PI = arb.pi()


def ball(lo, hi):
    return arb(lo).union(arb(hi))


def primal_classify(box, T, use_dpos, flip):
    Tb = arb(T)
    (rl, rh), (wl, wh), (pl, ph) = box
    if arb(pl) > PI and rl > 0 and L.g_feas(arb(rl), arb(pl)) > 1:
        return "INFEAS"
    rb, wb, pb = ball(rl, rh), ball(wl, wh), ball(pl, ph)

    def F(R, Wv, Ph):
        c = (1 - I * R) * EXP((R - I) * Ph)
        zeta = 1 / (1 + R * Wv - I * Wv)
        shift = Ph + (R - I) / (1 + R * R)
        a, da = [], []
        zp = zeta
        for k in range(3):
            P = c * zp
            a.append(1 - RE(P))
            da.append(-RE(P * (shift - (k + 1) * Wv * zeta)))
            zp = zp * zeta
        G = 2 * a[0] * a[2] - (1 + Tb) * a[1] * a[1]
        Dd = da[0] * a[1] * a[2] + a[0] * a[1] * da[2] - 2 * a[0] * da[1] * a[2]
        return (G, -Dd if flip else Dd)
    a0, a1, a2, G, Dn = L.primal_G_D(rb, wb, pb, Tb)
    mids = [arb((rl + rh) / 2), arb((wl + wh) / 2), arb((pl + ph) / 2)]
    hb = [ball(-(rh - rl) / 2, (rh - rl) / 2), ball(-(wh - wl) / 2, (wh - wl) / 2), ball(-(ph - pl) / 2, (ph - pl) / 2)]
    Gm, Dm = mvf(F, mids, [rb, wb, pb], hb)
    if a1 > 0 and (G > 0 or Gm > 0):
        return "SGE"
    if use_dpos and a0 > 0 and a1 > 0 and a2 > 0 and Dm > 0:
        return "DPOS"
    return None


def bb3(box0, classify, maxdepth):
    stack = [(box0, 0)]
    counts = {}
    while stack:
        box, d = stack.pop()
        out = classify(box)
        if out is None:
            if d >= maxdepth:
                counts["FAIL"] = counts.get("FAIL", 0) + 1
                continue
            widths = [box[i][1] - box[i][0] for i in range(3)]
            i = max(range(3), key=lambda j: widths[j])
            lo, hi = box[i]
            mid = (lo + hi) / 2
            b1, b2 = list(box), list(box)
            b1[i], b2[i] = (lo, mid), (mid, hi)
            stack.append((tuple(b2), d + 1))
            stack.append((tuple(b1), d + 1))
            continue
        counts[out] = counts.get(out, 0) + 1
    return counts


t0 = time.time()
out = {}
T = fmpq(11, 50)
reg = ((fmpq(0), fmpq(1, 20)), (fmpq(1), fmpq(107, 100)), (fmpq(3, 10), fmpq(37, 100)))
out["M1_no_DPOS"] = bb3(reg, lambda b: primal_classify(b, T, False, False), 10)
out["M2_flipped_derivative"] = bb3(reg, lambda b: primal_classify(b, T, True, True), 10)
out["M6_positive_control_with_DPOS"] = bb3(reg, lambda b: primal_classify(b, T, True, False), 16)
kapT = arb(1 / (1 + T))
regG = ((fmpq(0), fmpq(1)), (fmpq(0), fmpq(1, 20)), (fmpq(1), fmpq(107, 100)))
out["M3_dual_general_in_valley"] = bb3(regG, lambda b: ("CERT" if D8.test_general(b[0][0], b[0][1], b[1][0], b[1][1],
                                                                                   b[2][0], b[2][1], kapT, None)[0]
                                                         else None), 10)
kap3 = arb(1 / (1 + fmpq(3, 10)))
regC = ((fmpq(0), fmpq(1)), (fmpq(0), fmpq(1, 20)), (fmpq(0), fmpq(1, 20)))
out["M4_corner_with_T_0.30"] = bb3(regC, lambda b: ("CERT" if D8.test_corner(b[0][0], b[0][1], b[1][0], b[1][1],
                                                                              b[2][0], b[2][1], kap3, 20)[0] else None), 9)
m5 = []
for (rl, pl) in [(fmpq(3, 10), fmpq(46, 10)), (fmpq(1), fmpq(39, 10)), (fmpq(1, 100), fmpq(59, 10))]:
    box = ((rl, rl + fmpq(1, 100)), (fmpq(1), fmpq(2)), (pl, pl + fmpq(1, 100)))
    m5.append({"r_lo": str(rl), "phi_lo": str(pl),
               "classified_INFEAS": primal_classify(box, T, True, False) == "INFEAS",
               "g_r_lo(phi_lo)": str(L.g_feas(arb(rl), arb(pl)))})
out["M5_INFEAS_predicate_on_feasible_boxes"] = m5
out["expectations"] = {"M1": "FAIL > 0", "M2": "FAIL > 0", "M3": "FAIL > 0", "M4": "FAIL > 0",
                       "M5": "classified_INFEAS false for all (each box contains feasible points: phi_lo < theta1(r_lo))",
                       "M6": "no FAIL"}
out["verdicts"] = {
    "M1": out["M1_no_DPOS"].get("FAIL", 0) > 0,
    "M2": out["M2_flipped_derivative"].get("FAIL", 0) > 0,
    "M3": out["M3_dual_general_in_valley"].get("FAIL", 0) > 0,
    "M4": out["M4_corner_with_T_0.30"].get("FAIL", 0) > 0,
    "M5": all(not x["classified_INFEAS"] for x in m5),
    "M6": out["M6_positive_control_with_DPOS"].get("FAIL", 0) == 0}
out["elapsed_seconds"] = round(time.time() - t0, 2)
with lane_guard.xopen(RUN + "/controls.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))

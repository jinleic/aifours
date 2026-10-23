"""Corner-chart controls for the exact-coefficient library me3dual_v9.py (controls_v1.py kept; it used v8).

M4v9: corner test with T' = 3/10 > Delta_3 on s in [0,1], delta, w in [0, 1/20] (near the C-limit where S -> Delta_3 <
      T'): must leave FAIL boxes.
M7v9: positive control, corner test at T = 11/50 on the first SWC cell region s in [0, 1/16], delta, w in [0, 1/10]:
      must certify (no FAIL) within depth 16.
M8:   coefficient exactness. At s = 0 (p = 0) and real xi = delta = 1/2 (w = 0), U_m = m delta^(m-1) and
      c_j = 3(-1)^j/j exactly, so Ig_N = -sum_{j<=N} c_j U_j = 3 (1 - delta^N)/(1 + delta) exactly (N = 20 even).
      The v9 ball must CONTAIN this rational; the v8 ball (float-rounded c_j) must EXCLUDE it (demonstrates the
      repaired defect).
argv[1] = run dir; writes controls.json (exclusive create).
"""
import sys
import json
import time
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402
import me3dual_v9 as D9  # noqa: E402
import me3dual_v8 as D8  # noqa: E402

RUN = sys.argv[1]
flint.ctx.prec = 128


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
kap3 = arb(1 / (1 + fmpq(3, 10)))
kapT = arb(1 / (1 + fmpq(11, 50)))
regC = ((fmpq(0), fmpq(1)), (fmpq(0), fmpq(1, 20)), (fmpq(0), fmpq(1, 20)))
out["M4v9_corner_T0.30"] = bb3(regC, lambda b: ("CERT" if D9.test_corner(b[0][0], b[0][1], b[1][0], b[1][1], b[2][0],
                                                                          b[2][1], kap3, 20)[0] else None), 9)
regP = ((fmpq(0), fmpq(1, 16)), (fmpq(0), fmpq(1, 10)), (fmpq(0), fmpq(1, 10)))
out["M7v9_corner_positive_T"] = bb3(regP, lambda b: ("CERT" if D9.test_corner(b[0][0], b[0][1], b[1][0], b[1][1],
                                                                               b[2][0], b[2][1], kapT, 20)[0] else None), 16)
dl = fmpq(1, 2)
exact = 3 * (1 - dl ** 20) / (1 + dl)
_, ig9 = D9.corner_series_v9(acb(0), acb(arb(dl)), acb(0), kapT, 20)
_, ig8 = D8.corner_series_v8(acb(0), acb(arb(dl)), acb(0), kapT, 20)
out["M8_coefficient_exactness"] = {"exact_IgN": str(exact), "v9_ball": ig9.real.str(radius=True),
                                   "v9_contains_exact": bool(ig9.real.contains(arb(exact))),
                                   "v8_ball": ig8.real.str(radius=True),
                                   "v8_contains_exact": bool(ig8.real.contains(arb(exact)))}
out["verdicts"] = {"M4v9": out["M4v9_corner_T0.30"].get("FAIL", 0) > 0,
                   "M7v9": out["M7v9_corner_positive_T"].get("FAIL", 0) == 0,
                   "M8": out["M8_coefficient_exactness"]["v9_contains_exact"]
                   and not out["M8_coefficient_exactness"]["v8_contains_exact"]}
out["elapsed_seconds"] = round(time.time() - t0, 2)
with lane_guard.xopen(RUN + "/controls.json") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))

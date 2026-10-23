"""ME3 parent desk (ME3ParentPrimal): OPTIONAL independent decimal lower certificate for v_cos (D1 family).

Not needed for the main theorem (v_cos is defined exactly as the D1 minimum); it certifies a decimal lower bound,
e.g. the contract band lower edge, by branch-and-bound on the displayed D1 moment formulas.
Usage: d1_lower_v1.py RUN_DIR L MODE MAX_BOXES      (L exact decimal or p/q; MODE certify|reject)
Objective (definition): f = e^{-t}(1 - cos(w t - phi)), m_k = k!(1 - Re[e^{-i phi}(1 - i w)^{-(k+1)}]),
  SCV = m0 m2/m1^2 - 1; SCV > L  <=>  G_L := 2 a0 a2 - (1 + L) a1^2 > 0 (a_k = m_k/k!, a1 > 0).
  Evaluated with p_core_v1.Evaluator at r = 0 exactly (c = e^{-i phi}, zeta = 1/(1 - i w)), naive then mean-value
  form with exact centres; the r-component of the gradient is multiplied by the exact half-width 0.
Domain: w in [1/4, 4], phi in [0, 31416/5000] (contains a full period [0, 2 pi]; SCV is 2 pi-periodic in phi).
Tails (written lemmas, exact constants re-checked here): w <= 1/4: SCV >= (16 Delta3 - 1)/17 with Delta3 > 2765/10000
  (Sturm certificate, red_checks_v1 R1b); w >= 4: SCV >= 2(1 - rb)(1 - rb^3)/(1 + rb^2)^2 - 1, rb = 2426/10000.
B&B: initial grid 15 x 64; a box is either certified (G_L > 0 on the box) or bisected across its longer side
  (ties: w) at the exact midpoint; if a centre has certified SCV < L the claim is REFUTED and the run stops.
  Coverage: every leaf is an exact dyadic sub-box of the grid and the exact areas of the certified leaves sum to
  the domain area. Writes RUN_DIR/RESULT.json and RUN_DIR/leaves.txt.gz ("cell path method"), exclusive create.
"""
import sys
import os
import json
import gzip
import time
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import p_core_v1 as C  # noqa: E402

run, Ls, mode, maxboxes = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
L = C.parse_q(Ls) if "/" in Ls else Fraction(Ls)
t0 = time.time()
ev = C.Evaluator(L, 128)
W = (Fraction(1, 4), Fraction(4))
PH = (Fraction(0), Fraction(31416, 5000))
NW, NP = 15, 64
d3lo = Fraction(2765, 10000)
tail_low = (16 * d3lo - 1) / 17
rb = Fraction(2426, 10000)
tail_high = 2 * (1 - rb) * (1 - rb ** 3) / (1 + rb ** 2) ** 2 - 1
res = {"script": "d1_lower_v1.py", "L": str(L), "mode": mode,
       "tails": {"w<=1/4 bound": str(tail_low), "w<=1/4 ok": tail_low > L, "rb^2>1/17": rb ** 2 > Fraction(1, 17),
                 "w>=4 bound": str(tail_high), "w>=4 ok": tail_high > L}}
zero = (Fraction(0), Fraction(0))
raw = open(os.path.join(run, "leaves.txt.gz"), "xb")
gz = gzip.GzipFile(fileobj=raw, mode="wb", mtime=0)
stats = {"naive": 0, "mvf": 0}
boxes = 0
maxdepth = 0
area = Fraction(0)
refuted = None
capped = False
min_centre = None
for i in range(NW):
    for j in range(NP):
        cell = ((W[0] + (W[1] - W[0]) * Fraction(i, NW), W[0] + (W[1] - W[0]) * Fraction(i + 1, NW)),
                (PH[0] + (PH[1] - PH[0]) * Fraction(j, NP), PH[0] + (PH[1] - PH[0]) * Fraction(j + 1, NP)))
        stack = [(cell, "")]
        while stack:
            (wv, pv), path = stack.pop()
            boxes += 1
            box = (zero, wv, pv)
            how = ev.check_SGE(box)
            if how:
                stats[how] += 1
                area += (wv[1] - wv[0]) * (pv[1] - pv[0])
                maxdepth = max(maxdepth, len(path))
                gz.write(f"{i * NP + j} {path if path else '-'} {how}\n".encode())
                continue
            m, _ = ev.mid_half(box)
            P0, P1, P2, _ = ev.base(*ev.point(m))
            a0, a1, a2 = 1 - P0.real, 1 - P1.real, 1 - P2.real
            Sm = 2 * a0 * a2 / (a1 * a1) - 1
            if min_centre is None or Sm.upper() < min_centre[0].upper():
                min_centre = (Sm, [str(m[1]), str(m[2])])
            if Sm < ev.onepT - 1:
                refuted = {"centre": [str(m[1]), str(m[2])], "SCV_ball": Sm.str(30, radius=True)}
                break
            if boxes >= maxboxes:
                capped = True
                break
            if (wv[1] - wv[0]) >= (pv[1] - pv[0]):
                mid = (wv[0] + wv[1]) / 2
                kids = [((wv[0], mid), pv), ((mid, wv[1]), pv)]
            else:
                mid = (pv[0] + pv[1]) / 2
                kids = [(wv, (pv[0], mid)), (wv, (mid, pv[1]))]
            stack.append((kids[1], path + "1"))
            stack.append((kids[0], path + "0"))
        if refuted or capped:
            break
    if refuted or capped:
        break
gz.close()
raw.close()
total_area = (W[1] - W[0]) * (PH[1] - PH[0])
res.update({"boxes_processed": boxes, "leaves": stats, "max_depth": maxdepth, "refuted": refuted, "capped": capped,
            "certified_area_equals_domain_area": area == total_area, "certified_area": str(area),
            "domain_area": str(total_area),
            "smallest_centre_value_EXPLORATORY": None if min_centre is None else
            [min_centre[0].str(25, radius=True), min_centre[1]],
            "elapsed_seconds": round(time.time() - t0, 2)})
tails_ok = res["tails"]["w<=1/4 ok"] and res["tails"]["rb^2>1/17"] and res["tails"]["w>=4 ok"]
if mode == "certify":
    res["status"] = "CERTIFIED v_cos >= L" if (refuted is None and not capped and area == total_area and tails_ok) \
        else "NOT CERTIFIED"
    ok = res["status"].startswith("CERTIFIED")
else:
    res["status"] = "REJECTED as intended (refuted at a certified centre)" if refuted else "NOT REJECTED"
    ok = refuted is not None
with open(os.path.join(run, "RESULT.json"), "x") as fh:
    json.dump(res, fh, indent=1, default=str)
print("RESULT", res["status"], json.dumps({k: res[k] for k in ("boxes_processed", "leaves", "max_depth", "refuted",
                                                               "capped", "certified_area_equals_domain_area")}))
sys.exit(0 if ok else 1)

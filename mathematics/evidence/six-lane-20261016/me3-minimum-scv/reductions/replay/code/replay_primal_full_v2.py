"""v2 (2026-10-18): v1 stopped (exit 2) because it assumed the samples are leaves 0, 997, ...; the audit samples the
1-based leaf counter n with n % 997 == 0, i.e. 0-based leaves 996, 1993, ...  v2 tries offsets 996 and 0 and records
which one matches.  Nothing else changed.
EXTRA (beyond the 948-sample task): independent replay over ALL chart-P leaves of run c03 (smoke test, NOT a
certificate) plus an independent tiling audit.  Written by MathPhaseType3.ME3Reductions; imports nothing from L/code.

Geometry (from code/spec_primal_P_v1.json, read as a definition): region r in [0,3], w in [1/5,40], phi in [0,31416/5000];
initial grid 12 x 80 x 64 cells; split rule: bisect the axis maximizing width*weight (weights 1,1,1; ties -> lowest axis)
at the exact midpoint, child 0 = lower half.  Because the initial grid is uniform, the split axis at depth k is the same
for every leaf (computed here), so a leaf box is a_j + [m_j, m_j + 1] * width_j / 2^{k_j} with integer m_j, k_j.
Leaf records: "cell path outcome" (path "-" = empty).  The cell-index -> grid-index order is NOT in the spec; it is
determined here as the unique axis permutation for which the reconstructed boxes of leaves 0, 997, 1994, ... equal the
948 lines of runs/a01-coverP/sample_boxes.txt exactly (outcome and all six rationals); the run stops otherwise.
Tiling audit (per cell): the path set is prefix-free (adjacent pairs after sorting) and the Kraft sum
sum 2^{-len} equals 1 exactly, i.e. the leaves form a complete binary tree, which tiles the cell; all 61440 cells occur.
Evaluation (mpmath dps 50, own formulas as in replay_primal_v1.py):
  SGE: midpoint; if feasible, S > 11/50 (also report a1 <= 0 or S <= T at infeasible midpoints);
  DPOS: midpoint + 8 corners: dS/dr > 0 and a_k > 0;
  INFEAS: worst corner (r_lo, phi_lo): r_lo > 0 and (phi_lo >= 2 pi or (phi_lo > pi and g_{r_lo}(phi_lo) > 1)), which
    implies phi > theta1(r) on the whole box (theta1 decreasing, Lemma 6.5; g_r increasing on [pi, 2 pi]); and midpoint.
  Feasibility of a point: r = 0 or phi <= pi: feasible; phi >= 2 pi (r > 0): infeasible; else feasible iff g_r(phi) <= 1.
Usage: replay_primal_full_v2.py RUN LEAVES_GZ SAMPLE_PATH
"""
import os
import sys
import gzip
import json
import time
import hashlib
import itertools
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: E402,F401
import mpmath as mp  # noqa: E402

RUN, LEAVES, SAMPLE = sys.argv[1], sys.argv[2], sys.argv[3]
T0 = time.time()
mp.mp.dps = 50
T = mp.mpf(11) / 50
TINY = mp.mpf(10) ** -40
PI = mp.pi

LO = [Fr(0), Fr(1, 5), Fr(0)]
HI = [Fr(3), Fr(40), Fr(31416, 5000)]
NCELL = [12, 80, 64]
CW = [(HI[j] - LO[j]) / NCELL[j] for j in range(3)]
WEIGHT = [Fr(1), Fr(1), Fr(1)]
MAXD = 64
AXIS = []
k = [0, 0, 0]
for _ in range(MAXD):
    sc = [CW[j] / 2 ** k[j] * WEIGHT[j] for j in range(3)]
    j = max(range(3), key=lambda i: (sc[i], -i))
    AXIS.append(j)
    k[j] += 1


def leaf_geom(ci, path, order):
    idx = [0, 0, 0]
    rem = ci
    for ax in reversed(order):  # order = axes from most to least significant
        idx[ax] = rem % NCELL[ax]
        rem //= NCELL[ax]
    assert rem == 0
    m = [0, 0, 0]
    kk = [0, 0, 0]
    if path != "-":
        for depth, bit in enumerate(path):
            ax = AXIS[depth]
            m[ax] = 2 * m[ax] + (1 if bit == "1" else 0)
            kk[ax] += 1
    return idx, m, kk


def box_fr(geom):
    idx, m, kk = geom
    out = []
    for j in range(3):
        base = LO[j] + idx[j] * CW[j]
        wdt = CW[j] / 2 ** kk[j]
        out.append((base + m[j] * wdt, base + (m[j] + 1) * wdt))
    return out


def mpq(q):
    return mp.mpf(q.numerator) / q.denominator


def moments(r, w, p):
    E = mp.exp(mp.mpc(r, -1) * p)
    c = mp.mpc(1, -r) * E
    zeta = 1 / mp.mpc(1 + r * w, -w)
    a = [1 - mp.re(c * zeta ** (kq + 1)) for kq in range(3)]
    dc = E * (p * mp.mpc(1, -r) - mp.mpc(0, 1))
    da = [-mp.re(dc * zeta ** (kq + 1) - (kq + 1) * w * c * zeta ** (kq + 2)) for kq in range(3)]
    return a, da


def g(r, u):
    return mp.exp(r * u) * (mp.cos(u) - r * mp.sin(u))


def feasible(r, p):
    if r == 0 or p <= PI:
        return True
    if p >= 2 * PI:
        return False
    return g(r, p) - 1 <= 0


# ---------------- read leaves
with gzip.open(LEAVES, "rb") as fh:
    raw = fh.read()
leaves_sha = hashlib.sha256(raw).hexdigest()
leaves = []
for ln in raw.decode().splitlines():
    if ln.strip():
        c_, p_, o_ = ln.split()
        leaves.append((int(c_), p_, o_))
del raw
with open(SAMPLE, "rb") as fh:
    sraw = fh.read()
sample_sha = hashlib.sha256(sraw).hexdigest()
samples = [ln.split() for ln in sraw.decode().splitlines() if ln.strip()]

# ---------------- determine the cell ordering from the samples
order_ok = []
for offset in (996, 0):
    for order in itertools.permutations(range(3)):
        good = True
        for si, sl in enumerate(samples):
            li = 997 * si + offset
            if li >= len(leaves):
                good = False
                break
            ci, path, out = leaves[li]
            b = box_fr(leaf_geom(ci, path, order))
            want = [Fr(x) for x in sl[1:7]]
            got = [b[0][0], b[0][1], b[1][0], b[1][1], b[2][0], b[2][1]]
            if out != sl[0] or got != want:
                good = False
                break
        if good:
            order_ok.append((order, offset))
res = {"script": "replay_primal_full_v2.py", "label": "EXTRA EXPLORATORY full-leaf point replay + tiling audit",
       "leaves_path": LEAVES, "leaves_gz_uncompressed_sha256": leaves_sha, "sample_path": SAMPLE,
       "sample_sha256": sample_sha, "leaves": len(leaves), "axis_sequence_first40": "".join("rwp"[a] for a in AXIS[:40]),
       "orders_matching_all_948_samples": [[list(o), off] for o, off in order_ok]}
if len(order_ok) != 1:
    res["verdict"] = "STOP: cell ordering not uniquely determined by the samples"
    with lane_guard.xopen(os.path.join(RUN, "replay_primal_full.json")) as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res))
    sys.exit(2)
ORDER = order_ok[0][0]
res["sample_offset"] = order_ok[0][1]

# ---------------- tiling audit
bycell = {}
for ci, path, out in leaves:
    bycell.setdefault(ci, []).append("" if path == "-" else path)
tiling_err = []
for ci in range(NCELL[0] * NCELL[1] * NCELL[2]):
    ps = bycell.get(ci)
    if ps is None:
        tiling_err.append({"cell": ci, "err": "missing"})
        continue
    if len(ps) == 1 and ps[0] == "":
        continue
    ps.sort()
    kraft = sum(1 << (MAXD - len(p)) for p in ps)
    pref = any(ps[i + 1].startswith(ps[i]) for i in range(len(ps) - 1))
    if kraft != (1 << MAXD) or pref or "" in ps:
        tiling_err.append({"cell": ci, "kraft_ok": kraft == (1 << MAXD), "prefix_violation": pref})
extra_cells = [c for c in bycell if not (0 <= c < NCELL[0] * NCELL[1] * NCELL[2])]
res["tiling"] = {"cells_expected": NCELL[0] * NCELL[1] * NCELL[2], "cells_seen": len(bycell),
                 "cells_out_of_range": extra_cells[:20], "errors_first50": tiling_err[:50],
                 "tiling_ok": not tiling_err and not extra_cells}
del bycell

# ---------------- evaluation
stats = {"SGE": {"n": 0, "feasible_mid": 0, "min_margin": None, "argmin": None},
         "DPOS": {"n": 0, "points": 0, "min_dSdr": None, "argmin": None},
         "INFEAS": {"n": 0, "min_g_minus_1_worst_corner": None, "argmin": None, "phi_lo_ge_2pi": 0}}
viol = []
claims = []
other = []
for li, (ci, path, out) in enumerate(leaves):
    b = box_fr(leaf_geom(ci, path, ORDER))
    mid = [(lo + hi) / 2 for lo, hi in b]
    if out == "SGE":
        st = stats["SGE"]
        st["n"] += 1
        r, w, p = (mpq(x) for x in mid)
        a, _ = moments(r, w, p)
        S = 2 * a[0] * a[2] / a[1] ** 2 - 1
        if feasible(r, p):
            st["feasible_mid"] += 1
            mgn = S - T
            if st["min_margin"] is None or mgn < st["min_margin"]:
                st["min_margin"], st["argmin"] = mgn, {"leaf": li, "mid": [str(x) for x in mid]}
            if mgn <= TINY:
                viol.append({"leaf": li, "outcome": out, "mid": [str(x) for x in mid], "S": mp.nstr(S, 25)})
        elif a[1] <= 0 or S <= T:
            claims.append({"leaf": li, "outcome": out, "note": "infeasible midpoint with a1 <= 0 or S <= T"})
    elif out == "DPOS":
        st = stats["DPOS"]
        st["n"] += 1
        pts = [tuple(mid)] + [(b[0][i], b[1][j], b[2][kq]) for i in (0, 1) for j in (0, 1) for kq in (0, 1)]
        for pt in pts:
            st["points"] += 1
            r, w, p = (mpq(x) for x in pt)
            a, da = moments(r, w, p)
            dS = 2 * (da[0] * a[2] + a[0] * da[2]) / a[1] ** 2 - 4 * a[0] * a[2] * da[1] / a[1] ** 3
            if st["min_dSdr"] is None or dS < st["min_dSdr"]:
                st["min_dSdr"], st["argmin"] = dS, {"leaf": li, "point": [str(x) for x in pt]}
            if dS <= TINY:
                viol.append({"leaf": li, "outcome": out, "point": [str(x) for x in pt], "dSdr": mp.nstr(dS, 25)})
            if min(a) <= 0:
                claims.append({"leaf": li, "outcome": out, "note": "a_k <= 0", "point": [str(x) for x in pt]})
    elif out == "INFEAS":
        st = stats["INFEAS"]
        st["n"] += 1
        rl, pl = b[0][0], b[2][0]
        ok = rl > 0
        gm = None
        if ok:
            rr, pp = mpq(rl), mpq(pl)
            if pp >= 2 * PI:
                st["phi_lo_ge_2pi"] += 1
            elif pp > PI:
                gm = g(rr, pp) - 1
                ok = gm > TINY
                if st["min_g_minus_1_worst_corner"] is None or gm < st["min_g_minus_1_worst_corner"]:
                    st["min_g_minus_1_worst_corner"], st["argmin"] = gm, {"leaf": li, "r_lo": str(rl), "phi_lo": str(pl)}
            else:
                ok = False
        rm, wm, pm = (mpq(x) for x in mid)
        if (not ok) or feasible(rm, pm):
            viol.append({"leaf": li, "outcome": out, "r_lo": str(rl), "phi_lo": str(pl),
                         "g_minus_1": None if gm is None else mp.nstr(gm, 20)})
    else:
        other.append({"leaf": li, "outcome": out})


def nstr(x):
    return None if x is None else mp.nstr(x, 20)


for o, keyname in (("SGE", "min_margin"), ("DPOS", "min_dSdr"), ("INFEAS", "min_g_minus_1_worst_corner")):
    stats[o][keyname] = nstr(stats[o][keyname])
res.update({"cell_order_axes_most_to_least_significant": ["r", "w", "phi"][ORDER[0]] + "," +
            ["r", "w", "phi"][ORDER[1]] + "," + ["r", "w", "phi"][ORDER[2]],
            "stats": stats, "violations_count": len(viol), "violations_first100": viol[:100],
            "whole_box_claim_issues_count": len(claims), "whole_box_claim_issues_first50": claims[:50],
            "other_outcomes": other[:50], "elapsed_s": round(time.time() - T0, 1)})
okall = res["tiling"]["tiling_ok"] and not viol and not other
res["verdict"] = ("TILING OK and NO VIOLATION at any evaluated point" if okall else "ISSUES FOUND (see fields)")
with lane_guard.xopen(os.path.join(RUN, "replay_primal_full.json")) as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({kq: res[kq] for kq in ("leaves", "orders_matching_all_948_samples", "verdict", "violations_count",
                                         "whole_box_claim_issues_count", "elapsed_s")}))
print(json.dumps(res["tiling"]))
print(json.dumps(stats))
sys.exit(0 if okall else 1)

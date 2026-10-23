"""EXTRA (beyond the sample task): independent replay over ALL leaves of one dual chart (smoke test, NOT a certificate)
plus an independent tiling audit.  Written by MathPhaseType3.ME3Reductions; imports nothing from L/code.

Geometry (read as definitions from the chart's spec JSON): per-axis breakpoints (initial cells = products of breakpoint
intervals), split_weights, max_depth; split rule (charts-spec-v1.md): bisect the axis maximizing width*weight (ties ->
lowest axis) at the exact midpoint, child 0 = lower half.  Within a cell all boxes at a given depth have equal widths, so
the split-axis sequence is computed once per cell.  Leaf records "cell path outcome" (path "-" = empty), streamed.
Cell-index order: the unique (axis permutation, sample offset in {stride-1, 0}) reproducing every line of the chart's
sample_boxes.txt exactly (outcome and six rationals) from the leaves at indices offset + k*stride; otherwise STOP.
Tiling audit per cell: prefix-free path set and Kraft sum exactly 1 (complete binary tree); cells contiguous and all
present.
Evaluation (mpmath dps 50; formulas identical to replay_dual_v1.py, re-typed here): CERT leaves are tested at the
midpoint (CORNERS=1: midpoint + 8 corners); non-physical points are skipped and counted; SKIP leaves: geometric rule
(G: w_hi <= 40, w_lo >= 1/5, delta_hi <= 3 w_lo; LD2: chi_lo rt_lo > 1/16 or (1 - chi_hi) rt_lo > cos(beta_lo)/65);
any other outcome is reported.
Usage: replay_dual_full_v1.py RUN CHART SPEC_JSON LEAVES_GZ SAMPLE_PATH STRIDE CORNERS
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

RUN, CHART, SPEC, LEAVES, SAMPLE, STRIDE, CORNERS = sys.argv[1:8]
STRIDE = int(STRIDE)
CORNERS = CORNERS == "1"
T0 = time.time()
mp.mp.dps = 50
KAPPA = mp.mpf(50) / 61
PI = mp.pi
TINY = mp.mpf(10) ** -40

with open(SPEC, "rb") as fh:
    spec_raw = fh.read()
spec = json.loads(spec_raw)["charts"][CHART]
BP = [[Fr(x) for x in ax] for ax in spec["breakpoints"]]
NC = [len(ax) - 1 for ax in BP]
WT = [Fr(x) for x in spec["split_weights"]]
MAXD = 64


def mpq(q):
    return mp.mpf(q.numerator) / q.denominator


# ---------------- physics (re-typed from replay_dual_v1.py)
def to_physical(v):
    a, b, c = v
    if CHART in ("SWC", "SWB", "G"):
        if c <= 0:
            return None, "omega<=0"
        return (mpq(a), mpq(b), mpq(c)), None
    if CHART == "LW":
        if c <= 0:
            return None, "nu=0"
        return (mpq(a), mpq(b), 1 / mpq(c)), None
    be = mpq(c)
    if be <= 0 or be >= PI / 2:
        return None, "beta not in (0, pi/2)"
    if CHART == "LD1":
        if b <= 0:
            return None, "d=0"
        dm = mpq(b)
        return (mpq(a), 1 / dm - 1, mp.tan(be) / dm), None
    dnum = (1 - a) * b  # LD2: (chi, rho_t, beta)
    if dnum <= 0:
        return None, "d=0"
    dm = mpq(dnum) / mp.cos(be)
    return (mpq(a * b), 1 / dm - 1, mp.tan(be) / dm), None


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


def theta1(r):
    lo, hi = PI, 2 * PI
    for _ in range(60):
        mid = (lo + hi) / 2
        if g(r, mid) - 1 > 0:
            hi = mid
        else:
            lo = mid
    try:
        cand = mp.findroot(lambda u: g(r, u) - 1, (lo, hi), solver="anderson")
        eps = mp.mpf(10) ** -45 * cand
        if lo <= cand <= hi and g(r, cand - eps) - 1 < 0 and g(r, cand + eps) - 1 > 0:
            return cand
    except (ValueError, ZeroDivisionError):
        pass
    for _ in range(200):
        mid = (lo + hi) / 2
        if g(r, mid) - 1 > 0:
            hi = mid
        else:
            lo = mid
        if hi - lo < mp.mpf(10) ** -48 * hi:
            break
    return (lo + hi) / 2


def member(W, de, om):
    absW = abs(W)
    if absW == 0:
        return True, mp.mpf(0), "zero"
    alpha = mp.arg(W)
    if alpha < 0:
        alpha += 2 * PI
    r = de / om
    if r == 0:
        return absW <= 1, 1 - absW, "disk"
    if alpha <= PI:
        bound = mp.exp(-r * alpha)
        return absW <= bound, bound - absW, "radial"
    th = theta1(r)
    if alpha <= th:
        bound = mp.exp(-r * alpha)
        return absW <= bound, bound - absW, "radial"
    P1 = mp.exp(mp.mpc(-r, 1) * th)
    d1 = P1 - 1
    marg = mp.im(mp.conj(d1) * (W - 1)) * mp.sign(mp.im(mp.conj(d1) * (-1))) / abs(d1)
    return marg >= 0, marg, "chord"


def skip_rule_ok(b):
    if CHART == "G":
        (sl, sh), (dl, dh), (wl, wh) = b
        return wh <= 40 and wl >= Fr(1, 5) and dh <= 3 * wl
    if CHART == "LD2":
        (cl, ch), (tl, th_), (bl, bh) = b
        return cl * tl > Fr(1, 16) or mpq((1 - ch) * tl) > mp.cos(mpq(bl)) / 65
    return False


# ---------------- geometry
def cell_idx(ci, order):
    idx = [0, 0, 0]
    rem = ci
    for ax in reversed(order):
        idx[ax] = rem % NC[ax]
        rem //= NC[ax]
    return idx if rem == 0 else None


_axseq = {}


def axis_seq(idx):
    key = tuple(idx)
    if key not in _axseq:
        w = [BP[j][idx[j] + 1] - BP[j][idx[j]] for j in range(3)]
        k = [0, 0, 0]
        seq = []
        for _ in range(MAXD):
            sc = [w[j] / 2 ** k[j] * WT[j] for j in range(3)]
            j = max(range(3), key=lambda i: (sc[i], -i))
            seq.append(j)
            k[j] += 1
        _axseq[key] = (seq, w)
    return _axseq[key]


def leaf_box(ci, path, order):
    idx = cell_idx(ci, order)
    if idx is None:
        return None
    seq, w = axis_seq(idx)
    m = [0, 0, 0]
    kk = [0, 0, 0]
    if path != "-":
        for depth, bit in enumerate(path):
            ax = seq[depth]
            m[ax] = 2 * m[ax] + (1 if bit == "1" else 0)
            kk[ax] += 1
    out = []
    for j in range(3):
        base = BP[j][idx[j]]
        wd = w[j] / 2 ** kk[j]
        out.append((base + m[j] * wd, base + (m[j] + 1) * wd))
    return out


def stream():
    with gzip.open(LEAVES, "rt") as fh:
        for ln in fh:
            if ln.strip():
                c_, p_, o_ = ln.split()
                yield int(c_), p_, o_


with open(SAMPLE, "rb") as fh:
    sraw = fh.read()
samples = [ln.split() for ln in sraw.decode().splitlines() if ln.strip()]
want_idx = {}
for off in (STRIDE - 1, 0):
    for si in range(len(samples)):
        want_idx.setdefault(off + STRIDE * si, None)
h = hashlib.sha256()
nleaves = 0
for li, rec in enumerate(stream()):
    nleaves += 1
    if li in want_idx:
        want_idx[li] = rec
with gzip.open(LEAVES, "rb") as fh:
    for chunk in iter(lambda: fh.read(1 << 20), b""):
        h.update(chunk)
leaves_sha = h.hexdigest()
matches = []
for off in (STRIDE - 1, 0):
    for order in itertools.permutations(range(3)):
        good = True
        for si, sl in enumerate(samples):
            rec = want_idx.get(off + STRIDE * si)
            if rec is None:
                good = False
                break
            b = leaf_box(rec[0], rec[1], order)
            if b is None or rec[2] != sl[0] or [b[0][0], b[0][1], b[1][0], b[1][1], b[2][0], b[2][1]] != \
                    [Fr(x) for x in sl[1:7]]:
                good = False
                break
        if good:
            matches.append((order, off))
res = {"script": "replay_dual_full_v1.py", "label": "EXTRA EXPLORATORY full-leaf point replay + tiling audit",
       "chart": CHART, "spec": SPEC, "spec_sha256": hashlib.sha256(spec_raw).hexdigest(), "leaves_path": LEAVES,
       "leaves_gz_uncompressed_sha256": leaves_sha, "leaves": nleaves, "sample_path": SAMPLE,
       "sample_sha256": hashlib.sha256(sraw).hexdigest(), "stride": STRIDE, "corners": CORNERS,
       "matches_(order,offset)": [[list(o), off] for o, off in matches]}
if len(matches) != 1:
    res["verdict"] = "STOP: cell ordering/offset not uniquely determined by the samples"
    with lane_guard.xopen(os.path.join(RUN, "replay_dual_full_%s.json" % CHART)) as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res))
    sys.exit(2)
ORDER = matches[0][0]

# ---------------- second pass: tiling audit + evaluation
ncells = NC[0] * NC[1] * NC[2]
tiling_err = []
seen = set()
cur = None
paths = []
counts = {"outcomes": {}, "cert": 0, "skip": 0, "other": 0, "tested_points": 0, "nonphysical": {}, "modes": {}}
viol = []
skip_fail = []
other = []
nbad = {"viol": 0, "skip_fail": 0, "other": 0, "tiling": 0}
minm = None
argm = None


def close_cell(ci, ps):
    if ci is None:
        return
    if len(ps) == 1 and ps[0] == "":
        return
    ps.sort()
    kraft = sum(1 << (MAXD - len(p)) for p in ps)
    pref = any(ps[i + 1].startswith(ps[i]) for i in range(len(ps) - 1))
    if kraft != (1 << MAXD) or pref or "" in ps:
        tiling_err.append({"cell": ci, "kraft_ok": kraft == (1 << MAXD), "prefix_violation": pref})


for li, (ci, path, out) in enumerate(stream()):
    if ci != cur:
        close_cell(cur, paths)
        if ci in seen:
            tiling_err.append({"cell": ci, "err": "non-contiguous"})
        seen.add(ci)
        cur, paths = ci, []
    paths.append("" if path == "-" else path)
    counts["outcomes"][out] = counts["outcomes"].get(out, 0) + 1
    b = leaf_box(ci, path, ORDER)
    if b is None:
        tiling_err.append({"cell": ci, "err": "cell index out of range"})
        continue
    if out.startswith("SKIP"):
        counts["skip"] += 1
        if not skip_rule_ok(b):
            nbad["skip_fail"] += 1
            if len(skip_fail) < 100:
                skip_fail.append({"leaf": li, "box": [[str(x) for x in iv] for iv in b]})
        continue
    if not out.startswith("CERT"):
        counts["other"] += 1
        nbad["other"] += 1
        if len(other) < 100:
            other.append({"leaf": li, "outcome": out})
        continue
    counts["cert"] += 1
    mid = tuple((lo + hi) / 2 for lo, hi in b)
    pts = [mid]
    if CORNERS:
        pts += [(b[0][i], b[1][j], b[2][k]) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    for v in pts:
        phys, why = to_physical(v)
        if phys is None:
            counts["nonphysical"][why] = counts["nonphysical"].get(why, 0) + 1
            continue
        s, de, om = phys
        counts["tested_points"] += 1
        W = W_of(s, de, om)
        ins, marg, mode = member(W, de, om)
        counts["modes"][mode] = counts["modes"].get(mode, 0) + 1
        if minm is None or marg < minm:
            minm = marg
            argm = {"leaf": li, "chart_point": [str(x) for x in v], "s_delta_omega": [mp.nstr(s, 15), mp.nstr(de, 15),
                                                                                       mp.nstr(om, 15)], "mode": mode}
        if (not ins) or marg <= TINY:
            nbad["viol"] += 1
            if len(viol) < 100:
                viol.append({"leaf": li, "outcome": out, "chart_point": [str(x) for x in v], "mode": mode,
                             "margin": mp.nstr(marg, 20), "W": mp.nstr(W, 20)})
close_cell(cur, paths)
missing = [c for c in range(ncells) if c not in seen]
res.update({"cell_order": list(ORDER), "sample_offset": matches[0][1],
            "tiling": {"cells_expected": ncells, "cells_seen": len(seen), "missing_first20": missing[:20],
                       "errors_first50": tiling_err[:50], "tiling_ok": not tiling_err and not missing},
            "counts": counts, "min_margin": None if minm is None else mp.nstr(minm, 20), "argmin": argm,
            "violations_count": nbad["viol"], "violations_first100": viol, "skip_rule_failures": skip_fail,
            "skip_rule_failures_count": nbad["skip_fail"], "other_outcomes_count": nbad["other"],
            "other_outcomes_first100": other, "elapsed_s": round(time.time() - T0, 1)})
ok = res["tiling"]["tiling_ok"] and not nbad["viol"] and not nbad["skip_fail"] and not nbad["other"]
res["verdict"] = "TILING OK and NO VIOLATION at any evaluated point" if ok else "ISSUES FOUND (see fields)"
with lane_guard.xopen(os.path.join(RUN, "replay_dual_full_%s.json" % CHART)) as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({k: res[k] for k in ("chart", "leaves", "matches_(order,offset)", "verdict", "violations_count",
                                      "skip_rule_failures_count", "min_margin", "elapsed_s")}))
print(json.dumps(res["tiling"]))
print(json.dumps(counts))
sys.exit(0 if ok else 1)

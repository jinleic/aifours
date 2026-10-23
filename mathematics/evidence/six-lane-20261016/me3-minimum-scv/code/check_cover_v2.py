"""Independent coverage audit for DUAL chart leaf records (breakpoint grids), version 2.

argv[1] = run directory (output); argv[2] = spec; argv[3] = chart; argv[4] = leaves.txt.gz; argv[5] = sample stride.
Checks: every initial cell present in order; per cell the leaf paths are the DFS leaves of a full binary tree
(tiling with disjoint interiors); outcomes are CERT:<tag> or SKIP:<rule>, never FAIL; every SKIP leaf satisfies its
geometric rule exactly (in-primal-P: w_hi <= P_w_hi, w_lo >= P_w_lo, delta_hi <= P_r_hi * w_lo, exact rationals;
skip-s: chi_lo * rt_lo > s_max, exact; skip-d: (1 - chi_hi) * rt_lo > d_max * cos(beta_lo), arb ball comparison).
Writes cover.json and sample_boxes.txt (exclusive create).
"""
import sys
import json
import gzip
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
from fractions import Fraction  # noqa: E402
from flint import arb, fmpq  # noqa: E402

RUN, specp, chart, leafp, stride = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
spec = json.load(open(specp))
cs = spec["charts"][chart]
bps = [[Fraction(str(v)) for v in dim] for dim in cs["breakpoints"]]
wts = [Fraction(str(w)) for w in cs["split_weights"]]
par = {k: Fraction(str(v)) for k, v in cs.get("params", {}).items()}
n0, n1, n2 = len(bps[0]) - 1, len(bps[1]) - 1, len(bps[2]) - 1


def cell_box(ci):
    a, rem = divmod(ci, n1 * n2)
    b, c = divmod(rem, n2)
    return [(bps[0][a], bps[0][a + 1]), (bps[1][b], bps[1][b + 1]), (bps[2][c], bps[2][c + 1])]


def split_dim(box):
    sc = [(box[i][1] - box[i][0]) * wts[i] for i in range(3)]
    best = 0
    for i in (1, 2):
        if sc[i] > sc[best]:
            best = i
    return best


def box_of(ci, path):
    box = cell_box(ci)
    for ch in path:
        i = split_dim(box)
        lo, hi = box[i]
        mid = (lo + hi) / 2
        box[i] = (lo, mid) if ch == "0" else (mid, hi)
    return box


def fq(x):
    return fmpq(x.numerator, x.denominator)


def skip_ok(rule, box):
    if rule == "SKIP:in-primal-P":
        (sl, sh), (dl, dh), (wl, wh) = box
        return wh <= par["P_w_hi"] and wl >= par["P_w_lo"] and dh <= par["P_r_hi"] * wl
    if rule == "SKIP:skip-s":
        (xl, xh), (ql, qh), (bl, bh) = box
        return xl * ql > par["s_max"]
    if rule == "SKIP:skip-d":
        (xl, xh), (ql, qh), (bl, bh) = box
        return bool(arb(fq((1 - xh) * ql)) > arb(fq(par["d_max"])) * arb(fq(bl)).cos())
    return False


errors = []
counts = {}
cur = -1
expected = []
seen = 0
n = 0
sample = []
skips_checked = 0
with gzip.open(leafp, "rt") as fh:
    for line in fh:
        ci_s, path, out = line.split()
        ci = int(ci_s)
        path = "" if path == "-" else path
        counts[out] = counts.get(out, 0) + 1
        if not (out.startswith("CERT:") or out.startswith("SKIP:")):
            errors.append(f"bad outcome {out} cell {ci} path {path}")
        if ci != cur:
            if cur >= 0 and expected:
                errors.append(f"cell {cur} incomplete")
            if ci != cur + 1:
                errors.append(f"cell jump {cur}->{ci}")
            cur, seen, expected = ci, seen + 1, [""]
        if not expected:
            errors.append(f"cell {ci} extra leaf {path}")
            continue
        e = expected.pop()
        while e != path:
            if not path.startswith(e) or len(path) <= len(e):
                errors.append(f"cell {ci}: leaf {path} vs expected {e}")
                break
            expected.append(e + "1")
            e = e + "0"
        if out.startswith("SKIP:"):
            if not skip_ok(out, box_of(ci, path)):
                errors.append(f"skip rule {out} fails at cell {ci} path {path}")
            skips_checked += 1
        n += 1
        if n % stride == 0:
            b = box_of(ci, path)
            sample.append(f"{out} " + " ".join(f"{lo} {hi}" for lo, hi in b))
        if len(errors) > 50:
            break
if expected:
    errors.append(f"cell {cur} incomplete at end")
if seen != n0 * n1 * n2:
    errors.append(f"cells seen {seen} != {n0 * n1 * n2}")
res = {"chart": chart, "leaves": n, "counts": counts, "cells_expected": n0 * n1 * n2, "cells_seen": seen,
       "skips_checked": skips_checked, "errors_first50": errors[:50], "tiling_ok": not errors}
with lane_guard.xopen(RUN + "/cover.json") as fh:
    json.dump(res, fh, indent=1)
with lane_guard.xopen(RUN + "/sample_boxes.txt") as fh:
    fh.write("\n".join(sample) + "\n")
print(json.dumps(res, indent=1))

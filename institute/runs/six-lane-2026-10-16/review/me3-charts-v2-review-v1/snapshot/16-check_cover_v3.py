"""Independent coverage audit, version 3, for the primal chart P and the six dual charts (v1/v2 kept unchanged).

Changes (hostile review institute/runs/six-lane-2026-10-16/review/me3-charts-codex-v1.note.md, findings 3-4):
  * the allowed outcome set of every chart is HARD-CODED below (not read from the command line, not accepted by
    prefix); FAIL and every unknown outcome are rejected unconditionally;
  * the spec is bound to the proof: chart kind, T, variable order, outer domain (first/last breakpoints or region),
    chart parameters and series length must equal the hard-coded values of proof/me3-theorem-v4.md section 4;
    LD charts additionally need beta_top > pi/2 (ball comparison) and rho_t top = s_max + d_max (exact);
  * every leaf depth is checked against the spec's max_depth;
  * the leaf file is bound to the run summary: SHA-256 of the uncompressed leaf lines must equal the summary's
    leaf_lines_sha256 and the per-outcome counts must equal the summary's counts (FAIL-free, cap not hit,
    certificate_ok true);
  * SKIP rules re-checked as in v2 (in-primal-P and skip-s exactly in rationals; skip-d with 128-bit arb balls).
Geometry only: no chart test is evaluated. Tiling check as in v1/v2: per initial cell, in file order, the leaf paths
must be exactly the depth-first leaves of a full binary tree (no gaps, no overlaps, no extra or missing cells).
argv[1] = run dir (output); argv[2] = spec; argv[3] = chart (P, G, SWB, SWC, LW, LD1, LD2); argv[4] = leaves.txt.gz;
argv[5] = run summary (primal.json or dual.json); argv[6] = sample stride. Writes cover.json, sample_boxes.txt.
"""
import sys
import json
import gzip
import hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
from fractions import Fraction as Fr  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402

flint.ctx.prec = 128
RUN, specp, chart, leafp, summp, stride = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], int(sys.argv[6])

EXPECT = {
    "P": {"kind": None, "domain": [("0", "3"), ("1/5", "40"), ("0", "31416/5000")],
          "allowed": {"SGE", "DPOS", "INFEAS"}},
    "G": {"kind": "G", "domain": [("0", "1"), ("0", "64"), ("1/5", "640")],
          "allowed": {"CERT:small", "CERT:radial", "CERT:radial-mvf", "CERT:triangle", "SKIP:in-primal-P"},
          "params": {"P_w_lo": "1/5", "P_w_hi": "40", "P_r_hi": "3"}},
    "SWB": {"kind": "B", "domain": [("0", "1"), ("3/10", "64"), ("0", "1/5")],
            "allowed": {"CERT:bedge", "CERT:bedge-mvf"}},
    "SWC": {"kind": "C", "domain": [("0", "1"), ("0", "3/10"), ("0", "1/5")],
            "allowed": {"CERT:corner", "CERT:corner-mvf"}, "series_terms": 20},
    "LW": {"kind": "LW", "domain": [("0", "1"), ("0", "64"), ("0", "1/640")], "allowed": {"CERT:small"}},
    "LD1": {"kind": "LD1", "domain": [("1/16", "1"), ("0", "1/65"), ("0", "15708/10000")],
            "allowed": {"CERT:ld1"}, "params": {"beta_top": "15708/10000"}},
    "LD2": {"kind": "LD2", "domain": [("0", "1"), ("0", "81/1040"), ("0", "15708/10000")],
            "allowed": {"CERT:ld2", "SKIP:skip-s", "SKIP:skip-d"},
            "params": {"beta_top": "15708/10000", "s_max": "1/16", "d_max": "1/65"}},
}
E = EXPECT[chart]
spec = json.load(open(specp))
summ = json.load(open(summp))
errors = []


def F(x):
    return Fr(str(x))


def fq(x):
    return fmpq(x.numerator, x.denominator)


if F(spec["T"]) != Fr(11, 50):
    errors.append(f"spec T {spec['T']} != 11/50")
if chart == "P":
    names = ("r", "w", "phi")                      # bound to cert_primal_v3.py line 45
    reg = [(F(spec["region"][k][0]), F(spec["region"][k][1])) for k in names]
    nsplit = [int(spec["initial_split"][k]) for k in names]
    bps = [[reg[d][0] + (reg[d][1] - reg[d][0]) * Fr(i, nsplit[d]) for i in range(nsplit[d] + 1)] for d in range(3)]
    wts = [F(w) for w in spec["split_weights"]]
    maxdepth = int(spec["max_depth"])
else:
    cs = spec["charts"][chart]
    if cs["kind"] != E["kind"]:
        errors.append(f"chart kind {cs['kind']} != {E['kind']}")
    bps = [[F(v) for v in dim] for dim in cs["breakpoints"]]
    wts = [F(w) for w in cs["split_weights"]]
    maxdepth = int(cs["max_depth"])
    par = {k: F(v) for k, v in cs.get("params", {}).items()}
    if par != {k: F(v) for k, v in E.get("params", {}).items()}:
        errors.append(f"chart params {cs.get('params')} != {E.get('params')}")
    if "series_terms" in E and int(cs["series_terms"]) != E["series_terms"]:
        errors.append(f"series_terms {cs['series_terms']} != {E['series_terms']}")
for d in range(3):
    if len(bps[d]) < 2 or any(not (bps[d][i] < bps[d][i + 1]) for i in range(len(bps[d]) - 1)):
        errors.append(f"breakpoints of variable {d} not strictly increasing")
    if (bps[d][0], bps[d][-1]) != (F(E["domain"][d][0]), F(E["domain"][d][1])):
        errors.append(f"domain of variable {d}: [{bps[d][0]}, {bps[d][-1]}] != {E['domain'][d]}")
if any(w <= 0 for w in wts):
    errors.append("nonpositive split weight")
if chart in ("LD1", "LD2"):
    if not bool(arb(fq(F(E["params"]["beta_top"]))) > arb.pi() / 2):
        errors.append("beta_top not certified > pi/2")
    if not (bps[2][-1] >= F(E["params"]["beta_top"])):
        errors.append("beta range does not reach beta_top")
if chart == "LD2" and bps[1][-1] != F(E["params"]["s_max"]) + F(E["params"]["d_max"]):
    errors.append("rho_t top != s_max + d_max")
if chart == "LD1" and bps[0][0] != F(EXPECT["LD2"]["params"]["s_max"]):
    errors.append("LD1 s_lo != LD2 s_max (s-union gap)")
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


def skip_ok(rule, box):
    if chart == "G" and rule == "SKIP:in-primal-P":
        (sl, sh), (dl, dh), (wl, wh) = box
        return wh <= Fr(40) and wl >= Fr(1, 5) and dh <= 3 * wl
    if chart == "LD2" and rule == "SKIP:skip-s":
        (xl, xh), (ql, qh), (bl, bh) = box
        return xl * ql > Fr(1, 16)
    if chart == "LD2" and rule == "SKIP:skip-d":
        (xl, xh), (ql, qh), (bl, bh) = box
        return bool(arb(fq((1 - xh) * ql)) > arb(fq(Fr(1, 65))) * arb(fq(bl)).cos())
    return False


counts = {}
cur = -1
expected = []
seen = 0
n = 0
sample = []
skips_checked = 0
maxd_seen = 0
hasher = hashlib.sha256()
with gzip.open(leafp, "rt") as fh:
    for line in fh:
        hasher.update(line.encode())
        ci_s, path, out = line.split()
        ci = int(ci_s)
        path = "" if path == "-" else path
        counts[out] = counts.get(out, 0) + 1
        if out not in E["allowed"]:
            errors.append(f"outcome {out} not allowed in chart {chart} (cell {ci} path {path})")
        if out == "FAIL" or not set(path) <= {"0", "1"}:
            errors.append(f"FAIL or malformed path at cell {ci} path {path}")
        if len(path) > maxdepth:
            errors.append(f"depth {len(path)} > max_depth {maxdepth} at cell {ci}")
        maxd_seen = max(maxd_seen, len(path))
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
lines_sha = hasher.hexdigest()
if lines_sha != summ.get("leaf_lines_sha256"):
    errors.append(f"leaf lines sha256 {lines_sha} != summary {summ.get('leaf_lines_sha256')}")
nz = {k: v for k, v in summ.get("counts", {}).items() if v}
if counts != nz:
    errors.append(f"counts {counts} != summary counts {nz}")
if summ.get("certificate_ok") is not True or summ.get("eval_cap_hit") is not False:
    errors.append("summary not certificate_ok or eval cap hit")
gz_sha = hashlib.sha256(open(leafp, "rb").read()).hexdigest()
res = {"checker": "check_cover_v3", "chart": chart, "spec": specp, "leaves_file": leafp, "leaves_gz_sha256": gz_sha,
       "leaf_lines_sha256": lines_sha, "leaves": n, "counts": counts, "allowed": sorted(E["allowed"]),
       "cells_expected": n0 * n1 * n2, "cells_seen": seen, "max_depth_spec": maxdepth, "max_depth_seen": maxd_seen,
       "skips_checked": skips_checked, "errors_first50": errors[:50], "audit_ok": not errors}
with lane_guard.xopen(RUN + "/cover.json") as fh:
    json.dump(res, fh, indent=1)
with lane_guard.xopen(RUN + "/sample_boxes.txt") as fh:
    fh.write("\n".join(sample) + "\n")
print(json.dumps({k: res[k] for k in ("chart", "leaves", "counts", "cells_seen", "max_depth_seen", "skips_checked",
                                      "audit_ok", "errors_first50")}))

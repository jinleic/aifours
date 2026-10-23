"""Certified branch-and-bound for the DUAL far-region charts, version 4 (frozen spec JSON in argv[2]); identical to
cert_dual_v2.py except that the tests come from me3dual_v6.py (v2 used me3dual_v3.py; v3 imported the superseded v4).

argv[1] = run directory; argv[2] = spec; argv[3] = chart name. Writes dual.json and leaves.txt.gz (exclusive create).
Initial cells: product of the chart's breakpoint intervals (exact rationals); cells numbered with the first
variable most significant. Split: argmax_i width_i * weight_i (ties -> lowest index), exact midpoint; child 0 lower.
Leaf outcomes: CERT:<test tag> (test passed on the whole box), SKIP:<rule> (box outside the chart's assigned set,
covered elsewhere), FAIL (max depth).  Tests: see me3dual_v6.py (and me3dual_v3.py for the shared definitions).
"""
import sys
import json
import time
import gzip
import math
import hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, fmpq  # noqa: E402
import me3dual_v6 as D  # noqa: E402

RUN = sys.argv[1]
spec = json.load(open(sys.argv[2]))
chart = sys.argv[3]
cs = spec["charts"][chart]
flint.ctx.prec = spec["prec"]


def Q(x):
    x = str(x)
    if "/" in x:
        a, b = x.split("/")
        return fmpq(int(a), int(b))
    return fmpq(int(x))


T = Q(spec["T"])
kap = arb(1 / (1 + T))
bps = [[Q(v) for v in dim] for dim in cs["breakpoints"]]
wts = [Q(w) for w in cs["split_weights"]]
maxdepth = cs["max_depth"]
kind = cs["kind"]
par = {k: Q(v) for k, v in cs.get("params", {}).items()}


def theta1_float(r):
    if r <= 0:
        return 2 * math.pi
    lo, hi = math.pi, 2 * math.pi
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if math.cos(mid) - r * math.sin(mid) - math.exp(-r * mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo


def evaluate(box):
    (al, ah), (bl, bh), (cl, ch) = box
    if kind == "C":
        return D.test_corner(al, ah, bl, bh, cl, ch, kap, int(cs["series_terms"]))
    if kind == "B":
        return D.test_bedge(al, ah, bl, bh, ch, kap)
    if kind == "G":
        if ch <= par["P_w_hi"] and bh <= par["P_r_hi"] * cl and cl >= par["P_w_lo"]:
            return True, "SKIP:in-primal-P"
        rm = float((bl + bh) / 2) / float((cl + ch) / 2)
        th = theta1_float(rm)
        theta_tri = fmpq(int(math.floor(th * 10000)), 10000) if th < 2 * math.pi - 1e-6 else None
        return D.test_general(al, ah, bl, bh, cl, ch, kap, theta_tri)
    if kind == "LW":
        return D.test_largew(al, ah, bl, bh, cl, ch, kap)
    if kind == "LD1":
        return D.test_ld1(al, ah, bl, bh, cl, ch, kap, par["beta_top"])
    if kind == "LD2":
        ok, tag = D.test_ld2(al, ah, bl, bh, cl, ch, kap, par["beta_top"], par["s_max"], par["d_max"])
        if ok and tag.startswith("skip"):
            return True, "SKIP:" + tag
        return ok, tag
    raise SystemExit("unknown kind")


def split_dim(box):
    sc = [(box[i][1] - box[i][0]) * wts[i] for i in range(3)]
    best = 0
    for i in (1, 2):
        if sc[i] > sc[best]:
            best = i
    return best


t0 = time.time()
cells = []
for a in range(len(bps[0]) - 1):
    for b in range(len(bps[1]) - 1):
        for c in range(len(bps[2]) - 1):
            cells.append(((bps[0][a], bps[0][a + 1]), (bps[1][b], bps[1][b + 1]), (bps[2][c], bps[2][c + 1])))
counts = {}
reasons = {}
fails = []
hasher = hashlib.sha256()
gz = gzip.GzipFile(fileobj=lane_guard.xopen(RUN + "/leaves.txt.gz", "xb"), mode="wb", mtime=0)
evals = 0
capped = False
for ci, cell in enumerate(cells):
    stack = [(cell, "")]
    while stack:
        box, path = stack.pop()
        ok, tag = evaluate(box)
        evals += 1
        if ok:
            out = tag if tag.startswith("SKIP") else "CERT:" + tag
        else:
            reasons[tag] = reasons.get(tag, 0) + 1
            if len(path) >= maxdepth:
                out = "FAIL"
                if len(fails) < 40:
                    fails.append({"cell": ci, "path": path, "box": [[str(x), str(y)] for x, y in box], "why": tag})
            else:
                i = split_dim(box)
                lo, hi = box[i]
                mid = (lo + hi) / 2
                b0, b1 = list(box), list(box)
                b0[i], b1[i] = (lo, mid), (mid, hi)
                stack.append((tuple(b1), path + "1"))
                stack.append((tuple(b0), path + "0"))
                continue
        counts[out] = counts.get(out, 0) + 1
        line = f"{ci} {path if path else '-'} {out}\n"
        gz.write(line.encode())
        hasher.update(line.encode())
        if evals % 200000 == 0:
            print("progress", evals, counts, round(time.time() - t0, 1), flush=True)
        if evals > cs["eval_cap"]:
            capped = True
            break
    if capped:
        print("EVAL CAP REACHED; no conclusion", flush=True)
        break
gz.close()
res = {"spec": spec["name"], "chart": chart, "kind": kind, "counts": counts, "evaluations": evals, "cells": len(cells),
       "fail_reasons_before_split": reasons, "fails_first40": fails, "eval_cap_hit": capped,
       "leaf_lines_sha256": hasher.hexdigest(), "certificate_ok": ("FAIL" not in counts) and not capped,
       "elapsed_seconds": round(time.time() - t0, 2)}
with lane_guard.xopen(RUN + "/dual.json") as fh:
    json.dump(res, fh, indent=1)
print("SUMMARY", json.dumps({k: res[k] for k in ("chart", "counts", "evaluations", "certificate_ok", "elapsed_seconds")}))

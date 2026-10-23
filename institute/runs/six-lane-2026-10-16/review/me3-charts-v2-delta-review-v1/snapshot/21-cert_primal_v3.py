"""Certified branch-and-bound on a PRIMAL region (r, w, phi), version 3 (spec JSON in argv[2]).

Same box tests as cert_valley_v2.py (INFEAS | SGE naive-then-MVF | DPOS naive-then-MVF), plus a complete,
compressed leaf record for an independent coverage audit:
  leaves.txt.gz : one line per leaf, "<cell_index> <path> <OUTCOME>", path over {0,1} (0 = lower half, 1 = upper
                  half of the split dimension; the split dimension is a deterministic function of the box, see
                  split_dim), in depth-first order. Initial cells are numbered in r-major, then w, then phi order.
The leaves of every cell form a complete prefix-free binary code iff they tile the cell (checked by
check_cover_v1.py, which also rebuilds exact boxes from the paths).
Definitions (real pole 1, pair -(1+delta) +- i w, r = delta/w, phi = w tau):
  c = (1 - i r) e^{(r - i) phi}, zeta = 1/(1 + r w - i w), a_k = 1 - Re(c zeta^{k+1}) = m_k/k!,
  G = 2 a0 a2 - (1+T) a1^2  (S > T iff G > 0 when a1 > 0),
  D = a0' a1 a2 + a0 a1 a2' - 2 a0 a1' a2, a_k' = -Re(c zeta^{k+1} [phi + (r - i)/(1 + r^2) - (k+1) w zeta])
      (dS/dr at fixed (w, phi) > 0 iff D > 0 when a0, a1, a2 > 0),
  INFEAS: phi_lo > pi, r_lo > 0 and g_{r_lo}(phi_lo) = e^{r_lo phi_lo}(cos phi_lo - r_lo sin phi_lo) > 1.
argv[1] = run directory. Writes primal.json and leaves.txt.gz (exclusive create).
"""
import sys
import json
import time
import gzip
import hashlib
sys.path.insert(0, __file__.rsplit("/", 1)[0])
import lane_guard  # noqa: E402
import flint  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402
import me3lib_v1 as L  # noqa: E402
from me3jet_v1 import EXP, RE, mvf  # noqa: E402

RUN = sys.argv[1]
spec = json.load(open(sys.argv[2]))
flint.ctx.prec = spec["prec"]


def Q(s):
    s = str(s)
    if "/" in s:
        a, b = s.split("/")
        return fmpq(int(a), int(b))
    return fmpq(int(s))


T = Q(spec["T"])
Tb = arb(T)
reg = [(Q(spec["region"][k][0]), Q(spec["region"][k][1])) for k in ("r", "w", "phi")]
nsplit = [spec["initial_split"][k] for k in ("r", "w", "phi")]
PI = arb.pi()
I = acb(0, 1)
maxdepth = spec["max_depth"]


def primal_GD_generic(R, Wv, Ph):
    c = (1 - I * R) * EXP((R - I) * Ph)
    zeta = 1 / (1 + R * Wv - I * Wv)
    shift = Ph + (R - I) / (1 + R * R)
    a, da = [], []
    zp = zeta
    for k in range(3):
        P = c * zp
        a.append(1 - RE(P))
        dP = P * (shift - (k + 1) * Wv * zeta)
        da.append(-RE(dP))
        zp = zp * zeta
    G = 2 * a[0] * a[2] - (1 + Tb) * a[1] * a[1]
    D = da[0] * a[1] * a[2] + a[0] * a[1] * da[2] - 2 * a[0] * da[1] * a[2]
    return (G, D)


def ball(lo, hi):
    return arb(lo).union(arb(hi))


stats = {"naive_SGE": 0, "mvf_SGE": 0, "naive_DPOS": 0, "mvf_DPOS": 0}


def classify(box):
    (rl, rh), (wl, wh), (pl, ph) = box
    if arb(pl) > PI and rl > 0:
        if L.g_feas(arb(rl), arb(pl)) > 1:
            return "INFEAS"
    rb, wb, pb = ball(rl, rh), ball(wl, wh), ball(pl, ph)
    a0, a1, a2, G, D = L.primal_G_D(rb, wb, pb, Tb)
    apos = a0 > 0 and a1 > 0 and a2 > 0
    if a1 > 0 and G > 0:
        stats["naive_SGE"] += 1
        return "SGE"
    if apos and D > 0:
        stats["naive_DPOS"] += 1
        return "DPOS"
    mids = [arb((rl + rh) / 2), arb((wl + wh) / 2), arb((pl + ph) / 2)]
    hb = [ball(-(rh - rl) / 2, (rh - rl) / 2), ball(-(wh - wl) / 2, (wh - wl) / 2), ball(-(ph - pl) / 2, (ph - pl) / 2)]
    Gm, Dm = mvf(primal_GD_generic, mids, [rb, wb, pb], hb)
    if a1 > 0 and Gm > 0:
        stats["mvf_SGE"] += 1
        return "SGE"
    if apos and Dm > 0:
        stats["mvf_DPOS"] += 1
        return "DPOS"
    return None


def split_dim(box):
    """Deterministic: largest width scaled by spec weights; ties -> lowest index."""
    wts = spec["split_weights"]
    sc = [(box[i][1] - box[i][0]) * Q(wts[i]) for i in range(3)]
    best = 0
    for i in (1, 2):
        if sc[i] > sc[best]:
            best = i
    return best


def children(box):
    i = split_dim(box)
    lo, hi = box[i]
    mid = (lo + hi) / 2
    b0, b1 = list(box), list(box)
    b0[i], b1[i] = (lo, mid), (mid, hi)
    return tuple(b0), tuple(b1)


t0 = time.time()
cells = []
for i in range(nsplit[0]):
    for j in range(nsplit[1]):
        for k in range(nsplit[2]):
            idx = (i, j, k)
            cells.append(tuple((reg[d][0] + (reg[d][1] - reg[d][0]) * idx[d] / nsplit[d],
                                reg[d][0] + (reg[d][1] - reg[d][0]) * (idx[d] + 1) / nsplit[d]) for d in range(3)))

counts = {"INFEAS": 0, "SGE": 0, "DPOS": 0, "FAIL": 0}
depth_hist = {}
fails = []
hasher = hashlib.sha256()
dpos_bb = None
evals = 0
gz = gzip.GzipFile(fileobj=lane_guard.xopen(RUN + "/leaves.txt.gz", "xb"), mode="wb", mtime=0)
capped = False
for ci, cell in enumerate(cells):
    stack = [(cell, "")]
    while stack:
        box, path = stack.pop()
        out = classify(box)
        evals += 1
        if out is None:
            if len(path) >= maxdepth:
                out = "FAIL"
                if len(fails) < 50:
                    fails.append({"cell": ci, "path": path, "box": [[str(x) for x in iv] for iv in box]})
            else:
                b0, b1 = children(box)
                stack.append((b1, path + "1"))
                stack.append((b0, path + "0"))
                continue
        counts[out] += 1
        depth_hist[len(path)] = depth_hist.get(len(path), 0) + 1
        line = f"{ci} {path if path else '-'} {out}\n"
        gz.write(line.encode())
        hasher.update(line.encode())
        if out == "DPOS":
            lo = [float(iv[0]) for iv in box]
            hi = [float(iv[1]) for iv in box]
            dpos_bb = [lo, hi] if dpos_bb is None else [[min(a, b) for a, b in zip(dpos_bb[0], lo)],
                                                         [max(a, b) for a, b in zip(dpos_bb[1], hi)]]
        if evals % 200000 == 0:
            print("progress", evals, counts, stats, round(time.time() - t0, 1), flush=True)
        if evals > spec["eval_cap"]:
            capped = True
            break
    if capped:
        print("EVAL CAP REACHED; stopping without conclusion", flush=True)
        break
gz.close()
summary = {"spec": spec["name"], "counts": counts, "stats": stats, "evaluations": evals, "cells": len(cells),
           "eval_cap_hit": capped, "depth_histogram": {str(k): v for k, v in sorted(depth_hist.items())},
           "fails_first50": fails, "dpos_bounding_box_float": dpos_bb, "leaf_lines_sha256": hasher.hexdigest(),
           "certificate_ok": counts["FAIL"] == 0 and not capped, "elapsed_seconds": round(time.time() - t0, 2)}
with lane_guard.xopen(RUN + "/primal.json") as fh:
    json.dump(summary, fh, indent=1)
print("SUMMARY", json.dumps(summary))

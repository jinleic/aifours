#!/usr/bin/env python3
"""diag_g_v1.py -- DIAGNOSTIC ONLY (no certificate): why dualcheck_v1's G tests fail on early d01-G leaves.

For the first K CERT leaves of each requested G cell: v1 naive radial upper bound, v1 MVF bound, F(mid), gradient
enclosures, half-widths, a corner-sampled F maximum (ball values at the 8 corners and the midpoint; not a bound), and
the same naive bound computed from a centred-form W enclosure.  Writes OUT (exclusive).
Usage: python -I -B diag_g_v1.py PIN.json OUT.json K CELL [CELL ...]
"""
import sys
import os
import json
import gzip
import time
import itertools

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dualcheck_v1 as D  # noqa: E402
from flint import arb, acb, fmpq  # noqa: E402

PIN, OUT, K = sys.argv[1], sys.argv[2], int(sys.argv[3])
CELLS = [int(c) for c in sys.argv[4:]]
pin = json.load(open(PIN))
ent = pin["charts"]["G"]
sh, _ = D.sha256_file(ent["leaves"]["path"])
assert sh == ent["leaves"]["sha256"]
spec = json.load(open(ent["spec"]["path"]))
kind, cells, wts, maxdepth, problems = D.load_chart(spec, "G")
C = D.Ctx(fmpq(11, 50))
want = {c: [] for c in CELLS}
with gzip.open(ent["leaves"]["path"], "rt") as fh:
    for ln in fh:
        c = int(ln.split(" ", 1)[0])
        if c in want and len(want[c]) < K:
            want[c].append(ln.split())
        if c > max(CELLS):
            break


def F_point(sq, dq, wq, br):
    W = D.g_point_W(C, sq, dq, wq)
    if not D.branch_holds(W, br):
        return None
    return arb(wq) * abs(W).log() + arb(dq) * D.alpha_on(C, W, br)


def f(x, n=6):
    return x.str(n, radius=False) if x is not None else None


rows = []
t0 = time.time()
for c in CELLS:
    dims = D.split_dims(cells[c], wts, maxdepth + 1)
    for ci, path, tag in want[c]:
        if not tag.startswith("CERT"):
            continue
        p = "" if path == "-" else path
        box = D.leaf_box(cells[c], dims, p)
        (sl, sh_), (dl, dh), (wl, wh) = box
        s, d, w = D.I(sl, sh_), D.I(dl, dh), D.I(wl, wh)
        z = acb(1 + d, -w)
        W = D.Wfun(C, s, D.ONE / z)
        aW = abs(W)
        br = D.pick_branch(W)
        row = {"cell": c, "path": path, "tag": tag, "depth": len(p), "branch": br,
               "W_rad": [f(W.real.rad() if hasattr(W.real, "rad") else None, 3)],
               "small_rhs": f((-C.TWOPI * arb(dh) / arb(wl)).exp()), "absW": f(aW)}
        ok, how = D.ev_G(C, box)
        row["v1"] = [ok, how]
        if br is not None:
            alpha = D.alpha_on(C, W, br)
            F = w * aW.log() + d * alpha
            row["F_naive_upper"] = f(arb(F.upper()))
            # MVF pieces
            K_ = C.K
            one_s = 1 - s
            q = K_ * s * s * z * z - 2 * s * one_s * z + 2 * one_s * one_s
            N1 = K_ * s * s - 2 * s * one_s + 2 * one_s * one_s
            qz = 2 * K_ * s * s * z - 2 * s * one_s
            qs = 2 * K_ * s * z * z - 2 * (1 - 2 * s) * z - 4 * one_s
            N1s = 2 * K_ * s - 2 * (1 - 2 * s) - 4 * one_s
            L = qz / q - 3 / z
            Ls = qs / q - N1s / N1
            dFs = w * Ls.real + d * Ls.imag
            dFd = w * L.real + alpha + d * L.imag
            dFw = aW.log() + w * L.imag - d * L.real
            m, h = D.mids_halfwidths(box)
            FM = F_point(m[0], m[1], m[2], br)
            row["F_mid"] = f(FM)
            row["grad_abs_upper"] = [f(arb(abs(x).upper()), 3) for x in (dFs, dFd, dFw)]
            row["h"] = [f(x, 3) for x in h]
            row["mvf_terms"] = [f(arb((abs(x) * hh).upper()), 3) for x, hh in zip((dFs, dFd, dFw), h)]
            corners = []
            for a_, b_, c_ in itertools.product((sl, sh_), (dl, dh), (wl, wh)):
                v = F_point(a_, b_, c_, br)
                if v is not None:
                    corners.append(float(v.mid()))
            row["F_corner_max_float"] = max(corners) if corners else None
            # centred-form W: W(m) + sum dW/dx_j(box) [-h_j, h_j], dW = W*(Ls, L, -i L)
            WM = D.g_point_W(C, m[0], m[1], m[2])
            gW = [W * Ls, W * L, W * L * acb(0, -1)]
            Wc = WM
            for gj, hj in zip(gW, h):
                rr = arb(abs(gj).upper()) * hj
                Wc = Wc + acb(arb(0, rr.upper()) if False else arb(0).union(rr).union(-rr), arb(0).union(rr).union(-rr))
            row["Wc_rad_vs_naive"] = [f(arb(abs(Wc - WM).upper()), 3), f(arb(abs(W - WM).upper()), 3)]
            if D.branch_holds(Wc, br):
                alc = D.alpha_on(C, Wc, br)
                Fc = w * abs(Wc).log() + d * alc
                row["F_centred_upper"] = f(arb(Fc.upper()))
        rows.append(row)
res = {"tool": "diag_g_v1.py", "cells": CELLS, "K": K, "rows": rows, "seconds": round(time.time() - t0, 2),
       "note": "diagnostic only; corner maxima are float samples, not bounds"}
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print("rows", len(rows), "v1_fail", sum(1 for r in rows if not r["v1"][0]), "seconds", res["seconds"])

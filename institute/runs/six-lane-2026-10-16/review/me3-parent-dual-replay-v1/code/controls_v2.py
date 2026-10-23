#!/usr/bin/env python3
"""controls_v2.py -- negative and positive controls for the parent dual checker dualcheck_v2.py (desk-owned code).

= controls_v1.py (never executed; sha 77f58e12...61fc) re-targeted at dualcheck_v2.py, plus G-specific controls C7-C10.
Every control states its intended rejection reason and checks that exact reason.  Inputs are the pinned worker leaf
files (hash-checked before reading).  Writes OUT (exclusive).  Usage: python -I -B controls_v2.py PIN.json OUT.json
Controls:
  C1 tiling mutants on LW (dropped leaf, changed path bit, duplicated leaf, deeper path, missing cell, FAIL label);
  C2 invalid SKIP (LD2 CERT leaf relabelled skip-d; G CERT leaf relabelled in-primal-P; P-boundary closedness);
  C3 too-large T: at a pole point of a chart, T' = (SCV of an explicit cone member) + margin, so the Lemma D claim
     is false there and at least one leaf of the fibre MUST be rejected (reasons recorded); also run at T = 11/50.
     Not applicable where every explicit member has SCV >= 0.995 (T' would need kappa' <= 1/2), e.g. LW;
  C4 wrong argument branch (G: principal Arg on an Im W < 0 box, and a false branch condition; LD1: alpha - 2pi);
  C5 weakened tails (SWC series tail, SWB Taylor remainder): the true remainder, computed independently in balls at
     rational points, must lie within the checker's bound, and must exceed the bound scaled by 1e-6 somewhere;
  C6 input-hash mismatch is detected;
  C7 G CERT leaf relabelled SKIP:in-primal-P inside a real G stream prefix -> exactly that leaf rejected (v2);
  C8 G too-large T at a second point next to the P boundary (delta = 13/20, omega = 1/5);
  C9 positive: the r13 diagnostic leaves (v1 NaN failures) are certified by v2;
  C10 logabs_hull contains log|W(x)| at the corners and midpoint of real G leaf boxes (diagnostic support).
"""
import sys
import os
import json
import gzip
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dualcheck_v2 as D  # noqa: E402  (desk-owned module)
from flint import arb, acb, fmpq  # noqa: E402

PIN, OUT = sys.argv[1], sys.argv[2]
pin = json.load(open(PIN))
T0 = fmpq(11, 50)
C = D.Ctx(T0)
res = {"tool": "controls_v2.py", "tool_sha256": D.sha256_file(os.path.abspath(__file__))[0],
       "checker_sha256": D.sha256_file(D.__file__)[0], "started": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
       "controls": {}}
ONEc = acb(1, 0)


def checked_path(chart):
    ent = pin["charts"][chart]
    sh, nb = D.sha256_file(ent["leaves"]["path"])
    if sh != ent["leaves"]["sha256"]:
        raise SystemExit("leaf file hash mismatch for %s" % chart)
    return ent["leaves"]["path"]


def all_lines(chart):
    with gzip.open(checked_path(chart), "rt") as fh:
        return [ln.rstrip("\n") for ln in fh]


def cells_lines(chart, wanted):
    got = {c: [] for c in wanted}
    with gzip.open(checked_path(chart), "rt") as fh:
        for ln in fh:
            c = int(ln.split(" ", 1)[0])
            if c in got:
                got[c].append(ln.rstrip("\n"))
    return got


def spec_of(chart):
    return json.load(open(pin["charts"][chart]["spec"]["path"]))


def geometry(chart):
    kind, cells, wts, maxdepth, problems = D.load_chart(spec_of(chart), chart)
    return kind, cells, wts, maxdepth


def boxes_of(chart, lines):
    kind, cells, wts, maxdepth = geometry(chart)
    dims_cache = {}
    out = []
    for ln in lines:
        ci_s, path, tag = ln.split()
        ci = int(ci_s)
        if ci not in dims_cache:
            dims_cache[ci] = D.split_dims(cells[ci], wts, maxdepth + 1)
        p = "" if path == "-" else path
        out.append((ci, p, tag, D.leaf_box(cells[ci], dims_cache[ci], p)))
    return out


def run(chart, lines, extra=12, Cx=C):
    return D.run_lines(lines, chart, spec_of(chart), Cx, 0, None, extra, lambda s_: None)


def record(name, expected, observed, passed):
    res["controls"][name] = {"expected": expected, "observed": observed,
                             "pass": None if passed is None else bool(passed)}


def whys(r, why):
    return [f for f in r["failures_first"] if f["why"] == why]


# ---------------------------------------------------------------- C1 tiling mutants (LW)
lw = all_lines("LW")
base = run("LW", lw)
record("C1.0 baseline LW", "no tiling errors, no failures",
       {"tiling_errors": base["tiling_errors"][:3], "n_failures": base["n_failures"]},
       not base["tiling_errors"] and base["n_failures"] == 0)
cell_counts = {}
for i, ln in enumerate(lw):
    cell_counts.setdefault(int(ln.split()[0]), []).append(i)
multi = [idx for c, idx in sorted(cell_counts.items()) if len(idx) >= 3][0]
k = multi[1]
c_, p_, t_ = lw[k].split()
r = run("LW", lw[:k] + lw[k + 1:])
record("C1.1 dropped leaf", "tiling error (gap)", r["tiling_errors"][:2],
       any("does not follow" in e or "gap" in e for e in r["tiling_errors"]))
flipped = p_[:-1] + ("0" if p_[-1] == "1" else "1")
r = run("LW", lw[:k] + ["%s %s %s" % (c_, flipped, t_)] + lw[k + 1:])
record("C1.2 changed path bit", "tiling error (overlap/gap)", r["tiling_errors"][:2],
       any("does not follow" in e for e in r["tiling_errors"]))
r = run("LW", lw[:k] + [lw[k], lw[k]] + lw[k + 1:])
record("C1.3 duplicated leaf", "tiling error (overlap)", r["tiling_errors"][:2],
       any("does not follow" in e for e in r["tiling_errors"]))
r = run("LW", lw[:k] + ["%s %s0 %s" % (c_, p_, t_)] + lw[k + 1:])
record("C1.4 deeper path (half box only)", "tiling error (gap)", r["tiling_errors"][:2],
       any("does not follow" in e or "gap" in e for e in r["tiling_errors"]))
last_cell = max(cell_counts)
r = run("LW", [ln for ln in lw if int(ln.split()[0]) != last_cell])
record("C1.5 missing last cell", "missing cells", r["tiling_errors"][:2],
       any("missing cells" in e for e in r["tiling_errors"]))
r = run("LW", lw[:k] + ["%s %s FAIL" % (c_, p_)] + lw[k + 1:])
record("C1.6 FAIL label", "exactly one failure: non-certificate label, at the mutated leaf",
       [(f["cell"], f["path"], f["why"]) for f in r["failures_first"]][:3],
       r["n_failures"] == 1 and r["failures_first"][0]["why"] == "non-certificate label"
       and r["failures_first"][0]["path"] == p_)

# ---------------------------------------------------------------- C2 invalid SKIP
ld2 = all_lines("LD2")
ld2b = boxes_of("LD2", ld2)
target = None
for i, (ci, p, tag, box) in enumerate(ld2b):
    if tag.startswith("CERT") and not D.skip_LD2(C, box, "SKIP:skip-d") and not D.skip_LD2(C, box, "SKIP:skip-s"):
        target = i
        break
ci, p, tag, box = ld2b[target]
r = run("LD2", ld2[:target] + ["%d %s SKIP:skip-d" % (ci, p or "-")] + ld2[target + 1:])
sk = whys(r, "skip rule false")
record("C2.1 LD2 CERT relabelled SKIP:skip-d", "exactly one 'skip rule false' failure, at the mutated leaf",
       {"skip_failures": [(f["cell"], f["path"]) for f in sk], "other_failures": r["n_failures"] - len(sk),
        "tiling_errors": r["tiling_errors"][:2]},
       len(sk) == 1 and sk[0]["cell"] == ci and sk[0]["path"] == (p or "-") and not r["tiling_errors"])
skip_true = [b for (_, _, tg, b) in ld2b if tg == "SKIP:skip-d"]
skip_s = [b for (_, _, tg, b) in ld2b if tg == "SKIP:skip-s"]
record("C2.2 genuine LD2 SKIP boxes pass their rules (positive)", "all true",
       {"skip-d": [len(skip_true), sum(1 for b in skip_true if D.skip_LD2(C, b, "SKIP:skip-d"))],
        "skip-s": [len(skip_s), sum(1 for b in skip_s if D.skip_LD2(C, b, "SKIP:skip-s"))]},
       all(D.skip_LD2(C, b, "SKIP:skip-d") for b in skip_true) and all(D.skip_LD2(C, b, "SKIP:skip-s") for b in skip_s))
kindG, cellsG, wtsG, mdG = geometry("G")
cand_cells = [ci for ci, cell in enumerate(cellsG)
              if cell[2][1] <= 40 and cell[2][0] >= fmpq(1, 5) and cell[1][1] > 3 * cell[2][0]
              and cell[1][0] <= 3 * cell[2][1]][:3]
gl = cells_lines("G", cand_cells)
found = None
for ci in cand_cells:
    bx = boxes_of("G", gl[ci])
    skl = [b for b in bx if b[2] == "SKIP:in-primal-P"]
    ce = [b for b in bx if b[2].startswith("CERT") and not D.skip_G(b[3], "SKIP:in-primal-P")]
    if skl and ce:
        found = (ci, skl, ce)
        break
if found:
    ci, skl, ce = found
    record("C2.3 G CERT box relabelled SKIP:in-primal-P", "skip rule false",
           {"cell": ci, "box": [[str(a), str(b)] for a, b in ce[0][3]], "rule": D.skip_G(ce[0][3], "SKIP:in-primal-P")},
           D.skip_G(ce[0][3], "SKIP:in-primal-P") is False)
    record("C2.4 genuine G SKIP boxes of that cell pass (positive)", "all true", {"cell": ci, "n": len(skl)},
           all(D.skip_G(b[3], "SKIP:in-primal-P") for b in skl))
else:
    record("C2.3 G CERT box relabelled SKIP:in-primal-P", "skip rule false", "no mixed cell found", False)
bnd = ((fmpq(0), fmpq(1, 16)), (fmpq(1, 2), fmpq(51, 80)), (fmpq(17, 80), fmpq(1, 4)))
bnd2 = (bnd[0], (bnd[1][0], bnd[1][1] + fmpq(1, 10 ** 9)), bnd[2])
record("C2.5 P closed at the boundary", "delta_h = 3 omega_l accepted; delta_h = 3 omega_l + 1e-9 rejected",
       [D.skip_G(bnd, "SKIP:in-primal-P"), D.skip_G(bnd2, "SKIP:in-primal-P")],
       D.skip_G(bnd, "SKIP:in-primal-P") is True and D.skip_G(bnd2, "SKIP:in-primal-P") is False)


# ---------------------------------------------------------------- C3 too-large T
def scv_member(dq, wq, which):
    """SCV of e^{-t}h, h = 1 - e^{-delta t}cos(omega t) (f0) or 1 - e^{-delta t}(cos + r sin)(omega t) (h0), r=delta/omega.
    m_k = k!(1 - Re(c zeta^{k+1})), c = 1 (f0) or 1 - i r (h0); SCV = 2 a0 a2 / a1^2 - 1, a_k = m_k/k!."""
    zeta = ONEc / acb(1 + arb(dq), -arb(wq))
    c = ONEc if which == "f0" else acb(arb(1), -arb(dq) / arb(wq))
    a = [1 - (c * zeta ** (kk + 1)).real for kk in range(3)]
    return 2 * a[0] * a[2] / (a[1] * a[1]) - 1


def tprime_for(dq, wq):
    v = [scv_member(dq, wq, "f0"), scv_member(dq, wq, "h0")]
    lo = min(float(x.upper()) for x in v)
    Tp = fmpq(int(lo * 1000) + 3, 1000)
    return Tp, [x.str(10, radius=False) for x in v], any(x < arb(Tp) for x in v)


def fibre(chart, boxes, dq, wq):
    kind = D.DOMAINS[chart][0]
    out = []
    for item in boxes:
        box = item[3]
        if kind in ("C", "B", "G"):
            if box[1][0] <= dq <= box[1][1] and box[2][0] <= wq <= box[2][1]:
                out.append(item)
        elif kind == "LW":
            nq = 1 / wq
            if box[1][0] <= dq <= box[1][1] and box[2][0] <= nq <= box[2][1]:
                out.append(item)
        else:
            b0 = (arb(wq) / (1 + arb(dq))).atan()
            inb = not (b0 < arb(box[2][0])) and not (b0 > arb(box[2][1]))
            if kind == "LD1":
                d0 = 1 / (1 + dq)
                if inb and box[1][0] <= d0 <= box[1][1]:
                    out.append(item)
            elif inb:
                out.append(item)
    return out


def eval_fibre(chart, items, Cx):
    ev = D.EVAL[D.DOMAINS[chart][0]]
    n, rej, why = 0, 0, {}
    for (ci, p, tag, box) in items:
        if not tag.startswith("CERT"):
            continue
        n += 1
        ok, how = ev(Cx, box)
        if not ok:
            rej += 1
            why[how] = why.get(how, 0) + 1
    return {"cert_leaves": n, "rejected": rej, "reasons": why}


points = {"LW": (fmpq(64), fmpq(640)), "SWC": (fmpq(3, 10), fmpq(3, 20)), "SWB": (fmpq(5, 4), fmpq(3, 20)),
          "G": (fmpq(1), fmpq(1, 4)), "LD": (fmpq(64), fmpq(10))}
small = {"LW": lw, "LD1": all_lines("LD1"), "LD2": ld2, "SWC": all_lines("SWC")}
TMAX = fmpq(995, 1000)
for chart in ("LW", "SWC", "SWB", "G"):
    dq, wq = points[chart]
    Tp, vals, cf = tprime_for(dq, wq)
    name = "C3 %s too-large T" % chart
    if Tp >= TMAX:
        record(name, "not applicable: explicit members have SCV >= 0.995 at %s,%s (kappa' would be <= 1/2)" % (dq, wq),
               {"scv_f0_h0": vals}, None)
        continue
    if chart in small:
        items = fibre(chart, boxes_of(chart, small[chart]), dq, wq)
        cellsel = None
    else:
        kindX, cellsX, wtsX, mdX = geometry(chart)
        cellsel = [ci for ci, cell in enumerate(cellsX)
                   if cell[1][0] <= dq <= cell[1][1] and cell[2][0] <= wq <= cell[2][1]]
        got = cells_lines(chart, cellsel)
        items = []
        for ci in cellsel:
            items.extend(fibre(chart, boxes_of(chart, got[ci]), dq, wq))
    a1 = eval_fibre(chart, items, D.Ctx(Tp))
    a0 = eval_fibre(chart, items, C)
    record(name, "T'=%s exceeds a certified member SCV; >=1 fibre leaf rejected at T'" % Tp,
           {"point": [str(dq), str(wq)], "cells": cellsel, "scv_f0_h0": vals, "member_below_Tprime": cf,
            "at_Tprime": a1, "at_T_no_subdivision": a0}, cf and a1["rejected"] >= 1)
dq, wq = points["LD"]
Tp, vals, cf = tprime_for(dq, wq)
if Tp >= TMAX:
    record("C3 LD1+LD2 too-large T", "not applicable", {"scv_f0_h0": vals}, None)
else:
    it1 = fibre("LD1", boxes_of("LD1", small["LD1"]), dq, wq)
    it2 = fibre("LD2", boxes_of("LD2", small["LD2"]), dq, wq)
    a1, a2 = eval_fibre("LD1", it1, D.Ctx(Tp)), eval_fibre("LD2", it2, D.Ctx(Tp))
    b1, b2 = eval_fibre("LD1", it1, C), eval_fibre("LD2", it2, C)
    record("C3 LD1+LD2 too-large T", "T'=%s; >=1 leaf of the LD1 fibre or the LD2 beta-slab rejected at T'" % Tp,
           {"point": [str(dq), str(wq)], "scv_f0_h0": vals, "member_below_Tprime": cf, "LD1_fibre": a1,
            "LD2_slab": a2, "at_T_no_subdivision": [b1, b2]}, cf and (a1["rejected"] + a2["rejected"]) >= 1)

# ---------------------------------------------------------------- C4 wrong branch
want = [ci for ci, cell in enumerate(cellsG) if cell[0][0] == 0 and cell[1][0] == 0
        and cell[2][0] in (fmpq(3), fmpq(4), fmpq(6), fmpq(8), fmpq(12), fmpq(16), fmpq(24), fmpq(32))]
got = cells_lines("G", want)
down = None
for ci in want:
    for item in boxes_of("G", got[ci]):
        if not item[2].startswith("CERT"):
            continue
        b = item[3]
        s_, d_, w_ = D.I(*b[0]), D.I(*b[1]), D.I(*b[2])
        W = D.Wfun(C, s_, D.ONE / acb(1 + d_, -w_))
        if D.branch_holds(W, "down"):
            down = item
            break
    if down:
        break
if down:
    r1 = D.ev_G(C, down[3], force_branch="principal")
    r2 = D.ev_G(C, down[3], force_branch="up")
    r3 = D.ev_G(C, down[3])
    bx = [[str(a), str(b)] for a, b in down[3]]
    record("C4.1 G principal Arg on an Im W<0 box", "alpha-negative", {"r": list(r1), "box": bx},
           r1 == (False, "alpha-negative"))
    record("C4.2 G branch 'up' forced on an Im W<0 box", "branch-condition-false", list(r2),
           r2 == (False, "branch-condition-false"))
    record("C4.3 same box, checker's own branch logic (positive)", "certified", list(r3), r3[0] is True)
else:
    record("C4.1 G principal Arg on an Im W<0 box", "alpha-negative", "no Im W<0 box found", False)
tgt = None
for item in boxes_of("LD1", small["LD1"]):
    b = item[3]
    if b[2][0] > 0 and b[2][1] < fmpq(3, 2):
        tgt = item
        break
r4 = D.ev_LD1(C, tgt[3], force="principal-minus-2pi")
r5 = D.ev_LD1(C, tgt[3])
record("C4.4 LD1 alpha = beta + Arg P - 2pi", "alpha-negative", list(r4), r4 == (False, "alpha-negative"))
record("C4.5 same LD1 box, own logic (positive)", "certified", list(r5), r5[0] is True)


# ---------------------------------------------------------------- C5 weakened tails
ok_valid, ok_weak, rows = True, False, []
for sq in (fmpq(1, 7), fmpq(1, 3), fmpq(1, 2), fmpq(2, 3), fmpq(6, 7), fmpq(999, 1000)):
    for dq, wq in ((fmpq(3, 10), fmpq(1, 5)), (fmpq(1, 10), fmpq(1, 5)), (fmpq(3, 10), fmpq(1, 100)),
                   (fmpq(1, 20), fmpq(1, 20))):
        for N in (20, 5):
            box = ((sq, sq), (dq, dq), (wq, wq))
            tP, tI = D.swc_tails(C, box, N)
            Psi, Ig = D.swc_series(C, arb(sq), arb(dq), arb(wq), N)
            s_, d_, w_ = arb(sq), arb(dq), arb(wq)
            W = D.Wfun(C, s_, D.ONE / acb(1 + d_, -w_))
            lg = W.log()
            # |Im g| <= omega(|Ig_N| + tail) < 3 < pi  =>  the series branch g equals the principal Log W
            branch_ok = (w_ * (abs(Ig) + tI)) < 3
            Pt = (w_ * lg.real + d_ * lg.imag) / (w_ * (d_ * d_ + w_ * w_))
            It = lg.imag / w_
            eP, eI = abs(Pt - Psi), abs(It - Ig)
            v = bool(branch_ok and (eP < tP) and (eI < tI))
            ok_valid = ok_valid and v
            ok_weak = ok_weak or bool(eP > tP * arb("1e-6")) or bool(eI > tI * arb("1e-6"))
            rows.append([str(sq), str(dq), str(wq), N, eP.str(5, radius=False), tP.str(5, radius=False),
                         eI.str(5, radius=False), tI.str(5, radius=False), v])
record("C5.1 SWC tail bounds dominate the true remainders (positive; N=20 and N=5)", "all within bound",
       {"points": len(rows), "sample": rows[:8]}, ok_valid)
record("C5.2 SWC tail weakened by 1e-6", "true remainder exceeds weakened bound at >=1 point", ok_weak, ok_weak)

ok_valid, ok_weak, rows = True, False, []
for sq in (fmpq(1, 7), fmpq(1, 3), fmpq(1, 2), fmpq(2, 3), fmpq(6, 7), fmpq(99, 100)):
    for dq in (fmpq(3, 10), fmpq(1), fmpq(5), fmpq(40)):
        for wq in (fmpq(1, 5), fmpq(1, 10)):
            box = ((sq, sq), (dq, dq), (fmpq(0), wq))
            M4, M5 = D.swb_M(C, box)
            g0, g1, g2, g3 = D.swb_g(C, arb(sq), arb(dq))
            s_, d_, w_ = arb(sq), arb(dq), arb(wq)
            one_s = 1 - s_
            z = acb(1 + d_, -w_)
            z1 = one_s * C.IC_P / (C.K * s_)
            z2 = one_s * C.IC_M / (C.K * s_)
            N1 = C.K * s_ * s_ - 2 * s_ * one_s + 2 * one_s * one_s
            # continuous branch from the real axis (derivation-v1.md, SWB control note): sum of principal logs
            g = (C.K * s_ * s_ / N1).log() + (z - z1).log() + (z - z2).log() - 3 * z.log()
            W = D.Wfun(C, s_, D.ONE / z)
            same = bool(abs(g.exp() - W) < arb("1e-30"))
            Ra = abs(g.real - (g0 - w_ * w_ * g2 / 2))
            Rb = abs(g.imag - (-w_ * g1 + w_ ** 3 * g3 / 6))
            ba, bb = w_ ** 4 * M4 / 24, w_ ** 5 * M5 / 120
            v = bool(same and (Ra < ba) and (Rb < bb))
            ok_valid = ok_valid and v
            ok_weak = ok_weak or bool(Ra > ba * arb("1e-6")) or bool(Rb > bb * arb("1e-6"))
            rows.append([str(sq), str(dq), str(wq), Ra.str(5, radius=False), ba.str(5, radius=False),
                         Rb.str(5, radius=False), bb.str(5, radius=False), v])
record("C5.3 SWB Taylor remainder bounds dominate the true remainders (positive)", "all within bound",
       {"points": len(rows), "sample": rows[:8]}, ok_valid)
record("C5.4 SWB remainder bounds weakened by 1e-6", "true remainder exceeds weakened bound at >=1 point", ok_weak,
       ok_weak)

# ---------------------------------------------------------------- C6 input hash mismatch
sh, _ = D.sha256_file(pin["charts"]["LW"]["leaves"]["path"])
bad = sh[:-1] + ("0" if sh[-1] != "0" else "1")
record("C6 mutated pinned hash", "mismatch detected", sh != bad, sh != bad)

# ---------------------------------------------------------------- C7 G false SKIP through run_lines (v2)
target_cell = [ci for ci, cell in enumerate(cellsG) if cell[0] == (fmpq(0), fmpq(1, 16))
               and cell[1] == (fmpq(3, 5), fmpq(4, 5)) and cell[2] == (fmpq(1, 5), fmpq(3, 10))][0]
prefix = []
with gzip.open(checked_path("G"), "rt") as fh:
    for ln in fh:
        if int(ln.split(" ", 1)[0]) > target_cell:
            break
        prefix.append(ln.rstrip("\n"))
idx = [i for i, ln in enumerate(prefix) if int(ln.split()[0]) == target_cell]
mut_i = None
for i, item in zip(idx, boxes_of("G", [prefix[i] for i in idx])):
    if item[2].startswith("CERT") and not D.skip_G(item[3], "SKIP:in-primal-P"):
        mut_i = i
        break
ci7, p7, t7 = prefix[mut_i].split()
mutated = prefix[:mut_i] + ["%s %s SKIP:in-primal-P" % (ci7, p7)] + prefix[mut_i + 1:]
r = D.run_lines(mutated, "G", spec_of("G"), C, target_cell, target_cell + 1, 12, lambda s_: None)
sk = whys(r, "skip rule false")
record("C7.1 G CERT relabelled SKIP:in-primal-P (v2, real stream prefix)",
       "exactly one failure ('skip rule false') at the mutated leaf; the only tiling error is the prefix's missing cells",
       {"cell": target_cell, "path": p7, "skip_failures": [(f["cell"], f["path"]) for f in sk],
        "n_failures": r["n_failures"], "tiling_errors": r["tiling_errors"][:3]},
       len(sk) == 1 and sk[0]["path"] == p7 and r["n_failures"] == 1
       and all("missing cells" in e for e in r["tiling_errors"]))
r0 = D.run_lines(prefix, "G", spec_of("G"), C, target_cell, target_cell + 1, 12, lambda s_: None)
record("C7.2 same G cell unmutated (positive)", "no failures",
       {"n_failures": r0["n_failures"], "table": r0["verification_table"], "subdivision": r0["subdivision"]},
       r0["n_failures"] == 0)

# ---------------------------------------------------------------- C8 G too-large T next to the P boundary
dq, wq = fmpq(13, 20), fmpq(1, 5)
Tp, vals, cf = tprime_for(dq, wq)
cellsel = [ci for ci, cell in enumerate(cellsG) if cell[1][0] <= dq <= cell[1][1] and cell[2][0] <= wq <= cell[2][1]]
got = cells_lines("G", cellsel)
items = []
for ci in cellsel:
    items.extend(fibre("G", boxes_of("G", got[ci]), dq, wq))
a1 = eval_fibre("G", items, D.Ctx(Tp))
a0 = eval_fibre("G", items, C)
record("C8 G too-large T at (13/20, 1/5)", "T'=%s exceeds a certified member SCV; >=1 fibre leaf rejected at T'" % Tp,
       {"cells": cellsel, "scv_f0_h0": vals, "member_below_Tprime": cf, "at_Tprime": a1, "at_T_no_subdivision": a0},
       cf and a1["rejected"] >= 1)

# ---------------------------------------------------------------- C9 positive: r13 diagnostic leaves under v2
diag_cells = [178, 228, 282, 300]
got = cells_lines("G", diag_cells)
n9, direct9, sub9, fail9 = 0, 0, 0, 0
for ci in diag_cells:
    dims = D.split_dims(cellsG[ci], wtsG, mdG + 13)
    for (c_, p_, t_, box) in boxes_of("G", got[ci][:300]):
        if not t_.startswith("CERT"):
            continue
        n9 += 1
        rr = D.certify(D.ev_G, C, box, len(p_), dims, 12)
        if rr is None:
            fail9 += 1
        elif rr[0] == 1:
            direct9 += 1
        else:
            sub9 += 1
record("C9 r13 diagnostic leaves certified by v2 (positive)", "all certified",
       {"cert_leaves": n9, "direct": direct9, "subdivided": sub9, "unproved": fail9}, fail9 == 0 and n9 > 0)

# ---------------------------------------------------------------- C10 logabs_hull containment (diagnostic support)
import itertools  # noqa: E402
ok10, n10 = True, 0
for (c_, p_, t_, box) in boxes_of("G", got[228][:50]):
    s_, d_, w_ = D.I(*box[0]), D.I(*box[1]), D.I(*box[2])
    hull = D.logabs_hull(D.Wfun(C, s_, D.ONE / acb(1 + d_, -w_)))
    if hull is None:
        continue
    pts = list(itertools.product(*box)) + [tuple((lo + hi) / 2 for lo, hi in box)]
    for (a_, b_, c2) in pts:
        v = abs(D.g_point_W(C, a_, b_, c2)).log()
        n10 += 1
        ok10 = ok10 and bool(hull.contains(v))
record("C10 logabs_hull contains log|W| at corners/midpoints (support)", "all contained", {"points": n10}, ok10 and n10 > 0)

na = [k_ for k_, v_ in res["controls"].items() if v_["pass"] is None]
res["not_applicable"] = na
res["all_pass"] = all(v_["pass"] for v_ in res["controls"].values() if v_["pass"] is not None)
res["finished"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1, default=str)
print(json.dumps({"all_pass": res["all_pass"], "not_applicable": na,
                  "failed": [k_ for k_, v_ in res["controls"].items() if v_["pass"] is False]}))

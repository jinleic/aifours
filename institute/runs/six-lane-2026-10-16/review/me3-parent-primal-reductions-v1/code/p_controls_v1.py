"""ME3 parent desk (ME3ParentPrimal): in-memory mutation controls for the primal-chart replay (p_core_v1).

Usage: p_controls_v1.py RUN_DIR LEAVES LEAVES_SHA SPEC SPEC_SHA LAST_CELL
Reads the leaf stream in place up to cell LAST_CELL (complete cells only; no copy is written), then:
  C0  positive control: the unmutated in-memory cells pass coverage and verification (recorded subdivision allowed,
      exactly as in the full replay);
  C1a altered derivative sign (a_k' -> -a_k'): every DPOS leaf must be rejected at DPOS (also after extra bisection);
  C1b altered sign of one term of D (a0 a1 a2' -> -a0 a1 a2'): DPOS leaves must be rejected at DPOS (count > 0);
  C2  false infeasibility: relabelled leaves must be rejected by the INFEAS rule at the intended clause
      (a) r_lo = 0 -> DOMAIN_R_LO, (b) phi_lo <= pi -> DOMAIN_PHI_LO, (c) feasible corner -> G_NOT_GT_1,
      (d) real INFEAS leaves with phi_lo lowered below theta1(r_lo) -> G_NOT_GT_1;
  C3  coverage mutations: missing / duplicated / path-flipped / wrong-cell / dropped-cell leaves must be rejected
      at the intended COVER rule;
  C4  weakened bound: (a) per-leaf T' = S(mid) + 1e-6 must reject every tested SGE leaf (also after bisection),
      (b) T' = 1/4 must reject a positive number of SGE leaves, (c) DPOS leaves relabelled SGE with S(mid) < T must
      be rejected at SGE;
  C5  a FAIL label is never accepted.
Writes RUN_DIR/RESULT.json (exclusive create).
"""
import sys
import os
import re
import json
import gzip
import time
import hashlib
from fractions import Fraction
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp  # noqa: E402
import p_core_v1 as C  # noqa: E402

LINE = re.compile(rb"^(0|[1-9][0-9]*) (-|[01]+) (SGE|DPOS|INFEAS|FAIL)\n$")
T = Fraction(11, 50)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


class MutTerm(C.Evaluator):
    """C1b: D' = a0' a1 a2 - a0 a1 a2' - 2 a0 a1' a2 (one sign altered), with its consistent gradient."""

    def D_val(self, r, w, p):
        a, d, D, P, z = super().D_val(r, w, p)
        return a, d, D - 2 * a[0] * a[1] * d[2], P, z

    def grad_D(self, balls, a, d, P, z):
        dD, dd, da = super().grad_D(balls, a, d, P, z)
        out = [dD[j] - 2 * (da[0][j] * a[1] * d[2] + a[0] * da[1][j] * d[2] + a[0] * a[1] * dd[2][j])
               for j in range(3)]
        return out, dd, da


def main():
    run, leafp, leaf_sha, specp, spec_sha, last_cell = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], \
        sys.argv[5], int(sys.argv[6])
    t0 = time.time()
    res = {"script": "p_controls_v1.py", "argv": sys.argv[1:]}
    pre = {"leaves": sha256_file(leafp), "spec": sha256_file(specp)}
    res["pre_hashes"] = pre
    assert pre["leaves"] == leaf_sha and pre["spec"] == spec_sha, pre
    spec = json.load(open(specp))
    lines = []
    with gzip.open(leafp, "rb") as fh:
        for raw in fh:
            m = LINE.match(raw)
            ci = int(m.group(1))
            if ci > last_cell:
                break
            path = m.group(2).decode()
            lines.append((ci, "" if path == "-" else path, m.group(3).decode()))
    res["sample"] = {"cells": last_cell + 1, "leaves": len(lines)}
    ev = C.Evaluator(T, int(spec["prec"]))
    controls = {}

    def cover_run(seq):
        g = C.Geometry(spec)
        boxes = []
        errs = []
        for ci, path, out in seq:
            box, e = g.feed(ci, path)
            errs.extend(e)
            boxes.append(box)
        if g.stack and not g.bad_cell:
            errs.append(f"COVER:INCOMPLETE_CELL cell {g.cur} (end of sample)")
        if g.cells_seen != last_cell + 1 or g.cur != last_cell:
            errs.append(f"COVER:CELLS seen {g.cells_seen} last {g.cur} expected {last_cell + 1}")
        return boxes, errs, g

    # ---- C0 positive control --------------------------------------------------------------------------------------
    boxes, errs, geom = cover_run(lines)
    n_ok = 0
    n_sub = 0
    bad = []
    for (ci, path, out), box in zip(lines, boxes):
        ok, how = ev.verify(box, out)
        if not ok and out in ("SGE", "DPOS"):
            sok, nsub, deep, first = ev.verify_subdiv(box, out, geom, 12)
            if sok:
                ok = True
                n_sub += 1
        if ok:
            n_ok += 1
        elif len(bad) < 20:
            bad.append([ci, path, out, how])
    by = {k: sum(1 for x in lines if x[2] == k) for k in ("SGE", "DPOS", "INFEAS", "FAIL")}
    controls["C0_positive_unmutated_sample"] = {"cover_errors": errs[:5], "n_cover_errors": len(errs),
                                                "leaves": len(lines), "verified": n_ok, "via_subdivision": n_sub,
                                                "by_outcome": by, "failures": bad,
                                                "pass": (not errs) and n_ok == len(lines)}
    rec = list(zip(lines, boxes))
    dpos = [(l, b) for l, b in rec if l[2] == "DPOS"]
    sge = [(l, b) for l, b in rec if l[2] == "SGE"]
    infe = [(l, b) for l, b in rec if l[2] == "INFEAS"]

    # ---- C1a altered derivative sign ------------------------------------------------------------------------------
    evm = C.Evaluator(T, int(spec["prec"]), dsign=-1)
    rej = 0
    acc = []
    for (l, b) in dpos:
        ok, how = evm.verify(b, "DPOS")
        sok = False
        if not ok:
            sok, _, _, first = evm.verify_subdiv(b, "DPOS", geom, 3)
        if (not ok) and how == "DPOS:D_GT_0_NOT_CERTIFIED" and not sok:
            rej += 1
        elif len(acc) < 10:
            acc.append([l, how, sok])
    controls["C1a_altered_derivative_sign"] = {"intended_rule": "DPOS:D_GT_0_NOT_CERTIFIED", "tested": len(dpos),
                                               "rejected_at_intended_rule_even_after_3_bisections": rej,
                                               "not_rejected": acc, "pass": len(dpos) > 0 and rej == len(dpos)}

    # ---- C1b altered sign of one term of D ------------------------------------------------------------------------
    evt = MutTerm(T, int(spec["prec"]))
    rej = 0
    for (l, b) in dpos:
        ok, how = evt.verify(b, "DPOS")
        if (not ok) and how == "DPOS:D_GT_0_NOT_CERTIFIED":
            rej += 1
    controls["C1b_altered_sign_of_a2prime_term"] = {"intended_rule": "DPOS:D_GT_0_NOT_CERTIFIED",
                                                    "tested": len(dpos), "rejected_at_intended_rule": rej,
                                                    "pass": rej > 0}
    flint_prec = int(spec["prec"])

    # ---- C2 false infeasibility -----------------------------------------------------------------------------------
    def infeas_case(name, pairs, rule, limit=2000):
        tested = 0
        hit = 0
        other = []
        for (l, b) in pairs[:limit]:
            tested += 1
            ok, how = ev.check_INFEAS(b)
            if (not ok) and how == rule:
                hit += 1
            elif len(other) < 10:
                other.append([l, ok, how])
        controls[name] = {"intended_rule": rule, "tested": tested, "rejected_at_intended_rule": hit,
                          "other": other, "pass": tested > 0 and hit == tested}

    nonin = [(l, b) for l, b in rec if l[2] != "INFEAS"]
    infeas_case("C2a_false_INFEAS_r_lo_zero", [(l, b) for l, b in nonin if b[0][0] == 0], "INFEAS:DOMAIN_R_LO")
    pi_q = Fraction(314159265358979, 100000000000000)
    infeas_case("C2b_false_INFEAS_phi_lo_le_pi", [(l, b) for l, b in nonin if b[0][0] > 0 and b[2][0] < pi_q],
                "INFEAS:DOMAIN_PHI_LO")
    mp.mp.dps = 40

    def gfun(rv, u):
        return mp.exp(rv * u) * (mp.cos(u) - rv * mp.sin(u))

    feas_corner = []
    for (l, b) in nonin:
        rl, pl = b[0][0], b[2][0]
        if rl > 0 and pl > Fraction(315, 100) and pl < Fraction(6, 1):
            if gfun(mp.mpf(rl.numerator) / rl.denominator, mp.mpf(pl.numerator) / pl.denominator) < 1 - mp.mpf(
                    "1e-20"):
                feas_corner.append((l, b))
    infeas_case("C2c_false_INFEAS_feasible_corner", feas_corner, "INFEAS:G_NOT_GT_1")
    lowered = []
    for (l, b) in infe[:2000]:
        rl = b[0][0]
        rv = mp.mpf(rl.numerator) / rl.denominator
        # mutation construction only (mpmath); the rejection decision below is the Arb INFEAS rule
        th = mp.findroot(lambda u: gfun(rv, u) - 1, (mp.pi + mp.mpf("1e-12"), 2 * mp.pi - mp.mpf("1e-12")),
                         solver="anderson")
        newlo = Fraction(int(mp.floor((th - mp.mpf("1e-3")) * 10 ** 9)), 10 ** 9)
        if newlo > Fraction(315, 100):
            lowered.append((l, (b[0], b[1], (newlo, b[2][1]))))
    infeas_case("C2d_INFEAS_leaf_widened_below_theta1", lowered, "INFEAS:G_NOT_GT_1")

    # ---- C3 coverage mutations ------------------------------------------------------------------------------------
    cell_of = {}
    for i, (ci, path, out) in enumerate(lines):
        cell_of.setdefault(ci, []).append(i)
    big = max(cell_of, key=lambda c: len(cell_of[c]) if c < last_cell else -1)
    idx = cell_of[big]
    mid_i = idx[len(idx) // 2]
    last_i = idx[-1]
    flip_last = list(lines)
    p0 = flip_last[mid_i][1]
    flip_last[mid_i] = (flip_last[mid_i][0], p0[:-1] + ("1" if p0[-1] == "0" else "0"), flip_last[mid_i][2])
    flip_mid = list(lines)
    p1 = flip_mid[mid_i][1]
    k = len(p1) // 2
    flip_mid[mid_i] = (flip_mid[mid_i][0], p1[:k] + ("1" if p1[k] == "0" else "0") + p1[k + 1:], flip_mid[mid_i][2])
    wrong_cell = list(lines)
    wrong_cell[mid_i] = (wrong_cell[mid_i][0] + 1, wrong_cell[mid_i][1], wrong_cell[mid_i][2])
    muts = {
        "C3a_missing_middle_leaf": (lines[:mid_i] + lines[mid_i + 1:], ("COVER:PATH_MISMATCH",)),
        "C3b_missing_last_leaf_of_cell": (lines[:last_i] + lines[last_i + 1:], ("COVER:INCOMPLETE_CELL",)),
        "C3c_duplicate_middle_leaf": (lines[:mid_i + 1] + [lines[mid_i]] + lines[mid_i + 1:],
                                      ("COVER:PATH_MISMATCH",)),
        "C3d_duplicate_last_leaf_of_cell": (lines[:last_i + 1] + [lines[last_i]] + lines[last_i + 1:],
                                            ("COVER:EXTRA_LEAF",)),
        "C3e_path_last_bit_flipped": (flip_last, ("COVER:PATH_MISMATCH",)),
        "C3f_path_middle_bit_flipped": (flip_mid, ("COVER:PATH_MISMATCH",)),
        "C3g_leaf_moved_to_next_cell": (wrong_cell, ("COVER:INCOMPLETE_CELL", "COVER:CELL_ORDER")),
        "C3h_dropped_whole_cell": ([x for x in lines if x[0] != big], ("COVER:CELL_ORDER",)),
    }
    for name, (seq, rules) in muts.items():
        _, e, _ = cover_run(seq)
        first = e[0] if e else None
        controls[name] = {"intended_rule": list(rules), "cell": big, "first_error": first, "n_errors": len(e),
                          "all_error_kinds": sorted(set(x.split()[0] for x in e)),
                          "pass": bool(first) and first.startswith(rules)}

    # ---- C4 weakened bound ----------------------------------------------------------------------------------------
    def S_mid(b):
        m, _ = ev.mid_half(b)
        P0, P1, P2, _ = ev.base(*ev.point(m))
        a0, a1, a2 = 1 - P0.real, 1 - P1.real, 1 - P2.real
        return 2 * a0 * a2 / (a1 * a1) - 1, a1

    step = max(1, len(sge) // 600)
    tested = 0
    hit = 0
    other = []
    for (l, b) in sge[::step]:
        s, a1 = S_mid(b)
        if not (a1 > 0):
            continue
        up = Fraction(int(mp.ceil(mp.mpf(s.upper().str(30, radius=False)) * 10 ** 12)), 10 ** 12) + Fraction(1, 10 ** 6)
        evw = C.Evaluator(up, flint_prec)
        tested += 1
        ok = evw.check_SGE(b)
        sok = False
        if not ok:
            sok, _, _, _ = evw.verify_subdiv(b, "SGE", geom, 3)
        if (not ok) and not sok:
            hit += 1
        elif len(other) < 10:
            other.append([l, str(up), ok, sok])
    controls["C4a_weakened_bound_T_above_S_mid"] = {"intended_rule": "SGE:G_GT_0_NOT_CERTIFIED", "tested": tested,
                                                    "rejected_even_after_3_bisections": hit, "other": other,
                                                    "pass": tested > 0 and hit == tested}
    ev25 = C.Evaluator(Fraction(1, 4), flint_prec)
    rej = sum(1 for (l, b) in sge if not ev25.check_SGE(b))
    controls["C4b_weakened_bound_T_quarter"] = {"intended_rule": "SGE:G_GT_0_NOT_CERTIFIED", "tested": len(sge),
                                                "rejected": rej, "pass": rej > 0}
    tested = 0
    hit = 0
    other = []
    for (l, b) in dpos:
        s, a1 = S_mid(b)
        if not (s < ev.onepT - 1 and a1 > 0):
            continue
        tested += 1
        ok, how = ev.verify(b, "SGE")
        if (not ok) and how == "SGE:G_GT_0_NOT_CERTIFIED":
            hit += 1
        elif len(other) < 10:
            other.append([l, how])
    controls["C4c_DPOS_leaf_relabelled_SGE"] = {"intended_rule": "SGE:G_GT_0_NOT_CERTIFIED", "tested": tested,
                                                "rejected_at_intended_rule": hit, "other": other,
                                                "pass": tested > 0 and hit == tested}

    # ---- C5 FAIL label --------------------------------------------------------------------------------------------
    ok, how = ev.verify(rec[0][1], "FAIL")
    controls["C5_FAIL_label"] = {"intended_rule": "OUTCOME:FAIL", "result": [ok, how],
                                 "pass": (not ok) and how == "OUTCOME:FAIL"}

    res["controls"] = controls
    res["all_pass"] = all(v["pass"] for v in controls.values())
    res["post_leaves_sha256"] = sha256_file(leafp)
    res["leaves_unchanged"] = res["post_leaves_sha256"] == leaf_sha
    res["elapsed_seconds"] = round(time.time() - t0, 2)
    with open(os.path.join(run, "RESULT.json"), "x") as fh:
        json.dump(res, fh, indent=1)
    print("RESULT", "PASS" if res["all_pass"] and res["leaves_unchanged"] else "FAIL",
          json.dumps({k: v["pass"] for k, v in controls.items()}))
    return 0 if res["all_pass"] and res["leaves_unchanged"] else 1


if __name__ == "__main__":
    sys.exit(main())

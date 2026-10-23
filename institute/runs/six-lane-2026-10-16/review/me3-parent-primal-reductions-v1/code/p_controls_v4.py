"""ME3 parent desk (ME3ParentPrimal): addendum control v4 — sign-aware worst-case interval form of the E2 explanation.

Why v4: in c03 (p_controls_v3) X2 certified E > 0 naively on all 8018 DPOS leaves, but X3 multiplied the phi-ball by
the E-ball with plain ball arithmetic; for phi-ranges touching 0 that product has a negative lower end even though
both factors are >= 0 (ball wrapping), and one leaf additionally needs the r01 bisection for D > 0.
v4 uses the exact sign-aware bound: on a box with phi >= phi_lo >= 0 and E >= E_lo > 0 (certified),
  phi * E >= phi_lo * E_lo >= 0,  so  D_mut = D + phi E >= lower(D enclosure) + phi_lo * E_lo.
X5 certifies  lower(D enclosure) + phi_lo * E_lo > 0  on every DPOS leaf; a leaf whose whole-box D enclosure is not
positive is bisected (split rule of the spec, depth <= MAXDEPTH, recorded) and the same bound is certified on every
sub-box (E is re-certified on each sub-box).
Usage: p_controls_v4.py RUN_DIR LEAVES LEAVES_SHA SPEC SPEC_SHA LAST_CELL MAXDEPTH
Arithmetic: exact Fractions and Arb balls only. Writes RUN_DIR/RESULT.json (exclusive create).
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
import p_core_v1 as C  # noqa: E402
import p_controls_v3 as V3  # noqa: E402

LINE = re.compile(rb"^(0|[1-9][0-9]*) (-|[01]+) (SGE|DPOS|INFEAS|FAIL)\n$")
T = Fraction(11, 50)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def bound_ok(ev, box):
    """Certified lower(D) + phi_lo * E_lo > 0 on the box, with E_lo > 0 certified and phi_lo >= 0 exact."""
    how, Eb, Denc, phb = V3.E_pos(ev, box)
    pl = box[2][0]
    if not how or pl < 0:
        return False, None
    Elo = Eb.lower()
    if not (Elo > 0):
        return False, None
    val = Denc + C.qa(pl) * Elo
    return bool(val > 0), val


def main():
    run, leafp, leaf_sha, specp, spec_sha = sys.argv[1:6]
    last_cell, maxdepth = int(sys.argv[6]), int(sys.argv[7])
    t0 = time.time()
    res = {"script": "p_controls_v4.py", "argv": sys.argv[1:]}
    pre = {"leaves": sha256_file(leafp), "spec": sha256_file(specp)}
    res["pre_hashes"] = pre
    assert pre["leaves"] == leaf_sha and pre["spec"] == spec_sha, pre
    spec = json.load(open(specp))
    geom = C.Geometry(spec)
    dpos = []
    errs = []
    with gzip.open(leafp, "rb") as fh:
        for raw in fh:
            m = LINE.match(raw)
            ci = int(m.group(1))
            if ci > last_cell:
                break
            path = m.group(2).decode()
            path = "" if path == "-" else path
            box, e = geom.feed(ci, path)
            errs.extend(e)
            if m.group(3) == b"DPOS":
                dpos.append(((ci, path), box))
    ev = C.Evaluator(T, int(spec["prec"]))
    direct = 0
    subdiv = []
    fails = []
    minval = None
    for (key, b) in dpos:
        ok, val = bound_ok(ev, b)
        if ok:
            direct += 1
            if minval is None or val.lower() < minval.lower():
                minval = val
            continue
        stack = [(b, 0)]
        good = True
        n = 0
        while stack:
            bb, dep = stack.pop()
            o, vv = bound_ok(ev, bb)
            if o:
                n += 1
                if minval is None or vv.lower() < minval.lower():
                    minval = vv
                continue
            if dep >= maxdepth:
                good = False
                break
            c0, c1 = geom.split(bb)
            stack.append((c1, dep + 1))
            stack.append((c0, dep + 1))
        rec = {"leaf": list(key), "certified_by_bisection": good, "subboxes": n}
        (subdiv if good else fails).append(rec)
    nd = len(dpos)
    res["sample"] = {"cells": last_cell + 1, "dpos_leaves": nd, "n_cover_errors": len(errs)}
    res["X5_sign_aware_worst_case_D_plus_phiE"] = {
        "tested": nd, "certified_directly": direct, "certified_after_recorded_bisection": len(subdiv),
        "bisected_leaves": subdiv, "not_certified": fails,
        "min_certified_lower_bound": None if minval is None else minval.lower().str(12, radius=False),
        "ok": not fails and direct + len(subdiv) == nd and nd == 8018}
    res["all_ok"] = res["X5_sign_aware_worst_case_D_plus_phiE"]["ok"] and not errs
    res["post_leaves_sha256"] = sha256_file(leafp)
    res["leaves_unchanged"] = res["post_leaves_sha256"] == leaf_sha
    res["elapsed_seconds"] = round(time.time() - t0, 2)
    with open(os.path.join(run, "RESULT.json"), "x") as fh:
        json.dump(res, fh, indent=1, default=str)
    print("RESULT", "PASS" if res["all_ok"] and res["leaves_unchanged"] else "FAIL",
          json.dumps({"direct": direct, "bisected": len(subdiv), "fails": len(fails), "n": nd}))
    return 0 if res["all_ok"] and res["leaves_unchanged"] else 1


if __name__ == "__main__":
    sys.exit(main())

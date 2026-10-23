"""ME3 parent desk (ME3ParentPrimal): addendum control v3 — explain the benign E2 mutation of run c02.

E2 mutation: a_k' computed with L_k - phi instead of L_k. Since Re P_k = 1 - a_k,
  a_k'_mut = -Re(P_k (L_k - phi)) = a_k' + phi (1 - a_k),
and because D = a0' a1 a2 + a0 a1 a2' - 2 a0 a1' a2 is linear in (a0', a1', a2'),
  D_mut = D + phi * E,   E := a1 a2 + a0 a1 - 2 a0 a2 = a1 (a0 + a2 - (1 + S) a1)   (1 + S = 2 a0 a2 / a1^2).
(AM-GM: a0 + a2 >= a1 sqrt(2(1+S)), so E >= a1^2 sqrt(1+S)(sqrt 2 - sqrt(1+S)) >= 0 whenever S <= 1.)
On every DPOS box phi >= 0, so E > 0 on the box gives D_mut >= D > 0: the mutation cannot be rejected there.
Usage: p_controls_v3.py RUN_DIR LEAVES LEAVES_SHA SPEC SPEC_SHA LAST_CELL MAXDEPTH
  X1 exact sympy identities above (a'_mut, D_mut - D - phi E = 0, E = a1(a0 + a2 - (1+S)a1));
  X2 certify E > 0 on every DPOS leaf (naive ball, else mean-value form with library gradients of a_k, else recorded
     bisection up to MAXDEPTH);
  X3 worst-case interval form: certify  lower(D enclosure) + lower(phi-ball * E enclosure) > 0  on every DPOS leaf
     (D enclosure = naive if positive else the library mean-value form), i.e. DPOS with the dropped term replaced by
     its worst-case interval over the box;
  X4 (explanatory) naive certification of S < 1 (a0 a2 < a1^2) on DPOS leaves, the hypothesis of the AM-GM remark.
Arithmetic: exact Fractions, sympy exact symbols and Arb balls only. Writes RUN_DIR/RESULT.json (exclusive create).
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
import sympy as sp  # noqa: E402
import p_core_v1 as C  # noqa: E402

LINE = re.compile(rb"^(0|[1-9][0-9]*) (-|[01]+) (SGE|DPOS|INFEAS|FAIL)\n$")
T = Fraction(11, 50)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def E_parts(ev, box):
    """Returns (E naive ball, E mean-value-form ball, D enclosure ball used, phi ball)."""
    balls, a, d, D, P, z = ev.D_naive(box)
    En = a[1] * (a[0] + a[2]) - 2 * a[0] * a[2]
    mid, h = ev.mid_half(box)
    am, dm, Dm, _, _ = ev.D_val(*ev.point(mid))
    Em = am[1] * (am[0] + am[2]) - 2 * am[0] * am[2]
    r, w, p = balls
    da, _, _, _ = ev.grad_a(r, w, p, P, z)
    hb = [C.symb(x) for x in h]
    Emvf = Em
    for j in range(3):
        dE = da[1][j] * (a[0] + a[2]) + a[1] * (da[0][j] + da[2][j]) - 2 * (da[0][j] * a[2] + a[0] * da[2][j])
        Emvf = Emvf + dE * hb[j]
    if D > 0:
        Denc = D
    else:
        Denc, _ = ev.D_mvf(box, balls, a, d, P, z)
    return En, Emvf, Denc, balls[2]


def E_pos(ev, box):
    En, Emvf, Denc, phb = E_parts(ev, box)
    if En > 0:
        return "naive", En, Denc, phb
    if Emvf > 0:
        return "mvf", Emvf, Denc, phb
    return None, (En if En.lower() > Emvf.lower() else Emvf), Denc, phb


def main():
    run, leafp, leaf_sha, specp, spec_sha = sys.argv[1:6]
    last_cell, maxdepth = int(sys.argv[6]), int(sys.argv[7])
    t0 = time.time()
    res = {"script": "p_controls_v3.py", "argv": sys.argv[1:]}
    pre = {"leaves": sha256_file(leafp), "spec": sha256_file(specp)}
    res["pre_hashes"] = pre
    assert pre["leaves"] == leaf_sha and pre["spec"] == spec_sha, pre
    spec = json.load(open(specp))
    # ---- X1 exact identities ---------------------------------------------------------------------------------------
    a0, a1, a2, d0, d1, d2, ph, x, y, u, v = sp.symbols("a0 a1 a2 d0 d1 d2 phi x y u v", real=True)
    Dsym = d0 * a1 * a2 + a0 * a1 * d2 - 2 * a0 * d1 * a2
    Dmut = Dsym.subs({d0: d0 + ph * (1 - a0), d1: d1 + ph * (1 - a1), d2: d2 + ph * (1 - a2)}, simultaneous=True)
    Esym = a1 * a2 + a0 * a1 - 2 * a0 * a2
    id1 = sp.expand(Dmut - Dsym - ph * Esym)
    Ssym = 2 * a0 * a2 / a1 ** 2 - 1
    id2 = sp.simplify(Esym - a1 * (a0 + a2 - (1 + Ssym) * a1))
    Pc = x + sp.I * y          # P_k
    Lc = u + sp.I * v          # L_k
    ak = 1 - sp.re(Pc)
    id3 = sp.simplify(-sp.re(sp.expand(Pc * (Lc - ph))) - (-sp.re(sp.expand(Pc * Lc)) + ph * (1 - ak)))
    res["X1_exact_identities"] = {"Dmut-D-phi*E": str(id1), "E-a1(a0+a2-(1+S)a1)": str(id2),
                                  "a'_mut-(a'+phi(1-a))": str(id3),
                                  "ok": str(id1) == "0" and str(id2) == "0" and str(id3) == "0"}
    # ---- DPOS leaves -----------------------------------------------------------------------------------------------
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
    x2 = {"naive": 0, "mvf": 0, "subdiv": 0, "fail": 0}
    x3_ok = 0
    x3_fail = []
    x4_ok = 0
    sub_rec = []
    minE = None
    minE_key = None
    phi_lo_min = None
    for (key, b) in dpos:
        phi_lo_min = b[2][0] if phi_lo_min is None else min(phi_lo_min, b[2][0])
        how, Eb, Denc, phb = E_pos(ev, b)
        if how:
            x2[how] += 1
            lo = Eb.lower()
            if minE is None or lo < minE:
                minE, minE_key = lo, key
        else:
            stack = [(b, 0)]
            ok = True
            nsub = 0
            while stack:
                bb, dep = stack.pop()
                hw, Ebb, _, _ = E_pos(ev, bb)
                if hw:
                    nsub += 1
                    lo = Ebb.lower()
                    if minE is None or lo < minE:
                        minE, minE_key = lo, key
                    continue
                if dep >= maxdepth:
                    ok = False
                    break
                c0, c1 = geom.split(bb)
                stack.append((c1, dep + 1))
                stack.append((c0, dep + 1))
            x2["subdiv" if ok else "fail"] += 1
            sub_rec.append({"leaf": list(key), "ok": ok, "subboxes": nsub})
        worst = Denc + phb * Eb
        if worst > 0:
            x3_ok += 1
        elif len(x3_fail) < 20:
            x3_fail.append({"leaf": list(key), "D_lo": Denc.lower().str(12), "phiE": (phb * Eb).str(12, radius=True)})
        balls, a, d, D, P, z = ev.D_naive(b)
        if (a[0] * a[2] - a[1] * a[1]) < 0:
            x4_ok += 1
    n = len(dpos)
    res["sample"] = {"cells": last_cell + 1, "dpos_leaves": n, "cover_errors_first5": errs[:5],
                     "n_cover_errors": len(errs), "phi_lo_min_over_DPOS": str(phi_lo_min)}
    res["X2_E_positive_on_every_DPOS_leaf"] = {"tested": n, "by_method": x2, "subdivisions": sub_rec,
                                               "min_certified_lower_bound_of_E": None if minE is None else
                                               minE.str(15, radius=False), "attained_on_leaf": minE_key,
                                               "ok": x2["fail"] == 0 and n == 8018}
    res["X3_worst_case_interval_D_plus_phiE_positive"] = {"tested": n, "certified": x3_ok, "failures": x3_fail,
                                                          "ok": x3_ok == n}
    res["X4_S_lt_1_naive_explanatory"] = {"tested": n, "certified": x4_ok}
    res["all_ok"] = (res["X1_exact_identities"]["ok"] and res["X2_E_positive_on_every_DPOS_leaf"]["ok"]
                     and not errs and phi_lo_min is not None and phi_lo_min >= 0)
    res["post_leaves_sha256"] = sha256_file(leafp)
    res["leaves_unchanged"] = res["post_leaves_sha256"] == leaf_sha
    res["elapsed_seconds"] = round(time.time() - t0, 2)
    with open(os.path.join(run, "RESULT.json"), "x") as fh:
        json.dump(res, fh, indent=1, default=str)
    print("RESULT", "PASS" if res["all_ok"] and res["leaves_unchanged"] else "FAIL",
          json.dumps({"X1": res["X1_exact_identities"]["ok"], "X2": x2, "X3": [x3_ok, n], "X4": [x4_ok, n]}))
    return 0 if res["all_ok"] and res["leaves_unchanged"] else 1


if __name__ == "__main__":
    sys.exit(main())

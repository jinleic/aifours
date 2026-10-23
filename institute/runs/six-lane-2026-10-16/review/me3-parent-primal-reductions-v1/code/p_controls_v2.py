"""ME3 parent desk (ME3ParentPrimal): derivative-mutation controls, version 2 (addendum to p_controls_v1 / run c01).

Why v2: in run c01 the extra control C1b (flip the sign of the a0 a1 a2' term of D) was NOT rejected on any of the
8018 DPOS leaves. That is a control-design error (a benign mutation), not a checker failure: flipping that term
changes D by -2 a0 a1 a2', which is >= 0 wherever a2' <= 0. The required control C1a (global derivative sign flip)
passed 8018/8018 in c01. v2 (1) certifies the explanation, and (2) runs two further derivative-formula mutations
as sensitivity checks with the pre-declared expectation "rejected on at least one DPOS leaf at the DPOS rule".
Usage: p_controls_v2.py RUN_DIR LEAVES LEAVES_SHA SPEC SPEC_SHA LAST_CELL
  E1  certify a2' < 0 on every DPOS leaf (naive ball, else mean-value form with the library gradient of a2');
  E2  mutation 'drop phi in L_k' (a_k' computed without the r-dependence of e^{r phi}), consistent gradient;
  E3  mutation 'sign of d_r zeta flipped' (L_k = phi + (r-i)/(1+r^2) + (k+1) w zeta), consistent gradient.
Arithmetic: exact Fractions and Arb balls only (no floats). Writes RUN_DIR/RESULT.json (exclusive create).
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
from flint import acb  # noqa: E402
import p_core_v1 as C  # noqa: E402

LINE = re.compile(rb"^(0|[1-9][0-9]*) (-|[01]+) (SGE|DPOS|INFEAS|FAIL)\n$")
T = Fraction(11, 50)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


class MutL(C.Evaluator):
    """a_k' := -Re(P_k Lm_k) with a mutated Lm_k; gradient of the mutated D computed consistently."""

    def __init__(self, T_, prec, drop_phi=False, flip_wz=False):
        super().__init__(T_, prec)
        self.drop_phi = drop_phi
        self.flip_wz = flip_wz

    def _Lm(self, r, w, p, z):
        rmi = acb(r, -1)
        K = rmi / (1 + r * r)
        base = K if self.drop_phi else K + p
        sgn = 1 if self.flip_wz else -1
        return [base + sgn * (k + 1) * (w * z) for k in range(3)]

    def D_val(self, r, w, p):
        P0, P1, P2, z = self.base(r, w, p)
        P = (P0, P1, P2)
        a = [1 - x.real for x in P]
        Lm = self._Lm(r, w, p, z)
        d = [-(P[k] * Lm[k]).real for k in range(3)]
        D = d[0] * a[1] * a[2] + a[0] * a[1] * d[2] - 2 * a[0] * d[1] * a[2]
        return a, d, D, P, z

    def grad_D(self, balls, a, d, P, z):
        r, w, p = balls
        da, _, rmi, rz = self.grad_a(r, w, p, P, z)
        Lm = self._Lm(r, w, p, z)
        omr = acb(1, -r)
        inv2 = 1 / (omr * omr)
        z2 = z * z
        wz2 = (w * z) * (w * z)
        sgn = 1 if self.flip_wz else -1
        dd = []
        for k in range(3):
            kk = k + 1
            lam = (self.grad_a_lam_r(r, w, p, z, k), -kk * rz, rmi)
            # d_x of Lm_k = [phi] + (r - i)/(1 + r^2) + sgn (k+1) w zeta
            dLm = (inv2 - sgn * kk * wz2, sgn * kk * z2, acb(0) if self.drop_phi else acb(1))
            dd.append(tuple(-(P[k] * (lam[j] * Lm[k] + dLm[j])).real for j in range(3)))
        dD = []
        for j in range(3):
            t = (dd[0][j] * a[1] * a[2] + d[0] * da[1][j] * a[2] + d[0] * a[1] * da[2][j]
                 + da[0][j] * a[1] * d[2] + a[0] * da[1][j] * d[2] + a[0] * a[1] * dd[2][j]
                 - 2 * (da[0][j] * d[1] * a[2] + a[0] * dd[1][j] * a[2] + a[0] * d[1] * da[2][j]))
            dD.append(t)
        return dD, dd, da

    def grad_a_lam_r(self, r, w, p, z, k):
        """Lam_{k,r} = d_r log P_k (the TRUE log-derivative of P_k; only a_k' is mutated)."""
        rmi = acb(r, -1)
        return rmi / (1 + r * r) + p - (k + 1) * (w * z)


def main():
    run, leafp, leaf_sha, specp, spec_sha, last_cell = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], \
        sys.argv[5], int(sys.argv[6])
    t0 = time.time()
    res = {"script": "p_controls_v2.py", "argv": sys.argv[1:]}
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
    res["sample"] = {"cells": last_cell + 1, "dpos_leaves": len(dpos), "cover_errors": errs[:5]}
    prec = int(spec["prec"])
    ev = C.Evaluator(T, prec)
    # E1: a2' < 0 on every DPOS leaf
    cert = 0
    unc = []
    for (key, b) in dpos:
        balls, a, d, D, P, z = ev.D_naive(b)
        if d[2] < 0:
            cert += 1
            continue
        mid, h = ev.mid_half(b)
        am, dm, Dm, _, _ = ev.D_val(*ev.point(mid))
        dD, dd, da = ev.grad_D(balls, a, d, P, z)
        hb = [C.symb(x) for x in h]
        a2p = dm[2] + dd[2][0] * hb[0] + dd[2][1] * hb[1] + dd[2][2] * hb[2]
        if a2p < 0:
            cert += 1
        elif len(unc) < 10:
            unc.append(key)
    controls = {"E1_explain_C1b_a2prime_negative_on_DPOS": {"tested": len(dpos), "a2prime_lt_0_certified": cert,
                                                             "uncertified": unc, "pass": cert == len(dpos)}}
    for name, kw in (("E2_mutation_drop_phi_in_L", {"drop_phi": True}),
                     ("E3_mutation_flip_sign_of_dr_zeta", {"flip_wz": True})):
        evm = MutL(T, prec, **kw)
        rej = 0
        for (key, b) in dpos:
            ok, how = evm.verify(b, "DPOS")
            if (not ok) and how == "DPOS:D_GT_0_NOT_CERTIFIED":
                rej += 1
        controls[name] = {"intended_rule": "DPOS:D_GT_0_NOT_CERTIFIED", "expectation": ">= 1 rejected (sensitivity)",
                          "tested": len(dpos), "rejected_at_intended_rule": rej, "pass": rej >= 1}
    # positive control for the subclass machinery: no mutation flags => identical to the library evaluator
    evid = MutL(T, prec)
    same = 0
    for (key, b) in dpos:
        if evid.verify(b, "DPOS")[0] == ev.verify(b, "DPOS")[0]:
            same += 1
    controls["E0_unmutated_subclass_agrees_with_library"] = {"tested": len(dpos), "agree": same,
                                                             "pass": same == len(dpos)}
    res["controls"] = controls
    res["all_pass"] = all(v["pass"] for v in controls.values()) and not errs
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

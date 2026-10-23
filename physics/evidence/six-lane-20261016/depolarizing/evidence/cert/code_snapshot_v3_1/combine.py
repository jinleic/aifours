"""Combine per-sector records of cert.py into the global enclosure, with discriminating rejections (v3.1).

python combine.py WITNESS.json PART*.sectors.jsonl --ptail 1e-13 --pitail 1e-40 --out total.json [--allow-missing]

LIMIT: records are replayable evidence, not proof. combine.py checks provenance, parameters, coverage, record shape
and interval sanity, but it cannot detect a record whose numbers were altered consistently; replay.py recomputes
sectors and compares the decoded fields. A certificate is accepted only after replay of every sector (full rerun)
or an independent recomputation.

Rejections raise Reject(reason), reason in:
  malformed, witness_hash, no_provenance, cert_hash, dd_hash, param_mismatch, nonfinite, order, domain,
  D_effective, pN_mismatch, unexpected_sector, duplicate, missing
"""
from __future__ import annotations

import argparse
import json
import math

import numpy as np
from flint import arb

import cert
from cert import A, LOG2, lo, parse_witness, sector_probs_arb, up, witness_sha256

PROV = ("witness_sha256", "cert_py_sha256", "dd_py_sha256", "M", "p", "D_param", "ptail", "pitail")


class Reject(Exception):
    def __init__(self, reason, detail=""):
        super().__init__(f"REJECT {reason}: {detail}")
        self.reason = reason


def _num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def validate_record(rec, f):
    """Shape and domain checks of one sector record (v3.1)."""
    if not isinstance(rec, dict) or not isinstance(rec.get("N"), int) or isinstance(rec.get("N"), bool):
        raise Reject("malformed", f"record without integer N in {f}")
    N = rec["N"]
    for key in PROV:
        if key not in rec:
            raise Reject("no_provenance", f"sector {N} in {f} lacks {key}")
    for key in ("lo", "hi", "eps_tail", "w_tail", "relE", "pN"):
        if key not in rec or not _num(rec[key]):
            raise Reject("malformed", f"sector {N}: field {key} missing or not a number")
    it = rec.get("ic_trunc")
    if not (isinstance(it, list) and len(it) == 2 and all(_num(v) for v in it)):
        raise Reject("malformed", f"sector {N}: ic_trunc must be a list of two numbers")
    for key in ("smin", "nsteps", "D"):
        if not isinstance(rec.get(key), int) or isinstance(rec.get(key), bool) or rec[key] < 0:
            raise Reject("malformed", f"sector {N}: {key} must be a nonnegative integer")
    if not all(math.isfinite(v) for v in (rec["lo"], rec["hi"], *it, rec["eps_tail"], rec["w_tail"], rec["relE"], rec["pN"])):
        raise Reject("nonfinite", f"sector {N}")
    if rec["lo"] > rec["hi"] or it[0] > it[1]:
        raise Reject("order", f"sector {N}: inverted interval")
    if not (0 <= rec["eps_tail"] <= 1 and 0 <= rec["w_tail"] <= 1 and rec["relE"] >= 0 and rec["pN"] > 0):
        raise Reject("domain", f"sector {N}: eps_tail/w_tail/relE/pN outside their domains")

def validate_witness(w):
    """Explicit premise checks (no assert): q exact rationals > 0 summing to 1; distinct residues; every nonzero
    amplitude of codeword i sits on k = residues[i] (mod k); support <= M; real amplitudes in the modular path."""
    from fractions import Fraction
    try:
        M = int(w["M"]); qs = [Fraction(x) for x in w["q"]]; D = int(w["D"]); Fraction(w["p"])
    except Exception as e:
        raise Reject("witness_invalid", f"unparsable M/p/q/D: {e}")
    if sum(qs) != 1 or any(q <= 0 for q in qs) or len(qs) != len(w["amps"]):
        raise Reject("witness_invalid", "weights must be positive exact rationals summing to 1, one per codeword")
    k, res = w.get("k"), w.get("residues")
    for i, row in enumerate(w["amps"]):
        if len(row) - 1 > M:
            raise Reject("witness_invalid", f"codeword {i}: support beyond M")
        if k is not None:
            if not row or isinstance(row[0], list):
                raise Reject("witness_invalid", f"codeword {i}: modular path requires real amplitudes")
            for j, h in enumerate(row):
                if float.fromhex(h) != 0.0 and j % k != res[i] % k:
                    raise Reject("witness_invalid", f"codeword {i}: nonzero amplitude at {j} off residue {res[i]} mod {k}")
    if k is not None and len({x % k for x in res}) != len(res):
        raise Reject("witness_invalid", "residues must be pairwise distinct mod k")
    return M, D


def upper_from_record(rec, r, Srho_hi):
    """m1: recompute the sector UPPER bound in Arb from recorded ic_trunc[1], w_tail, eps_tail (PROOFS §4):
    I_c(Phi_hat) <= ic_trunc_hi + r*h(w) + w log r + 2 sqrt(w) log r + (1+sqrt w) h2(sqrt w/(1+sqrt w)),
    using sum_i h(q_i w_i) <= r h(w) (h increasing on [0,1/e], q_i w_i <= w <= 1/e);
    I_c(Phi_N) <= (1-e) I_c(Phi_hat) [if negative, else I_c(Phi_hat)] + e S(rho) + h2(e)."""
    def h(x):
        return arb(0) if x == 0 else -x * x.log() / LOG2

    def h2(x):
        return arb(0) if x == 0 else h(x) + h(1 - x)
    w = arb(rec["w_tail"])
    e = arb(rec["eps_tail"])
    lr = arb(r).log() / LOG2
    if rec["w_tail"] > 0.36:
        raise Reject("domain", f"sector {rec['N']}: w_tail too large for the AFW/flag bound")
    sw = w.sqrt()
    upI = arb(rec["ic_trunc"][1]) + r * h(w) + w * lr + 2 * sw * lr + (1 + sw) * h2(sw / (1 + sw))
    base = (1 - e) * upI if up(upI) < 0 else upI
    return up(base + e * arb(Srho_hi) + h2(e))


def combine(w, parts, ptail, pitail, allow_missing=False, expect_cert=None, expect_dd=None):
    expect_cert = expect_cert or cert.CODE_SHA256
    expect_dd = expect_dd or cert.DD_SHA256
    validate_witness(w)
    M, p, eta, qs, amps, k, residues, D = parse_witness(w)
    r = len(qs)
    Kmax = max(len(c) for c in amps)
    amps = [np.pad(c, (0, Kmax - len(c))) for c in amps]
    orth = all(np.vdot(amps[i], amps[j]) == 0 for i in range(r) for j in range(i + 1, r))
    Srho = sum((-A(q) * A(q).log() / LOG2 for q in qs), arb(0)) if orth else arb(r).log() / LOG2
    Srho_hi = up(Srho)
    pN = sector_probs_arb(M, eta)
    sel = sorted(n for n in pN if float(pN[n].mid()) >= ptail)
    selset = set(sel)
    rest = sum((pN[n] for n in pN if float(pN[n].mid()) < ptail), arb(0))
    wsha = witness_sha256(w)
    got = {}
    for f in parts:
        for line in open(f):
            if not line.strip():
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError as e:
                raise Reject("malformed", f"unparsable line in {f}: {e}")
            validate_record(rec, f)
            N = rec["N"]
            if rec["witness_sha256"] != wsha:
                raise Reject("witness_hash", f"sector {N} in {f}")
            if rec["cert_py_sha256"] != expect_cert:
                raise Reject("cert_hash", f"sector {N}: {str(rec['cert_py_sha256'])[:12]} != {expect_cert[:12]}")
            if rec["dd_py_sha256"] != expect_dd:
                raise Reject("dd_hash", f"sector {N}")
            if (rec["M"], rec["p"], rec["D_param"], rec["ptail"], rec["pitail"]) != (M, str(p), D, ptail, pitail):
                raise Reject("param_mismatch", f"sector {N}: {(rec['M'], rec['p'], rec['D_param'], rec['ptail'], rec['pitail'])}")
            if N not in selset:
                raise Reject("unexpected_sector", f"sector {N} not in the ptail-selected set")
            if rec["D"] != min(D, N):      # effective truncation index recorded by cert.py (diagnostic)
                raise Reject("D_effective", f"sector {N}: D {rec['D']} != min(D_param, N) = {min(D, N)}")
            if rec["pN"] != float(pN[N].mid()):   # diagnostic copy must equal the recomputed midpoint
                raise Reject("pN_mismatch", f"sector {N}")
            if N in got:
                raise Reject("duplicate", f"sector {N}")
            got[N] = rec
    missing = [n for n in sel if n not in got]
    if missing and not allow_missing:
        raise Reject("missing", f"{len(missing)} selected sectors absent, e.g. {missing[:5]}")
    tot_lo, tot_hi = arb(0), arb(0)
    max_up_shift = 0.0
    for n in sel:
        if n in got:
            hiN = max(upper_from_record(got[n], r, Srho_hi), got[n]["hi"])   # m1: Arb recomputation, never looser
            max_up_shift = max(max_up_shift, hiN - got[n]["hi"])
            tot_lo += pN[n] * arb(got[n]["lo"])
            tot_hi += pN[n] * arb(hiN)
        else:   # explicit honest bound for an omitted sector: -S(rho) <= I_c(Phi_N) <= S(rho)
            tot_lo -= pN[n] * arb(Srho_hi)
            tot_hi += pN[n] * arb(Srho_hi)
    tot_lo -= rest * arb(Srho_hi)
    tot_hi += rest * arb(Srho_hi)
    omitted = sum((pN[n] for n in missing), arb(0))
    return {"witness_sha256": wsha, "cert_py_sha256": expect_cert, "dd_py_sha256": expect_dd,
            "M": M, "p": str(p), "eta": str(eta), "D": D, "ptail": ptail, "pitail": pitail,
            "lower": lo(tot_lo), "upper": up(tot_hi), "upper_recomputed_in_arb": True,
            "max_sector_upper_shift_vs_record": max_up_shift,
            "selected_sectors": len(sel), "computed": len(got),
            "missing": missing, "omitted_mass_hi": (up(omitted) if missing else 0.0), "rest_mass_hi": up(rest),
            "Srho_hi": Srho_hi,
            "max_relE": max((g["relE"] for g in got.values()), default=None),
            "max_w_tail": max((g["w_tail"] for g in got.values()), default=None),
            "max_eps_tail": max((g["eps_tail"] for g in got.values()), default=None),
            "classification": "POS" if lo(tot_lo) > 0 else ("NEG" if up(tot_hi) < 0 else "UNDECIDED"),
            "note": "records are replayable evidence; acceptance requires replay.py on every sector or an independent recomputation"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("witness")
    ap.add_argument("parts", nargs="+")
    ap.add_argument("--ptail", type=float, required=True)
    ap.add_argument("--pitail", type=float, required=True)
    ap.add_argument("--allow-missing", action="store_true")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    w = json.load(open(a.witness))
    try:
        out = combine(w, a.parts, a.ptail, a.pitail, a.allow_missing)
    except Reject as e:
        print(str(e))
        raise SystemExit(2)
    out["parts"] = a.parts
    json.dump(out, open(a.out, "w"), indent=1)
    print(json.dumps(out))

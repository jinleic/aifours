"""Combine per-sector records of cert.py into the global enclosure, with discriminating rejections (v3).

python combine.py WITNESS.json PART*.sectors.jsonl --ptail 1e-13 --pitail 1e-40 --out total.json [--allow-missing]

LIMIT: records are replayable evidence, not proof. combine.py checks provenance, parameters, coverage and
interval sanity, but it cannot detect a record whose numbers were altered consistently; replay.py recomputes
sectors and compares them bitwise. A certificate is accepted only after replay of every sector (full rerun) or
an independent recomputation.

Rejections raise Reject(reason) with reason in:
  witness_hash, no_provenance, cert_hash, dd_hash, param_mismatch, duplicate, order, nonfinite,
  unexpected_sector, missing
"""
from __future__ import annotations

import argparse
import json
import math

import numpy as np
from flint import arb

import cert
from cert import A, LOG2, lo, parse_witness, sector_probs_arb, up, witness_sha256


class Reject(Exception):
    def __init__(self, reason, detail=""):
        super().__init__(f"REJECT {reason}: {detail}")
        self.reason = reason


def combine(w, parts, ptail, pitail, allow_missing=False, expect_cert=None, expect_dd=None):
    expect_cert = expect_cert or cert.CODE_SHA256
    expect_dd = expect_dd or cert.DD_SHA256
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
            rec = json.loads(line)
            N = rec.get("N")
            for key in ("witness_sha256", "cert_py_sha256", "dd_py_sha256", "M", "p", "D_param", "ptail", "pitail"):
                if key not in rec:
                    raise Reject("no_provenance", f"sector {N} in {f} lacks {key}")
            if rec["witness_sha256"] != wsha:
                raise Reject("witness_hash", f"sector {N} in {f}")
            if rec["cert_py_sha256"] != expect_cert:
                raise Reject("cert_hash", f"sector {N}: {rec['cert_py_sha256'][:12]} != {expect_cert[:12]}")
            if rec["dd_py_sha256"] != expect_dd:
                raise Reject("dd_hash", f"sector {N}")
            if (rec["M"], rec["p"], rec["D_param"], rec["ptail"], rec["pitail"]) != (M, str(p), D, ptail, pitail):
                raise Reject("param_mismatch", f"sector {N}: {(rec['M'], rec['p'], rec['D_param'], rec['ptail'], rec['pitail'])}")
            vals = [rec["lo"], rec["hi"], *rec["ic_trunc"], rec["eps_tail"], rec["w_tail"], rec["relE"]]
            if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in vals):
                raise Reject("nonfinite", f"sector {N}")
            if rec["lo"] > rec["hi"] or rec["ic_trunc"][0] > rec["ic_trunc"][1]:
                raise Reject("order", f"sector {N}: lo {rec['lo']} > hi {rec['hi']}")
            if N not in selset:
                raise Reject("unexpected_sector", f"sector {N} not in the ptail-selected set")
            if N in got:
                raise Reject("duplicate", f"sector {N}")
            got[N] = rec
    missing = [n for n in sel if n not in got]
    if missing and not allow_missing:
        raise Reject("missing", f"{len(missing)} selected sectors absent, e.g. {missing[:5]}")
    tot_lo, tot_hi = arb(0), arb(0)
    for n in sel:
        if n in got:
            tot_lo += pN[n] * arb(got[n]["lo"])
            tot_hi += pN[n] * arb(got[n]["hi"])
        else:   # explicit honest bound for an omitted sector: -S(rho) <= I_c(Phi_N) <= S(rho)
            tot_lo -= pN[n] * arb(Srho_hi)
            tot_hi += pN[n] * arb(Srho_hi)
    tot_lo -= rest * arb(Srho_hi)
    tot_hi += rest * arb(Srho_hi)
    omitted_mass = up(sum((pN[n] for n in missing), arb(0)))
    return {"witness_sha256": wsha, "cert_py_sha256": expect_cert, "dd_py_sha256": expect_dd,
            "M": M, "p": str(p), "eta": str(eta), "D": D, "ptail": ptail, "pitail": pitail,
            "lower": lo(tot_lo), "upper": up(tot_hi), "selected_sectors": len(sel), "computed": len(got),
            "missing": missing, "omitted_mass_hi": omitted_mass, "rest_mass_hi": up(rest), "Srho_hi": Srho_hi,
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

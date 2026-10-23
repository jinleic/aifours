"""Combine per-sector rigorous results (cert.py --sectors runs) into the global enclosure.

python combine.py WITNESS.json PART1.json.sectors.jsonl [PART2...] --ptail 1e-30 --out total.json
Recomputes p_N in Arb, the selected sector set {N : mid(p_N) >= ptail}, checks every selected sector appears
exactly once (identical duplicates allowed), and bounds the rest by Araki-Lieb (PROOFS §4).
"""
from __future__ import annotations

import argparse
import json

from flint import arb

from cert import A, LOG2, lo, parse_witness, sector_probs_arb, up, witness_sha256

ap = argparse.ArgumentParser()
ap.add_argument("witness")
ap.add_argument("parts", nargs="+")
ap.add_argument("--ptail", type=float, default=1e-30)
ap.add_argument("--out", required=True)
a = ap.parse_args()
w = json.load(open(a.witness))
M, p, eta, qs, amps, k, residues, D = parse_witness(w)
import numpy as np
r = len(qs)
Kmax = max(len(c) for c in amps)
amps = [np.pad(c, (0, Kmax - len(c))) for c in amps]
orth = all(np.vdot(amps[i], amps[j]) == 0 for i in range(r) for j in range(i + 1, r))
Srho = sum((-A(q) * A(q).log() / LOG2 for q in qs), arb(0)) if orth else arb(r).log() / LOG2
Srho_hi = up(Srho)
pN = sector_probs_arb(M, eta)
sel = sorted(n for n in pN if float(pN[n].mid()) >= a.ptail)
rest = sum((pN[n] for n in pN if float(pN[n].mid()) < a.ptail), arb(0))
got = {}
for f in a.parts:
    for line in open(f):
        rec = json.loads(line)
        N = rec["N"]
        if N in got and (got[N]["lo"], got[N]["hi"]) != (rec["lo"], rec["hi"]):
            raise SystemExit(f"conflicting duplicate sector {N}")
        got[N] = rec
missing = [n for n in sel if n not in got]
extra = [n for n in got if n not in sel]
tot_lo = arb(0)
tot_hi = arb(0)
for n in sel:
    if n in got:
        tot_lo += pN[n] * arb(got[n]["lo"])
        tot_hi += pN[n] * arb(got[n]["hi"])
    else:   # missing sectors are bounded by -S(rho) <= I_c <= S(rho)
        tot_lo -= pN[n] * arb(Srho_hi)
        tot_hi += pN[n] * arb(Srho_hi)
tot_lo -= rest * arb(Srho_hi)
tot_hi += rest * arb(Srho_hi)
worst = min(got.values(), key=lambda g: g["lo"]) if got else None
out = {"witness_sha256": witness_sha256(w), "M": M, "p": str(p), "eta": str(eta), "D": D,
       "lower": lo(tot_lo), "upper": up(tot_hi), "selected_sectors": len(sel), "computed": len(got),
       "missing": missing, "extra_ignored": extra, "rest_mass_hi": up(rest), "Srho_hi": Srho_hi,
       "max_relE": max((g["relE"] for g in got.values()), default=None),
       "max_w_tail": max((g["w_tail"] for g in got.values()), default=None),
       "max_eps_tail": max((g["eps_tail"] for g in got.values()), default=None),
       "classification": "POS" if lo(tot_lo) > 0 else ("NEG" if up(tot_hi) < 0 else "UNDECIDED")}
json.dump(out, open(a.out, "w"), indent=1)
print(json.dumps(out))

"""Exact tables of SO(5)>SO(3) reduced one-body CFPs r(v e L ; v-1 e' L') for spin-2 bosons.

r is the one-body CFP at N = v (harmonic states); by Theorem A every spin-2 one-body CFP
equals an explicit N-factor times r.  Basis: Gram-Schmidt of harmonic projections of
covariant monomials f^a H^b T^c j^e (see spin2_basis.py), in order of e ascending ("asc",
default) or descending ("desc").

Output: results/spin2_r_table_<tag>.json  with entries
  {"v","L","e","Lp","ep","r2" (exact p/q), "sign"}  plus per-(v,L) multiplicity checks.
Run: $PY code/spin2_tables.py VMAX [LMAX|-] [asc|desc]
"""
import json
import os
import sys
import time

from flint import fmpq

from fpc_core import frac_str
from spin2_basis import Spin2, labels


def main(vmax, lmax=None, order="asc"):
    """All parents with v <= vmax (and L <= lmax if given: the low-spin 'bottom' sector)."""
    S = Spin2()
    B = S.B
    rows = []
    mult_checks = []
    t0 = time.time()
    for v in range(1, vmax + 1):
        for L in range(0, (2 * v if lmax is None else min(2 * v, lmax)) + 1):
            labs = labels(v, L)
            nul = B.hw_harmonic_basis(v, L) if v <= 14 else None
            if nul is not None:
                assert len(nul) == len(labs), (v, L, len(nul), labs)
                mult_checks.append((v, L, len(labs)))
            if not labs:
                continue
            parents = S.orthogonal_basis(v, L, order)
            for e, psi in parents:
                tot = fmpq(0)
                for Lp in range(max(0, L - 2), L + 3):
                    if not labels(v - 1, Lp):
                        continue
                    for ep, phi in S.orthogonal_basis(v - 1, Lp, order):
                        sq, sg = B.cfp_sq_sign(psi, v, L, phi, Lp)
                        tot += sq
                        rows.append({"v": v, "L": L, "e": e, "Lp": Lp, "ep": ep,
                                     "r2": frac_str(sq), "sign": sg})
                assert tot == 1, (v, L, e, tot)
        print(f"v={v} done  ({time.time() - t0:.1f}s)", flush=True)
    here = os.path.dirname(os.path.abspath(__file__))
    tag = (f"v{vmax}" if lmax is None else f"v{vmax}_L{lmax}") + ("" if order == "asc" else "_desc")
    out = os.path.join(here, "..", "results", f"spin2_r_table_{tag}.json")
    with open(out, "w") as fh:
        json.dump({"description": "spin-2 SO(5)>SO(3) reduced one-body CFPs r(v e L; v-1 e' L'), "
                                  f"GS basis (e {order}) of projected covariants f^a H^b T^c j^e; "
                                  "sign convention: see spin2_basis.py / fpc_core.py",
                   "vmax": vmax, "multiplicity_checks_vs_nullspace": mult_checks,
                   "rows": rows}, fh, indent=0)
    print(f"wrote {len(rows)} rows; completeness exact for every parent; "
          f"label count == null-space dimension for {len(mult_checks)} (v,L) pairs")


if __name__ == "__main__":
    lm = sys.argv[2] if len(sys.argv) > 2 else "-"
    main(int(sys.argv[1]), None if lm == "-" else int(lm), sys.argv[3] if len(sys.argv) > 3 else "asc")

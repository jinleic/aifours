"""Produce and exactly verify rational dual certificates for the replay gates.

Certificates (identity checked in Fractions by certify.check; floats only propose):
  shannon_Rminus : h(V) <= 114/17  (elemental Shannon + game equalities + h(v)<=1)
  shannon_R      : h(V) <= 27/4
  ingl1_Rminus   : h(V) <= 20/3 using ONE extra row Ing(3,10;4,8 | {1,2,5,6,7,9}) >= 0
                   (LP fact only: that row is NOT valid for all entropic vectors; see diamond_and_or.py)
Output: evidence/certs/<name>.json with the nonzero multipliers as 'p/q' strings and the bound.
"""
import sys, os, json
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_EDGES, R_MINUS_EDGES, nbmasks
import entropy_lp, certify
from ingleton_cg import ing_row

def cert(nbm, extra, maxden=100000):
    o = entropy_lp.solve(nbm, extra_ge=extra)
    ge, eq = o["ge"], o["eq"]; rd, cd = o["row_dual"], o["col_dual"]
    y = certify.rationalize(-rd[:len(ge)], maxden)
    z = certify.rationalize(-rd[len(ge):], maxden)
    u = [Fr(0)] * 10
    for v in range(10):
        u[v] = Fr(float(cd[(1 << v) - 1])).limit_denominator(maxden)
    y = [max(Fr(0), t) for t in y]
    ok, bad, B = certify.check(10, ge, eq, y, z, u)
    return o, ge, eq, y, z, u, ok, bad, B

def serialize(ge, eq, y, z, u):
    def fmt(r): return {str(k): v for k, v in r.items()}
    return dict(ge=[dict(row=fmt(r), y=str(t)) for r, t in zip(ge, y) if t],
                eq=[dict(row=fmt(r), z=str(t)) for r, t in zip(eq, z) if t],
                u=[str(t) for t in u])

if __name__ == "__main__":
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "certs")
    os.makedirs(outdir, exist_ok=True)
    Z = sum(1 << (i - 1) for i in [1, 2, 5, 6, 7, 9])
    key = (Z | 1 << 2, Z | 1 << 9, Z | 1 << 3, Z | 1 << 7)
    jobs = [("shannon_Rminus", R_MINUS_EDGES, []), ("shannon_R", R_EDGES, []),
            ("ingl1_Rminus", R_MINUS_EDGES, [ing_row(*key)])]
    summary = {}
    for name, E, extra in jobs:
        o, ge, eq, y, z, u, ok, bad, B = cert(nbmasks(E), extra)
        rec = dict(name=name, float_value=o["value"], exact_bound=str(B), identity_exact=ok,
                   residual_terms=len(bad), nnz_ge=sum(1 for t in y if t), nnz_eq=sum(1 for t in z if t))
        summary[name] = rec
        payload = dict(rec, **serialize(ge, eq, y, z, u))
        json.dump(payload, open(os.path.join(outdir, name + ".json"), "w"))
        print(json.dumps(rec)); sys.stdout.flush()
    if not all(r["identity_exact"] for r in summary.values()):
        sys.exit(1)

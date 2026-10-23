"""Positive controls through the same KM2 -> resolve -> assemble -> checker path.

v=9 : points Z7 ∪ {∞1,∞2} (∞ = 7, 8); G = Z7 ⋊ <x->2x> (order 21), base
      stabilizer H = <x->2x> (f=3); resolution r = x->2x, class orbits [1,3].
v=15: points Z13 ∪ {∞1,∞2}; G = Z13 ⋊ <x->3x> (order 39), H = <x->3x>;
      resolution class orbits [1,3,3].
v=15 (Denniston-type): G = Z13, H trivial, unrestricted resolution.
Each successful run writes a certificate and runs check_lkts57.py on it.
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from assemble import develop, write_certificate
from km2 import KM2
from lkts_core import closure
from resolve import check_resolution, resolve_symmetric
from satlib import solve

HERE = os.path.dirname(os.path.abspath(__file__))


def affine(q, a, b):
    n = q + 2
    return tuple([(a * x + b) % q for x in range(q)] + [q, q + 1])


def run(v, q, mult, sizes, outdir, tag):
    os.makedirs(outdir, exist_ok=True)
    n = v
    tr = affine(q, 1, 1)
    Ggens = [tr] + ([affine(q, mult, 0)] if mult else [])
    Hgens = [affine(q, mult, 0)] if mult else []
    M = KM2(n, Ggens, [(Hgens, [])], names=["S"])
    cnf, rv = M.cnf()
    p = os.path.join(outdir, f"{tag}_km.cnf")
    sha = cnf.write(p)
    rec = {"tag": tag, "v": v, "G_order": M.order, "km_rows": len(M.rows), "attempts": []}
    r = affine(q, mult, 0) if mult else tuple(range(n))
    classes = None
    for it in range(200):
        sha = cnf.write(p)
        st, model, dt = solve(p, "kissat", timeout=120, seed=it)
        rec["km_status"] = st
        if st != "SAT":
            break
        sel = [i for i, x in enumerate(rv) if x in model]
        base = sorted(tuple(int(y) for y in M.trip[t]) for t in M.bases_from(sel)[0])
        info, classes = resolve_symmetric(base, n, r, sizes, os.path.join(outdir, f"{tag}_res.cnf"), timeout=120, seed=1)
        rec["attempts"].append({"km_cnf_sha256": sha, "resolution": info["status"]})
        rec["resolution"] = info
        if classes is not None:
            break
        cnf.add([-rv[i] for i in sel])
    if classes is None:
        return rec
    check_resolution(base, n, classes)
    G = M.G
    H = closure(Hgens, n) if Hgens else [tuple(range(n))]
    cons = develop(G, [(classes, H)], v)
    cert = os.path.join(outdir, f"{tag}.lkts.txt")
    write_certificate(cons, v, cert, header_comment=f"control {tag}")
    chk = subprocess.run([sys.executable, os.path.join(HERE, "check_lkts57.py"), cert], capture_output=True, text=True)
    rec["checker"] = json.loads(chk.stdout)
    return rec


if __name__ == "__main__":
    out = sys.argv[1]
    recs = [run(9, 7, 2, [1, 3], out, "v9_z7x3"),
            run(15, 13, 3, [1, 3, 3], out, "v15_z13x3"),
            run(15, 13, None, [1] * 7, out, "v15_z13")]
    json.dump(recs, open(os.path.join(out, "controls.json"), "w"), indent=1)
    for r in recs:
        print(r["tag"], r["km_status"], r.get("resolution", {}).get("status"), r.get("checker", {}).get("result"))

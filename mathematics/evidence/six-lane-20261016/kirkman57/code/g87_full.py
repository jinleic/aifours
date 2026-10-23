"""LKTS(87) attempt with G903 = Z43 ⋊ Z21 on {inf} ∪ Z43×{0,1}.
Constituent orbits: S-family (43 constituents, stabilizer Z21 = multipliers about 0)
and two families of 21 constituents with stabilizer Z43 (translations).
Resolutions: S0 invariant under m21 (order 21) with classes [1,21,21];
B_k invariant under tau with one regular orbit of 43 classes.
Usage: g87_full.py OUTDIR [MAX_ITER]   (run with PYTHONHASHSEED=0 for determinism)
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from assemble import develop, write_certificate
from g87_groups import *
from km2 import KM2
from lkts_core import closure
from resolve import check_resolution, resolve_symmetric
from satlib import solve


def main():
    out = sys.argv[1]
    max_iter = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    os.makedirs(out, exist_ok=True)
    t0 = time.time()
    specs = [("S0", Z21, m21, [1, 21, 21]), ("B1", Z43, tau, [43]), ("B2", Z43, tau, [43])]
    M = KM2(N, G_GENS, [(h, []) for _, h, _, _ in specs], names=[s[0] for s in specs])
    log = {"summary": M.summary(), "iterations": []}
    print(json.dumps(log["summary"]), flush=True)
    cnf, rv = M.cnf()
    for it in range(max_iter):
        p = os.path.join(out, f"km_{it}.cnf")
        sha = cnf.write(p)
        st, model, dt = solve(p, "kissat", timeout=600, seed=it)
        rec = {"iter": it, "km_status": st, "km_seconds": round(dt, 3), "km_cnf_sha256": sha}
        log["iterations"].append(rec)
        if st != "SAT":
            print(json.dumps(rec), flush=True)
            break
        sel = [i for i, v in enumerate(rv) if v in model]
        bases = M.bases_from(sel)
        resolved, ok = [], True
        for j, (name, H, r, sizes) in enumerate(specs):
            blocks = sorted(tuple(int(x) for x in M.trip[t]) for t in bases[j])
            info, classes = resolve_symmetric(blocks, N, r, sizes, os.path.join(out, f"res_{it}_{name}.cnf"),
                                              timeout=300, seed=1)
            rec[name] = info
            if classes is None:
                ok = False
                cnf.add([-rv[i] for i in sel if M.rows[i][0] == j])
                break
            check_resolution(blocks, N, classes)
            resolved.append((classes, closure(H, N)))
        print(json.dumps(rec), flush=True)
        if not ok:
            continue
        cons = develop(M.G, resolved, N)
        cert = os.path.join(out, "lkts87_candidate.txt")
        write_certificate(cons, N, cert, header_comment="LKTS(87) candidate from G903 pipeline (unverified until checked)")
        chk = subprocess.run([sys.executable, os.path.join(HERE, "check_lkts57.py"), cert], capture_output=True, text=True)
        rec["checker"] = json.loads(chk.stdout)
        json.dump({"rows": sel, "bases": [sorted(b) for b in bases]}, open(os.path.join(out, "km_solution.json"), "w"))
        json.dump([c for c, _ in resolved], open(os.path.join(out, "base_resolutions.json"), "w"))
        print("CHECKER", chk.stdout, flush=True)
        break
    log["seconds"] = round(time.time() - t0, 2)
    json.dump(log, open(os.path.join(out, "pipeline_log.json"), "w"), indent=1)


if __name__ == "__main__":
    main()

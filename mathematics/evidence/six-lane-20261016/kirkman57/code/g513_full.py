"""Full G513 pipeline: KM2 (STS level, five bases with extra base symmetry) ->
per-base symmetric resolutions -> development by G513 -> certificate -> checker.

Usage: g513_full.py OUTDIR [MAX_ITER]
All inputs are generated deterministically from code; solver seeds fixed.
"""
import collections
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from assemble import develop, write_certificate
from g513_groups import *
from km2 import KM2
from lkts_core import closure
from resolve import build_group, check_resolution, decode_group, resolve_symmetric
from satlib import solve


def orient(b):
    ls = [p // 19 for p in b]
    c = collections.Counter(ls)
    if len(c) != 2:
        return None
    two = [l for l, k in c.items() if k == 2][0]
    one = [l for l, k in c.items() if k == 1][0]
    return "+" if one == (two + 1) % 3 else "-"


def main():
    out = sys.argv[1]
    max_iter = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    os.makedirs(out, exist_ok=True)
    t0 = time.time()
    specs = [("S0", P27, [], None), ("B1", F57, [gamma(1, 1)], (mu, gamma(1, 1))),
             ("B2", F57, [gamma(2, 1)], (mu, gamma(2, 1))),
             ("B3", F57P, [gamma(1, -1)], (mup, gamma(1, -1))),
             ("B4", F57P, [gamma(2, -1)], (mup, gamma(2, -1)))]
    M = KM2(N, G_GENS, [(h, k) for _, h, k, _ in specs], names=[s[0] for s in specs])
    log = {"summary": M.summary(), "iterations": []}
    cnf, rv = M.cnf()
    # orientation: every B base must use both positive and negative two-layer rows
    for j in range(1, 5):
        pos = [rv[i] for i, (jj, U, c) in enumerate(M.rows) if jj == j and orient(M.trip[U[0]]) == "+"]
        neg = [rv[i] for i, (jj, U, c) in enumerate(M.rows) if jj == j and orient(M.trip[U[0]]) == "-"]
        cnf.add(pos)
        cnf.add(neg)
    ident = [tuple(range(N))]
    for it in range(max_iter):
        p = os.path.join(out, f"km_{it}.cnf")
        sha = cnf.write(p)
        st, model, dt = solve(p, "kissat", timeout=300, seed=it)
        rec = {"iter": it, "km_status": st, "km_seconds": round(dt, 3), "km_cnf_sha256": sha}
        log["iterations"].append(rec)
        if st != "SAT":
            break
        sel = [i for i, v in enumerate(rv) if v in model]
        bases = M.bases_from(sel)
        resolved = []
        ok = True
        for j, (name, H, K, rgens) in enumerate(specs):
            blocks = sorted(tuple(int(x) for x in M.trip[t]) for t in bases[j])
            if j == 0:
                info, classes = resolve_symmetric(blocks, N, nu, [1, 9, 9, 9], os.path.join(out, f"res_{it}_{name}.cnf"),
                                                  timeout=300, seed=1)
                info["struct"] = "nu:[1,9,9,9]"
            else:
                R = closure(list(rgens), N)
                gsub = closure([rgens[1]], N)
                classes = None
                for sname, stabs in [("g61", [R] + [gsub] * 6 + [ident]), ("g32", [R] + [gsub] * 3 + [ident] * 2)]:
                    cnf2, orbits, choice, cosets, stb = build_group(blocks, N, R, stabs)
                    p2 = os.path.join(out, f"res_{it}_{name}_{sname}.cnf")
                    sha2 = cnf2.write(p2)
                    st2, model2, dt2 = solve(p2, "kissat", timeout=120, seed=1)
                    info = {"status": st2, "seconds": round(dt2, 3), "cnf_sha256": sha2, "struct": sname,
                            "vars": cnf2.nv, "clauses": len(cnf2.clauses)}
                    if st2 == "SAT":
                        classes = decode_group(model2, orbits, choice, cosets, stb, R)
                        break
            rec[name] = info
            if classes is None:
                ok = False
                # block this base's row choice
                cnf.add([-rv[i] for i in sel if M.rows[i][0] == j])
                break
            check_resolution(blocks, N, classes)
            resolved.append((classes, closure(H, N) if H else ident))
        print(json.dumps(rec), flush=True)
        if not ok:
            continue
        # develop and certify
        cons = develop(M.G, resolved, N)
        cert = os.path.join(out, "lkts57_candidate.txt")
        write_certificate(cons, N, cert, header_comment="LKTS(57) candidate from G513 pipeline (unverified until checked)")
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

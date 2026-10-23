"""Generic pipeline for v = 2q+1, q prime ≡ 7 (mod 12): G = Z_q ⋊ C_m, m=(q−1)/2,
acting on {∞} ∪ Z_q×{0,1} by (x,j)↦(ax+b,j).  Orbit structure (as Proposition
87-D): S-family q constituents (stabilizer C_m), two families of m constituents
(stabilizer Z_q).  Resolutions: S0 C_m-invariant [1, m, m]; B τ-invariant [q].
Usage: g2q1_full.py q OUTDIR [MAX_ITER] [RES_TIMEOUT]   (use PYTHONHASHSEED=0)
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from assemble import develop, write_certificate
from km2 import KM2
from km3 import KM3
from lkts_core import closure
from resolve import check_resolution, resolve_symmetric
from satlib import solve


def order_mod(a, q):
    k, x = 1, a % q
    while x != 1:
        x = x * a % q
        k += 1
    return k


def main():
    q = int(sys.argv[1])
    out = sys.argv[2]
    max_iter = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    rto = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    assert q % 12 == 7
    m = (q - 1) // 2
    g = next(a for a in range(2, q) if order_mod(a, q) == m)
    n = 2 * q + 1
    inf = 2 * q

    def P(f):
        o = [0] * n
        for j in range(2):
            for x in range(q):
                x2, j2 = f(x, j)
                o[q * j + x] = q * j2 + (x2 % q)
        o[inf] = inf
        return tuple(o)

    tau = P(lambda x, j: (x + 1, j))
    mg = P(lambda x, j: (g * x, j))
    os.makedirs(out, exist_ok=True)
    t0 = time.time()
    specs = [("S0", [mg], mg, [1, m, m]), ("B1", [tau], tau, [q]), ("B2", [tau], tau, [q])]
    KMclass = KM3 if os.environ.get("KM3") == "1" else KM2
    M = KMclass(n, [tau, mg], [(h, []) for _, h, _, _ in specs], names=[s[0] for s in specs])
    log = {"q": q, "v": n, "m": m, "g": g, "summary": M.summary(), "iterations": []}
    print(json.dumps({"q": q, "v": n, "g": g, **M.summary()}), flush=True)
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
        sel = [i for i, x in enumerate(rv) if x in model]
        bases = M.bases_from(sel)
        resolved, ok = [], True
        for j, (name, H, r, sizes) in enumerate(specs):
            blocks = sorted(tuple(int(x) for x in M.trip[t]) for t in bases[j])
            info, classes = resolve_symmetric(blocks, n, r, sizes, os.path.join(out, f"res_{it}_{name}.cnf"),
                                              timeout=rto, seed=1)
            rec[name] = {k: info[k] for k in ("status", "seconds", "cnf_sha256")}
            if classes is None:
                ok = False
                cnf.add([-rv[i] for i in sel if M.rows[i][0] == j])
                break
            check_resolution(blocks, n, classes)
            resolved.append((classes, closure(H, n)))
        print(json.dumps(rec), flush=True)
        if not ok:
            continue
        cons = develop(M.G, resolved, n)
        cert = os.path.join(out, f"lkts{n}_candidate.txt")
        write_certificate(cons, n, cert, header_comment=f"LKTS({n}) candidate, Z{q} x| C{m} on inf + Z{q}x2")
        chk = subprocess.run([sys.executable, os.path.join(HERE, "check_lkts57.py"), cert], capture_output=True, text=True)
        rec["checker"] = json.loads(chk.stdout)["result"]
        json.dump([c for c, _ in resolved], open(os.path.join(out, "base_resolutions.json"), "w"))
        print("CHECKER", rec["checker"], flush=True)
        break
    log["seconds"] = round(time.time() - t0, 2)
    json.dump(log, open(os.path.join(out, "pipeline_log.json"), "w"), indent=1)


if __name__ == "__main__":
    main()

"""Structured ansatz for the 2q+1 framework (q ≡ 7 mod 12, m=(q−1)/2, m' = m/3 coprime to 3):
B_k additionally invariant under the twisted multiplier ψ_k = h_{d_k} μ_λ h_{d_k}^{-1}
(λ of order m'; x_0 ↦ λx_0, x_1 ↦ λ(x_1−d_k)+d_k), with d_1 = 1, d_2 = a fixed non-square
(WLOG up to the Q-action on each family).  B_k's base parallel class P_k is required
to be ψ_k-invariant (then the τ-translates of P_k are the resolution).  S is
Q-invariant with an m-invariant resolution [1, m, m] (as in g2q1_full.py).
Usage: g2q1_struct.py q OUTDIR [MAX_ITER]
"""
import collections
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from assemble import develop, write_certificate
from km2 import KM2
from lkts_core import closure
from resolve import check_resolution, resolve_symmetric
from satlib import CNF, solve


def order_mod(a, q):
    k, x = 1, a % q
    while x != 1:
        x = x * a % q
        k += 1
    return k


def resolve_psi_class(blocks, n, tau, psi, path, timeout=300):
    """Find a psi-invariant parallel class P with exactly one block in each tau-orbit."""
    bset = set(blocks)
    img = lambda g, b: tuple(sorted(g[p] for p in b))
    # tau-orbits
    torb = {}
    orbs = []
    for b in sorted(bset):
        if b in torb:
            continue
        o, x = [], b
        while x not in torb:
            torb[x] = len(orbs)
            o.append(x)
            x = img(tau, x)
        orbs.append(o)
    # psi acts on tau-orbits
    seen = set()
    reps = []
    for W in range(len(orbs)):
        if W in seen:
            continue
        chain, x = [], W
        while x not in seen:
            seen.add(x)
            chain.append(x)
            x = torb[img(psi, orbs[x][0])]
        reps.append(chain)
    cnf = CNF()
    cover = collections.defaultdict(list)
    choice = []
    for chain in reps:
        opts = []
        for b in orbs[chain[0]]:
            blks, x = [], b
            for _ in range(len(chain)):
                blks.append(x)
                x = img(psi, x)
            if x != b:  # psi^len(chain) must return to b (P is psi-invariant)
                continue
            pts = collections.Counter(p for y in blks for p in y)
            if any(c > 1 for c in pts.values()):
                continue
            v = cnf.var()
            opts.append((v, blks))
            for p in pts:
                cover[p].append(v)
        if not opts:
            cnf.add([])
        else:
            cnf.exactly_one([o[0] for o in opts])
        choice.append(opts)
    for p in range(n):
        lits = cover.get(p, [])
        if not lits:
            cnf.add([])
        else:
            cnf.exactly_one(lits)
    sha = cnf.write(path)
    st, model, dt = solve(path, "kissat", timeout=timeout, seed=1)
    info = {"status": st, "seconds": round(dt, 3), "cnf_sha256": sha, "vars": cnf.nv, "psi_chains": len(reps)}
    if st != "SAT":
        return info, None
    P = [y for opts in choice for (v, blks) in opts if v in model for y in blks]
    # the resolution is P together with its tau-translates
    classes = [P]
    cur = P
    while True:
        cur = [img(tau, b) for b in cur]
        if sorted(cur) == sorted(P):
            break
        classes.append(cur)
    return info, classes


def main():
    q = int(sys.argv[1]); out = sys.argv[2]
    max_iter = int(sys.argv[3]) if len(sys.argv) > 3 else 20
    assert q % 12 == 7
    m = (q - 1) // 2
    assert m % 3 == 0 and (m // 3) % 3 != 0, "need m/3 coprime to 3"
    mp = m // 3
    g = next(a for a in range(2, q) if order_mod(a, q) == m)
    lam = next(a for a in range(2, q) if order_mod(a, q) == mp)
    nonsq = next(a for a in range(2, q) if pow(a, m, q) == q - 1)
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

    def psi(d):
        return P(lambda x, j: (lam * x, 0) if j == 0 else (lam * (x - d) + d, 1))

    psis = [psi(1), psi(nonsq)]
    os.makedirs(out, exist_ok=True)
    t0 = time.time()
    M = KM2(n, [tau, mg], [([mg], []), ([tau], [psis[0]]), ([tau], [psis[1]])], names=["S0", "B1", "B2"])
    log = {"q": q, "m": m, "mprime": mp, "g": g, "lambda": lam, "nonsquare": nonsq, "summary": M.summary(), "iterations": []}
    print(json.dumps({"q": q, "lambda": lam, "nonsq": nonsq, **M.summary()}), flush=True)
    cnf, rv = M.cnf()
    for it in range(max_iter):
        p = os.path.join(out, f"km_{it}.cnf")
        sha = cnf.write(p)
        st, model, dt = solve(p, "kissat", timeout=900, seed=it)
        rec = {"iter": it, "km_status": st, "km_seconds": round(dt, 3), "km_cnf_sha256": sha}
        log["iterations"].append(rec)
        if st != "SAT":
            print(json.dumps(rec), flush=True)
            break
        sel = [i for i, x in enumerate(rv) if x in model]
        bases = M.bases_from(sel)
        resolved, ok = [], True
        for j, name in enumerate(["S0", "B1", "B2"]):
            blocks = sorted(tuple(int(x) for x in M.trip[t]) for t in bases[j])
            if j == 0:
                info, classes = resolve_symmetric(blocks, n, mg, [1, m, m], os.path.join(out, f"res_{it}_{name}.cnf"),
                                                  timeout=300, seed=1)
                info = {k: info[k] for k in ("status", "seconds", "cnf_sha256")}
            else:
                info, classes = resolve_psi_class(blocks, n, tau, psis[j - 1], os.path.join(out, f"res_{it}_{name}.cnf"))
            rec[name] = info
            if classes is None:
                ok = False
                cnf.add([-rv[i] for i in sel if M.rows[i][0] == j])
                break
            check_resolution(blocks, n, classes)
            resolved.append((classes, closure([mg] if j == 0 else [tau], n)))
        print(json.dumps(rec), flush=True)
        if not ok:
            continue
        cons = develop(M.G, resolved, n)
        cert = os.path.join(out, f"lkts{n}_struct.txt")
        write_certificate(cons, n, cert, header_comment=f"LKTS({n}) structured-B ansatz q={q}")
        chk = subprocess.run([sys.executable, os.path.join(HERE, "check_lkts57.py"), cert], capture_output=True, text=True)
        rec["checker"] = json.loads(chk.stdout)["result"]
        json.dump({"bases": [sorted(b) for b in bases]}, open(os.path.join(out, "km_solution.json"), "w"))
        json.dump([c for c, _ in resolved], open(os.path.join(out, "base_resolutions.json"), "w"))
        print("CHECKER", rec["checker"], flush=True)
        break
    log["seconds"] = round(time.time() - t0, 2)
    json.dump(log, open(os.path.join(out, "pipeline_log.json"), "w"), indent=1)


if __name__ == "__main__":
    main()

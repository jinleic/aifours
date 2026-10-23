#!/usr/bin/env python3
"""R3: SQS(2q+2) on F_q x {0,1} ∪ {∞0, ∞1} invariant under G = <x->x+b, x->c x (c in C)>
acting identically on both copies (∞'s fixed), optionally with the swap σ
((x,0)<->(x,1), ∞0<->∞1).  Resolutions at point-orbit representatives with class
symmetry R (subgroup of the stabilizer) and anchor-forced class structure.

Usage: r3_pipeline.py q OUT --c-order k [--swap] [--rinf SPEC] [--rfin SPEC]
       [--samples K] [--seed0 S] [--res-timeout T] [--workers W]
SPEC for --rinf: "full" (= translations ⋊ C_r with r = --rinf-c) ; --rfin: order r of C_r ≤ C.
"""
import argparse
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mult_pipeline import sym_model
from rdsqs_lib import SQSKM, closure, derived, kissat, transport, verify_resolution, write_certificate
import symres


class Field:
    def __init__(self, q):
        self.q = q
        if q == 25:
            import pg125 as F
            self.add, self.mul = F.add, F.mul
            self.addgens = [1, 5]
        else:
            self.add = lambda x, y: (x + y) % q
            self.mul = lambda x, y: (x * y) % q
            self.addgens = [1]
        self.els = list(range(q))

    def order(self, x):
        k, y = 1, x
        while y != 1:
            y = self.mul(y, x)
            k += 1
        return k

    def subgroup_gen(self, k):
        """generator of the unique cyclic subgroup of order k of F_q*."""
        return next(x for x in range(1, self.q) if self.order(x) == k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("q", type=int)
    ap.add_argument("out")
    ap.add_argument("--c-order", type=int, required=True)
    ap.add_argument("--swap", action="store_true")
    ap.add_argument("--rinf-c", type=int, default=None, help="order r: R at ∞0 = translations ⋊ C_r")
    ap.add_argument("--rfin-c", type=int, default=None, help="order r: R at (0,0) = C_r")
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--res-timeout", type=int, default=120)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    F = Field(a.q)
    q = a.q
    v = 2 * q + 2
    I0, I1 = 2 * q, 2 * q + 1

    def lift(f):  # x -> f(x) on both copies
        return tuple([f(x) for x in range(q)] + [f(x) + q for x in range(q)] + [I0, I1])

    trans = [lift(lambda x, b=b: F.add(x, b)) for b in F.addgens]
    c = F.subgroup_gen(a.c_order) if a.c_order > 1 else 1
    mults = [lift(lambda x: F.mul(c, x))] if a.c_order > 1 else []
    swap = tuple([x + q for x in range(q)] + [x for x in range(q)] + [I1, I0])
    gens = trans + mults + ([swap] if a.swap else [])
    os.makedirs(a.out, exist_ok=True)
    t0 = time.time()
    M = SQSKM(v, gens)
    G = closure(gens, v)
    # point orbits and representatives
    reps = [I0, 0] if a.swap else [I0, I1, 0, q]
    # R at ∞0 and at (0,0)
    rinf_c = a.rinf_c if a.rinf_c is not None else a.c_order
    rfin_c = a.rfin_c if a.rfin_c is not None else a.c_order
    cinf = F.subgroup_gen(rinf_c) if rinf_c > 1 else 1
    cfin = F.subgroup_gen(rfin_c) if rfin_c > 1 else 1
    Rinf = closure(trans + ([lift(lambda x: F.mul(cinf, x))] if rinf_c > 1 else []), v)
    Rfin = closure([lift(lambda x: F.mul(cfin, x))] if rfin_c > 1 else [], v) if rfin_c > 1 else [tuple(range(v))]
    rspec = {}
    for r in reps:
        if r in (I0, I1):
            other = I1 if r == I0 else I0
            rspec[r] = (Rinf, other)
        else:
            rspec[r] = (Rfin, I0)
    summ = {"model": "R3", "q": q, "v": v, "c_order": a.c_order, "swap": a.swap, "G_order": len(G),
            "reps": reps, "R_orders": {str(r): len(rspec[r][0]) for r in reps}, "km": M.summary(),
            "args": vars(a), "samples": []}
    print(json.dumps({"G": len(G), "km": {k: summ["km"][k] for k in ("triple_orbits", "valid_rows")},
                      "R": summ["R_orders"]}), flush=True)
    cnf, rv = M.cnf()
    jobs = []
    for i in range(a.samples):
        p = os.path.join(a.out, f"km_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, 600, seed=a.seed0 + i)
        rec = {"sample": i, "km_seed": a.seed0 + i, "km_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3),
               "res": {}}
        summ["samples"].append(rec)
        if st != "SAT":
            print(json.dumps({k: rec[k] for k in ("sample", "km_status", "km_seconds")}), flush=True)
            break
        sel = [j for j, x in enumerate(rv) if x in model]
        rec["rows"] = sel
        cnf.add([-rv[j] for j in sel])
        blocks = M.blocks_of(sel)
        for r in reps:
            R, anchor = rspec[r]
            der = derived(blocks, r)
            pts = [p for p in range(v) if p != r]
            if len(R) > 1:
                rc, orbits, choice, cosets, stb, osz = sym_model(der, pts, R, anchor)
            else:
                from rdsqs_lib import resolution_cnf
                rc, tv = resolution_cnf(der, pts, (v - 2) // 2, anchor=anchor)
                orbits = choice = cosets = stb = None
                osz = [1] * ((v - 2) // 2)
            rp = os.path.join(a.out, f"res_{i}_p{r}.cnf")
            sha2 = rc.write(rp)
            rec["res"][str(r)] = {"cnf_sha256": sha2, "vars": rc.nv, "class_orbits": sorted(osz)}
            jobs.append((i, r, rp, der, pts, R, (orbits, choice, cosets, stb), blocks))
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)

    def run(job):
        st, model, dt = kissat(job[2], a.res_timeout, seed=1, log=job[2] + ".log")
        return job, st, model, dt

    resolved = {}
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for job, st, model, dt in ex.map(run, jobs):
            i, r, rp, der, pts, R, dec, blocks = job
            rr = summ["samples"][i]["res"][str(r)]
            rr["status"], rr["seconds"] = st, round(dt, 3)
            if st == "SAT":
                if dec[0] is None:
                    raise SystemExit("plain decode not wired for R3")
                classes = symres.decode(model, dec[0], dec[1], dec[2], dec[3], R)
                verify_resolution(der, pts, classes)
                resolved.setdefault(i, {})[r] = classes
            print(json.dumps({"sample": i, "point": r, **rr}), flush=True)
    found = []
    for i, rs in sorted(resolved.items()):
        if set(rs) == set(reps):
            job_blocks = next(j[7] for j in jobs if j[0] == i)
            res = transport(G, rs, v)
            cert = os.path.join(a.out, f"rdsqs{v}_r3_sample{i}.txt")
            summ["samples"][i]["certificate_sha256"] = write_certificate(
                cert, v, job_blocks, res, f"RDSQS({v}) candidate: R3 q={q} |C|={a.c_order} swap={a.swap} sample {i}")
            chk = subprocess.run([sys.executable, os.path.join(HERE, "check_rdsqs.py"), cert], capture_output=True, text=True)
            summ["samples"][i]["checker"] = json.loads(chk.stdout)["result"]
            found.append(i)
            print("CERT", cert, summ["samples"][i]["checker"], flush=True)
    summ["found"] = found
    summ["total_seconds"] = round(time.time() - t0, 2)
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    print("FOUND", found, "total_seconds", summ["total_seconds"], flush=True)


if __name__ == "__main__":
    main()

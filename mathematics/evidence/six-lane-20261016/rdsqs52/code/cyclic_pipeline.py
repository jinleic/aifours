#!/usr/bin/env python3
"""Cyclic (optionally multiplier-extended) SQS(v) -> derived resolution at 0 -> RDSQS certificate.

Usage:
  cyclic_pipeline.py V OUTDIR [--mult m1,m2,...] [--samples K] [--seed0 S]
                     [--res-timeout T] [--workers W] [--km-timeout T] [--stop-first]

Steps (all inputs deterministic; seeds recorded):
 1. G = <x->x+1, x->m*x (m in --mult)> on Z_V; Kramer–Mesner model (rdsqs_lib.SQSKM).
 2. Sample up to K SQS solutions: kissat seed S+i, blocking clause on the chosen row set.
 3. For each sample, the derived design at 0 -> unrestricted resolution CNF (anchor = point 1).
 4. Run the resolution CNFs on W workers with cap T seconds each.
 5. For every SAT resolution: verify, transport by G, write certificate, run check_rdsqs.py.
Writes OUTDIR/summary.json (+ per-sample records); CNFs stay in OUTDIR.
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
from rdsqs_lib import (SQSKM, closure, decode_resolution, derived, kissat, resolution_cnf, transport,
                       verify_resolution, write_certificate)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("v", type=int)
    ap.add_argument("out")
    ap.add_argument("--mult", default="")
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--res-timeout", type=int, default=60)
    ap.add_argument("--km-timeout", type=int, default=600)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--stop-first", action="store_true")
    a = ap.parse_args()
    v = a.v
    os.makedirs(a.out, exist_ok=True)
    mults = [int(m) for m in a.mult.split(",") if m]
    gens = [tuple((x + 1) % v for x in range(v))] + [tuple((m * x) % v for x in range(v)) for m in mults]
    t0 = time.time()
    M = SQSKM(v, gens)
    summ = {"v": v, "mult": mults, "km": M.summary(), "km_build_seconds": round(time.time() - t0, 2),
            "args": vars(a), "samples": []}
    print(json.dumps(summ["km"]), flush=True)
    cnf, rv = M.cnf()
    jobs = []
    for i in range(a.samples):
        p = os.path.join(a.out, f"km_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, a.km_timeout, seed=a.seed0 + i)
        rec = {"sample": i, "km_seed": a.seed0 + i, "km_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3)}
        summ["samples"].append(rec)
        if st != "SAT":
            print(json.dumps(rec), flush=True)
            break
        sel = [j for j, x in enumerate(rv) if x in model]
        cnf.add([-rv[j] for j in sel])
        blocks = M.blocks_of(sel)
        assert len(blocks) == v * (v - 1) * (v - 2) // 24
        der = derived(blocks, 0)
        pts = list(range(1, v))
        rc, tv = resolution_cnf(der, pts, (v - 2) // 2, anchor=1)
        rp = os.path.join(a.out, f"res_{i}.cnf")
        rec["res_cnf_sha256"] = rc.write(rp)
        rec["res_vars"] = rc.nv
        rec["res_clauses"] = len(rc.clauses)
        rec["rows"] = sel
        jobs.append((i, rp, der, pts, tv, blocks))
    summ["km_sampling_seconds"] = round(time.time() - t0, 2)
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)

    def run(job):
        i, rp, der, pts, tv, blocks = job
        st, model, dt = kissat(rp, a.res_timeout, seed=1, log=rp + ".log")
        return job, st, model, dt

    found = []
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for job, st, model, dt in ex.map(run, jobs):
            i, rp, der, pts, tv, blocks = job
            rec = summ["samples"][i]
            rec["res_status"] = st
            rec["res_seconds"] = round(dt, 3)
            if st == "SAT":
                classes = decode_resolution(model, der, tv, (v - 2) // 2)
                verify_resolution(der, pts, classes)
                G = closure(gens, v)
                res = transport(G, {0: classes}, v)
                cert = os.path.join(a.out, f"rdsqs{v}_sample{i}.txt")
                rec["certificate_sha256"] = write_certificate(
                    cert, v, blocks, res, f"RDSQS({v}) candidate: cyclic pipeline sample {i}, mult={mults}")
                chk = subprocess.run([sys.executable, os.path.join(HERE, "check_rdsqs.py"), cert],
                                     capture_output=True, text=True)
                rec["checker"] = json.loads(chk.stdout)["result"]
                found.append(i)
            print(json.dumps({k: rec[k] for k in rec if k != "rows"}), flush=True)
            json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    summ["found"] = found
    summ["total_seconds"] = round(time.time() - t0, 2)
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    print("FOUND", found, "total_seconds", summ["total_seconds"], flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""R2: doubling of a cyclic (multiplier-extended) SQS(26) to an SQS(52), resolution of the
derived design at (0,0) with an R-invariant class structure, transport by Z26 x Z2.

Points: (y,i) in Z26 x F2 encoded y + 26 i.  Doubled blocks (classical doubling):
  (i)  for every block {a,b,c,d} of the SQS(26) and every (i,j,k,l) in F2^4 with
       i+j+k+l = 0:  {(a,i),(b,j),(c,k),(d,l)}            (8 per block)
  (ii) for every pair {x,y} of Z26:  {(x,0),(x,1),(y,0),(y,1)}
The SQS(52) is invariant under (y,i)->(y+1,i) and (y,i)->(y,i+1) (regular action of
Z26 x Z2), so the resolution at (x,i) is the image of the resolution at (0,0).
R = multipliers (y,i)->(m y,i) of the SQS(26) (they fix (0,0)); the class structure is
forced by the R-orbits of derived triples through the anchor (0,1) (see mult_pipeline).

Usage: doubling_pipeline.py OUT --mult m1,... [--res-mult r1,...] [--samples K]
       [--seed0 S] [--res-timeout T] [--workers W]
"""
import argparse
import itertools
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mult_pipeline import sym_model
from rdsqs_lib import (SQSKM, closure, decode_resolution, derived, kissat, resolution_cnf, transport,
                       verify_resolution, write_certificate)
import symres

Y = int(os.environ.get("DOUBLING_Y", "26"))
N = 2 * Y


def double(blocks26):
    out = set()
    for b in blocks26:
        for bits in itertools.product((0, 1), repeat=4):
            if sum(bits) % 2 == 0:
                out.add(tuple(sorted(p + Y * e for p, e in zip(b, bits))))
    for x, y in itertools.combinations(range(Y), 2):
        out.add(tuple(sorted((x, x + Y, y, y + Y))))
    return sorted(out)


def quick_sqs_check(blocks, n):
    seen = set()
    for b in blocks:
        for t in itertools.combinations(b, 3):
            assert t not in seen, "triple covered twice"
            seen.add(t)
    assert len(seen) == n * (n - 1) * (n - 2) // 6
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--mult", default="")
    ap.add_argument("--res-mult", default=None)
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--res-timeout", type=int, default=120)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    mults = [int(m) for m in a.mult.split(",") if m]
    rmults = mults if a.res_mult is None else [int(m) for m in a.res_mult.split(",") if m]
    gens26 = [tuple((x + 1) % Y for x in range(Y))] + [tuple((m * x) % Y for x in range(Y)) for m in mults]
    rperm = lambda m: tuple((m * (p % Y)) % Y + Y * (p // Y) for p in range(N))
    R = closure([rperm(m) for m in rmults], N) if rmults else [tuple(range(N))]
    G52 = closure([tuple((p % Y + 1) % Y + Y * (p // Y) for p in range(N)),
                   tuple(p % Y + Y * (1 - p // Y) for p in range(N))], N)
    assert len(G52) == N
    t0 = time.time()
    M = SQSKM(Y, gens26)
    summ = {"model": "R2 doubling of cyclic SQS(26)", "mult": mults, "res_mult": rmults, "R_order": len(R),
            "km26": M.summary(), "args": vars(a), "samples": []}
    print(json.dumps({"km26": summ["km26"], "R_order": len(R)}), flush=True)
    cnf, rv = M.cnf()
    pts = list(range(1, N))
    anchor = Y  # (0,1)
    jobs = []
    for i in range(a.samples):
        p = os.path.join(a.out, f"km26_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, 120, seed=a.seed0 + i)
        rec = {"sample": i, "km_seed": a.seed0 + i, "km26_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3)}
        summ["samples"].append(rec)
        if st != "SAT":
            print(json.dumps(rec), flush=True)
            break
        sel = [j for j, x in enumerate(rv) if x in model]
        rec["rows26"] = sel
        cnf.add([-rv[j] for j in sel])
        b26 = M.blocks_of(sel)
        rec["sqs26_blocks"] = b26
        blocks = double(b26)
        quick_sqs_check(blocks, N)
        der = derived(blocks, 0)
        rp = os.path.join(a.out, f"res_{i}.cnf")
        if len(R) > 1:
            rc, orbits, choice, cosets, stb, osz = sym_model(der, pts, R, anchor)
            rec["class_orbit_sizes"] = sorted(osz)
            dec = ("sym", orbits, choice, cosets, stb)
        else:
            rc, tv = resolution_cnf(der, pts, (N - 2) // 2, anchor=anchor)
            dec = ("plain", tv)
        rec["res_cnf_sha256"] = rc.write(rp)
        rec["res_vars"] = rc.nv
        jobs.append((i, rp, der, blocks, dec))
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)

    def run(job):
        st, model, dt = kissat(job[1], a.res_timeout, seed=1, log=job[1] + ".log")
        return job, st, model, dt

    found = []
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for job, st, model, dt in ex.map(run, jobs):
            i, rp, der, blocks, dec = job
            rec = summ["samples"][i]
            rec["res_status"] = st
            rec["res_seconds"] = round(dt, 3)
            if st == "SAT":
                if dec[0] == "sym":
                    classes = symres.decode(model, dec[1], dec[2], dec[3], dec[4], R)
                else:
                    classes = decode_resolution(model, der, dec[1], (N - 2) // 2)
                verify_resolution(der, pts, classes)
                res = transport(G52, {0: classes}, N)
                cert = os.path.join(a.out, f"rdsqs{N}_doubling_sample{i}.txt")
                rec["certificate_sha256"] = write_certificate(
                    cert, N, blocks, res,
                    f"RDSQS({N}) candidate: doubling of SQS({Y}) (Z{Y} x| <{mults}>), R=<{rmults}>, sample {i}")
                chk = subprocess.run([sys.executable, os.path.join(HERE, "check_rdsqs.py"), cert],
                                     capture_output=True, text=True)
                rec["checker"] = json.loads(chk.stdout)["result"]
                found.append(i)
            print(json.dumps({k: rec[k] for k in rec if k not in ("rows26", "sqs26_blocks")}), flush=True)
            json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    summ["found"] = found
    summ["total_seconds"] = round(time.time() - t0, 2)
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)
    print("FOUND", found, "total_seconds", summ["total_seconds"], flush=True)


if __name__ == "__main__":
    main()

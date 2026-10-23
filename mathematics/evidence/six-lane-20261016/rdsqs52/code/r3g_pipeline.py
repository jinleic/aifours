#!/usr/bin/env python3
"""R3γ (frozen in README §4): R3 at q=25 with C=<ω> (order 3) and the copy swap, plus a
LOCAL order-3 symmetry γ of the derived design D at (0,0) imposed through equalities
between Kramer–Mesner row variables.  Resolution at (0,0) invariant under R=<ω,γ>
(anchor ∞0); at ∞0 invariant under the translations (anchor ∞1); transport by G.

Usage: r3g_pipeline.py OUT --gamma-seed S [--m 4] [--km-samples K] [--res-timeout T] [--workers W]
"""
import argparse
import json
import os
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mult_pipeline import sym_model
from r3_pipeline import Field
from rdsqs_lib import SQSKM, closure, comp, derived, kissat, rank, transport, verify_resolution, write_certificate
import symres

Q, V, I0, I1 = 25, 52, 50, 51


def make_gamma(F, w, seed, m):
    """Return (gamma permutation on 52 points, description)."""
    rng = random.Random(seed)
    wp = [1, w, F.mul(w, w)]
    seen, reps = set(), []
    for x in range(1, Q):
        if x not in seen:
            reps.append(x)
            seen |= {F.mul(x, e) for e in wp}
    cycles = [(r, j) for r in reps for j in (0, 1)]          # 16 ω-cycles
    pt = lambda r, i, j: F.mul(r, wp[i % 3]) + Q * j
    idx = list(range(16)); rng.shuffle(idx)
    fixed = idx[:16 - 3 * m]
    trip = [idx[16 - 3 * m + 3 * t: 16 - 3 * m + 3 * t + 3] for t in range(m)]
    # twists on fixed cycles: each value an even number of times, counts <= 6
    nf = len(fixed)
    while True:
        tw = [rng.randrange(3) for _ in range(nf)]
        cnt = [tw.count(a) for a in range(3)]
        if all(c % 2 == 0 and c <= 6 for c in cnt):
            break
    g = list(range(V))
    for c, k in zip(fixed, tw):
        r, j = cycles[c]
        for i in range(3):
            g[pt(r, i, j)] = pt(r, i + k, j)
    desc_trip = []
    for t in trip:
        s1, s2 = rng.randrange(3), rng.randrange(3)
        s3 = (-s1 - s2) % 3
        for (ca, cb, s) in ((t[0], t[1], s1), (t[1], t[2], s2), (t[2], t[0], s3)):
            ra, ja = cycles[ca]
            rb, jb = cycles[cb]
            for i in range(3):
                g[pt(ra, i, ja)] = pt(rb, i + s, jb)
        desc_trip.append({"cycles": [cycles[c] for c in t], "shifts": [s1, s2, s3]})
    desc = {"seed": seed, "m": m, "fixed_cycles": [cycles[c] for c in fixed], "twists": tw, "three_cycles": desc_trip}
    return tuple(g), desc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--gamma-seed", type=int, required=True)
    ap.add_argument("--m", type=int, default=4)
    ap.add_argument("--km-samples", type=int, default=4)
    ap.add_argument("--res-timeout", type=int, default=300)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    F = Field(Q)
    w = F.subgroup_gen(3)
    lift = lambda f: tuple([f(x) for x in range(Q)] + [f(x) + Q for x in range(Q)] + [I0, I1])
    trans = [lift(lambda x, b=b: F.add(x, b)) for b in F.addgens]
    mult = lift(lambda x: F.mul(w, x))
    swap = tuple([x + Q for x in range(Q)] + [x for x in range(Q)] + [I1, I0])
    gens = trans + [mult, swap]
    gamma, gdesc = make_gamma(F, w, a.gamma_seed, a.m)
    assert comp(gamma, mult) == comp(mult, gamma), "γ must commute with ω"
    assert comp(gamma, comp(gamma, gamma)) == tuple(range(V)) and gamma != tuple(range(V))
    R = closure([mult, gamma], V)
    assert len(R) == 9 and all(g[0] == 0 for g in R)
    fixsizes = sorted({sum(1 for p in range(1, V) if g[p] == p) for g in R if g != tuple(range(V))})
    assert set(fixsizes) <= {3, 9, 15, 21}, fixsizes
    t0 = time.time()
    M = SQSKM(V, gens)
    rowidx = {lab: i for i, (lab, _) in enumerate(M.rows)}
    cnf, rv = M.cnf()
    # γ-invariance of D at point 0
    from itertools import combinations
    trip = np.array(list(combinations(range(1, V), 3)), dtype=np.int64)
    quads = np.concatenate([np.zeros((len(trip), 1), dtype=np.int64), trip], axis=1)
    garr = np.asarray(gamma, dtype=np.int64)
    lab1 = M.LQ[rank(quads)]
    lab2 = M.LQ[rank(garr[quads])]
    pairs, forced = set(), set()
    for l1, l2 in zip(lab1.tolist(), lab2.tolist()):
        r1, r2 = rowidx.get(l1), rowidx.get(l2)
        if r1 == r2:
            continue
        if r1 is None:
            forced.add(r2)
        elif r2 is None:
            forced.add(r1)
        else:
            pairs.add((min(r1, r2), max(r1, r2)))
    for r in forced:
        cnf.add([-rv[r]])
    for r1, r2 in pairs:
        cnf.add([-rv[r1], rv[r2]])
        cnf.add([rv[r1], -rv[r2]])
    summ = {"model": "R3gamma", "gamma": gdesc, "gamma_perm": list(gamma), "R_fixed_set_sizes": fixsizes,
            "km": M.summary(), "gamma_equalities": len(pairs), "gamma_forced_false": len(forced),
            "args": vars(a), "samples": []}
    print(json.dumps({"gamma_seed": a.gamma_seed, "eq": len(pairs), "forced": len(forced), "fix": fixsizes}), flush=True)
    G = closure(gens, V)
    Rinf = closure(trans, V)
    jobs = []
    for i in range(a.km_samples):
        p = os.path.join(a.out, f"km_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, 600, seed=i)
        rec = {"sample": i, "km_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3), "res": {}}
        summ["samples"].append(rec)
        print(json.dumps({k: rec[k] for k in ("sample", "km_status", "km_seconds")}), flush=True)
        if st != "SAT":
            break
        sel = [j for j, x in enumerate(rv) if x in model]
        rec["rows"] = sel
        cnf.add([-rv[j] for j in sel])
        blocks = M.blocks_of(sel)
        der0 = derived(blocks, 0)
        dset = set(der0)
        assert all(tuple(sorted(gamma[p] for p in t)) in dset for t in der0), "D not γ-invariant"
        for r, RR, anchor in ((0, R, I0), (I0, Rinf, I1)):
            der = der0 if r == 0 else derived(blocks, r)
            pts = [x for x in range(V) if x != r]
            rc, orbits, choice, cosets, stb, osz = sym_model(der, pts, RR, anchor)
            rp = os.path.join(a.out, f"res_{i}_p{r}.cnf")
            rec["res"][str(r)] = {"cnf_sha256": rc.write(rp), "vars": rc.nv, "class_orbits": sorted(osz)}
            jobs.append((i, r, rp, der, pts, RR, (orbits, choice, cosets, stb), blocks))
    json.dump(summ, open(os.path.join(a.out, "summary.json"), "w"), indent=1)

    def run(job):
        st, model, dt = kissat(job[2], a.res_timeout, seed=1, log=job[2] + ".log")
        return job, st, model, dt

    resolved = {}
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for job, st, model, dt in ex.map(run, jobs):
            i, r, rp, der, pts, RR, dec, blocks = job
            rr = summ["samples"][i]["res"][str(r)]
            rr["status"], rr["seconds"] = st, round(dt, 3)
            if st == "SAT":
                classes = symres.decode(model, dec[0], dec[1], dec[2], dec[3], RR)
                verify_resolution(der, pts, classes)
                resolved.setdefault(i, {})[r] = (classes, blocks)
            print(json.dumps({"sample": i, "point": r, **rr}), flush=True)
    found = []
    for i, rs in sorted(resolved.items()):
        if set(rs) == {0, I0}:
            blocks = rs[0][1]
            res = transport(G, {r: c for r, (c, _) in rs.items()}, V)
            cert = os.path.join(a.out, f"rdsqs52_r3g_seed{a.gamma_seed}_sample{i}.txt")
            summ["samples"][i]["certificate_sha256"] = write_certificate(
                cert, V, blocks, res, f"RDSQS(52) candidate: R3gamma q=25 C3+swap, gamma seed {a.gamma_seed}, sample {i}")
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

#!/usr/bin/env python3
"""CQS(g^4 : 0) invariant under a prescribed group (Kramer–Mesner, kissat), then a good colouring
of the derived design at x = (0,0) invariant under R (README §3), transported by the group to all
points, written as a GCDCQS certificate and checked by code/check_gcdcqs.py.

Every CNF / kissat log / record is retained (exclusive create); the output directory must be new.
Usage: pipeline.py OUT --g G --group A4xC [--res C3|1] [--avoid SPEC[,SPEC...]] [--samples K]
       [--seed0 S] [--km-timeout T] [--col-timeout T] [--workers W]
SPEC: ';'-separated stabilizers of the hole-avoiding class orbits, each 'R' (whole R) or '1'.
"""
import lane_guard  # noqa: F401

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import fresh_dir, xopen
from lanelib import closure, gcsts_params, kissat, sha256_file
from cqs_km import CQSKM
import colour_model as cm
import groups as grp


def derived(blocks, x):
    return sorted(tuple(p for p in b if p != x) for b in blocks if x in b)


def certificate_text(v, n, g, r, s, groups_, blocks, col, header):
    lines = [f"# {header}", f"GCDCQS {v} {n} {g}", f"COLOURS {r}", f"HOLEFREE {s}", "GROUPS"]
    lines += [" ".join(map(str, G)) for G in groups_]
    lines.append("BLOCKS")
    lines += [" ".join(map(str, b)) for b in sorted(tuple(sorted(b)) for b in blocks)]
    for y in range(v):
        lines.append(f"POINT {y}")
        for j, C in enumerate(col[y]):
            lines.append(f"CLASS {j}")
            lines += [" ".join(map(str, t)) for t in C]
    return "\n".join(lines) + "\n"


def transport(G, classes0, x0, v):
    out = {}
    for gg in G:  # G sorted: least element mapping x0 to y
        y = gg[x0]
        if y not in out:
            out[y] = [sorted(tuple(sorted(gg[p] for p in t)) for t in C) for C in classes0]
    assert sorted(out) == list(range(v)), "group is not transitive"
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--g", type=int, required=True)
    ap.add_argument("--group", default="A4xC")
    ap.add_argument("--res", default="C3")
    ap.add_argument("--avoid", default="R")
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--km-timeout", type=int, default=600)
    ap.add_argument("--col-timeout", type=int, default=300)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    fresh_dir(a.out)
    progress = xopen(os.path.join(a.out, "progress.jsonl"))

    def log(rec):
        progress.write(json.dumps(rec) + "\n")
        progress.flush()
        print(json.dumps(rec), flush=True)

    n, g = 4, a.g
    v = n * g
    r, s = gcsts_params(v - 1, g - 1)
    spec = grp.build(a.group, n, g)
    gens, group_of, groups_ = spec["gens"], spec["group_of"], spec["groups"]
    x0, h = 0, 1  # (0,0) and the anchor (0,1)
    Rg = spec["res"][a.res]
    R = closure(Rg, v) if Rg else [tuple(range(v))]
    assert all(e[x0] == x0 and e[h] == h for e in R), "R must fix x and the anchor"
    G = closure(gens, v)
    assert set(R) <= set(G)
    avoid_specs = [sp.split(";") for sp in a.avoid.split(",")]
    for sp in avoid_specs:
        assert all(t in ("R", "1") for t in sp)
        assert sum(1 if t == "R" else len(R) for t in sp) == s, f"avoid spec {sp} does not give {s} classes"
    t0 = time.time()
    km = CQSKM(v, group_of, gens)
    summ = {"v": v, "n": n, "g": g, "r": r, "s": s, "group": a.group, "group_order": len(G),
            "res": a.res, "R_order": len(R), "avoid_specs": avoid_specs, "km": km.summary(),
            "args": vars(a), "samples": []}
    log({"km": summ["km"], "group_order": len(G), "R_order": len(R), "r": r, "s": s})
    cnf, rv = km.cnf()
    hole = [p for p in range(v) if group_of[p] == group_of[x0] and p != x0]
    pts = [p for p in range(v) if p != x0]
    jobs = []
    for i in range(a.samples):
        p = os.path.join(a.out, f"km_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, a.km_timeout, seed=a.seed0 + i, log=p + ".log")
        rec = {"sample": i, "km_seed": a.seed0 + i, "km_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3)}
        summ["samples"].append(rec)
        if st != "SAT":
            log(rec)
            break
        sel = [j for j, x in enumerate(rv) if x in model]
        rec["rows"] = sel
        cnf.add([-rv[j] for j in sel])
        blocks = km.blocks_of(sel)
        der = derived(blocks, x0)
        rec["blocks"] = len(blocks)
        rec["colourings"] = []
        for k, sp in enumerate(avoid_specs):
            avoid_stabs = [R if t == "R" else [tuple(range(v))] for t in sp]
            rc, orbits, choice, cosets, stb, sizes = cm.anchored(der, pts, hole, R, h, avoid_stabs)
            cp = os.path.join(a.out, f"col_{i}_{k}.cnf")
            csha = rc.write(cp)
            rec["colourings"].append({"avoid": sp, "class_orbit_sizes": sizes, "triple_orbits": len(orbits),
                                      "col_cnf_sha256": csha, "col_vars": rc.nv, "col_clauses": len(rc.clauses)})
            jobs.append((i, k, cp, der, blocks, (orbits, choice, cosets, stb)))
        log({kk: rec[kk] for kk in rec if kk != "rows"})

    def run(job):
        st, model, dt = kissat(job[2], a.col_timeout, seed=1, log=job[2] + ".log")
        return job, st, model, dt

    found = []
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        for job, st, model, dt in ex.map(run, jobs):
            i, k, cp, der, blocks, dec = job
            crec = summ["samples"][i]["colourings"][k]
            crec["col_status"], crec["col_seconds"] = st, round(dt, 3)
            if st == "SAT":
                classes = cm.decode(model, *dec, R)
                cm.verify_good_colouring(der, pts, hole, classes, r, s)
                crec["class_sizes_at_x"] = [len(C) for C in classes]
                col = transport(G, classes, x0, v)
                cert = os.path.join(a.out, f"gcdcqs{g}_s{i}_a{k}.txt")
                text = certificate_text(v, n, g, r, s, groups_, blocks, col,
                                        f"gcDCQS({g}^4:0) candidate: group {a.group} (order {len(G)}), "
                                        f"R={a.res}, avoid={';'.join(avoid_specs[k])}, KM sample {i}")
                with xopen(cert) as fh:
                    fh.write(text)
                crec["certificate"] = cert
                crec["certificate_sha256"] = hashlib.sha256(text.encode()).hexdigest()
                chk = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs.py"), cert],
                                     capture_output=True, text=True)
                crec["checker"] = json.loads(chk.stdout)["result"]
                found.append((i, k))
            log({"sample": i, "avoid_index": k, **{kk: crec[kk] for kk in crec if kk != "avoid"}})
    summ["found"] = found
    summ["total_seconds"] = round(time.time() - t0, 2)
    with xopen(os.path.join(a.out, "summary.json")) as fh:
        json.dump(summ, fh, indent=1)
    print("FOUND", found, "total_seconds", summ["total_seconds"], flush=True)


if __name__ == "__main__":
    main()

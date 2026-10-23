#!/usr/bin/env python3
"""README A0b: gcDCQS(g^4 : 2) pipeline in the cyclic model of Tan–Zhou Lemma 3.1 (numpy + kissat).

Group points Z_{4g}, group i = {a : a ≡ i (mod 4)}, stems 4g, 4g+1.  rho: a -> a + 1 on Z_{4g} and swaps the
stems (as (0 1 ... 31)(a b) in Lemma 3.1); optional multipliers u ≡ 1 (mod 4) (a -> u a, stems fixed).  Lemma I
is re-checked on all elements.  Kramer–Mesner by code/cqs_km_s.py; colouring at the representative of each
group-point orbit with R = its stabilizer, anchor = stem 4g (fixed by R); transport by the least e in G; stem
frames = orbits of <rho^4> (preserves groups, regular on each group, fixes the stems: Lemma K).  Format S output
with GROUPS lines i, i+4, ..., checked by route 1 (and route 2 if present).
Usage: pipeline_s3.py OUT --g G [--mult u,...] [--avoid SPEC|...] [--samples K] [--seed0 S] [--km-timeout T]
       [--col-timeout T] [--col-seed S] [--strengthen] [--profile P10] [--no-solve] [--stop-on-first]
       [--model-from LOG|...]"""
import lane_guard  # noqa: F401

import argparse
import collections
import hashlib
import json
import math
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import closure, gcsts_params, kissat, model_satisfies, parse_status  # noqa: E402
from cqs_km_s import CQSKMS  # noqa: E402
import colour_model as cm  # noqa: E402
from pipeline_s import derived  # noqa: E402
from pipeline_s2 import cyclic_subgroup, lemma_i_violations  # noqa: E402


def cert_text(v, g, r, s, blocks, col, frames, header):
    N = 4 * g
    L = [f"# {header}", f"GCDCQS {v} 4 {g} 2", f"COLOURS {r}", f"HOLEFREE {s}", "GROUPS"]
    L += [" ".join(str(a) for a in range(i, N, 4)) for i in range(4)]
    L += ["STEM", f"{N} {N + 1}", "BLOCKS"]
    L += [" ".join(map(str, b)) for b in sorted(tuple(sorted(b)) for b in blocks)]
    for y in range(N):
        L.append(f"POINT {y}")
        for j, C in enumerate(col[y]):
            L.append(f"CLASS {j}")
            L += [" ".join(map(str, t)) for t in C]
    for a in (N, N + 1):
        L.append(f"STEMPOINT {a}")
        for k, C in frames[a]:
            L.append(f"FRAME {k}")
            L += [" ".join(map(str, t)) for t in C]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--g", type=int, required=True)
    ap.add_argument("--mult", default="")
    ap.add_argument("--avoid", default=None)
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--km-timeout", type=int, default=600)
    ap.add_argument("--col-timeout", type=int, default=600)
    ap.add_argument("--col-seed", type=int, default=1)
    ap.add_argument("--strengthen", action="store_true")
    ap.add_argument("--profile", default=None)
    ap.add_argument("--no-solve", action="store_true")
    ap.add_argument("--stop-on-first", action="store_true")
    ap.add_argument("--model-from", default=None)
    a = ap.parse_args()
    fresh_dir(a.out)
    prog = xopen(os.path.join(a.out, "progress.jsonl"))

    def log(rec):
        prog.write(json.dumps(rec) + "\n")
        prog.flush()
        print(json.dumps(rec), flush=True)

    g = a.g
    N, v = 4 * g, 4 * g + 2
    stems = (N, N + 1)
    group_of = [p % 4 for p in range(N)] + [-1, -1]
    rho = tuple([(p + 1) % N for p in range(N)] + [N + 1, N])
    gens = [rho]
    mults = [int(u) for u in a.mult.split(",") if u]
    for u in mults:
        assert u % 4 == 1 and math.gcd(u, N) == 1, "multipliers must be units ≡ 1 (mod 4)"
        gens.append(tuple([(u * p) % N for p in range(N)] + [N, N + 1]))
    G = closure(gens, v)
    rho4 = tuple([(p + 4) % N for p in range(N)] + [N, N + 1])
    Hreg = closure([rho4], v)
    nbad = lemma_i_violations(G, group_of, stems)
    r, s = gcsts_params(v - 1, g + 1)
    reps, seen = [], set()
    for p in range(N):
        if p not in seen:
            reps.append(p)
            seen |= {e[p] for e in G}
    info = {"v": v, "g": g, "r": r, "s": s, "group_order": len(G), "mult": mults, "lemma_I_violating_elements": nbad,
            "reps": reps}
    if nbad:
        log({**info, "stop": "Lemma I excludes every CQS invariant under this group"})
        return
    Rs = [[e for e in G if e[x] == x] for x in reps]
    anchor = N
    assert all(all(e[anchor] == anchor for e in R) for R in Rs)
    specs = a.avoid.split("|") if a.avoid else [None] * len(reps)
    stabs_all = []
    for x, R, sp in zip(reps, Rs, specs):
        toks = sp.split(";") if sp else [str(len(R))] * (s % len(R)) + ["1"] * ((s - s % len(R)) // len(R))
        stabs = [cyclic_subgroup(R, int(t)) for t in toks]
        assert sum(len(R) // len(st) for st in stabs) == s, f"avoid {toks} does not give {s} classes at x={x}"
        stabs_all.append((toks, stabs))
    info["R_orders"] = [len(R) for R in Rs]
    info["avoid"] = [";".join(t) for t, _ in stabs_all]
    t0 = time.time()
    km = CQSKMS(v, group_of, gens)
    summ = {**info, "km": km.summary(), "km_build_seconds": round(time.time() - t0, 2), "args": vars(a),
            "samples": [], "certificates": []}
    log({**info, "km": summ["km"], "km_build_seconds": summ["km_build_seconds"]})
    cnf, rv = km.cnf()
    models_from = a.model_from.split("|") if a.model_from else None
    for i in range(a.samples):
        p = os.path.join(a.out, f"km_{i}.cnf")
        sha = cnf.write(p)
        st, model, dt = kissat(p, a.km_timeout, seed=a.seed0 + i, log=p + ".log")
        rec = {"sample": i, "km_seed": a.seed0 + i, "km_cnf_sha256": sha, "km_vars": cnf.nv,
               "km_clauses": len(cnf.clauses), "km_status": st, "km_seconds": round(dt, 3)}
        summ["samples"].append(rec)
        if st != "SAT":
            log(rec)
            break
        sel = [j for j, xx in enumerate(rv) if xx in model]
        rec["rows"] = sel
        cnf.add([-rv[j] for j in sel])
        blocks = km.blocks_of(sel)
        rec["blocks"] = len(blocks)
        rec["block_types"] = dict(collections.Counter(
            "+".join(str(c) for c in sorted(collections.Counter(group_of[q] for q in b).values(), reverse=True))
            for b in blocks))
        jobs, rec["colourings"] = [], []
        for ri, (x, R, (toks, stabs)) in enumerate(zip(reps, Rs, stabs_all)):
            der = derived(blocks, x)
            hole = [q for q in range(v) if (group_of[q] == group_of[x] or group_of[q] == -1) and q != x]
            pts = [q for q in range(v) if q != x]
            rc, orbits, choice, cosets, stb, sizes = cm.anchored(der, pts, hole, R, anchor, stabs,
                                                                 strengthen=a.strengthen, profile=a.profile)
            cp = os.path.join(a.out, f"col_{i}_r{ri}.cnf")
            csha = rc.write(cp)
            rec["colourings"].append({"rep": x, "R_order": len(R), "avoid": ";".join(toks), "triple_orbits": len(orbits),
                                      "class_orbit_sizes": sizes, "col_cnf_sha256": csha, "col_vars": rc.nv,
                                      "col_clauses": len(rc.clauses)})
            jobs.append((cp, der, pts, hole, R, (orbits, choice, cosets, stb)))
        log({kk: rec[kk] for kk in rec if kk != "rows"})
        if a.no_solve:
            continue
        done = {}
        for ri, (cp, der, pts, hole, R, dec) in enumerate(jobs):
            if models_from:
                cst, cmodel = parse_status(open(models_from[ri]).read())
                assert cst == "SAT" and model_satisfies(cp, cmodel), "retained model does not satisfy the rebuilt CNF"
                cdt = 0.0
            else:
                cst, cmodel, cdt = kissat(cp, a.col_timeout, seed=a.col_seed, log=cp + ".log")
            rec["colourings"][ri].update({"col_status": cst, "col_seconds": round(cdt, 3)})
            log({"sample": i, "rep": reps[ri], "col_status": cst, "col_seconds": round(cdt, 3)})
            if cst != "SAT":
                break
            classes = cm.decode(cmodel, *dec, R)
            cm.verify_good_colouring(der, pts, hole, classes, r, s)
            done[ri] = classes
        if len(done) != len(reps):
            continue
        col = {}
        for ri, x in enumerate(reps):
            for e in G:
                y = e[x]
                if y not in col:
                    col[y] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in done[ri]]
        assert sorted(col) == list(range(N))
        frames = {}
        for al in stems:
            dset = set(derived(blocks, al))
            fr = []
            while dset:
                t = min(dset)
                orb = {tuple(sorted(e[q] for q in t)) for e in Hreg}
                assert orb <= dset
                dset -= orb
                k = ({0, 1, 2, 3} - {group_of[q] for q in t}).pop()
                fr.append((k, sorted(orb)))
            frames[al] = sorted(fr)
        cert = os.path.join(a.out, f"gcdcqs{g}_4_2_cyc_s{i}.txt")
        text = cert_text(v, g, r, s, blocks, col, frames,
                         f"gcDCQS({g}^4:2) candidate, cyclic model: G = <rho> x| <{','.join(map(str, mults))}> "
                         f"(order {len(G)}), KM sample {i} (seed {a.seed0 + i}), colouring seed {a.col_seed}, "
                         f"avoid {'|'.join(info['avoid'])}")
        with xopen(cert) as fh:
            fh.write(text)
        crt = {"sample": i, "certificate": cert, "sha256": hashlib.sha256(text.encode()).hexdigest()}
        chk = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs_s.py"), cert], capture_output=True, text=True)
        crt["route1"] = json.loads(chk.stdout)["result"]
        cbin = os.path.join(HERE, "bin", "check_gcdcqs_s_c")
        if os.path.exists(cbin):
            crt["route2"] = subprocess.run([cbin, cert], capture_output=True, text=True).stdout.strip()
        summ["certificates"].append(crt)
        log(crt)
        if a.stop_on_first and crt["route1"] == "PASS":
            break
    summ["total_seconds"] = round(time.time() - t0, 2)
    with xopen(os.path.join(a.out, "summary.json")) as fh:
        json.dump(summ, fh, indent=1)
    print("DONE", json.dumps({"certificates": summ["certificates"], "total_seconds": summ["total_seconds"]}), flush=True)


if __name__ == "__main__":
    main()

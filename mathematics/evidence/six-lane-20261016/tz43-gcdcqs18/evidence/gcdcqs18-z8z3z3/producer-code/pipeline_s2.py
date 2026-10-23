#!/usr/bin/env python3
"""README A0 (revised, after Lemma I): gcDCQS(g^4 : 2) pipeline with G = <pi1> x (C_g x| M), stems fixed.

Points (i, a) -> g*i + a, stems 4g, 4g+1.  pi1 = (1 2 3) on group indices; tau: a -> a + 1 and the multipliers
u in M (a -> u*a mod g) act on the coordinates of every group; stems fixed.  Lemma I is re-checked on every
element of G (an involution fixing the stems that swaps points of different groups must fix a group point
outside their groups).  Kramer–Mesner by code/cqs_km_s.py; colourings at one representative per group-point
orbit (least point of the orbit) with R = Stab_G(x), anchor = stem point 4g, hole-avoiding class orbits from
--avoid (per representative, '|'-separated; tokens = stabilizer orders of a cyclic R) or the default (f classes
fixed by R, f ≡ s mod |R| minimal, the rest in free orbits); transport by the least e in G with e(x) = y;
stem frames = orbits of the regular subgroup <tau> (Lemma K).  Format S output; route-1 checker (and route 2).
Usage: pipeline_s2.py OUT --g G [--mult u,u,...] [--no-pi1] [--avoid SPEC0|SPEC1] [--samples K] [--seed0 S]
       [--km-timeout T] [--col-timeout T] [--col-seed S] [--strengthen] [--profile P10] [--no-solve]
       [--stop-on-first] [--model-from LOG0|LOG1]"""
import lane_guard  # noqa: F401

import argparse
import collections
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import closure, comp, gcsts_params, kissat, model_satisfies, parse_status  # noqa: E402
from cqs_km_s import CQSKMS  # noqa: E402
import colour_model as cm  # noqa: E402
from pipeline_s import certificate_text, derived  # noqa: E402


def lift(g, imap, cmap):
    return tuple([g * imap[i] + cmap[a] for i in range(4) for a in range(g)] + [4 * g, 4 * g + 1])


def lemma_i_violations(G, group_of, stems):
    bad = 0
    for e in G:
        if comp(e, e) != tuple(range(len(e))) or any(e[a] != a for a in stems):
            continue
        fixed = [p for p in range(len(e)) if e[p] == p and group_of[p] >= 0]
        for y in range(len(e)):
            z = e[y]
            if group_of[y] >= 0 and z != y and group_of[z] != group_of[y]:
                if not any(group_of[w] not in (group_of[y], group_of[z]) for w in fixed):
                    bad += 1
                    break
    return bad


def cyclic_subgroup(R, order):
    ident = tuple(range(len(R[0])))
    for e in R:
        k, f = 1, e
        while f != ident:
            f, k = comp(e, f), k + 1
        if k == order:
            S, f = [ident], e
            while f != ident:
                S.append(f)
                f = comp(e, f)
            return sorted(S)
    if order == 1:
        return [ident]
    raise SystemExit(f"R has no element of order {order}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--g", type=int, required=True)
    ap.add_argument("--mult", default="", help="comma-separated multipliers u (units mod g) generating M")
    ap.add_argument("--no-pi1", action="store_true")
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
    v = 4 * g + 2
    stems = (4 * g, 4 * g + 1)
    group_of = [i for i in range(4) for _ in range(g)] + [-1, -1]
    idi, idc = {i: i for i in range(4)}, list(range(g))
    tau = lift(g, idi, [(c + 1) % g for c in idc])
    gens = [tau]
    if not a.no_pi1:
        gens.append(lift(g, {0: 0, 1: 2, 2: 3, 3: 1}, idc))
    mults = [int(u) for u in a.mult.split(",") if u]
    for u in mults:
        assert u % g and __import__("math").gcd(u, g) == 1
        gens.append(lift(g, idi, [(u * c) % g for c in idc]))
    G = closure(gens, v)
    Hreg = closure([tau], v)
    nbad = lemma_i_violations(G, group_of, stems)
    r, s = gcsts_params(v - 1, g + 1)
    reps, seen = [], set()
    for p in range(4 * g):
        if p not in seen:
            reps.append(p)
            seen |= {e[p] for e in G}
    info = {"v": v, "g": g, "r": r, "s": s, "group_order": len(G), "mult": mults, "pi1": not a.no_pi1,
            "lemma_I_violating_elements": nbad, "reps": reps}
    if nbad:
        log({**info, "stop": "Lemma I excludes every CQS invariant under this group"})
        return
    Rs = [[e for e in G if e[x] == x] for x in reps]
    anchor = 4 * g
    specs = a.avoid.split("|") if a.avoid else [None] * len(reps)
    assert len(specs) == len(reps)
    stabs_all = []
    for x, R, sp in zip(reps, Rs, specs):
        if sp is None:
            f = s % len(R)
            toks = [str(len(R))] * f + ["1"] * ((s - f) // len(R))
        else:
            toks = sp.split(";")
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
        jobs = []
        rec["colourings"] = []
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
        for ri, x in enumerate(reps):  # orbits of different representatives are disjoint; G is sorted
            for e in G:
                y = e[x]
                if y not in col:
                    col[y] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in done[ri]]
        assert sorted(col) == list(range(4 * g))
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
        cert = os.path.join(a.out, f"gcdcqs{g}_4_2_s{i}.txt")
        text = certificate_text(v, g, r, s, blocks, col, frames,
                                f"gcDCQS({g}^4:2) candidate: G = <pi1> x (C{g} x| <{','.join(map(str, mults))}>) "
                                f"(order {len(G)}), reps {reps}, avoid {'|'.join(info['avoid'])}, KM sample {i} "
                                f"(seed {a.seed0 + i}), colouring seed {a.col_seed}")
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

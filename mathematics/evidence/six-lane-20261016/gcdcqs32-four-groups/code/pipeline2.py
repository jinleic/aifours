#!/usr/bin/env python3
"""Generalized pipeline (README §3 E2/E2b): CQS(g^4 : 0) invariant under a prescribed group
(Kramer–Mesner), good colourings at EVERY point-orbit representative x (anchor h, symmetry R),
transport within each point orbit, GCDCQS certificate, check by code/check_gcdcqs.py.
KM samples and colourings are interleaved (sample i is coloured before sample i+1 is drawn);
--stop-on-first stops after the first complete certificate (README stop rule).

All files are retained (exclusive create); OUT must be new.
Usage: pipeline2.py OUT --group NAME [--res NAME] [--avoid SPEC[,SPEC...]] [--samples K]
       [--seed0 S] [--km-timeout T] [--col-timeout T] [--workers W] [--stop-on-first]
SPEC: ';'-separated stabilizer tokens of the hole-avoiding class orbits: 'R' (all of R), '1'
(trivial) or a word in the R-generators a, b (e.g. 'a', 'b', 'ab', 'ab2', 'a2b') generating a
cyclic subgroup.
"""
import lane_guard  # noqa: F401

import argparse
import collections
import hashlib
import json
import os
import random
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import fresh_dir, xopen
from lanelib import closure, comp, gcsts_params, kissat, model_satisfies, parse_status
from cqs_km import CQSKM
import colour_model as cm
import groups as grp
from pipeline import certificate_text, derived


def word_perm(word, gens, v):
    e = tuple(range(v))
    out, i = e, 0
    while i < len(word):
        ch = word[i]
        i += 1
        k = 1
        if i < len(word) and word[i].isdigit():
            k = int(word[i]); i += 1
        gidx = "abc".index(ch)
        for _ in range(k):
            out = comp(out, gens[gidx])
    return out


def subgroup(token, R, Rgens, v):
    """'R', '1', or '+'-joined words in the R-generators a, b, c (e.g. 'a+b3')."""
    if token == "R":
        return R
    if token == "1":
        return [tuple(range(v))]
    return cm.subgroup_from_gens(R, [word_perm(w, Rgens, v) for w in token.split("+")])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--group", required=True)
    ap.add_argument("--g", type=int, default=20)
    ap.add_argument("--res", required=True)
    ap.add_argument("--avoid", required=True)
    ap.add_argument("--samples", type=int, default=1)
    ap.add_argument("--seed0", type=int, default=0)
    ap.add_argument("--km-timeout", type=int, default=300)
    ap.add_argument("--col-timeout", type=int, default=300)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--stop-on-first", action="store_true")
    ap.add_argument("--rows-from", default=None, help="SUMMARY.json:SAMPLE of a run of the same group")
    ap.add_argument("--hybrid", action="store_true", help="hole-avoiding classes without symmetry (README E5)")
    ap.add_argument("--strengthen", action="store_true", help="redundant S1/S2 coverage constraints (README E7)")
    ap.add_argument("--profile", default=None, help="optional class-size ansatz, e.g. P10 (README E8)")
    ap.add_argument("--col-seed", type=int, default=1, help="kissat seed for the colouring runs")
    ap.add_argument("--kissat-opts", default="", help="extra kissat options for colouring runs, e.g. --sat")
    ap.add_argument("--model-from", default=None,
                    help="decode-only replay: read the colouring model from this retained kissat log instead of "
                         "solving (one colouring job only); the model must satisfy the rebuilt CNF")
    ap.add_argument("--no-solve", action="store_true",
                    help="README E2: build and log the colouring CNFs (sizes, sha256) without running kissat")
    ap.add_argument("--km-forbid1111", type=float, default=0.0,
                    help="README E2b steering: forbid 1+1+1+1 rows on this random fraction of the 1+1+1 columns")
    ap.add_argument("--km-steer-seed", type=int, default=0)
    ap.add_argument("--skip-lemma-p", action="store_true",
                    help="README E2b: do not colour designs satisfying the Lemma P hypotheses at x (whole design, "
                         "or the A-fixed sub-design when the group has A)")
    ap.add_argument("--km-exclude-lemma-s", action="store_true",
                    help="README E3d (Lemma S): forbid KM rows of type 2+2 with a pair difference (XOR) in {1,2,3}")
    ap.add_argument("--symbreak", action="store_true",
                    help="README E5: break the symmetry of the full hole-avoiding orbits (needs a P-profile)")
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
    reps = spec.get("reps", [(0, 1)])
    G = closure(gens, v)
    Rgens = spec["res"][a.res]
    R = closure(Rgens, v) if Rgens else [tuple(range(v))]
    orbit_of = {}
    for ri, (x, h) in enumerate(reps):
        assert all(e[x] == x and e[h] == h for e in R), "R must fix every representative and anchor"
        assert group_of[h] == group_of[x] and h != x
        for e in G:
            orbit_of.setdefault(e[x], ri)
    assert sorted(orbit_of) == list(range(v)), "representatives do not cover all point orbits"
    avoid_specs = [sp.split(";") for sp in a.avoid.split(",")]
    for sp in (avoid_specs if not a.hybrid else []):
        tot = sum(len(R) // len(subgroup(t, R, Rgens, v)) for t in sp)
        assert tot == s, f"avoid spec {sp} gives {tot} classes, not {s}"
    t0 = time.time()
    km = CQSKM(v, group_of, gens)
    summ = {"v": v, "g": g, "r": r, "s": s, "group": a.group, "group_order": len(G), "reps": reps,
            "res": a.res, "R_order": len(R), "avoid_specs": avoid_specs, "km": km.summary(),
            "args": vars(a), "samples": [], "certificates": []}
    log({"km": summ["km"], "group_order": len(G), "R_order": len(R), "reps": reps, "r": r, "s": s})
    cnf, rv = km.cnf()

    def ptype(pts_):
        return "+".join(str(c) for c in sorted(collections.Counter(group_of[int(p)] for p in pts_).values(),
                                               reverse=True))

    if a.km_forbid1111 > 0:
        cols1111 = [ci for ci, lab in enumerate(km.tcols) if ptype(km.T[lab]) == "1+1+1"]
        rng = random.Random(a.km_steer_seed)
        chosen = set(rng.sample(cols1111, int(round(a.km_forbid1111 * len(cols1111)))))
        nforb = 0
        for j, (lab, cols) in enumerate(km.rows):
            if ptype(km.Q[lab]) == "1+1+1+1" and chosen & set(cols):
                cnf.add([-rv[j]])
                nforb += 1
        summ["km_steering"] = {"fraction": a.km_forbid1111, "seed": a.km_steer_seed, "columns_1+1+1": len(cols1111),
                               "chosen": len(chosen), "rows_forbidden": nforb}
        log({"km_steering": summ["km_steering"]})
    if a.km_exclude_lemma_s:
        nex = 0
        for j, (lab, cols) in enumerate(km.rows):
            b = [int(p) for p in km.Q[lab]]
            if ptype(b) != "2+2":
                continue
            by = collections.defaultdict(list)
            for p in b:
                by[group_of[p]].append(p % g)
            if any((c[0] ^ c[1]) in (1, 2, 3) for c in by.values()):
                cnf.add([-rv[j]])
                nex += 1
        summ["km_lemma_s_excluded_rows"] = nex
        log({"km_lemma_s_excluded_rows": nex})

    def lemma_p(der, hole_, sub=None):
        pts_ok = (lambda t: True) if sub is None else (lambda t: set(t) <= sub)
        for t in der:
            if not pts_ok(t):
                continue
            hs = [p for p in t if p in hole_]
            rest = [group_of[p] for p in t if p not in hole_]
            if hs and rest[0] != rest[1]:
                return False
            if not hs and len(set(rest)) != 3:
                return False
        return True
    ex = ThreadPoolExecutor(max_workers=a.workers)
    given = None
    if a.rows_from:  # reuse a KM solution recorded in another run's summary.json (no KM solving)
        path, idx = a.rows_from.rsplit(":", 1)
        src = json.load(open(path))
        assert src["group"] == a.group and src["g"] == g, "rows-from must come from the same group"
        given = src["samples"][int(idx)]["rows"]
        summ["rows_from"] = a.rows_from
    for i in range(a.samples if given is None else 1):
        if given is None:
            p = os.path.join(a.out, f"km_{i}.cnf")
            sha = cnf.write(p)
            st, model, dt = kissat(p, a.km_timeout, seed=a.seed0 + i, log=p + ".log")
            rec = {"sample": i, "km_seed": a.seed0 + i, "km_cnf_sha256": sha, "km_status": st, "km_seconds": round(dt, 3)}
        else:
            st, model = "SAT", {rv[j] for j in given}
            rec = {"sample": i, "km_status": "GIVEN", "rows_from": a.rows_from}
        summ["samples"].append(rec)
        if st != "SAT":
            log(rec)
            break
        sel = [j for j, xx in enumerate(rv) if xx in model]
        rec["rows"] = sel
        cnf.add([-rv[j] for j in sel])
        blocks = km.blocks_of(sel)
        rec["blocks"] = len(blocks)
        rec["block_types"] = dict(collections.Counter(ptype(b) for b in blocks))
        if a.skip_lemma_p:
            x0 = reps[0][0]
            der0 = derived(blocks, x0)
            hole0 = {q for q in range(v) if group_of[q] == group_of[x0] and q != x0}
            fixA = None
            if "C3A" in spec["res"]:
                A_ = spec["res"]["C3A"][0]
                fixA = {q for q in range(v) if A_[q] == q}
            lp_full = lemma_p(der0, hole0)
            lp_sub = lemma_p(der0, hole0, fixA) if fixA is not None else False
            rec["lemma_p"] = {"full": lp_full, "A_fixed_sub": lp_sub}
            if lp_full or lp_sub:
                rec["colourings"] = []
                rec["skipped"] = "Lemma P hypotheses hold (sources/symmetry-notes.md): no good colouring" + \
                    ("" if lp_full else " of the A-fixed sub-design, hence none invariant under A")
                log({kk: rec[kk] for kk in rec if kk != "rows"})
                continue
        jobs, rec["colourings"] = [], []
        for ri, (x, h) in enumerate(reps):
            der = derived(blocks, x)
            hole = [q for q in range(v) if group_of[q] == group_of[x] and q != x]
            pts = [q for q in range(v) if q != x]
            for k, sp in enumerate(avoid_specs):
                if a.hybrid:  # hole-avoiding classes without symmetry (spec only labels the run)
                    rc, dec, sizes = cm.hybrid(der, pts, hole, R, h, s, strengthen=a.strengthen)
                    norb = len(dec[0])
                    dec = ("hybrid", dec)
                else:
                    stabs = [subgroup(t, R, Rgens, v) for t in sp]
                    rc, orbits, choice, cosets, stb, sizes = cm.anchored(der, pts, hole, R, h, stabs, strengthen=a.strengthen,
                                                                         profile=a.profile, symbreak=a.symbreak)
                    norb = len(orbits)
                    dec = ("anchored", (orbits, choice, cosets, stb))
                cp = os.path.join(a.out, f"col_{i}_r{ri}_a{k}.cnf")
                csha = rc.write(cp)
                rec["colourings"].append({"rep": ri, "x": x, "h": h, "avoid": sp if not a.hybrid else ["hybrid"],
                                          "class_orbit_sizes": sizes, "triple_orbits": norb, "col_cnf_sha256": csha,
                                          "col_vars": rc.nv, "col_clauses": len(rc.clauses)})
                jobs.append((len(rec["colourings"]) - 1, cp, der, pts, hole, dec))
                if a.hybrid:
                    break
        log({kk: rec[kk] for kk in rec if kk != "rows"})
        done = {}

        def run(job):
            if a.no_solve:
                return job, "NOT_SOLVED", set(), 0.0
            if a.model_from:
                assert len(jobs) == 1, "--model-from needs exactly one colouring job"
                stt, mdl = parse_status(open(a.model_from).read())
                assert stt == "SAT" and model_satisfies(job[1], mdl), "retained model does not satisfy the rebuilt CNF"
                return job, stt, mdl, 0.0
            stt, mdl, dtt = kissat(job[1], a.col_timeout, seed=a.col_seed, log=job[1] + ".log",
                                   extra=a.kissat_opts.split())
            return job, stt, mdl, dtt

        for job, stt, mdl, dtt in ex.map(run, jobs):
            ci, cp, der, pts, hole, dec = job
            crec = rec["colourings"][ci]
            crec["col_status"], crec["col_seconds"] = stt, round(dtt, 3)
            if stt == "SAT":
                classes = cm.decode_hybrid(mdl, dec[1], R) if dec[0] == "hybrid" else cm.decode(mdl, *dec[1], R)
                cm.verify_good_colouring(der, pts, hole, classes, r, s)
                crec["class_sizes_at_x"] = [len(C) for C in classes]
                done.setdefault(crec["rep"], (ci, classes))
            log({"sample": i, "colouring": ci, **{kk: crec[kk] for kk in crec if kk != "avoid"}, "avoid": crec["avoid"]})
        if len(done) == len(reps):
            col = {}
            for e in G:
                for ri, (x, h) in enumerate(reps):
                    y = e[x]
                    if orbit_of[y] == ri and y not in col:
                        col[y] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in done[ri][1]]
            assert sorted(col) == list(range(v))
            used = ";".join(f"rep{ri}:avoid{done[ri][0]}" for ri in sorted(done))
            cert = os.path.join(a.out, f"gcdcqs{g}_s{i}.txt")
            text = certificate_text(v, n, g, r, s, groups_, blocks, col,
                                    f"gcDCQS({g}^4:0) candidate: group {a.group} (order {len(G)}), R={a.res}, "
                                    f"reps={reps}, colourings {used}, KM sample {i}")
            with xopen(cert) as fh:
                fh.write(text)
            chk = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs.py"), cert],
                                 capture_output=True, text=True)
            crt = {"sample": i, "certificate": cert, "sha256": hashlib.sha256(text.encode()).hexdigest(),
                   "checker": json.loads(chk.stdout)["result"], "colourings_used": used}
            summ["certificates"].append(crt)
            log(crt)
            if a.stop_on_first and crt["checker"] == "PASS":
                break
    ex.shutdown()
    summ["total_seconds"] = round(time.time() - t0, 2)
    with xopen(os.path.join(a.out, "summary.json")) as fh:
        json.dump(summ, fh, indent=1)
    print("CERTIFICATES", [c["certificate"] for c in summ["certificates"]], "total_seconds", summ["total_seconds"], flush=True)


if __name__ == "__main__":
    main()

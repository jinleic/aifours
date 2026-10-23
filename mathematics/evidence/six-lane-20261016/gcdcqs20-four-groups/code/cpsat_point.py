#!/usr/bin/env python3
"""README E8: per-point good colouring of one derived design by CP-SAT (lane-local OR-Tools 9.15,
run with the uv-managed CPython 3.12 and PYTHONPATH=<lane>/pydeps312; see README §5).

Model: one integer colour per triple of D_x (hole triples: colours S..R-1; others 0..R-1);
AllDifferent over the triples through every point (partial parallel classes); the triples through
the anchor h (a hole point) get colours S, S+1, ..., R-1 in sorted order (lossless: they lie in
the R-S non-avoiding classes, one each).  Colours 0..S-1 are then exactly the hole-avoiding
classes.  Optional --c3: the colouring is invariant under pi1 (fixes G0 pointwise): colour(pi1 t)
= sigma(colour t) with sigma induced by the anchor on S..R-1 and the declared structure on 0..S-1.
On FEASIBLE: verified, transported by the design group (transitive), written as a GCDCQS
certificate (exclusive create) and checked by code/check_gcdcqs.py.
Usage: cpsat_point.py OUTDIR --group G --rows-from SUMMARY:IDX [--x 0] [--anchor 1] [--c3 R;1;1;1]
       [--seconds T] [--workers W] [--seed S]
"""
import lane_guard  # noqa: F401

import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from lane_guard import fresh_dir, xopen
from ortools.sat.python import cp_model
from lanelib import closure, gcsts_params
import colour_model as cm
from derived_io import load_design
from pipeline import certificate_text, derived


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--group", required=True)
    ap.add_argument("--rows-from", required=True)
    ap.add_argument("--x", type=int, default=0)
    ap.add_argument("--anchor", type=int, default=1)
    ap.add_argument("--c3", default=None, help="structure of the hole-avoiding colours under pi1, e.g. R;1;1;1")
    ap.add_argument("--seconds", type=float, default=600)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    fresh_dir(a.out)
    spec, v, g, blocks = load_design(a.group, a.rows_from)
    r, s = gcsts_params(v - 1, g - 1)
    x, h = a.x, a.anchor
    group_of = spec["group_of"]
    hole = {q for q in range(v) if group_of[q] == group_of[x] and q != x}
    assert h in hole
    der = derived(blocks, x)
    idx = {t: i for i, t in enumerate(der)}
    md = cp_model.CpModel()
    col = []
    for i, t in enumerate(der):
        lo = s if set(t) & hole else 0
        col.append(md.NewIntVar(lo, r - 1, f"c{i}"))
    inc = {}
    for i, t in enumerate(der):
        for p in t:
            inc.setdefault(p, []).append(i)
    for p, ts in inc.items():
        md.AddAllDifferent([col[i] for i in ts])
    anc = sorted(i for i, t in enumerate(der) if h in t)
    assert len(anc) == r - s
    for c, i in enumerate(anc):
        md.Add(col[i] == s + c)
    rec = {"group": a.group, "rows_from": a.rows_from, "x": x, "anchor": h, "triples": len(der), "r": r, "s": s,
           "c3": a.c3, "seconds_cap": a.seconds, "workers": a.workers, "seed": a.seed,
           "solver": "OR-Tools CP-SAT 9.15.6755 (lane-local copy)"}
    if a.c3:
        pi1 = spec["res"]["C3"][0]
        assert pi1[x] == x and pi1[h] == h
        im = lambda t: tuple(sorted(pi1[p] for p in t))
        sigma = list(range(r))
        for c, i in enumerate(anc):  # anchored colours follow the anchored triples
            sigma[s + c] = s + anc.index(idx[im(der[i])])
        toks, nxt = a.c3.split(";"), 0
        for tok in toks:
            if tok == "R":
                sigma[nxt] = nxt
                nxt += 1
            else:
                sigma[nxt], sigma[nxt + 1], sigma[nxt + 2] = nxt + 1, nxt + 2, nxt
                nxt += 3
        assert nxt == s and sorted(sigma) == list(range(r))
        rec["sigma"] = sigma
        for i, t in enumerate(der):
            md.AddElement(col[i], sigma, col[idx[im(t)]])
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = a.seconds
    solver.parameters.num_workers = a.workers
    solver.parameters.random_seed = a.seed
    t0 = time.time()
    st = solver.Solve(md)
    rec["status"] = solver.StatusName(st)
    rec["wall_seconds"] = round(time.time() - t0, 2)
    rec["conflicts"] = solver.NumConflicts()
    rec["branches"] = solver.NumBranches()
    if rec["status"] in ("FEASIBLE", "OPTIMAL"):
        classes = [[] for _ in range(r)]
        for i, t in enumerate(der):
            classes[solver.Value(col[i])].append(t)
        classes = [sorted(C) for C in classes]
        pts = [q for q in range(v) if q != x]
        cm.verify_good_colouring(der, pts, sorted(hole), classes, r, s)
        rec["class_sizes_at_x"] = [len(C) for C in classes]
        with xopen(os.path.join(a.out, "colouring_at_x.json")) as fh:
            json.dump(classes, fh)
        G = closure(spec["gens"], v)
        colo = {}
        for e in G:
            y = e[x]
            if y not in colo:
                colo[y] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in classes]
        assert sorted(colo) == list(range(v)), "group not transitive"
        text = certificate_text(v, 4, g, r, s, spec["groups"], blocks, colo,
                                f"gcDCQS({g}^4:0) candidate: group {a.group} (order {len(G)}), design {a.rows_from}, "
                                f"CP-SAT colouring at {x} (anchor {h}, c3={a.c3}, seed {a.seed})")
        cert = os.path.join(a.out, f"gcdcqs{g}_cpsat.txt")
        with xopen(cert) as fh:
            fh.write(text)
        rec["certificate"] = cert
        rec["certificate_sha256"] = hashlib.sha256(text.encode()).hexdigest()
        chk = subprocess.run(["/usr/bin/python3", os.path.join(HERE, "check_gcdcqs.py"), cert], capture_output=True, text=True)
        rec["checker"] = json.loads(chk.stdout)["result"]
    with xopen(os.path.join(a.out, "result.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({k: rec[k] for k in rec if k != "sigma"}))


if __name__ == "__main__":
    main()

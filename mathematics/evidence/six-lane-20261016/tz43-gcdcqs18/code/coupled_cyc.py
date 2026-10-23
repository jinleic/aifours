#!/usr/bin/env python3
"""README A2 step 1: coupled Kramer–Mesner + good colouring at 0 for a CQS(g^4 : 2) in the cyclic model
(group points Z_{4g}, group i = residues ≡ i mod 4, rho: a -> a + 1 swapping the stems; no multipliers, so
Stab(0) is trivial) — one CNF (numpy + kissat).

Variables: y_r (KM rows, every column exactly once); for every potential derived triple t at 0 (t ∪ {0} a block
of a valid row) and class c: z(t, c), classes 0..s-1 hole-avoiding (no hole point allowed), s..r-1 the others.
t present <=> its row chosen <=> t in exactly one class; at most one triple per (class, point); every
non-avoiding class contains every hole point (implied, added).  Symmetry breaking (sound): the triples through
the anchor (stem 4g) fill the non-avoiding classes in increasing triple order.  The colouring at y = rho^y(0)
is rho^y(colouring at 0); stem frames = <rho^4>-orbits.  Format S certificate checked by both routes.
Usage: coupled_cyc.py OUT --g G [--timeout T] [--seed S] [--exclude-from CERT ...]"""
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
from lanelib import CNF, closure, gcsts_params, kissat  # noqa: E402
from cqs_km_s import CQSKMS  # noqa: E402
from pipeline_s import derived  # noqa: E402
from pipeline_s3 import cert_text  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--g", type=int, required=True)
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    fresh_dir(a.out)
    g = a.g
    N, v = 4 * g, 4 * g + 2
    group_of = [p % 4 for p in range(N)] + [-1, -1]
    rho = tuple([(p + 1) % N for p in range(N)] + [N + 1, N])
    G = closure([rho], v)
    rho4 = tuple([(p + 4) % N for p in range(N)] + [N, N + 1])
    H4 = closure([rho4], v)
    r, s = gcsts_params(v - 1, g + 1)
    t0 = time.time()
    km = CQSKMS(v, group_of, [rho])
    cnf, rv = km.cnf()
    x, anchor = 0, N
    hole = {q for q in range(v) if (group_of[q] == 0 or group_of[q] == -1) and q != x}
    pot = {}
    for ri in range(len(km.rows)):
        for b in km.blocks_of([ri]):
            if x in b:
                t = tuple(q for q in b if q != x)
                assert t not in pot
                pot[t] = ri
    z = {}
    for t, ri in pot.items():
        opts = [c for c in range(r) if c >= s or not (set(t) & hole)]
        lits = []
        for c in opts:
            z[(t, c)] = cnf.var()
            lits.append(z[(t, c)])
            cnf.add([-z[(t, c)], rv[ri]])
        cnf.add([-rv[ri]] + lits)
        cnf.amo(lits)
    bycp = collections.defaultdict(list)
    for (t, c), var in z.items():
        for q in t:
            bycp[(c, q)].append(var)
    for key, lits in bycp.items():
        cnf.amo(lits)
    for c in range(s, r):
        for h in hole:
            cnf.add(bycp.get((c, h), []))
    A = sorted(t for t in pot if anchor in t)
    nsb = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            for ci in range(s, r):
                for cj in range(s, ci + 1):
                    if (A[i], ci) in z and (A[j], cj) in z:
                        cnf.add([-z[(A[i], ci)], -z[(A[j], cj)]])
                        nsb += 1
    path = os.path.join(a.out, "coupled.cnf")
    sha = cnf.write(path)
    st, model, dt = kissat(path, a.timeout, seed=a.seed, log=path + ".log")
    rec = {"g": g, "v": v, "r": r, "s": s, "group_order": len(G), "km": km.summary(), "potential_derived_triples": len(pot),
           "anchor_triples": len(A), "vars": cnf.nv, "clauses": len(cnf.clauses), "symbreak_clauses": nsb,
           "cnf_sha256": sha, "kissat_seed": a.seed, "status": st, "solve_seconds": round(dt, 2)}
    if st == "SAT":
        sel = [j for j, xx in enumerate(rv) if xx in model]
        blocks = km.blocks_of(sel)
        der = derived(blocks, x)
        classes = [sorted(t for t in pot if (t, c) in z and z[(t, c)] in model) for c in range(r)]
        assert sorted(t for C in classes for t in C) == sorted(der)
        col = {}
        for e in G:
            y = e[x]
            if y not in col:
                col[y] = [sorted(tuple(sorted(e[q] for q in t)) for t in C) for C in classes]
        frames = {}
        for al in (N, N + 1):
            dset = set(derived(blocks, al))
            fr = []
            while dset:
                t = min(dset)
                orb = {tuple(sorted(e[q] for q in t)) for e in H4}
                assert orb <= dset
                dset -= orb
                fr.append((({0, 1, 2, 3} - {group_of[q] for q in t}).pop(), sorted(orb)))
            frames[al] = sorted(fr)
        cert = os.path.join(a.out, f"gcdcqs{g}_4_2_cyc_coupled_s{a.seed}.txt")
        text = cert_text(v, g, r, s, blocks, col, frames,
                         f"gcDCQS({g}^4:2) candidate, cyclic model (rho swaps the stems), coupled KM+colouring, kissat seed {a.seed}")
        with xopen(cert) as fh:
            fh.write(text)
        rec["certificate"] = cert
        rec["sha256"] = hashlib.sha256(text.encode()).hexdigest()
        rec["blocks"] = len(blocks)
        rec["class_sizes_at_0"] = [len(C) for C in classes]
        chk = subprocess.run([sys.executable, os.path.join(HERE, "check_gcdcqs_s.py"), cert], capture_output=True, text=True)
        rec["route1"] = json.loads(chk.stdout)["result"]
        rec["route2"] = subprocess.run([os.path.join(HERE, "bin", "check_gcdcqs_s_c"), cert], capture_output=True,
                                       text=True).stdout.strip()
    rec["total_seconds"] = round(time.time() - t0, 2)
    with xopen(os.path.join(a.out, "summary.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


if __name__ == "__main__":
    main()

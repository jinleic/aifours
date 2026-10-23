#!/usr/bin/env python3
"""README B1g: no-global-symmetry coupled FD m=6 model, with a supplied one-point KF(6^4) restriction.
Copied from gdd_seed_search5.py; instead of forcing the inflated KF(2^4), the final argument may supply a
separately constructed frame JSON from kf6_seed.py (points0..23, frame keys0..3). It is relabelled to6..29
and checked directly before use. All29 other point frames are independent. Restricted UNSAT is not a
nonexistence result for the target.
Class ordering uses the same sound prefix-OR encoding calibrated in gdd_regular_fast.py, not the earlier
quadratic pairwise clauses.
Usage: gdd_seed_search7.py FD 6 0 0 0 OUTDIR TIMEOUT SEED KF6.json"""
import itertools
import json
import math
import os
import subprocess
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import CNF  # noqa: E402


def main():
    kind, m, d, rot, kmonly = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    out, tl, seed = sys.argv[6], int(sys.argv[7]), int(sys.argv[8])
    assert kind in ("FD", "RD") and m % 2 == 0
    fresh_dir(out)
    sub = sorted({(d * i) % m for i in range(m)})
    N = 5 * m
    G = [(k, h) for k in (range(5) if rot else [0]) for h in sub]
    act = lambda g, p: m * ((p // m + g[0]) % 5) + (p % m + g[1]) % m  # noqa: E731
    gof = lambda p: p // m  # noqa: E731
    trans = lambda S: len({gof(p) for p in S}) == len(S)  # noqa: E731
    canon = lambda S: min(tuple(sorted(act(g, p) for p in S)) for g in G)  # noqa: E731
    cols = sorted({canon(t) for t in itertools.combinations(range(N), 3) if trans(t)})
    cidx = {c: i for i, c in enumerate(cols)}
    quads = sorted({canon(q) for q in itertools.combinations(range(N), 4) if trans(q)})
    rows = []
    for q in quads:
        sub_ = [cidx[canon(t)] for t in itertools.combinations(q, 3)]
        if len(set(sub_)) == 4:
            rows.append((q, sub_))
    cnf = CNF()
    yv = [cnf.var() for _ in rows]
    bycol = defaultdict(list)
    for ri, (q, s_) in enumerate(rows):
        for c in s_:
            bycol[c].append(yv[ri])
    assert len(bycol) == len(cols)
    for c in range(len(cols)):
        cnf.exactly_one(bycol[c])
    reps, seenp = [], set()
    for p in range(N):
        if p not in seenp:
            reps.append(p)
            seenp |= {act(g, p) for g in G}
    if kmonly:
        reps = []
    ncl = m // 2 if kind == "FD" else 3 * m // 2
    zall, potall, missall, nsb = {}, {}, {}, 0
    for x in reps:
        pot = {}
        for ri, (q, _) in enumerate(rows):
            for g in G:
                img = tuple(sorted(act(g, p) for p in q))
                if x in img:
                    t = tuple(p for p in img if p != x)
                    assert t not in pot or pot[t] == ri
                    pot[t] = ri
        gx = gof(x)
        missing = {t: (set(range(5)) - {gx} - {gof(p) for p in t}).pop() for t in pot}
        if kind == "FD":
            fams = [(y, [p for p in range(N) if gof(p) not in (gx, y)]) for y in range(5) if y != gx]
            member = lambda t, y, missing=missing: missing[t] == y  # noqa: E731
        else:
            fams = [(0, [p for p in range(N) if gof(p) != gx])]
            member = lambda t, y: True  # noqa: E731
        z = {}
        for t, ri in pot.items():
            lits = []
            for j in range(ncl):
                z[(t, j)] = cnf.var()
                lits.append(z[(t, j)])
                cnf.add([-z[(t, j)], yv[ri]])
            cnf.add([-yv[ri]] + lits)
            cnf.amo(lits)
        for y, pts in fams:
            for j in range(ncl):
                for p in pts:
                    cnf.exactly_one([z[(t, j)] for t in pot if member(t, y) and p in t])
        for y, pts in fams:
            py = min(pts)
            Ts = sorted(t for t in pot if member(t, y) and py in t)
            before = [None] * ncl
            for T in Ts:
                for j in range(1,ncl):
                    cnf.add([-z[(T,j)],before[j-1]] if before[j-1] is not None else [-z[(T,j)]])
                    nsb += 1
                after = []
                for j in range(ncl):
                    v = cnf.var()
                    if before[j] is None:
                        cnf.add([-v,z[(T,j)]]); cnf.add([v,-z[(T,j)]]); nsb += 2
                    else:
                        cnf.add([-before[j],v]); cnf.add([-z[(T,j)],v])
                        cnf.add([-v,before[j],z[(T,j)]]); nsb += 3
                    after.append(v)
                before = after
        zall[x], potall[x], missall[x] = z, pot, missing
    assert (kind, m, d, rot, kmonly) == ("FD", 6, 0, 0, 0), "B1g uses no global action at m=6"
    external = sys.argv[9]
    frame_doc = json.load(open(external))
    assert frame_doc["points"] == 24 and frame_doc["group_size"] == 6
    fixed = {int(y)+1: [[tuple(sorted(6+p for p in T)) for T in C] for C in Cs]
             for y, Cs in frame_doc["frames"].items()}
    assert set(fixed) == set(range(1,5))
    for y, Cs in fixed.items():
        assert len(Cs) == 3
        target = {p for p in range(6,30) if p // 6 != y}
        for C in Cs:
            flat = [p for T in C for p in T]
            assert len(C) == 6 and len(flat) == len(set(flat)) == 18 and set(flat) == target
        py = min(target)
        Cs.sort(key=lambda C: next(T for T in C if py in T))
    seed_tri = {T for Cs in fixed.values() for C in Cs for T in C}
    expected_pairs = [pr for pr in itertools.combinations(range(6, 30), 2) if pr[0] // 6 != pr[1] // 6]
    seed_pairs = [pr for T in seed_tri for pr in itertools.combinations(T, 2)]
    assert len(seed_tri) == 72 and sorted(seed_pairs) == expected_pairs, "seed is not a KF(6^4)"
    fixed_assignment = {T: j for Cs in fixed.values() for j, C in enumerate(Cs) for T in C}
    for T, ri in potall[0].items():
        cnf.add([yv[ri] if T in seed_tri else -yv[ri]])
        for j in range(ncl):
            cnf.add([zall[0][(T, j)] if fixed_assignment.get(T) == j else -zall[0][(T, j)]])
    with xopen(os.path.join(out, "fixed-kf6.json")) as fh:
        json.dump(fixed, fh, indent=1)
    path = os.path.join(out, "model.cnf")
    sha = cnf.write(path)
    print(json.dumps({"stage": "model_built", "columns": len(cols), "rows": len(rows),
                      "points_with_frame_variables": len(reps), "vars": cnf.nv, "clauses": len(cnf.clauses),
                      "cnf_sha256": sha}), flush=True)
    r = subprocess.run(["kissat", "-q", f"--time={tl}", f"--seed={seed}", path], capture_output=True, text=True)
    with xopen(path + ".log") as fh:
        fh.write(r.stdout)
    status = "SAT" if "s SATISFIABLE" in r.stdout else ("UNSAT" if "s UNSATISFIABLE" in r.stdout else "UNKNOWN")
    rec = {"kind": kind, "m": m, "d": d, "rot": rot, "km_only": kmonly, "group_order": len(G), "reps": reps,
           "columns": len(cols), "quad_orbits": len(quads), "rows": len(rows),
           "potential_derived_triples": {x: len(potall[x]) for x in reps},
           "vars": cnf.nv, "clauses": len(cnf.clauses), "symbreak_clauses": nsb, "cnf_sha256": sha,
           "fixed_KF_at_point0": {"path": external, "sha256": __import__("hashlib").sha256(open(external,"rb").read()).hexdigest()},
           "kissat_seed": seed, "status": status}
    if status == "SAT" and not kmonly:
        model = {int(v) for line in r.stdout.splitlines() if line.startswith("v ") for v in line[2:].split() if int(v) > 0}
        chosen = [rows[ri][0] for ri in range(len(rows)) if yv[ri] in model]
        blocks = sorted({tuple(sorted(act(g, p) for p in q)) for q in chosen for g in G})
        sec = {}
        for x in reps:
            z, pot, missing = zall[x], potall[x], missall[x]
            if kind == "FD":
                classes = [(y, [t for t in pot if missing[t] == y and z[(t, j)] in model])
                           for y in range(5) if y != gof(x) for j in range(ncl)]
            else:
                classes = [(j, [t for t in pot if z[(t, j)] in model]) for j in range(ncl)]
            for g in G:
                xp = act(g, x)
                assert xp not in sec
                sec[xp] = [((lab + g[0]) % 5 if kind == "FD" else lab,
                            sorted(tuple(sorted(act(g, p) for p in t)) for t in C)) for lab, C in classes]
        lines = [f"GDD34 {kind}GDD 5 {m}", "GROUPS"] + [" ".join(str(m * i + a) for a in range(m)) for i in range(5)]
        lines += ["BLOCKS"] + [" ".join(map(str, b)) for b in blocks]
        for xp in sorted(sec):
            lines.append(f"POINT {xp}")
            for lab, C in sec[xp]:
                lines.append(f"{'FRAME' if kind == 'FD' else 'PC'} {lab}")
                lines += [" ".join(map(str, tr)) for tr in C]
        cert = os.path.join(out, f"{kind.lower()}gdd_5_{m}_d{d}_rot{rot}_s{seed}.txt")
        with xopen(cert) as fh:
            fh.write("\n".join(lines) + "\n")
        rec["certificate"] = cert
        rec["blocks"] = len(blocks)
    with xopen(os.path.join(out, "summary.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


if __name__ == "__main__":
    main()

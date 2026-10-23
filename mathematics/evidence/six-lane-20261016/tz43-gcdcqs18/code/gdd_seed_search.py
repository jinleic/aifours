#!/usr/bin/env python3
"""README B1: seed FDGDD(3,4,5{m}) or RDGDD(3,4,5{m}) by the E10 coupled model generalized (stdlib + kissat).
Adapted from ../code/fdh_search.py (copied from the gcdcqs32 lane, sha256 57d39a13…4842): group size m and a
regular coordinate group H, and a resolution (RD) variant.

Points (i, a) -> m*i + a, i in Z5 (groups), a in H (m elements, H given by its multiplication table).
Gamma = Z5 x H acting regularly: (k, h).(i, a) = (i + k, h*a).  Every transverse triple/4-set orbit is free.
Coupled model: y_r for every Gamma-orbit of transverse 4-sets whose 4 sub-triples lie in 4 distinct column
orbits (KM rows); every column (orbit of transverse triples) covered exactly once.  At x = 0 the potential
derived triples are the 4-sets through x of valid rows (present iff the row is chosen):
  FD: class (y, j), y in {1,2,3,4} the missed group, j < m/2; every class contains every point of the three
      groups other than 0 and y exactly once (Kirkman frame KF(m^4));
  RD: class j < 3m/2; every class contains every point outside group 0 exactly once (resolution).
Symmetry breaking (sound): the triples through the least admissible point of each class family fill the
classes in increasing triple order.  Transport: the classes at g(x) are g(classes at x).
Usage: gdd_seed_search.py KIND(FD|RD) H(Z<m>|S3) OUTDIR TIMEOUT SEED"""
import itertools
import json
import os
import subprocess
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import CNF  # noqa: E402


def coord_group(name):
    if name == "S3":
        els = sorted(itertools.permutations(range(3)))
        idx = {e: i for i, e in enumerate(els)}
        mul = [[idx[tuple(a[b[t]] for t in range(3))] for b in els] for a in els]
        return 6, mul
    if name.startswith("E"):  # elementary abelian 2-group of order 2^d, XOR (E10 used E8 = F2^3)
        m = int(name[1:])
        return m, [[a ^ b for b in range(m)] for a in range(m)]
    m = int(name[1:])
    return m, [[(a + b) % m for b in range(m)] for a in range(m)]


def main():
    kind, hname, out, tl, seed = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
    assert kind in ("FD", "RD")
    fresh_dir(out)
    m, mul = coord_group(hname)
    N = 5 * m
    G = [(k, h) for k in range(5) for h in range(m)]
    act = lambda g, p: m * ((p // m + g[0]) % 5) + mul[g[1]][p % m]  # noqa: E731
    gof = lambda p: p // m  # noqa: E731
    trans = lambda S: len({gof(p) for p in S}) == len(S)  # noqa: E731
    canon = lambda S: min(tuple(sorted(act(g, p) for p in S)) for g in G)  # noqa: E731
    cols = sorted({canon(t) for t in itertools.combinations(range(N), 3) if trans(t)})
    cidx = {c: i for i, c in enumerate(cols)}
    quads = sorted({canon(q) for q in itertools.combinations(range(N), 4) if trans(q)})
    rows = []
    for q in quads:
        sub = [cidx[canon(t)] for t in itertools.combinations(q, 3)]
        if len(set(sub)) == 4:
            rows.append((q, sub))
    cnf = CNF()
    yv = [cnf.var() for _ in rows]
    bycol = defaultdict(list)
    for ri, (q, sub) in enumerate(rows):
        for c in sub:
            bycol[c].append(yv[ri])
    assert len(bycol) == len(cols)
    for c in range(len(cols)):
        cnf.exactly_one(bycol[c])
    x = 0
    pot = {}
    for ri, (q, _) in enumerate(rows):
        for g in G:
            img = tuple(sorted(act(g, p) for p in q))
            if x in img:
                t = tuple(p for p in img if p != x)
                assert t not in pot or pot[t] == ri
                pot[t] = ri
    missing = {t: ({1, 2, 3, 4} - {gof(p) for p in t}).pop() for t in pot}
    if kind == "FD":
        fams = [(y, [p for p in range(m, N) if gof(p) != y]) for y in range(1, 5)]
        ncl = m // 2
        member = lambda t, y: missing[t] == y  # noqa: E731
    else:
        fams = [(0, list(range(m, N)))]
        ncl = 3 * m // 2
        member = lambda t, y: True  # noqa: E731
    z = {}
    for t, ri in pot.items():
        lits = []
        y = missing[t] if kind == "FD" else 0
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
    nsb = 0
    for y, pts in fams:
        py = min(pts)
        Ts = sorted(t for t in pot if member(t, y) and py in t)
        for a, b in itertools.combinations(range(len(Ts)), 2):
            for ja in range(ncl):
                for jb in range(ja + 1):
                    cnf.add([-z[(Ts[a], ja)], -z[(Ts[b], jb)]])
                    nsb += 1
    path = os.path.join(out, "model.cnf")
    sha = cnf.write(path)
    r = subprocess.run(["kissat", "-q", f"--time={tl}", f"--seed={seed}", path], capture_output=True, text=True)
    with xopen(path + ".log") as fh:
        fh.write(r.stdout)
    status = "SAT" if "s SATISFIABLE" in r.stdout else ("UNSAT" if "s UNSATISFIABLE" in r.stdout else "UNKNOWN")
    rec = {"kind": kind, "H": hname, "m": m, "columns": len(cols), "quad_orbits": len(quads), "rows": len(rows),
           "potential_derived_triples": len(pot), "vars": cnf.nv, "clauses": len(cnf.clauses),
           "symbreak_clauses": nsb, "cnf_sha256": sha, "kissat_seed": seed, "status": status}
    if status == "SAT":
        model = {int(v) for line in r.stdout.splitlines() if line.startswith("v ") for v in line[2:].split() if int(v) > 0}
        chosen = [rows[ri][0] for ri in range(len(rows)) if yv[ri] in model]
        blocks = sorted({tuple(sorted(act(g, p) for p in q)) for q in chosen for g in G})
        if kind == "FD":
            classes = [(y, [t for t in pot if missing[t] == y and z[(t, j)] in model]) for y in range(1, 5) for j in range(ncl)]
        else:
            classes = [(j, [t for t in pot if z[(t, j)] in model]) for j in range(ncl)]
        lines = [f"GDD34 {kind}GDD 5 {m}", "GROUPS"] + [" ".join(str(m * i + a) for a in range(m)) for i in range(5)]
        lines += ["BLOCKS"] + [" ".join(map(str, b)) for b in blocks]
        for g in sorted(G, key=lambda g: act(g, x)):
            xp = act(g, x)
            lines.append(f"POINT {xp}")
            for lab, C in classes:
                lab2 = (lab + g[0]) % 5 if kind == "FD" else lab
                lines.append(f"{'FRAME' if kind == 'FD' else 'PC'} {lab2}")
                lines += [" ".join(map(str, tr)) for tr in sorted(tuple(sorted(act(g, p) for p in t)) for t in C)]
        cert = os.path.join(out, f"{kind.lower()}gdd_5_{m}_{hname}_s{seed}.txt")
        with xopen(cert) as fh:
            fh.write("\n".join(lines) + "\n")
        rec["certificate"] = cert
        rec["blocks"] = len(blocks)
    with xopen(os.path.join(out, "summary.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


if __name__ == "__main__":
    main()

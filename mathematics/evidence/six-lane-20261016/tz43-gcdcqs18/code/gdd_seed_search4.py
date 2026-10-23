#!/usr/bin/env python3
"""README B1e: FDGDD(3,4,5{6}) / RDGDD(3,4,5{6}) invariant under a REGULAR non-abelian group of order 30
acting on itself by left multiplication, the 5 groups being the left cosets of a subgroup K of order 6 (stdlib +
kissat).  Groups: 'D15' (K = <r^5, s>) or 'Z3xD5' (K = Z3 x <s>).  Same coupled model as code/gdd_seed_search*.py
but with the GENERAL orbit-size condition (a quad orbit may have a stabilizer of order 2: it is a valid row iff
|orbit(Q)| * multiplicity = |orbit(T)| for every column T it meets).  Frames/resolution at x = identity are
transported by left multiplication (regular action: no invariance condition).
Usage: gdd_seed_search4.py KIND(FD|RD) GROUP KMONLY OUTDIR TIMEOUT SEED"""
import itertools
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402
from lanelib import CNF  # noqa: E402


def group_D15():
    els = [(i, e) for e in range(2) for i in range(15)]  # r^i s^e
    idx = {x: k for k, x in enumerate(els)}
    mul = lambda a, b: ((a[0] + (b[0] if a[1] == 0 else -b[0])) % 15, (a[1] + b[1]) % 2)  # noqa: E731
    K = [(5 * k, f) for k in range(3) for f in range(2)]
    return els, idx, mul, K


def group_Z3xD5():
    els = [(c, i, e) for e in range(2) for c in range(3) for i in range(5)]  # (c, r^i s^e)
    idx = {x: k for k, x in enumerate(els)}
    mul = lambda a, b: ((a[0] + b[0]) % 3, (a[1] + (b[1] if a[2] == 0 else -b[1])) % 5, (a[2] + b[2]) % 2)  # noqa: E731
    K = [(c, 0, f) for c in range(3) for f in range(2)]
    return els, idx, mul, K


def main():
    kind, gname, kmonly, out, tl, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], int(sys.argv[5]), int(sys.argv[6])
    assert kind in ("FD", "RD")
    fresh_dir(out)
    els, idx, mul, K = {"D15": group_D15, "Z3xD5": group_Z3xD5}[gname]()
    N = len(els)
    assert N == 30 and len(K) == 6
    cos, gof = [], {}
    for x in els:
        if idx[x] in gof:
            continue
        c = sorted(idx[mul(x, k)] for k in K)
        for p in c:
            gof[p] = len(cos)
        cos.append(c)
    assert len(cos) == 5
    # relabel points so that group i = {6i, ..., 6i+5}
    order = [p for c in cos for p in c]
    lab = {p: k for k, p in enumerate(order)}
    perms = []
    for gamma in els:
        perms.append(tuple(lab[idx[mul(gamma, els[order[q]])]] for q in range(N)))
    G = sorted(set(perms))
    assert len(G) == 30
    gp = lambda p: p // 6  # noqa: E731
    for g in G:  # preserves the group partition
        assert all(len({gp(g[p]) for p in range(6 * i, 6 * i + 6)}) == 1 for i in range(5))
    trans = lambda S: len({gp(p) for p in S}) == len(S)  # noqa: E731
    img = lambda g, S: tuple(sorted(g[p] for p in S))  # noqa: E731
    canon = lambda S: min(img(g, S) for g in G)  # noqa: E731
    tri = [t for t in itertools.combinations(range(N), 3) if trans(t)]
    tcan = {t: canon(t) for t in tri}
    tsize = Counter(tcan.values())
    cols = sorted(tsize)
    cidx = {c: i for i, c in enumerate(cols)}
    qcan = {}
    for q in itertools.combinations(range(N), 4):
        if trans(q):
            qcan[q] = canon(q)
    qsize = Counter(qcan.values())
    rows = []
    for q in sorted(qsize):
        mult = Counter(cidx[tcan[t]] for t in itertools.combinations(q, 3))
        if all(qsize[q] * m == tsize[cols[c]] for c, m in mult.items()):
            rows.append((q, sorted(mult)))
    cnf = CNF()
    yv = [cnf.var() for _ in rows]
    bycol = defaultdict(list)
    for ri, (q, cs) in enumerate(rows):
        for c in cs:
            bycol[c].append(yv[ri])
    for c in range(len(cols)):
        cnf.exactly_one(bycol.get(c, []))
    x = 0
    ncl = 3 if kind == "FD" else 9
    pot, z, nsb = {}, {}, 0
    if not kmonly:
        for ri, (q, _) in enumerate(rows):
            for g in G:
                b = img(g, q)
                if x in b:
                    t = tuple(p for p in b if p != x)
                    assert t not in pot or pot[t] == ri
                    pot[t] = ri
        missing = {t: (set(range(5)) - {gp(x)} - {gp(p) for p in t}).pop() for t in pot}
        if kind == "FD":
            fams = [(y, [p for p in range(N) if gp(p) not in (gp(x), y)]) for y in range(5) if y != gp(x)]
            member = lambda t, y: missing[t] == y  # noqa: E731
        else:
            fams = [(0, [p for p in range(N) if gp(p) != gp(x)])]
            member = lambda t, y: True  # noqa: E731
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
    rec = {"kind": kind, "group": gname, "km_only": kmonly, "columns": len(cols), "column_sizes": dict(Counter(tsize.values())),
           "quad_orbits": len(qsize), "rows": len(rows), "row_sizes": dict(Counter(qsize[q] for q, _ in rows)),
           "potential_derived_triples": len(pot), "vars": cnf.nv, "clauses": len(cnf.clauses), "symbreak_clauses": nsb,
           "cnf_sha256": sha, "kissat_seed": seed, "status": status}
    if status == "SAT" and not kmonly:
        model = {int(v) for line in r.stdout.splitlines() if line.startswith("v ") for v in line[2:].split() if int(v) > 0}
        chosen = [rows[ri][0] for ri in range(len(rows)) if yv[ri] in model]
        blocks = sorted({img(g, q) for q in chosen for g in G})
        if kind == "FD":
            classes = [(y, [t for t in pot if missing[t] == y and z[(t, j)] in model]) for y in range(5) if y != gp(x)
                       for j in range(ncl)]
        else:
            classes = [(j, [t for t in pot if z[(t, j)] in model]) for j in range(ncl)]
        sec = {}
        for g in G:
            xp = g[x]
            assert xp not in sec
            sec[xp] = [(gp(g[6 * lab_]) if kind == "FD" else lab_, sorted(img(g, t) for t in C)) for lab_, C in classes]
        lines = [f"GDD34 {kind}GDD 5 6", "GROUPS"] + [" ".join(str(6 * i + a) for a in range(6)) for i in range(5)]
        lines += ["BLOCKS"] + [" ".join(map(str, b)) for b in blocks]
        for xp in sorted(sec):
            lines.append(f"POINT {xp}")
            for lb, C in sec[xp]:
                lines.append(f"{'FRAME' if kind == 'FD' else 'PC'} {lb}")
                lines += [" ".join(map(str, t)) for t in C]
        cert = os.path.join(out, f"{kind.lower()}gdd_5_6_{gname}_s{seed}.txt")
        with xopen(cert) as fh:
            fh.write("\n".join(lines) + "\n")
        rec["certificate"] = cert
        rec["blocks"] = len(blocks)
    with xopen(os.path.join(out, "summary.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


if __name__ == "__main__":
    main()

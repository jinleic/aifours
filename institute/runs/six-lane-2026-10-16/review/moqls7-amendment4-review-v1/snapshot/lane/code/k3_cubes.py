#!/usr/bin/env python3
"""Append a covering K3 row-frame cube and forced same-ray Gram identities.

Base encoders remain unchanged. See review/AMENDMENT-2.r1.md. Commands:
  coverage OUT.json
  make A|B C311|C321|C411 OUT.cnf OUT.json
No solver is launched by this module.
"""
import argparse
import hashlib
import itertools
import json
import os
import subprocess

import gram_enc

HERE = os.path.dirname(os.path.abspath(__file__))
CUBES = {"C311": ({1, 2, 3}, {4}, {5}),
         "C321": ({1, 2, 3}, {4, 5}, {6}),
         "C411": ({1, 2, 3, 4}, {5}, {6})}
PTS = [(i, j) for i in range(7) for j in range(7)]
POINT = (1, 0)


def digest(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def coverage():
    valid = set()
    for labels in itertools.product(range(4), repeat=3):
        if 2 in labels and 3 in labels:
            valid.add(labels)
    orbits = {}
    for name, supports in CUBES.items():
        orbit = set()
        for perm in itertools.permutations((4, 5, 6)):
            relabel = dict(zip((4, 5, 6), perm))
            for swap in (False, True):
                result = [set() for _ in range(3)]
                for a, S in enumerate(supports):
                    b = 3 - a if swap and a in (1, 2) else a
                    result[b] = {relabel.get(k, k) for k in S}
                labels = tuple(next((a + 1 for a in range(3) if k in result[a]), 0) for k in (4, 5, 6))
                assert 2 in labels and 3 in labels
                orbit.add(labels)
        orbits[name] = orbit
    union = set().union(*orbits.values())
    assert len(valid) == 18 and union == valid
    assert all(not (orbits[a] & orbits[b]) for a, b in itertools.combinations(CUBES, 2))
    return {"status": "PASS", "valid_assignments": sorted(valid), "n_valid": len(valid),
            "orbits": {name: sorted(orbit) for name, orbit in orbits.items()},
            "complete_disjoint_cover": True}


def variable_map():
    # Written independently of encoder A's map. Encoder B allocates exactly
    # this prefix: square, earlier point, later point, skipping common lines.
    result = {}
    for a in (1, 2, 3):
        for p, q in itertools.combinations(PTS, 2):
            if p[0] != q[0] and p[1] != q[1]:
                result[(a, p, q)] = len(result) + 1
    assert len(result) == 2646
    return result


def cube_clauses(vmap, name):
    supports = CUBES[name]
    def g(a, p, q):
        return vmap.get((a, min(p, q), max(p, q)))
    clauses = []
    for a, S in enumerate(supports, 1):
        for k in range(1, 7):
            v = g(a, POINT, (0, k))
            assert v is not None
            clauses.append([v if k in S else -v])
    n_units = len(clauses)
    singletons = []
    for a, S in enumerate(supports, 1):
        if len(S) != 1:
            continue
        q = (0, next(iter(S)))
        singletons.append({"square": a, "p": POINT, "q": q})
        for t in PTS:
            if t in (POINT, q):
                continue
            left, right = g(a, POINT, t), g(a, q, t)
            if left is None and right is None:
                continue
            if left is None:
                clauses.append([-right])
            elif right is None:
                clauses.append([-left])
            else:
                clauses.extend(([-left, right], [left, -right]))
    return clauses, n_units, singletons


def make(encoder, cube, outcnf, outmeta):
    for path in (outcnf, outmeta):
        if os.path.exists(path):
            raise FileExistsError(path)
    coverage()
    vmap = variable_map()
    # Base output is a disposable scratch product, never frozen evidence.
    scratch = os.path.join(HERE, "..", "explore", "scratch")
    os.makedirs(scratch, exist_ok=True)
    if encoder == "A":
        F, actual = gram_enc.build(3, None, True, True, None)
        expected = {"%d|%d,%d|%d,%d" % (a, p[0], p[1], q[0], q[1]): v
                    for (a, p, q), v in vmap.items()}
        assert actual == expected
        base = F.text()
    else:
        basepath = os.path.join(scratch, "k3_cube_B_base.cnf")
        subprocess.run(["/usr/bin/python3", "-B", os.path.join(HERE, "gram_encB.py"),
                        "--squares", "3", "--heavy", "--sym", "--out", basepath],
                       check=True, capture_output=True)
        with open(basepath) as f:
            base = f.read()
    header, body = base.split("\n", 1)
    tag, form, nv, nc = header.split()
    assert (tag, form) == ("p", "cnf") and int(nv) >= len(vmap)
    clauses, units, twins = cube_clauses(vmap, cube)
    with open(outcnf, "x") as f:
        f.write("p cnf %s %d\n" % (nv, int(nc) + len(clauses)))
        f.write(body)
        for cl in clauses:
            f.write(" ".join(map(str, cl)) + " 0\n")
    meta = {"encoder": encoder, "cube": cube, "base_cnf_sha256": hashlib.sha256(base.encode()).hexdigest(),
            "cnf_sha256": digest(outcnf), "wrapper_sha256": digest(__file__),
            "base_encoder_sha256": digest(os.path.join(HERE, "gram_enc.py" if encoder == "A" else "gram_encB.py")),
            "support_sets": [sorted(S) for S in CUBES[cube]], "cube_unit_clauses": units,
            "same_ray_identities": twins, "extra_clauses": len(clauses)}
    with open(outmeta, "x") as f:
        json.dump(meta, f, indent=2)
        f.write("\n")
    print(json.dumps(meta))


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="command", required=True)
    cov = sub.add_parser("coverage")
    cov.add_argument("out")
    mk = sub.add_parser("make")
    mk.add_argument("encoder", choices=("A", "B"))
    mk.add_argument("cube", choices=tuple(CUBES))
    mk.add_argument("outcnf")
    mk.add_argument("outmeta")
    a = ap.parse_args()
    if a.command == "coverage":
        with open(a.out, "x") as f:
            json.dump(coverage(), f, indent=2)
            f.write("\n")
        print("PASS: 18 predicate assignments, three disjoint six-element residual-symmetry orbits")
    else:
        make(a.encoder, a.cube, a.outcnf, a.outmeta)


if __name__ == "__main__":
    main()

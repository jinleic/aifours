"""Independent SECOND-PATH check of the pinned K4 permutation arrays (Claude orbit review m1; no NumPy, no name table,
no code shared with k4_automorphism_r3.py). Reads the CNF bytes once (SHA-256 of exactly these bytes must equal the
pin), parses them with its own line-by-line DIMACS reader (header 'p cnf V C'; every clause line: integer tokens, the
last one 0 and no other 0; exactly C clause lines; every |literal| in [1,V]), loads each pinned array with the stdlib
`array` module (little-endian int32, V+1 entries, entry 0 = 0; SHA-256 of the file bytes must equal the pin), and checks
  - bijection: entries 1..V are exactly {1..V};
  - automorphism: the sorted list of packed sorted-literal clauses of F equals that of π(F) (Timsort + list equality,
    exact; multiplicities kept);
  - group: g1∘g1 = g2∘g2 = id, (g1∘g2)^3 = id, g1∘g2 ≠ id, closure of order 6, each element an automorphism;
  - cube maps: every element maps V1 root assignments to V1 root assignments and V2 assignments to V2 assignments;
  - controls: identity PASS; g1 with the images of 57 and 64 swapped FAIL; polarity flip FAIL.
python -B k4_auto_secondpath.py --g1 PERM_g1.i32le --g1-sha SHA --g2 PERM_g2.i32le --g2-sha SHA --out R.json
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import struct
import sys
import time
from array import array

HERE = os.path.dirname(os.path.abspath(__file__))
CNF = os.path.normpath(os.path.join(HERE, "..", "evidence", "k4_w1_v1", "GA3_K4w1.cnf"))
BASE_SHA = "7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7"
V1 = [57, 106, 155, 204, 253, 302, 351]
V2 = [64, 113, 162, 211, 260, 309, 358]


def clauses(raw):
    f = io.BytesIO(raw)
    head = f.readline().split()
    if len(head) != 4 or head[0] != b"p" or head[1] != b"cnf":
        raise SystemExit("bad header")
    V, C = int(head[2]), int(head[3])
    n = 0
    for line in f:
        t = line.split()
        if not t:
            continue
        lits = [int(x) for x in t]
        if lits[-1] != 0 or 0 in lits[:-1] or len(lits) < 2:
            raise SystemExit("bad clause line %d" % (n + 1))
        n += 1
        yield V, C, lits[:-1]
    if n != C:
        raise SystemExit("clause count %d != header %d" % (n, C))


def packed_sorted(raw, perm=None, flip=False):
    out = []
    V = None
    for V, C, lits in clauses(raw):
        if perm is not None:
            lits = [(perm[l] if l > 0 else -perm[-l]) * (-1 if flip else 1) for l in lits]
        for l in lits:
            if not 1 <= abs(l) <= V:
                raise SystemExit("literal out of range")
        lits.sort()
        out.append(struct.pack("<%di" % len(lits), *lits))
    out.sort()
    return V, out


def load(path, pin):
    b = open(path, "rb").read()
    if hashlib.sha256(b).hexdigest() != pin:
        raise SystemExit("array hash mismatch: %s" % path)
    a = array("i")
    if a.itemsize != 4:
        raise SystemExit("int32 itemsize")
    a.frombytes(b)
    if sys.byteorder != "little":
        a.byteswap()
    return a


def assign(Vs, b):
    return tuple(sorted(v if (b >> k) & 1 else -v for k, v in enumerate(Vs)))


def img(p, cube):
    return tuple(sorted(p[l] if l > 0 else -p[-l] for l in cube))


def main():
    ap = argparse.ArgumentParser()
    for k in ("g1", "g1-sha", "g2", "g2-sha", "out"):
        ap.add_argument("--" + k, required=True)
    a = ap.parse_args()
    t0 = time.time()
    raw = open(CNF, "rb").read()
    res = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "python": sys.version, "cnf_sha256": hashlib.sha256(raw).hexdigest()}
    if res["cnf_sha256"] != BASE_SHA:
        raise SystemExit("CNF hash mismatch")
    V, F = packed_sorted(raw)
    res["clauses"] = len(F)
    g1, g2 = load(a.g1, a.g1_sha), load(a.g2, a.g2_sha)
    ident = array("i", range(V + 1))
    memo = {}

    def bij(p):
        return len(p) == V + 1 and p[0] == 0 and set(p[1:]) == set(range(1, V + 1))

    def auto(p, flip=False):
        key = (p.tobytes(), flip)
        if key not in memo:
            memo[key] = bij(p) and packed_sorted(raw, p, flip)[1] == F
        return memo[key]

    comp = lambda p, q: array("i", (p[q[i]] for i in range(V + 1)))
    out = {"g1": {"bijection": bij(g1), "automorphism": auto(g1)},
           "g2": {"bijection": bij(g2), "automorphism": auto(g2)}}
    g12 = comp(g1, g2)
    grp = {"g1_squared_id": comp(g1, g1) == ident, "g2_squared_id": comp(g2, g2) == ident, "g1g2_ne_id": g12 != ident,
           "g1g2_cubed_id": comp(g12, comp(g12, g12)) == ident}
    elems = {ident.tobytes(): ident}
    frontier = [ident]
    while frontier:
        nxt = []
        for p in frontier:
            for gen in (g1, g2):
                q = comp(gen, p)
                if q.tobytes() not in elems:
                    elems[q.tobytes()] = q
                    nxt.append(q)
        frontier = nxt
    grp["order"] = len(elems)
    grp["all_elements_automorphisms"] = all(auto(p) for p in elems.values())
    roots = {assign(V1, b) for b in range(128)}
    kids = {assign(V2, b) for b in range(128)}
    cubes = {"V1_roots_closed": all(img(p, c) in roots for p in elems.values() for c in roots),
             "V2_assignments_closed": all(img(p, c) in kids for p in elems.values() for c in kids)}
    bad = array("i", g1)
    bad[57], bad[64] = bad[64], bad[57]
    ctl = {"identity": auto(ident), "NEG swap 57/64": auto(bad), "NEG polarity flip": auto(g1, flip=True)}
    res.update({"arrays": {"g1": {"path": a.g1, "sha256": a.g1_sha}, "g2": {"path": a.g2, "sha256": a.g2_sha}},
                "checks": out, "group": grp, "cubes": cubes, "controls": ctl,
                "verdict": bool(all(out[k]["bijection"] is True and out[k]["automorphism"] is True for k in out)
                                and grp["order"] == 6 and all(grp[k] is True for k in grp if k != "order")
                                and all(cubes.values()) and ctl["identity"] is True
                                and ctl["NEG swap 57/64"] is False and ctl["NEG polarity flip"] is False),
                "secs": round(time.time() - t0, 1)})
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({k: res[k] for k in ("checks", "group", "cubes", "controls", "verdict", "secs")}))


if __name__ == "__main__":
    main()

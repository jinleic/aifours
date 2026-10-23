"""K4 base-CNF automorphism check, revision r2 (supersedes the never-run draft code/k4_automorphism.py). CHECK ONLY.
Inputs (all hash-pinned): the stored K4 base CNF (SHA-256 7bb806fc…01f7, streamed SHA verified), the parent's full
semantic name table review/moqls8-encoder-binding-v1/K4.names.json.gz (SHA-256 ed0462bc…8e2d; g entries cross-checked
with the lane map evidence/k4_w1_v1/GA3_K4w1.map.json).
Permutation: σ on {0..7} acting simultaneously on rows, columns and coordinates (cell (i,j) ↦ (σi,σj)); square
relabelling ρ. Variable map π from CANONICAL identities: g ↦ (s, {p,q}); b3 ↦ (s, {x,y}, z); c4 ↦ (s, a, {p,q});
u5 ↦ (s, line, q, a); w3 ↦ (s, line, p) with line = ("row", i) or ("col", j); every canonical identity must belong to
exactly one variable (injectivity), every image identity must exist (totality); π must be a bijection of 1..V.
Equality test: EXACT — each clause is its int32 literal vector sorted ascending; clauses are grouped by length and the
rows of each group sorted lexicographically; F and π(F) must be element-wise identical (no hashing).
Group: generators (5 6) and (6 7) with ρ swapping the matching Q2/Q3/Q4; checks g1² = g2² = id, (g1g2)³ = id, closure
of order 6, every element an automorphism; V1 roots and V2 children mapped to complete assignments; orbit tables.
Controls: identity (must PASS), σ = (4 5) with ρ = id (must FAIL: moves the SB2 units), and π(5 6) with the images of
variables 57 and 64 swapped (must FAIL). Guards: free ≥ 12e9 at start; own max RSS ≤ 1.75 GiB at every phase.
python -B k4_automorphism_r2.py --out ../evidence/k4_split_v1/AUTOMORPHISM_S3_567_r2.json
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import resource
import shutil
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
CNF = os.path.join(LANE, "evidence", "k4_w1_v1", "GA3_K4w1.cnf")
MAP = os.path.join(LANE, "evidence", "k4_w1_v1", "GA3_K4w1.map.json")
NAMES = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-encoder-binding-v1/K4.names.json.gz"
BASE_SHA = "7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7"
NAMES_SHA = "ed0462bc4de7fdcbc34397e1b05304160e47b9ba4a1bd1c858c5f997df3f8e2d"
V1 = [57, 106, 155, 204, 253, 302, 351]
V2 = [64, 113, 162, 211, 260, 309, 358]
RSS_CAP = int(1.75 * 2 ** 30)
LOG = []


def guard(phase):
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    LOG.append([phase, round(time.time(), 1), rss])
    if rss > RSS_CAP:
        raise SystemExit("RSS guard tripped at %s: %d" % (phase, rss))


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 24), b""):
            h.update(chunk)
    return h.hexdigest()


def T(c):
    return (int(c[0]), int(c[1]))


def line_id(l0, l1):
    return ("row", l0[0]) if l0[0] == l1[0] else ("col", l0[1])


def canon(name):
    t, s = name[0], int(name[1])
    if t == "g":
        return ("g", s, frozenset((T(name[2]), T(name[3]))))
    if t == "b3":
        return ("b3", s, frozenset((T(name[2]), T(name[3]))), T(name[4]))
    if t == "c4":
        return ("c4", s, T(name[2]), frozenset((T(name[3]), T(name[4]))))
    if t == "u5":
        return ("u5", s, line_id(T(name[2]), T(name[3])), T(name[4]), T(name[5]))
    if t == "w3":
        return ("w3", s, line_id(T(name[2]), T(name[3])), T(name[4]))
    raise ValueError("unknown family %r" % t)


def image(key, sigma, rho):
    cell = lambda p: (sigma[p[0]], sigma[p[1]])
    ln = lambda l: (l[0], sigma[l[1]])
    t, s = key[0], rho[key[1]]
    if t == "g":
        return ("g", s, frozenset(cell(p) for p in key[2]))
    if t == "b3":
        return ("b3", s, frozenset(cell(p) for p in key[2]), cell(key[3]))
    if t == "c4":
        return ("c4", s, cell(key[2]), frozenset(cell(p) for p in key[3]))
    if t == "u5":
        return ("u5", s, ln(key[2]), cell(key[3]), cell(key[4]))
    return ("w3", s, ln(key[2]), cell(key[3]))


def build_perm(keys, index, sigma, rho, V):
    perm = np.zeros(V + 1, dtype=np.int32)
    missing = 0
    for v in range(1, V + 1):
        w = index.get(image(keys[v], sigma, rho))
        if w is None:
            missing += 1
        else:
            perm[v] = w
    bij = missing == 0 and np.array_equal(np.sort(perm[1:]), np.arange(1, V + 1))
    return perm, missing, bool(bij)


def groups_of(flat, starts, lens):
    out = {}
    for L in np.unique(lens):
        idx = np.flatnonzero(lens == L)
        M = flat[starts[idx][:, None] + np.arange(L)[None, :]]
        M.sort(axis=1)
        order = np.lexsort(M.T[::-1])
        out[int(L)] = M[order]
    return out


def apply(perm, arr):
    out = perm[np.abs(arr)]
    np.negative(out, where=arr < 0, out=out)
    return out


def is_auto(perm, arr, starts, lens, G0):
    G1 = groups_of(apply(perm, arr), starts, lens)
    return all(np.array_equal(G0[L], G1[L]) for L in G0) and set(G0) == set(G1)


def cube_image(perm, lits):
    return sorted(int(np.sign(l) * perm[abs(l)]) for l in lits)


def assignment(Vs, b):
    return sorted(v if (b >> k) & 1 else -v for k, v in enumerate(Vs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    t0 = time.time()
    res = {"argv": sys.argv, "script_sha256": sha_file(__file__), "start": time.ctime()}
    free = shutil.disk_usage(LANE).free
    res["free_at_start"] = free
    if free < 12_000_000_000:
        raise SystemExit("disk floor")
    res["names_sha256"] = sha_file(NAMES)
    res["cnf_sha256"] = sha_file(CNF)
    res["map_sha256"] = sha_file(MAP)
    if res["names_sha256"] != NAMES_SHA or res["cnf_sha256"] != BASE_SHA:
        raise SystemExit("pinned input hash mismatch")
    table = json.load(gzip.open(NAMES))
    V = len(table)
    keys = [None] * (V + 1)
    for v, name in table:
        if keys[v] is not None:
            raise SystemExit("duplicate id in names table")
        keys[v] = canon(name)
    del table
    assert all(k is not None for k in keys[1:])
    index = {}
    for v in range(1, V + 1):
        if keys[v] in index:
            raise SystemExit("two variables share one canonical identity: %r" % (keys[v],))
        index[keys[v]] = v
    lane_g = json.load(open(MAP))["vars"]
    gmis = sum(1 for k, v in lane_g.items() if json.loads(k)[0] == "g"
               and index.get(canon(json.loads(k))) != v)
    res["names"] = {"variables": V, "injective_canonical_identities": True, "lane_map_g_mismatches": gmis,
                    "families": {f: sum(1 for k in keys[1:] if k[0] == f) for f in ("g", "b3", "c4", "u5", "w3")}}
    guard("names")
    raw = open(CNF, "rb").read()
    nl = raw.index(b"\n")
    hv, hc = int(raw[:nl].split()[2]), int(raw[:nl].split()[3])
    arr = np.fromstring(raw[nl + 1:].decode(), dtype=np.int32, sep=" ")
    del raw
    zeros = np.flatnonzero(arr == 0)
    starts = np.concatenate(([0], zeros[:-1] + 1))
    lens = zeros - starts
    res["cnf"] = {"header_vars": hv, "header_clauses": hc, "parsed_clauses": int(len(zeros)),
                  "literals": int(len(arr) - len(zeros)), "max_var": int(np.abs(arr).max())}
    if hv != V or hc != len(zeros):
        raise SystemExit("CNF/names size mismatch")
    G0 = groups_of(arr, starts, lens)
    guard("parsed")
    ident = list(range(8))
    s56 = [0, 1, 2, 3, 4, 6, 5, 7]
    s67 = [0, 1, 2, 3, 4, 5, 7, 6]
    s45 = [0, 1, 2, 3, 5, 4, 6, 7]
    rho_id = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    rho56 = {1: 1, 2: 3, 3: 2, 4: 4, 5: 5}
    rho67 = {1: 1, 2: 2, 3: 4, 4: 3, 5: 5}
    checks = {}
    P = {}
    for nm, sg, rh in (("identity", ident, rho_id), ("g1=(5 6)", s56, rho56), ("g2=(6 7)", s67, rho67),
                       ("NEG sigma=(4 5), rho=id", s45, rho_id)):
        perm, missing, bij = build_perm(keys, index, sg, rh, V)
        auto = bool(bij and is_auto(perm, arr, starts, lens, G0))
        checks[nm] = {"sigma": sg, "rho": rh, "unmapped": missing, "bijection": bij, "automorphism": auto}
        P[nm] = perm
        guard(nm)
    bad = P["g1=(5 6)"].copy()
    bad[57], bad[64] = bad[64], bad[57]
    checks["NEG corrupted map (g1 with images of 57, 64 swapped)"] = {
        "bijection": bool(np.array_equal(np.sort(bad[1:]), np.arange(1, V + 1))),
        "automorphism": bool(is_auto(bad, arr, starts, lens, G0))}
    guard("corrupt")
    g1, g2 = P["g1=(5 6)"], P["g2=(6 7)"]
    idp = np.arange(V + 1, dtype=np.int32)
    comp = lambda p, q: p[q]
    g12 = comp(g1, g2)
    res["group"] = {"g1_squared_id": bool(np.array_equal(comp(g1, g1), idp)),
                    "g2_squared_id": bool(np.array_equal(comp(g2, g2), idp)),
                    "g1g2_ne_id": not np.array_equal(g12, idp),
                    "g1g2_cubed_id": bool(np.array_equal(comp(g12, comp(g12, g12)), idp))}
    elems = {idp.tobytes(): idp}
    frontier = [idp]
    while frontier:
        nxt = []
        for p in frontier:
            for gen in (g1, g2):
                q = comp(gen, p)
                if q.tobytes() not in elems:
                    elems[q.tobytes()] = q
                    nxt.append(q)
        frontier = nxt
    group = list(elems.values())
    res["group"]["order"] = len(group)
    res["group"]["all_elements_automorphisms"] = all(is_auto(p, arr, starts, lens, G0) for p in group)
    guard("group")
    roots = {tuple(assignment(V1, b)): b for b in range(128)}
    orb, rep = {}, {}
    ok_cubes = True
    for b in range(128):
        imgs = set()
        for p in group:
            im = tuple(cube_image(p, assignment(V1, b)))
            if im not in roots:
                ok_cubes = False
            else:
                imgs.add(roots[im])
        r = min(imgs) if imgs else b
        rep[b] = r
        orb.setdefault(r, sorted(imgs))
    res["V1_roots"] = {"all_images_are_roots": ok_cubes, "orbits": len(orb),
                       "orbit_table": {"c%03d" % r: ["c%03d" % x for x in v] for r, v in sorted(orb.items())}}
    ch = {tuple(assignment(V2, b)): b for b in range(128)}
    stab = {}
    for r in sorted(orb):
        st = [p for p in group if tuple(cube_image(p, assignment(V1, r))) == tuple(assignment(V1, r))]
        corb, okc = {}, True
        for b in range(128):
            imgs = set()
            for p in st:
                im = tuple(cube_image(p, assignment(V2, b)))
                if im not in ch:
                    okc = False
                else:
                    imgs.add(ch[im])
            corb.setdefault(min(imgs) if imgs else b, sorted(imgs))
        stab["c%03d" % r] = {"stabiliser_order": len(st), "V2_images_are_children": okc,
                              "child_orbits": len(corb)}
    res["V2_children_under_stabilisers"] = stab
    res["checks"] = checks
    res["verdict"] = {
        "controls_as_intended": (checks["identity"]["automorphism"] is True
                                 and checks["NEG sigma=(4 5), rho=id"]["automorphism"] is False
                                 and checks["NEG corrupted map (g1 with images of 57, 64 swapped)"]["automorphism"]
                                 is False),
        "generators_automorphisms": checks["g1=(5 6)"]["automorphism"] and checks["g2=(6 7)"]["automorphism"],
        "S3_of_order_6": res["group"]["order"] == 6 and all(res["group"][k] for k in (
            "g1_squared_id", "g2_squared_id", "g1g2_ne_id", "g1g2_cubed_id", "all_elements_automorphisms"))}
    res["guard_log"] = LOG
    res["secs"] = round(time.time() - t0, 1)
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1, default=str)
    print(json.dumps({"names": res["names"], "cnf": res["cnf"], "checks": checks, "group": res["group"],
                      "V1_orbits": res["V1_roots"]["orbits"], "verdict": res["verdict"], "secs": res["secs"],
                      "max_rss": LOG[-1][2]}, default=str))


if __name__ == "__main__":
    main()

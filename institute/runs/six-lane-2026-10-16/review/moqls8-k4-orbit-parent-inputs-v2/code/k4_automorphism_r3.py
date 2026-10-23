"""K4 base-CNF automorphism check, revision r3 (Claude orbit review M1, m3, m5, m10, m11; supersedes r2's receipt for
certification use). CHECK ONLY; writes the permutation arrays and a receipt (exclusive create).
1. Reads the K4 base CNF ONCE into memory; the SHA-256 is computed on exactly these bytes and must equal the pin; the
   SAME bytes are parsed (NumPy, warnings are errors); asserts: last token 0, Σ clause lengths + #terminators =
   #tokens, #terminators = header clauses, max |literal| = header variables.
2. Builds π_g1, π_g2 from the pinned name table (construction only: σ1 = (5 6), ρ1 = (Q2 Q3); σ2 = (6 7),
   ρ2 = (Q3 Q4); canonical identities must be injective and every image must exist).
3. Writes each as a little-endian int32 array over 0..V with perm[0] = 0 (files PERM_g1.i32le, PERM_g2.i32le),
   RELOADS the files from disk and runs every test on the reloaded arrays only; records their SHA-256.
4. Tests on reloaded arrays: values in [1,V] and a bijection; EXACT clause-multiset invariance (per length, sorted
   int32 rows, lexicographically sorted matrices compared element-wise); group relations and closure (order 6, all
   elements automorphisms); V1 root images, stabiliser V2 images, orbit tables (planning only).
5. Controls (each must come out as stated): identity PASS; σ = (4 5), ρ = id FAIL; π_g1 with images of 57/64 swapped
   FAIL; polarity flip v ↦ −π_g1(v) FAIL; non-injective (π_g1 with perm[64] := perm[57]) not a bijection → FAIL.
python -B k4_automorphism_r3.py --names <K4.names.json.gz> --outdir ../evidence/k4_split_v1/auto_r3
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import platform
import resource
import shutil
import sys
import time
import warnings

import numpy as np

warnings.simplefilter("error")
HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.normpath(os.path.join(HERE, ".."))
CNF = os.path.join(LANE, "evidence", "k4_w1_v1", "GA3_K4w1.cnf")
BASE_SHA = "7bb806fc8f7793fa5088cc78caf3ebf5b49a72cad82c527f47cf6faced4301f7"
NAMES_SHA = "ed0462bc4de7fdcbc34397e1b05304160e47b9ba4a1bd1c858c5f997df3f8e2d"
V1 = [57, 106, 155, 204, 253, 302, 351]
V2 = [64, 113, 162, 211, 260, 309, 358]
RSS_CAP = int(1.75 * 2 ** 30)
LOG = []


def guard(phase):
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = r if sys.platform == "darwin" else r * 1024
    LOG.append([phase, round(time.time(), 1), rss])
    if rss > RSS_CAP:
        raise SystemExit("RSS guard tripped at %s: %d" % (phase, rss))


def T(c):
    if len(c) != 2:
        raise SystemExit("bad cell %r" % (c,))
    return (int(c[0]), int(c[1]))


def line_id(l0, l1):
    if l0[0] == l1[0]:
        return ("row", l0[0])
    if l0[1] == l1[1]:
        return ("col", l0[1])
    raise SystemExit("non-collinear line identity %r %r" % (l0, l1))


def canon(name):
    t, s = name[0], int(name[1])
    if t == "g" and len(name) == 4:
        return ("g", s, frozenset((T(name[2]), T(name[3]))))
    if t == "b3" and len(name) == 5:
        return ("b3", s, frozenset((T(name[2]), T(name[3]))), T(name[4]))
    if t == "c4" and len(name) == 5:
        return ("c4", s, T(name[2]), frozenset((T(name[3]), T(name[4]))))
    if t == "u5" and len(name) == 6:
        return ("u5", s, line_id(T(name[2]), T(name[3])), T(name[4]), T(name[5]))
    if t == "w3" and len(name) == 5:
        return ("w3", s, line_id(T(name[2]), T(name[3])), T(name[4]))
    raise SystemExit("unknown variable name %r" % (name,))


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
    perm = np.zeros(V + 1, dtype="<i4")
    for v in range(1, V + 1):
        w = index.get(image(keys[v], sigma, rho))
        if w is None:
            raise SystemExit("image identity missing for variable %d" % v)
        perm[v] = w
    return perm


def is_bijection(perm, V):
    return bool(perm[0] == 0 and perm.shape == (V + 1,) and np.array_equal(np.sort(perm[1:]), np.arange(1, V + 1)))


def groups_of(flat, starts, lens):
    out = {}
    for L in np.unique(lens):
        idx = np.flatnonzero(lens == L)
        M = flat[starts[idx][:, None] + np.arange(L)[None, :]]
        M.sort(axis=1)
        out[int(L)] = M[np.lexsort(M.T[::-1])]
    return out


def apply(perm, arr):
    out = perm[np.abs(arr)].astype(np.int32)
    np.negative(out, where=arr < 0, out=out)
    return out


def is_auto(perm, arr, starts, lens, G0, V):
    if not is_bijection(np.abs(perm), V):
        return False
    G1 = groups_of(apply(perm, arr), starts, lens)
    return bool(set(G0) == set(G1) and all(np.array_equal(G0[L], G1[L]) for L in G0))


def cube_image(perm, lits):
    return sorted(int(perm[abs(l)]) * (1 if l > 0 else -1) for l in lits)


def assignment(Vs, b):
    return sorted(v if (b >> k) & 1 else -v for k, v in enumerate(Vs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", required=True)
    ap.add_argument("--outdir", required=True)
    a = ap.parse_args()
    t0 = time.time()
    os.makedirs(a.outdir, exist_ok=False)
    res = {"argv": sys.argv, "script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "python": sys.version, "numpy": np.__version__, "platform": platform.platform(), "start": time.ctime()}
    if shutil.disk_usage(LANE).free < 12_000_000_000:
        raise SystemExit("disk floor")
    nb = open(a.names, "rb").read()
    res["names_sha256"] = hashlib.sha256(nb).hexdigest()
    if res["names_sha256"] != NAMES_SHA:
        raise SystemExit("names hash mismatch")
    table = json.loads(gzip.decompress(nb))
    del nb
    V = len(table)
    keys = [None] * (V + 1)
    for v, name in table:
        if not (isinstance(v, int) and 1 <= v <= V) or keys[v] is not None:
            raise SystemExit("bad or duplicate id in names table: %r" % (v,))
        keys[v] = canon(name)
    del table
    if any(k is None for k in keys[1:]):
        raise SystemExit("names table not total")
    index = {}
    for v in range(1, V + 1):
        if keys[v] in index:
            raise SystemExit("canonical identity shared by two variables")
        index[keys[v]] = v
    guard("names")
    raw = open(CNF, "rb").read()
    res["cnf_sha256"] = hashlib.sha256(raw).hexdigest()
    if res["cnf_sha256"] != BASE_SHA:
        raise SystemExit("CNF hash mismatch")
    nl = raw.index(b"\n")
    head = raw[:nl].split()
    if head[:2] != [b"p", b"cnf"] or len(head) != 4:
        raise SystemExit("bad header")
    hv, hc = int(head[2]), int(head[3])
    body = raw[nl + 1:].decode("ascii")
    del raw
    arr = np.fromstring(body, dtype=np.int32, sep=" ")
    del body
    zeros = np.flatnonzero(arr == 0)
    starts = np.concatenate(([0], zeros[:-1] + 1))
    lens = zeros - starts
    parse = {"header_vars": hv, "header_clauses": hc, "tokens": int(arr.size), "terminators": int(zeros.size),
             "last_token_zero": bool(arr.size > 0 and arr[-1] == 0),
             "lengths_identity": bool(int(lens.sum()) + int(zeros.size) == int(arr.size)),
             "max_abs_literal": int(np.abs(arr).max()), "min_clause_len": int(lens.min())}
    res["parse"] = parse
    if not (parse["last_token_zero"] and parse["lengths_identity"] and hc == zeros.size and hv == V
            and parse["max_abs_literal"] == V and parse["min_clause_len"] >= 1):
        raise SystemExit("parse checks failed: %r" % parse)
    G0 = groups_of(arr, starts, lens)
    guard("parsed")
    s56, s67, s45 = [0, 1, 2, 3, 4, 6, 5, 7], [0, 1, 2, 3, 4, 5, 7, 6], [0, 1, 2, 3, 5, 4, 6, 7]
    rid = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
    files = {}
    for nm, sg, rh in (("g1", s56, {1: 1, 2: 3, 3: 2, 4: 4, 5: 5}), ("g2", s67, {1: 1, 2: 2, 3: 4, 4: 3, 5: 5})):
        p = build_perm(keys, index, sg, rh, V)
        path = os.path.join(a.outdir, "PERM_%s.i32le" % nm)
        with open(path, "xb") as fh:
            fh.write(p.astype("<i4").tobytes())
        files[nm] = {"path": os.path.relpath(path, LANE), "sigma": sg, "rho": rh}
        del p
    neg45 = build_perm(keys, index, s45, rid, V)
    del keys, index
    guard("built")
    P = {}
    for nm in ("g1", "g2"):
        b = open(os.path.join(LANE, files[nm]["path"]), "rb").read()
        files[nm]["sha256"] = hashlib.sha256(b).hexdigest()
        files[nm]["bytes"] = len(b)
        P[nm] = np.frombuffer(b, dtype="<i4").astype(np.int32)
        files[nm]["bijection"] = is_bijection(P[nm], V)
        files[nm]["automorphism"] = is_auto(P[nm], arr, starts, lens, G0, V)
        guard("reloaded " + nm)
    res["arrays"] = files
    idp = np.arange(V + 1, dtype=np.int32)
    ctl = {"identity": is_auto(idp, arr, starts, lens, G0, V),
           "NEG sigma=(4 5), rho=id": is_auto(neg45, arr, starts, lens, G0, V)}
    bad = P["g1"].copy()
    bad[57], bad[64] = bad[64], bad[57]
    ctl["NEG g1 with images of 57/64 swapped"] = is_auto(bad, arr, starts, lens, G0, V)
    ctl["NEG polarity flip of g1"] = is_auto(-P["g1"], arr, starts, lens, G0, V)
    ni = P["g1"].copy()
    ni[64] = ni[57]
    ctl["NEG non-injective g1"] = is_auto(ni, arr, starts, lens, G0, V)
    res["controls"] = ctl
    del bad, ni, neg45
    guard("controls")
    g1, g2 = P["g1"], P["g2"]
    comp = lambda p, q: p[q]
    g12 = comp(g1, g2)
    grp = {"g1_squared_id": bool(np.array_equal(comp(g1, g1), idp)),
           "g2_squared_id": bool(np.array_equal(comp(g2, g2), idp)),
           "g1g2_ne_id": bool(not np.array_equal(g12, idp)),
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
    grp["order"] = len(group)
    grp["all_elements_automorphisms"] = all(is_auto(p, arr, starts, lens, G0, V) for p in group)
    res["group"] = grp
    guard("group")
    roots = {tuple(assignment(V1, b)): b for b in range(128)}
    children = {tuple(assignment(V2, b)): b for b in range(128)}
    ok_roots = all(tuple(cube_image(p, assignment(V1, b))) in roots for p in group for b in range(128))
    ok_v2 = all(tuple(cube_image(p, assignment(V2, b))) in children for p in group for b in range(128))
    orb = {}
    for b in range(128):
        imgs = sorted({roots[tuple(cube_image(p, assignment(V1, b)))] for p in group})
        orb.setdefault(imgs[0], imgs)
    stab = {}
    for r in sorted(orb):
        st = [p for p in group if tuple(cube_image(p, assignment(V1, r))) == tuple(assignment(V1, r))]
        co = {}
        for b in range(128):
            imgs = sorted({children[tuple(cube_image(p, assignment(V2, b)))] for p in st})
            co.setdefault(imgs[0], imgs)
        stab["c%03d" % r] = {"stabiliser_order": len(st), "child_orbits": len(co)}
    res["planning_only_orbits"] = {
        "all_group_images_of_V1_roots_are_roots": ok_roots, "all_group_images_of_V2_assignments_are_V2": ok_v2,
        "root_orbits": len(orb), "orbit_table": {"c%03d" % r: ["c%03d" % x for x in v] for r, v in sorted(orb.items())},
        "stabilisers": stab}
    res["verdict"] = {
        "arrays_bijective_automorphisms": all(files[n]["bijection"] is True and files[n]["automorphism"] is True
                                              for n in ("g1", "g2")),
        "controls_as_intended": (ctl["identity"] is True and all(ctl[k] is False for k in ctl if k.startswith("NEG"))),
        "S3_of_order_6": grp["order"] == 6 and all(grp[k] is True for k in grp if k != "order")}
    res["guard_log"] = LOG
    res["secs"] = round(time.time() - t0, 1)
    with open(os.path.join(a.outdir, "RECEIPT.json"), "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps({"arrays": {n: {k: files[n][k] for k in ("sha256", "bijection", "automorphism")}
                                 for n in files}, "controls": ctl, "group": grp, "parse": parse,
                      "verdict": res["verdict"], "secs": res["secs"], "max_rss": LOG[-1][2]}))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""rqls10-maximal EXACT probe v1: quaternary Hadamard-product family. Integer arithmetic only, standard library only.

Family:
  H = I + iC is the Paley quaternary complex Hadamard matrix of order 10. C is the symmetric conference matrix on
  PG(1,9): C[oo][oo] = 0, C[oo][z] = C[z][oo] = 1, C[z][w] = chi(z - w), where chi is the quadratic character of
  GF(9) = GF(3)[x]/(x^2+1).
  Exponent form: H[i][t] = i^{e[i][t]}, with e = 0 on the diagonal, 1 where C = +1, and 3 where C = -1.
  For a permutation pi of the coordinates (GO scope: beta_j(t) = alpha_j(pi(t)) only):
      q_ij(t) = i^{ e[i][t] + e[j][pi(t)] } / sqrt10.
  Rows and columns are orthonormal automatically, and this is re-checked exactly.

Exact tests on exponent vectors mod 4:
  orthogonal(p,p')  iff  h = E_p' - E_p (mod 4) has #0 = #2 and #1 = #3. A sum of +-1, +-i vanishes iff it is
                         balanced.
  parallel(p,p')    iff  h is constant.

Search per pi:
  1. Maximal-cardinality test: no parallel pair among the 100 cells.
  2. Enumerate transversal 10-cliques: sets {(r, sigma(r))} that are pairwise orthogonal, with sigma a
     permutation. Capped by CLIQUE_CAP.
  3. Exact cover: 10 disjoint transversal cliques. Any such set is a Latin square B whose classes are ONBs.
A hit is a candidate only after the frozen exact_rqls_checker_v1.check() passes it in-process (N=4).

NOT exhaustive over the family: pi is sampled. A miss is UNKNOWN.
Self-budget: 290 s. Disk guard: statvfs free >= 12e9 checked every 5 s. Output: one JSON, created exclusively.
"""
import importlib.util
import json
import os
import random
import sys
import time

FROZEN = {
    "version": "quaternary_paley_probe_v1",
    "budget_total_s": 290.0,
    "disk_floor_bytes": 12_000_000_000,
    "disk_check_period_s": 5.0,
    "seed": 20261018045,
    "max_samples": 2000,
    "variants": ["plain"],
    "clique_cap": 200000,
    "per_case_time_cap_s": 3.0,
}
T0 = time.monotonic()
HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
_last = [-1e9]
STOP = {"reason": None}


def free_bytes():
    st = os.statvfs(HERE)
    return st.f_bavail * st.f_frsize


def guard():
    now = time.monotonic()
    if now - T0 > FROZEN["budget_total_s"]:
        STOP["reason"] = STOP["reason"] or "BUDGET"
        return False
    if now - _last[0] >= FROZEN["disk_check_period_s"]:
        _last[0] = now
        fb = free_bytes()
        if fb < FROZEN["disk_floor_bytes"]:
            STOP["reason"] = "DISK_FLOOR free=%d" % fb
            return False
    return STOP["reason"] is None


# ---- GF(9) and the Paley conference matrix ----
def gf9_elems():
    return [(a, b) for a in range(3) for b in range(3)]


def gf9_mul(u, v):
    a, b = u
    c, d = v
    return ((a * c - b * d) % 3, (a * d + b * c) % 3)


def gf9_sub(u, v):
    return ((u[0] - v[0]) % 3, (u[1] - v[1]) % 3)


def paley_C():
    els = gf9_elems()
    nz = [z for z in els if z != (0, 0)]
    squares = {gf9_mul(z, z) for z in nz}
    assert len(squares) == 4

    def chi(z):
        if z == (0, 0):
            return 0
        return 1 if z in squares else -1
    n = 10
    C = [[0] * n for _ in range(n)]
    for k in range(1, n):
        C[0][k] = 1
        C[k][0] = 1
    for k in range(1, n):
        for l in range(1, n):
            C[k][l] = chi(gf9_sub(els[k - 1], els[l - 1]))
    # checks: symmetric, zero diagonal, C C^T = 9 I
    for k in range(n):
        assert C[k][k] == 0
        for l in range(n):
            assert C[k][l] == C[l][k]
            s = sum(C[k][m] * C[l][m] for m in range(n))
            assert s == (9 if k == l else 0), (k, l, s)
    return C


def balanced(h):
    c = [0, 0, 0, 0]
    for x in h:
        c[x] += 1
    return c[0] == c[2] and c[1] == c[3]


def is_const(h):
    return all(x == h[0] for x in h)


def run_case(e, pi, s, deadline):
    n = 10
    cells = [(i, j) for i in range(n) for j in range(n)]
    E = {}
    for (i, j) in cells:
        E[(i, j)] = tuple((e[i][t] + s * e[j][pi[t]]) % 4 for t in range(n))
    out = {"rows_cols_ok": True}
    # rows/cols (should be automatic)
    for i in range(n):
        for j in range(n):
            for j2 in range(j + 1, n):
                h = [(b - a) % 4 for a, b in zip(E[(i, j)], E[(i, j2)])]
                if not balanced(h):
                    out["rows_cols_ok"] = False
            for i2 in range(i + 1, n):
                h = [(b - a) % 4 for a, b in zip(E[(i, j)], E[(i2, j)])]
                if not balanced(h):
                    out["rows_cols_ok"] = False
    # maximal cardinality and transversal adjacency
    par = 0
    adj = {p: 0 for p in cells}  # bitmask over cell index i*10+j
    for a in range(100):
        pa = cells[a]
        Ea = E[pa]
        for b in range(a + 1, 100):
            pb = cells[b]
            h = [(y - x) % 4 for x, y in zip(Ea, E[pb])]
            if is_const(h):
                par += 1
            if pa[0] != pb[0] and pa[1] != pb[1] and balanced(h):
                adj[pa] |= 1 << b
                adj[pb] |= 1 << a
    out["parallel_pairs"] = par
    out["max_card"] = (par == 0)
    # enumerate transversal cliques by rows
    cliques = []
    capped = [False]
    nodes = [0]

    def bt(r, usedcols, mask, chosen):
        if len(cliques) >= FROZEN["clique_cap"]:
            capped[0] = True
            return
        nodes[0] += 1
        if (nodes[0] & 4095) == 0 and time.monotonic() > deadline:
            capped[0] = True
            return
        if r == n:
            cliques.append((mask, tuple(chosen)))
            return
        for j in range(n):
            if usedcols >> j & 1:
                continue
            p = (r, j)
            idx = r * n + j
            ok = True
            for q in chosen:
                if not (adj[q] >> idx & 1):
                    ok = False
                    break
            if ok:
                chosen.append(p)
                bt(r + 1, usedcols | (1 << j), mask | (1 << idx), chosen)
                chosen.pop()
                if capped[0]:
                    return
    bt(0, 0, 0, [])
    out["n_cliques"] = len(cliques)
    out["clique_enum_capped"] = capped[0]
    # exact cover: group cliques by row-0 cell column
    by0 = {j: [] for j in range(n)}
    for mask, ch in cliques:
        by0[ch[0][1]].append((mask, ch))
    out["cliques_by_row0"] = [len(by0[j]) for j in range(n)]
    sol = []
    found = [None]
    cover_capped = [False]

    def xc(j, used):
        if found[0] is not None or cover_capped[0]:
            return
        if time.monotonic() > deadline:
            cover_capped[0] = True
            return
        if j == n:
            found[0] = list(sol)
            return
        for mask, ch in by0[j]:
            if mask & used:
                continue
            sol.append(ch)
            xc(j + 1, used | mask)
            sol.pop()
            if found[0] is not None or cover_capped[0]:
                return
    if all(by0[j] for j in range(n)):
        xc(0, 0)
    out["cover_capped"] = cover_capped[0]
    out["partition_found"] = found[0] is not None
    if found[0] is not None:
        B = [[None] * n for _ in range(n)]
        for sidx, ch in enumerate(found[0]):
            for (r, c) in ch:
                B[r][c] = sidx
        out["B"] = B
        out["E"] = {"%d,%d" % p: list(E[p]) for p in cells}
    return out


def load_checker():
    path = os.path.join(LANE, "exact_rqls_checker_v1.py")
    spec = importlib.util.spec_from_file_location("exact_rqls_checker_v1", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(out_path):
    if os.path.exists(out_path):
        print("REFUSE: output exists")
        return 2
    res = {"frozen": FROZEN, "python": sys.version, "argv": sys.argv, "cases": [], "hits": []}
    res["free_bytes_start"] = free_bytes()
    if res["free_bytes_start"] < FROZEN["disk_floor_bytes"]:
        res["stop_reason"] = "NOT_STARTED_DISK"
    else:
        C = paley_C()
        n = 10
        e = [[0 if i == t else (1 if C[i][t] == 1 else 3) for t in range(n)] for i in range(n)]
        # exact check: H H^* = 10 I (rows pairwise balanced)
        for i in range(n):
            for i2 in range(i + 1, n):
                assert balanced([(b - a) % 4 for a, b in zip(e[i], e[i2])])
        res["paley_ok"] = True
        checker = load_checker()
        rng = random.Random(FROZEN["seed"])
        k = 0
        summary = {"cases": 0, "max_card_cases": 0, "cases_with_cliques": 0, "max_cliques": 0,
                   "capped_enum": 0, "capped_cover": 0, "partitions": 0}
        while guard() and k < FROZEN["max_samples"]:
            k += 1
            pi = list(range(n))
            rng.shuffle(pi)
            for v in FROZEN["variants"]:
                if not guard():
                    break
                s = 1 if v == "plain" else -1
                dl = time.monotonic() + FROZEN["per_case_time_cap_s"]
                r = run_case(e, pi, s, dl)
                summary["cases"] += 1
                summary["max_card_cases"] += int(r["max_card"])
                summary["cases_with_cliques"] += int(r["n_cliques"] > 0)
                summary["max_cliques"] = max(summary["max_cliques"], r["n_cliques"])
                summary["capped_enum"] += int(r["clique_enum_capped"])
                summary["capped_cover"] += int(r["cover_capped"])
                rec = {"k": k, "pi": pi, "variant": v, "max_card": r["max_card"],
                       "parallel_pairs": r["parallel_pairs"], "n_cliques": r["n_cliques"],
                       "enum_capped": r["clique_enum_capped"], "cover_capped": r["cover_capped"],
                       "partition": r["partition_found"], "rows_cols_ok": r["rows_cols_ok"]}
                if (r["n_cliques"] > 0 or k <= 20) and len(res["cases"]) < 1500:
                    res["cases"].append(rec)
                if r["partition_found"]:
                    summary["partitions"] += 1
                    data = {"v": 10, "N": 4, "B": r["B"],
                            "cells": [[{"n": 10, "x": [[[ex, 1]] for ex in r["E"]["%d,%d" % (i, j)]]}
                                       for j in range(n)] for i in range(n)]}
                    rep = checker.check(data)
                    hit = {"k": k, "pi": pi, "variant": v, "checker": {kk: rep[kk] for kk in (
                        "ALL_PASS", "P1_latin", "P2_norms", "P3_lines", "P4_nonparallel", "distinct_rays",
                        "parallel_pairs", "nonorthogonal_line_pairs")}, "instance": data}
                    res["hits"].append(hit)
                    if len(res["hits"]) >= 3:
                        STOP["reason"] = "HITS_LIMIT"
        res["summary"] = summary
        res["samples_drawn"] = k
        res["stop_reason"] = STOP["reason"] or "MAX_SAMPLES"
    res["elapsed_total_s"] = time.monotonic() - T0
    res["free_bytes_end"] = free_bytes()
    with open(out_path, "x") as fh:
        json.dump(res, fh)
    print("WROTE", out_path, "stop", res["stop_reason"], "elapsed", round(res["elapsed_total_s"], 1))
    print("summary", res.get("summary"), "samples", res.get("samples_drawn"), "hits", len(res["hits"]))
    for h in res["hits"]:
        print("HIT", h["k"], h["variant"], h["checker"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

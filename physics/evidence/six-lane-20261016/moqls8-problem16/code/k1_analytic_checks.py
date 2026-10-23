"""Exact GF(8) checks for the analytic K1 lemma (parent lead, review/K1_ANALYTIC_N8.md). Two implementations:
 impl1: set arithmetic with a shift-and-reduce multiplication (x^3 = x + 1);
 impl2: F2-linear algebra: multiplication by r as a 3x3 matrix over F2 (columns r*1, r*x, r*x^2), subspaces as
        row-reduced bases; rV is the image of V under that matrix; intersections via dimension counting
        dim(U ∩ U') = dim U + dim U' - dim(U + U').
Claims, for every 3-subset T of GF(8) (84 sets):
 (a) t0 = t1 + t2 + t3 is not in T;
 (b) V = T + t0 consists of 3 distinct nonzero elements and V ∪ {0} is a 2-dim F2-subspace;
 (c) for distinct nonzero r, r': |rV ∩ r'V| = 1 (impl2: dim(rW ∩ r'W) = 1);
 (d) for every b: the seven allowed sets b + rV (r != 0) avoid b and pairwise meet in exactly one element.
Mutations (must FAIL the pairwise property): (m1) another included direction t in GF(8) \\ (T ∪ {t0}) in place of t0
(for each T there must be such a t with some pair meeting in 0 or 2 elements); (m2) multiplication of Z8 in place of
GF(8) (with + as XOR replaced by + mod 8) — the pairwise property fails for some T.
python -B k1_analytic_checks.py --out ../evidence/k1_analytic/checks.json
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json


def mul(a, b):
    r = 0
    for k in range(3):
        if (b >> k) & 1:
            r ^= a << k
    for d in (4, 3):
        if (r >> d) & 1:
            r ^= 0b1011 << (d - 3)
    return r


def impl1():
    out = {"a": True, "b": True, "c": True, "d": True, "m1_fails_for_every_T": True}
    for T in itertools.combinations(range(8), 3):
        t0 = T[0] ^ T[1] ^ T[2]
        out["a"] &= t0 not in T
        V = {t ^ t0 for t in T}
        W = V | {0}
        out["b"] &= len(V) == 3 and 0 not in V and all((x ^ y) in W for x in W for y in W)
        for r, r2 in itertools.combinations(range(1, 8), 2):
            out["c"] &= len({mul(r, v) for v in V} & {mul(r2, v) for v in V}) == 1
        for b in range(8):
            sets = [{b ^ mul(r, v) for v in V} for r in range(1, 8)]
            out["d"] &= all(b not in S for S in sets) and \
                all(len(S & S2) == 1 for S, S2 in itertools.combinations(sets, 2))
        # m1: another included direction t (not in T, not t0)
        fails = False
        for t in range(8):
            if t in T or t == t0:
                continue
            Vt = {x ^ t for x in T}
            if any(len({mul(r, v) for v in Vt} & {mul(r2, v) for v in Vt}) != 1
                   for r, r2 in itertools.combinations(range(1, 8), 2)):
                fails = True
        out["m1_fails_for_every_T"] &= fails
    # m2: Z8 arithmetic
    m2_fail = False
    for T in itertools.combinations(range(8), 3):
        t0 = sum(T) % 8
        if t0 in T:
            m2_fail = True
            continue
        V = {(t - t0) % 8 for t in T}
        for r, r2 in itertools.combinations([1, 3, 5, 7], 2):
            if len({(r * v) % 8 for v in V} & {(r2 * v) % 8 for v in V}) != 1:
                m2_fail = True
    out["m2_z8_property_fails"] = m2_fail
    return out


# ---------------- impl2: linear algebra over F2
def vec(x):
    return [(x >> k) & 1 for k in range(3)]


def matmul_vec(Mcols, v):
    out = [0, 0, 0]
    for k in range(3):
        if v[k]:
            out = [o ^ c for o, c in zip(out, Mcols[k])]
    return out


def rank(rows):
    rows = [list(r) for r in rows]
    rk = 0
    for col in range(3):
        piv = next((i for i in range(rk, len(rows)) if rows[i][col]), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        for i in range(len(rows)):
            if i != rk and rows[i][col]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[rk])]
        rk += 1
    return rk


def impl2():
    # multiplication matrices from the field relation x^3 = x + 1 (basis 1, x, x^2): columns are images of basis
    def mat(r):
        cols = []
        e = [1, 0, 0]
        cur = vec(r)            # r * 1
        cols.append(cur)
        for _ in range(2):      # multiply previous image by x: shift up, reduce x^3 = x + 1
            c0, c1, c2 = cur
            cur = [c2, c0 ^ c2, c1]
            cols.append(cur)
        return cols
    ok_b = ok_c = True
    for T in itertools.combinations(range(8), 3):
        t0 = T[0] ^ T[1] ^ T[2]
        V = [t ^ t0 for t in T]
        Wb = [vec(v) for v in V]
        ok_b &= rank(Wb) == 2 and all(v != 0 for v in V)
        for r, r2 in itertools.combinations(range(1, 8), 2):
            A = [matmul_vec(mat(r), w) for w in Wb]
            B = [matmul_vec(mat(r2), w) for w in Wb]
            dA, dB, dS = rank(A), rank(B), rank(A + B)
            ok_c &= (dA == 2 and dB == 2 and dA + dB - dS == 1)
    # sanity: matrix multiplication agrees with impl1's mul
    agree = all(matmul_vec(mat(r), vec(x)) == vec(mul(r, x)) for r in range(8) for x in range(8))
    return {"b_rank2": ok_b, "c_dim_intersection_1": ok_c, "matrix_agrees_with_impl1": agree}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(), "impl1": impl1(),
           "impl2": impl2()}
    res["all_ok"] = all(res["impl1"][k] for k in ("a", "b", "c", "d", "m1_fails_for_every_T", "m2_z8_property_fails")) \
        and all(res["impl2"].values())
    with open(a.out, "x") as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res))
    if not res["all_ok"]:
        raise SystemExit("K1 ANALYTIC CHECK FAILED")


if __name__ == "__main__":
    main()

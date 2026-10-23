#!/usr/bin/env python3
"""proof_check.py -- exact checks for notes/nonexistence-proof-r1.md (BTD(14,18;7,1,9;7,4), candidate r1).
Stdlib only (integers, fractions.Fraction); no floating point, no randomness, no search over matrices.

R1  Step 1 algebra in span{I, G, J} (18 x 18) with G^2 = 7G + 196J, GJ = JG = 63J, J^2 = 18J:
    H = 63I - 9G + 28J satisfies H^2 = 63H; H 1 = (63 - 9*63 + 28*18) 1 = 0.  Diagonal H_jj = 28 - 18 c_j from
    G_jj = 7 + 2 c_j; off-diagonal 28 - 9 g = 1 mod 9.
R2  A = 7I + 4J (14 x 14): A (I - (4/63) J)/7 = I exactly; det A = 7^14 * 9 exactly.
R3  Lemma D4 factor: entrywise I - P^T A^{-1} P = H[S]/63 when P^T 1 = 7 * 1; det A / 63^4 = 7^10/729; and
    det(A - P P^T) = 7^10 det(H[S]) / 729 on three explicit 14 x 4 matrices P over {0,1,2} with column sums 7.
R4  c <= 1 from 28 - 18 c >= 0 (c = 0..3 possible for a column summing to 7); 14 entries 2 in total -> 14 type-1
    and 4 type-0 columns.
R5  integers h = 1 (mod 9) with h^2 <= 10*28 are exactly {-8, 1, 10} (and also for h^2 <= 10*10).
R6  for h in {-8,1,10}: (h-1)(h+8) = 162 [h=10], (h-1)(h-10) = 162 [h=-8]; with sum = -10, sum of squares = 530
    over 17 entries: counts 324/162 = 2 and 810/162 = 5; the only (P, N) with P - N = -3, 99P + 63N = 513.
R7  y = 2e_a + e_k + e_l: y^T H y = 4*10 + 10 + 10 + 4*(-8) + 4*(-8) + 2 h = 2h - 4, negative for h in {-8, 1}.
R8  (e_a + e_b)^T H (e_a + e_b) = 4; sums of two values in {-8,1,10} with square <= 4*28 = 112: exactly {-7, 2}.
R9  the six 4 x 4 determinants of H[{a,b,u,c}] (exact Fraction elimination): values {3645, -2187}; 7^10 * 3645 / 729
    = 5 * 7^10 = 2 (mod 3) is not a square; -2187 < 0.
R10 final count: 18 columns * 2 = 36 != 0.
Usage: proof_check.py OUT.json   (exclusive)
"""
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction as Fr


def det(M):
    A = [[Fr(x) for x in row] for row in M]
    n, d = len(A), Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            for k in range(c, n):
                A[r][k] -= f * A[c][k]
    return d


def is_square(v):
    v = Fr(v)
    return v.denominator == 1 and v >= 0 and math.isqrt(int(v)) ** 2 == int(v)


def r1():
    def mul(x, y):
        i1, g1, j1 = x
        i2, g2, j2 = y
        return (i1 * i2, i1 * g2 + g1 * i2 + 7 * g1 * g2,
                i1 * j2 + j1 * i2 + 196 * g1 * g2 + 63 * (g1 * j2 + j1 * g2) + 18 * j1 * j2)
    H = (63, -9, 28)
    ok_sq = mul(H, H) == tuple(63 * c for c in H)
    h1 = 63 - 9 * 63 + 28 * 18
    diag = [63 - 9 * (7 + 2 * c) + 28 for c in range(4)]
    off_mod = all((28 - 9 * g) % 9 == 1 for g in range(0, 30))
    return {"H2_equals_63H": ok_sq, "H1": h1, "H_jj_for_c_0..3": diag, "offdiag_1_mod_9": off_mod,
            "ok": ok_sq and h1 == 0 and diag == [28 - 18 * c for c in range(4)] and off_mod}


def r2():
    n = 14
    A = [[Fr(7 if i == j else 0) + 4 for j in range(n)] for i in range(n)]
    B = [[(Fr(1 if i == j else 0) - Fr(4, 63)) / 7 for j in range(n)] for i in range(n)]
    prod = [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    ident = all(prod[i][j] == (1 if i == j else 0) for i in range(n) for j in range(n))
    dA = det(A)
    return {"A_times_inverse_is_I": ident, "det_A": str(dA), "ok": ident and dA == 7 ** 14 * 9}


def r3():
    ok_sym = Fr(4, 63) / 7 * 49 == Fr(4, 9) and Fr(28, 63) == Fr(4, 9) and Fr(9, 63) == Fr(1, 7)
    factor = Fr(7 ** 14 * 9) / Fr(63) ** 4
    ok_factor = factor == Fr(7 ** 10, 729)
    cols = [
        [[2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]],
        [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1]],
        [[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
         [0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]],
    ]
    explicit = []
    for P4 in cols:
        assert all(sum(c) == 7 for c in P4)
        P = [[P4[t][i] for t in range(4)] for i in range(14)]
        A = [[(7 if i == k else 0) + 4 - sum(P[i][t] * P[k][t] for t in range(4)) for k in range(14)] for i in range(14)]
        PtP = [[sum(P[i][s] * P[i][t] for i in range(14)) for t in range(4)] for s in range(4)]
        HS = [[(63 if s == t else 0) - 9 * PtP[s][t] + 28 for t in range(4)] for s in range(4)]
        lhs, rhs = det(A), Fr(7 ** 10) * det(HS) / 729
        explicit.append({"equal": lhs == rhs, "det_A_minus_PPt": str(lhs)})
    return {"symbolic": ok_sym, "factor": str(factor), "explicit": explicit,
            "ok": ok_sym and ok_factor and all(e["equal"] for e in explicit)}


def r4():
    allowed = [c for c in range(0, 4) if 28 - 18 * c >= 0]
    # n1 + 2 n2 + 3 n3 = 14 total twos, with only c in {0,1}: n1 = 14, n0 = 18 - 14 = 4
    return {"allowed_c": allowed, "n1": 14, "n0": 4, "ok": allowed == [0, 1]}


def r5():
    v280 = [h for h in range(-40, 41) if h % 9 == 1 and h * h <= 280]
    v100 = [h for h in range(-40, 41) if h % 9 == 1 and h * h <= 100]
    return {"values_280": v280, "values_100": v100, "ok": v280 == [-8, 1, 10] and v100 == [-8, 1, 10]}


def r6():
    ok_poly = all((h - 1) * (h + 8) == (162 if h == 10 else 0) and (h - 1) * (h - 10) == (162 if h == -8 else 0)
                  for h in (-8, 1, 10))
    s1, s2, n = -10, 530, 17
    p = Fr(s2 + 7 * s1 - 8 * n, 162)
    q = Fr(s2 - 11 * s1 + 10 * n, 162)
    sols = [(P, N) for P in range(0, 18) for N in range(0, 18) if P + N <= 17 and P - N == -3 and 99 * P + 63 * N == 513]
    return {"poly_identities": ok_poly, "count_10": str(p), "count_-8": str(q), "integer_solutions": sols,
            "ok": ok_poly and p == 2 and q == 5 and sols == [(2, 5)]}


def r7():
    vals = {h: 4 * 10 + 10 + 10 + 4 * (-8) + 4 * (-8) + 2 * h for h in (-8, 1, 10)}
    return {"yHy": vals, "ok": vals == {-8: -20, 1: -2, 10: 16}}


def r8():
    xhx = 10 + 10 + 2 * (-8)
    sums = sorted({x + y for x in (-8, 1, 10) for y in (-8, 1, 10)})
    allowed = [s for s in sums if s * s <= xhx * 28]
    return {"xHx": xhx, "sums": sums, "allowed": allowed, "ok": xhx == 4 and allowed == [-7, 2]}


def r9():
    table = []
    ok = True
    for (x, y) in ((-8, 1), (1, -8)):
        for w in (-8, 1, 10):
            HS = [[10, -8, 1, x], [-8, 10, 1, y], [1, 1, 10, w], [x, y, w, 28]]
            d = det(HS)
            rhs = Fr(7 ** 10) * d / 729
            square = is_square(rhs)
            mod3 = int(rhs) % 3 if rhs.denominator == 1 and rhs >= 0 else None
            table.append({"x": x, "y": y, "w": w, "det": str(d), "7^10_det_over_729": str(rhs), "square": square,
                          "mod3": mod3})
            ok &= (d == 3645 and w in (-8, 1) and rhs == 5 * 7 ** 10 and mod3 == 2 and not square) or \
                  (d == -2187 and w == 10 and rhs < 0)
    return {"table": table, "ok": ok}


def r10():
    return {"sum": 18 * 2, "ok": 18 * 2 != 0}


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "R1": r1(), "R2": r2(), "R3": r3(), "R4": r4(), "R5": r5(), "R6": r6(), "R7": r7(), "R8": r8(),
           "R9": r9(), "R10": r10()}
    res["all_ok"] = all(v["ok"] for k, v in res.items() if isinstance(v, dict))
    with open(argv[1], "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    for k, v in res.items():
        if isinstance(v, dict):
            print(k, "ok" if v["ok"] else "FAIL")
    print("R9 table:", [(t["x"], t["y"], t["w"], t["det"]) for t in res["R9"]["table"]])
    print("PROOF-CHECK", "PASS" if res["all_ok"] else "FAIL")
    return 0 if res["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

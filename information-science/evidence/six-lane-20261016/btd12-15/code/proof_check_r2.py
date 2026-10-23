#!/usr/bin/env python3
"""proof_check_r2.py -- exact checks for notes/nonexistence-proof-r2.md (BTD(12,15;6,2,10;8,6), candidate r2).
Stdlib only: integers and fractions.Fraction; no floating point, no random sampling, no parameter grid.
Independent of code/proof_check.py (r1 checker, frozen and unchanged).

R1  Step 1 algebra in span{I, G, J} with G^2 = 8G + 384J, GJ = JG = 80J, J^2 = 15J:
    H = 40I - 5G + 24J satisfies H^2 = 40H; H1 = (40 - 5*80 + 24*15) 1 = 0; trace H = 15*24 - 10*24 = 120.
R2  Step 6 ingredients for A = 8I + 6J (12 x 12): A (I - (3/40) J) / 8 = I exactly; det A = 2^37 * 5 exactly.
R3  Step 6 factor: I - P^T A^{-1} P = H[S]/40 whenever P^T 1 = 8 * 1, checked entrywise as an exact identity in the
    entries of P^T P (the J-term is (3/40)/8 * 64 = 3/5); hence det(N)^2 = det A * det(H[S]/40) = 2^28 det H[S] / 25.
    Also evaluated exactly on three explicit 12 x 3 matrices P over {0,1,2} with column sums 8.
R4  Step 2-3: H_jj = 24 - 10 c >= 0 forces c <= 2 (c = 0..4 possible for a column summing to 8); splits n2 = 9..12.
R5  Step 4: integer multisets (|t| <= 2 since t^2 <= 6) with sum 2 and sum of squares 6: exactly {1,1,1,1,-1,-1} and
    {2,1,-1}; at most four entries equal 1.
R6  Step 5: integers h = -1 (mod 5) with h^2 <= 4*4: exactly {-1, 4}.
R7  Step 7: det(5I - J) (3 x 3) = 50, not a perfect square.
R8  Step 8 (r2 closure): x, y range over integers = -1 (mod 5) with x^2 <= 4*14 = 56, i.e. {-6, -1, 4};
    det [[4,-1,x],[-1,4,y],[x,y,14]] computed by exact cofactor expansion equals 210 - (4x^2 + 2xy + 4y^2) and lies in
    {-150, 50, 150, 200}; none is a nonnegative perfect square.
Usage: proof_check_r2.py OUT.json   (exclusive)
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


def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]


def is_nonneg_square(v):
    v = Fr(v)
    return v.denominator == 1 and v >= 0 and math.isqrt(int(v)) ** 2 == int(v)


def det3_cofactor(M):
    (a, b, c), (d, e, f), (g, h, i) = M
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def r1():
    def mul(x, y):
        i1, g1, j1 = x
        i2, g2, j2 = y
        return (i1 * i2,
                i1 * g2 + g1 * i2 + 8 * g1 * g2,
                i1 * j2 + j1 * i2 + 384 * g1 * g2 + 80 * (g1 * j2 + j1 * g2) + 15 * j1 * j2)
    H = (40, -5, 24)
    ok = mul(H, H) == (1600, -200, 960) == tuple(40 * c for c in H)
    h1 = 40 - 5 * 80 + 24 * 15
    tr = 15 * 24 - 10 * 24
    return {"H2_equals_40H": ok, "H1_coefficient": h1, "trace_H": tr, "ok": ok and h1 == 0 and tr == 120}


def r2():
    n = 12
    A = [[Fr(8 if i == j else 0) + 6 for j in range(n)] for i in range(n)]
    Ainv = [[(Fr(1 if i == j else 0) - Fr(3, 40)) / 8 for j in range(n)] for i in range(n)]
    prod = matmul(A, Ainv)
    ident = all(prod[i][j] == (1 if i == j else 0) for i in range(n) for j in range(n))
    dA = det(A)
    return {"A_times_claimed_inverse_is_I": ident, "det_A": str(dA), "det_A_equals_2^37*5": dA == 2 ** 37 * 5,
            "ok": ident and dA == 2 ** 37 * 5}


def r3():
    # entrywise identity: (I - P^T A^{-1} P)_ab = d_ab - (P^T P)_ab / 8 + (3/40)/8 * (P^T 1)_a (P^T 1)_b
    #                                         = d_ab - (P^T P)_ab / 8 + 3/5      when P^T 1 = 8 * 1
    #                     H[S]_ab / 40 = (40 d_ab - 5 (P^T P)_ab + 24) / 40 = d_ab - (P^T P)_ab / 8 + 3/5
    j_term = Fr(3, 40) / 8 * 8 * 8
    ok_sym = j_term == Fr(3, 5) and Fr(24, 40) == Fr(3, 5) and Fr(5, 40) == Fr(1, 8)
    factor = Fr(2 ** 37 * 5) / Fr(40) ** 3
    ok_factor = factor == Fr(2 ** 28, 25)
    cols = [
        [[2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 2, 2, 2, 1, 1, 0, 0, 0]],
        [[0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1], [2, 0, 2, 0, 2, 0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 2, 2, 1, 1]],
        [[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 2, 2, 0, 0, 1, 1, 1, 1], [2, 0, 0, 2, 0, 0, 1, 1, 0, 1, 0, 1]],
    ]
    explicit = []
    for P3 in cols:
        assert all(sum(c) == 8 for c in P3)
        P = [[P3[c][i] for c in range(3)] for i in range(12)]
        A = [[(8 if i == k else 0) + 6 - sum(P[i][c] * P[k][c] for c in range(3)) for k in range(12)] for i in range(12)]
        PtP = [[sum(P[i][a] * P[i][b] for i in range(12)) for b in range(3)] for a in range(3)]
        HS = [[(40 if a == b else 0) - 5 * PtP[a][b] + 24 for b in range(3)] for a in range(3)]
        lhs, rhs = det(A), Fr(2 ** 28) * det(HS) / 25
        explicit.append({"P_columns": P3, "det_A_minus_PPt": str(lhs), "2^28_detHS_over_25": str(rhs), "equal": lhs == rhs})
    ok = ok_sym and ok_factor and all(e["equal"] for e in explicit)
    return {"symbolic_entry_identity": ok_sym, "factor_detA_over_40^3": str(factor), "factor_is_2^28/25": ok_factor,
            "explicit_instances": explicit, "ok": ok}


def r4():
    allowed_c = [c for c in range(0, 5) if 24 - 10 * c >= 0]
    splits = []
    for n2 in range(0, 16):
        n1 = 24 - 2 * n2
        n0 = 15 - n1 - n2
        if 0 <= n1 <= 15 and n0 >= 0:
            splits.append((n0, n1, n2))
    return {"allowed_c": allowed_c, "splits_(n0,n1,n2)": splits,
            "ok": allowed_c == [0, 1, 2] and splits == [(0, 6, 9), (1, 4, 10), (2, 2, 11), (3, 0, 12)]}


def r5():
    sols = set()
    for size in range(0, 7):
        for ms in itertools.combinations_with_replacement((-2, -1, 1, 2), size):
            if sum(ms) == 2 and sum(t * t for t in ms) == 6:
                sols.add(tuple(sorted(ms)))
    max_ones = max(ms.count(1) for ms in sols)
    return {"multisets": sorted(sols), "max_entries_equal_1": max_ones,
            "ok": sols == {(-1, -1, 1, 1, 1, 1), (-1, 1, 2)} and max_ones == 4}


def r6():
    vals = [h for h in range(-10, 11) if h % 5 == 4 and h * h <= 16]
    return {"type2_pair_values": vals, "ok": vals == [-1, 4]}


def r7():
    d = det3_cofactor([[4, -1, -1], [-1, 4, -1], [-1, -1, 4]])
    return {"det_5I_minus_J": d, "nonneg_square": is_nonneg_square(d), "ok": d == 50 and not is_nonneg_square(d)}


def r8():
    xs = [h for h in range(-20, 21) if h % 5 == 4 and h * h <= 56]
    table = []
    ok = xs == [-6, -1, 4]
    for x in xs:
        for y in xs:
            d = det3_cofactor([[4, -1, x], [-1, 4, y], [x, y, 14]])
            closed = 210 - (4 * x * x + 2 * x * y + 4 * y * y)
            sq = is_nonneg_square(d)
            table.append({"x=H_ka": x, "y=H_kb": y, "det": d, "closed_form": closed, "nonneg_square": sq})
            ok &= d == closed and not sq
    values = sorted({row["det"] for row in table})
    ok &= values == [-150, 50, 150, 200]
    return {"x_values": xs, "table": table, "det_values": values, "ok": ok}


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    res = {"script_sha256": hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
           "R1_step1_algebra": r1(), "R2_matrix_A": r2(), "R3_lemma_D_factor": r3(), "R4_column_types": r4(),
           "R5_step4_multisets": r5(), "R6_step5_type2_pairs": r6(), "R7_step7_det": r7(),
           "R8_step8_closure_table": r8()}
    res["all_ok"] = all(v["ok"] for k, v in res.items() if isinstance(v, dict))
    with open(argv[1], "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    for k, v in res.items():
        if isinstance(v, dict):
            print(k, "ok" if v["ok"] else "FAIL")
    print("Step 8 table (x, y, det):", [(r["x=H_ka"], r["y=H_kb"], r["det"]) for r in res["R8_step8_closure_table"]["table"]])
    print("PROOF-CHECK-R2", "PASS" if res["all_ok"] else "FAIL")
    return 0 if res["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

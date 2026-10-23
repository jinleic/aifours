#!/usr/bin/env python3
"""proof_check.py -- exact-arithmetic mechanical checks of the candidate nonexistence proof for BTD(12,15;6,2,10;8,6)
(notes/nonexistence-proof.md).  Stdlib only (fractions, itertools, random with fixed seeds).  It re-derives the
finite case analysis by exhaustive enumeration from the lemmas, instead of replaying the hand argument.

Checks:
  C1  algebra: in the commutative algebra spanned by I, G, J with G^2 = 8G + 384J, GJ = JG = 80J, J^2 = 15J,
      H = 40I - 5G + 24J satisfies H^2 = 40H, and H applied to the all-ones vector is 0 (G1 = 80*1, J1 = 15*1).
  C2  Lemma D identity: det(8I + 6J - P P^T) = 2^28 det(40I - 5P^T P + 24J) / 25 for random integer 12x3 matrices P
      with column sums 8 (exact rational determinants), 40 instances.
  C3  det(5I - J) (3x3) = 50 is not a perfect square; the 3x3 type-2 patterns with off-diagonal entries in {4,-1}.
  C4  integer solutions t (multisets) of sum t = 2, sum t^2 = 6: exactly {1,1,1,1,-1,-1} and {2,1,-1}.
  C5  exhaustive enumeration for every (n2, class sizes): n2 in 9..12, one or two classes (three are excluded by C3),
      each non-type-2 column k with p_k = (H_ka, H_kb) over the Cauchy-Schwarz-allowed values (type-1: |p| <= sqrt(56),
      type-0: |p| <= sqrt(96), p = -1 mod 5), subject to the H^2 = 40H and H1 = 0 relations at the class
      representatives a, b (sum_k H_ka = 0, sum_k H_ka^2 = 160, sum_k H_kb = 0, sum_k H_kb^2 = 160,
      sum_k H_ka H_kb = -40), the PSD Schur condition Y_kk = H_kk - F_kk >= 0, and the rank-1 sign condition:
      some y with y_k^2 = Y_kk, sum_k y_k = 0, and F_kl + y_k y_l an integer = -1 (mod 5) for all k != l.
      Expected: no configuration survives.
Usage: proof_check.py OUT.json   (exclusive)
"""
import itertools
import json
import math
import random
import sys
from fractions import Fraction as Fr


def det(M):
    M = [[Fr(x) for x in row] for row in M]
    n = len(M)
    d = Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            if f:
                for k in range(c, n):
                    M[r][k] -= f * M[c][k]
    return d


def is_square_int(x):
    if x < 0 or Fr(x).denominator != 1:
        return False
    x = int(x)
    r = math.isqrt(x)
    return r * r == x


def c1_algebra():
    # elements as (i, g, j) meaning i*I + g*G + j*J
    def mul(x, y):
        i1, g1, j1 = x
        i2, g2, j2 = y
        i = i1 * i2
        g = i1 * g2 + g1 * i2 + g1 * g2 * 8
        j = i1 * j2 + j1 * i2 + g1 * g2 * 384 + (g1 * j2 + j1 * g2) * 80 + j1 * j2 * 15
        return (i, g, j)
    H = (Fr(40), Fr(-5), Fr(24))
    H2 = mul(H, H)
    ok1 = H2 == tuple(40 * c for c in H)
    ones = 40 + (-5) * 80 + 24 * 15
    Q = (Fr(1), Fr(-1, 8), Fr(3, 5))
    ok2 = mul(Q, Q) == Q
    return {"H2_equals_40H": ok1, "H_times_ones_coefficient": ones, "Q_idempotent": ok2,
            "ok": ok1 and ones == 0 and ok2}


def c2_lemma_d():
    rng = random.Random(20261017)
    results = []
    for inst in range(40):
        P = [[0] * 3 for _ in range(12)]
        for c in range(3):
            # random nonnegative integer column with sum 8 (entries may exceed 2: the identity is purely algebraic)
            for _ in range(8):
                P[rng.randrange(12)][c] += 1
            if inst % 2:
                # also allow negative entries while keeping the column sum 8
                i, k = rng.randrange(12), rng.randrange(12)
                P[i][c] += 3
                P[k][c] -= 3
        A = [[(8 if i == k else 0) + 6 - sum(P[i][c] * P[k][c] for c in range(3)) for k in range(12)] for i in range(12)]
        PtP = [[sum(P[i][a] * P[i][b] for i in range(12)) for b in range(3)] for a in range(3)]
        HS = [[(40 if a == b else 0) - 5 * PtP[a][b] + 24 for b in range(3)] for a in range(3)]
        lhs = det(A)
        rhs = Fr(2) ** 28 * det(HS) / 25
        results.append(lhs == rhs)
    return {"instances": len(results), "all_equal": all(results), "ok": all(results)}


def c3_patterns():
    out = []
    ok = True
    for off in itertools.product((4, -1), repeat=3):
        h12, h13, h23 = off
        HS = [[4, h12, h13], [h12, 4, h23], [h13, h23, 4]]
        d = det(HS)
        psd = all(det([[HS[i][j] for j in S] for i in S]) >= 0
                  for r in (1, 2, 3) for S in itertools.combinations(range(3), r))
        allowed = psd and is_square_int(d)
        out.append({"offdiag": off, "det": str(d), "psd": psd, "det_square": is_square_int(d), "allowed": allowed})
        # allowed patterns must be exactly those where "H=4" is transitive and not all three are -1
        n4 = off.count(4)
        if allowed != (n4 in (1, 3)):
            ok = False
    d50 = det([[4, -1, -1], [-1, 4, -1], [-1, -1, 4]])
    ok &= d50 == 50 and not is_square_int(d50)
    return {"patterns": out, "det_5I_minus_J": str(d50), "ok": ok}


def c4_t_multisets():
    sols = set()
    for n in range(0, 7):
        for combo in itertools.combinations_with_replacement((-2, -1, 1, 2), n):
            if sum(combo) == 2 and sum(x * x for x in combo) == 6:
                sols.add(tuple(sorted(combo)))
    want = {(-1, -1, 1, 1, 1, 1), (-1, 1, 2)}
    return {"solutions": sorted(sols), "ok": sols == want}


def allowed_p(hkk):
    # p = H_ka with p^2 <= 4 * hkk and p = -1 mod 5 (H_aa = 4)
    return [p for p in range(-40, 41) if p % 5 == 4 and p * p <= 4 * hkk]


GINV = [[Fr(4, 15), Fr(1, 15)], [Fr(1, 15), Fr(4, 15)]]


def F(p, q):
    return p[0] * (GINV[0][0] * q[0] + GINV[0][1] * q[1]) + p[1] * (GINV[1][0] * q[0] + GINV[1][1] * q[1])


def sqrt_parts(y):
    """y = Fraction >= 0 -> (r, d) with sqrt(y) = r * sqrt(d), r Fraction, d squarefree int (d = 0 if y = 0)"""
    if y == 0:
        return Fr(0), 0
    n, m = y.numerator * y.denominator, y.denominator
    d, r = 1, 1
    x = n
    f = 2
    while f * f <= x:
        while x % (f * f) == 0:
            x //= f * f
            r *= f
        f += 1
    d = x
    return Fr(r, m), d


def rank1_feasible(cols):
    """cols: list of (hkk, p) for non-type-2 columns. Search signs s_k for y_k = s_k sqrt(Y_kk)."""
    Y = [hkk - F(p, p) for hkk, p in cols]
    parts = [sqrt_parts(y) for y in Y]
    nz = [k for k in range(len(cols)) if Y[k] != 0]
    for signs in itertools.product((1, -1), repeat=len(nz)):
        s = dict(zip(nz, signs))
        # sum y = 0, grouped by squarefree part
        tot = {}
        for k in nz:
            r, d = parts[k]
            tot[d] = tot.get(d, 0) + s[k] * r
        if any(v != 0 for v in tot.values()):
            continue
        good = True
        for k, l in itertools.combinations(range(len(cols)), 2):
            fkl = F(cols[k][1], cols[l][1])
            if Y[k] == 0 or Y[l] == 0:
                ykl = Fr(0)
            else:
                (rk, dk), (rl, dl) = parts[k], parts[l]
                if dk != dl:
                    good = False
                    break
                ykl = s[k] * s[l] * rk * rl * dk
            h = fkl + ykl
            if h.denominator != 1 or h.numerator % 5 != 4:
                good = False
                break
        if good:
            return True
    return False


def pairwise_feasible(cols):
    """finitary model (no rank-one factorisation): Y_kl = +-sqrt(Y_kk Y_ll) chosen independently per pair such that
    H_kl = F_kl + Y_kl is an integer = -1 mod 5, and every row of Y sums to 0 (Y 1 = 0)."""
    n = len(cols)
    Y = [hkk - F(p, p) for hkk, p in cols]
    options = {}
    for k, l in itertools.combinations(range(n), 2):
        prod = Y[k] * Y[l]
        fkl = F(cols[k][1], cols[l][1])
        opts = []
        if prod == 0:
            cand = [Fr(0)]
        else:
            num, den = prod.numerator, prod.denominator
            rn, rd = math.isqrt(num), math.isqrt(den)
            cand = [Fr(rn, rd), Fr(-rn, rd)] if rn * rn == num and rd * rd == den else []
        for y in cand:
            h = fkl + y
            if h.denominator == 1 and h.numerator % 5 == 4:
                opts.append(y)
        if not opts:
            return False
        options[(k, l)] = sorted(set(opts))
    keys = list(options)
    for choice in itertools.product(*(options[key] for key in keys)):
        Ym = {key: v for key, v in zip(keys, choice)}
        ok = True
        for k in range(n):
            s = Y[k] + sum(Ym[(min(k, l), max(k, l))] for l in range(n) if l != k)
            if s != 0:
                ok = False
                break
        if ok:
            return True
    return False


def c5_enumeration():
    report = []
    survivors_rank1, survivors_pairwise = 0, 0
    for n2 in (9, 10, 11, 12):
        n0 = n2 - 9
        n1 = 24 - 2 * n2
        kinds = [14] * n1 + [24] * n0
        for alpha in range(1, n2 + 1):
            beta = n2 - alpha
            if beta > alpha:
                continue  # symmetric under swapping the class names
            if beta == 0:
                # one class: row conditions at a: sum_k H_ka = 0 and sum_k H_ka^2 = 160
                opts = [allowed_p(h) for h in kinds]
                cnt = 0
                for ps in itertools.product(*opts):
                    if 4 * alpha + sum(ps) == 0 and 16 * alpha + sum(p * p for p in ps) == 160:
                        cnt += 1
                report.append({"n2": n2, "classes": [alpha], "row_condition_solutions": cnt})
                survivors_rank1 += cnt
                survivors_pairwise += cnt
                continue
            opts = []
            for h in kinds:
                al = allowed_p(h)
                opts.append([(pa, pb) for pa in al for pb in al])
            cnt_rows, cnt_psd, cnt_sum, cnt_rank1, cnt_pair = 0, 0, 0, 0, 0
            for ps in itertools.product(*opts):
                # row relations of H at a (class A, H_aa = 4) and b (class B, H_bb = 4); type-2 columns contribute
                # H_ka = 4 (class A, alpha of them incl. a), -1 (class B), and symmetrically for b
                if 4 * alpha - beta + sum(p[0] for p in ps) != 0:
                    continue
                if 4 * beta - alpha + sum(p[1] for p in ps) != 0:
                    continue
                if 16 * alpha + beta + sum(p[0] * p[0] for p in ps) != 160:
                    continue
                if 16 * beta + alpha + sum(p[1] * p[1] for p in ps) != 160:
                    continue
                if -4 * alpha - 4 * beta + sum(p[0] * p[1] for p in ps) != -40:
                    continue
                cnt_rows += 1
                cols = list(zip(kinds, ps))
                if any(h - F(p, p) < 0 for h, p in cols):
                    continue
                cnt_psd += 1
                # identity check: sum of Y_kk over non-type-2 columns must be 40 (follows from the row relations)
                if sum(h - F(p, p) for h, p in cols) == 40:
                    cnt_sum += 1
                if rank1_feasible(cols):
                    cnt_rank1 += 1
                if pairwise_feasible(cols):
                    cnt_pair += 1
            report.append({"n2": n2, "classes": [alpha, beta], "non_type2_columns": len(kinds),
                           "row_condition_solutions": cnt_rows, "psd_solutions": cnt_psd,
                           "psd_with_sumY_40": cnt_sum, "rank1_integral_solutions": cnt_rank1,
                           "pairwise_finitary_solutions": cnt_pair})
            survivors_rank1 += cnt_rank1
            survivors_pairwise += cnt_pair
    return {"cases": report, "survivors_rank1_model": survivors_rank1,
            "survivors_pairwise_model": survivors_pairwise,
            "ok": survivors_rank1 == 0 and survivors_pairwise == 0}


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    res = {"C1_algebra": c1_algebra(), "C2_lemma_D_identity": c2_lemma_d(), "C3_type2_triples": c3_patterns(),
           "C4_t_multisets": c4_t_multisets(), "C5_enumeration": c5_enumeration()}
    res["all_ok"] = all(v["ok"] for v in res.values() if isinstance(v, dict))
    with open(argv[1], "x") as f:
        json.dump(res, f, indent=1, default=str)
        f.write("\n")
    for k, v in res.items():
        if isinstance(v, dict):
            print(k, "ok" if v["ok"] else "FAIL")
    print("C5 cases:")
    for c in res["C5_enumeration"]["cases"]:
        print(" ", c)
    print("PROOF-CHECK", "PASS" if res["all_ok"] else "FAIL")
    return 0 if res["all_ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

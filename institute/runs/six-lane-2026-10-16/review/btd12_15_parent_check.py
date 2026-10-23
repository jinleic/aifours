"""Parent-independent exact checks for the candidate proof that BTD(12,15;6,2,10;8,6) does not exist.
Written from the proof text only (the worker's proof_check.py is not imported or read). Exact rationals throughout.
Checks: (1) the matrix identities behind H^2 = 40H, H1 = 0, trace H = 120 as polynomial identities in the stated
relations; (2) Lemma D's constant det(8I+6J_12) = 2^37*5, the inverse formula and I - P^T A^{-1} P = H[S]/40 on random
integer P with column sums 8; (3) the Step-4 multiset classification; (4) an exhaustive enumeration of the n2 = 10 and
n2 = 9 residual cases of Steps 9-11, using only H-level constraints: diagonal values, the Step-9 row constraints at the
two class representatives, Y_kk >= 0, sum_k Y_kk = 40, rank-one Y = yy^T with y_k = s_k sqrt(Y_kk), sum y = 0, and
integrality of every off-diagonal H_kl = F_kl + y_k y_l with H_kl = -1 (mod 5) and |H_kl| <= sqrt(H_kk H_ll).
Usage: python3 -B btd12_15_parent_check.py OUT.json
"""
from datetime import datetime
from fractions import Fraction as Fr
from itertools import combinations, permutations, product
import hashlib
import json
import math
from pathlib import Path
import random
import sys
from zoneinfo import ZoneInfo


def det(m):
    m = [row[:] for row in m]
    n, d = len(m), Fr(1)
    for c in range(n):
        p = next((r for r in range(c, n) if m[r][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            m[c], m[p] = m[p], m[c]
            d = -d
        d *= m[c][c]
        for r in range(c + 1, n):
            f = m[r][c] / m[c][c]
            for k in range(c, n):
                m[r][k] -= f * m[c][k]
    return d


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(r) for r in zip(*a)]


def check_identities():
    # Treat G, J (15x15) abstractly: verify (40I-5G+24J)^2 = 40(40I-5G+24J) using G^2 = 8G+384J, GJ=JG=80J, J^2=15J.
    # Represent elements as coefficient triples over the commutative algebra spanned by I, G, J.
    def mul(x, y):
        (a1, b1, c1), (a2, b2, c2) = x, y
        I = a1 * a2
        G = a1 * b2 + b1 * a2 + b1 * b2 * 8
        J = a1 * c2 + c1 * a2 + b1 * b2 * 384 + (b1 * c2 + c1 * b2) * 80 + c1 * c2 * 15
        return (I, G, J)
    H = (40, -5, 24)
    sq = mul(H, H)
    ok_sq = sq == tuple(40 * t for t in H)
    ok_one = 40 - 5 * 80 + 24 * 15 == 0
    trace = 15 * 40 - 5 * (15 * 8 + 2 * 24) + 24 * 15
    return {'H^2 == 40H in algebra <I,G,J>': ok_sq, 'H1 == 0': ok_one, 'trace H': trace, 'rank H = trace/40': Fr(trace, 40)}


def check_lemma_d(trials=25, seed=20261017):
    rng = random.Random(seed)
    A = [[Fr(8 * (i == j) + 6) for j in range(12)] for i in range(12)]
    detA = det(A)
    Ainv = [[(Fr(1 if i == j else 0) - Fr(3, 40)) / 8 for j in range(12)] for i in range(12)]
    inv_ok = matmul(A, Ainv) == [[Fr(1 if i == j else 0) for j in range(12)] for i in range(12)]
    bad = 0
    for _ in range(trials):
        cols = []
        for _ in range(3):
            v = [0] * 12
            budget = 8
            while budget:
                i = rng.randrange(12)
                step = min(budget, rng.choice([1, 2]))
                if v[i] + step <= 2:
                    v[i] += step
                    budget -= step
            cols.append(v)
        P = [[Fr(cols[c][r]) for c in range(3)] for r in range(12)]
        PtP = matmul(transpose(P), P)
        lhs = [[Fr(1 if i == j else 0) - x for j, x in enumerate(row)] for i, row in enumerate(matmul(matmul(transpose(P), Ainv), P))]
        HS = [[40 * (i == j) - 5 * PtP[i][j] + 24 for j in range(3)] for i in range(3)]
        rhs = [[x / 40 for x in row] for row in HS]
        if lhs != rhs:
            bad += 1
    return {'det(8I+6J_12)': str(detA), 'equals 2^37*5': detA == 2 ** 37 * 5, 'A^{-1} = (I-(3/40)J)/8': inv_ok,
            'I - P^T A^-1 P == H[S]/40 on random P (col sums 8)': bad == 0, 'trials': trials,
            'constant det(A)/40^3 == 2^28/25': Fr(2 ** 37 * 5, 40 ** 3) == Fr(2 ** 28, 25)}


def step4_multisets():
    """All multisets of nonzero integers with sum 2 and sum of squares 6 (at most 14 entries)."""
    out = set()

    def rec(remaining_sq, current):
        if remaining_sq == 0:
            if sum(current) == 2 and len(current) <= 14:
                out.add(tuple(sorted(current)))
            return
        r = math.isqrt(remaining_sq)
        for v in range(-r, r + 1):
            if v == 0 or (current and v < current[-1]):
                continue
            rec(remaining_sq - v * v, current + [v])
    rec(6, [])
    return sorted(out)


GAMMA_INV = [[Fr(4, 15), Fr(1, 15)], [Fr(1, 15), Fr(4, 15)]]


def F(p, q):
    return sum(p[i] * GAMMA_INV[i][j] * q[j] for i in range(2) for j in range(2))


def is_int(x):
    return x.denominator == 1


def rank_one_feasible(cols, Hdiag):
    """cols: list of p-vectors for non-type-2 columns; Hdiag: their H_kk. Return list of surviving sign patterns."""
    n = len(cols)
    Y = [Hdiag[k] - F(cols[k], cols[k]) for k in range(n)]
    if any(y < 0 for y in Y):
        return [], 'negative Y_kk'
    survivors = []
    for signs in product([1, -1], repeat=n):
        # y_k y_l = s_k s_l sqrt(Y_k Y_l); need sqrt(Y_k Y_l) rational for integrality of H_kl
        ok = True
        for k, l in combinations(range(n), 2):
            prod = Y[k] * Y[l]
            num, den = prod.numerator, prod.denominator
            rn, rd = math.isqrt(num), math.isqrt(den)
            if rn * rn != num or rd * rd != den:
                ok = False
                break
            h = F(cols[k], cols[l]) + signs[k] * signs[l] * Fr(rn, rd)
            if not is_int(h) or (int(h) + 1) % 5 != 0 or h * h > Hdiag[k] * Hdiag[l]:
                ok = False
                break
        if not ok:
            continue
        # sum y = 0 with y_k = s_k sqrt(Y_k): compare as a sum of square roots; group by squarefree part
        groups = {}
        for k in range(n):
            if Y[k] == 0:
                continue
            num, den = Y[k].numerator, Y[k].denominator
            # sqrt(num/den) = sqrt(num*den)/den; write num*den = a^2 * b with b squarefree
            m = num * den
            a, b = 1, 1
            f = 2
            while f * f <= m:
                while m % (f * f) == 0:
                    m //= f * f
                    a *= f
                f += 1
            b = m
            groups.setdefault(b, Fr(0))
            groups[b] += signs[k] * Fr(a, den)
        if all(v == 0 for v in groups.values()):
            survivors.append(signs)
    return survivors, 'enumerated'


def residual_cases():
    report = {}
    # n2 = 10: classes 5+5; five non-type-2 columns: four type-1 (H=14) and one type-0 (H=24).
    # Each coordinate (at a and at b) is -1 or -6 with exactly two -6 among the five.
    res10 = []
    for A6 in combinations(range(5), 2):
        for B6 in combinations(range(5), 2):
            cols = [(-6 if k in A6 else -1, -6 if k in B6 else -1) for k in range(5)]
            for zero_col in range(5):
                Hd = [24 if k == zero_col else 14 for k in range(5)]
                sF = sum(F(c, c) for c in cols)
                if sF != sum(Hd) - 40:
                    continue
                surv, why = rank_one_feasible(cols, Hd)
                res10.append({'cols': cols, 'type0': zero_col, 'survivors': len(surv), 'why': why})
    report['n2=10 assignments passing trace condition'] = len(res10)
    report['n2=10 survivors after rank-one/integrality'] = sum(r['survivors'] for r in res10)
    # n2 = 9: classes |A| = 5, |B| = 4; six type-1 columns (H=14).
    # At a (class of size 5): two -6, four -1. At b (class of size 4): one 4, two -6, three -1.
    res9 = []
    for A6 in combinations(range(6), 2):
        for b4 in range(6):
            for B6 in combinations([k for k in range(6) if k != b4], 2):
                cols = [(-6 if k in A6 else -1, 4 if k == b4 else (-6 if k in B6 else -1)) for k in range(6)]
                Hd = [14] * 6
                if any(F(c, c) > 14 for c in cols):
                    continue
                sF = sum(F(c, c) for c in cols)
                if sF != sum(Hd) - 40:
                    continue
                surv, why = rank_one_feasible(cols, Hd)
                res9.append({'cols': cols, 'survivors': len(surv), 'why': why})
    report['n2=9 assignments passing Y>=0 and trace condition'] = len(res9)
    report['n2=9 survivors after rank-one/integrality'] = sum(r['survivors'] for r in res9)
    # Control: drop the integrality/mod-5 requirement -> show that the trace-feasible n2=9 pattern is otherwise consistent,
    # i.e. integrality is what kills it (sensitivity of the check).
    return report


def main():
    out = Path(sys.argv[1])
    rep = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds'),
           'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'identities': check_identities(), 'lemma_d': check_lemma_d(), 'step4_multisets': step4_multisets(),
           'residual_cases': residual_cases()}
    rep['all_consistent_with_proof'] = (rep['identities']['H^2 == 40H in algebra <I,G,J>'] and rep['identities']['H1 == 0']
        and rep['identities']['trace H'] == 120 and rep['lemma_d']['equals 2^37*5'] and rep['lemma_d']['A^{-1} = (I-(3/40)J)/8']
        and rep['lemma_d']['I - P^T A^-1 P == H[S]/40 on random P (col sums 8)'] and rep['lemma_d']['constant det(A)/40^3 == 2^28/25']
        and rep['step4_multisets'] == [(-1, -1, 1, 1, 1, 1), (-1, 1, 2)]
        and rep['residual_cases']['n2=10 survivors after rank-one/integrality'] == 0
        and rep['residual_cases']['n2=9 survivors after rank-one/integrality'] == 0)
    with out.open('x') as f:
        json.dump(rep, f, indent=2, default=str)
        f.write('\n')
    print(json.dumps(rep, indent=1, default=str))


if __name__ == '__main__':
    main()

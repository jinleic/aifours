"""Lemma DL (dominance of rigid step pairs), degree 7, regular Theorem-J case.  Two parts:
 (1) exact identity controls on random rational data for the coefficient formulas used in the
     written proof, plus a mutation control (negative top width coefficient lets the forbidden
     order occur);
 (2) the list of the 43 regular n=7 census rows removed by DL: rows where two corners with three
     contacts form a step pair X -> Y (Y = X with one component raised from '-' to '+') and Y's
     sorted node indices are componentwise <= X's (then Y's contacts are componentwise smaller).
Usage: python lemma_dl.py OUT.json
"""
from __future__ import annotations

import json
import random
import sys
from fractions import Fraction as Fr

import sympy as sp

t = sp.symbols('t')


def identity_controls(trials=40, seed=7):
    rng = random.Random(seed)
    ok = True
    for _ in range(trials):
        r = sorted(Fr(rng.randint(1, 400), rng.randint(1, 30)) for _ in range(3))
        b7, d = Fr(rng.randint(1, 50), 7), Fr(rng.randint(1, 50), 11)
        Q = sp.expand((t - r[0]) * (t - r[1]) * (t - r[2]))
        P = sp.Poly(sp.expand((b7 * t + d) * Q ** 2), t)
        c = P.all_coeffs()[::-1]
        ok &= (c[7] == b7) and (c[6] == d - 2 * b7 * sum(r)) and (c[0] == d * (r[0] * r[1] * r[2]) ** 2)
        b = [Fr(rng.randint(1, 30), rng.randint(1, 9)) for _ in range(8)]
        w = [Fr(rng.randint(0, 30), rng.randint(1, 9)) for _ in range(4)]
        v = [Fr(rng.randint(0, 30), rng.randint(1, 9)) for _ in range(3)]
        Eb = b[0] - b[2] * t + b[4] * t ** 2 - b[6] * t ** 3
        Ob = b[1] - b[3] * t + b[5] * t ** 2 - b[7] * t ** 3
        WE = sum(w[k] * t ** k for k in range(4)); WO = sum(v[k] * t ** k for k in range(3))
        DE = sp.Poly(sp.expand(Eb * WE), t).all_coeffs()[::-1]
        DO = sp.Poly(sp.expand(t * Ob * WO), t).all_coeffs()[::-1]
        DE += [0] * (8 - len(DE)); DO += [0] * (8 - len(DO))
        ok &= (DE[6] == -b[6] * w[3]) and (DE[0] == b[0] * w[0]) and (DE[7] == 0)
        ok &= (DO[6] == -b[7] * v[2]) and (DO[0] == 0) and (DO[7] == 0)
    return bool(ok)


def mutation_control():
    """With a NEGATIVE top width coefficient the forbidden order is consistent with the two
    coefficient relations: exhibit rationals with rho_Y < rho_X, sigma_Y < sigma_X,
    P_Y(0) >= P_X(0) and [t^6](P_Y - P_X) = -b6*w3 > 0 when w3 < 0."""
    rX, rY = [Fr(2), Fr(5), Fr(9)], [Fr(1), Fr(4), Fr(8)]
    b7, b6 = Fr(1), Fr(1)
    dX = Fr(1)
    rhoX, rhoY = rX[0] * rX[1] * rX[2], rY[0] * rY[1] * rY[2]
    dY = dX * (rhoX / rhoY) ** 2          # equal constant terms
    lhs = (dY - 2 * b7 * sum(rY)) - (dX - 2 * b7 * sum(rX))   # [t^6](P_Y - P_X)
    w3 = -lhs / b6                         # the top width coefficient this would require
    return {'rhoY<rhoX': rhoY < rhoX, 'sigmaY<sigmaX': sum(rY) < sum(rX),
            't6_difference': str(lhs), 'required_w3': str(w3), 'required_w3_negative': w3 < 0}


STEP = {('--', '+-'), ('-+', '++'), ('--', '-+'), ('+-', '++')}   # (X, Y): Y raises one component


def removed_rows():
    rows = json.load(open('../evidence/census7_regular.json'))
    removed = []
    for r in rows:
        idx = {}
        for i, c in enumerate(r['corners'], 1):
            idx.setdefault(c, []).append(i)
        rigid = [c for c, v in idx.items() if len(v) == 3]
        hit = None
        for X in rigid:
            for Y in rigid:
                if (X, Y) in STEP:
                    if all(a <= b for a, b in zip(sorted(idx[Y]), sorted(idx[X]))):
                        hit = (X, Y, idx[X], idx[Y])
        if hit:
            removed.append({'kappa': r['kappa'], 'q': ''.join(map(str, r['q'])),
                            'corners': ' '.join(r['corners']), 'X': hit[0], 'Y': hit[1],
                            'X_nodes': hit[2], 'Y_nodes': hit[3]})
    rigid_pairs = sum(1 for r in rows if sum(1 for c in set(r['corners'])
                                                if r['corners'].count(c) == 3) >= 2)
    return removed, rigid_pairs, len(rows)


if __name__ == '__main__':
    rem, npairs, tot = removed_rows()
    out = {'identity_controls_exact': identity_controls(), 'mutation_control': mutation_control(),
           'rows_total': tot, 'rows_with_two_rigid_corners': npairs, 'rows_removed': rem}
    json.dump(out, open(sys.argv[1], 'w'), indent=1, default=str)
    print(json.dumps({k: out[k] for k in ('identity_controls_exact', 'mutation_control',
                                          'rows_total', 'rows_with_two_rigid_corners')}, default=str))
    for x in rem:
        print(x)

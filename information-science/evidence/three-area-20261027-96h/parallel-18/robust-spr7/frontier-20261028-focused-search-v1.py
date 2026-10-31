#!/usr/bin/env python3
"""Focus prior box search at actual corner component-root neighborhoods.

Double-precision location/LP is scouting ONLY. Every output certificate is
recomputed using Fraction; output is exclusive-created. Four exact Routh tables
certify Kharitonov corner stability, with the standard Kharitonov theorem named
as an external mathematical input for all-member box stability.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('frontier_box_search', HERE / 'frontier-20261028-box-search-v1.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def focused_grid(cs):
    points = set(base.grid())
    for a in cs:
        even = [float(a[0]), -float(a[2]), float(a[4]), -float(a[6])]
        odd = [float(a[1]), -float(a[3]), float(a[5]), -1.0]
        for poly in (even, odd):
            for z in np.roots(list(reversed(poly))):
                if z.real > 0 and abs(z.imag) <= 1e-7 * (1 + abs(z.real)):
                    t = F(float(z.real)).limit_denominator(10**7)
                    if t > 0:
                        for ratio in (F(999,1000), F(99999,100000), F(1), F(100001,100000), F(1001,1000)):
                            points.add(t*ratio)
    return sorted(points)


def exact_solve_unique(matrix, rhs):
    """Unique solution of an overdetermined rational system; reject inconsistency."""
    A = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    m, n = len(A), len(A[0])-1
    pivots = []
    r = 0
    for c in range(n):
        hit = next((j for j in range(r, m) if A[j][c] != 0), None)
        if hit is None:
            continue
        A[r], A[hit] = A[hit], A[r]
        pivot = A[r][c]
        A[r] = [v/pivot for v in A[r]]
        for j in range(m):
            if j != r and A[j][c] != 0:
                scale = A[j][c]
                A[j] = [u-scale*v for u,v in zip(A[j],A[r])]
        pivots.append(c)
        r += 1
        if r == m:
            break
    if any(all(row[c] == 0 for c in range(n)) and row[n] != 0 for row in A):
        return None
    if len(pivots) != n:
        return None
    solution = [F(0)]*n
    for j,c in enumerate(pivots):
        solution[c] = A[j][n]
    return solution


def exact_unrestricted_separation(cs, ts, weights):
    support = [(i//len(ts), i%len(ts)) for i,w in enumerate(weights) if w > 1e-8]
    if not (0 < len(support) <= 8):
        return None
    rows = [base.row_exact(cs[ci], ts[ti]) for ci,ti in support]
    matrix = [[row[j] for row in rows] for j in range(7)]
    matrix.append([F(1)]*len(rows))
    weights_q = exact_solve_unique(matrix, [F(0)]*7+[F(1)])
    if weights_q is None or any(w < 0 for w in weights_q):
        return None
    coefficient = sum(w*row[7] for w,row in zip(weights_q,rows))
    if coefficient >= 0:
        return None
    return {'weights': [{'corner':ci,'t':str(ts[ti]),'weight':str(w)}
                        for (ci,ti),w in zip(support,weights_q) if w],
            'weighted_leading_coefficient':str(coefficient),
            'scope':'exact finite-frequency annihilator excludes every exact-degree-7 numerator after positive leading normalization'}


def strings(xs):
    return [str(x) for x in xs]


def snapshot(trial, box, restricted, unrestricted, ts):
    center,lo,hi,cs,cols,scale = box
    return {'trial':trial, 'center':strings(center), 'lower':strings(lo), 'upper':strings(hi),
            'corners':[strings(c) for c in cs], 'routh_first_columns':[strings(col) for col in cols],
            'width_scale':str(scale), 'grid_count':len(ts),
            'restricted_grid_margin':restricted and restricted['margin'],
            'unrestricted_grid_margin':unrestricted and unrestricted['margin'],
            'unrestricted_grid_b':unrestricted and unrestricted['b']}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--seed', type=int, required=True)
    p.add_argument('--trials', type=int, default=300)
    p.add_argument('--seconds', type=float, default=90)
    p.add_argument('--output', required=True)
    args = p.parse_args()
    if not (1 <= args.trials <= 5000 and 0 < args.seconds <= 120):
        p.error('trials 1..5000; seconds 0..120')
    out = Path(args.output).open('x',encoding='utf-8')
    rng = np.random.default_rng(args.seed)
    started = time.monotonic()
    visited = stable = solved = 0
    best_u = best_r = None
    exact_u = exact_r = None
    try:
        for trial in range(args.trials):
            if time.monotonic()-started >= args.seconds:
                break
            visited += 1
            box = base.build_box(rng)
            if box is None:
                continue
            stable += 1
            center,lo,hi,cs,cols,scale = box
            ts = focused_grid(cs)
            restricted = base.solve(center,lo,hi,cs,ts,True)
            unrestricted = base.solve(center,lo,hi,cs,ts,False)
            if restricted is None or unrestricted is None:
                continue
            solved += 1
            if best_u is None or unrestricted['margin'] < best_u['unrestricted_grid_margin']:
                best_u = snapshot(trial,box,restricted,unrestricted,ts)
                print('best unrestricted trial',trial,'grid margin',unrestricted['margin'],
                      'restricted',restricted['margin'],'grid points',len(ts),flush=True)
            if best_r is None or restricted['margin'] < best_r['restricted_grid_margin']:
                best_r = snapshot(trial,box,restricted,unrestricted,ts)
            if unrestricted['margin'] < 0:
                cert = exact_unrestricted_separation(cs,ts,unrestricted['weights'])
                if cert:
                    exact_u = snapshot(trial,box,restricted,unrestricted,ts)
                    exact_u['certificate'] = cert
                    print('EXACT UNRESTRICTED SEPARATION trial',trial,flush=True)
                    break
            if restricted['margin'] < 0:
                cert = base.exact_box_separation(cs,ts,lo,hi,restricted['weights'])
                if cert:
                    exact_r = snapshot(trial,box,restricted,unrestricted,ts)
                    exact_r['certificate'] = cert
                    print('EXACT IN-BOX SEPARATION trial',trial,flush=True)
                    break
        result = {'schema':1,'seed':args.seed,'requested_trials':args.trials,'visited_trials':visited,
                  'exact_corner_routh_pass':stable,'grid_lp_solved':solved,
                  'elapsed_seconds':time.monotonic()-started,'best_unrestricted_grid':best_u,
                  'best_restricted_grid':best_r,'exact_unrestricted_certificate':exact_u,
                  'exact_restricted_certificate':exact_r,
                  'scope':'float root/grid locations and LP are exploratory; exact Fraction checks only on reported finite certificates; four-corner exact Routh + named Kharitonov theorem for all-member stability; grid positive is not a proof'}
        json.dump(result,out,indent=2,sort_keys=True,allow_nan=False)
        out.write('\n')
        print('RESULT',json.dumps({'visited':visited,'exact_stable':stable,'solved':solved,
                                  'exact_unrestricted':bool(exact_u),'exact_restricted':bool(exact_r),
                                  'best_unrestricted':best_u and best_u['unrestricted_grid_margin'],
                                  'best_restricted':best_r and best_r['restricted_grid_margin'],
                                  'elapsed':result['elapsed_seconds']}),flush=True)
    finally:
        out.close()


if __name__ == '__main__':
    main()

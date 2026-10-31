#!/usr/bin/env python3
"""Bounded exploratory common-numerator search; exact audit of any certificate.

All coefficient arrays are ascending. Search uses double-precision root and LP
screening only; a saved certificate uses Fraction and is explicitly conditional
on the four-corner Kharitonov theorem. A positive grid margin is NOT a proof of
positive realness. Nothing here treats a finite grid as a global positivity test.

Run: python -B ... --seed 1031 --trials 120 --seconds 90 --output NEW.json
Output is exclusive-created. No files outside the assigned root are written.
"""
from __future__ import annotations
import argparse
import json
import math
import time
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

N = 7


def conv(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def corners(lo, hi):
    result = []
    for e in (0, 1):
        for o in (0, 1):
            a = []
            for j in range(7):
                # alternating signs in each parity's real part
                lower = ((j // 2) % 2 == 0) == ((e if j % 2 == 0 else o) == 0)
                a.append(lo[j] if lower else hi[j])
            result.append(a + [F(1)])
    return result


def numerically_stable(cs):
    for c in cs:
        roots = np.roots([float(x) for x in reversed(c)])
        if not np.all(np.real(roots) < -1e-9):
            return False
    return True


def routh_first_column(a):
    """Exact Routh array, strict Hurwitz iff first column >0 for this real monic polynomial."""
    coeff = list(reversed(a))
    width = (len(coeff) + 1) // 2
    row0 = coeff[0::2] + [F(0)] * (width - len(coeff[0::2]))
    row1 = coeff[1::2] + [F(0)] * (width - len(coeff[1::2]))
    rows = [row0, row1]
    for _ in range(N - 1):
        x, y = rows[-2], rows[-1]
        if y[0] == 0:
            return None
        rows.append([(y[0] * x[j + 1] - x[0] * y[j + 1]) / y[0]
                     for j in range(width - 1)] + [F(0)])
    return [row[0] for row in rows]


def make_center(rng):
    rates = (F(1, 2), F(1), F(2), F(3))
    damping = (F(1, 20), F(1, 10), F(1, 5), F(2, 5), F(4, 5))
    c = [rates[int(rng.integers(len(rates)))], F(1)]
    for _ in range(3):
        w = rates[int(rng.integers(len(rates)))]
        z = damping[int(rng.integers(len(damping)))]
        c = conv(c, [w*w, 2*z*w, F(1)])
    return c


def build_box(rng):
    center = make_center(rng)
    wl = [center[j] * F(int(rng.integers(1, 11)), 10) for j in range(7)]
    wu = [center[j] * F(int(rng.integers(1, 11)), 10) for j in range(7)]
    cf = np.array([float(x) for x in center])
    wlf, wuf = np.array([float(x) for x in wl]), np.array([float(x) for x in wu])
    def box_at(x):
        return (list(cf[:7] - x*wlf) + [1.0], list(cf[:7] + x*wuf) + [1.0])
    lower, upper = 0.0, 1.0
    while upper < 16.0 and numerically_stable(corners(*box_at(upper))):
        lower, upper = upper, upper * 2.0
    for _ in range(34):
        mid = (lower + upper) / 2.0
        if numerically_stable(corners(*box_at(mid))):
            lower = mid
        else:
            upper = mid
    safety = (F(9, 10), F(19, 20), F(99, 100), F(999, 1000))
    mult = safety[int(rng.integers(len(safety)))]
    scale = F(max(1, math.floor(lower * float(mult) * 10**7)), 10**7)
    lo = [center[j] - scale*wl[j] for j in range(7)] + [F(1)]
    hi = [center[j] + scale*wu[j] for j in range(7)] + [F(1)]
    if not all(0 < lo[j] < hi[j] for j in range(7)):
        return None
    cs = corners(lo, hi)
    cols = [routh_first_column(c) for c in cs]
    if any(col is None or any(x <= 0 for x in col) for col in cols):
        return None
    return center, lo, hi, cs, cols, scale


def grid():
    g = {F(0)}
    for k in range(-13, 14):
        x = F(2) ** k
        g.add(x)
        g.add(F(3, 2) * x)
    return sorted(g)


def row_exact(a, t):
    E = sum(((-1)**(j//2)) * a[j] * t**(j//2) for j in range(0, 8, 2))
    O = sum(((-1)**(j//2)) * a[j] * t**(j//2) for j in range(1, 8, 2))
    den = (1+t)**7
    return [F((-1)**(j//2)) * t**(j//2) * E / den if j % 2 == 0
            else F((-1)**(j//2)) * t**((j+1)//2) * O / den
            for j in range(8)]


def row_float(a, ts):
    a = np.asarray([float(x) for x in a])
    E = a[0] - a[2]*ts + a[4]*ts**2 - a[6]*ts**3
    O = a[1] - a[3]*ts + a[5]*ts**2 - ts**3
    d = (1 + ts)**7
    return np.column_stack([((-1)**(j//2))*ts**(j//2)*E/d if j % 2 == 0
                            else ((-1)**(j//2))*ts**((j+1)//2)*O/d
                            for j in range(8)])


def solve(center, lo, hi, cs, ts, restricted):
    vals = np.array([float(t) for t in ts])
    rows = np.vstack([row_float(a, vals) for a in cs])
    scale = np.array([float(x) for x in center[:7]])
    A = np.column_stack((-rows[:, :7]*scale, np.ones(len(rows))))
    objective = np.array([0.0]*7 + [-1.0])
    if restricted:
        bounds = [(float(lo[j]/center[j]), float(hi[j]/center[j])) for j in range(7)]
    else:
        bounds = [(None, None)]*7
    bounds.append((None, 1.0))
    res = linprog(objective, A_ub=A, b_ub=rows[:, 7], bounds=bounds,
                  method='highs', options={'time_limit': 3.0})
    if not res.success:
        return None
    return {'margin': float(res.x[-1]),
            'b': list(res.x[:7]*scale) + [1.0],
            'weights': -np.asarray(res.ineqlin.marginals),
            'iterations': int(res.nit)}


def exact_box_separation(cs, ts, lo, hi, dual):
    """Any nonnegative rational weights suffice: maximize their sum on b in K."""
    active = [(i//len(ts), i%len(ts), F(float(w)).limit_denominator(10**9))
              for i, w in enumerate(dual) if w > 1e-9]
    if not active:
        return None
    accum = [F(0)]*8
    for ci, ti, w in active:
        row = row_exact(cs[ci], ts[ti])
        accum = [x+w*y for x, y in zip(accum, row)]
    maximum = accum[7] + sum(accum[j] * (hi[j] if accum[j] >= 0 else lo[j])
                             for j in range(7))
    if maximum >= 0:
        return None
    return {'weights': [{'corner': ci, 't': str(ts[ti]), 'weight': str(w)}
                        for ci, ti, w in active],
            'max_over_b_in_box': str(maximum),
            'scope': 'strict pairing impossible for a common numerator constrained to b in K; NOT unrestricted SPR failure'}


def jsonify_fracs(items):
    return [str(x) for x in items]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--seed', type=int, required=True)
    parser.add_argument('--trials', type=int, default=80)
    parser.add_argument('--seconds', type=float, default=75)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    if args.trials < 1 or args.trials > 1000 or not (0 < args.seconds <= 120):
        parser.error('trials must be 1..1000 and seconds 0..120')
    dest = Path(args.output)
    # Claim path before computation; never overwrite a receipt.
    handle = dest.open('x', encoding='utf-8')
    rng = np.random.default_rng(args.seed)
    ts = grid()
    started = time.monotonic()
    seen = exact_stable = 0
    best = None
    negative_unrestricted = []
    exact_restricted = None
    try:
        for trial in range(args.trials):
            if time.monotonic()-started >= args.seconds:
                break
            seen += 1
            box = build_box(rng)
            if box is None:
                continue
            center, lo, hi, cs, cols, scale = box
            exact_stable += 1
            restricted = solve(center, lo, hi, cs, ts, True)
            if restricted is None:
                continue
            unrestricted = solve(center, lo, hi, cs, ts, False)
            if best is None or restricted['margin'] < best['restricted_margin']:
                best = {'trial': trial, 'center': jsonify_fracs(center),
                        'lower': jsonify_fracs(lo), 'upper': jsonify_fracs(hi),
                        'corners': [jsonify_fracs(c) for c in cs],
                        'routh_first_columns': [jsonify_fracs(x) for x in cols],
                        'width_scale': str(scale),
                        'restricted_margin': restricted['margin'],
                        'unrestricted_grid_margin': unrestricted and unrestricted['margin'],
                        'unrestricted_grid_b': unrestricted and unrestricted['b']}
                print('best trial', trial, 'restricted', restricted['margin'],
                      'unrestricted', unrestricted and unrestricted['margin'], flush=True)
            if restricted['margin'] < -1e-8:
                cert = exact_box_separation(cs, ts, lo, hi, restricted['weights'])
                if cert:
                    unrestricted = solve(center, lo, hi, cs, ts, False)
                    exact_restricted = {'trial': trial, 'center': jsonify_fracs(center),
                                        'lower': jsonify_fracs(lo), 'upper': jsonify_fracs(hi),
                                        'corners': [jsonify_fracs(c) for c in cs],
                                        'routh_first_columns': [jsonify_fracs(x) for x in cols],
                                        'certificate': cert,
                                        'unrestricted_grid_margin': unrestricted and unrestricted['margin'],
                                        'unrestricted_grid_b': unrestricted and unrestricted['b']}
                    print('EXACT restricted separation at trial', trial, flush=True)
                    break
            if unrestricted and unrestricted['margin'] < -1e-8:
                negative_unrestricted.append({'trial': trial, 'grid_margin': unrestricted['margin'],
                                              'status': 'numerical lead only; no exact dual certificate'})
        result = {'schema': 1, 'seed': args.seed, 'requested_trials': args.trials,
                  'visited_trials': seen, 'exact_corner_routh_pass': exact_stable,
                  'grid_t': jsonify_fracs(ts), 'elapsed_seconds': time.monotonic()-started,
                  'stability_scope': 'exact Routh positivity on four parity corners; full box Hurwitz conditional on classical Kharitonov theorem',
                  'numerics_scope': 'grid LP upper bounds only; float values NOT rigorous and positive margins do not prove half-line positivity',
                  'exact_restricted_certificate': exact_restricted,
                  'best_grid_candidate': best, 'numerical_negative_unrestricted_leads': negative_unrestricted}
        json.dump(result, handle, indent=2, sort_keys=True, allow_nan=False)
        handle.write('\n')
        print('RESULT', json.dumps({'visited': seen, 'exact_corner_routh_pass': exact_stable,
                                    'exact_restricted': exact_restricted is not None,
                                    'best': best and best['restricted_margin'],
                                    'elapsed': result['elapsed_seconds']}), flush=True)
    finally:
        handle.close()


if __name__ == '__main__':
    main()

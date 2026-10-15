#!/usr/bin/env python3
"""Generate column-count candidates; correctness is decided by verify.py."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path
import platform
import sys
import time
import warnings
import numpy as np
import scipy
from scipy.optimize import Bounds, LinearConstraint, linprog, milp


def monotone_tables(n):
    tables = [0, 1]
    for k in range(n):
        half = 1 << k
        tables = [a | (b << half) for a in tables for b in tables if a & ~b == 0]
    return tables


def instances(n):
    transforms = [[sum(1 << p[i] for i in range(n) if s >> i & 1)
                   for s in range(1 << n)] for p in permutations(range(n))]
    reps = {}
    for truth in monotone_tables(n):
        if truth == 0 or truth & 1:
            continue
        a = tuple(s for s in range(1, 1 << n) if truth >> s & 1
                  and all(not (truth >> (s ^ (1 << i)) & 1)
                          for i in range(n) if s >> i & 1))
        canonical = min(tuple(sorted(t[s] for s in a)) for t in transforms)
        reps[canonical] = True
    return sorted(reps)


def partition(n, a):
    q = [s for s in range(1 << n) if any(s & b == b for b in a)]
    f = [s for s in range(1 << n) if s not in q]
    return q, f


def moment(n, s):
    z = [int(t & s == 0) for t in range(1 << n)]
    return z + [-v for v in z]


def rational(values):
    return [str(Fraction(float(v)).limit_denominator(1000000)) for v in values]


def contrast_lp(n, a):
    k = 1 << n
    q, f = partition(n, a)
    eq = [[1] * k + [0] * (k + 1), [0] * k + [1] * k + [0]]
    rhs = [1, 1]
    for s in f:
        if s:
            eq.append(moment(n, s) + [0])
            rhs.append(0)
    ub = [[-v for v in moment(n, s)] + [1] for s in q]
    c = [0] * (2 * k) + [-1]
    result = linprog(c, A_ub=ub, b_ub=[0] * len(q), A_eq=eq, b_eq=rhs,
                     bounds=(0, None), method='highs', options={'threads': 1})
    if not result.success:
        raise RuntimeError(result.message)
    return {'alpha': rational([result.x[-1]])[0],
            'primal': rational(result.x),
            'dual_inequality': rational(result.ineqlin.marginals),
            'dual_equality': rational(result.eqlin.marginals)}


def integer_program(n, a, mode, alpha=None, fixed_m=None):
    k = 1 << n
    q, f = partition(n, a)
    with_gap = mode == 'fixed_m'
    size = 2 * k + int(with_gap)
    rows = [[1] * k + [-1] * k + ([0] if with_gap else [])]
    low, high = [0], [0]
    for s in f:
        if s:
            rows.append(moment(n, s) + ([0] if with_gap else []))
            low.append(0)
            high.append(0)
    for s in q:
        row = moment(n, s)
        if mode == 'alpha':
            row = [alpha.denominator * v - (alpha.numerator if i < k else 0)
                   for i, v in enumerate(row)]
            bound = 0
        elif with_gap:
            row += [-1]
            bound = 0
        else:
            bound = 1
        rows.append(row)
        low.append(bound)
        high.append(np.inf)
    if fixed_m is not None or mode == 'alpha':
        rows.append([1] * k + [0] * (size - k))
        low.append(fixed_m if fixed_m is not None else 1)
        high.append(fixed_m if fixed_m is not None else np.inf)
    cost = [1] * k + [0] * (size - k)
    if with_gap:
        cost = [0] * (size - 1) + [-1]
    result = milp(np.array(cost, float), integrality=np.ones(size),
                  bounds=Bounds(np.zeros(size), np.full(size, np.inf)),
                  constraints=LinearConstraint(np.array(rows, float), low, high),
                  options={'time_limit': 30, 'mip_rel_gap': 0, 'threads': 1})
    if not result.success or result.x is None:
        raise RuntimeError(f'{mode}: {result.message}')
    z = [int(round(v)) for v in result.x]
    if max(abs(v - w) for v, w in zip(result.x, z)) > 1e-6:
        raise RuntimeError('Non-integral MILP candidate')
    return {'white': z[:k], 'black': z[k:2*k], 'm': sum(z[:k]),
            'gap': min(sum(v*w for v, w in zip(moment(n, s), z)) for s in q)}


def run(max_n, output):
    started = time.monotonic()
    records = []
    counts = {}
    for n in range(1, max_n + 1):
        reps = instances(n)
        counts[str(n)] = len(reps)
        for a in reps:
            lp = contrast_lp(n, a)
            minimum = integer_program(n, a, 'minimum')
            fixed = integer_program(n, a, 'fixed_m', fixed_m=minimum['m'])
            best = integer_program(n, a, 'alpha', alpha=Fraction(lp['alpha']))
            records.append({'id': f'n{n}-' + '-'.join(map(str, a)), 'n': n,
                            'minimal_qualified': list(a), 'lp': lp,
                            'minimum_expansion': minimum,
                            'contrast_at_minimum': fixed,
                            'expansion_at_maximum_contrast': best})
        print(f'n={n}: {len(reps)} classes; total {len(records)}', flush=True)
    data = {'schema': 'vcs-column-certificates-1', 'model': 'strong-basis-OR',
            'command': ' '.join(sys.argv), 'python': platform.python_version(),
            'numpy': np.__version__, 'scipy': scipy.__version__, 'threads': 1,
            'class_counts': counts, 'seconds': time.monotonic() - started,
            'records': records}
    output.write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({k: v for k, v in data.items() if k != 'records'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, choices=range(1, 6), default=5)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', message='.*[Uu]nrecognized options.*')
        run(args.max_n, args.output)

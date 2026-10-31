#!/usr/bin/env python3
"""Screen one-row replacements of a level-six minor by exact axis gcd degrees.

For the baseline selected rows and K slot replacements, exact determinants on
the two axes x=0 and y=0 give exact univariate restrictions; their gcd degrees
with the baseline restrictions bound the size of any common bivariate factor.
This only CHOOSES a second minor; no rank or injectivity claim follows.
"""
import argparse
import importlib.util
import json
from fractions import Fraction as Q
from multiprocessing import Pool
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


al6 = load('al6', 'frontier-20261028-level6-alternate-type-minor-search.py')
h = al6.h
S = load('sympyhelper', 'frontier-review-f18-ph7-independent-check.py').S
JOBS = None


def init(jobs):
    global JOBS
    JOBS = jobs


def task(key):
    label, axis, t = key
    data = JOBS[label]
    return key, (h.value(data, 0, t) if axis == 'y' else h.value(data, t, 0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--slot', type=int, default=0)
    ap.add_argument('--count', type=int, default=10)
    ap.add_argument('--skip', type=int, default=0)
    ap.add_argument('--workers', type=int, default=12)
    args = ap.parse_args()
    P = json.loads((ROOT / f'frontier-20261028-level6-free-{args.a}{args.b}-pencil-v1.json').read_text())
    out = ROOT / f'frontier-20261028-level6-{args.a}{args.b}6-axis-screen-slot{args.slot}-skip{args.skip}-v1.json'
    if out.exists():
        raise FileExistsError(out)
    rows = al6.full_rows(P)
    selected = P['selected_target_words']
    cands = sorted(w for w in rows if w not in set(selected))[args.skip:args.skip + args.count]
    jobs, scales = {}, {}
    for label in ['baseline'] + cands:
        words = selected[:]
        if label != 'baseline':
            words[args.slot] = label
        jobs[label], scales[label] = h.int_rows([rows[w] for w in words])
    n = len(selected)
    keys = [(label, axis, t) for label in jobs for axis in ('x', 'y') for t in range(n + 1)]
    with Pool(args.workers, initializer=init, initargs=(jobs,)) as pool:
        vals = dict(pool.imap_unordered(task, keys, chunksize=4))
    var = S.Symbol('t')
    polys = {}
    for label in jobs:
        for axis in ('x', 'y'):
            co = h.axis_coeff([vals[label, axis, t] for t in range(n + 1)])
            polys[label, axis] = S.Poly([S.Rational(q.numerator, q.denominator * scales[label]) for q in reversed(co)], var)
    report = []
    for label in cands:
        entry = {'word': label}
        for axis in ('x', 'y'):
            base, cand = polys['baseline', axis], polys[label, axis]
            entry[f'{axis}_axis_candidate_degree'] = cand.degree() if not cand.is_zero else -1
            entry[f'{axis}_axis_gcd_degree'] = S.gcd(base, cand).degree() if not cand.is_zero else None
        report.append(entry)
    result = {'degree': [args.a, args.b, 6], 'slot': args.slot,
              'baseline_axis_degrees': {axis: polys['baseline', axis].degree() for axis in ('x', 'y')},
              'candidates': report, 'scope': 'second-minor selection screen only; no rank or injectivity claim'}
    out.write_text(json.dumps(result, indent=2) + '\n')
    best = sorted((e for e in report if e['x_axis_gcd_degree'] is not None and e['y_axis_gcd_degree'] is not None),
                  key=lambda e: (e['x_axis_gcd_degree'] + e['y_axis_gcd_degree']))
    print('DONE screen', (args.a, args.b, 6), 'baseline', result['baseline_axis_degrees'], 'best', best[:3], out.name, flush=True)


if __name__ == '__main__':
    main()

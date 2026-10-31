#!/usr/bin/env python3
"""Choose an alternative full-rank row set of a level-six pencil (selection only).

Rows are scanned in a seeded random order and kept when they increase the exact
rank of the affine matrix evaluated at one rational point.  The output is just a
row list for a second minor; no rank or injectivity claim follows from it.
"""
import argparse
import importlib.util
import json
import random
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


al6 = load('al6', 'frontier-20261028-level6-alternate-type-minor-search.py')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--seed', type=int, required=True)
    ap.add_argument('--x0', type=int, default=7)
    ap.add_argument('--y0', type=int, default=11)
    args = ap.parse_args()
    P = json.loads((ROOT / f'frontier-20261028-level6-free-{args.a}{args.b}-pencil-v1.json').read_text())
    out = ROOT / f'frontier-20261028-level6-{args.a}{args.b}6-rowset-seed{args.seed}-v1.json'
    if out.exists():
        raise FileExistsError(out)
    rows = al6.full_rows(P)
    n = len(P['selected_target_words'])
    order = sorted(rows)
    random.Random(args.seed).shuffle(order)
    span = al6.lift.Span()
    chosen = []
    for w in order:
        vec = {j: e[0] + args.x0 * e[1] + args.y0 * e[2] for j, e in enumerate(rows[w])}
        vec = {j: q for j, q in vec.items() if q}
        before = len(span)
        if vec:
            span.add(vec)
        if len(span) > before:
            chosen.append(w)
        if len(chosen) == n:
            break
    assert len(chosen) == n
    overlap = len(set(chosen) & set(P['selected_target_words']))
    result = {'degree': [args.a, args.b, 6], 'seed': args.seed, 'point': [args.x0, args.y0], 'rows': chosen,
              'overlap_with_baseline_selection': overlap,
              'scope': 'row-set selection only; exact minor and any claim are computed separately'}
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('DONE rowset', (args.a, args.b, 6), 'size', n, 'overlap', overlap, out.name, flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Bounded search for sign-definite minors on the actual horizontal kernel.

Only two parameter classes with mixed-sign first minors are searched.  The
search changes the target-row order, never the original source/ideal/targets.
Every returned polynomial is exact and must be independently replayed.
"""
import importlib.util
import json
import random
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('horizontal', ROOT / 'frontier-20261028-horizontal-kernel-minors.py')
horizontal = importlib.util.module_from_spec(spec)
spec.loader.exec_module(horizontal)
lift, minors = horizontal.lift, horizontal.minors


def solve(original, seed):
    rclass, sclass = original['r_class'], original['s_class']
    r0 = 4 if rclass == '>=4' else rclass
    s0 = 4 if sclass == '>=4' else sclass
    matrix = lambda r, s: ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    target = lift.direct_sum_ideal(lift.ideal_bases((2, 2, 4), matrix(r0, s0)), (2, 2, 4))
    basis = [lift.lyndon_bracket(tuple(map(int, w))) for w in original['source_basis_lyndon_words']]
    coeffs = [{int(k): Fraction(v) for k, v in item.items()} for item in original['horizontal_kernel_coefficients']]
    vectors = [lift.combine(basis, c) for c in coeffs]
    keep = lambda x: horizontal.restrict(x, (2,))
    base = [keep(target.reduce(lift.delta(v, matrix(r0, s0)))) for v in vectors]
    dr = [minors.diff(keep(target.reduce(lift.delta(v, matrix(r0 + 1, s0)))), base[j])
          if rclass == '>=4' else {} for j, v in enumerate(vectors)]
    ds = [minors.diff(keep(target.reduce(lift.delta(v, matrix(r0, s0 + 1))),), base[j])
          if sclass == '>=4' else {} for j, v in enumerate(vectors)]
    # Available rows are all exact nonzero coefficients in the affine family.
    keys = sorted(set().union(*(set(v) for v in base + dr + ds)))
    rng = random.Random(seed)
    for attempt in range(1, 501):
        order = keys[:]
        rng.shuffle(order)
        priority = {key: j for j, key in enumerate(order)}
        span = lift.Span()
        if any(span.add({priority[k]: c for k, c in vector.items()}) is None for vector in base):
            continue
        rows = [order[j] for j in sorted(span.rows)]
        entries = []
        for row in rows:
            row_poly = []
            for j in range(len(vectors)):
                p = {}
                if base[j].get(row, 0): p[(0, 0)] = base[j][row]
                if dr[j].get(row, 0): p[(1, 0)] = dr[j][row]
                if ds[j].get(row, 0): p[(0, 1)] = ds[j][row]
                row_poly.append(p)
            entries.append(row_poly)
        det = minors.determinant(entries)
        if det.get((0, 0), 0) and len({1 if c > 0 else -1 for c in det.values()}) == 1:
            return {
                **original,
                'target_word_pivots': [f'{i + 1}:' + ''.join(map(str, word)) for i, word in rows],
                'determinant_coefficients': [
                    {'x_power': i, 'y_power': j, 'coefficient': lift.rational_text(c)}
                    for (i, j), c in sorted(det.items())],
                'status': 'CERTIFIED_ONE_SIGN_ALTERNATE', 'attempt': attempt,
                'search_seed': seed,
            }
    return {**original, 'status': 'NO_SIGN_DEFINITE_MINOR_FOUND_WITHIN_500', 'search_seed': seed}


def main():
    source = json.loads((ROOT / 'frontier-20261028-224-horizontal-minors-v1.json').read_text(encoding='utf-8'))
    selected = [c for c in source['cases'] if c['status'] == 'MIXED_SIGNS_NEEDS_ANALYSIS']
    assert len(selected) == 2
    cases = [solve(c, 1028 + j) for j, c in enumerate(selected)]
    out = ROOT / 'frontier-20261028-224-alternate-minors-v1.json'
    if out.exists(): raise FileExistsError(out)
    out.write_text(json.dumps({'degree': [2, 2, 4], 'cases': cases,
                               'not_a_formal_proof_or_external_review': True}, indent=2) + '\n', encoding='utf-8')
    print('cases', len(cases), 'found', sum(c['status'] == 'CERTIFIED_ONE_SIGN_ALTERNATE' for c in cases),
          'attempts', [c.get('attempt') for c in cases], out.name)


if __name__ == '__main__': main()

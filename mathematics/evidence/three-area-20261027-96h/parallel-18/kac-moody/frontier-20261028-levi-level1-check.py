#!/usr/bin/env python3
"""Exact matrix-unit and bounded free-Lie checks for the level-one Levi module.

All computations are over Q.  The finite parameter checks are corroboration,
not a proof of the all-parameter theorem in the companion manuscript.
"""
import importlib.util
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lift_exact', ROOT / 'frontier-20261028-lift-exact.py')
lift = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lift)


def unit(i, j):
    return {(i, j): Fraction(1)}


def add(*terms):
    out = {}
    for scalar, matrix in terms:
        for key, value in matrix.items():
            out[key] = out.get(key, Fraction(0)) + scalar * value
    return {key: value for key, value in out.items() if value}


def multiply(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, ell), y in b.items():
            if j == k:
                out[(i, ell)] = out.get((i, ell), Fraction(0)) + x * y
    return {key: value for key, value in out.items() if value}


def bracket(a, b):
    return add((1, multiply(a, b)), (-1, multiply(b, a)))


def action(a, v):
    return bracket(a, v)


def main():
    x, y, f1, f2, v = unit(1, 2), unit(2, 3), unit(2, 1), unit(3, 2), unit(3, 1)
    h1 = add((1, unit(1, 1)), (-1, unit(2, 2)))
    h2 = add((1, unit(2, 2)), (-1, unit(3, 3)))
    z = bracket(x, y)
    assert z == unit(1, 3)
    assert not action(x, z) and not action(y, z)
    assert not action(f1, v) and not action(f2, v)
    assert action(h1, v) == add((-1, v)) and action(h2, v) == add((-1, v))
    assert not action(x, action(x, v)) and not action(y, action(y, v))
    xv, yv, zv = action(x, v), action(y, v), action(z, v)
    xyv = action(x, yv)
    zxv, zyv, z2v = action(z, xv), action(z, yv), action(z, zv)
    actual = [v, xv, yv, zv, xyv, zxv, zyv, z2v]
    expected = [unit(3, 1), add((-1, unit(3, 2))), unit(2, 1),
                add((1, unit(1, 1)), (-1, unit(3, 3))), h1,
                add((-1, unit(1, 2))), add((-1, unit(2, 3))), add((-2, unit(1, 3)))]
    assert actual == expected
    assert lift.rank(actual) == 8
    assert z2v == add((2, action(z, xyv)))
    assert not action(z, action(z, xv))
    assert not action(z, action(z, yv))
    assert not action(z, z2v)
    expected_dims = {(0, 0): 1, (1, 0): 1, (0, 1): 1, (1, 1): 2,
                     (2, 1): 1, (1, 2): 1, (2, 2): 1}
    results = []
    for r in range(1, 5):
        for s in range(1, 5):
            matrix = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
            for a in range(3):
                for b in range(3):
                    degree = (a, b, 1)
                    basis = lift.lie_basis(degree)
                    ideals = lift.ideal_bases(degree, matrix)
                    ideal = ideals.get(degree, lift.Span())
                    dim = len(basis) - len(ideal)
                    expected_dim = expected_dims.get((a, b), 0)
                    assert dim == expected_dim, (r, s, degree, dim, expected_dim)
                    results.append({'r': r, 's': s, 'degree': degree, 'dimension': dim})
    path = ROOT / 'frontier-20261028-levi-level1-check-results-v1.json'
    if path.exists(): raise FileExistsError(path)
    path.write_text(json.dumps({
        'matrix_unit_checks': 'PASS', 'eight_image_rank': 8,
        'universal_relations_checked_in_adjoint_model': 'PASS',
        'full_Serre_quotient_tested_r_s': [1, 4],
        'tested_a_b': [0, 2], 'degree3': 1,
        'case_count': len(results), 'cases': results,
        'not_proof_of_unbounded_parameters_or_independent_review': True,
    }, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: fixed matrix-unit identities/rank8; {len(results)} exact quotient-component checks; {path.name}')


if __name__ == '__main__': main()

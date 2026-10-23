#!/usr/bin/env python3
"""Bind corrected Lemma20 clause generation to an independent declarative six-point set.
Only AST-executes the pinned pure triangle_clauses function; imports no lane modules or solvers.
Usage: python3 -B ame46_v4_triangle_binding_parent.py NEW_OUTPUT_DIRECTORY
"""
import ast
from collections import Counter
from datetime import datetime
import hashlib
import itertools
import json
from math import comb, prod
from pathlib import Path
from types import SimpleNamespace
from zoneinfo import ZoneInfo
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LANE = ROOT / 'physics/evidence/six-lane-20261016/ame46-support'
EXPECTED = '4a7aed5565f3396aeed9b5b02238881b089f624e0e1e78b236e192fc697eeb37'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def declared(S):
    """Choose the two values on each coordinate, orient the three distinct shared edges."""
    result = set()
    for i in range(4):
        other = [k for k in range(4) if k != i]
        for a, b in itertools.combinations(S.V[i], 2):
            for u, v in itertools.permutations(S.V[other[0]], 2):
                for p, q in itertools.permutations(S.V[other[1]], 2):
                    for r, s in itertools.permutations(S.V[other[2]], 2):
                        points = []
                        for z in [(u, p, r), (u, q, s), (v, q, r)]:
                            for x_i in [a, b]:
                                x = [0] * 4
                                x[i] = x_i
                                for k, val in zip(other, z):
                                    x[k] = val
                                points.append(S.var[tuple(x)])
                        result.add(tuple(sorted(points)))
    return result


def has_shape(points):
    for i in range(4):
        vals = Counter(p[i] for p in points)
        if sorted(vals.values()) != [3, 3]:
            continue
        other = [k for k in range(4) if k != i]
        fibers = {v: {tuple(p[k] for k in other) for p in points if p[i] == v} for v in vals}
        zsets = list(fibers.values())
        if len(zsets[0]) != 3 or zsets[0] != zsets[1]:
            continue
        shared = []
        for z, w in itertools.combinations(zsets[0], 2):
            agree = [j for j in range(3) if z[j] == w[j]]
            if len(agree) != 1:
                break
            shared.append(agree[0])
        if sorted(shared) == [0, 1, 2]:
            return True
    return False


def main():
    out = Path(sys.argv[1])
    out.mkdir(exist_ok=False)
    source = (LANE / 'code/exp_triangle.py').read_bytes()
    require(sha(source) == EXPECTED, 'producer source changed; freeze a new version')
    with (out / 'exp_triangle.py').open('xb') as f:
        f.write(source)
    module = ast.parse(source)
    nodes = [n for n in module.body if isinstance(n, ast.FunctionDef) and n.name == 'triangle_clauses']
    require(len(nodes) == 1, 'ambiguous pure generator')
    ns = {'itertools': itertools}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), '<pinned-triangle_clauses>', 'exec'), ns)
    rows = []
    for sizes in [(2, 2, 2, 2), (2, 3, 4, 5), (2, 6, 6, 6)]:
        V = [list(range(6 - m, 6)) for m in sizes]
        points = list(itertools.product(*V))
        S = SimpleNamespace(V=V, var={p: j + 1 for j, p in enumerate(points)})
        inverse = {j: p for p, j in S.var.items()}
        clauses = ns['triangle_clauses'](S)
        actual = set()
        for c in clauses:
            require(len(c) == 6 and all(type(l) is int and l < 0 for l in c), 'not six negative literals')
            key = tuple(sorted(-l for l in c))
            require(len(set(key)) == 6, 'repeated point')
            require(has_shape([inverse[j] for j in key]), 'wrong agreement shape')
            require(key not in actual, 'duplicate clause')
            actual.add(key)
        expected = declared(S)
        formula = sum(comb(sizes[i], 2) * prod(sizes[k] * (sizes[k] - 1) for k in range(4) if k != i)
                      for i in range(4))
        require(actual == expected and len(actual) == formula, 'written-schema set/count mismatch')
        # Scientific controls: deleting a clause breaks set equality; a six-set of wrong shape is not accepted.
        missing_control = actual - {next(iter(actual))}
        require(missing_control != expected, 'missing-clause control failed')
        bad = next(list(t) for t in itertools.combinations(points, 6) if not has_shape(t))
        require(not has_shape(bad), 'shape-negative control failed')
        rows.append({'sizes': sizes, 'clauses': len(clauses), 'distinct': len(actual),
                     'formula': formula, 'all_shape_valid': True, 'full_set_equals_independent_schema': True,
                     'deleted_clause_rejected': True, 'wrong_six_point_shape_rejected': True})
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'status': 'PASS', 'script_sha256': sha(Path(__file__).read_bytes()),
              'generator_sha256': EXPECTED, 'profiles': rows,
              'all_six_value_formula': 2 * prod(6 * 5 for _ in range(4)),
              'limits': 'Pure W clause-family binding only; no solver/proof replay, J/base/lex binding or AME existence claimed.'}
    with (out / 'result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps(result, indent=1))


if __name__ == '__main__':
    main()

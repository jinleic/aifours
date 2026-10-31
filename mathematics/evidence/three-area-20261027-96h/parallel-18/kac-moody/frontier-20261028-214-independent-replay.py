#!/usr/bin/env python3
"""Independent exact replay of the (2,1,4) symbolic-minor certificates.

Does not import the producer.  Builds free and ideal spans from ALL nested
simple-adjoint words, performs canonical sparse Gauss-Jordan elimination,
and verifies determinant polynomial coefficients by exact interpolation
on a degree-bounding grid.  Output is evidence for review, not a proof
checker for the entire mathematical argument.
"""
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ROOT / 'frontier-20261028-214-symbolic-minors-v1.json'
ALPHA = (2, 1, 4)


def add_scaled(a, b, factor):
    for w, c in b.items():
        value = a.get(w, Q(0)) + factor * c
        if value:
            a[w] = value
        else:
            a.pop(w, None)


def bracket(a, b):
    out = {}
    for w, x in a.items():
        for v, y in b.items():
            out[w + v] = out.get(w + v, Q(0)) + x * y
            out[v + w] = out.get(v + w, Q(0)) - y * x
    return {w: Q(c) for w, c in out.items() if c}


def e(i):
    return {str(i): Q(1)}


def words(counts):
    remaining = list(counts)
    out = []

    def visit(prefix):
        if sum(remaining) == 0:
            out.append(prefix)
            return
        for j in range(3):
            if remaining[j]:
                remaining[j] -= 1
                visit(prefix + str(j + 1))
                remaining[j] += 1

    visit('')
    return out


def nested(word):
    if len(word) == 1:
        return e(int(word))
    return bracket(e(int(word[0])), nested(word[1:]))


def seed(i, j, times):
    result = e(j)
    for _ in range(times):
        result = bracket(e(i), result)
    return result


def formal_ideal_generators(degree, r, s):
    cartan = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    generators = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            exponent = 1 - cartan[i][j]
            deg = [0, 0, 0]
            deg[i] += exponent
            deg[j] += 1
            rest = tuple(degree[k] - deg[k] for k in range(3))
            if min(rest) < 0:
                continue
            base = seed(i + 1, j + 1, exponent)
            for prefix in words(rest):
                v = base
                for a in reversed(prefix):
                    v = bracket(e(int(a)), v)
                generators.append(v)
    return generators


class ReducedSpace:
    """Canonical Gauss-Jordan row span, independently implemented."""
    def __init__(self, vectors=()):
        self.pivots = {}
        for v in vectors:
            self.insert(v)

    def remainder(self, vector):
        result = {k: Q(v) for k, v in vector.items() if v}
        for p in sorted(self.pivots):
            c = result.get(p, 0)
            if c:
                add_scaled(result, self.pivots[p], -c)
        return result

    def insert(self, vector):
        v = self.remainder(vector)
        if not v:
            return False
        p = min(v)
        q = v[p]
        v = {k: value / q for k, value in v.items()}
        for old, row in self.pivots.items():
            if p in row:
                add_scaled(row, v, -row[p])
        self.pivots[p] = v
        return True

    def __len__(self):
        return len(self.pivots)


def lyndon(word):
    return all(word < word[k:] for k in range(1, len(word)))


def standard_bracket(word):
    if len(word) == 1:
        return e(int(word))
    for i in range(1, len(word)):
        if lyndon(word[i:]):
            return bracket(standard_bracket(word[:i]), standard_bracket(word[i:]))
    raise AssertionError(word)


def lower(vector, i, r, s):
    cartan = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    out = {}
    remainder_h = {}
    for word, c in vector.items():
        for k, letter in enumerate(word):
            if int(letter) != i:
                continue
            w = word[:k] + word[k + 1:]
            remainder_h[w] = remainder_h.get(w, Q(0)) - c
            scalar = sum(cartan[i - 1][int(x) - 1] for x in word[k + 1:])
            out[w] = out.get(w, Q(0)) - c * scalar
    assert all(v == 0 for v in remainder_h.values())
    return {w: v for w, v in out.items() if v}


def delta(vector, r, s):
    return {f'{i}:{word}': value
            for i in (1, 2, 3) for word, value in lower(vector, i, r, s).items()}


def determinant(m):
    n = len(m)
    a = [[Q(x) for x in row] for row in m]
    det = Q(1)
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det = -det
        diag = a[j][j]
        det *= diag
        for i in range(j + 1, n):
            if a[i][j]:
                ratio = a[i][j] / diag
                for k in range(j + 1, n):
                    a[i][k] -= ratio * a[j][k]
                a[i][j] = 0
    return det


def eval_polynomial(coefficients, x, y):
    return sum(Q(t['coefficient']) * x ** t['x_power'] * y ** t['y_power']
               for t in coefficients)


def replay(case):
    rclass, sclass = case['r_class'], case['s_class']
    r0 = 4 if rclass == '>=4' else rclass
    s0 = 4 if sclass == '>=4' else sclass
    source = ReducedSpace(nested(w) for w in words(ALPHA))
    ideal_generators = formal_ideal_generators(ALPHA, r0, s0)
    ideal = ReducedSpace(ideal_generators)
    for v in ideal.pivots.values():
        assert not source.remainder(v), 'ideal not contained in full free source'
    m = case['quotient_source_dim']
    assert len(source) - len(ideal) == m, ('source quotient dimension', case)
    if case['status'] == 'ZERO_SOURCE':
        assert m == 0
        return {'r_class': rclass, 's_class': sclass, 'status': 'PASS_ZERO_SOURCE',
                'determinant_checks': 0}
    source_basis = [standard_bracket(w) for w in case['source_basis_lyndon_words']]
    combined = ReducedSpace(ideal_generators)
    for v in source_basis:
        assert not source.remainder(v), 'certificate basis outside source'
        assert combined.insert(v), 'certificate basis dependent modulo ideal'
    assert len(combined) == len(source), 'certificate basis incomplete modulo ideal'
    target_generators = []
    for i in range(3):
        degree = list(ALPHA)
        degree[i] -= 1
        for v in formal_ideal_generators(tuple(degree), r0, s0):
            target_generators.append({f'{i + 1}:{word}': c for word, c in v.items()})
    target = ReducedSpace(target_generators)
    # Lowering maps are affine in each parameter; check ideal stability on a
    # basis and its independent parameter directions.
    testpoints = [(r0, s0)]
    if rclass == '>=4': testpoints.append((r0 + 1, s0))
    if sclass == '>=4': testpoints.append((r0, s0 + 1))
    for r, s in testpoints:
        for v in ideal.pivots.values():
            assert not target.remainder(delta(v, r, s)), 'ideal lowering escaped target ideal'
    rows = case['target_word_pivots']
    assert len(rows) == m and len(set(rows)) == m
    coefficients = case['determinant_coefficients']
    assert Q(next(t['coefficient'] for t in coefficients
                  if t['x_power'] == 0 and t['y_power'] == 0)) != 0
    assert all(Q(t['coefficient']) > 0 for t in coefficients) or all(
        Q(t['coefficient']) < 0 for t in coefficients)
    xs = range(m + 1) if rclass == '>=4' else range(1)
    ys = range(m + 1) if sclass == '>=4' else range(1)
    checks = 0
    for x, y in itertools.product(xs, ys):
        r = r0 + x if rclass == '>=4' else r0
        s = s0 + y if sclass == '>=4' else s0
        columns = [target.remainder(delta(v, r, s)) for v in source_basis]
        mat = [[columns[j].get(row, Q(0)) for j in range(m)] for row in rows]
        assert determinant(mat) == eval_polynomial(coefficients, x, y), (
            'determinant polynomial mismatch', rclass, sclass, x, y)
        checks += 1
    return {'r_class': rclass, 's_class': sclass, 'quotient_source_dim': m,
            'status': 'PASS_EXACT_GRID_AND_SIGN', 'determinant_checks': checks}


def main():
    data = json.loads(CERT.read_text(encoding='utf-8'))
    assert tuple(data['selected_degree']) == ALPHA
    cases = [replay(c) for c in data['cases']]
    assert len(cases) == 16
    out = ROOT / 'frontier-20261028-214-independent-replay-v1.json'
    if out.exists():
        raise FileExistsError(out)
    out.write_text(json.dumps({
        'method': 'independent all-nested-commutator source and ideal spans; canonical exact Gauss-Jordan; degree-bounded determinant interpolation grid',
        'cases': cases,
        'all_classes_passed': True,
        'total_exact_determinant_evaluations': sum(c['determinant_checks'] for c in cases),
        'not_a_formal_proof_or_external_review': True,
    }, indent=2) + '\n', encoding='utf-8')
    print('PASS independent exact replay: 16 parameter classes;',
          sum(c['determinant_checks'] for c in cases), 'determinants;', out.name)


if __name__ == '__main__':
    main()

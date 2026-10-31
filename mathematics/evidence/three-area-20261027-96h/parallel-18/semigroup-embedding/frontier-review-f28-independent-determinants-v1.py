#!/usr/bin/env python3
"""Independent representative exact replay of level-four Lie certificates.

Reads pinned producer JSON only, never imports either author engine/replay.
Builds all right-nested source words, all six seed descendants and exact target
quotients independently. Checks selected actual determinant evaluations only;
all other cases remain outside this check's coverage.
"""
import json
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path

ROOT = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
PINS = {
    'frontier-20261028-214-symbolic-minors-v1.json': '15ee23511638af13eaebe332c3dbad0ec194da1a4c9b59385c41436be4fe0683',
    'frontier-20261028-224-horizontal-minors-v1.json': '08725d2fdcd7b5738e677b04c2ba9b4cbfd374de49505ede4b967282414b91ba',
    'frontier-20261028-224-alternate-minors-v1.json': '46b037e9f5c5f2c57444e71c44200427a3acb55cc6cad14f1262aa01a6b61979',
    'frontier-20261028-predecessor-certificates-v1.json': '39742fa183d9290835e25b29ab246a66e3065d1fecb1c2796210e59dbb8388c2',
    'frontier-20261028-221-horizontal-minors-v1.json': 'aa9f38f92f58303b20d021e4c7102572bdf8239246716ce43f695ea3f2e848d7',
    'frontier-20261028-222-horizontal-minors-v1.json': '94e2bac395862b645f1ef463546ad6e244021a3143e67aa22d59c5f0c30536b9',
    'frontier-20261028-223-horizontal-minors-v1.json': 'a4c58943bb39cd8624faa298ddb087596825db4ef6c183a2cd805ce2807310e2',
}


def ensure(ok, message):
    if not ok:
        raise ValueError(message)


def plus(a, b, scale=1):
    z = dict(a)
    for word, value in b.items():
        z[word] = z.get(word, 0) + scale*value
        if not z[word]:
            del z[word]
    return z


def bracket(a, b):
    z = {}
    for u, cu in a.items():
        for v, cv in b.items():
            z[u+v] = z.get(u+v, 0) + cu*cv
            z[v+u] = z.get(v+u, 0) - cu*cv
    return {w: c for w, c in z.items() if c}


def letter(i):
    return {str(i): Fraction(1)}


def words(counts, prefix=''):
    if sum(counts) == 0:
        yield prefix
    for i, n in enumerate(counts):
        if n:
            new = list(counts)
            new[i] -= 1
            yield from words(tuple(new), prefix + str(i+1))


def nest(word):
    v = letter(int(word[-1]))
    for c in reversed(word[:-1]):
        v = bracket(letter(int(c)), v)
    return v


def lyndon(word):
    return all(word < word[k:] for k in range(1, len(word)))


def standard(word):
    if len(word) == 1:
        return letter(int(word))
    for k in range(1, len(word)):
        if lyndon(word[k:]):
            return bracket(standard(word[:k]), standard(word[k:]))
    raise ValueError(('not Lyndon', word))


def seeds(degree, r, s):
    A = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            power = 1 - A[i][j]
            deg = [0, 0, 0]
            deg[i] += power
            deg[j] += 1
            rest = tuple(degree[k] - deg[k] for k in range(3))
            if min(rest) < 0:
                continue
            base = letter(j+1)
            for _ in range(power):
                base = bracket(letter(i+1), base)
            for sequence in words(rest):
                v = base
                for c in reversed(sequence):
                    v = bracket(letter(int(c)), v)
                yield v


class Space:
    def __init__(self):
        self.pivots = {}

    def rem(self, v):
        out = {k: Fraction(c) for k, c in v.items() if c}
        for p in sorted(self.pivots):
            if p in out:
                out = plus(out, self.pivots[p], -out[p])
        return out

    def add(self, v):
        v = self.rem(v)
        if not v:
            return False
        pivot = min(v)
        coeff = v[pivot]
        v = {k: c/coeff for k, c in v.items()}
        for p in list(self.pivots):
            if pivot in self.pivots[p]:
                self.pivots[p] = plus(self.pivots[p], v, -self.pivots[p][pivot])
        self.pivots[pivot] = v
        return True


def lower(v, node, r, s):
    A = ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))
    scalar, cartan = {}, {}
    for word, coeff in v.items():
        for k, c in enumerate(word):
            if int(c) != node:
                continue
            rest = word[:k]+word[k+1:]
            scalar[rest] = scalar.get(rest, 0) - coeff*sum(A[node-1][int(z)-1] for z in word[k+1:])
            cartan[rest] = cartan.get(rest, 0) - coeff
    ensure(all(v == 0 for v in cartan.values()), ('Cartan term', node))
    return {k: v for k, v in scalar.items() if v}


def delta(v, r, s):
    out = {}
    for i in (1, 2, 3):
        for w, c in lower(v, i, r, s).items():
            out[str(i)+':'+w] = c
    return out


def determinant(mat):
    a = [[Fraction(x) for x in row] for row in mat]
    out = Fraction(1)
    for col in range(len(a)):
        idx = next((i for i in range(col, len(a)) if a[i][col]), None)
        if idx is None:
            return Fraction(0)
        if idx != col:
            a[col], a[idx] = a[idx], a[col]
            out = -out
        p = a[col][col]
        out *= p
        for row in range(col+1, len(a)):
            factor = a[row][col]/p
            for j in range(col+1, len(a)):
                a[row][j] -= factor*a[col][j]
    return out


def polynomial(case, x, y):
    return sum(Fraction(z['coefficient'])*x**z['x_power']*y**z['y_power']
               for z in case['determinant_coefficients'])


def read_pins():
    data = {}
    for name, expected in PINS.items():
        raw = (ROOT/name).read_bytes()
        ensure(sha256(raw).hexdigest() == expected, ('pin mismatch', name))
        data[name] = json.loads(raw)
    return data


def pick(cases, r, s):
    hits = [x for x in cases if x['r_class'] == r and x['s_class'] == s]
    ensure(len(hits) == 1, ('case key', r, s))
    return hits[0]


def replay(degree, case, points, horizontal=False):
    r0 = 4 if case['r_class'] == '>=4' else case['r_class']
    s0 = 4 if case['s_class'] == '>=4' else case['s_class']
    source = Space()
    for word in words(degree):
        source.add(nest(word))
    ideals = list(seeds(degree, r0, s0))
    ideal = Space()
    for v in ideals:
        ensure(not source.rem(v), 'source ideal outside free Lie source')
        ideal.add(v)
    m = case['quotient_source_dim']
    ensure(len(source.pivots) - len(ideal.pivots) == m, ('source quotient dimension', degree, r0, s0))
    if m == 0:
        print('ZERO source', degree, r0, s0, 'source_dim=', len(source.pivots), sep=' ')
        return 0
    basis = [standard(w) for w in case['source_basis_lyndon_words']]
    complement = Space()
    for v in ideals:
        complement.add(v)
    for v in basis:
        ensure(not source.rem(v), 'complement outside source')
        ensure(complement.add(v), 'complement dependent modulo ideal')
    ensure(len(complement.pivots) == len(source.pivots), 'incomplete source complement')

    target = Space()
    for i in range(3):
        d = list(degree)
        d[i] -= 1
        if min(d) < 0:
            continue
        target_source = Space()
        for w in words(tuple(d)):
            target_source.add(nest(w))
        for v in seeds(tuple(d), r0, s0):
            ensure(not target_source.rem(v), 'target ideal outside target')
            target.add({str(i+1)+':'+w: c for w, c in v.items()})

    for x, y in points:
        rr = r0+x if case['r_class'] == '>=4' else r0
        ss = s0+y if case['s_class'] == '>=4' else s0
        for v in ideal.pivots.values():
            ensure(not target.rem(delta(v, rr, ss)), ('ideal lowering unstable', degree, rr, ss))

    if horizontal:
        horizontal_span = Space()
        for v in basis:
            image = target.rem(delta(v, r0, s0))
            horizontal_span.add({k: c for k, c in image.items() if k.startswith(('1:', '2:'))})
        kernel_dim = m - len(horizontal_span.pivots)
        ensure(kernel_dim == case['horizontal_kernel_dim'], ('horizontal dimension', degree, r0, s0))
        if kernel_dim == 0:
            print('ZERO horizontal kernel', degree, r0, s0, 'm=', m, sep=' ')
            return 0
        vectors, coeff_span = [], Space()
        for sparse in case['horizontal_kernel_coefficients']:
            coeff_span.add({k: Fraction(v) for k, v in sparse.items()})
            w = {}
            for j, c in sparse.items():
                w = plus(w, basis[int(j)], Fraction(c))
            out = target.rem(delta(w, r0, s0))
            ensure(not any(k.startswith(('1:', '2:')) for k in out), 'kernel vector escapes')
            vectors.append(w)
        ensure(len(vectors) == kernel_dim == len(coeff_span.pivots), 'incomplete kernel basis')
    else:
        vectors = basis
    rows = case['target_word_pivots']
    ensure(len(rows) == len(vectors) and len(set(rows)) == len(rows), 'invalid minor rows')
    checks = 0
    for x, y in points:
        rr = r0+x if case['r_class'] == '>=4' else r0
        ss = s0+y if case['s_class'] == '>=4' else s0
        images = [target.rem(delta(v, rr, ss)) for v in vectors]
        got = determinant([[col.get(row, 0) for col in images] for row in rows])
        want = polynomial(case, x, y)
        ensure(got == want and got != 0, ('det mismatch', degree, rr, ss, got, want))
        checks += 1
    print('PASS', degree, 'class=', (case['r_class'], case['s_class']),
          'source=', m, 'minor=', len(rows), 'exact_determinants=', checks)
    return checks


def audit_signs(cases, name):
    require_classes = {(r,s) for r in (1,2,3,'>=4') for s in (1,2,3,'>=4')}
    ensure({(c['r_class'], c['s_class']) for c in cases} == require_classes and len(cases) == 16,
           ('class coverage', name))
    for c in cases:
        if c['status'] in ('ZERO_SOURCE', 'ZERO_HORIZONTAL_KERNEL'):
            continue
        poly = c['determinant_coefficients']
        constant = [Fraction(z['coefficient']) for z in poly if z['x_power'] == 0 and z['y_power'] == 0]
        coeffs = [Fraction(z['coefficient']) for z in poly]
        ensure(len(constant) == 1 and constant[0] != 0, ('zero constant', name, c))
        ensure(all(v > 0 for v in coeffs) or all(v < 0 for v in coeffs), ('mixed sign', name, c))


def main():
    data = read_pins()
    d214 = data['frontier-20261028-214-symbolic-minors-v1.json']['cases']
    original224 = data['frontier-20261028-224-horizontal-minors-v1.json']['cases']
    alternatives = data['frontier-20261028-224-alternate-minors-v1.json']['cases']
    replacement = {(c['r_class'],c['s_class']): c for c in alternatives}
    d224 = [replacement.get((c['r_class'],c['s_class']), c) for c in original224]
    audit_signs(d214, '214')
    audit_signs(d224, '224 with alternatives')
    pred = data['frontier-20261028-predecessor-certificates-v1.json']['degrees']
    ensure(len(pred) == 7, 'predecessor degrees')
    for d in pred:
        audit_signs(d['cases'], ('predecessor', d['degree']))
    for n in (1,2,3):
        audit_signs(data[f'frontier-20261028-22{n}-horizontal-minors-v1.json']['cases'], ('central', n))
    print('PASS SHA pins and exact sign/constant/16-class coverage for all 192 degree-class records')
    checks = 0
    checks += replay((2,1,4), pick(d214, 1, 1), [(0,0)])
    checks += replay((2,1,4), pick(d214, 1, 3), [(0,0)])
    checks += replay((2,1,4), pick(d214, 2, '>=4'), [(0,0),(0,1)])
    checks += replay((2,1,4), pick(d214, '>=4', '>=4'), [(0,0),(1,0),(0,1),(1,1)])
    checks += replay((2,2,4), pick(d224, 1, 2), [(0,0)], horizontal=True)
    checks += replay((2,2,4), pick(d224, '>=4', '>=4'), [(0,0),(1,0),(0,1),(1,1)], horizontal=True)
    d203 = next(d['cases'] for d in pred if d['degree'] == [2,0,3])
    checks += replay((2,0,3), pick(d203, 3, 1), [(0,0)])
    d223 = data['frontier-20261028-223-horizontal-minors-v1.json']['cases']
    checks += replay((2,2,3), pick(d223, 1, 1), [(0,0)], horizontal=True)
    print('PASS independent nested-word/seed/target exact representative replay; determinants=', checks, sep='')
    print('LIMIT: representative cases only; no author replay or engine imported; no global machine proof')


if __name__ == '__main__':
    main()

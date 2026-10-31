#!/usr/bin/env python3
"""Independently replay all 192 rectangle certificate classes over Q.

Uses the reviewer's separate tensor-word engine, pinned below, and the original
certificate bytes; imports no author's Python.  Interpolation grid checks are
exact, and sparse output is kept on stdout. No files are created or modified.
"""
import importlib.util
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ENGINE = HERE / 'frontier-review-f28-independent-determinants-v1.py'
ENGINE_PIN = '535e58e04b7d40c86127d0956d8dabe0875e3ff6d67b8d4d6c1515638b0112af'
if sha256(ENGINE.read_bytes()).hexdigest() != ENGINE_PIN:
    raise ValueError('reviewer engine pin mismatch')
spec = importlib.util.spec_from_file_location('f28_review_engine', ENGINE)
ind = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ind)


def ensure(ok, message):
    if not ok:
        raise ValueError(message)


def source_basis(case, degree, ideals):
    labels = case.get('source_basis_lyndon_words')
    if labels is not None:
        return [ind.standard(w) for w in labels]
    # Some zero-horizontal-kernel certificates do not carry source complement
    # labels. Reconstruct a complement independently from all Lyndon words.
    span = ind.Space()
    for v in ideals:
        span.add(v)
    basis = []
    for word in ind.words(degree):
        if ind.lyndon(word):
            v = ind.standard(word)
            if span.add(v):
                basis.append(v)
    return basis


def replay(degree, case, horizontal=False):
    rc, sc = case['r_class'], case['s_class']
    r0, s0 = (4 if rc == '>=4' else rc), (4 if sc == '>=4' else sc)
    source = ind.Space()
    for w in ind.words(degree):
        source.add(ind.nest(w))
    ideals = list(ind.seeds(degree, r0, s0))
    ideal = ind.Space()
    for v in ideals:
        ensure(not source.rem(v), ('source inclusion', degree, rc, sc))
        ideal.add(v)
    m = case['quotient_source_dim']
    ensure(len(source.pivots)-len(ideal.pivots) == m, ('source quotient', degree, rc, sc))
    if m == 0:
        ensure(case['status'] == 'ZERO_SOURCE', ('zero status', degree, rc, sc))
        return 0
    basis = source_basis(case, degree, ideals)
    combined = ind.Space()
    for v in ideals:
        combined.add(v)
    for v in basis:
        ensure(not source.rem(v) and combined.add(v), ('source complement', degree, rc, sc))
    ensure(len(combined.pivots) == len(source.pivots) and len(basis) == m,
           ('source basis coverage', degree, rc, sc))
    target = ind.Space()
    for i in range(3):
        t = list(degree)
        t[i] -= 1
        if min(t) < 0:
            continue
        target_source = ind.Space()
        for w in ind.words(tuple(t)):
            target_source.add(ind.nest(w))
        for v in ind.seeds(tuple(t), r0, s0):
            ensure(not target_source.rem(v), ('target source inclusion', degree, rc, sc, i))
            target.add({str(i+1)+':'+w: c for w, c in v.items()})
    # The derivative depends affinely on r,s, so base and each varying
    # direction prove ideal stability throughout the entire threshold class.
    checks = [(r0,s0)]
    if rc == '>=4': checks.append((r0+1,s0))
    if sc == '>=4': checks.append((r0,s0+1))
    for rr, ss in checks:
        for v in ideal.pivots.values():
            ensure(not target.rem(ind.delta(v, rr, ss)), ('lowering ideal', degree, rc, sc, rr, ss))
    if horizontal:
        span = ind.Space()
        for v in basis:
            row = target.rem(ind.delta(v,r0,s0))
            span.add({k:c for k,c in row.items() if k.startswith(('1:','2:'))})
        k = m-len(span.pivots)
        ensure(k == case['horizontal_kernel_dim'], ('horizontal dimension', degree, rc, sc))
        if k == 0:
            ensure(case['status'] == 'ZERO_HORIZONTAL_KERNEL', ('zero kernel status', degree, rc, sc))
            return 0
        coefficients = case['horizontal_kernel_coefficients']
        coeff_space = ind.Space()
        vectors = []
        for row in coefficients:
            coeff_space.add({str(j):Fraction(c) for j,c in row.items()})
            v = {}
            for j,c in row.items():
                v = ind.plus(v,basis[int(j)],Fraction(c))
            image = target.rem(ind.delta(v,r0,s0))
            ensure(not any(key.startswith(('1:','2:')) for key in image),
                   ('kernel vector', degree, rc, sc))
            vectors.append(v)
        ensure(len(vectors) == k == len(coeff_space.pivots), ('kernel basis', degree, rc, sc))
    else:
        vectors = basis
        k = m
    rows = case['target_word_pivots']
    ensure(len(rows) == k and len(set(rows)) == k, ('pivot count', degree, rc, sc))
    if horizontal:
        ensure(all(row.startswith('3:') for row in rows), ('vertical pivots',degree,rc,sc))
    # Compute each projected matrix at three affine parameter values once.
    matrices = []
    for rr,ss in ((r0,s0),(r0+1,s0),(r0,s0+1)):
        columns = [target.rem(ind.delta(v,rr,ss)) for v in vectors]
        matrices.append([[col.get(row,0) for col in columns] for row in rows])
    xs = range(k+1) if rc == '>=4' else range(1)
    ys = range(k+1) if sc == '>=4' else range(1)
    count = 0
    for x,y in product(xs,ys):
        matrix = [[matrices[0][i][j]
                   +x*(matrices[1][i][j]-matrices[0][i][j])
                   +y*(matrices[2][i][j]-matrices[0][i][j])
                   for j in range(k)] for i in range(k)]
        got = ind.determinant(matrix)
        want = ind.polynomial(case,x,y)
        ensure(got == want and got != 0, ('determinant', degree,rc,sc,x,y,got,want))
        count += 1
    return count


def main():
    data = ind.read_pins()
    d214 = data['frontier-20261028-214-symbolic-minors-v1.json']['cases']
    original224 = data['frontier-20261028-224-horizontal-minors-v1.json']['cases']
    alternatives = data['frontier-20261028-224-alternate-minors-v1.json']['cases']
    replacement = {(c['r_class'],c['s_class']):c for c in alternatives}
    d224 = [replacement.get((c['r_class'],c['s_class']),c) for c in original224]
    groups = [((2,1,4),d214,False), ((2,2,4),d224,True)]
    for rec in data['frontier-20261028-predecessor-certificates-v1.json']['degrees']:
        groups.append((tuple(rec['degree']),rec['cases'],False))
    for n in (1,2,3):
        groups.append(((2,2,n),data[f'frontier-20261028-22{n}-horizontal-minors-v1.json']['cases'],True))
    total_classes = total_det = 0
    for degree,cases,horizontal in groups:
        ind.audit_signs(cases,degree)
        count = sum(replay(degree,c,horizontal) for c in cases)
        total_classes += len(cases)
        total_det += count
        print('PASS degree=',degree,' classes=',len(cases),' determinants=',count,flush=True,sep='')
    ensure(total_classes == 192 and total_det == 516, ('coverage counts',total_classes,total_det))
    print('PASS ALL independent exact replays: 192 classes; 516 rational determinant grid evaluations')
    print('LIMIT: depends on written interpolation/seed-spanning/first-defect arguments and named PBW imports')


if __name__ == '__main__':
    main()

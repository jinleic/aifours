#!/usr/bin/env python3
"""f56 independent reconstruction of the 192 rectangle certificate classes.

Review-side program.  Uses ONLY the review-side original three-generator
model in f56-original-model-crosscheck.py (own Lyndon basis, own six-seed
ideal generation, own tree-Leibniz lowerings, own least-word Gauss/echelon
normal form); no author module is imported.  For every class of
  (2,1,4) and the seven predecessor degrees (full-column m x m minors), and
  (2,2,1),(2,2,2),(2,2,3),(2,2,4) with the two (2,2,4) alternates
    (joint f1/f2 quotient kernel, k x k f3 minors),
it recomputes quotient source dimension, complement validity, target ideal,
horizontal kernel (own nullspace), f3 affineness, the exact symbolic minor
polynomial in Q[x,y] (own determinant), per-variable/total degree <= size,
nonzero constant, one-signedness, direct injectivity ranks at sample points,
and enforces exact degree/class/replacement sets.  `--corrupt` controls.
"""
import argparse
import importlib.util
import itertools
import json
import sys
import time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVID = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody')
spec = importlib.util.spec_from_file_location('own', HERE / 'f56-original-model-crosscheck.py')
own = importlib.util.module_from_spec(spec)
spec.loader.exec_module(own)
CLASSES = [(r, s) for r in (1, 2, 3, '>=4') for s in (1, 2, 3, '>=4')]
CORRUPT = None


def vadd(a, b, c=Q(1)):
    return own.vadd(a, b, c)


class Tracked:
    def __init__(self):
        self.rows = {}
        self.count = 0

    def express(self, v):
        v = {k: Q(x) for k, x in v.items() if x}
        combo = {}
        for p in sorted(self.rows):
            if p in v:
                row, cmb = self.rows[p]
                c = v[p]
                vadd(v, row, -c)
                vadd(combo, cmb, c)
        return v, combo

    def add(self, v):
        idx = self.count
        self.count += 1
        rem, combo = self.express(v)
        if not rem:
            return None
        cmb = {idx: Q(1)}
        vadd(cmb, combo, Q(-1))
        p = min(rem)
        d = rem[p]
        self.rows[p] = ({k: x / d for k, x in rem.items()}, {j: x / d for j, x in cmb.items()})
        return idx


def nullspace(columns):
    tr = Tracked()
    out = []
    for j, col in enumerate(columns):
        rem, combo = tr.express(col)
        if not rem:
            c = {j: Q(1)}
            vadd(c, combo, Q(-1))
            out.append(c)
            tr.count += 1
        else:
            assert tr.add(col) == j
    return out


def rank(vectors):
    return len(own.TriSpan(vectors))


def pmul(p, q):
    out = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            out[(i + k, j + l)] = out.get((i + k, j + l), 0) + a * b
    return {m: c for m, c in out.items() if c}


def pdet(M):
    n = len(M)

    @lru_cache(maxsize=None)
    def rec(i, mask):
        if i == n:
            return {(0, 0): Q(1)}
        out = {}
        pos = 0
        for j in range(n):
            if mask >> j & 1:
                continue
            if M[i][j]:
                vadd(out, pmul(M[i][j], rec(i + 1, mask | (1 << j))), Q(1 if pos % 2 == 0 else -1))
            pos += 1
        return out
    return dict(rec(0, 0))


def poly_from_cert(entries):
    out = {}
    for t in entries:
        key = (int(t['x_power']), int(t['y_power']))
        assert key not in out
        c = Q(t['coefficient'])
        assert c != 0
        out[key] = c
    return out


def target_space(degree, r, s):
    rows = []
    for i in (1, 2, 3):
        d = list(degree)
        d[i - 1] -= 1
        if min(d) < 0:
            continue
        for v in own.ideal_generators(tuple(d), r, s):
            rows.append({(i, w): c for w, c in v.items()})
    return own.TriSpan(rows)


def parse_pivot(txt):
    i, w = txt.split(':')
    return (int(i), tuple(int(ch) for ch in w))


def analyse(degree, case, mode, producer_original=None):
    rc, sc = case['r_class'], case['s_class']
    r0 = 4 if rc == '>=4' else rc
    s0 = 4 if sc == '>=4' else sc
    N = len(own.lyndon_words(degree))
    I = own.TriSpan(own.ideal_generators(degree, r0, s0))
    if rc == '>=4' or sc == '>=4':
        for dr_, ds_ in ((1, 0), (3, 0), (0, 1), (0, 3), (2, 2)):
            if (dr_ and rc != '>=4') or (ds_ and sc != '>=4'):
                continue
            J = own.TriSpan(own.ideal_generators(degree, r0 + dr_, s0 + ds_))
            assert len(J) == len(I) and all(not I.reduce(v) for v in J.rows.values()), ('ideal not constant in class', degree, rc, sc)
    m = N - len(I)
    out = {'r_class': rc, 's_class': sc, 'own_free_dim': N, 'own_ideal_dim': len(I), 'own_source_dim': m}
    assert case['quotient_source_dim'] == m, ('source dim', degree, rc, sc, case['quotient_source_dim'], m)
    if m == 0:
        assert case['status'] == 'ZERO_SOURCE'
        out['own_status'] = 'ZERO_SOURCE'
        return out
    assert case['status'] != 'ZERO_SOURCE'
    if 'source_basis_lyndon_words' not in case:
        # producer omission (disclosed by the author): ZERO_HORIZONTAL_KERNEL records of the
        # (2,2,n) certificates carry no complement labels; k=0 is complement-independent, so
        # build an own Lyndon complement and continue.
        assert case['status'] == 'ZERO_HORIZONTAL_KERNEL' and mode == 'HORIZONTAL', case['status']
        tmp = own.TriSpan(I.rows.values())
        words = [w for w in own.lyndon_words(degree) if tmp.add(own.std_bracket(w)) is not None]
        out['complement_labels_missing_in_producer_record'] = True
    else:
        words = [tuple(int(ch) for ch in w) for w in case['source_basis_lyndon_words']]
    if CORRUPT == 'cert_words':
        words[0] = next(w for w in own.lyndon_words(degree) if w not in words)
    assert len(words) == m == len(set(words))
    comp = own.TriSpan(I.rows.values())
    basis = []
    for w in words:
        assert own.is_lyndon(w) and tuple(w.count(i) for i in (1, 2, 3)) == degree
        v = own.std_bracket(w)
        assert comp.add(v) is not None, ('complement word dependent modulo ideal', w)
        basis.append(v)
    assert len(comp) == N
    T = target_space(degree, r0, s0)
    points = [(r0, s0)]
    if rc == '>=4':
        points += [(r0 + 1, s0), (r0 + 2, s0)]
    if sc == '>=4':
        points += [(r0, s0 + 1), (r0, s0 + 2)]
    if rc == '>=4' and sc == '>=4':
        points += [(r0 + 1, s0 + 1)]
    for r, s in points:
        for v in I.rows.values():
            assert not T.reduce(own.delta(v, degree, r, s)), ('ideal derivative escaped target', degree, rc, sc, r, s)
    cols = {(r, s): [T.reduce(own.delta(v, degree, r, s)) for v in basis] for r, s in points}
    if mode == 'FULL':
        size = m
        vectors = basis
        vcols = cols
        out['direct_full_rank_at_points'] = {f'{r},{s}': rank(cols[(r, s)]) for r, s in points}
        assert all(v == m for v in out['direct_full_rank_at_points'].values()), 'not injective at a sample point'
        assert case['status'] in ('CERTIFIED_ONE_SIGN',), case['status']
    else:
        hor = [{k: c for k, c in col.items() if k[0] in (1, 2)} for col in cols[(r0, s0)]]
        ker = nullspace(hor)
        k = len(ker)
        assert m - rank(hor) == k
        out['own_horizontal_kernel_dim'] = k
        assert case['horizontal_kernel_dim'] == k, ('horizontal kernel dim', degree, rc, sc, case['horizontal_kernel_dim'], k)
        out['direct_quotient_kernel_at_points'] = {f'{r},{s}': m - rank(cols[(r, s)]) for r, s in points}
        assert all(v == 0 for v in out['direct_quotient_kernel_at_points'].values()), 'nonzero direct kernel'
        if k == 0:
            assert case['status'] == 'ZERO_HORIZONTAL_KERNEL'
            out['own_status'] = 'ZERO_HORIZONTAL_KERNEL'
            return out
        coeffs = [{int(j): Q(c) for j, c in row.items()} for row in case['horizontal_kernel_coefficients']]
        if CORRUPT == 'cert_kernel':
            j0 = next(iter(coeffs[0]))
            coeffs[0][j0] += 1
        assert len(coeffs) == k and rank(coeffs) == k
        assert rank(coeffs + ker) == k, 'certificate kernel is not the own kernel'
        vectors = []
        for row in coeffs:
            v = {}
            for j, c in row.items():
                vadd(v, basis[j], c)
            vectors.append(v)
        vcols = {}
        for r, s in points:
            vcols[(r, s)] = []
            for v in vectors:
                col = T.reduce(own.delta(v, degree, r, s))
                assert not {q: c for q, c in col.items() if q[0] in (1, 2)}, 'kernel vector not horizontal-singular'
                vcols[(r, s)].append(col)
        size = k
    base = vcols[(r0, s0)]
    dr = [dict() for _ in range(size)]
    ds = [dict() for _ in range(size)]
    if rc == '>=4':
        for q in range(size):
            dr[q] = vadd(dict(vcols[(r0 + 1, s0)][q]), base[q], Q(-1))
            assert not vadd(vadd(dict(vcols[(r0 + 2, s0)][q]), vcols[(r0 + 1, s0)][q], Q(-2)), base[q]), 'not affine in r'
    if sc == '>=4':
        for q in range(size):
            ds[q] = vadd(dict(vcols[(r0, s0 + 1)][q]), base[q], Q(-1))
            assert not vadd(vadd(dict(vcols[(r0, s0 + 2)][q]), vcols[(r0, s0 + 1)][q], Q(-2)), base[q]), 'not affine in s'
    if rc == '>=4' and sc == '>=4':
        for q in range(size):
            assert not vadd(vadd(vadd(dict(vcols[(r0 + 1, s0 + 1)][q]), vcols[(r0 + 1, s0)][q], Q(-1)), vcols[(r0, s0 + 1)][q], Q(-1)), base[q]), 'bilinear term'
    if mode == 'FULL':
        # rows 1,2 (f1,f2) must not depend on r,s at all
        for q in range(size):
            assert not {key for key in dr[q] if key[0] != 3} and not {key for key in ds[q] if key[0] != 3}, 'f1/f2 entries vary with r,s'

    def minor_poly(pivtexts):
        rows = [parse_pivot(t) for t in pivtexts]
        assert len(rows) == size == len(set(rows))
        if mode != 'FULL':
            assert all(i == 3 for i, _ in rows)
        for key in rows:
            assert any(key in base[q] or key in dr[q] or key in ds[q] for q in range(size)), ('pivot absent', key)
        M = [[{mon: c for mon, c in (((0, 0), base[q].get(key, 0)), ((1, 0), dr[q].get(key, 0)), ((0, 1), ds[q].get(key, 0))) if c} for q in range(size)] for key in rows]
        return pdet(M)
    pivots = list(case['target_word_pivots'])
    if CORRUPT == 'cert_pivot':
        used = {parse_pivot(t) for t in pivots}
        cand = sorted({key for q in range(size) for key in base[q]} - used)
        pivots[0] = f'{cand[0][0]}:' + ''.join(map(str, cand[0][1]))
    poly = minor_poly(pivots)
    cpoly = poly_from_cert(case['determinant_coefficients'])
    if CORRUPT == 'cert_sign' and len(cpoly) >= 2:
        key = max(cpoly)
        cpoly[key] = -cpoly[key]
    assert poly == cpoly, ('polynomial mismatch', degree, rc, sc)
    const = poly.get((0, 0), 0)
    assert const != 0
    signs = {1 if c > 0 else -1 for c in poly.values()}
    maxx = max(i for i, _ in poly)
    maxy = max(j for _, j in poly)
    maxt = max(i + j for i, j in poly)
    assert maxx <= size and maxy <= size and maxt <= size, ('degree bound', degree, rc, sc)
    if rc != '>=4':
        assert maxx == 0
    if sc != '>=4':
        assert maxy == 0
    grid = 0
    for xg, yg in itertools.product(range(size + 1) if rc == '>=4' else range(1), range(size + 1) if sc == '>=4' else range(1)):
        r, s = r0 + xg, s0 + yg
        rows = [parse_pivot(t) for t in pivots]
        numeric = [T.reduce(own.delta(v, degree, r, s)) for v in vectors]
        mat = [[{(0, 0): numeric[q].get(key, 0)} if numeric[q].get(key, 0) else {} for q in range(size)] for key in rows]
        assert pdet(mat).get((0, 0), 0) == sum(c * Q(xg) ** i * Q(yg) ** j for (i, j), c in poly.items()), ('grid', degree, rc, sc, xg, yg)
        grid += 1
    out.update({'size': size, 'own_polynomial': {f'{i},{j}': str(c) for (i, j), c in sorted(poly.items())}, 'constant': str(const),
                'one_signed': len(signs) == 1, 'max_x_degree': maxx, 'max_y_degree': maxy, 'max_total_degree': maxt, 'grid_points': grid})
    if case['status'] == 'MIXED_SIGNS_NEEDS_ANALYSIS':
        assert len(signs) == 2
        out['own_status'] = 'MIXED_SIGNS_CONFIRMED_NOT_A_CERTIFICATE'
        return out
    assert len(signs) == 1, ('mixed signs in certified class', degree, rc, sc)
    out['own_status'] = 'CERTIFIED_ONE_SIGN_OWN'
    if producer_original is not None:
        opoly = minor_poly(producer_original['target_word_pivots'])
        assert opoly == poly_from_cert(producer_original['determinant_coefficients'])
        assert len({1 if c > 0 else -1 for c in opoly.values()}) == 2, 'original minor was not mixed'
        assert set(producer_original['target_word_pivots']) != set(pivots)
        out['replaced_producer_minor'] = {'pivots': producer_original['target_word_pivots'], 'mixed_confirmed': True, 'alternate_pivots': pivots}
    return out


def main():
    global CORRUPT
    ap = argparse.ArgumentParser()
    ap.add_argument('--corrupt', default=None)
    ap.add_argument('--only', default=None)
    ap.add_argument('--output', default=None)
    args = ap.parse_args()
    CORRUPT = args.corrupt
    t0 = time.time()
    jobs = []
    d = json.loads((EVID / 'frontier-20261028-214-symbolic-minors-v1.json').read_text())
    assert tuple(d['selected_degree']) == (2, 1, 4)
    jobs.append(((2, 1, 4), d['cases'], 'FULL', {}))
    d = json.loads((EVID / 'frontier-20261028-predecessor-certificates-v1.json').read_text())
    assert [tuple(x['degree']) for x in d['degrees']] == [(2, 0, 1), (2, 0, 2), (2, 0, 3), (2, 0, 4), (2, 1, 1), (2, 1, 2), (2, 1, 3)]
    for x in d['degrees']:
        jobs.append((tuple(x['degree']), x['cases'], 'FULL', {}))
    for name in ('221', '222', '223', '224'):
        d = json.loads((EVID / f'frontier-20261028-{name}-horizontal-minors-v1.json').read_text())
        assert tuple(d['degree']) == tuple(int(ch) for ch in name)
        alt = {}
        if name == '224':
            a = json.loads((EVID / 'frontier-20261028-224-alternate-minors-v1.json').read_text())
            alt = {(c['r_class'], c['s_class']): c for c in a['cases']}
            mixed = {(c['r_class'], c['s_class']) for c in d['cases'] if c['status'] == 'MIXED_SIGNS_NEEDS_ANALYSIS'}
            assert set(alt) == mixed == {('>=4', 3), ('>=4', '>=4')} and len(a['cases']) == 2
            for key, c in alt.items():
                assert c['status'] == 'CERTIFIED_ONE_SIGN_ALTERNATE'
                base = next(b for b in d['cases'] if (b['r_class'], b['s_class']) == key)
                for f in ('quotient_source_dim', 'horizontal_kernel_dim', 'source_basis_lyndon_words', 'horizontal_kernel_coefficients'):
                    assert c[f] == base[f]
        else:
            assert all(c['status'] != 'MIXED_SIGNS_NEEDS_ANALYSIS' for c in d['cases'])
        jobs.append((tuple(d['degree']), d['cases'], 'HORIZONTAL', alt))
    assert len(jobs) == 12
    only = tuple(int(x) for x in args.only.split(',')) if args.only else None
    blocks = []
    totals = {'classes': 0, 'zero_source': 0, 'zero_horizontal': 0, 'certified': 0, 'grid_points': 0}
    for degree, cases, mode, alt in jobs:
        if only and degree != only:
            continue
        assert [(c['r_class'], c['s_class']) for c in cases] == CLASSES, ('class set/order', degree)
        rows = []
        for c in cases:
            key = (c['r_class'], c['s_class'])
            cert = c if CORRUPT == 'use_original_mixed' else alt.get(key, c)
            rec = analyse(degree, cert, mode, producer_original=c if (key in alt and CORRUPT != 'use_original_mixed') else None)
            st = rec['own_status']
            totals['classes'] += 1
            if st == 'ZERO_SOURCE':
                totals['zero_source'] += 1
            elif st == 'ZERO_HORIZONTAL_KERNEL':
                totals['zero_horizontal'] += 1
            elif st == 'CERTIFIED_ONE_SIGN_OWN':
                totals['certified'] += 1
                totals['grid_points'] += rec['grid_points']
            else:
                raise AssertionError(('unexpected own status', st))
            rows.append(rec)
            print('OK', degree, mode, key, st, 'm', rec['own_source_dim'], 'k', rec.get('own_horizontal_kernel_dim', '-'), flush=True)
        blocks.append({'degree': list(degree), 'mode': mode, 'classes': rows})
    result = {'corrupt': CORRUPT, 'blocks': blocks, 'totals': totals, 'elapsed_seconds': round(time.time() - t0, 2), 'python': sys.version}
    if not CORRUPT:
        out = Path(args.output) if args.output else HERE / 'f56-rectangle-independent-verifier-result-v1.json'
        with open(out, 'x', encoding='utf-8') as fh:
            fh.write(json.dumps(result, indent=1, default=str) + '\n')
        print('WROTE', out.name)
    print('ALL CHECKS PASSED', totals, 'elapsed', result['elapsed_seconds'], 's')


if __name__ == '__main__':
    main()

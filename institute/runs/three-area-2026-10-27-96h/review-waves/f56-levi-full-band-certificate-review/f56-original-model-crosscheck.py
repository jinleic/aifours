#!/usr/bin/env python3
"""f56 original three-generator cross-model check (review-side, no author imports).

Own implementation of the ORIGINAL preliminary positive free Lie algebra on
e1,e2,e3 (tensor embedding, Lyndon basis), the FULL six-seed positive Serre
ideal at a degree and at its three lowering targets (all iterated simple
adjoints of all six seeds), the three actual lowerings [f_i, .] computed by
tree Leibniz on Lyndon standard factorizations using only
[f_i,e_j]=-delta_ij h_i and [h_i,x]=alpha(h_i)x, and the simultaneous quotient
kernel dim = N - rank(Delta mod T) - dim I.  Also the actual joint f1/f2
quotient kernel dimension.  Results are compared with the eight-letter
Levi-model class values (source dim m, horizontal kernel dim k) of the
certificate; kernel must be 0.  This is finite sampled corroboration of the
free-Levi source identification at the critical degrees -- including (3,3,4),
which the author's own original-vs-Levi comparisons did not cover -- not a
proof for unbounded parameters.
"""
import argparse
import itertools
import json
import sys
import time
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261028-levi-critical-minors-v1.json')


def vadd(a, b, c=Q(1)):
    for k, x in b.items():
        y = a.get(k, 0) + c * x
        if y:
            a[k] = y
        else:
            a.pop(k, None)
    return a


class TriSpan:
    """Triangular echelon span with least-key pivots (own implementation)."""

    def __init__(self, vectors=()):
        self.rows = {}
        for v in vectors:
            self.add(v)

    def reduce(self, v):
        v = {k: Q(x) for k, x in v.items() if x}
        for p in sorted(self.rows):
            if p in v:
                vadd(v, self.rows[p], -v[p])
        return v

    def add(self, v):
        v = self.reduce(v)
        if not v:
            return None
        p = min(v)
        d = v[p]
        self.rows[p] = {k: x / d for k, x in v.items()}
        return p

    def __len__(self):
        return len(self.rows)


def tbr(a, b):
    out = {}
    for w, x in a.items():
        for u, y in b.items():
            out[w + u] = out.get(w + u, 0) + x * y
            out[u + w] = out.get(u + w, 0) - x * y
    return {w: Q(c) for w, c in out.items() if c}


def letter(i):
    return {(i,): Q(1)}


def is_lyndon(w):
    return all(w < w[k:] for k in range(1, len(w)))


@lru_cache(maxsize=None)
def split(w):
    return next(i for i in range(1, len(w)) if is_lyndon(w[i:]))


@lru_cache(maxsize=None)
def std_bracket(w):
    if len(w) == 1:
        return letter(w[0])
    i = split(w)
    res = tbr(std_bracket(w[:i]), std_bracket(w[i:]))
    assert res.get(w) == 1 and min(res) == w
    return res


def words_counts(counts):
    letters = [i + 1 for i in range(3) for _ in range(counts[i])]
    return sorted(set(itertools.permutations(letters)))


@lru_cache(maxsize=None)
def lyndon_words(degree):
    return tuple(w for w in words_counts(degree) if is_lyndon(w))


def cartan(r, s):
    return ((2, -1, -1), (-1, 2, -1), (-r, -s, 2))


def rootval(w, i, A):
    return sum(w.count(j + 1) * A[i - 1][j] for j in range(3))


def seed(i, j, exponent):
    v = letter(j)
    for _ in range(exponent):
        v = tbr(letter(i), v)
    return v


def seeds(r, s):
    A = cartan(r, s)
    out = []
    for i in range(3):
        for j in range(3):
            if i != j:
                e = 1 - A[i][j]
                d = [0, 0, 0]
                d[i] += e
                d[j] += 1
                out.append((seed(i + 1, j + 1, e), tuple(d)))
    return out


def ideal_generators(degree, r, s):
    out = []
    for poly, sdeg in seeds(r, s):
        rest = tuple(degree[k] - sdeg[k] for k in range(3))
        if min(rest) < 0:
            continue
        for prefix in words_counts(rest):
            v = poly
            for a in reversed(prefix):
                v = tbr(letter(a), v)
            if v:
                out.append(v)
    return out


@lru_cache(maxsize=None)
def D_tree(w, i, r, s):
    """[f_i, std_bracket(w)]: (coefficient of h_i, positive polynomial)."""
    A = cartan(r, s)
    if len(w) == 1:
        return (Q(-1) if w[0] == i else Q(0)), {}
    k = split(w)
    L, R = w[:k], w[k:]
    cL, pL = D_tree(L, i, r, s)
    cR, pR = D_tree(R, i, r, s)
    out = {}
    if cL:
        vadd(out, std_bracket(R), cL * rootval(R, i, A))
    if pL:
        vadd(out, tbr(pL, std_bracket(R)))
    if cR:
        vadd(out, std_bracket(L), -cR * rootval(L, i, A))
    if pR:
        vadd(out, tbr(std_bracket(L), pR))
    return Q(0), out


def lyndon_coordinates(vec, degree):
    rem = {w: Q(c) for w, c in vec.items() if c}
    coords = {}
    for w in lyndon_words(degree):
        c = rem.get(w, 0)
        if c:
            coords[w] = c
            vadd(rem, std_bracket(w), -c)
    assert not rem, 'vector is not a Lie element of this degree'
    return coords


def lower(vec, degree, i, r, s):
    out = {}
    for w, c in lyndon_coordinates(vec, degree).items():
        ch, p = D_tree(w, i, r, s)
        assert ch == 0, 'length>=2 input gave a Cartan term'
        vadd(out, p, c)
    return out


def delta(vec, degree, r, s):
    out = {}
    for i in (1, 2, 3):
        if degree[i - 1] == 0:
            continue
        out.update({(i, w): c for w, c in lower(vec, degree, i, r, s).items()})
    return out


def run(degree, r, s):
    t0 = time.time()
    basis_words = lyndon_words(degree)
    N = len(basis_words)
    source_span = TriSpan(std_bracket(w) for w in basis_words)
    assert len(source_span) == N
    I = TriSpan(ideal_generators(degree, r, s))
    for row in I.rows.values():
        assert not source_span.reduce(row), 'ideal outside free source'
    rows = []
    for i in (1, 2, 3):
        d = list(degree)
        d[i - 1] -= 1
        if min(d) < 0:
            continue
        for v in ideal_generators(tuple(d), r, s):
            rows.append({(i, w): c for w, c in v.items()})
    T = TriSpan(rows)
    for row in I.rows.values():
        assert not T.reduce(delta(row, degree, r, s)), 'ideal derivative escaped target ideal'
    cols = [T.reduce(delta(std_bracket(w), degree, r, s)) for w in basis_words]
    rho = len(TriSpan(cols))
    m = N - len(I)
    kernel = m - rho
    hor = [{k: c for k, c in col.items() if k[0] in (1, 2)} for col in cols]
    # joint horizontal kernel on the quotient: m - rank of horizontal columns modulo... columns already reduced mod T;
    # the horizontal map on F/I: rank over the full source equals rank over quotient since Delta(I) subset T.
    rho_h = len(TriSpan(hor))
    k_h = m - rho_h
    return {'degree': list(degree), 'r': r, 's': s, 'free_dim': N, 'ideal_dim': len(I), 'quotient_source_dim': m,
            'target_ideal_dim': len(T), 'delta_mod_target_rank': rho, 'simultaneous_quotient_kernel_dim': kernel,
            'joint_horizontal_quotient_kernel_dim': k_h, 'seconds': round(time.time() - t0, 1)}


def cls(x):
    return '>=4' if x >= 4 else x


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cases', default='324:1,1;324:2,2;324:4,4;333:1,1;333:2,3;333:4,4;334:1,1;334:1,2;334:2,2;334:2,3;334:3,3;334:4,4;334:5,5')
    ap.add_argument('--output', default=None)
    args = ap.parse_args()
    cert = json.loads(CERT.read_text(encoding='utf-8'))
    expected = {}
    for b in cert['degrees']:
        for c in b['cases']:
            expected[(tuple(b['degree']), c['r_class'], c['s_class'])] = (c['source_dim'], c['horizontal_kernel_dim'])
    results = []
    for item in args.cases.split(';'):
        dtxt, rs = item.split(':')
        degree = tuple(int(ch) for ch in dtxt)
        r, s = (int(x) for x in rs.split(','))
        rec = run(degree, r, s)
        m_exp, k_exp = expected[(degree, cls(r), cls(s))]
        rec['levi_model_class'] = [cls(r), cls(s)]
        rec['levi_model_source_dim'] = m_exp
        rec['levi_model_horizontal_kernel_dim'] = k_exp
        rec['source_dim_matches_levi_model'] = rec['quotient_source_dim'] == m_exp
        rec['horizontal_kernel_matches_levi_model'] = rec['joint_horizontal_quotient_kernel_dim'] == k_exp
        print(json.dumps(rec), flush=True)
        assert rec['source_dim_matches_levi_model'], ('source dim mismatch', rec)
        assert rec['horizontal_kernel_matches_levi_model'], ('horizontal kernel mismatch', rec)
        assert rec['simultaneous_quotient_kernel_dim'] == 0, ('nonzero original kernel', rec)
        results.append(rec)
    out = Path(args.output) if args.output else HERE / 'f56-original-model-crosscheck-result-v1.json'
    with open(out, 'x', encoding='utf-8') as fh:
        fh.write(json.dumps({'cases': results, 'python': sys.version,
                             'scope': 'own original three-generator model; finite sampled corroboration only'}, indent=1) + '\n')
    print('PASS', len(results), 'original-model cases; WROTE', out.name)


if __name__ == '__main__':
    main()

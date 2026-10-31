#!/usr/bin/env python3
"""Bounded matrix/resultant-only independent replay for the level-six invariant.

The full tree-Jacobi source replay is separate. This script reads the pinned
20-column pencil and producer's factor/resultant tables, checks both minors on
all shifted unisolvent grid points, and certifies the exact resultant by all
362 unisolvent specializations with direct integer Sylvester determinants.
It then supplies an independently computed Hensel/Cauchy list of integer fibres.
It imports only the standard library and the independently authored arithmetic
functions from the general replay (not the producer).
"""
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('independent_arithmetic', ROOT / 'frontier-20261028-level6-two-minor-general-replay.py')
r = importlib.util.module_from_spec(sp)
sp.loader.exec_module(r)


def main():
    name = 'frontier-20261028-level6-666-two-minor-certificate-v1.json'
    raw = (ROOT / name).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == 'a59569fdecaff1c7c81a7c6d28b48ee8548d5ccbdc1107a145ede26d452a19ef'
    C = json.loads(raw)
    pbytes = (ROOT / C['pencil']).read_bytes()
    assert hashlib.sha256(pbytes).hexdigest() == C['pencil_sha256']
    P = json.loads(pbytes)
    # A new row 04657 is not serialized by the pencil. Its affine entries must
    # be independently reconstructed; only 20 source combinations are used,
    # without the costly full 2520-column horizontal-rank reconstruction.
    degree = tuple(C['degree'])
    basis = [r.ind.ind.standard_bracket(w) for w in P['source_words']]
    vectors = [r.ind.combine(basis, co) for co in P['horizontal_kernel_coefficients']]
    aa = [r.ind.d3(v, degree, 6, 6) for v in vectors]
    bb = [r.ind.d3(v, degree, 7, 6) for v in vectors]
    cc = [r.ind.d3(v, degree, 6, 7) for v in vectors]
    target = sorted(set(w for z in aa + bb + cc for w in z))
    rows = {w: [[aa[j].get(w, 0), bb[j].get(w, 0) - aa[j].get(w, 0), cc[j].get(w, 0) - aa[j].get(w, 0)]
                for j in range(20)] for w in target}
    bad = []
    count = 0
    for label, words in (('P1', C['selected_rows']), ('P2', C['second_minor_rows'])):
        F = C['minor_factorizations'][label]
        polynomial = {(0, 0): Q(F['content'])}
        for entry in F['factors']:
            f = r.poly(entry)
            positive = f.get((0, 0), 0) != 0 and (all(c > 0 for c in f.values()) or all(c < 0 for c in f.values()))
            assert positive == entry['strictly_positive_on_quadrant']
            if not positive:
                bad.append(f)
            for _ in range(entry['multiplicity']):
                polynomial = r.mul(polynomial, f)
        assert max(i + j for i, j in polynomial) <= 20
        mat = [[[Q(v) for v in e] for e in rows[w]] for w in words]
        scales = [math.lcm(*(q.denominator for e in row for q in e)) for row in mat]
        data = [[[int(v * scale) for v in e] for e in row] for row, scale in zip(mat, scales)]
        for i in range(21):
            for j in range(21 - i):
                xv, yv = i - 3, j + 2
                det = r.bareiss([[a + xv * b + yv * c for a, b, c in row] for row in data])
                assert Q(det, math.prod(scales)) == sum(c * xv**u * yv**v for (u, v), c in polynomial.items())
                count += 1
    assert len(bad) == 2
    H = [int(c) for c in C['bad_pairs'][0]['resultant_coefficients_low_to_high']]
    def spec(poly, y0):
        n = max(i for i, j in poly)
        out = [Q(0)] * (n + 1)
        for (i, j), c in poly.items():
            out[i] += c * y0**j
        assert all(v.denominator == 1 for v in out)
        return [int(v) for v in out]
    for f in bad:
        n = max(i for i, j in f)
        assert all(j == 0 for (i, j) in f if i == n)
    for y0 in range(362):
        assert r.bareiss(r.sylvester(spec(bad[0], y0), spec(bad[1], y0))) == r.ev(H, y0)
    W = [Q(v) for v in H]
    linears = C['bad_pairs'][0]['repeated_part_linear_factors_a_t_plus_b_mult_in_H']
    for a, b, m in linears:
        for _ in range(m):
            q = [Q(0)] * (len(W) - 1)
            work = W[:]
            for i in range(len(W) - 1, 0, -1):
                q[i - 1] = work[i] / a
                work[i - 1] -= q[i - 1] * b
            assert work[0] == 0
            W = q
    assert all(c.denominator == 1 for c in W)
    W = [int(c) for c in W]
    dW = [i * c for i, c in enumerate(W)][1:]
    p = 5003
    assert all(p % d for d in range(2, math.isqrt(p) + 1)) and W[-1] % p
    assert len(r.gcd_modp(W, dW, p)) == 1
    bound = 1 + (max(abs(c) for c in W[:-1]) + abs(W[-1]) - 1) // abs(W[-1])
    modulus = p
    while modulus <= 2 * bound:
        modulus *= p
    integers = []
    for a in [a for a in range(p) if r.ev(W, a, p) == 0]:
        for _ in range(64):
            if r.ev(W, a, modulus) == 0:
                break
            a = (a - r.ev(W, a, modulus) * pow(r.ev(dW, a, modulus), -1, modulus)) % modulus
        assert r.ev(W, a, modulus) == 0
        symmetric = a if a <= modulus // 2 else a - modulus
        if abs(symmetric) <= bound and r.ev(W, symmetric) == 0:
            integers.append(symmetric)
    roots = sorted(set(integers) | {-b // a for a, b, _ in linears if b % a == 0})
    assert roots == [-6, -5, -4]
    out = ROOT / 'frontier-20261028-level6-666-matrix-replay-v1.json'
    with out.open('x') as stream:
        json.dump({'certificate_sha256': sha, 'degree': [6, 6, 6], 'source_combinations': 20,
                   'shifted_grid_exact_minor_checks': count, 'exact_integer_sylvester_checks': 362,
                   'hensel_prime': p, 'integer_resultant_roots': roots,
                   'status': 'PASS_MATRIX_AND_RESULTANT_CERTIFICATE',
                   'limits': 'does NOT reconstruct the full 2520-column horizontal rank or actual Lie source identification'}, stream, indent=2)
        stream.write('\n')
    print('PASS 666 matrix/minors/resultant replay', count, 362, roots, out.name)


if __name__ == '__main__':
    main()

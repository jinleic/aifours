#!/usr/bin/env python3
"""Strict standard-library replay of a finite cofinite-pair algebra certificate.

Does not import FLINT, SymPy, a producer, or a determinant algorithm. It checks
exact rational coefficient convolution back to BOTH pinned stored minors and an
exhaustive modular Bezout identity certifying residual coprimality. The stored
minors' equality to actual matrix determinants and actual source identification
are deliberately separate gates, not certified by this checker.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class CertificateError(Exception):
    pass


def require(test, reason):
    if not test:
        raise CertificateError(reason)


def parse_terms(rows):
    result = {}
    for row in rows:
        require(set(row) == {'x_power', 'y_power', 'coefficient'}, 'bad term fields')
        i, j = row['x_power'], row['y_power']
        require(type(i) is int and type(j) is int and i >= 0 and j >= 0, 'invalid exponents')
        require((i, j) not in result, 'duplicate exponent')
        c = Fraction(row['coefficient'])
        require(c != 0, 'explicit zero term')
        result[i, j] = c
    require(bool(result), 'zero polynomial')
    return result


def mul(a, b):
    result = {}
    for (i, j), c in a.items():
        for (k, ell), d in b.items():
            key = (i + k, j + ell)
            result[key] = result.get(key, 0) + c * d
    return {key: c for key, c in result.items() if c}


def one_variable_mul(a, b, p):
    result = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            result[i + j] = (result[i + j] + c * d) % p
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--certificate', required=True)
    ap.add_argument('--sha256', required=True)
    args = ap.parse_args()
    path = ROOT / args.certificate
    raw = path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == args.sha256, 'certificate SHA mismatch')
    C = json.loads(raw)
    require(len(C['inputs']) == len(C['decompositions']) == 2, 'pair cardinality')
    A, B = parse_terms(C['residual_A']), parse_terms(C['residual_B'])
    F = parse_terms(C['positive_common_factor'])
    require(all(v.denominator == 1 for p in (A, B, F) for v in p.values()), 'noninteger residual coefficient')
    fc = list(F.values())
    require(F.get((0, 0), 0) and (all(c > 0 for c in fc) or all(c < 0 for c in fc)), 'common factor is not strictly one-sign')
    degrees = []
    axes = []
    counts = []
    for k, residual in enumerate((A, B)):
        pin = C['inputs'][k]
        require(Path(pin['minor']).name == pin['minor'], 'minor path not owner-local')
        mraw = (ROOT / pin['minor']).read_bytes()
        require(hashlib.sha256(mraw).hexdigest() == pin['sha256'], 'minor SHA mismatch')
        M = json.loads(mraw)
        require(M['degree'] == C['degree'], 'degree identity mismatch')
        require(M['pencil_sha256'] == pin['pencil_sha256'], 'pencil reference mismatch')
        actual = parse_terms(M['coefficients'])
        rebuilt = mul(residual, F)
        d = C['decompositions'][k]
        scalar = Fraction(d['scale'])
        require(scalar != 0, 'zero scale')
        for lin in d['positive_linear_factors']:
            idx, const, exponent = lin['variable_index'], lin['constant'], lin['exponent']
            require(type(idx) is int and idx in (0, 1), 'invalid linear variable')
            require(type(const) is int and const > 0 and type(exponent) is int and exponent > 0, 'linear factor not strictly positive')
            factor = {(1, 0) if idx == 0 else (0, 1): 1, (0, 0): const}
            for _ in range(exponent):
                rebuilt = mul(rebuilt, factor)
        require({m: scalar * c for m, c in rebuilt.items()} == actual, 'minor reconstruction fails')
        dx = max(i for i, j in residual)
        leading = {m: c for m, c in residual.items() if m[0] == dx}
        require(len(leading) == 1 and (dx, 0) in leading, 'nonconstant x-leading coefficient')
        require(str(leading[dx, 0]) == C['x_leading_constants'][k], 'leading constant mismatch')
        degrees.append(max(i + j for i, j in residual))
        ax = [0] * (dx + 1)
        for (i, j), c in residual.items():
            if j == 0:
                ax[i] += int(c)
        axes.append(ax)
        counts.append(len(actual))
    require(C['inputs'][0]['pencil_sha256'] == C['inputs'][1]['pencil_sha256'], 'pair uses different pencils')
    Z = C['axis_coprimality']
    require(Z['fixed_y'] == 0, 'unsupported specialization')
    p = Z['prime']
    require(type(p) is int and p >= 2 and all(p % d for d in range(2, math.isqrt(p) + 1)), 'modulus not prime')
    require(all(ax[-1] % p for ax in axes), 'axis degree drop mod prime')
    u, v = Z['bezout_u'], Z['bezout_v']
    require(all(type(c) is int and 0 <= c < p for c in u + v), 'bad Bezout coefficients')
    ua, vb = one_variable_mul(u, axes[0], p), one_variable_mul(v, axes[1], p)
    size = max(len(ua), len(vb))
    ua += [0] * (size - len(ua))
    vb += [0] * (size - len(vb))
    total = [(a + b) % p for a, b in zip(ua, vb)]
    require(total[0] == 1 and all(c == 0 for c in total[1:]), 'full Bezout identity fails')
    require(degrees == C['residual_total_degrees'], 'residual degree mismatch')
    bound = degrees[0] * degrees[1]
    require(bound == C['bezout_bound_on_exceptional_complex_pairs'], 'Bezout bound mismatch')
    out = path.with_name(path.name.replace('-algebra-v1.json', '-algebra-independent-replay-v1.json'))
    require(out != path, 'bad output suffix')
    result = {'certificate': args.certificate, 'certificate_sha256': args.sha256,
              'stored_minor_coefficient_counts': counts, 'exact_coefficient_products_checked': 2,
              'axis_prime': p, 'all_Bezout_coefficients_checked': size,
              'residual_degrees': degrees, 'exceptional_complex_pair_bound': bound,
              'status': 'PASS_EXACT_RESIDUAL_PAIR_RECONSTRUCTION_AND_COPRIMALITY',
              'scope': 'stored polynomial algebra only; determinant/source reconstruction is NOT supplied',
              'engine': 'Python standard-library integers and fractions.Fraction only'}
    with out.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print('PASS cofinite-pair polynomial replay', degrees, 'exception bound', bound, out.name, flush=True)


if __name__ == '__main__':
    main()

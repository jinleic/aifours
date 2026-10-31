#!/usr/bin/env python3
"""Independent standard-library replay of all fourteen positive boundary proofs.

Reconstructs both original minor polynomials from pinned coefficient/factor
sources without FLINT or producer imports. Checks exact univariate products,
all coefficients of the shifted positive gcd, degree preservation and every
coefficient of the finite-field Bezout identity. No root-finding black box.
"""
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def terms(rows):
    out = {}
    for e in rows:
        mon = e['x_power'], e['y_power']
        assert mon not in out and all(type(i) is int and i >= 0 for i in mon)
        q = Fraction(e['coefficient'])
        assert q
        out[mon] = q
    return out


def mul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (k, ell), d in b.items():
            key = i + k, j + ell
            out[key] = out.get(key, 0) + c * d
    return {m: c for m, c in out.items() if c}


def primitive(p):
    den = math.lcm(*(c.denominator for c in p.values()))
    ints = {m: int(c * den) for m, c in p.items()}
    common = math.gcd(*ints.values())
    return {m: c // common for m, c in ints.items()}


def conv(a, b, p=None):
    out = [0] * (len(a) + len(b) - 1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i + j] += c * d
            if p:
                out[i + j] %= p
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def main():
    name = 'frontier-20261028-level6-boundary-five-positive-v1.json'
    raw = (ROOT / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == 'f049b40075c0ff7cc17d94208488e0fa56d3497feca57c62fb7d9e8aa3cd35c8'
    C = json.loads(raw)
    cache = {}
    for pin in C['inputs']:
        b = (ROOT / pin['file']).read_bytes()
        assert hashlib.sha256(b).hexdigest() == pin['sha256']
        cache[pin['file']] = json.loads(b)
    assert [t['degree'] for t in C['types']] == [[2,2,6],[3,2,6],[3,3,6],[4,3,6],[4,4,6],[5,5,6],[6,6,6]]
    count = 0
    for entry in C['types']:
        a, b, _ = entry['degree']
        ab = str(a) + str(b)
        if ab == '22':
            A = primitive(terms(cache['frontier-20261028-level6-free-22-determinant-v1.json']['determinant_coefficients']))
            B = primitive(terms(cache['frontier-20261028-level6-226-two-minor-resultant-v1.json']['P2_coefficients']))
        elif ab in ('32', '66'):
            packet = cache[f'frontier-20261028-level6-{ab}6-two-minor-certificate-v1.json']
            pair = []
            for label in ('P1', 'P2'):
                F = packet['minor_factorizations'][label]
                assert Fraction(F['content']) != 0
                prod = {(0, 0): Fraction(1)}
                for factor in F['factors']:
                    poly = terms(factor['coefficients'])
                    for _ in range(factor['multiplicity']):
                        prod = mul(prod, poly)
                assert all(c.denominator == 1 for c in prod.values())
                pair.append({m: int(c) for m, c in prod.items()})
            A, B = pair
        else:
            A = primitive(terms(cache[f'frontier-20261028-level6-{ab}6-minor-baseline-v1.json']['coefficients']))
            B = primitive(terms(cache[f'frontier-20261028-level6-{ab}6-minor-seed1-v1.json']['coefficients']))
        assert {e['fixed_variable_index'] for e in entry['boundaries']} == {0, 1}
        for row in entry['boundaries']:
            idx = row['fixed_variable_index']
            assert row['fixed_value'] == row['other_coordinate_lower_bound'] == -1
            axes = []
            for poly in (A, B):
                cs = [0] * (1 + max(m[1 - idx] for m in poly))
                for m, c in poly.items():
                    cs[m[1 - idx]] += c * (-1)**m[idx]
                while len(cs) > 1 and cs[-1] == 0:
                    cs.pop()
                axes.append(cs)
            g = [int(c) for c in row['gcd']]
            qa, qb = [int(c) for c in row['quotient_A']], [int(c) for c in row['quotient_B']]
            assert g[-1] and qa[-1] and qb[-1]
            assert conv(g, qa) == axes[0] and conv(g, qb) == axes[1]
            shifted = [sum(g[j] * math.comb(j, i) * (-1)**(j - i) for j in range(i, len(g))) for i in range(len(g))]
            assert shifted == [int(c) for c in row['gcd_shifted_by_minus_one']]
            assert shifted[0] and (all(c >= 0 for c in shifted) or all(c <= 0 for c in shifted))
            p = row['prime']
            assert p >= 2 and all(p % d for d in range(2, math.isqrt(p) + 1))
            assert qa[-1] % p and qb[-1] % p
            u, v = row['bezout_u'], row['bezout_v']
            assert all(type(c) is int and 0 <= c < p for c in u + v)
            one, two = conv(u, qa, p), conv(v, qb, p)
            n = max(len(one), len(two))
            total = [((one[i] if i < len(one) else 0) + (two[i] if i < len(two) else 0)) % p for i in range(n)]
            assert total[0] == 1 and all(c == 0 for c in total[1:])
            count += 1
    assert count == 14
    out = ROOT / 'frontier-20261028-level6-boundary-five-positive-replay-v1.json'
    with out.open('x') as stream:
        json.dump({'certificate_sha256': hashlib.sha256(raw).hexdigest(), 'boundary_lines': count,
                   'exact_specialized_minor_products': 28, 'full_modular_Bezout_identities': 14,
                   'shifted_positive_polynomials': 14, 'status': 'PASS_ALL_FOURTEEN_REAL_BOUNDARY_POLYNOMIAL_PROOFS',
                   'engine': 'Python standard-library integers and Fraction; no FLINT/SymPy/producer imports',
                   'limits': 'stored-minor equality to actual matrices and actual-source transport remain separate gates'}, stream, indent=2)
        stream.write('\n')
    print('PASS all fourteen exact real boundary-line proofs', out.name)


if __name__ == '__main__':
    main()

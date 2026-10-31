#!/usr/bin/env python3
"""Exact residual-minor, resultant and integer-fibre certificate using FLINT 0.9.

Reads two stored minors; divides only verified positive linear factors; removes
and verifies a common positive-coefficient factor; and certifies the residual
pair coprime by a modular univariate Bezout identity, using constant leading
coefficient specialization. This already proves at most deg(A)*deg(B) complex
exceptional parameter pairs. Optional direct exact resultant and Hensel/Cauchy
integer-root certification then decide every remaining integer fibre.

Every stage is a new immutable JSON. Software arithmetic is not a formal proof
or independent scientific acceptance; the actual-source identification is a
separate written input. All generated files stay in the owner root.
"""
import argparse
import hashlib
import json
import math
import sys
import time
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'frontier-20261028-fastalgebra'))
import flint

sys.set_int_max_str_digits(0)
CTX = flint.fmpz_mpoly_ctx.get(('x', 'y'), 'lex')
x, y = CTX.gens()


def save(path, data):
    # Refuse existing artifacts, including earlier partial-stage receipts.
    with path.open('x') as stream:
        json.dump(data, stream, indent=2)
        stream.write('\n')
    print('WROTE', path.name, hashlib.sha256(path.read_bytes()).hexdigest(), flush=True)


def terms(p):
    return [{'x_power': int(i), 'y_power': int(j), 'coefficient': str(c)}
            for (i, j), c in sorted(p.to_dict().items())]


def degree(p, var):
    return max(mon[var] for mon in p.to_dict())


def load_minor(name):
    raw = (ROOT / name).read_bytes()
    packet = json.loads(raw)
    data = {(e['x_power'], e['y_power']): Fraction(e['coefficient']) for e in packet['coefficients']}
    assert len(data) == len(packet['coefficients'])
    den = math.lcm(*(q.denominator for q in data.values()))
    ints = {mon: int(q * den) for mon, q in data.items()}
    content = math.gcd(*ints.values())
    poly = CTX.from_dict({mon: c // content for mon, c in ints.items()})
    scalar = Fraction(content, den)
    assert {(m): Fraction(int(c)) * scalar for m, c in poly.to_dict().items()} == data
    return packet, hashlib.sha256(raw).hexdigest(), poly, scalar


def axis_polynomial(poly, fixed_index, fixed_value):
    other = 1 - fixed_index
    cs = [0] * (degree(poly, other) + 1)
    for mon, c in poly.to_dict().items():
        cs[mon[other]] += int(c) * fixed_value**mon[fixed_index]
    return flint.fmpz_poly(cs)


def eval_mod_poly(coefficients, value, modulus):
    # The FLINT polynomial is over Z/modulus, not a field; Newton only inverts
    # derivative values explicitly checked to be units by gcd==1.
    ctx = flint.fmpz_mod_poly_ctx(modulus)
    return int(ctx(coefficients)(value))


def integer_root_certificate(poly, prime_start):
    coeffs = list(poly)
    assert poly.degree() >= 1
    largest = max(abs(int(c)) for c in coeffs[:-1])
    leading = abs(int(coeffs[-1]))
    bound = 1 + (largest + leading - 1) // leading
    derivative = poly.derivative()
    p = prime_start
    while True:
        p += 1
        if not flint.fmpz(p).is_prime() or int(coeffs[-1]) % p == 0:
            continue
        reduced = flint.nmod_poly([int(c % p) for c in coeffs], p)
        if reduced.gcd(reduced.derivative()).degree() == 0:
            break
    roots = reduced.roots()
    assert all(int(m) == 1 for _, m in roots)
    # This independently checks that the returned residues exhaust all F_p
    # roots, instead of trusting a returned root count.
    residues = {int(r) for r, _ in roots}
    assert residues == {a for a in range(p) if int(reduced(a)) == 0}
    modulus = p
    exponent = 1
    while modulus <= 2 * bound:
        modulus *= p
        exponent += 1
    found, lifts = [], []
    for root in sorted(residues):
        a, current = root, p
        while current < modulus:
            current = min(current * current, modulus)
            fp = eval_mod_poly(coeffs, a, current)
            dfp = eval_mod_poly(list(derivative), a, current)
            assert math.gcd(dfp, current) == 1
            a = (a - fp * pow(dfp, -1, current)) % current
            assert eval_mod_poly(coeffs, a, current) == 0
        symmetric = a if a <= modulus // 2 else a - modulus
        within = abs(symmetric) <= bound
        exact = within and poly(symmetric) == 0
        if exact:
            found.append(symmetric)
        lifts.append({'residue': root, 'symmetric_lift': str(symmetric),
                      'within_cauchy_bound': within, 'exact_integer_root': exact})
    return sorted(found), {'prime': p, 'prime_is_proved_by_flint_is_prime': True,
                           'reduction_degree': reduced.degree(), 'gcd_derivative_degree': 0,
                           'all_residues_exhaustively_checked': True, 'cauchy_bound': str(bound),
                           'modulus_exponent': exponent, 'modulus': str(modulus), 'lifts': lifts}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--a', type=int, required=True)
    parser.add_argument('--b', type=int, required=True)
    parser.add_argument('--tag1', default='baseline')
    parser.add_argument('--tag2', default='seed1')
    parser.add_argument('--resultant', action='store_true')
    args = parser.parse_args()
    assert flint.__version__ == '0.9.0'
    prefix = f'frontier-20261028-level6-{args.a}{args.b}6-fast-pair'
    packets, residuals, pins, decompositions = [], [], [], []
    for tag in (args.tag1, args.tag2):
        name = f'frontier-20261028-level6-{args.a}{args.b}6-minor-{tag}-v1.json'
        packet, sha, initial, scalar = load_minor(name)
        poly = initial
        factors = []
        for idx, const in ((0, 5), (1, 5), (0, 4), (1, 4)):
            lin = (x if idx == 0 else y) + const
            exponent = 0
            while True:
                q, r = divmod(poly, lin)
                if r:
                    break
                poly, exponent = q, exponent + 1
            if exponent:
                factors.append({'variable_index': idx, 'constant': const, 'exponent': exponent})
        rebuilt = poly
        for fac in factors:
            rebuilt *= ((x if fac['variable_index'] == 0 else y) + fac['constant'])**fac['exponent']
        assert rebuilt == initial
        residuals.append(poly)
        packets.append(packet)
        pins.append({'minor': name, 'sha256': sha, 'pencil_sha256': packet['pencil_sha256']})
        decompositions.append({'scale': str(scalar), 'positive_linear_factors': factors})
    assert packets[0]['degree'] == packets[1]['degree'] == [args.a, args.b, 6]
    assert packets[0]['pencil_sha256'] == packets[1]['pencil_sha256']
    common = residuals[0].gcd(residuals[1])
    common_cs = list(common.to_dict().values())
    assert common.to_dict().get((0, 0), 0) and (all(c > 0 for c in common_cs) or all(c < 0 for c in common_cs)), 'shared factor not one-sign'
    A, ra = divmod(residuals[0], common)
    B, rb = divmod(residuals[1], common)
    assert not ra and not rb and A.gcd(B).is_one()
    assert A * common == residuals[0] and B * common == residuals[1]
    # Both x-leading coefficients must be nonzero constants. Every hypothetical
    # nonconstant common factor then has positive preserved x-degree at y=0.
    leading = []
    for poly in (A, B):
        dx = degree(poly, 0)
        leadterms = {mon: c for mon, c in poly.to_dict().items() if mon[0] == dx}
        assert len(leadterms) == 1 and next(iter(leadterms))[1] == 0
        leading.append(str(next(iter(leadterms.values()))))
    aa, bb = axis_polynomial(A, 1, 0), axis_polynomial(B, 1, 0)
    p = 1009
    while True:
        if flint.fmpz(p).is_prime() and aa.leading_coefficient() % p and bb.leading_coefficient() % p:
            am = flint.nmod_poly([int(c % p) for c in aa], p)
            bm = flint.nmod_poly([int(c % p) for c in bb], p)
            g, u, v = am.xgcd(bm)
            if g.degree() == 0:
                assert g == 1 and u * am + v * bm == 1
                break
        p += 1
    bound = int(A.total_degree()) * int(B.total_degree())
    algebra = {'degree': packets[0]['degree'], 'variables': 'x=r-6,y=s-6', 'inputs': pins,
               'decompositions': decompositions, 'positive_common_factor': terms(common),
               'residual_A': terms(A), 'residual_B': terms(B),
               'residual_total_degrees': [int(A.total_degree()), int(B.total_degree())],
               'x_leading_constants': leading, 'axis_coprimality': {'fixed_y': 0, 'prime': p,
                'gcd_degree': 0, 'bezout_u': [int(c) for c in u], 'bezout_v': [int(c) for c in v]},
               'bezout_bound_on_exceptional_complex_pairs': bound,
               'software': 'python-flint 0.9.0, exact integers/modular arithmetic',
               'status': 'COFINITE_PAIR_CERTIFIED_AT_STORED_MINOR_INPUTS',
               'limits': 'not formal or independent review; stored minors and actual source identification require their own audit'}
    save(ROOT / (prefix + '-algebra-v1.json'), algebra)
    if not args.resultant:
        return
    before = time.monotonic()
    print('COMPUTING exact resultant with respect to x', flush=True)
    HR = A.resultant(B, 'x')
    assert HR and all(mon[0] == 0 for mon in HR.to_dict())
    coeff = [0] * (degree(HR, 1) + 1)
    for mon, c in HR.to_dict().items():
        coeff[mon[1]] = c
    H = flint.fmpz_poly(coeff)
    assert H.degree() <= bound
    for y0 in (0, 1, 7, 19):
        assert H(y0) == axis_polynomial(A, 1, y0).resultant(axis_polynomial(B, 1, y0))
    save(ROOT / (prefix + '-resultant-v1.json'), {'definition': 'Res_x(A,B)', 'degree': H.degree(),
        'coefficients_low_to_high': [str(c) for c in H], 'degree_bound': bound,
        'exact_specialization_checks': [0, 1, 7, 19], 'seconds': time.monotonic() - before})
    repeated = H.gcd(H.derivative())
    W, rem = divmod(H, repeated)
    assert not rem and W * repeated == H
    roots, cert = integer_root_certificate(W, 1000)
    save(ROOT / (prefix + '-integer-fibres-v1.json'), {'resultant_degree': H.degree(),
        'repeated_part_degree': repeated.degree(), 'squarefree_part_degree': W.degree(),
        'squarefree_coefficients_low_to_high': [str(c) for c in W],
        'integer_roots': roots, 'nonnegative_integer_roots': [r for r in roots if r >= 0],
        'root_certificate': cert, 'status': 'NO_NONNEGATIVE_INTEGER_RESULTANT_ROOT' if all(r < 0 for r in roots) else 'NONNEGATIVE_FIBRES_REQUIRE_CHECK',
        'limits': 'actual source identification and independent full verification remain separate'})


if __name__ == '__main__':
    main()

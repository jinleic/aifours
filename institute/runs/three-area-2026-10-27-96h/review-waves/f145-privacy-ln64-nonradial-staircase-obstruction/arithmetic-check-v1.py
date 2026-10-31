#!/usr/bin/env python3
"""Independent Fraction/polynomial audit of the pinned f145 arithmetic only.

No author code is imported. The cap and diamond integrals are reconstructed from
monomials; the geometric moments use factorial moments and a separate raw-series
identity. This does not establish the candidate's geometry or privacy.
"""
from datetime import datetime
from fractions import Fraction as F
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h')
INPUTS = [
    (HERE / 'manifest-v1.json', '8b11415d77d1cc66f4a79cf59f4ed441de8ff46436ea06ba6755944214fe6c01', 3312, 38),
    (HERE / 'parent-required-numeric-correction-v1.json', '3b29787c171857d35099fded30bc7d1c2bd9b957537d64b54891209a8a1197bb', 1446, 16),
    (Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-ln64-rational-nonradial-obstruction-v1.md'), '028397b5e5c5cae583f9fc69ed1efadbaeda169c729d3cb878b74b1e2cc14e01', 7063, 87),
    (ROOT / 'written-releases/info-1-mda-primary-definitions-v1.md', '25740af38e4ed3d36e925be499e7a0fa4920182989c8ba55c99811538fb03718', 1542, 9),
]


class CheckFailure(Exception):
    pass


def require(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def text(q):
    q = F(q)
    return str(q.numerator) + '/' + str(q.denominator)


def poly_add(p, q):
    return tuple((p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0))
                 for i in range(max(len(p), len(q))))


def poly_mul(p, q):
    result = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            result[i + j] += x * y
    return tuple(result)


def poly_sub(p, q):
    return poly_add(p, tuple(-x for x in q))


def poly_derivative(p):
    return tuple(i * p[i] for i in range(1, len(p)))


def poly_value(p, x):
    value = F(0)
    for c in reversed(p):
        value = value * x + c
    return value


def frac_list(p):
    return [text(c) for c in p]


def variation(p):
    signs = [1 if c > 0 else -1 for c in reversed(p) if c]
    return sum(x != y for x, y in zip(signs, signs[1:]))


def cap_integral(terms, eta):
    # Integrate R^r u^i v^j over 0<=u<=eta, -u<=v<=u.
    out = [F(0)] * 3
    for (r, i, j), coefficient in terms.items():
        symmetric_v = F(1 - (-1) ** (j + 1), j + 1)
        power = i + j + 2
        out[r] += coefficient * symmetric_v * eta ** power / power
    return tuple(out)


def quadrant_coefficient(i, j):
    # Integrate x^i y^j over 0<=x<=R and 0<=y<=R-x.
    return sum((F((-1) ** h * comb(j + 1, h), (j + 1) * (i + h + 1))
                for h in range(j + 2)), F(0))


def expect_failure(label, operation, reason):
    try:
        operation()
    except CheckFailure as error:
        require(str(error) == reason, label + ': wrong rejection reason: ' + str(error))
        return {'case': label, 'status': 'rejected', 'reason': str(error)}
    raise CheckFailure(label + ': mutation unexpectedly accepted')


def main():
    start = datetime.now().astimezone().isoformat()
    own_bytes = Path(__file__).read_bytes()
    input_receipts = []
    for path, expected, size, lf in INPUTS:
        data = path.read_bytes()  # correction precedes the candidate in INPUTS
        digest = sha256(data).hexdigest()
        require((digest, len(data), data.count(b'\n')) == (expected, size, lf),
                'pinned input mismatch: ' + str(path))
        data.decode('utf-8')
        input_receipts.append({'path': str(path), 'sha256': digest,
                               'bytes': len(data), 'LF': data.count(b'\n')})

    b, eta = F(1, 64), F(1, 100)
    a, z = F(3761763123, 10**10), F(3761763124, 10**10)
    m = b / (1 - b)
    require(m == F(1, 63) and 0 < 2 * eta < a < z < 1, 'parameters')

    # The probability generating function yields E[(N)_r]=r! m^r.  Stirling
    # conversion gives raw moments, independently of the supplied formulas.
    stirling = [[1]]
    for j in range(1, 5):
        prev = stirling[-1]
        stirling.append([(prev[r - 1] if r > 0 else 0) +
                         r * (prev[r] if r < len(prev) else 0)
                         for r in range(j + 1)])
    raw = [sum((F(stirling[j][r] * factorial(r)) * m ** r
                for r in range(j + 1)), F(0)) for j in range(5)]
    expected_raw = [F(1), m, m + 2*m**2, m + 6*m**2 + 6*m**3,
                    m + 14*m**2 + 36*m**3 + 24*m**4]
    require(raw == expected_raw, 'factorial-to-raw moment identity')

    # Independent Eulerian-series expressions for sum k^j b^k, j<=4.
    series = [1/(1-b), b/(1-b)**2, b*(1+b)/(1-b)**3,
              b*(1+4*b+b**2)/(1-b)**4,
              b*(1+11*b+11*b**2+b**3)/(1-b)**5]
    require([(1-b)*v for v in series] == raw, 'geometric raw-series check')
    cutoff = 7
    tail_equalities = []
    for j in range(5):
        prefix = sum(((1-b)*b**k*F(k**j) for k in range(cutoff)), F(0))
        tail = b**cutoff * sum((F(comb(j, r))*cutoff**(j-r)*raw[r]
                                for r in range(j+1)), F(0))
        require(prefix + tail == raw[j], 'infinite tail identity j=' + str(j))
        tail_equalities.append({'degree': j, 'prefix': text(prefix),
                                'exact_tail': text(tail), 'total': text(raw[j])})

    def moment_polynomial(j):
        p = [F(0)] * (j + 1)
        for r in range(j + 1):
            p[j-r] += F(comb(j, r)) * raw[r]
        return tuple(p)

    M1, M2, M4 = [moment_polynomial(j) for j in (1, 2, 4)]
    require(M1 == (m, F(1)), 'M1 expansion')
    require(M2 == (m+2*m*m, 2*m, F(1)), 'M2 expansion')
    require(M4 == (m+14*m*m+36*m**3+24*m**4,
                   4*(m+6*m*m+6*m**3), 6*(m+2*m*m), 4*m, F(1)), 'M4 expansion')
    require(all(c > 0 for c in M2 + M4), 'moment positivity and monotonicity')

    numerator = poly_sub(poly_mul(poly_derivative(M4), M2),
                         poly_mul(M4, poly_derivative(M2)))
    P = (m*m*(1+2*m), -m*(1+2*m)*(1+6*m), 12*m**3-2*m,
         2*m+12*m*m, 5*m, F(1))
    require(numerator == tuple(2*c for c in P), 'derivative numerator is 2P')
    require(variation(P) == 2, 'Descartes sign changes')
    points = {'zero': F(0), 'a': a, 'z': z, 'one': F(1)}
    p_values = {name: poly_value(P, point) for name, point in points.items()}
    require(p_values['zero'] > 0 and p_values['a'] < 0 and
            p_values['z'] > 0 and p_values['one'] > 0, 'required quintic signs')

    def bracket(left, right):
        require(left < right and poly_value(P, left) < 0 < poly_value(P, right),
                'root bracket lacks negative-to-positive endpoint signs')

    bracket(a, z)
    def staircase(g):
        return poly_value(M4, g) / (3*poly_value(M2, g))
    require(staircase(F(0)) == staircase(F(1)), 'uncut staircase endpoint equality')
    require(poly_value(M2, F(1)) == poly_value(M2, F(0))/b and
            poly_value(M4, F(1)) == poly_value(M4, F(0))/b,
            'endpoint shifted geometric moments')

    # Recompute each axis cap by its two-variable monomial integrals.
    cap_area = cap_integral({(0, 0, 0): F(1)}, eta)
    cap_moment = cap_integral({(2, 0, 0): F(1), (1, 1, 0): F(-2),
                               (0, 2, 0): F(1), (0, 0, 2): F(1)}, eta)
    require(cap_area == (eta**2, F(0), F(0)), 'integrated cap area')
    require(cap_moment == (F(2, 3)*eta**4, -F(4, 3)*eta**3, eta**2),
            'integrated cap squared moment')
    full_area_coefficient = 4*quadrant_coefficient(0, 0)
    full_moment_coefficient = 4*(quadrant_coefficient(2, 0) + quadrant_coefficient(0, 2))
    require(full_area_coefficient == 2 and full_moment_coefficient == F(2, 3),
            'integrated full diamond')
    E1, E2, E4 = poly_value(M1, a), poly_value(M2, a), poly_value(M4, a)
    cap_expected = cap_moment[0] + cap_moment[1]*E1 + cap_moment[2]*E2
    Z = full_area_coefficient*E2 - 4*cap_area[0]
    numerator_cost = full_moment_coefficient*E4 - 4*cap_expected
    require(Z > 0 and numerator_cost > 0, 'clipped area and moment positivity')
    J = numerator_cost / Z
    reported_J = F(4355768046089487574226880288026708390699272667,
                   26721376640271909097532496900000000000000000000)
    require(J == reported_J, 'candidate clipped-law cost equality')

    # Positive eta=0 control: compute an uncut R=1/2+N integral from the
    # independently listed raw geometric sums rather than the moment builder.
    gamma = F(1, 2)
    uncut_area = (1-b) * sum((F(comb(2, r))*gamma**(2-r)*series[r]
                              for r in range(3)), F(0))
    uncut_moment = (1-b) * sum((F(comb(4, r))*gamma**(4-r)*series[r]
                                for r in range(5)), F(0))
    uncut_direct = full_moment_coefficient*uncut_moment / (full_area_coefficient*uncut_area)
    require(uncut_direct == staircase(gamma), 'eta=0 positive control')
    zero_direct = series[4] / (3*series[2])
    require(zero_direct == staircase(F(0)), 'eta=0 zero-core series control')

    lower = poly_value(M4, a) / (3*poly_value(M2, z))
    gap = lower - J
    corrected = F(55892104628095766169604064637687395172793197064705238995982813,
                  28589579218686463271455054512504719394059809867200000000000000000000)
    require(gap == corrected, 'corrected gap fraction')
    require(gap > F(1, 10**6), 'corrected gap exceeds 10^-6')
    integer_margin = gap.numerator*10**6 - gap.denominator
    require(integer_margin > 0, 'strict integer gap certificate')

    def check_normalization(mass):
        require(mass == 1, 'candidate density integrates to a value other than 1')
    check_normalization(Z/Z)
    mutated_Z = full_area_coefficient*E2 - 3*cap_area[0]
    mutation_mass = Z/mutated_Z
    normalization_control = expect_failure('three-cap normalizer used on four-cap law',
                                           lambda: check_normalization(mutation_mass),
                                           'candidate density integrates to a value other than 1')
    normalization_control.update({'mutated_normalizer': text(mutated_Z),
                                  'actual_integral_using_mutated_normalizer': text(mutation_mass)})

    wrong_denominator = 28589579218686463271455054512504719394059809867200000000000000
    wrong_gap = F(55892104628095766169604064637687395172793197064705238995982813,
                  wrong_denominator)
    def check_gap(candidate_gap):
        require(candidate_gap == gap, 'declared fraction is not the recomputed gap')
    denominator_control = expect_failure('original denominator divided by one million',
                                         lambda: check_gap(wrong_gap),
                                         'declared fraction is not the recomputed gap')
    require(wrong_gap / gap == 10**6, 'wrong-denominator factor')
    denominator_control.update({'wrong_display': text(wrong_gap),
                                'wrong_over_correct': text(wrong_gap/gap),
                                'wrong_display_also_exceeds_10^-6': wrong_gap > F(1, 10**6)})

    unit = F(1, 10**10)
    bracket_control = expect_failure('both altered bracket endpoints to right of z',
                                     lambda: bracket(z, z+unit),
                                     'root bracket lacks negative-to-positive endpoint signs')
    bracket_control.update({'left': text(z), 'right': text(z+unit),
                            'P_left': text(poly_value(P, z)),
                            'P_right': text(poly_value(P, z+unit))})
    coarse_a, coarse_z = F(37617, 100000), F(37618, 100000)
    bracket(coarse_a, coarse_z)
    coarse_gap = poly_value(M4, coarse_a)/(3*poly_value(M2, coarse_z)) - J
    require(coarse_gap < 0, 'coarse valid bracket has negative lower-gap enclosure')
    coarse_control = expect_failure('valid but too-coarse root bracket',
                                    lambda: require(coarse_gap > F(1, 10**6),
                                                    'coarse bracket does not certify the strict gap'),
                                    'coarse bracket does not certify the strict gap')
    coarse_control.update({'left': text(coarse_a), 'right': text(coarse_z),
                           'P_left': text(poly_value(P, coarse_a)),
                           'P_right': text(poly_value(P, coarse_z)),
                           'outward_gap': text(coarse_gap)})

    receipt = {
        'scope': 'Arithmetic conditional on the stated shell geometry; no privacy, global optimum, radial-extension, formal or novelty verdict.',
        'started_local_iso': start,
        'completed_local_iso_before_receipt_write': datetime.now().astimezone().isoformat(),
        'code_path': str(Path(__file__).resolve()), 'code_sha256': sha256(own_bytes).hexdigest(),
        'ordered_verified_inputs': input_receipts,
        'parameters': {'b': text(b), 'm': text(m), 'a': text(a), 'z': text(z), 'eta': text(eta)},
        'geometric_raw_moments_0_through_4': frac_list(raw),
        'infinite_tail_check_at_k': cutoff, 'tail_equalities': tail_equalities,
        'coefficient_convention': 'ascending powers',
        'M1': frac_list(M1), 'M2': frac_list(M2), 'M4': frac_list(M4),
        'derivative_numerator': frac_list(numerator), 'quintic_P': frac_list(P),
        'descartes_sign_changes': variation(P),
        'P_values': {name: text(q) for name, q in p_values.items()},
        'diamond_area_R2_coefficient': text(full_area_coefficient),
        'diamond_moment_R4_coefficient': text(full_moment_coefficient),
        'cap_area_R_coefficients': frac_list(cap_area),
        'cap_moment_R_coefficients': frac_list(cap_moment),
        'cap_moment_at_R_a': text(poly_value(cap_moment, a)),
        'clipped_normalizer': text(Z), 'clipped_moment_numerator': text(numerator_cost),
        'clipped_cost': text(J), 'staircase_endpoint_cost': text(staircase(F(0))),
        'uncut_eta0_gamma_half_positive_control': text(uncut_direct),
        'staircase_outward_lower_bound': text(lower), 'corrected_gap': text(gap),
        'gap_minus_10^-6': text(gap - F(1, 10**6)),
        'strict_gap_integer_numerator_times_10^6_minus_denominator': str(integer_margin),
        'negative_controls': [normalization_control, denominator_control, bracket_control, coarse_control],
        'status': 'ALL SPECIFIED ARITHMETIC CHECKS PASSED'
    }
    output = HERE / 'arithmetic-receipt-v1.json'
    with output.open('x', encoding='utf-8') as handle:
        json.dump(receipt, handle, indent=2, ensure_ascii=False)
        handle.write('\n')
    print(json.dumps({'receipt': str(output), 'code_sha256': receipt['code_sha256'],
                      'started_local_iso': start,
                      'completed_local_iso_before_receipt_write': receipt['completed_local_iso_before_receipt_write'],
                      'status': receipt['status']}, indent=2))


if __name__ == '__main__':
    main()

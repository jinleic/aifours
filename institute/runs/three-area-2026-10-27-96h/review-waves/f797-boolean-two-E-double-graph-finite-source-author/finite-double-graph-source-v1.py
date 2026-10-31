#!/usr/bin/env python3
"""UNRUN proposed finite scrutiny of the d_E=2 double-graph-row obstruction.

No physical caller is generated.  See author-candidate-v1.md for the exact
coverage, overapproximations and parent-GO boundary.  Standard library only;
Python 3.10 or newer.  Writes no files and performs no network or subprocess I/O.
"""

import argparse
import itertools
import json
import math
import signal
import sys
import time


class Finding(Exception):
    def __init__(self, reason, detail=None):
        super().__init__(reason)
        self.reason = reason
        self.detail = detail


class Incomplete(Exception):
    pass


STOP = False
DEADLINE = 0.0


def request_stop(_signum, _frame):
    global STOP
    STOP = True


def guard():
    if STOP or time.monotonic() >= DEADLINE:
        raise Incomplete()


def insist(condition, reason, detail=None):
    if not condition:
        raise Finding(reason, detail)


def dot(a, b):
    return (a & b).bit_count() & 1


def pm(bit):
    return -1 if bit & 1 else 1


def xor_all(values):
    out = 0
    for value in values:
        out ^= value
    return out


def defect_direction(p, q):
    insist(0 <= p < 4 and 0 <= q < 4 and p != q, 'DEFECT_SITES')
    delta = p ^ q
    kappas = [a for a in (1, 2, 3) if dot(a, delta) == 0]
    insist(len(kappas) == 1, 'DEFECT_ANNIHILATOR')
    return delta, kappas[0]


def require_odd_f(f):
    insist(len(f) == 4 and all(x in (0, 1) for x in f) and sum(f) % 2 == 1,
           'ODD_F')


def require_row_zero(f, theta, sigma, points, signs):
    insist(f in (0, 1) and theta in range(4) and sigma in (-1, 1),
           'ROW_PARAMETER')
    insist(len(points) == len(signs) and all(x in (-1, 1) for x in signs),
           'ROW_MATES')
    value = sum(sigma * pm(dot(theta, b)) for b in range(4)) + 2 * sum(signs)
    insist(value == 0, 'ROW_ZERO', {'sum': value})


def validate_profile(v):
    insist(len(v) == 8, 'PROFILE_LENGTH')
    nz = [i for i, x in enumerate(v) if x != 0]
    if len(nz) == 1:
        insist(abs(v[nz[0]]) == 2, 'PROFILE_SINGLETON')
        return 'singleton'
    insist(len(nz) == 4, 'PROFILE_SUPPORT')
    insist(all(abs(v[i]) == 1 for i in nz), 'PROFILE_AMPLITUDE')
    insist(xor_all(nz) == 0, 'PROFILE_FLAT')
    insist(math.prod(v[i] for i in nz) == -1, 'PROFILE_SIGN')
    return 'plane'


def profile_universe():
    profiles = []
    for i in range(8):
        for sign in (-1, 1):
            v = [0] * 8
            v[i] = 2 * sign
            profiles.append(tuple(v))
    planes = [c for c in itertools.combinations(range(8), 4) if xor_all(c) == 0]
    insist(len(planes) == 14, 'PROFILE_PLANE_UNIVERSE')
    for plane in planes:
        for signs in itertools.product((-1, 1), repeat=4):
            if math.prod(signs) == -1:
                v = [0] * 8
                for i, sign in zip(plane, signs):
                    v[i] = sign
                profiles.append(tuple(v))
    insist(len(profiles) == 128 and len(set(profiles)) == 128, 'PROFILE_UNIVERSE')
    for v in profiles:
        validate_profile(v)
    return profiles


def require_projection(v, projections):
    insist(tuple(v) in projections, 'PROFILE_PROJECTION')


def require_theta(theta, kappa):
    insist(xor_all(theta) == kappa, 'THETA_XOR',
           {'theta': list(theta), 'kappa': kappa})


def row_vector(f, theta, sigma, points, signs):
    require_row_zero(f, theta, sigma, points, signs)
    etas = [(1, 0)] + [(s, a) for a in (1, 2, 3) for s in (0, 1)]
    values = []
    for s, alpha in etas:
        total = sum(sigma * pm(dot(theta, b) ^ (s * f) ^ dot(alpha, b))
                    for b in range(4))
        total += sum(2 * e * pm((s * (f ^ 1)) ^ dot(alpha, b))
                     for b, e in zip(points, signs))
        insist(total % 4 == 0, 'ROW_QUOTIENT_INTEGRAL')
        values.append(total // 4)
    return tuple(values)


def inventory_e_allocations():
    sites = [(i, h) for i in (1, 2, 3) for h in (0, 1)]
    shapes = {'2': 0, '1+1': 0}
    signed = 0
    for pair in itertools.combinations(sites, 2):
        shapes['2' if pair[0][0] == pair[1][0] else '1+1'] += 1
        for signs in itertools.product((-1, 1), repeat=2):
            insist(len(set(pair)) == 2 and all(i != 0 for i, _ in pair)
                   and all(e in (-1, 1) for e in signs), 'E_ALLOCATION')
            signed += 1
    insist(shapes == {'2': 3, '1+1': 12} and signed == 60, 'E_INVENTORY')
    return {'unsigned': 15, 'signed': signed, 'allocation_shapes': shapes,
            'scope': 'inventory factored; E-side seven-column extendability not asserted'}


def same_x_graph_profiles(projections):
    odd_fs = [f for f in itertools.product((0, 1), repeat=4) if sum(f) % 2]
    ordinary = list(itertools.product((1, 2, 3), (-1, 1)))
    cached = {}

    def vector(f, theta, sigma, points=(), signs=()):
        key = (f, theta, sigma, points, signs)
        if key not in cached:
            cached[key] = row_vector(f, theta, sigma, points, signs)
        return cached[key]

    total = 0
    accepted = 0
    accepted_sign_cases = {'equal': 0, 'opposite': 0}
    for f in odd_fs:
        require_odd_f(f)
        for j in range(4):
            other = [i for i in range(4) if i != j]
            for p, q in itertools.combinations(range(4), 2):
                _, kappa = defect_direction(p, q)
                for ep, eq in itertools.product((-1, 1), repeat=2):
                    guard()
                    for tj, sj in itertools.product(range(4), (-1, 1)):
                        rowsum = sum(sj * pm(dot(tj, b)) for b in range(4)) + 2 * (ep + eq)
                        if rowsum != 0:
                            continue
                        dj = vector(f[j], tj, sj, (p, q), (ep, eq))
                        for choices in itertools.product(ordinary, repeat=3):
                            total += 1
                            theta = [0] * 4
                            rv = [None] * 4
                            theta[j], rv[j] = tj, dj
                            for i, (ti, si) in zip(other, choices):
                                theta[i] = ti
                                rv[i] = vector(f[i], ti, si)
                            if not all(tuple(rv[i][k] for i in range(4)) in projections
                                       for k in range(7)):
                                continue
                            accepted += 1
                            accepted_sign_cases['equal' if ep == eq else 'opposite'] += 1
                            require_theta(theta, kappa)
    insist(total == 580608, 'ROW_DOMAIN_COVERAGE', total)
    insist(accepted > 0 and all(v > 0 for v in accepted_sign_cases.values()),
           'ROW_DOMAIN_VACUOUS', accepted_sign_cases)
    return {'graph_row_assignments': total, 'projection_admitted': accepted,
            'admitted_by_graph_mate_signs': accepted_sign_cases,
            'odd_f_tables': len(odd_fs), 'defect_rows': 4, 'mate_pairs_per_row': 6,
            'proof_scope': 'same graph-row data in all seven columns; E completion per column is relaxed'}


def fixture_x(prime):
    # Packet S4, examples III and III-prime; all entries not listed are zero.
    f = (0, 0, 0, 1)
    theta = (2, 2, 3, 1)
    sigma = (1, 1, -1, -1) if prime else (1, -1, -1, 1)
    x = {}
    for i in range(4):
        for b in range(4):
            x[(1, f[i], i, b)] = sigma[i] * pm(dot(theta[i], b))
    x[(1, 1, 0, 0)] = 2
    x[(1, 1, 0, 1)] = -2
    if prime:
        ell = [(2, 0, 2, 1), (2, 0, 3, 1), (2, 1, 0, -1), (2, 1, 3, -1),
               (3, 0, 0, 1), (3, 0, 3, -1), (0, 0, 2, 1), (0, 0, 3, -1)]
    else:
        ell = [(2, 0, 0, 1), (2, 0, 1, 1), (2, 1, 0, -1), (2, 1, 3, -1),
               (3, 0, 1, 1), (3, 0, 2, -1), (0, 0, 2, 1), (0, 0, 3, -1)]
    for i, h, b, e in ell:
        insist((0, h, i, b) not in x, 'FIXTURE_DUPLICATE')
        x[(0, h, i, b)] = 2 * e
    return x, f, theta


def check_fixture(prime):
    x, f, theta = fixture_x(prime)
    require_odd_f(f)
    require_theta(theta, defect_direction(0, 1)[1])
    es = [(i, h) for ell, h, i, b in x if ell == 0 and i != 0 and b == 0]
    zs = [(h, i, b) for ell, h, i, b in x if ell == 0 and b != 0]
    insist(len(es) == 2 and len(zs) == 6 and
           not any(ell == 0 and i == 0 and b == 0 for ell, h, i, b in x),
           'FIXTURE_SUPPORT')
    shape = '2' if es[0][0] == es[1][0] else '1+1'
    insist(shape == ('1+1' if prime else '2'), 'FIXTURE_E_SHAPE')
    etas = [(0, 0), (1, 0)] + [(s, a) for a in (1, 2, 3) for s in (0, 1)]
    all_z = []
    for s, alpha in etas:
        z = []
        for ell in range(2):
            for i in range(4):
                raw = sum(x.get((ell, h, i, b), 0) * pm(s * h ^ dot(alpha, b))
                          for h in range(2) for b in range(4))
                insist(raw % 4 == 0, 'FIXTURE_QUOTIENT_INTEGRAL')
                z.append(raw // 4)
        all_z.append(z)
    insist(not any(all_z[0]), 'FIXTURE_ZERO_ETA')
    kinds = [validate_profile(z) for z in all_z[1:]]
    lam = all_z[1]
    insist(sum(v != 0 for v in lam) == 1 and abs(lam[2]) == 2,
           'FIXTURE_LAMBDA_SINGLETON')
    packed = {((ell << 5) | (h << 4) | (i << 2) | b): value
              for (ell, h, i, b), value in x.items()}
    walsh = [sum(value * pm(dot(freq, site)) for site, value in packed.items())
             for freq in range(64)]
    insist(walsh[0] == 0 and all(w in (-8, 0, 8) for w in walsh), 'FIXTURE_U0')
    return {'name': 'III-prime' if prime else 'III', 'E_allocation': shape,
            'profile_kinds': kinds, 'walsh_zero_at_zero': True,
            'scope': 'X only; no physical inverse, Y, J, Z4 or U3 witness'}


def check_full_mate_parity(values):
    insist(len(values) == 4 and all(v == values[0] for v in values), 'FULL_MATE_PARITY')


def check_defect_mate_parity(values, delta):
    insist(len(values) == 4 and all(values[a] == (values[0] ^ dot(a, delta))
                                     for a in range(4)), 'DEFECT_MATE_PARITY')


def mate_parities():
    full_count = 0
    defect_count = 0
    for signs in itertools.product((-1, 1), repeat=4):
        guard()
        hats = [sum(signs[b] * pm(dot(a, b)) for b in range(4)) for a in range(4)]
        insist(all(h % 2 == 0 for h in hats), 'MATE_NOT_EVEN')
        vals = [(h // 2) & 1 for h in hats]
        check_full_mate_parity(vals)
        for weight in (-1, 1):
            insist(all(((weight * hats[a] // 2) & 1) == vals[a] for a in range(4)),
                   'MATE_WEIGHT_PARITY')
        full_count += 1
    for p, q in itertools.combinations(range(4), 2):
        delta, _ = defect_direction(p, q)
        remaining = [b for b in range(4) if b not in (p, q)]
        insist(xor_all(remaining) == delta, 'COMPLEMENT_XOR')
        for signs in itertools.product((-1, 1), repeat=2):
            hats = [sum(e * pm(dot(a, b)) for b, e in zip(remaining, signs))
                    for a in range(4)]
            insist(all(h % 2 == 0 for h in hats), 'MATE_NOT_EVEN')
            vals = [(h // 2) & 1 for h in hats]
            check_defect_mate_parity(vals, delta)
            for weight in (-1, 1):
                insist(all(((weight * hats[a] // 2) & 1) == vals[a] for a in range(4)),
                       'MATE_WEIGHT_PARITY')
            defect_count += 1
    insist(full_count == 16 and defect_count == 24, 'MATE_COVERAGE')
    insist(3 * 4 + 2 == 14, 'D3_MATE_COUNT')
    return {'full_row_sign_patterns': full_count, 'defect_pair_and_sign_patterns': defect_count,
            'defect_rows': 4, 'factored_full_location_sign_assignments': 4 * 6 * 4 * 16**3,
            'D3_mates_per_full_assignment': 14,
            'scope': 'all full assignments covered by independent local parity factorization, not looped'}


def check_graph_parity(actual, base, s, alpha, delta):
    insist(actual == (base ^ s ^ dot(alpha, delta)), 'GRAPH_PARITY')


def check_slices(slices):
    insist(len(slices) == 2 and all(len(row) == 16 for row in slices), 'SLICE_SHAPE')
    insist(all(all(v == row[0] for v in row) for row in slices), 'SLICE_NONUNIFORM')
    insist(slices[0][0] != slices[1][0], 'SLICE_NOT_OPPOSITE')


def phase_and_common_y_parity():
    r_count = 0
    for theta in itertools.product(range(4), repeat=4):
        for r in itertools.permutations(range(4)):
            mu = tuple(theta[i] ^ r[i] for i in range(4))
            insist(xor_all(mu) == xor_all(theta), 'PHASE_COVECTOR_XOR')
            r_count += 1
    insist(r_count == 6144, 'PHASE_COVECTOR_COVERAGE')

    # Direct two-bit bent row transform divided by two; no imported table.
    unit = {}
    for mu in range(4):
        for alpha in range(4):
            value = sum(pm(((b >> 1) & 1) * (b & 1) ^ dot(mu ^ alpha, b))
                        for b in range(4))
            insist(value in (-2, 2), 'BENT_WALSH')
            unit[(mu, alpha)] = value // 2
    fs = [f for f in itertools.product((0, 1), repeat=4) if sum(f) % 2]
    cells = 0
    phase_configs = 0
    for delta in (1, 2, 3):
        kappa = next(a for a in (1, 2, 3) if dot(a, delta) == 0)
        for a, b, c in itertools.product(range(4), repeat=3):
            mu = (a, b, c, a ^ b ^ c ^ kappa)
            for tau in itertools.product((-1, 1), repeat=4):
                for f in fs:
                    guard()
                    phase_configs += 1
                    def graph_parity(s, alpha, beta):
                        xis = [tau[i] * unit[(mu[i], alpha)] * pm(s * f[i] ^ dot(beta, i))
                               for i in range(4)]
                        value = (sum(xis) // 2) & 1
                        insist(value == (1 if math.prod(xis) == -1 else 0),
                               'GRAPH_SIGN_PRODUCT')
                        return value
                    base = graph_parity(0, 0, 0)
                    graph_slices = []
                    for s in (0, 1):
                        row = []
                        for alpha in range(4):
                            for beta in range(4):
                                value = graph_parity(s, alpha, beta)
                                check_graph_parity(value, base, s, alpha, delta)
                                row.append(value)
                                cells += 1
                        graph_slices.append(row)
                    # A local full-row baseline can be either parity.  Combining
                    # it with the defect row proves every 14-mate assignment.
                    for mate_base in (0, 1):
                        slices = [[graph_slices[s][4 * alpha + beta] ^ mate_base ^ dot(alpha, delta)
                                   for alpha in range(4) for beta in range(4)]
                                  for s in (0, 1)]
                        check_slices(slices)
                        insist(slices[0][0] == (base ^ mate_base), 'MATE_CANCELLATION')
    insist(phase_configs == 3 * 64 * 16 * 8 and cells == phase_configs * 32,
           'PHASE_DOMAIN_COVERAGE')
    return {'all_theta_and_distinct_r_checks': r_count, 'nonzero_defect_directions': 3,
            'mu_tuples_per_direction': 64, 'graph_sign_tuples': 16, 'odd_f_tables': 8,
            'phase_configurations': phase_configs, 'direct_graph_frequency_cells': cells,
            'mate_baseline_parities_per_configuration': 2,
            'scope': 'mu superset with xor kappa; 14-mate assignments lifted by verified local factorization'}


def require_pair(a0, a1):
    insist(abs(a0) + abs(a1) <= 3, 'PAIR_CAP')
    insist((a0 + a1) % 2 == 1 and (a0 - a1) % 2 == 1, 'PAIR_RESIDUE')


def require_counts(m, n, e, z):
    insist(0 <= m <= 16 and 0 <= n <= 16 and 0 <= e <= m and 0 <= z <= 16 - n,
           'CENSUS_RANGE')
    insist(4 * n + m + 9 * (16 - m) == 144, 'CENSUS_PARTIAL_ENERGY')
    insist(n + m + e + 2 * z == 8, 'CENSUS_SMALL_COUNT')
    insist(8 * (m - e) <= 16, 'ODD_L1_BOUND')


def integer_cases():
    signatures = set()
    for a0 in range(-3, 4):
        for a1 in range(-3, 4):
            try:
                require_pair(a0, a1)
            except Finding as exc:
                if exc.reason not in ('PAIR_CAP', 'PAIR_RESIDUE'):
                    raise
                continue
            small = int(abs(a0 + a1) == 1) + int(abs(a0 - a1) == 1)
            signatures.add((abs(a1), abs(a0), small))
    expected = {(0, 1, 2), (0, 3, 0), (1, 0, 2), (1, 2, 1), (2, 1, 1), (3, 0, 0)}
    insist(signatures == expected, 'PAIR_SIGNATURES')
    solutions = []
    for m in range(17):
        for n in range(17):
            for e in range(m + 1):
                for z in range(17 - n):
                    if 4 * n + m + 9 * (16 - m) != 144:
                        continue
                    if n + m + e + 2 * z != 8:
                        continue
                    require_counts(m, n, e, z)
                    solutions.append((m, n, e, z))
    expected_cases = {(0, 0, 0, 4), (1, 2, 1, 2), (2, 4, 0, 1), (2, 4, 2, 0)}
    insist(set(solutions) == expected_cases, 'CENSUS_CASES', solutions)
    return {'normalized_pair_signatures': sorted([list(x) for x in signatures]),
            'm_n_e_z': sorted([list(x) for x in solutions]),
            'odd_slice_A0_l1_values': sorted({8 * (m - e) for m, n, e, z in solutions}),
            'scope': 'necessary paired-frequency integer census; not a realizable full spectrum'}


def require_z4_pair(z4, other, weight):
    insist(abs(z4) == 4 and weight in (-1, 1), 'Z4_VALUE')
    insist(other in (-2, 0, 2), 'Z4_PARTNER_BOUND')
    insist(abs(z4 + weight * other) >= 2, 'Z4_TRIANGLE')


def z4_boundary():
    cases = 0
    for z4 in (-4, 4):
        for other in (-2, 0, 2):
            for weight in (-1, 1):
                require_z4_pair(z4, other, weight)
                cases += 1
    return {'physical_value_sign_cases': cases,
            'scope': 'conditional on actual unique Z4 and physical opposite-h Z partner'}


def expect_failure(name, reason, action):
    try:
        action()
    except Finding as exc:
        insist(exc.reason == reason, 'CONTROL_WRONG_REASON',
               {'control': name, 'expected': reason, 'actual': exc.reason})
        return {'control': name, 'reason': reason}
    raise Finding('CONTROL_DID_NOT_FAIL', name)


def controls(projections):
    cases = [
        ('duplicate_defect_site', 'DEFECT_SITES', lambda: defect_direction(0, 0)),
        ('even_F', 'ODD_F', lambda: require_odd_f((0, 0, 0, 0))),
        ('nonzero_row_sum', 'ROW_ZERO', lambda: require_row_zero(0, 0, 1, (0, 1), (1, 1))),
        ('bad_singleton', 'PROFILE_SINGLETON', lambda: validate_profile([1, 0, 0, 0, 0, 0, 0, 0])),
        ('three_profile_sites', 'PROFILE_SUPPORT', lambda: validate_profile([1, 1, 1, 0, 0, 0, 0, 0])),
        ('bad_plane_amplitude', 'PROFILE_AMPLITUDE', lambda: validate_profile([2, 1, 1, -1, 0, 0, 0, 0])),
        ('nonflat_support', 'PROFILE_FLAT', lambda: validate_profile([1, 1, 1, 0, -1, 0, 0, 0])),
        ('positive_plane_product', 'PROFILE_SIGN', lambda: validate_profile([1, 1, 1, 1, 0, 0, 0, 0])),
        ('odd_graph_intersection', 'PROFILE_PROJECTION', lambda: require_projection((1, 1, 1, 0), projections)),
        ('wrong_theta_xor', 'THETA_XOR', lambda: require_theta((0, 0, 0, 0), 2)),
        ('varying_full_mate', 'FULL_MATE_PARITY', lambda: check_full_mate_parity([0, 1, 0, 0])),
        ('missing_defect_response', 'DEFECT_MATE_PARITY', lambda: check_defect_mate_parity([1, 1, 1, 1], 1)),
        ('wrong_graph_factor', 'GRAPH_PARITY', lambda: check_graph_parity(0, 0, 0, 1, 1)),
        ('nonuniform_slice', 'SLICE_NONUNIFORM', lambda: check_slices([[0] * 15 + [1], [1] * 16])),
        ('same_slice_parity', 'SLICE_NOT_OPPOSITE', lambda: check_slices([[0] * 16, [0] * 16])),
        ('pair_cap', 'PAIR_CAP', lambda: require_pair(4, 0)),
        ('pair_residue', 'PAIR_RESIDUE', lambda: require_pair(0, 2)),
        ('partial_energy', 'CENSUS_PARTIAL_ENERGY', lambda: require_counts(0, 1, 0, 0)),
        ('small_count', 'CENSUS_SMALL_COUNT', lambda: require_counts(0, 0, 0, 3)),
        ('second_z4', 'Z4_PARTNER_BOUND', lambda: require_z4_pair(4, 4, 1)),
    ]
    return [expect_failure(name, reason, action) for name, reason, action in cases]


def main():
    global DEADLINE
    parser = argparse.ArgumentParser()
    parser.add_argument('--seconds', type=float, default=180.0,
                        help='cooperative time ceiling, greater than 0 and at most 300 seconds')
    args = parser.parse_args()
    if not math.isfinite(args.seconds) or not (0 < args.seconds <= 300):
        print(json.dumps({'status': 'INVALID_LIMIT'}), flush=True)
        return 2
    started = time.monotonic()
    DEADLINE = started + args.seconds
    signal.signal(signal.SIGINT, request_stop)
    signal.signal(signal.SIGTERM, request_stop)
    try:
        profiles = profile_universe()
        projections = {tuple(v[4:8]) for v in profiles}
        results = {'E_allocations': inventory_e_allocations(),
                   'controls': controls(projections),
                   'same_X_fixtures': [check_fixture(False), check_fixture(True)],
                   'same_X_graph_profiles': same_x_graph_profiles(projections),
                   'mate_factorization': mate_parities(),
                   'phase_common_Y_parity': phase_and_common_y_parity(),
                   'paired_integer_cases': integer_cases(),
                   'physical_Z4_boundary': z4_boundary()}
        guard()
        print(json.dumps({'status': 'PASS_FINITE_SCOPES_ONLY', 'results': results,
                          'elapsed_seconds': time.monotonic() - started}, sort_keys=True), flush=True)
        return 0
    except Incomplete:
        print(json.dumps({'status': 'INCOMPLETE', 'reason': 'signal_or_cooperative_deadline',
                          'elapsed_seconds': time.monotonic() - started}), flush=True)
        return 3
    except Finding as exc:
        print(json.dumps({'status': 'FAIL', 'reason': exc.reason, 'detail': exc.detail,
                          'elapsed_seconds': time.monotonic() - started}, sort_keys=True), flush=True)
        return 1
    except Exception as exc:
        print(json.dumps({'status': 'ERROR', 'type': type(exc).__name__, 'detail': str(exc),
                          'elapsed_seconds': time.monotonic() - started}, sort_keys=True), flush=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())

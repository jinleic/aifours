#!/usr/bin/env python3
"""Prospective f719 partial-spectrum assay. NOT RUN BY AUTHOR.

Standalone standard-library only.  No input, subprocesses, network or file
writes; one JSON record on stdout.  Parent must first read this entire source,
pin it, and grant a separate one-shot GO.  Monotonic cooperative limit 45 s;
parent external limit <=55 s.  This checks the larger-class equality boundary
and one explicit physical x only; it neither chooses A0 nor exhausts 24 signs.
"""
import itertools
import json
import math
import signal
import sys
import time
from collections import Counter

START = time.monotonic()
STOP = False

def signal_stop(_signum, _frame):
    global STOP
    STOP = True

signal.signal(signal.SIGINT, signal_stop)
signal.signal(signal.SIGTERM, signal_stop)

class Failure(Exception):
    pass

class Reject(Exception):
    pass

class Stopped(Exception):
    pass

def guard():
    if STOP or time.monotonic() - START >= 45.0:
        raise Stopped('cooperative_limit_or_signal')

def need(condition, reason):
    if not condition:
        raise Failure(reason)

def expect_reject(reason, function, *args):
    try:
        function(*args)
    except Reject as exc:
        if str(exc) != reason:
            raise Failure('CONTROL_WRONG_REASON:' + reason + ':' + str(exc))
        return
    raise Failure('CONTROL_DID_NOT_REJECT:' + reason)

def character(mask, point):
    return 1 - 2 * ((mask & point).bit_count() & 1)

def fwht(values):
    out = list(values)
    width = 1
    while width < len(out):
        for base in range(0, len(out), 2 * width):
            for offset in range(width):
                i, j = base + offset, base + offset + width
                x, y = out[i], out[j]
                out[i], out[j] = x + y, x - y
        width *= 2
    return out

def direct_at(values, frequency):
    return sum(value * character(frequency, point)
               for point, value in enumerate(values))

def good_structure(kappa, sigma, f):
    if len(kappa) != 4 or any(k not in range(4) for k in kappa):
        raise Reject('KAPPA_DOMAIN')
    if len(sigma) != 4 or any(s not in (-1, 1) for s in sigma):
        raise Reject('SIGMA_DOMAIN')
    if len(f) != 4 or any(bit not in (0, 1) for bit in f):
        raise Reject('F_DOMAIN')
    if any(kappa.count(k) % 2 for k in range(4)):
        raise Reject('KAPPA_ODD_MULTIPLICITY')
    if sum(f) % 2 != 1:
        raise Reject('F_EVEN_PARITY')

def equality_d(kappa, sigma, nparity):
    # d_jb = -(-1)^n sigma_j (-1)^(kappa_j dot b), b=1,2,3.
    common = -character(1, nparity)
    return tuple(common * sigma[j] * character(kappa[j], b)
                 for j in range(4) for b in (1, 2, 3))

def partial_array(kappa, sigma, f, d):
    # Independent physical 32-cell ell=1 array, coordinates h,j,b.
    need(len(d) == 12 and all(x in (-1, 1) for x in d), 'D_DOMAIN')
    values = [0] * 32
    for j in range(4):
        for b in range(4):
            values[(f[j] << 4) | (j << 2) | b] = (
                sigma[j] * character(kappa[j], b))
        for b in (1, 2, 3):
            values[((1 ^ f[j]) << 4) | (j << 2) | b] = 2 * d[3*j+b-1]
    return values

def freq(s, alpha, beta):
    return (s << 4) | (beta << 2) | alpha

def aligned(v, active, beta):
    if len(active) != 2:
        raise Reject('BETA_ACTIVE_COUNT')
    i, j = active
    if v[i] * character(beta, i) != v[j] * character(beta, j):
        raise Reject('BETA_NOT_ALIGNED')

def full_frequency_requirements(values):
    # Necessary spectral constraints ONLY; does not construct a real y or A0.
    if len(values) != 64:
        raise Reject('FULL_LENGTH')
    if any(v % 8 != 4 for v in values):
        raise Reject('FULL_RESIDUE')
    if any(abs(v) > 12 for v in values):
        raise Reject('FULL_CAP')
    if sum(v*v for v in values) != 64 * 128:
        raise Reject('FULL_ENERGY')

def scope_guard(claim):
    if claim != 'fixed_x_partial_spectrum':
        raise Reject('SCOPE_' + claim)

def compare_profiles(measured, expected):
    for key in sorted(expected):
        if measured[key] != expected[key]:
            raise Reject('PROFILE_' + str(key[0]) + '_' + str(key[1]))

def compare_census(measured, expected):
    if tuple(measured) != tuple(expected):
        raise Reject('GRAPH_W0_CENSUS')

PROFILES = {
    (1, 0): ((0, 0, 0, 0), (-1, -1, -1, 1)),
    (0, 1): ((0, 1, 0, -1), (1, 0, 1, 0)),
    (1, 1): ((0, -1, 0, -1), (0, -1, 0, 1)),
    (0, 2): ((0, 0, -1, 1), (1, 1, 0, 0)),
    (1, 2): ((0, 0, 1, 1), (0, 0, -1, 1)),
    (0, 3): ((0, -1, 1, 0), (1, 0, 0, 1)),
    (1, 3): ((0, 1, -1, 0), (0, -1, -1, 0)),
}

def physical_reference():
    # Reconstructed from the literal f689 mathematical description, not code.
    f = (0, 0, 0, 1)
    z2 = {(1, 1, 2): 2, (1, 1, 3): -2,
          (2, 1, 1): -2, (2, 1, 3): 2,
          (3, 0, 1): 2, (3, 0, 2): -2}
    x, y, a, g = ([0] * 64 for _ in range(4))
    for ell in range(2):
        for h in range(2):
            for j in range(4):
                for b in range(4):
                    c = (ell << 5) | (h << 4) | (j << 2) | b
                    rho = 1 if b == 3 else -1
                    if ell == 1:
                        if h == f[j]:
                            a[c] = character(j, b)
                            g[c] = rho
                            x[c] = 1 if b == j else -1
                            y[c] = -a[c] * g[c] * x[c]
                        else:
                            g[c] = -2 * rho
                            if b == 0:
                                x[c] = 2
                            else:
                                y[c] = 2
                    elif b == 0:
                        g[c] = 4 if j == 0 else -2
                        if j != 0:
                            y[c] = 2
                    else:
                        x[c] = z2.get((j, h, b), 0)
                        if x[c] != 0:
                            y[c] = 2
                        elif (j, h, b) == (0, 0, 1):
                            y[c] = 4
    return x, y, a, g

def measured_profiles(x_t, t):
    result = {}
    for s, alpha in PROFILES:
        halves = []
        for ell in range(2):
            row = []
            for j in range(4):
                total = 0
                for h in range(2):
                    for b in range(4):
                        c = (ell << 5) | (h << 4) | (j << 2) | b
                        total += (x_t[c] * character(t, c)
                                  * character(s, h) * character(alpha, b))
                need(total % 4 == 0, 'PROFILE_NONINTEGRAL')
                row.append(total // 4)
            halves.append(tuple(row))
        result[(s, alpha)] = tuple(halves)
    return result

def physical_checks():
    x, y, a, g = physical_reference()
    need(sum(v*v for v in x) == 56, 'PHYSICAL_X_ENERGY')
    need(sum(v*v for v in y) == 128, 'PHYSICAL_Y_ENERGY')
    need(sum(v == 0 for v in y) == 23, 'PHYSICAL_Y_ZEROS')
    kappa, sigma, f = (3, 0, 0, 3), (1, -1, -1, -1), (0, 0, 0, 1)
    for j in range(4):
        for b in range(4):
            c = 32 | (f[j] << 4) | (j << 2) | b
            need(y[c] == sigma[j] * character(kappa[j], b), 'GRAPH_MATCH')
    graph_census = None
    off_counts = None
    for t in range(64):
        guard()
        xt = [x[c] * character(t, c) for c in range(64)]
        yt = [y[c] * character(t, c) for c in range(64)]
        xw, yw = fwht(xt), fwht(yt)
        need(xw == [direct_at(xt, q) for q in range(64)], 'X_WALSH_AGREEMENT')
        need(yw == [direct_at(yt, q) for q in range(64)], 'Y_WALSH_AGREEMENT')
        need(all(v in (-8, 0, 8) for v in xw), 'U0_CAP')
        zeros = {q for q in range(64) if xw[q] == 0}
        expected_zeros = {t ^ (nu << 5) ^ (beta << 2)
                          for nu in range(2) for beta in range(4)}
        need(zeros == expected_zeros and xw[t] == 0, 'CARRIED_ZERO')
        need(yw[t] == 44 and all(v % 8 == 4 for v in yw), 'Y_RESIDUE_OR_44')
        try:
            compare_profiles(measured_profiles(xt, t), PROFILES)
        except Reject as exc:
            raise Failure(str(exc))
        support = 0
        at_zero = 0
        by_b = [0, 0, 0, 0]
        off = [0, 0, 0, 0, 0]  # F,D0,D3,Z2,Z4
        for c in range(64):
            ell, h, j, b = (c >> 5) & 1, (c >> 4) & 1, (c >> 2) & 3, c & 3
            is_graph = ell == 1 and h == f[j]
            if is_graph:
                need(yt[c] == -a[c] * g[c] * xt[c], 'GRAPH_SAME_OBJECT')
            for w in range(4):
                numerator = (xt[c] + 3*a[c]*character(1, w)
                             + g[c]*character(2, w) + yt[c]*character(3, w))
                need(numerator % 4 == 0, 'INVERSE_NONINTEGRAL')
                value = numerator // 4
                need(value in (-1, 0, 1), 'INVERSE_NOT_TERNARY')
                support += value != 0
                if w == 0 and value != 0:
                    at_zero += 1
                    if t == 0:
                        if is_graph:
                            by_b[b] += 1
                        elif ell == 0 and b == 0 and j == 0:
                            off[0] += 1
                        elif ell == 1 and b == 0:
                            off[1] += 1
                        elif (ell == 1 and b != 0) or (ell == 0 and b == 0):
                            off[2] += 1
                        elif x[c] != 0:
                            off[3] += 1
                        elif y[c] != 0:
                            off[4] += 1
        need(support == 116 and at_zero % 2 == 1, 'SUPPORT_OR_J')
        if t == 0:
            graph_census, off_counts = tuple(by_b), tuple(off)
    try:
        compare_census(graph_census, (1, 2, 2, 4))
    except Reject as exc:
        raise Failure(str(exc))
    need(off_counts == (2, 4, 8, 3, 1), 'OFF_GRAPH_W0_CENSUS')
    return x, y, graph_census, off_counts

def check_uniform_boundary():
    kappas = [k for k in itertools.product(range(4), repeat=4)
              if all(k.count(a) % 2 == 0 for a in range(4))]
    fs = [f for f in itertools.product((0, 1), repeat=4) if sum(f) % 2 == 1]
    sigmas = list(itertools.product((-1, 1), repeat=4))
    need(len(kappas) == 40 and len(fs) == 8 and len(sigmas) == 16,
         'UNIVERSE_SIZE')
    shape_counts = Counter()
    consistent_counts = Counter()
    inconsistent_counts = Counter()
    magnitude_hist = Counter()
    witness_hist = Counter()
    zero_coefficients = 0
    zero_witness_cases = 0
    checked_cases = 0
    for kappa in kappas:
        guard()
        shape = 'all_same' if len(set(kappa)) == 1 else 'two_pairs'
        shape_counts[shape] += 1
        need(shape == 'all_same' or len(set(kappa)) == 2, 'KAPPA_CLASS')
        for sigma in sigmas:
            for f in fs:
                good_structure(kappa, sigma, f)
                for nparity in (0, 1):
                    d = equality_d(kappa, sigma, nparity)
                    actual_parity = sum(v == -1 for v in d) % 2
                    # kappa characters multiply to +1 over b=1,2,3.
                    need(math.prod(d) == math.prod(sigma), 'PRODUCT_IDENTITY')
                    need(math.prod(d) == character(1, actual_parity),
                         'NEGATIVE_PARITY_PRODUCT')
                    if actual_parity != nparity:
                        inconsistent_counts[shape] += 1
                        continue
                    consistent_counts[shape] += 1
                    checked_cases += 1
                    s = 1 ^ nparity
                    values = partial_array(kappa, sigma, f, d)
                    need(sum(v*v for v in values) == 64, 'PARTIAL_ARRAY_ENERGY')
                    transform = fwht(values)
                    v = tuple(sigma[j] * character(s, f[j]) for j in range(4))
                    need(math.prod(v) == -1, 'OPPOSITE_SLICE_PRODUCT')
                    found = []
                    for alpha in range(4):
                        for beta in range(4):
                            index = freq(s, alpha, beta)
                            direct = direct_at(values, index)
                            closed = sum(character(beta, j) * v[j]
                                         * (12 * (alpha == kappa[j]) - 2)
                                         for j in range(4))
                            need(direct == transform[index] == closed,
                                 'OPPOSITE_TRANSFORM_MISMATCH')
                            magnitude_hist[abs(direct)] += 1
                            zero_coefficients += direct == 0
                            if abs(direct) == 20:
                                found.append((alpha, beta))
                    if not found:
                        zero_witness_cases += 1
                    witness_hist[len(found)] += 1
                    need(len(found) == 4, 'OPPOSITE_WITNESS_COUNT')
                    alpha = kappa[0]
                    if shape == 'all_same':
                        beta = 0
                    else:
                        active = [j for j in range(4) if kappa[j] == alpha]
                        need(len(active) == 2, 'ACTIVE_PAIR')
                        beta = next(b for b in range(4)
                                    if v[active[0]] * character(b, active[0])
                                    == v[active[1]] * character(b, active[1]))
                        aligned(v, active, beta)
                    need(abs(direct_at(values, freq(s, alpha, beta))) == 20,
                         'CONSTRUCTIVE_BETA_WITNESS')
    need(shape_counts == {'all_same': 4, 'two_pairs': 36}, 'KAPPA_COUNTS')
    need(consistent_counts == {'all_same': 512, 'two_pairs': 4608},
         'CONSISTENT_COUNTS')
    need(inconsistent_counts == consistent_counts, 'INCONSISTENT_COUNTS')
    need(checked_cases == 5120 and zero_witness_cases == 0
         and zero_coefficients == 0, 'UNIFORM_ZERO_CASES')
    need(magnitude_hist == {4: 12*5120, 20: 4*5120}, 'MAGNITUDE_CENSUS')
    return {'kappa_shapes': dict(shape_counts),
            'parity_consistent_cases': dict(consistent_counts),
            'parity_mismatch_rejected': dict(inconsistent_counts),
            'cases_with_zero_abs20_witnesses': zero_witness_cases,
            'opposite_slice_zero_coefficients': zero_coefficients,
            'opposite_slice_magnitude_counts': dict(magnitude_hist),
            'per_case_number_of_abs20': dict(witness_hist),
            'direct_and_butterfly_frequencies_checked': 16 * checked_cases}

def check_fixed_x_partial():
    kappa, sigma, f = (3, 0, 0, 3), (1, -1, -1, -1), (0, 0, 0, 1)
    good_structure(kappa, sigma, f)
    cases, parity_counts, max_hist, eo_hist = 0, Counter(), Counter(), Counter()
    cap_pass = 0
    partial_cap_fail = 0
    forced_small_at_most_eight = 0
    first_slice_e_hist = Counter()
    zero_opposite_coefficients = 0
    for d in itertools.product((-1, 1), repeat=12):
        if cases % 16 == 0:
            guard()
        cases += 1
        n = sum(v == -1 for v in d) % 2
        parity_counts[n] += 1
        values = partial_array(kappa, sigma, f, d)
        transform = fwht(values)
        direct = [direct_at(values, q) for q in range(32)]
        need(direct == transform, 'ACTUAL_ALL32_DIRECT_WALSH')
        need(sum(v*v for v in values) == 64, 'ACTUAL_ELL1_ENERGY')
        need(sum(v*v for v in direct) == 32*64, 'ACTUAL_PARTIAL_PARSEVAL')
        for s in range(2):
            for alpha in range(4):
                for beta in range(4):
                    value = direct[freq(s, alpha, beta)]
                    need(value % 8 == (4*(n+s)) % 8, 'ACTUAL_RESIDUE')
                    if s == (1 ^ n) and value == 0:
                        zero_opposite_coefficients += 1
        first = [direct[freq(n, alpha, beta)]
                 for alpha in range(4) for beta in range(4)]
        second = [direct[freq(1 ^ n, alpha, beta)]
                  for alpha in range(4) for beta in range(4)]
        correlation = sum(sigma[j] * character(kappa[j], b) * d[3*j+b-1]
                          for j in range(4) for b in (1, 2, 3))
        need(sum((v//4)**2 for v in first) == 64 + 4*character(1, n)*correlation,
             'FIRST_SLICE_PARSEVAL_CORRELATION')
        maximum = max(abs(v) for v in direct)
        max_hist[maximum] += 1
        if maximum > 12:
            partial_cap_fail += 1
            continue
        cap_pass += 1
        need(all(abs(v) in (0, 8) for v in first), 'FIRST_SLICE_CAP_TYPES')
        need(all(abs(v) in (4, 12) for v in second), 'SECOND_SLICE_CAP_TYPES')
        e = sum(abs(v) == 8 for v in first)
        o = sum(abs(v) == 4 for v in second)
        first_slice_e_hist[e] += 1
        eo_hist[str(e) + ',' + str(o)] += 1
        need(4*e + o + 9*(16-o) == 128, 'EO_PARTIAL_ENERGY')
        need(2*o == 4 + e, 'EO_IDENTITY')
        need(e == 16 + character(1, n)*correlation and e >= 4, 'E_LOWER_BOUND')
        if e + o <= 8:
            forced_small_at_most_eight += 1
            # Under a full residue+cap hypothesis E+O<=8; with E>=4 and
            # O=2+E/2, equality forces d=equality_d and its opposite |20|.
            need(e == 4 and o == 4, 'EO_BOUNDARY_ALGEBRA')
            need(d == equality_d(kappa, sigma, n), 'EQUALITY_SIGNS')
            raise Failure('CAP_PASS_CONTRADICTS_EQUALITY_WITNESS')
    need(cases == 4096 and cap_pass + partial_cap_fail == cases,
         'ACTUAL_4096_CENSUS')
    need(parity_counts == {0: 2048, 1: 2048}, 'ACTUAL_PARITY_CENSUS')
    need(zero_opposite_coefficients == 0, 'ACTUAL_OPPOSITE_ZERO')
    # Exercise the boundary even if no actual partial-cap case exists.
    d = equality_d(kappa, sigma, 1)
    need(sum(v == -1 for v in d) % 2 == 1, 'BOUNDARY_N_PARITY')
    arr = partial_array(kappa, sigma, f, d)
    first = [direct_at(arr, freq(1, a, b)) for a in range(4) for b in range(4)]
    need(all(abs(v) in (0, 8) for v in first)
         and sum(abs(v) == 8 for v in first) == 4, 'BOUNDARY_E_FOUR')
    need(direct_at(arr, freq(0, 3, 1)) == 20, 'BOUNDARY_ACTUAL_20')
    return {'actual_d_sign_vectors': cases, 'n_parity_counts': dict(parity_counts),
            'all32_direct_vs_butterfly_frequency_pairs': 32*cases,
            'maximum_abs_A1_histogram': dict(max_hist),
            'partial_cap_fail': partial_cap_fail,
            'partial_cap_pass': cap_pass,
            'partial_cap_pass_E_histogram': dict(first_slice_e_hist),
            'partial_cap_pass_E_O_histogram': dict(eo_hist),
            'partial_cap_pass_forced_small_at_most_eight': forced_small_at_most_eight,
            'opposite_slice_zero_coefficients': zero_opposite_coefficients,
            'boundary_E4_opposite_witness': {'s': 0, 'alpha': 3,
                                            'beta': 1, 'A1': 20},
            'A0_chosen': False}

def run_controls(x):
    controls = []
    sigma = (1, 1, 1, 1)
    odd_f = (0, 0, 0, 1)
    odd_k = (0, 0, 0, 1)
    expect_reject('KAPPA_ODD_MULTIPLICITY', good_structure, odd_k, sigma, odd_f)
    controls.append('odd_kappa_multiplicity_guard')
    expect_reject('F_EVEN_PARITY', good_structure, (0, 0, 0, 0), sigma, (0, 0, 0, 0))
    controls.append('even_f_guard')
    # Two actual partial arrays show the |20| boundary conclusion can fail
    # when the stated structural hypothesis is removed; neither is a full-y
    # counterexample to the lemma, and neither is a capped physical witness.
    for label, kappa, f, expected_max in (
            ('odd_kappa', odd_k, odd_f, 32),
            ('even_f', (0, 0, 0, 0), (0, 0, 0, 0), 40)):
        d = equality_d(kappa, sigma, 0)
        need(sum(v == -1 for v in d) % 2 == 0, 'MUTANT_N_PARITY_' + label)
        arr = partial_array(kappa, sigma, f, d)
        vals = [direct_at(arr, freq(1, a, b)) for a in range(4) for b in range(4)]
        need(all(abs(v) != 20 for v in vals), 'MUTANT_HAS_20_' + label)
        need(max(abs(v) for v in vals) == expected_max, 'MUTANT_MAX_' + label)
        controls.append(label + '_actual_partial_array_no_20')
    fake_full = [4]*8 + [12]*56
    full_frequency_requirements(fake_full)
    expect_reject('FULL_RESIDUE', full_frequency_requirements, [0] + fake_full[1:])
    controls.append('wrong_residue_structural_guard')
    expect_reject('FULL_ENERGY', full_frequency_requirements, [12]*64)
    controls.append('wrong_energy_structural_guard')
    measured = measured_profiles(x, 0)
    for alpha in (1, 2, 3):
        wrong = dict(PROFILES)
        key = (1, alpha)
        wrong[key] = (wrong[key][0], tuple(-v for v in wrong[key][1]))
        expect_reject('PROFILE_1_' + str(alpha), compare_profiles, measured, wrong)
        controls.append('wrong_profile_row_' + str(alpha))
    expect_reject('GRAPH_W0_CENSUS', compare_census, (1, 2, 2, 4), (3, 2, 2, 0))
    controls.append('wrong_graph_w0_census')
    v, active = (1, -1, -1, -1), (0, 3)
    expect_reject('BETA_NOT_ALIGNED', aligned, v, active, 0)
    aligned(v, active, 1)
    controls.append('beta_selection_wrong_then_correct')
    scope_guard('fixed_x_partial_spectrum')
    for claim in ('all_x', 'whole_branch', 'V', 'global_boolean',
                  'full_24_sign_exhaustion', 'A0_chosen'):
        expect_reject('SCOPE_' + claim, scope_guard, claim)
        controls.append('scope_' + claim)
    return {'intended_reason_controls': controls,
            'fake_full_spectrum_is_not_a_realization': True,
            'mutant_partial_arrays_are_not_lemma_counterexamples': True}

def main():
    uniform = check_uniform_boundary()
    x, _y, graph, off = physical_checks()
    fixed = check_fixed_x_partial()
    controls = run_controls(x)
    guard()
    return {'marker': 'COMPLETE_PARTIAL_SPECTRUM_ONLY',
            'uniform_equality_boundary': uniform,
            'independently_reconstructed_fixed_x': {
                'transports': 64, 'reference_graph_w0_by_b': graph,
                'reference_offgraph_F_D0_D3_Z2_Z4_w0': off,
                'reference_yhat_at_carried_t': 44},
            'fixed_x_d_enumeration': fixed, 'controls': controls,
            'scope': {'actual_full_A0_selected': False,
                      '24_signs_exhausted': False, 'V_checked': False,
                      'other_x_or_global_checked': False},
            'elapsed_seconds': time.monotonic() - START}

if __name__ == '__main__':
    try:
        result = main()
        print(json.dumps(result, sort_keys=True, separators=(',', ':')), flush=True)
    except Stopped as exc:
        print(json.dumps({'marker': 'INCOMPLETE', 'reason': str(exc)}), flush=True)
        sys.exit(2)
    except Exception as exc:
        print(json.dumps({'marker': 'FAIL', 'reason': type(exc).__name__ + ':' + str(exc)}), flush=True)
        sys.exit(1)

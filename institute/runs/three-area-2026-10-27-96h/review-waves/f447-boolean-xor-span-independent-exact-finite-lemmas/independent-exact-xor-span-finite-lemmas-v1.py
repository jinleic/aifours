#!/usr/bin/env python3
"""F447 independent finite lemmas. All generated fixtures are FORMALSHADOW.
No files, network, subprocesses, randomness, author-program imports or dependencies.
This source is NOTRUN in its authoring child. It does not certify an actual U/V.
"""
import argparse
from collections import Counter
from itertools import product
import sys
from time import monotonic

A = (0, 1, 2, 4)
X = 7
EVEN_NONZERO = (3, 5, 6)
ACTIVE_D = (0, 1, 2, 4, 7)
DEADLINE = None


class InvariantFailure(Exception):
    def __init__(self, reason, detail=""):
        self.reason = reason
        super().__init__(reason + (": " + detail if detail else ""))


def need(condition, reason, detail=""):
    if not condition:
        raise InvariantFailure(reason, detail)


def tick():
    if DEADLINE is not None and monotonic() >= DEADLINE:
        raise TimeoutError("55-second-or-smaller cooperative bound reached")


def chi(r, c):
    return -1 if (r & c).bit_count() & 1 else 1


def signs(n):
    for mask in range(1 << n):
        yield tuple(-1 if (mask >> j) & 1 else 1 for j in range(n))


def sign_product(values):
    result = 1
    for value in values:
        result *= value
    return result


def walsh(values):
    tick()
    out = list(values)
    n = len(out)
    need(n > 0 and n & (n - 1) == 0, "WALSH_POWER_OF_TWO")
    width = 1
    while width < n:
        for start in range(0, n, 2 * width):
            for j in range(start, start + width):
                left, right = out[j], out[j + width]
                out[j], out[j + width] = left + right, left - right
        width *= 2
    return tuple(out)


def direct_walsh(values):
    return tuple(sum(value * chi(r, c) for c, value in enumerate(values))
                 for r in range(len(values)))


def balanced_residue(value):
    residue = value % 3
    return -1 if residue == 2 else residue


def xor_of(values):
    result = 0
    for value in values:
        result ^= value
    return result


def check_A(a_set):
    need(len(a_set) == 4 and len(set(a_set)) == 4
         and all(type(r) is int and 0 <= r < 64 for r in a_set),
         "FOUR_DISTINCT_FREQUENCIES")
    x = xor_of(a_set)
    need(x != 0, "A_XOR_NONZERO")
    need(set(a_set).isdisjoint({r ^ x for r in a_set}), "A_AX_DISJOINT")
    return x


def sets_from_signs(a_set, eps):
    x = check_A(a_set)
    need(len(eps) == 4 and all(v in (-1, 1) for v in eps), "SMALL_SIGNS")
    e = sign_product(eps)
    E = {c for c in range(64)
         if len({eps[j] * chi(r, c) for j, r in enumerate(a_set)}) == 1}
    B = {c for c in range(64) if e * chi(x, c) == -1}
    return E, B


def check_spectral_pattern(spectrum, a_set):
    check_A(a_set)
    a_lookup = set(a_set)
    need(len(spectrum) == 64 and all(type(v) is int for v in spectrum),
         "INTEGER_64_SPECTRUM")
    need(all(abs(v) == (4 if r in a_lookup else 12)
             for r, v in enumerate(spectrum)), "ACTUAL_4_12_PATTERN")


def check_forced_signs(spectrum, a_set):
    check_spectral_pattern(spectrum, a_set)
    x = xor_of(a_set)
    eps = tuple(spectrum[r] // 4 for r in a_set)
    e = sign_product(eps)
    need(all(spectrum[r ^ x] == -12 * e * eps[j]
             for j, r in enumerate(a_set)), "SIGNED_XOR_FORCE")


def shell_spectrum(eps):
    # Spectral shell ONLY: inverse need not be integral or an actual block value.
    out = [12] * 64
    e = sign_product(eps)
    for j, r in enumerate(A):
        out[r] = 4 * eps[j]
        out[r ^ X] = -12 * e * eps[j]
    return tuple(out)


def check_actual_g_range(spectrum):
    # Necessary local test only; passing would NOT certify a shared actual u/V.
    for c, numerator in enumerate(walsh(spectrum)):
        need(numerator % 64 == 0, "ACTUAL_G_INTEGRAL", "c=" + str(c))
        need(numerator // 64 in (0, -1, 1, -2, 2, -4, 4),
             "ACTUAL_BLOCK_RANGE", "c=" + str(c))


def check_kappa_denominator(denominator):
    for c in range(64):
        inverse_numerator = walsh(tuple(chi(r, c) for r in range(64)))
        need(all(value == denominator * (4 if h == c else 0)
                 for h, value in enumerate(inverse_numerator)),
             "INVERSE_KAPPA_DENOMINATOR")


def check_residue_model(model, expected):
    need(set(model) == {-1, 0, 1}
         and all(set(model[rho]) == set(expected[rho]) for rho in expected),
         "MOD3_ALLOWED_VALUES_COMPLETE")


def check_shared_phase(a_values, sigma):
    need(len(a_values) == 64 and all(v in (-1, 0, 1) for v in a_values)
         and sum(v != 0 for v in a_values) == 16, "TERNARY_16_PHASE_FIXTURE")
    need(len(sigma) == 64 and all(v in (-1, 1) for v in sigma), "FLAT_PHASE_SIGNS")
    need(walsh(a_values) == tuple(4 * v for v in sigma), "SHARED_PHASE")


def gf2_rank(vectors):
    pivots = {}
    for value in vectors:
        while value:
            bit = value.bit_length() - 1
            if bit in pivots:
                value ^= pivots[bit]
            else:
                pivots[bit] = value
                break
    return len(pivots)


def check_E_inverse(coefficients):
    need(len(coefficients) == 8 and all(v in (-4, 0, 4) for v in coefficients),
         "E_PARTIAL_COEFFICIENTS")
    m0 = sum(v * v for v in coefficients) // 8
    need(m0 in (0, 2, 4), "E_OCCUPANCY_BOUND")
    numerators = walsh(coefficients)
    need(all(v % 8 == 0 for v in numerators), "K_INVERSE_INTEGRAL")
    a0 = tuple(v // 8 for v in numerators)
    need(all(v in (-1, 0, 1) for v in a0), "E_TERNARY_INVERSE")
    support = [h for h, v in enumerate(a0) if v]
    need(len(support) == m0, "E_PARSEVAL_SUPPORT")
    if m0 == 4:
        need(gf2_rank(h ^ support[0] for h in support) == 2, "E_AFFINE_TWO_FLAT")
    return a0


def check_occupancy(m, f):
    need(len(m) == len(f) == 5
         and all(type(v) is int and 0 <= v <= 8 for v in m)
         and all(type(v) is int and 0 <= v <= 2 for v in f), "OCCUPANCY_DOMAIN")
    need(sum(m) == 16 and sum(f) == 2, "GLOBAL_16S_2F")
    need(all(m[j] + 2 * f[j] == 4 for j in range(5)), "FIVE_COSET_IDENTITY")
    need(m[0] in (0, 4), "E_OCCUPANCY_MOD4")


def structure_group(sigma):
    answer = {}
    for t in range(64):
        factor = sigma[t] * sigma[0]
        if all(sigma[r ^ t] == factor * sigma[r] for r in range(64)):
            answer[t] = factor
    return answer


def support_group(a_values):
    support = [c for c, value in enumerate(a_values) if value]
    return {t: chi(t, support[0]) for t in range(64)
            if all(chi(t, c) == chi(t, support[0]) for c in support)}


def phase_fixture():
    # FORMALSHADOW: bent signs on a four-flat, NOT an actual 4/12 caller.
    values = []
    for c in range(64):
        d0, d1 = c & 1, (c >> 1) & 1
        h0, h1 = (c >> 3) & 1, (c >> 4) & 1
        if (c & 7).bit_count() % 2 == 1 and c & 32 == 0:
            values.append(-1 if (d0 * d1 + h0 * h1) % 2 else 1)
        else:
            values.append(0)
    return tuple(values)


def expect_rejection(name, reason, action, controls):
    tick()
    try:
        action()
    except InvariantFailure as failure:
        need(failure.reason == reason, "MUTATION_WRONG_REASON",
             name + ": " + str(failure))
        controls.append((name, reason))
        return
    raise InvariantFailure("MUTATION_ACCEPTED", name)


def run(seconds):
    global DEADLINE
    started = monotonic()
    DEADLINE = started + seconds
    stats = {}
    controls = []
    for n in (8, 64):
        for c in range(n):
            delta = tuple(int(h == c) for h in range(n))
            transformed = walsh(delta)
            need(transformed == tuple(chi(r, c) for r in range(n)), "WALSH_BASIS")
            need(walsh(transformed) == tuple(n * v for v in delta), "WALSH_SQUARE")
    check_kappa_denominator(16)
    stats["Walsh_basis_vectors"] = 72

    on, off, eligible = set(), set(), 0
    for block in product((-1, 0, 1), repeat=4):
        u1 = sum(block[w] * chi(1, w) for w in range(4))
        u2 = sum(block[w] * chi(2, w) for w in range(4))
        if u1 not in (0, -3, 3):
            continue
        eligible += 1
        support_size = sum(v != 0 for v in block)
        if u1:
            need(support_size == 3 and u2 in (-1, 1), "ACTUAL_ON_BLOCK")
            on.add(u2)
        else:
            need(support_size % 2 == 0 and u2 in (0, -2, 2, -4, 4), "ACTUAL_OFF_BLOCK")
            off.add(u2)
    need(on == {-1, 1} and off == {0, -2, 2, -4, 4}, "LOCAL_BLOCK_EXHAUSTIVE")
    residues = {rho: {v for v in on | off if balanced_residue(v) == rho}
                for rho in (-1, 0, 1)}
    need(residues == {-1: {-4, -1, 2}, 0: {0}, 1: {-2, 1, 4}}, "ACTUAL_MOD3_TABLE")
    check_residue_model(residues, residues)
    stats["ternary_blocks_examined"] = 81
    stats["eligible_local_blocks"] = eligible

    rho0 = tuple((1, -1, -1, 0, -1, 0, 0, 1)[c & 7] for c in range(64))
    gauge_count, scalar_count = 0, 0
    need([f for f in range(25) if 16 + 4 * (24 - f) + 16 * f == 136] == [2],
         "PARSEVAL_TWO_FULL_BLOCKS")
    for eps in signs(4):
        tick()
        e = sign_product(eps)
        P = tuple(sum(eps[j] * chi(r, c) for j, r in enumerate(A)) for c in range(64))
        rho = tuple(balanced_residue(v) for v in P)
        E, B = sets_from_signs(A, eps)
        need(len(E) == 8 and len(B) == 32 and E.isdisjoint(B), "E_B_GEOMETRY")
        need({c for c, v in enumerate(rho) if v} == E | B, "RHO_FULL_64_SUPPORT")
        need(all(8 * rho[c] == -P[c] + 3 * e * chi(X, c) * P[c]
                 for c in range(64)), "RHO_CUBIC_IDENTITY")
        expected_hat = [0] * 64
        for j, r in enumerate(A):
            expected_hat[r] = -8 * eps[j]
            expected_hat[r ^ X] = 24 * e * eps[j]
        rho_hat = walsh(rho)
        need(rho_hat == tuple(expected_hat) == direct_walsh(rho), "RHO_SPECTRUM")
        tau = sum((1 << j) for j in range(3) if eps[j + 1] != eps[0])
        normalizers = {t for t in range(64)
                       if all(eps[0] * eps[j] * chi(r, t) == 1
                              for j, r in enumerate(A))}
        need(normalizers == {tau | (h << 3) for h in range(8)}, "ALL_SIGN_NORMALIZERS")
        for t in normalizers:
            need(tuple(eps[0] * rho[c ^ t] for c in range(64)) == rho0,
                 "RHO_TRANSLATION_NORMALIZATION")
            gauge_count += 1
        winners = []
        for eta in signs(4):
            numerator = sum(4 * eps[j] * rho_hat[r] for j, r in enumerate(A))
            numerator += sum(12 * eta[j] * rho_hat[r ^ X] for j, r in enumerate(A))
            scalar_count += 1
            if numerator == 64 * (-2 * 40 + 3 * 16 + 6 * 2):
                winners.append(eta)
        need(winners == [tuple(-e * v for v in eps)], "EXTREME_FOUR_SIGN_CLASSIFICATION")
        shell = shell_spectrum(eps)
        check_forced_signs(shell, A)
        need(sum(v * v for v in shell) == 64 * 136, "ACTUAL_SPECTRAL_ENERGY")
    stats["small_sign_assignments"] = 16
    stats["translation_normalizers"] = gauge_count
    stats["scalar_four_sign_cases"] = scalar_count

    row_histogram = Counter()
    for sigma8 in signs(8):
        transform = walsh(sigma8)
        need(transform == direct_walsh(sigma8), "EIGHT_POINT_DIRECT_WALSH")
        restricted = all(transform[d] == 0 for d in EVEN_NONZERO)
        pair_sums = {sigma8[z] + sigma8[z ^ 7] for z in range(8)}
        need(restricted == (len(pair_sums) == 1), "EVEN_RESTRICTION_PAIR_SUM_EQUIVALENCE")
        if restricted:
            need(transform[0] % 2 == 0, "PARTIAL_HALF_NORMALIZATION")
            a0 = transform[0] // 2
            need(a0 in (-4, 0, 4), "A0_ZERO_OR_FOUR")
            if a0:
                need(len(set(sigma8)) == 1, "EXTREME_ROW_CONSTANT")
            else:
                need(all(sigma8[z ^ 7] == -sigma8[z] for z in range(8)), "ROW_ANTI_INVARIANCE")
            row_histogram[a0] += 1
    need(row_histogram == Counter({-4: 1, 0: 16, 4: 1}), "ALL_256_ROW_CLASSIFICATION")
    stats["eight_sign_rows_examined"] = 256
    stats["restricted_rows"] = sum(row_histogram.values())

    integral_E, half_E, bounded_E = 0, 0, 0
    for coefficients in product((-4, 0, 4), repeat=8):
        inverse_numerator = walsh(coefficients)
        N = sum(v != 0 for v in coefficients)
        integral = all(v % 8 == 0 for v in inverse_numerator)
        need(integral == (N % 2 == 0), "K_CHARACTER_SUM_PARITY")
        if N > 2:
            continue
        bounded_E += 1
        if N == 1:
            try:
                check_E_inverse(coefficients)
            except InvariantFailure as failure:
                need(failure.reason == "K_INVERSE_INTEGRAL", "TWO_ATOM_REJECTION_REASON")
            else:
                raise InvariantFailure("TWO_ATOM_BRANCH_ACCEPTED")
            half_E += 1
        else:
            check_E_inverse(coefficients)
            integral_E += 1
    need((bounded_E, integral_E, half_E) == (129, 113, 16), "ALL_E_INVERSE_CLASSIFICATION")
    stats["partial_coefficient_vectors_examined"] = 3 ** 8
    stats["bounded_E_vectors"] = bounded_E
    stats["integral_E_vectors"] = integral_E
    stats["half_integral_two_atom_vectors"] = half_E

    local_patterns, forbidden_E = 0, 0
    occupancy_classes = Counter()
    for f in product(range(3), repeat=5):
        if sum(f) != 2:
            continue
        local_patterns += 1
        m = tuple(4 - 2 * v for v in f)
        if m[0] == 2:
            forbidden_E += 1
            continue
        check_occupancy(m, f)
        occupancy_classes[(f[0], tuple(sorted(f[1:], reverse=True)))] += 1
    need(local_patterns == 15 and forbidden_E == 4, "LOCAL_OCCUPANCY_EXHAUSTIVE")
    need(occupancy_classes == Counter({(2, (0, 0, 0, 0)): 1,
                                      (0, (2, 0, 0, 0)): 4,
                                      (0, (1, 1, 0, 0)): 6}), "EXACT_THREE_OCCUPANCY_CLASSES")
    stats["labelled_local_occupancy_patterns"] = local_patterns
    stats["labelled_final_occupancy_patterns"] = sum(occupancy_classes.values())

    a_values = phase_fixture()
    a_hat = walsh(a_values)
    need(all(abs(v) == 4 for v in a_hat), "SHADOW_BENT_FLAT_PHASE")
    sigma = tuple(v // 4 for v in a_hat)
    check_shared_phase(a_values, sigma)
    original_group = structure_group(sigma)
    need(original_group == support_group(a_values)
         == {0: 1, 7: -1, 32: 1, 39: -1}, "SHADOW_PHASE_SUPPORT_EQUIVALENCE")
    g_values, g_hat = rho0, walsh(rho0)
    canonical_shell = shell_spectrum((1, 1, 1, 1))
    E0, B0 = sets_from_signs(A, (1, 1, 1, 1))
    transported = 0
    for t in range(64):
        shifted_a = tuple(a_values[c ^ t] for c in range(64))
        expected_group = {n: value * chi(n, t) for n, value in original_group.items()}
        need(support_group(shifted_a) == expected_group, "SUPPORT_TRANSLATION_PHASE")
        for modulation in range(64):
            translated_A = tuple(r ^ modulation for r in A)
            for gamma in (-1, 1):
                tick()
                at = tuple(gamma * chi(modulation, c) * a_values[c ^ t] for c in range(64))
                gt = tuple(gamma * chi(modulation, c) * g_values[c ^ t] for c in range(64))
                sigma_t = tuple(gamma * chi(r ^ modulation, t) * sigma[r ^ modulation]
                                for r in range(64))
                predicted_g = tuple(gamma * chi(r ^ modulation, t) * g_hat[r ^ modulation]
                                    for r in range(64))
                check_shared_phase(at, sigma_t)
                need(walsh(gt) == predicted_g, "CHARACTER_GAUGE_FOURIER_TRANSPORT")
                need(structure_group(sigma_t) == expected_group, "PHASE_STRUCTURE_TRANSPORT")
                shell_t = tuple(gamma * chi(r ^ modulation, t) * canonical_shell[r ^ modulation]
                                for r in range(64))
                check_forced_signs(shell_t, translated_A)
                eps_t = tuple(shell_t[r] // 4 for r in translated_A)
                Et, Bt = sets_from_signs(translated_A, eps_t)
                need(Et == {c ^ t for c in E0} and Bt == {c ^ t for c in B0},
                     "INTRINSIC_E_B_TRANSPORT")
                transported += 1
    need(transported == 8192, "TRANSPORT_DOMAIN_EXHAUSTIVE")
    stats["common_gauge_transport_cases"] = transported

    expect_rejection("wrong-Walsh-kappa-normalization", "INVERSE_KAPPA_DENOMINATOR",
                     lambda: check_kappa_denominator(64), controls)
    bad_spectrum = list(canonical_shell)
    bad_spectrum[8] = 4
    expect_rejection("missing-4-12-pattern", "ACTUAL_4_12_PATTERN",
                     lambda: check_spectral_pattern(bad_spectrum, A), controls)
    expect_rejection("xor-zero-affine-four-set", "A_XOR_NONZERO",
                     lambda: check_A((0, 1, 2, 3)), controls)
    unsigned = list(canonical_shell)
    unsigned[A[0] ^ X] *= -1
    check_spectral_pattern(unsigned, A)
    expect_rejection("unsigned-forced-sign", "SIGNED_XOR_FORCE",
                     lambda: check_forced_signs(unsigned, A), controls)
    for rho in (-1, 0, 1):
        for value in sorted(residues[rho]):
            missing = {r: set(values) for r, values in residues.items()}
            missing[rho].remove(value)
            expect_rejection("missing-mod3-case-" + str(value), "MOD3_ALLOWED_VALUES_COMPLETE",
                             lambda model=missing: check_residue_model(model, residues), controls)
    unshared = list(sigma)
    unshared[0] *= -1
    expect_rejection("unshared-flat-phase", "SHARED_PHASE",
                     lambda: check_shared_phase(a_values, unshared), controls)
    expect_rejection("inverse-K-two-atom-branch", "K_INVERSE_INTEGRAL",
                     lambda: check_E_inverse((4, 0, 0, 0, 0, 0, 0, 0)), controls)
    expect_rejection("occupancy-two-atom-E-branch", "E_OCCUPANCY_MOD4",
                     lambda: check_occupancy((2, 2, 4, 4, 4), (1, 1, 0, 0, 0)), controls)
    check_forced_signs(canonical_shell, A)
    need(walsh(canonical_shell)[0] == 640, "SHADOW_EXACT_INVERSE_AT_ZERO")
    expect_rejection("spectral-shell-is-not-actual-g", "ACTUAL_BLOCK_RANGE",
                     lambda: check_actual_g_range(canonical_shell), controls)
    need(len(controls) == 15, "MUTATION_COUNT")
    tick()
    print("STATUS: FINITE_LEMMAS_AND_CONTROLS_COMPLETED")
    print("FIXTURES: FORMALSHADOW_ONLY; NO_ACTUAL_U_OR_V_CERTIFIED")
    for name, value in stats.items():
        print(name + ": " + str(value))
    print("row_A0_histogram: " + str(sorted(row_histogram.items())))
    print("occupancy_class_multiplicities: " + str(sorted(occupancy_classes.items())))
    for name, reason in controls:
        print("CONTROL_REJECTED: " + name + " => " + reason)
    print("controls_rejected_for_intended_reason: " + str(len(controls)))
    print("elapsed_monotonic_seconds: " + format(monotonic() - started, ".6f"))
    print("SCOPE: finite lemmas only; universal target/adoption/novelty/family/human/kernel UNPAID")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-seconds", type=float, default=55.0)
    args = parser.parse_args()
    if not 0 < args.max_seconds <= 55:
        parser.error("--max-seconds must be positive and at most 55")
    try:
        return run(args.max_seconds)
    except TimeoutError as failure:
        print("STATUS: NOT_COMPLETED: " + str(failure), file=sys.stderr)
        return 2
    except InvariantFailure as failure:
        print("STATUS: INVARIANT_FAILURE: " + str(failure), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

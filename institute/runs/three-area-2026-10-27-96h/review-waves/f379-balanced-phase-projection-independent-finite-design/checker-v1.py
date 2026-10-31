import sys
from itertools import combinations, product
from time import monotonic

START = monotonic()
DEADLINE = START + 50.0
CHECK_COUNT = 0
NEGATIVE_RESULTS = []


class IdentityError(Exception):
    def __init__(self, identity, detail=""):
        self.identity = identity
        text = identity if not detail else identity + ": " + detail
        super().__init__(text)


class BudgetExpired(Exception):
    pass


def guard():
    if monotonic() >= DEADLINE:
        raise BudgetExpired("cooperative 50-second deadline reached")


def need(condition, identity, detail=""):
    global CHECK_COUNT
    guard()
    if not condition:
        raise IdentityError(identity, detail)
    CHECK_COUNT += 1


def reject(name, identity, operation):
    guard()
    try:
        operation()
    except IdentityError as error:
        need(
            error.identity == identity,
            "negative.wrong_reason",
            name + " raised " + error.identity + ", expected " + identity,
        )
        NEGATIVE_RESULTS.append((name, identity))
        return
    raise IdentityError("negative.unexpected_acceptance", name)


def multiply(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def xor_all(values):
    answer = 0
    for value in values:
        answer ^= value
    return answer


def ceil_div(numerator, denominator):
    need(denominator > 0, "integer.positive_denominator")
    return -((-numerator) // denominator)


CHI = tuple(
    tuple(1 - 2 * ((x & y).bit_count() & 1) for y in range(64))
    for x in range(64)
)
QCHI = tuple(tuple(CHI[x][y] for y in range(4)) for x in range(4))
SUPPORT = tuple(range(16))
SUPPORT_SET = frozenset(SUPPORT)


def bent_sign(x):
    exponent = (
        ((x >> 0) & 1) * ((x >> 1) & 1)
        + ((x >> 2) & 1) * ((x >> 3) & 1)
    )
    return 1 - 2 * (exponent & 1)


SIGMA = [bent_sign(r) for r in range(64)]
A = [bent_sign(c) if c < 16 else 0 for c in range(64)]


def walsh(values):
    need(len(values) == 64, "walsh.length_64")
    answer = []
    for x in range(64):
        guard()
        answer.append(sum(CHI[x][y] * values[y] for y in range(64)))
    return answer


def convolution(left, right):
    need(
        len(left) == 64 and len(right) == 64,
        "convolution.length_64",
    )
    answer = []
    for t in range(64):
        guard()
        answer.append(sum(left[r] * right[r ^ t] for r in range(64)))
    return answer


def divide_exact(values, denominator, identity):
    need(
        all(value % denominator == 0 for value in values),
        identity,
        "nonintegral exact quotient",
    )
    return [value // denominator for value in values]


def local_transforms(raw):
    return [
        [
            sum(raw[c][w] * QCHI[s][w] for w in range(4))
            for c in range(64)
        ]
        for s in range(4)
    ]


def half_spectra(local):
    return [
        divide_exact(walsh(row), 2, "spectrum.even_full_transform")
        for row in local
    ]


def recover_common_phase(code, w0):
    need(len(code) == 4, "common.four_fibres")
    recovered = [
        divide_exact(walsh(row), 512, "common.inverse_factor_512")
        for row in code
    ]
    for s in range(4):
        for c in range(64):
            if c in SUPPORT_SET:
                need(
                    abs(recovered[s][c]) == 1,
                    "common.individual_support_sign",
                )
            else:
                need(
                    recovered[s][c] == 0,
                    "common.individual_support_zero",
                )
    theta = [0] * 64
    for c in SUPPORT:
        theta[c] = recovered[0][c]
        for s in range(4):
            need(
                recovered[s][c] * QCHI[s][w0[c]] == theta[c],
                "common.theta",
                "fibre=" + str(s) + ", c=" + str(c),
            )
    return recovered, theta


def validate_linked_template(translations, flips):
    need(
        len(translations) == 4 and len(flips) == 4,
        "linked.four_entries",
    )
    need(
        all(isinstance(t, int) and 0 <= t < 64 for t in translations),
        "linked.translation_range",
    )
    need(all(e in (-1, 1) for e in flips), "linked.flip_signs")
    need(xor_all(translations) == 0, "linked.shift_xor")
    need(multiply(flips) == -1, "linked.epsilon_product")


SHIFT_SAMPLES = (
    (0, 0, 0, 0),
    (0, 1, 2, 3),
    (1, 2, 4, 7),
    (3, 5, 8, 14),
    (16, 1, 32, 49),
    (63, 7, 21, 45),
    (0, 16, 32, 48),
    (5, 9, 34, 46),
)
FLIP_SAMPLES = tuple(
    flips for flips in product((-1, 1), repeat=4)
    if multiply(flips) == -1
)


def check_templates(fixture):
    code = fixture["C"]
    q = fixture["q"]
    z = fixture["z"]
    maxima = fixture["maxima"]
    absolute_sums = [sum(abs(value) for value in row) for row in z]
    need(
        all(value != 0 for row in z for value in row),
        "counts.nonzero_phases",
    )
    count = 0
    minimum_h = 257
    maximum_h = -1
    for translations in SHIFT_SAMPLES:
        for flips in FLIP_SAMPLES:
            guard()
            validate_linked_template(translations, flips)
            for c in SUPPORT:
                eta = [
                    flips[s] * q[s][c] * CHI[translations[s]][c]
                    for s in range(4)
                ]
                need(multiply(eta) == -1, "linked.local_product")
                need(sum(eta) in (-2, 2), "linked.local_sum")
            signed = sum(
                flips[s] * code[s][translations[s]] for s in range(4)
            )
            total_d = 0
            total_h = 0
            direct_signed = 0
            for s in range(4):
                h = 0
                d = 0
                correlation = 0
                for r in range(64):
                    target = flips[s] * SIGMA[r ^ translations[s]]
                    value = z[s][r]
                    correlation += target * value
                    if target * value < 0:
                        h += 1
                        d += abs(value)
                need(
                    correlation == flips[s] * code[s][translations[s]],
                    "counts.direct_correlation",
                )
                need(
                    correlation == absolute_sums[s] - 2 * d,
                    "counts.weighted_identity",
                )
                # Use the fixture's actual maximum, NOT the original cap 7.
                need(d <= maxima[s] * h, "counts.actual_maximum_bound")
                total_d += d
                total_h += h
                direct_signed += correlation
            need(direct_signed == signed, "linked.direct_count_agreement")
            need(
                signed == sum(absolute_sums) - 2 * total_d,
                "linked.total_weighted_identity",
            )
            need(abs(signed) <= 256, "linked.bound_256")
            minimum_h = min(minimum_h, total_h)
            maximum_h = max(maximum_h, total_h)
            count += 1
    need(count == 64, "linked.sample_count_64")
    return count, minimum_h, maximum_h


def build_and_check_fixture(mode):
    need(mode in ("indexed", "calibration"), "fixture.known_mode")
    u = [[0] * 4 for _ in range(64)]
    v = [[1] * 4 for _ in range(64)]
    w0 = [0] * 64
    b = [0] * 64
    for c in SUPPORT:
        guard()
        w0[c] = (c & 3) if mode == "indexed" else 0
        b[c] = CHI[1][c] if mode == "indexed" else A[c]
        for w in range(4):
            u[c][w] = 0 if w == w0[c] else A[c] * QCHI[1][w]
            v[c][w] = b[c] if w == w0[c] else 0
    v[16][0] = -1

    need(
        all(
            u[c][w] in (-1, 0, 1)
            and v[c][w] in (-1, 0, 1)
            and u[c][w] ** 2 + v[c][w] ** 2 == 1
            for c in range(64) for w in range(4)
        ),
        "raw.ternary_complementarity",
    )
    if mode == "indexed":
        need(
            {w0[c] for c in SUPPORT} == {0, 1, 2, 3},
            "fixture.all_missing_point_labels",
        )

    U = local_transforms(u)
    Z = local_transforms(v)
    k = half_spectra(U)
    z = half_spectra(Z)

    need(U[1] == [3 * value for value in A], "fixture.U1_3a")
    need(k[1] == [6 * value for value in SIGMA], "fixture.k1_6sigma")
    need(
        tuple(c for c in range(64) if U[1][c] != 0) == SUPPORT,
        "fixture.exact_sixteen_support",
    )

    # Independent direct 256-point sums check the Q-then-R indexing.
    for r in range(64):
        guard()
        for s in range(4):
            direct_u = 0
            direct_v = 0
            for c in range(64):
                for w in range(4):
                    sign = CHI[r][c] * QCHI[s][w]
                    direct_u += u[c][w] * sign
                    direct_v += v[c][w] * sign
            need(direct_u == 2 * k[s][r], "direct256.U_dispatch")
            need(direct_v == 2 * z[s][r], "direct256.V_dispatch")

    for s in range(4):
        need(walsh(z[s]) == [32 * x for x in Z[s]], "inverse.z_factor_32")
        need(walsh(k[s]) == [32 * x for x in U[s]], "inverse.k_factor_32")
    for c in range(64):
        for w in range(4):
            need(
                sum(Z[s][c] * QCHI[s][w] for s in range(4))
                == 4 * v[c][w],
                "inverse.Q_factor_4",
            )

    q = [[A[c] * Z[s][c] for c in range(64)] for s in range(4)]
    code = [convolution(SIGMA, z[s]) for s in range(4)]
    sigma_k = [convolution(SIGMA, k[s]) for s in range(4)]
    sigma_self = convolution(SIGMA, SIGMA)

    for s in range(4):
        need(
            code[s] == [8 * x for x in walsh(q[s])],
            "projection.factor_8",
        )
        need(
            walsh(code[s]) == [512 * x for x in q[s]],
            "projection.dual_factor_512",
        )
        need(all(x % 16 == 0 for x in code[s]), "code.divisible_by_16")
        need(max(abs(x) for x in code[s]) <= 128, "code.coordinate_128")
        need(sum(x * x for x in code[s]) == 65536, "code.norm_65536")
        need(
            convolution(code[s], code[s])
            == [1024 * x for x in sigma_self],
            "self.factor_1024",
        )

    for s, t in combinations(range(4), 2):
        j = s ^ t ^ 1
        need(j != 1, "cross.distinct_fibre_index")
        pointwise_product = [q[s][c] * q[t][c] for c in range(64)]
        need(
            pointwise_product == [-A[c] * U[j][c] for c in range(64)],
            "cross.local_product",
        )
        actual = convolution(code[s], code[t])
        need(
            actual == [4096 * x for x in walsh(pointwise_product)],
            "cross.walsh_factor_4096",
        )
        need(
            actual == [-512 * x for x in sigma_k[j]],
            "cross.factor_minus512",
        )

    recovered, theta = recover_common_phase(code, w0)
    need(recovered == q, "common.recovered_q")
    need(
        all(theta[c] == A[c] * b[c] for c in SUPPORT),
        "common.actual_theta",
    )
    for c in SUPPORT:
        for w in range(4):
            numerator = sum(
                A[c] * recovered[s][c] * QCHI[s][w]
                for s in range(4)
            )
            need(
                numerator == 4 * b[c] * int(w == w0[c]),
                "local.converse_singleton",
            )

    support_u = sum(value != 0 for row in u for value in row)
    support_v = sum(value != 0 for row in v for value in row)
    sum_u = sum(sum(row) for row in u)
    sum_v = sum(sum(row) for row in v)
    energies = tuple(sum(value * value for value in row) for row in Z)
    maxima = tuple(max(abs(value) for value in row) for row in z)
    expected_maxima = (95, 9, 9, 9) if mode == "indexed" else (97, 3, 3, 3)

    need((support_u, support_v) == (48, 208), "caller.raw_support_counts")
    need(sum_u == -4, "caller.balance_not_satisfied")
    need(
        sum_v == (190 if mode == "indexed" else 194),
        "caller.raw_v_sum",
    )
    need(sum_v % 4 == 2, "caller.v_sum_congruence_only")
    need(energies == (772, 20, 20, 20), "caller.actual_fixture_energies")
    need(maxima == expected_maxima, "caller.actual_fixture_maxima")
    need(sum(energies) == 4 * support_v == 832, "caller.actual_total_832")
    need(sum(energies) != 560, "caller.target_total_not_applicable")
    need(
        all(value % 2 != 0 for row in z for value in row),
        "caller.fixture_odd_nonzero",
    )
    need(
        not all(abs(value) <= 7 for row in z for value in row),
        "caller.original_cap_not_satisfied",
    )
    need(
        all((2 * value) % 4 == 0 for row in k for value in row),
        "caller.U_transform_in_4Z",
    )
    need(
        sum(k[s][r] * z[s][r] for s in range(4) for r in range(64)) == 0,
        "caller.mixed_spectral_inner_product",
    )
    need(
        sum(value == 0 for row in k for value in row) == 0,
        "caller.eight_zero_condition_not_satisfied",
    )

    xor_u = xor_all(
        4 * c + w
        for c in range(64) for w in range(4)
        if u[c][w] != 0
    )
    xor_v = xor_all(
        4 * c + w
        for c in range(64) for w in range(4)
        if v[c][w] != 0
    )
    need((xor_u, xor_v) == (0, 0), "caller.support_xors_only")

    fixture = {
        "mode": mode,
        "w0": w0,
        "U": U,
        "Z": Z,
        "k": k,
        "z": z,
        "q": q,
        "C": code,
        "maxima": maxima,
        "energies": energies,
    }
    fixture["templates"] = check_templates(fixture)
    return fixture


def check_projection_negative_controls(fixture):
    code = fixture["C"]
    q = fixture["q"]
    k = fixture["k"]
    z = fixture["z"]
    Z = fixture["Z"]
    zero = (0, 0, 0, 0)
    odd_flips = (1, 1, 1, -1)

    reject(
        "wrong_projection_factor_4",
        "projection.factor_8",
        lambda: need(
            code[0] == [4 * x for x in walsh(q[0])],
            "projection.factor_8",
        ),
    )
    reject(
        "wrong_inverse_factor_16",
        "inverse.z_factor_32",
        lambda: need(
            walsh(z[0]) == [16 * x for x in Z[0]],
            "inverse.z_factor_32",
        ),
    )
    reject(
        "wrong_cross_factor_minus256",
        "cross.factor_minus512",
        lambda: need(
            convolution(code[0], code[1])
            == [-256 * x for x in convolution(SIGMA, k[0])],
            "cross.factor_minus512",
        ),
    )
    reject(
        "wrong_self_factor_512",
        "self.factor_1024",
        lambda: need(
            convolution(code[0], code[0])
            == [512 * x for x in convolution(SIGMA, SIGMA)],
            "self.factor_1024",
        ),
    )
    reject(
        "wrong_norm_32768",
        "code.norm_65536",
        lambda: need(
            sum(x * x for x in code[0]) == 32768,
            "code.norm_65536",
        ),
    )

    bad_q = [row[:] for row in q]
    bad_q[3][0] *= -1
    bad_code = [row[:] for row in code]
    bad_code[3] = [8 * x for x in walsh(bad_q[3])]

    need(
        divide_exact(
            walsh(bad_code[3]), 512, "negative.individual_inverse"
        ) == bad_q[3],
        "negative.individual_word_valid",
    )
    need(
        all(abs(bad_q[3][c]) == 1 for c in SUPPORT)
        and all(bad_q[3][c] == 0 for c in range(16, 64)),
        "negative.individual_support_valid",
    )
    need(
        sum(x * x for x in bad_code[3]) == 65536,
        "negative.individual_norm_still_valid",
    )
    need(
        all(x % 16 == 0 for x in bad_code[3]),
        "negative.individual_divisibility_still_valid",
    )
    need(
        convolution(bad_code[3], bad_code[3])
        == convolution(code[3], code[3]),
        "negative.individual_self_still_valid",
    )
    reject(
        "independently_changed_projected_fibre",
        "common.theta",
        lambda: recover_common_phase(bad_code, fixture["w0"]),
    )
    reject(
        "changed_fibre_breaks_cross_coupling",
        "cross.fibre_coupling",
        lambda: need(
            convolution(bad_code[0], bad_code[3])
            == [-512 * x for x in convolution(SIGMA, k[2])],
            "cross.fibre_coupling",
        ),
    )

    validate_linked_template(zero, odd_flips)
    changed_lhs = sum(odd_flips[s] * bad_code[s][0] for s in range(4))
    need(changed_lhs == 272, "negative.changed_fibre_value_272")
    reject(
        "changed_fibre_breaks_linked_bound",
        "linked.bound_256",
        lambda: need(abs(changed_lhs) <= 256, "linked.bound_256"),
    )

    even_flips = (1, 1, 1, 1)
    reject(
        "linked_template_wrong_flip_parity",
        "linked.epsilon_product",
        lambda: validate_linked_template(zero, even_flips),
    )
    invalid_lhs = sum(code[s][0] for s in range(4))
    need(invalid_lhs == 512, "negative.wrong_parity_value_512")
    reject(
        "wrong_parity_numeric_counterexample",
        "linked.bound_256",
        lambda: need(abs(invalid_lhs) <= 256, "linked.bound_256"),
    )
    reject(
        "wrong_parity_local_sum",
        "linked.local_sum",
        lambda: need(
            sum(q[s][0] for s in range(4)) in (-2, 2),
            "linked.local_sum",
        ),
    )
    reject(
        "linked_template_wrong_translation_xor",
        "linked.shift_xor",
        lambda: validate_linked_template((0, 0, 0, 1), odd_flips),
    )
    need(
        abs(sum(odd_flips[s] * code[s][0] for s in range(4))) == 256,
        "linked.sharp_positive_control",
    )


def require_energy_quantum(energy):
    need(energy % 4 == 0, "energy.multiple_of_four")


def demand_energy196_residue(local_sign):
    need(local_sign in (-1, 1), "energy196.local_sign")
    need((32 * local_sign) % 7 == 0, "energy196.mod7_equation")


def demand_energy192_residue(local_sign, correction4, correction2):
    need(
        all(x in (-1, 1) for x in (local_sign, correction4, correction2)),
        "energy192.input_signs",
    )
    need(
        (32 * local_sign) % 7
        == (-4 * correction4 - 2 * correction2) % 7,
        "energy192.mod7_equation",
    )


def check_hypothetical_energy_logic():
    # This function does NOT consume fixture energies or fixture spectra.
    # Hypotheses:
    # 64 capped odd coefficients, integral Z, 16 local unit squares,
    # even Z off the support, and sum(E_s)=560 for weighted claims.
    magnitude_set = (1, 3, 5, 7)
    for d in magnitude_set:
        need(d * d <= 8 * d - 7, "weighted.allowed_magnitude_chord")

    rows_by_energy = {}
    for energy in (196, 192):
        guard()
        require_energy_quantum(energy)
        deficit = (64 * 49 - 16 * energy) // 8
        rows = []
        for n1 in range(deficit // 6 + 1):
            for n3 in range(deficit // 5 + 1):
                for n5 in range(deficit // 3 + 1):
                    guard()
                    n7 = 64 - n1 - n3 - n5
                    if n7 < 0:
                        continue
                    if 6 * n1 + 5 * n3 + 3 * n5 == deficit:
                        need(
                            n1 + 9 * n3 + 25 * n5 + 49 * n7
                            == 16 * energy,
                            "energy.deficit_matches_squares",
                        )
                        rows.append((n1, n3, n5, n7))
        rows_by_energy[energy] = rows
    need(rows_by_energy[196] == [(0, 0, 0, 64)], "energy196.unique_counts")
    need(rows_by_energy[192] == [(0, 1, 1, 62)], "energy192.unique_counts")

    left_residues = {(32 * sign) % 7 for sign in (-1, 1)}
    right_residues = {
        (-4 * sign4 - 2 * sign2) % 7
        for sign4, sign2 in product((-1, 1), repeat=2)
    }
    need(left_residues == {3, 4}, "energy.local_mod7_residues")
    need(right_residues == {1, 2, 5, 6}, "energy192.correction_residues")
    need(left_residues.isdisjoint({0}), "energy196.mod7_obstruction")
    need(
        left_residues.isdisjoint(right_residues),
        "energy192.mod7_obstruction",
    )

    reject(
        "invalid_energy_residue_190",
        "energy.multiple_of_four",
        lambda: require_energy_quantum(190),
    )
    for sign in (-1, 1):
        reject(
            "energy196_impossible_local_sign_" + str(sign),
            "energy196.mod7_equation",
            lambda sign=sign: demand_energy196_residue(sign),
        )
    for sign, sign4, sign2 in product((-1, 1), repeat=3):
        reject(
            "energy192_impossible_residue_"
            + str((sign, sign4, sign2)),
            "energy192.mod7_equation",
            lambda sign=sign, sign4=sign4, sign2=sign2:
                demand_energy192_residue(sign, sign4, sign2),
        )

    # Exhaustive formal energy ledgers, not realized Fourier objects.
    values = tuple(range(16, 189, 4))
    selections = {
        m: tuple(combinations(range(4), m)) for m in (2, 3, 4)
    }
    minima = {2: 10 ** 9, 3: 10 ** 9, 4: 10 ** 9}
    ledger_count = 0
    for e0 in values:
        for e1 in values:
            for e2 in values:
                guard()
                e3 = 560 - e0 - e1 - e2
                if e3 < 16 or e3 > 188 or e3 % 4:
                    continue
                ledger = (e0, e1, e2, e3)
                ledger_count += 1
                for m in (2, 3, 4):
                    for selected in selections[m]:
                        selected_sum = sum(ledger[s] for s in selected)
                        minima[m] = min(minima[m], selected_sum)
    need(ledger_count == 20685, "weighted.formal_ledger_count")
    need(
        minima == {2: 184, 3: 372, 4: 560},
        "weighted.selected_energy_minima",
    )

    disagreement_bounds = {}
    for m, expected in ((2, 16), (3, 38), (4, 60)):
        numerator = minima[m] - 36 * m
        ceiling = ceil_div(numerator, 7)
        by_integer_enumeration = next(
            h for h in range(64 * m + 1) if 7 * h >= numerator
        )
        need(
            ceiling == by_integer_enumeration == expected,
            "weighted.count_ceiling_" + str(m),
        )
        need(
            7 * (expected - 1) < numerator <= 7 * expected,
            "weighted.exact_integer_threshold_" + str(m),
        )
        disagreement_bounds[m] = ceiling

    a_floor = 2 * 560 + 4 * 56
    need(a_floor == 1344, "weighted.linked_absolute_sum_floor")
    need((a_floor - 256) % 2 == 0, "weighted.linked_deficit_integral")
    d_floor = (a_floor - 256) // 2
    need(d_floor == 544, "weighted.linked_weight_floor")
    linked_bound = ceil_div(d_floor, 7)
    linked_by_enumeration = next(h for h in range(257) if 7 * h >= d_floor)
    need(
        linked_bound == linked_by_enumeration == 78,
        "weighted.linked_count_78",
    )
    need(7 * 77 < d_floor <= 7 * 78, "weighted.linked_exact_threshold")
    need(ceil_div(140 - 36, 7) == 15, "weighted.high_energy_single_fibre")

    return (
        "formal_energy_counts=" + str(rows_by_energy),
        "formal_energy_ledgers=" + str(ledger_count),
        "formal_selected_energy_minima=" + str(minima),
        "conditional_disagreement_bounds=" + str(disagreement_bounds),
        "conditional_linked_disagreement_bound=" + str(linked_bound),
    )


def run():
    need(sys.version_info >= (3, 10), "runtime.python_3_10_or_newer")
    need(walsh(SIGMA) == [16 * x for x in A], "plateaued.sigma_to_a")
    need(walsh(A) == [4 * x for x in SIGMA], "plateaued.a_to_sigma")
    need(
        walsh(walsh(SIGMA)) == [64 * x for x in SIGMA],
        "walsh.involution_factor_64",
    )
    need(
        tuple(c for c in range(64) if A[c] != 0) == SUPPORT,
        "plateaued.exact_support",
    )

    indexed = build_and_check_fixture("indexed")
    calibration = build_and_check_fixture("calibration")
    need(
        all(
            indexed["C"][s]
            == [32 * SIGMA[t ^ (s ^ 1)] for t in range(64)]
            for s in range(4)
        ),
        "fixture.indexed_closed_form",
    )
    need(
        all(
            calibration["C"][s]
            == [128 if (t & 15) == 0 else 0 for t in range(64)]
            for s in range(4)
        ),
        "fixture.calibration_closed_form",
    )
    check_projection_negative_controls(calibration)
    energy_report = check_hypothetical_energy_logic()

    report = [
        "scope=finite identities plus separate conditional integer arithmetic",
        "original_caller=NOT_CERTIFIED",
    ]
    for fixture in (indexed, calibration):
        report.append(
            "fixture=" + fixture["mode"]
            + " support_u=48 support_v=208"
            + " energies=" + str(fixture["energies"])
            + " total_energy=832"
            + " max_abs_z=" + str(fixture["maxima"])
            + " original_cap=FAIL"
            + " balance=FAIL"
            + " sampled_template_count_and_h_range="
            + str(fixture["templates"])
        )
    report.extend(energy_report)
    report.append("checked_equalities_and_conditions=" + str(CHECK_COUNT))
    report.append("intended_negative_controls=" + str(len(NEGATIVE_RESULTS)))
    for name, identity in NEGATIVE_RESULTS:
        report.append("intended_rejection=" + name + " identity=" + identity)
    return report


def main():
    try:
        report = run()
        guard()
        for line in report:
            print(line)
        guard()
        print(
            "RESULT: PASS_FINITE; "
            "original_UV_existence=NOT_CERTIFIED; "
            "uniform_or_whole_target_acceptance=NOT_CERTIFIED"
        )
        print("elapsed_seconds=" + format(monotonic() - START, ".6f"))
        return 0
    except BudgetExpired as error:
        print("RESULT: INCOMPLETE; " + str(error))
        return 2
    except IdentityError as error:
        print("RESULT: FAIL; " + str(error))
        return 1
    except BaseException as error:
        print(
            "RESULT: INCOMPLETE; unexpected "
            + type(error).__name__ + ": " + str(error)
        )
        return 2


if __name__ == "__main__":
    sys.exit(main())

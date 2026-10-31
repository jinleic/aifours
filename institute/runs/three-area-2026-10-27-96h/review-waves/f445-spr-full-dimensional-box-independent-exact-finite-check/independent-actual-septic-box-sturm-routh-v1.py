from fractions import Fraction as Q
from itertools import product
from time import monotonic
import sys

START = monotonic()
DEADLINE = START + 55.0
AUDIT = []
CONTROL_LOG = []


class Incomplete(Exception):
    pass


class Failure(Exception):
    def __init__(self, code, detail=""):
        self.code = code
        super().__init__(code + (": " + detail if detail else ""))


def guard():
    if monotonic() >= DEADLINE:
        raise Incomplete("COOPERATIVE_DEADLINE_55_SECONDS")


def need(condition, code, detail=""):
    guard()
    if not condition:
        raise Failure(code, detail)


def trim(values):
    guard()
    p = [Q(c) for c in values]
    if not p:
        p = [Q(0)]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)


ZERO = (Q(0),)
ONE = (Q(1),)
T = (Q(0), Q(1))
ONE_PLUS_T = (Q(1), Q(1))


def add(p, r):
    return trim(
        (p[k] if k < len(p) else 0)
        + (r[k] if k < len(r) else 0)
        for k in range(max(len(p), len(r)))
    )


def scale(p, c):
    return trim(Q(c) * x for x in p)


def sub(p, r):
    return add(p, scale(r, -1))


def mul(p, r):
    out = [Q(0)] * (len(p) + len(r) - 1)
    for i, x in enumerate(p):
        guard()
        for j, y in enumerate(r):
            out[i + j] += x * y
    return trim(out)


def times_t(p):
    return trim((Q(0),) + tuple(p))


def power(p, n):
    need(isinstance(n, int) and n >= 0, "POLYNOMIAL_POWER_DOMAIN")
    out = ONE
    for _ in range(n):
        out = mul(out, p)
    return out


def value(p, x):
    out = Q(0)
    for c in reversed(p):
        guard()
        out = out * x + c
    return out


def derivative(p):
    return trim(k * p[k] for k in range(1, len(p)))


def remainder(p, divisor):
    need(divisor != ZERO, "POLYNOMIAL_DIVISION_BY_ZERO")
    r = list(p)
    while len(r) >= len(divisor) and tuple(r) != ZERO:
        guard()
        offset = len(r) - len(divisor)
        factor = r[-1] / divisor[-1]
        for j, c in enumerate(divisor):
            r[offset + j] -= factor * c
        r = list(trim(r))
    return trim(r)


def positive_normalize(p):
    need(p != ZERO, "NORMALIZE_ZERO_POLYNOMIAL")
    return scale(p, Q(1) / abs(p[-1]))


def sturm_chain(p):
    need(p != ZERO, "STURM_ZERO_POLYNOMIAL")
    first = positive_normalize(p)
    second = derivative(first)
    chain = [first]
    if second == ZERO:
        return tuple(chain)
    chain.append(positive_normalize(second))
    while True:
        guard()
        nxt = scale(remainder(chain[-2], chain[-1]), -1)
        if nxt == ZERO:
            return tuple(chain)
        chain.append(positive_normalize(nxt))


def sign(x):
    return (x > 0) - (x < 0)


def variations(signs):
    nonzero = [s for s in signs if s != 0]
    return sum(a != b for a, b in zip(nonzero, nonzero[1:]))


def variation_at(chain, x):
    if x is None:
        return variations(sign(p[-1]) for p in chain)
    return variations(sign(value(p, x)) for p in chain)


def certify_positive(p, left=Q(0), right=None, tag=""):
    p = trim(p)
    need(p != ZERO, "SPECTRAL_ZERO_POLYNOMIAL", tag)
    need(value(p, left) > 0, "LEFT_ENDPOINT_NOT_POSITIVE", tag)
    if right is None:
        need(p[-1] > 0, "INFINITE_LEADING_NOT_POSITIVE", tag)
    else:
        need(right >= left, "INTERVAL_ORDER", tag)
        need(value(p, right) > 0, "RIGHT_ENDPOINT_NOT_POSITIVE", tag)
    chain = sturm_chain(p)
    roots = variation_at(chain, left) - variation_at(chain, right)
    reason = (
        "STURM_POSITIVE_AXIS_ZERO"
        if left == 0 and right is None
        else "STURM_INTERVAL_ZERO"
    )
    need(roots == 0, reason, tag + "; distinct_roots=" + str(roots))
    AUDIT.append((tag, len(p) - 1, left, right, roots))


def factored_minus_t(markers):
    p = ONE
    for root in markers:
        p = mul(p, (Q(root), Q(-1)))
    return p


F = factored_minus_t((Q(1, 2), Q(2), Q(4)))
G = factored_minus_t((Q(1), Q(3), Q(5)))
QREF = tuple(Q(x) for x in (4, 15, 11, 23, Q(13, 2), 9, 1, 1))
M = Q(65, 4096)
GAMMA = M / (7 ** 6)
EPS = GAMMA / 38

CORE = (
    (Q(3), Q(5)),
    (Q(1197, 80), Q(15)),
    (Q(11), Q(11)),
    (Q(23), Q(467, 20)),
    (Q(13, 2), Q(13, 2)),
    (Q(179, 20), Q(9)),
    (Q(1), Q(1)),
)
EXPANDED = tuple((lo - EPS, hi + EPS) for lo, hi in CORE)


def require_monic_septic(a):
    need(len(a) == 8, "SEPTIC_DEGREE")
    need(a[7] == 1, "MONIC_LEADING")


def physical_parity(a):
    require_monic_septic(a)
    even = tuple(((-1) ** k) * a[2 * k] for k in range(4))
    odd = tuple(((-1) ** k) * a[2 * k + 1] for k in range(4))
    return trim(even), trim(odd)


def compose_s(even, odd):
    out = [Q(0)] * 8
    need(len(even) <= 4 and len(odd) <= 4, "PARITY_DEGREE")
    for k, c in enumerate(even):
        out[2 * k] = ((-1) ** k) * c
    for k, c in enumerate(odd):
        out[2 * k + 1] = ((-1) ** k) * c
    return trim(out)


def require_numerator(a):
    require_monic_septic(a)
    need(a == QREF, "NUMERATOR_FACTOR_COEFFICIENT")
    need(a == compose_s(F, G), "NUMERATOR_FACTORIZATION")


def direct_real_product(q, a, conjugated=True):
    out = [Q(0)] * 8
    for i, qi in enumerate(q):
        guard()
        for j, aj in enumerate(a):
            if (i + j) % 2:
                continue
            k = (i + j) // 2
            exponent = k + (j if conjugated else 0)
            out[k] += ((-1) ** exponent) * qi * aj
    return trim(out)


def physical_pair(a, even=None, odd=None, pairing=None):
    actual_even, actual_odd = physical_parity(a)
    even = actual_even if even is None else trim(even)
    odd = actual_odd if odd is None else trim(odd)
    need(
        compose_s(even, odd) == a,
        "PHYSICAL_PARITY_RECONSTRUCTION",
    )
    if pairing is None:
        pairing = add(mul(F, even), times_t(mul(G, odd)))
    pairing = trim(pairing)
    need(pairing[0] == QREF[0] * a[0], "DC_NORMALIZATION")
    need(
        pairing == direct_real_product(QREF, a, True),
        "REAL_CONJUGATE_PRODUCT",
    )
    need(
        len(pairing) == 8 and pairing[-1] == 1,
        "MONIC_SPECTRAL_LEADING",
    )
    return pairing


def require_member(a, bounds):
    require_monic_septic(a)
    for j, (lo, hi) in enumerate(bounds):
        need(lo <= a[j] <= hi, "BOX_MEMBERSHIP", "coefficient=" + str(j))


def routh_first_column(a):
    require_monic_septic(a)
    upper = [a[7], a[5], a[3], a[1]]
    lower = [a[6], a[4], a[2], a[0]]
    first_column = [upper[0], lower[0]]
    need(
        all(x > 0 for x in first_column),
        "ROUTH_NONPOSITIVE_FIRST_COLUMN",
        "initial_rows",
    )
    for level in range(2, 8):
        guard()
        pivot = lower[0]
        row = [
            (pivot * upper[j + 1] - upper[0] * lower[j + 1]) / pivot
            for j in range(3)
        ] + [Q(0)]
        need(
            row[0] > 0,
            "ROUTH_NONPOSITIVE_FIRST_COLUMN",
            "row=" + str(level),
        )
        first_column.append(row[0])
        upper, lower = lower, row
    return tuple(first_column)


def endpoint_member(bounds, even_low, odd_low):
    out = []
    for j, (lo, hi) in enumerate(bounds):
        want_low = even_low if j % 2 == 0 else odd_low
        physical_sign = 1 if (j // 2) % 2 == 0 else -1
        take_lower_coefficient = (
            physical_sign > 0 if want_low else physical_sign < 0
        )
        out.append(lo if take_lower_coefficient else hi)
    return tuple(out) + (Q(1),)


def four_endpoints(bounds):
    return {
        (sf, sg): endpoint_member(bounds, sf > 0, sg > 0)
        for sf, sg in product((-1, 1), repeat=2)
    }


def mutated(a, index, new_value):
    out = list(a)
    out[index] = Q(new_value)
    return tuple(out)


def expect_rejection(name, expected_reason, operation):
    guard()
    try:
        operation()
    except Failure as exc:
        need(
            exc.code == expected_reason,
            "CONTROL_WRONG_REASON",
            name + "; expected=" + expected_reason + "; got=" + exc.code,
        )
        CONTROL_LOG.append((name, exc.code))
        return
    raise Failure("CONTROL_NOT_REJECTED", name)


def run_controls():
    require_numerator(QREF)
    require_member(QREF, CORE)
    expected_column = (
        Q(1), Q(1), Q(5, 2), Q(17, 10),
        Q(39, 17), Q(73, 26), Q(135, 73), Q(4),
    )
    need(
        routh_first_column(QREF) == expected_column,
        "Q_ROUTH_EXACT_COLUMN",
    )
    binomial_septic = tuple(Q(x) for x in (1, 7, 21, 35, 35, 21, 7, 1))
    routh_first_column(binomial_septic)
    certify_positive((Q(5),), tag="positive_constant")
    certify_positive((Q(1), Q(1)), tag="positive_linear")
    certify_positive((Q(2), Q(-2), Q(1)), tag="positive_nontrivial_quadratic")
    certify_positive(physical_pair(QREF), tag="q_physical_spectral_positive")

    expect_rejection(
        "wrong_numerator_coefficient",
        "NUMERATOR_FACTOR_COEFFICIENT",
        lambda: require_numerator(mutated(QREF, 3, Q(24))),
    )
    expect_rejection(
        "nonmonic_leading",
        "MONIC_LEADING",
        lambda: require_numerator(mutated(QREF, 7, Q(2))),
    )
    even, odd = physical_parity(QREF)
    wrong_even = list(even)
    wrong_even[1] = -wrong_even[1]
    expect_rejection(
        "wrong_physical_parity",
        "PHYSICAL_PARITY_RECONSTRUCTION",
        lambda: physical_pair(QREF, tuple(wrong_even), odd),
    )
    unconjugated = direct_real_product(QREF, QREF, False)
    expect_rejection(
        "missing_conjugation",
        "REAL_CONJUGATE_PRODUCT",
        lambda: physical_pair(QREF, pairing=unconjugated),
    )
    missing_t = add(mul(F, even), mul(G, odd))
    expect_rejection(
        "missing_spectral_t_weight",
        "DC_NORMALIZATION",
        lambda: physical_pair(QREF, pairing=missing_t),
    )
    false_denominator = mutated(QREF, 1, Q(-15))
    false_spectral = physical_pair(false_denominator)
    need(
        value(false_spectral, Q(1, 2)) == Q(-8775, 128),
        "FALSE_SPECTRAL_CONTROL_WITNESS",
    )
    need(
        false_spectral[0] > 0 and false_spectral[-1] > 0,
        "FALSE_SPECTRAL_CONTROL_ENDPOINTS",
    )
    expect_rejection(
        "false_physical_spectral_positivity",
        "STURM_POSITIVE_AXIS_ZERO",
        lambda: certify_positive(false_spectral, tag="false_physical_spectrum"),
    )
    outside = mutated(QREF, 0, EXPANDED[0][1] + 1)
    expect_rejection(
        "false_actual_box_membership",
        "BOX_MEMBERSHIP",
        lambda: require_member(outside, EXPANDED),
    )
    wrong_orientation = tuple(
        -c if j % 2 == 0 else c for j, c in enumerate(QREF)
    )
    expect_rejection(
        "wrong_hurwitz_orientation",
        "ROUTH_NONPOSITIVE_FIRST_COLUMN",
        lambda: routh_first_column(wrong_orientation),
    )
    expect_rejection(
        "tangential_positive_axis_zero",
        "STURM_POSITIVE_AXIS_ZERO",
        lambda: certify_positive((Q(1), Q(-2), Q(1)), tag="touching_zero"),
    )


def check_constants():
    need(F == (Q(4), Q(-11), Q(13, 2), Q(-1)), "F_EXPANSION")
    need(G == (Q(15), Q(-23), Q(9), Q(-1)), "G_EXPANSION")
    need(compose_s(F, G) == QREF, "Q_FROM_FACTORS")
    need(GAMMA == Q(65, 481890304), "GAMMA_EXACT")
    need(EPS == Q(65, 18311831552), "EPSILON_EXACT")
    need(
        EPS > 0 and EPS < 1 and GAMMA - 19 * EPS == GAMMA / 2,
        "EPSILON_POSITIVE_MARGIN",
    )
    cubic_binomial = power(ONE_PLUS_T, 3)
    quadratic_binomial = power(ONE_PLUS_T, 2)
    need(
        all(abs(c) <= 4 * cubic_binomial[k] for k, c in enumerate(F)),
        "F_ABSOLUTE_COEFFICIENT_BOUND",
    )
    need(
        all(abs(c) <= 15 * cubic_binomial[k] for k, c in enumerate(G)),
        "G_ABSOLUTE_COEFFICIENT_BOUND",
    )
    need(all(c >= 1 for c in cubic_binomial), "DELTA_E_COEFFICIENT_BOUND")
    need(all(c >= 1 for c in quadratic_binomial), "DELTA_O_COEFFICIENT_BOUND")
    difference = sub(
        power(ONE_PLUS_T, 6),
        times_t(power(ONE_PLUS_T, 5)),
    )
    need(all(c >= 0 for c in difference), "SPECTRAL_WEIGHT_NORM_BOUND")
    need(Q(7, 6) ** 6 < 3, "TAIL_BINOMIAL_CONSTANT")
    need(Q(25, 2592) > GAMMA, "TAIL_NORMALIZED_CONSTANT")


def check_all_actual_corners(envelopes):
    corners = [
        tuple(EXPANDED[j][bit] for j, bit in enumerate(bits)) + (Q(1),)
        for bits in product((0, 1), repeat=7)
    ]
    need(len(corners) == 128 and len(set(corners)) == 128, "ACTUAL_CORNER_COUNT")
    need(len(set(envelopes.values())) == 4, "ACTUAL_ENVELOPE_COUNT")
    need(
        all(a in corners for a in envelopes.values()),
        "ENVELOPES_ARE_ACTUAL_CORNERS",
    )
    envelope_data = {}
    for key, a in envelopes.items():
        require_member(a, EXPANDED)
        e, o = physical_parity(a)
        envelope_data[key] = (e, o, physical_pair(a))
    for number, a in enumerate(corners):
        guard()
        require_member(a, EXPANDED)
        e, o = physical_parity(a)
        p = physical_pair(a)
        need(p[0] >= 4 * (3 - EPS), "ACTUAL_CORNER_DC_BOUND", str(number))
        routh_first_column(a)
        for (sf, sg), (ee, oo, pp) in envelope_data.items():
            need(
                all(sf * (x - y) >= 0 for x, y in zip(e, ee)),
                "EVEN_ENDPOINT_DOMINATION",
                str(number),
            )
            need(
                all(sg * (x - y) >= 0 for x, y in zip(o, oo)),
                "ODD_ENDPOINT_DOMINATION",
                str(number),
            )
            need(
                sub(p, pp)
                == add(mul(F, sub(e, ee)), times_t(mul(G, sub(o, oo)))),
                "ENVELOPE_PAIRING_DIFFERENCE_IDENTITY",
                str(number),
            )
    return len(corners)


def regional_specs():
    residual = (
        (Q(0), Q(1, 4)),
        (Q(3, 4), Q(19, 20)),
        (Q(1), Q(3, 2)),
        (Q(5, 2), Q(3)),
        (Q(7, 2), Q(15, 4)),
        (Q(17, 4), Q(9, 2)),
        (Q(5), None),
    )
    return (
        ("I1", ((Q(1, 4), Q(3, 4)),), Q(3, 4)),
        ("I2", ((Q(3, 2), Q(5, 2)),), Q(43, 128)),
        ("I3", ((Q(15, 4), Q(17, 4)),), Q(7, 32)),
        ("J1", ((Q(19, 20), Q(1)),), Q(89, 400)),
        ("J2", ((Q(3), Q(7, 2)),), Q(39, 320)),
        ("J3", ((Q(9, 2), Q(5)),), Q(77, 16)),
        ("residual", residual, M),
    )


def check_core_certificates():
    specs = regional_specs()
    need(min(bound for _, _, bound in specs) == M, "SEVEN_REGION_MINIMUM")
    cover = sorted(
        [interval for _, intervals, _ in specs for interval in intervals],
        key=lambda interval: interval[0],
    )
    need(cover[0][0] == 0 and cover[-1][1] is None, "REGION_COVER_ENDPOINTS")
    for previous, following in zip(cover, cover[1:]):
        need(previous[1] == following[0], "REGION_COVER_GAP_OR_OVERLAP")
    weight = power(ONE_PLUS_T, 6)
    tail = scale(power(T, 7), Q(25, 5184))
    core_endpoints = four_endpoints(CORE)
    for key, a in core_endpoints.items():
        require_member(a, CORE)
        p = physical_pair(a)
        for name, intervals, bound in specs:
            shifted = sub(p, (bound,))
            for index, (left, right) in enumerate(intervals):
                certify_positive(
                    shifted, left, right,
                    "core_" + str(key) + "_" + name + "_" + str(index),
                )
        certify_positive(
            sub(p, tail), Q(6), None,
            "core_tail_" + str(key),
        )
        certify_positive(
            sub(p, scale(weight, GAMMA)),
            tag="core_uniform_weighted_" + str(key),
        )


def check_maximum_box_certificates(envelopes):
    weight = power(ONE_PLUS_T, 6)
    for key, a in envelopes.items():
        p = physical_pair(a)
        certify_positive(
            sub(p, scale(weight, GAMMA / 2)),
            tag="maximum_box_uniform_weighted_" + str(key),
        )


def main():
    check_constants()
    run_controls()
    require_member(QREF, EXPANDED)
    envelopes = four_endpoints(EXPANDED)
    corner_count = check_all_actual_corners(envelopes)
    check_core_certificates()
    check_maximum_box_certificates(envelopes)
    guard()
    print("RESULT: VALID_FINITE_CERTIFICATES")
    print("actual_corners=" + str(corner_count))
    print("actual_endpoint_envelopes=" + str(len(envelopes)))
    print("corner_routh_checks=" + str(corner_count))
    print("sturm_certificates=" + str(len(AUDIT)))
    print("maximum_epsilon=" + str(EPS))
    print("certified_weighted_margin=" + str(GAMMA / 2))
    print("q_routh_first_column=" + ",".join(map(str, routh_first_column(QREF))))
    for name, reason in CONTROL_LOG:
        print("control_" + name + "=REJECTED:" + reason)
    print("elapsed_seconds=%.6f" % (monotonic() - START))
    print(
        "NOT_ESTABLISHED: parent_adoption; standalone_all_box_theorem; "
        "original_universal_synthesis; novelty; human_kernel_or_cross_family_review"
    )
    return 0


if __name__ == "__main__":
    try:
        status = main()
    except Incomplete as exc:
        print("RESULT: INCOMPLETE")
        print(str(exc))
        status = 2
    except Failure as exc:
        print("RESULT: REJECTED")
        print(str(exc))
        status = 1
    except Exception as exc:
        print("RESULT: INCOMPLETE")
        print("UNEXPECTED_EXCEPTION:" + type(exc).__name__ + ":" + str(exc))
        status = 2
    sys.exit(status)

from collections import Counter
from itertools import product
from time import monotonic
import sys


class CheckFailure(RuntimeError):
    def __init__(self, code, detail=""):
        self.code = code
        super().__init__(code + (": " + detail if detail else ""))


def need(condition, code, detail=""):
    if not condition:
        raise CheckFailure(code, detail)


def deadline(start):
    need(monotonic() - start < 50.0, "DEADLINE",
         "Cooperative limit reached; no completed finite certificate.")


def sign_product(values):
    result = 1
    for value in values:
        result *= value
    return result


def character_table(n):
    return tuple(
        tuple(1 - 2 * ((a & b).bit_count() & 1) for b in range(n))
        for a in range(n)
    )


W4 = character_table(4)
W16 = character_table(16)
T0 = (0, 1, 2, 3)
BETAS = tuple(
    beta for beta in product((-1, 1), repeat=4)
    if sign_product(beta) == -1
)


def direct(values, table):
    return tuple(sum(a * b for a, b in zip(values, row))
                 for row in table)


def fwht(values):
    out = list(values)
    n = len(out)
    need(n > 0 and (n & (n - 1)) == 0, "POWER_OF_TWO")
    width = 1
    while width < n:
        for base in range(0, n, 2 * width):
            for offset in range(width):
                i = base + offset
                a, b = out[i], out[i + width]
                out[i], out[i + width] = a + b, a - b
        width *= 2
    return tuple(out)


def mask_of(values):
    need(len(values) == 16 and all(v in (-1, 1) for v in values),
         "NOT_SIGN_FUNCTION")
    return sum((v == -1) << i for i, v in enumerate(values))


def affine_two(points):
    if len(points) != 4:
        return False
    translated = {p ^ points[0] for p in points}
    return len(translated) == 4 and all(
        (a ^ b) in translated for a in translated for b in translated
    )


def flat_values(points, beta):
    phase = tuple(
        sum(beta[i] * W16[points[i]][h] for i in range(4))
        for h in range(16)
    )
    need(all(abs(v) == 2 for v in phase), "FOUR_SIGN_PRODUCT")
    return tuple(v // 2 for v in phase)


def make_catalog(start):
    directions = {
        tuple(sorted((0, a, b, a ^ b)))
        for a in range(1, 16) for b in range(a + 1, 16)
    }
    need(len(directions) == 35, "DIRECTION_COUNT")
    flats = {
        tuple(sorted(t ^ v for v in direction))
        for direction in directions for t in range(16)
    }
    need(len(flats) == 140 and all(affine_two(t) for t in flats),
         "AFFINE_FLAT_CATALOG")
    catalog = {}
    for y in range(16):
        for sign in (-1, 1):
            values = tuple(sign * c for c in W16[y])
            mask = mask_of(values)
            need(mask not in catalog, "CATALOG_DUPLICATE")
            catalog[mask] = "character"
    for points in sorted(flats):
        for beta in BETAS:
            values = flat_values(points, beta)
            coefficients = dict(zip(points, beta))
            expected = tuple(8 * coefficients.get(y, 0)
                             for y in range(16))
            need(direct(values, W16) == expected,
                 "CATALOG_INVERSE_SPECTRUM")
            mask = mask_of(values)
            need(mask not in catalog, "CATALOG_DUPLICATE")
            catalog[mask] = "four-flat-spectrum"
        deadline(start)
    need(Counter(catalog.values()) == Counter({
        "character": 32, "four-flat-spectrum": 1120
    }), "CATALOG_CLASS_COUNTS")
    return catalog


def classify(spectrum):
    support = tuple(i for i, value in enumerate(spectrum) if value)
    if len(support) == 1 and abs(spectrum[support[0]]) == 16:
        return "character"
    if (len(support) == 4
            and all(abs(spectrum[i]) == 8 for i in support)
            and affine_two(support)
            and sign_product(
                1 if spectrum[i] > 0 else -1 for i in support
            ) == -1):
        return "four-flat-spectrum"
    return None


def exhaust_signs(catalog, start):
    histogram = Counter()
    eligible = {}
    for mask in range(1 << 16):
        values = tuple(1 - 2 * ((mask >> i) & 1) for i in range(16))
        spectrum = fwht(values)
        need(spectrum == direct(values, W16), "FWHT_DIRECT_DISAGREE",
             "mask=" + str(mask))
        residue_support = sum(value % 3 != 0 for value in spectrum)
        histogram[residue_support] += 1
        if residue_support <= 4:
            label = classify(spectrum)
            need(label is not None, "UNCLASSIFIED_ELIGIBLE",
                 "mask=" + str(mask))
            eligible[mask] = label
        if (mask & 127) == 0:
            deadline(start)
    need(sum(histogram.values()) == 65536, "EXHAUSTION_COUNT")
    need(eligible == catalog, "CLASSIFICATION_SET_COMPLETENESS")
    need(histogram[1] == 32 and histogram[4] == 1120
         and all(histogram[k] == 0 for k in (0, 2, 3)),
         "SMALL_RESIDUE_SUPPORT_COUNTS")
    return histogram, Counter(eligible.values())


def balanced_route(values):
    need(len(values) == 4 and all(v in (-1, 1) for v in values),
         "FOUR_POINT_DOMAIN")
    spectrum = direct(values, W4)
    need(spectrum[0] == 0, "FOUR_POINT_UNBALANCED")
    support = tuple(i for i, v in enumerate(spectrum) if v)
    need(len(support) == 1 and support[0] != 0
         and abs(spectrum[support[0]]) == 4, "FOUR_POINT_ROUTE")
    d = support[0]
    eta = spectrum[d] // 4
    need(tuple(values) == tuple(eta * c for c in W4[d]),
         "FOUR_POINT_CHARACTER")
    return d, eta


def check_partial(kappa, expected, denominator=4):
    full = direct(tuple(4 * v for v in kappa), W4)
    need(denominator > 0
         and all(v % denominator == 0 for v in full),
         "PARTIAL_SCALING")
    received = tuple(v // denominator for v in full)
    need(received == tuple(expected), "PARTIAL_SCALING")
    return received


def check_four_points():
    dc_counts, routes = Counter(), Counter()
    for mask in range(16):
        values = tuple(1 - 2 * ((mask >> i) & 1) for i in range(4))
        spectrum = direct(values, W4)
        need(fwht(values) == spectrum, "FOUR_POINT_FWHT")
        dc_counts[spectrum[0]] += 1
        if spectrum[0] == 0:
            d, eta = balanced_route(values)
            routes[d] += 1
            expected = tuple(12 * eta if j == d else 0
                             for j in range(4))
            check_partial(tuple(3 * v for v in values), expected)
    need(dc_counts == Counter({-4: 1, -2: 4, 0: 6, 2: 4, 4: 1}),
         "FOUR_POINT_DC_COUNTS")
    need(routes == Counter({1: 2, 2: 2, 3: 2}),
         "BALANCED_ROUTE_COMPLETENESS")
    for beta in (-1, 1):
        for alpha in range(4):
            kappa = tuple(beta * (3 - 4 * (z == alpha))
                          for z in range(4))
            expected = tuple(
                8 * beta if d == 0 else -4 * beta * W4[d][alpha]
                for d in range(4)
            )
            check_partial(kappa, expected)
    return dc_counts, routes


def check_mod3_inverse(values, spectrum, factor=1):
    received = tuple((factor * v) % 3
                     for v in direct(spectrum, W16))
    need(received == tuple(v % 3 for v in values), "MOD3_INVERSE")


def check_h_inverse(values, spectrum, denominator=16):
    numerator = direct(spectrum, W16)
    need(denominator > 0
         and all(v % denominator == 0 for v in numerator),
         "H_SCALE")
    need(tuple(v // denominator for v in numerator) == tuple(values),
         "H_SCALE")


def coset_summary(beta, labels, prediction_sign=-1):
    need(len(beta) == 4 and all(v in (-1, 1) for v in beta)
         and sign_product(beta) == -1, "BETA_DOMAIN")
    need(len(labels) == 4 and all(a in range(4) for a in labels),
         "LABEL_DOMAIN")
    x = 0
    for label in labels:
        x ^= label
    supports = []
    for d in (1, 2, 3):
        gamma = tuple(-beta[i] * W4[d][labels[i]] for i in range(4))
        actual_product = sign_product(gamma)
        need(actual_product == prediction_sign * W4[d][x],
             "COSET_SIGN_PRODUCT")
        phase = tuple(
            sum(gamma[i] * W16[T0[i]][h] for i in range(4))
            for h in range(16)
        )
        if actual_product == -1:
            need(all(abs(v) == 2 for v in phase), "COSET_PHASE")
        else:
            need(phase.count(0) == 12
                 and all(v in (-4, 0, 4) for v in phase), "COSET_PHASE")
        m = sum(v % 3 != 0 for v in phase)
        need(m == (16 if W4[d][x] == 1 else 4), "COSET_SUPPORT")
        supports.append(m)
    return x, tuple(supports)


def exhaust_cosets(start):
    patterns, xor_counts = Counter(), Counter()
    total = 0
    for beta in BETAS:
        for labels in product(range(4), repeat=4):
            x, supports = coset_summary(beta, labels)
            xor_counts[x] += 1
            patterns[supports] += 1
            total += 1
        deadline(start)
    need(total == 2048, "COSET_CASE_COUNT")
    need(xor_counts == Counter({0: 512, 1: 512, 2: 512, 3: 512}),
         "XOR_LABEL_FREQUENCIES")
    need(patterns == Counter({
        (16, 16, 16): 512,
        (4, 16, 4): 512,
        (16, 4, 4): 512,
        (4, 4, 16): 512,
    }), "COSET_PATTERN_FREQUENCIES")
    return patterns, xor_counts


def check_shadow(ms, ns, mod4=True, total12=True):
    need(len(ms) == len(ns) == 3
         and all(m in (4, 16) for m in ms)
         and all(isinstance(n, int) and 0 <= n <= 12 for n in ns),
         "SHADOW_DOMAIN")
    if total12:
        need(sum(ns) == 12, "TOTAL12")
    if mod4:
        need(all(n % 4 == 0 for n in ns), "NDIV4")
    need(all(4 + 9 * n >= 4 * m for m, n in zip(ms, ns)),
         "ENERGY_LOWER")


def shadow_solutions(ms, mod4=True, total12=True):
    return tuple(
        ns for ns in product(range(13), repeat=3)
        if (not total12 or sum(ns) == 12)
        and (not mod4 or all(n % 4 == 0 for n in ns))
        and all(4 + 9 * n >= 4 * m for m, n in zip(ms, ns))
    )


def check_deficits(patterns):
    partitions = set()
    for a in range(13):
        for b in range(13 - a):
            c = 12 - a - b
            receiving_labels = (1,) * a + (2,) * b + (3,) * c
            ns = tuple(receiving_labels.count(d) for d in (1, 2, 3))
            need(ns == (a, b, c) and sum(ns) == 12,
                 "TWELVE_FREQUENCY_ROUTING")
            partitions.add(ns)
    need(len(partitions) == 91, "PARTITION_COUNT")
    need(partitions == {
        ns for ns in product(range(13), repeat=3) if sum(ns) == 12
    }, "PARTITION_COMPLETENESS")
    minima = {
        m: min(n for n in range(13)
               if n % 4 == 0 and 4 + 9 * n >= 4 * m)
        for m in (4, 16)
    }
    need(minima == {4: 4, 16: 8}, "COUNT_LOWER_BOUNDS")
    summaries = []
    for ms in sorted(patterns):
        need(not shadow_solutions(ms), "SHADOW_SURVIVOR", str(ms))
        no_div = len(shadow_solutions(ms, mod4=False))
        no_total = len(shadow_solutions(ms, total12=False))
        all_large = ms == (16, 16, 16)
        need(no_div == (0 if all_large else 3),
             "DROPPED_DIVISIBILITY_COUNT")
        need(no_total == (8 if all_large else 18),
             "DROPPED_TOTAL_COUNT")
        summaries.append((ms, no_div, no_total))
    return minima, summaries


def expect_rejection(name, expected_code, action, controls):
    try:
        action()
    except CheckFailure as error:
        need(error.code == expected_code, "WRONG_REJECTION_REASON",
             name + ": received " + error.code)
        controls.append((name, expected_code))
        return
    raise CheckFailure("CONTROL_NOT_REJECTED", name)


def main():
    start = monotonic()
    need(len(sys.argv) == 1, "ARGV", "This checker accepts no arguments.")
    catalog = make_catalog(start)
    histogram, class_counts = exhaust_signs(catalog, start)
    dc_counts, routes = check_four_points()
    patterns, xor_counts = exhaust_cosets(start)
    minima, shadow_counts = check_deficits(patterns)

    constant = (1,) * 16
    bent_quotient = flat_values(T0, (-1, 1, 1, 1))
    constant_spectrum = direct(constant, W16)
    bent_spectrum = direct(bent_quotient, W16)
    for values, spectrum in (
        (constant, constant_spectrum), (bent_quotient, bent_spectrum)
    ):
        check_mod3_inverse(values, spectrum)
        check_h_inverse(values, spectrum)

    controls = []
    expect_rejection(
        "wrong-mod3-inverse-factor", "MOD3_INVERSE",
        lambda: check_mod3_inverse(constant, constant_spectrum, factor=2),
        controls)
    expect_rejection(
        "positive-four-sign-product", "FOUR_SIGN_PRODUCT",
        lambda: flat_values(T0, (1, 1, 1, 1)), controls)
    expect_rejection(
        "wrong-coset-product-sign", "COSET_SIGN_PRODUCT",
        lambda: coset_summary((-1, 1, 1, 1), (0, 0, 0, 0),
                              prediction_sign=1),
        controls)
    expect_rejection(
        "wrong-sixteen-point-scale", "H_SCALE",
        lambda: check_h_inverse(bent_quotient, bent_spectrum,
                                denominator=8),
        controls)
    expect_rejection(
        "wrong-four-point-scale", "PARTIAL_SCALING",
        lambda: check_partial((-1, 3, 3, 3), (8, -4, -4, -4),
                              denominator=2),
        controls)

    check_shadow((16, 4, 4), (7, 2, 3), mod4=False)
    expect_rejection(
        "dropping-n-divisible-four", "NDIV4",
        lambda: check_shadow((16, 4, 4), (7, 2, 3)), controls)
    check_shadow((16, 4, 4), (8, 4, 4), total12=False)
    expect_rejection(
        "dropping-total-nonzero-x", "TOTAL12",
        lambda: check_shadow((16, 4, 4), (8, 4, 4)), controls)
    check_shadow((16, 16, 16), (8, 8, 8), total12=False)
    expect_rejection(
        "dropping-total-zero-x", "TOTAL12",
        lambda: check_shadow((16, 16, 16), (8, 8, 8)), controls)
    expect_rejection(
        "zero-is-not-a-sign-function", "FOUR_POINT_DOMAIN",
        lambda: balanced_route((0, 0, 0, 0)), controls)
    expect_rejection(
        "constant-is-not-balanced", "FOUR_POINT_UNBALANCED",
        lambda: balanced_route((1, 1, 1, 1)), controls)

    need(len(controls) == 10, "CONTROL_COUNT")
    deadline(start)
    print("enumerated_sign_vectors", 65536)
    print("residue_nonzero_histogram", sorted(histogram.items()))
    print("eligible_class_counts", sorted(class_counts.items()))
    print("ineligible_count", 65536 - sum(class_counts.values()))
    print("four_point_dc_counts", sorted(dc_counts.items()))
    print("balanced_receiving_routes", sorted(routes.items()))
    print("coset_support_patterns", sorted(patterns.items()))
    print("xor_label_counts", sorted(xor_counts.items()))
    print("necessary_count_minima", sorted(minima.items()))
    print("shadow_counts_ms_no_div_no_total", shadow_counts)
    print("intended_rejections", controls)
    print("elapsed_seconds", round(monotonic() - start, 6))
    print("RESULT: PASS (finite lemmas and formal necessary shadows only)")


if __name__ == "__main__":
    try:
        main()
    except CheckFailure as error:
        print("RESULT: FAIL", str(error), file=sys.stderr)
        raise SystemExit(1)

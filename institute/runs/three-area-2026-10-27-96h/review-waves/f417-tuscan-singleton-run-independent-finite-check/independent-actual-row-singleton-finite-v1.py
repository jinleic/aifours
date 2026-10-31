import sys
import time
from collections import Counter
from itertools import permutations, product
from math import comb

START = time.monotonic()
BUDGET_SECONDS = 55.0


class CheckFailure(Exception):
    def __init__(self, invariant, detail):
        self.invariant = invariant
        super().__init__(f"{invariant}: {detail}")


def require(condition, invariant, detail):
    if not condition:
        raise CheckFailure(invariant, detail)


def guard():
    require(
        time.monotonic() - START < BUDGET_SECONDS,
        "cooperative_deadline",
        "55-second calculation budget reached",
    )


def word_counts(bits):
    guard()
    n = len(bits)
    require(n >= 3, "word_length", str(n))
    require(all(x in (0, 1) for x in bits), "binary_word", repr(bits))
    runs = []
    start = 0
    for end in range(1, n + 1):
        if end == n or bits[end] != bits[start]:
            runs.append((bits[start], start, end))
            start = end
    b = sum(bits)
    q = sum(color == 1 for color, left, right in runs)
    s = sum(
        color == 1 and right - left == 1
        for color, left, right in runs
    )
    t = sum(
        color == 0 and right - left == 1 and left > 0 and right < n
        for color, left, right in runs
    )
    d = sum(bits[i] == 1 and bits[i + 2] == 1 for i in range(n - 2))
    require(
        d == b - 2 * q + s + t,
        "row_distance_two_identity",
        f"bits={bits}, direct={d}, bqst={(b, q, s, t)}",
    )
    cycle = (0,) + tuple(bits)
    finite_singletons = sum(
        cycle[j - 1] != cycle[j]
        and cycle[(j + 1) % (n + 1)] != cycle[j]
        for j in range(1, n + 1)
    )
    all_singletons = sum(
        cycle[(j - 1) % (n + 1)] != cycle[j]
        and cycle[(j + 1) % (n + 1)] != cycle[j]
        for j in range(n + 1)
    )
    require(
        finite_singletons == s + t,
        "finite_hamiltonian_singletons",
        repr(bits),
    )
    require(
        all_singletons - finite_singletons
        == int(bits[0] == 1 and bits[-1] == 1),
        "infinity_exclusion",
        repr(bits),
    )
    augmented_black_endpoints = sum(
        cycle[j] == 1 and cycle[(j + 2) % (n + 1)] == 1
        for j in range(n + 1)
    )
    require(
        augmented_black_endpoints == d + bits[0] * bits[-1],
        "augmented_wrap_separation",
        repr(bits),
    )
    return b, q, s, t, d


def exhaust_words():
    total = 0
    for n in range(3, 12):
        by_b = Counter()
        boundaries = Counter()
        infinity = Counter()
        for bits in product((0, 1), repeat=n):
            b, q, s, t, d = word_counts(bits)
            by_b[b] += 1
            boundaries[(bits[0], bits[-1])] += 1
            infinity[int(bits[0] == 1 and bits[-1] == 1)] += 1
            total += 1
        require(
            all(by_b[b] == comb(n, b) for b in range(n + 1)),
            "all_b_coverage",
            f"n={n}, histogram={dict(by_b)}",
        )
        require(
            all(boundaries[key] == 2 ** (n - 2)
                for key in product((0, 1), repeat=2)),
            "endpoint_coverage",
            f"n={n}",
        )
        require(
            infinity[1] == 2 ** (n - 2)
            and infinity[0] == 3 * 2 ** (n - 2),
            "infinity_coverage",
            f"n={n}",
        )
        print("WORDS", n, 2 ** n, "ALL_B_AND_BOUNDARIES")
    require(total == 4088, "word_total", str(total))
    print("WORD_TOTAL", total)


def translates(base):
    n = len(base)
    return tuple(
        tuple((x + shift) % n for x in base)
        for shift in range(n)
    )


def validate_t1(rows):
    guard()
    n = len(rows)
    require(n >= 3, "array_order", str(n))
    symbols = set(range(n))
    for index, row in enumerate(rows):
        guard()
        require(
            len(row) == n and sorted(row) == list(range(n)),
            "row_permutation",
            f"row={index}, data={row}",
        )
    universe = {(a, b) for a in symbols for b in symbols if a != b}
    adjacency = Counter(
        (row[i], row[i + 1])
        for row in rows for i in range(n - 1)
    )
    require(
        set(adjacency) == universe
        and sum(adjacency.values()) == n * (n - 1)
        and all(count == 1 for count in adjacency.values()),
        "distance_one_exact",
        f"order={n}, distinct={len(adjacency)}",
    )
    require(
        {row[0] for row in rows} == symbols
        and {row[-1] for row in rows} == symbols,
        "endpoint_permutations",
        f"order={n}",
    )
    events = tuple(
        (row_index, j, row[j - 1], row[j + 1])
        for row_index, row in enumerate(rows)
        for j in range(1, n - 1)
    )
    distance_two = Counter((a, b) for _, _, a, b in events)
    require(
        len(events) == n * (n - 2)
        and set(distance_two).issubset(universe),
        "original_distance_two_slots",
        f"order={n}",
    )
    augmented_adjacency = Counter()
    for row in rows:
        cycle = (n,) + tuple(row)
        for j in range(n + 1):
            augmented_adjacency[
                (cycle[j], cycle[(j + 1) % (n + 1)])
            ] += 1
    augmented_universe = {
        (a, b) for a in range(n + 1) for b in range(n + 1) if a != b
    }
    require(
        set(augmented_adjacency) == augmented_universe
        and all(count == 1 for count in augmented_adjacency.values()),
        "actual_augmented_adjacency_decomposition",
        f"order={n}",
    )
    return {
        "rows": rows, "n": n, "universe": universe,
        "d2": distance_two, "events": events,
    }


def require_t2(data):
    guard()
    repeated = sorted(
        (pair, count) for pair, count in data["d2"].items() if count > 1
    )
    require(
        not repeated,
        "distance_two_injective",
        f"repeated={repeated[:3]}",
    )
    require(
        len(data["universe"] - set(data["d2"])) == data["n"],
        "distance_two_missing_count",
        f"order={data['n']}",
    )


def measure_subset(data, subset):
    q_total = 0
    w_total = 0
    d_total = 0
    for row in data["rows"]:
        bits = tuple(int(x in subset) for x in row)
        b, q, s, t, d = word_counts(bits)
        require(b == len(subset), "subset_row_cardinality", repr(subset))
        q_total += q
        w_total += s + t
        d_total += d
    b = len(subset)
    n = data["n"]
    require(
        q_total == b * (n + 1 - b),
        "t1_black_run_total",
        f"B={sorted(subset)}, q={q_total}",
    )
    direct_from_pairs = sum(
        count for (a, b), count in data["d2"].items()
        if a in subset and b in subset
    )
    require(
        d_total == direct_from_pairs,
        "actual_pair_slot_agreement",
        repr(sorted(subset)),
    )
    require(
        d_total == b * (2 * b - n - 2) + w_total,
        "summed_row_identity",
        repr(sorted(subset)),
    )
    return q_total, w_total, d_total


def missing_mu(data, subset):
    missing = data["universe"] - set(data["d2"])
    return sum(a in subset and b in subset for a, b in missing)


def check_budget(data, subset, claimed_mu=None):
    require_t2(data)
    q_total, w_total, d_total = measure_subset(data, subset)
    actual_mu = missing_mu(data, subset)
    b = len(subset)
    require(
        d_total == b * (b - 1) - actual_mu,
        "t2_distinct_pair_budget",
        repr(sorted(subset)),
    )
    used_mu = actual_mu if claimed_mu is None else claimed_mu
    require(
        w_total == b * (data["n"] + 1 - b) - used_mu,
        "subset_singleton_budget",
        f"B={sorted(subset)}, W={w_total}, "
        f"actual_mu={actual_mu}, claimed_mu={used_mu}",
    )
    return w_total, actual_mu


def expect_rejection(name, operation, intended_invariant):
    guard()
    try:
        operation()
    except CheckFailure as error:
        require(
            error.invariant == intended_invariant,
            "control_wrong_reason",
            f"{name}: wanted={intended_invariant}, got={error}",
        )
        print("CONTROL_REJECTED", name, intended_invariant)
        return 1
    raise CheckFailure("control_survived", name)


def omitted_boundary_mutant(bits):
    b, q, s, t, d = word_counts(bits)
    omitted = int(bits[0] == 1 and bits[1] == 0)
    omitted += int(bits[-1] == 1 and bits[-2] == 0)
    require(omitted > 0, "mutation_fixture", repr(bits))
    require(
        d == b - 2 * q + (s - omitted) + t,
        "row_distance_two_identity",
        f"boundary omitted in {bits}",
    )


def check_original_domain(data, supplied_events):
    require_t2(data)
    expected = data["events"]
    require(
        len(supplied_events) == len(expected)
        and set(supplied_events) == set(expected),
        "original_distance_two_domain",
        f"expected={len(expected)}, supplied={len(supplied_events)}",
    )


def augmented_finite_events(data):
    n = data["n"]
    events = []
    for row_index, row in enumerate(data["rows"]):
        cycle = (n,) + tuple(row)
        for j in range(n + 1):
            a = cycle[j]
            b = cycle[(j + 2) % (n + 1)]
            if a != n and b != n:
                events.append((row_index, j, a, b))
    return tuple(events)


def find_t1_not_t2():
    n = 6
    for tested, tail in enumerate(permutations(range(1, n)), 1):
        guard()
        base = (0,) + tail
        differences = {
            (base[i + 1] - base[i]) % n for i in range(n - 1)
        }
        if differences != set(range(1, n)):
            continue
        data = validate_t1(translates(base))
        if any(count > 1 for count in data["d2"].values()):
            require(tested <= 120, "negative_search_bound", str(tested))
            return data, base, tested
    raise CheckFailure("negative_control_missing", "all 120 bases exhausted")


def check_finite_floors():
    count = 0
    for m in range(2, 21):
        guard()
        numerator = m * m
        denominator = 2 * m - 1
        quotient = numerator // denominator
        require(
            quotient == m // 2
            and quotient * denominator <= numerator
            and numerator < (quotient + 1) * denominator,
            "finite_floor_identity",
            f"m={m}",
        )
        print("FINITE_FLOOR", m, quotient)
        count += 1
    require(count == 19, "finite_floor_coverage", str(count))


def main():
    require(
        len(sys.argv) == 1,
        "fixed_argv",
        "Use: python3 -I -B f417_finite_checker.py",
    )
    exhaust_words()
    positive = validate_t1(translates((0, 3, 1, 2)))
    require_t2(positive)
    require(
        len(positive["d2"]) == 8,
        "positive_t2_binding",
        repr(positive["d2"]),
    )
    expected_missing = {(0, 2), (2, 0), (1, 3), (3, 1)}
    require(
        positive["universe"] - set(positive["d2"]) == expected_missing,
        "positive_missing_pairs",
        "actual ordered missing-pair set",
    )
    print("ACTUAL_T2", positive["rows"])
    print("MISSING_ORDERED_PAIRS", sorted(expected_missing))
    for mask in range(16):
        guard()
        subset = frozenset(x for x in range(4) if (mask >> x) & 1)
        w_total, mu = check_budget(positive, subset)
        print("SUBSET", sorted(subset), "b", len(subset), "mu", mu, "W", w_total)
    check_original_domain(positive, positive["events"])
    rejected = 0
    for name, bits in (
        ("omit_first_black_singleton", (1, 0, 0, 0)),
        ("omit_last_black_singleton", (0, 0, 0, 1)),
    ):
        rejected += expect_rejection(
            name,
            lambda bits=bits: omitted_boundary_mutant(bits),
            "row_distance_two_identity",
        )
    wrong_events = augmented_finite_events(positive)
    require(
        len(positive["events"]) == 8 and len(wrong_events) == 12,
        "mutation_fixture",
        "original versus augmented finite slot counts",
    )
    rejected += expect_rejection(
        "augmented_wrap_as_original",
        lambda: check_original_domain(positive, wrong_events),
        "original_distance_two_domain",
    )
    subset = frozenset((0, 2))
    w_total, mu = check_budget(positive, subset)
    unordered_mu = len({
        tuple(sorted((a, b))) for a, b in expected_missing
        if a in subset and b in subset
    })
    require(
        w_total == 4 and mu == 2 and unordered_mu == 1,
        "mutation_fixture",
        "directed missing-pair controls",
    )
    rejected += expect_rejection(
        "double_missing_pair_count",
        lambda: check_budget(positive, subset, 2 * mu),
        "subset_singleton_budget",
    )
    rejected += expect_rejection(
        "collapse_ordered_missing_pairs",
        lambda: check_budget(positive, subset, unordered_mu),
        "subset_singleton_budget",
    )
    negative, base, tested = find_t1_not_t2()
    print("ACTUAL_T1_NOT_T2_BASE", base, "BASES_EXAMINED", tested)
    print("ACTUAL_T1_NOT_T2_ROWS", negative["rows"])
    rejected += expect_rejection(
        "actual_t1_fails_t2",
        lambda: require_t2(negative),
        "distance_two_injective",
    )
    repeated_pair = min(
        pair for pair, count in negative["d2"].items() if count > 1
    )
    negative_subset = frozenset(repeated_pair)
    q_total, w_total, d_total = measure_subset(negative, negative_subset)
    mu = missing_mu(negative, negative_subset)
    b = len(negative_subset)
    false_t2_budget = b * (negative["n"] + 1 - b) - mu
    distinct_internal = sum(
        a in negative_subset and b in negative_subset
        for a, b in negative["d2"]
    )
    require(
        d_total > distinct_internal and w_total > false_t2_budget,
        "negative_control_exposes_t2_premise",
        f"slots={d_total}, distinct={distinct_internal}, "
        f"W={w_total}, false_budget={false_t2_budget}",
    )
    print(
        "NEGATIVE_SUBSET", sorted(negative_subset),
        "D_SLOTS", d_total, "D_DISTINCT", distinct_internal,
        "MU", mu, "W", w_total, "FALSE_T2_BUDGET", false_t2_budget,
    )
    check_finite_floors()
    require(rejected == 6, "rejection_control_coverage", str(rejected))
    guard()
    print("CONTROL_REJECTIONS", rejected)
    print("RESULT: FINITE_CHECKS_PASS")


if __name__ == "__main__":
    try:
        main()
    except CheckFailure as error:
        print("RESULT: FAIL", str(error), file=sys.stderr)
        sys.exit(1)

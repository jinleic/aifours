
from collections import Counter
from itertools import combinations, permutations, product
import resource
import sys
import time


class CheckError(Exception):
    pass


START = time.monotonic()
TIME_LIMIT = 55.0
RSS_LIMIT = 128 * 1024 * 1024
PAIRS = ((0, 1), (0, 2), (1, 2))
VERTICES = tuple((i, a) for i in range(3) for a in range(4))
ONE_EACH = Counter({v: 1 for v in VERTICES})
UNIVERSE = frozenset(range(4))


def require(condition, reason):
    if not condition:
        raise CheckError(reason)


def peak_rss_bytes():
    require(sys.platform in ("darwin", "linux"), "UNSUPPORTED_RSS_UNITS")
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == "darwin" else value * 1024)


def guard():
    if time.monotonic() - START >= TIME_LIMIT:
        raise CheckError("BUDGET_TIME")
    if peak_rss_bytes() > RSS_LIMIT:
        raise CheckError("BUDGET_RSS")


def edge(i, a, j, b):
    return tuple(sorted(((i, a), (j, b))))


def edge_pair(e):
    return (e[0][0], e[1][0])


def make_system(sigma):
    return (
        frozenset(edge(0, a, 1, a) for a in range(4)),
        frozenset(edge(0, a, 2, a) for a in range(4)),
        frozenset(edge(1, a, 2, sigma[a]) for a in range(4)),
    )


def union_edges(system):
    return frozenset(e for matching in system for e in matching)


def check_system(system):
    require(len(system) == 3, "SYSTEM_SIZE")
    for pair, matching in zip(PAIRS, system):
        require(len(matching) == 4, "PAIR_MATCHING_SIZE")
        require(
            all(edge_pair(e) == pair for e in matching),
            "PAIR_MATCHING_PARTIES",
        )
        expected = Counter(
            {(i, a): 1 for i in pair for a in range(4)}
        )
        observed = Counter(v for e in matching for v in e)
        require(observed == expected, "PAIR_MATCHING_DEGREE")


def check_t_shape(t):
    require(len(t) == 6, "T_SIZE")
    require(
        Counter(v for e in t for v in e) == ONE_EACH,
        "T_DEGREE",
    )
    require(
        Counter(edge_pair(e) for e in t)
        == Counter({pair: 2 for pair in PAIRS}),
        "T_PAIR_COUNT",
    )


def check_shared_incidence(system, t):
    whole = union_edges(system)
    require(t <= whole, "T_SHARED_INCIDENCE")
    f = whole - t
    require(len(f) == 6, "F_SIZE")
    require(
        Counter(v for e in f for v in e) == ONE_EACH,
        "F_DEGREE",
    )


def complements(n_sets):
    require(
        len(n_sets) == 3
        and all(len(n) == 2 and n <= UNIVERSE for n in n_sets),
        "N_BALANCE",
    )
    return tuple(UNIVERSE - n for n in n_sets)


def endpoint_ok(color, s_sets):
    return all(
        all(a in s_sets[i] for i, a in e)
        for e in color
    )


def quadrant_counts(system, sets):
    return tuple(
        sum(all(a in sets[i] for i, a in e) for e in matching)
        for matching in system
    )


def shadow_ok(counts):
    return sum(value > 0 for value in counts) <= 1


def check_local(system, t, color, n_sets):
    check_system(system)
    check_t_shape(t)
    require(len(color) == 2 and color <= t, "COLOR")
    s_sets = complements(n_sets)
    require(endpoint_ok(color, s_sets), "COLOR_ENDPOINTS")
    require(
        shadow_ok(quadrant_counts(system, s_sets)),
        "SLICE_SHADOW",
    )
    check_shared_incidence(system, t)


def check_binary_rows(rows):
    require(
        len(rows) == 4 and all(len(row) == 3 for row in rows),
        "BINARY_SHAPE",
    )
    require(
        all(value in (0, 1) for row in rows for value in row),
        "BINARY_ALPHABET",
    )
    require(
        all(sum(row[i] for row in rows) == 2 for i in range(3)),
        "BINARY_BALANCE",
    )
    require(len(set(rows)) == 4, "DUPLICATE_WORDS")
    return sum(
        len({(row[i], row[j]) for row in rows}) < 4
        for i, j in PAIRS
    )


def check_actual_slice(system, n_sets, rows):
    complements(n_sets)
    require(
        len(rows) == 4 and all(len(row) == 3 for row in rows),
        "SLICE_SHAPE",
    )
    require(len(set(rows)) == 4, "SLICE_DUPLICATES")
    for i in range(3):
        expected = Counter({a: 2 for a in n_sets[i]})
        require(
            Counter(row[i] for row in rows) == expected,
            "SLICE_BALANCE",
        )
    sizes = []
    for (i, j), matching in zip(PAIRS, system):
        projection = {(row[i], row[j]) for row in rows}
        require(
            all(edge(i, a, j, b) not in matching for a, b in projection),
            "SLICE_FORBIDDEN_PAIR",
        )
        sizes.append(len(projection))
    nonfull = sum(size < 4 for size in sizes)
    require(nonfull <= 1, "SLICE_PARTITION_LEMMA")
    return nonfull


def component_signature(system):
    adjacency = {v: set() for v in VERTICES}
    for e in union_edges(system):
        a, b = e
        adjacency[a].add(b)
        adjacency[b].add(a)
    require(
        all(len(adjacency[v]) == 2 for v in VERTICES),
        "UNION_DEGREE",
    )
    seen = set()
    sizes = []
    for start in VERTICES:
        if start in seen:
            continue
        stack = [start]
        seen.add(start)
        size = 0
        while stack:
            v = stack.pop()
            size += 1
            for w in adjacency[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        sizes.append(size)
    return tuple(sorted(sizes))


def expect_error(label, reason, operation):
    try:
        operation()
    except CheckError as exc:
        require(str(exc) == reason, "WRONG_CONTROL_REASON_" + label)
        return label
    raise CheckError("CONTROL_ACCEPTED_" + label)


def partition_checks():
    bases = (
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
    )
    categories = {
        1: "all_equal",
        2: "exactly_two_equal",
        3: "all_distinct",
    }
    partitions = Counter()
    orientations = Counter()
    valid_nonfull = Counter()
    duplicates = 0

    for choices in product(range(3), repeat=3):
        guard()
        category = categories[len(set(choices))]
        partitions[category] += 1
        for flips in product(range(2), repeat=3):
            rows = tuple(
                tuple(
                    bases[choices[i]][r] ^ flips[i]
                    for i in range(3)
                )
                for r in range(4)
            )
            orientations[category] += 1
            require(
                all(sum(row[i] for row in rows) == 2 for i in range(3)),
                "GENERATED_BINARY_BALANCE",
            )
            sizes = tuple(
                len({(row[i], row[j]) for row in rows})
                for i, j in PAIRS
            )
            expected_sizes = tuple(
                2 if choices[i] == choices[j] else 4
                for i, j in PAIRS
            )
            require(sizes == expected_sizes, "PARTITION_INTERSECTION")
            if len(set(choices)) == 1:
                require(len(set(rows)) == 2, "ALL_EQUAL_DUPLICATION")
                duplicates += 1
            else:
                nonfull = check_binary_rows(rows)
                require(nonfull <= 1, "FOUR_WORD_LEMMA")
                valid_nonfull[nonfull] += 1

    require(
        partitions == Counter({
            "all_equal": 3,
            "exactly_two_equal": 18,
            "all_distinct": 6,
        }),
        "PARTITION_TOTALS",
    )
    require(
        orientations == Counter({
            "all_equal": 24,
            "exactly_two_equal": 144,
            "all_distinct": 48,
        }),
        "ORIENTATION_TOTALS",
    )
    require(valid_nonfull == Counter({0: 48, 1: 144}), "VALID_WORD_TOTALS")
    require(duplicates == 24, "DUPLICATE_TOTAL")
    return partitions, orientations, valid_nonfull, duplicates


def matching_records():
    graphs = Counter()
    t_count_distribution = Counter()
    records_by_graph = Counter()
    records = []
    t_candidates = 0

    for sigma in permutations(range(4)):
        guard()
        system = make_system(sigma)
        check_system(system)
        signature = component_signature(system)
        graphs[signature] += 1
        choices = [
            tuple(combinations(sorted(matching), 2))
            for matching in system
        ]
        accepted_here = 0
        for groups in product(*choices):
            guard()
            t_candidates += 1
            t = frozenset(e for group in groups for e in group)
            if Counter(v for e in t for v in e) != ONE_EACH:
                continue
            check_t_shape(t)
            check_shared_incidence(system, t)
            accepted_here += 1
            records.append((system, t))
            records_by_graph[signature] += 1
        t_count_distribution[accepted_here] += 1

    require(
        graphs == Counter({
            (3, 3, 3, 3): 1,
            (3, 3, 6): 6,
            (6, 6): 3,
            (3, 9): 8,
            (12,): 6,
        }),
        "GRAPH_CLASSIFICATION",
    )
    require(t_candidates == 5184, "T_CANDIDATE_TOTAL")
    require(
        t_count_distribution == Counter({0: 15, 2: 6, 4: 3}),
        "T_COUNT_DISTRIBUTION",
    )
    require(len(records) == 24, "T_RECORD_TOTAL")
    require(
        records_by_graph == Counter({(6, 6): 12, (12,): 12}),
        "ALTERNATING_COMPONENT_TOTALS",
    )
    return graphs, t_count_distribution, records_by_graph, records, t_candidates


def local_and_coloring_checks(records):
    two_subsets = tuple(
        frozenset(values) for values in combinations(range(4), 2)
    )
    n_triples = tuple(product(two_subsets, repeat=3))
    require(len(n_triples) == 216, "N_TRIPLE_TOTAL")
    totals = Counter()
    color_families = Counter()
    colorings = 0
    colorings_with_local_options = 0

    for system, t in records:
        ordered = tuple(sorted(t))
        option_counts = {}
        for selected in combinations(ordered, 2):
            guard()
            color = frozenset(selected)
            totals["color_choices"] += 1
            same_pair = edge_pair(selected[0]) == edge_pair(selected[1])
            key = "same" if same_pair else "split"
            options = 0
            for n_sets in n_triples:
                guard()
                totals["tested"] += 1
                totals[key + "_tested"] += 1
                s_sets = complements(n_sets)
                nn = quadrant_counts(system, n_sets)
                ss = quadrant_counts(system, s_sets)
                require(nn == ss, "MATCHING_QUADRANT_IDENTITY")
                totals["identity_checks"] += 3
                if not endpoint_ok(color, s_sets):
                    continue
                totals["endpoint_pass"] += 1
                totals[key + "_endpoint"] += 1
                if shadow_ok(ss):
                    options += 1
                    totals["slice_shadow_survivors"] += 1
                else:
                    totals[key + "_shadow_rejected"] += 1
            option_counts[color] = options

        coverage = Counter()
        for first in combinations(range(6), 2):
            remaining = tuple(i for i in range(6) if i not in first)
            for second in combinations(remaining, 2):
                guard()
                third = tuple(i for i in remaining if i not in second)
                groups = (first, second, third)
                colors = tuple(
                    frozenset(ordered[i] for i in group)
                    for group in groups
                )
                require(
                    frozenset().union(*colors) == t
                    and sum(len(c) for c in colors) == 6,
                    "COLOR_PARTITION",
                )
                matrix = tuple(
                    tuple(
                        sum(edge_pair(e) == pair for e in color)
                        for pair in PAIRS
                    )
                    for color in colors
                )
                require(
                    all(sum(row) == 2 for row in matrix)
                    and all(
                        sum(matrix[r][c] for r in range(3)) == 2
                        for c in range(3)
                    ),
                    "COLOR_INCIDENCE_BALANCE",
                )
                concentrated = sum(2 in row for row in matrix)
                require(concentrated in (0, 1, 3), "COLOR_FAMILY")
                color_families[concentrated] += 1
                coverage.update(colors)
                colorings += 1
                if all(option_counts[color] > 0 for color in colors):
                    colorings_with_local_options += 1
        require(
            set(coverage) == set(option_counts)
            and all(value == 18 for value in coverage.values()),
            "LABELED_COLOR_COVERAGE",
        )

    expected = {
        "color_choices": 360,
        "tested": 77760,
        "same_tested": 15552,
        "split_tested": 62208,
        "identity_checks": 233280,
        "endpoint_pass": 3024,
        "same_endpoint": 432,
        "split_endpoint": 2592,
        "slice_shadow_survivors": 0,
        "same_shadow_rejected": 432,
        "split_shadow_rejected": 2592,
    }
    require(totals == Counter(expected), "LOCAL_ENUMERATION_TOTALS")
    require(colorings == 2160, "LABELED_COLORING_TOTAL")
    require(
        color_families == Counter({3: 144, 1: 864, 0: 1152}),
        "COLOR_FAMILY_TOTALS",
    )
    require(
        colorings_with_local_options == 0,
        "GLOBAL_COLORING_SURVIVOR",
    )
    return totals, color_families, colorings, colorings_with_local_options


def control_checks():
    guard()
    distinct_partitions = (
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    )
    two_equal_partitions = (
        (0, 0, 0),
        (0, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    )
    require(check_binary_rows(distinct_partitions) == 0, "POSITIVE_BINARY_0")
    require(check_binary_rows(two_equal_partitions) == 1, "POSITIVE_BINARY_1")

    system = make_system((1, 0, 3, 2))
    t = frozenset((
        edge(0, 0, 1, 0),
        edge(0, 2, 1, 2),
        edge(0, 1, 2, 1),
        edge(0, 3, 2, 3),
        edge(1, 1, 2, 0),
        edge(1, 3, 2, 2),
    ))
    color = frozenset((
        edge(0, 0, 1, 0),
        edge(0, 2, 1, 2),
    ))
    check_system(system)
    check_t_shape(t)
    check_shared_incidence(system, t)

    mutated = make_system((2, 3, 0, 1))
    n_incidence = (
        frozenset((1, 3)),
        frozenset((1, 3)),
        frozenset((0, 2)),
    )
    actual_rows = (
        (1, 3, 0),
        (1, 3, 2),
        (3, 1, 0),
        (3, 1, 2),
    )
    check_system(mutated)
    require(
        check_actual_slice(mutated, n_incidence, actual_rows) == 1,
        "POSITIVE_ACTUAL_SLICE",
    )
    s_incidence = complements(n_incidence)
    require(endpoint_ok(color, s_incidence), "CONTROL_ENDPOINTS")
    require(
        quadrant_counts(mutated, s_incidence) == (2, 0, 0),
        "CONTROL_INCIDENCE_SHADOW",
    )
    require(not t <= union_edges(mutated), "CONTROL_NOT_MUTATED")

    n_shadow = tuple(frozenset((1, 3)) for _ in range(3))
    require(endpoint_ok(color, complements(n_shadow)), "CONTROL_SHADOW_ENDPOINTS")
    require(
        quadrant_counts(system, complements(n_shadow)) == (2, 2, 0),
        "CONTROL_SHADOW_COUNTS",
    )
    check_shared_incidence(system, t)

    rejected = []
    rejected.append(expect_error(
        "duplicate_binary",
        "DUPLICATE_WORDS",
        lambda: check_binary_rows((
            (0, 0, 0),
            (0, 0, 0),
            (1, 1, 1),
            (1, 1, 1),
        )),
    ))
    rejected.append(expect_error(
        "slice_shadow",
        "SLICE_SHADOW",
        lambda: check_local(system, t, color, n_shadow),
    ))
    rejected.append(expect_error(
        "shared_incidence",
        "T_SHARED_INCIDENCE",
        lambda: check_local(mutated, t, color, n_incidence),
    ))
    return rejected


def main():
    require(len(sys.argv) == 1, "UNEXPECTED_ARGUMENTS")
    guard()
    partitions, orientations, valid_nonfull, duplicates = partition_checks()
    graphs, distribution, by_graph, records, t_candidates = matching_records()
    totals, families, colorings, global_survivors = local_and_coloring_checks(records)
    rejected = control_checks()
    guard()

    print("status: COMPLETE_FINITE_QUOTIENT_CHECK")
    print("partition_triples:", sorted(partitions.items()))
    print("oriented_arrays:", sorted(orientations.items()))
    print("valid_arrays_by_nonfull_pairs:", sorted(valid_nonfull.items()))
    print("duplicate_arrays:", duplicates)
    print("graph_signatures:", sorted(graphs.items()))
    print("T_candidates:", t_candidates)
    print("systems_by_number_of_T:", sorted(distribution.items()))
    print("accepted_T_by_graph:", sorted(by_graph.items()))
    print("accepted_M_T_records:", len(records))
    for name in (
        "color_choices",
        "tested",
        "same_tested",
        "split_tested",
        "identity_checks",
        "endpoint_pass",
        "same_endpoint",
        "split_endpoint",
        "same_shadow_rejected",
        "split_shadow_rejected",
        "slice_shadow_survivors",
    ):
        print(name + ":", totals[name])
    print("labeled_colorings:", colorings)
    print("color_families_by_concentrated_rows:", sorted(families.items()))
    print("colorings_with_local_options:", global_survivors)
    print("intended_negative_controls:", ", ".join(rejected))
    print("elapsed_seconds_observed:", time.monotonic() - START)
    print("peak_rss_bytes_observed:", peak_rss_bytes())
    print("scope: necessary combinatorial quotient only")


if __name__ == "__main__":
    try:
        main()
    except CheckError as exc:
        print("status: INCOMPLETE")
        print("reason:", str(exc))
        raise SystemExit(1)


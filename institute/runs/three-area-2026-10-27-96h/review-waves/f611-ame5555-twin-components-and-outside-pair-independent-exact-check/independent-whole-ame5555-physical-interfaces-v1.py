from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from time import monotonic
import sys

PAIRS = tuple(combinations(range(4), 2))
CUTS = (
    ((0, 1), (2, 3)),
    ((0, 2), (1, 3)),
    ((0, 3), (1, 2)),
)
ZERO = (Fraction(0), Fraction(0))
TWO = (Fraction(2), Fraction(0))
DEADLINE = 0.0


class CheckFailure(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def tick():
    need(monotonic() <= DEADLINE, "cooperative-55-second-budget-exhausted")


def project(word, coordinates):
    return tuple(word[i] for i in coordinates)


def compositions(total, parts, minimum):
    if parts == 1:
        if total >= minimum:
            yield (total,)
        return
    upper = total - minimum * (parts - 1)
    for first in range(minimum, upper + 1):
        for tail in compositions(total - first, parts - 1, minimum):
            yield (first,) + tail


def pair_counters(words):
    need(len(set(words)) == len(words), "duplicate-support-word")
    return {
        pair: Counter(project(word, pair) for word in words)
        for pair in PAIRS
    }


def require_pair_multiplicity(words, multiplicity):
    counters = pair_counters(words)
    for pair in PAIRS:
        need(bool(counters[pair]), "empty-pair-projection")
        need(
            set(counters[pair].values()) == {multiplicity},
            "physical-pair-multiplicity",
        )
    return counters


def require_injective_pair(words, pair):
    values = tuple(project(word, pair) for word in words)
    need(len(set(values)) == len(values), "maximal-pair-collision")


def actual_claims(words):
    return {
        pair: tuple(project(word, pair) for word in words)
        for pair in PAIRS
    }


def require_bound_claims(words, claims):
    need(set(claims) == set(PAIRS), "missing-pair-claim")
    for pair in PAIRS:
        need(len(claims[pair]) == len(words), "pair-claim-length")
        need(
            tuple(claims[pair]) ==
            tuple(project(word, pair) for word in words),
            "same-word-projection",
        )


def block_count(words, cut):
    row_coordinates, column_coordinates = cut
    rows = {}
    columns = {}
    for word in words:
        row = project(word, row_coordinates)
        column = project(word, column_coordinates)
        rows.setdefault(row, set()).add(column)
        columns.setdefault(column, set()).add(row)
    need(all(len(values) == 2 for values in rows.values()),
         "physical-row-degree")
    need(all(len(values) == 2 for values in columns.values()),
         "physical-column-degree")
    blocks = set()
    for row, values in rows.items():
        c0, c1 = sorted(values)
        need(columns[c0] == columns[c1], "non-rectangular-actual-cut")
        need(len(columns[c0]) == 2, "physical-block-row-count")
        block_rows = frozenset(columns[c0])
        for other in block_rows:
            need(rows[other] == values, "physical-block-closure")
        blocks.add((block_rows, frozenset(values)))
    return len(blocks)


def check_degrees_and_moments(stats):
    profiles = tuple(compositions(12, 5, 2))
    need(len(profiles) == 15, "ordered-degree-profile-count")
    need(
        {tuple(sorted(p)) for p in profiles} ==
        {(2, 2, 2, 3, 3), (2, 2, 2, 2, 4)},
        "degree-profile-classification",
    )
    c = 4 * (5 * 6 - 12)
    m = len(PAIRS) * (5 * 5 - 12)
    need((c, m) == (72, 78), "5555-maximal-moments")
    histograms = set()
    for n in compositions(24, 5, 0):
        tick()
        if sum(k * n[k] for k in range(5)) != c:
            continue
        if sum(k * (k - 1) // 2 * n[k] for k in range(5)) != m:
            continue
        if 6 * n[0] + 3 * n[1] + n[2] != 6:
            continue
        if n[1] > 1:
            continue
        need(3 * n[0] + n[1] + n[4] == 6,
             "moment-elimination-one")
        need(n[4] == 3 * n[0] + 2 * n[1] + n[2],
             "moment-elimination-two")
        histograms.add(n)
    expected = {
        (1, 0, 0, 20, 3),
        (0, 0, 6, 12, 6),
        (0, 1, 3, 15, 5),
    }
    need(histograms == expected, "moment-outside-histograms")
    exceptional_occupancies = set()
    for degree in (2, 3, 4):
        for occupancy in compositions(6 - degree, 4, 0):
            if sum(h * occupancy[h] for h in range(4)) != 3:
                continue
            need(
                degree ==
                3 - occupancy[0] + occupancy[2] + 2 * occupancy[3],
                "local-outside-identity",
            )
            if degree == 4:
                exceptional_occupancies.add(tuple(
                    h
                    for h in range(4)
                    for unused in range(occupancy[h])
                ))
    need(exceptional_occupancies == {(0, 3), (1, 2)},
         "exceptional-outside-occupancies")
    need(all(max(values) >= 2 for values in exceptional_occupancies),
         "exceptional-needs-two-outside")
    for p in profiles:
        need(not any(
            p[a] >= 4 and p[b] >= 4
            for a, b in combinations(range(5), 2)
        ), "two-degree-four-profile")
    stats["ordered_degree_profiles"] = len(profiles)
    stats["maximal_histograms"] = len(histograms)
    return profiles


def require_distinct_slice_demands(profile, demands):
    need(len(profile) == 5 and min(profile) >= 2 and sum(profile) == 12,
         "invalid-degree-profile")
    fits = any(
        all(profile[index] >= demand
            for index, demand in zip(indices, demands))
        for indices in permutations(range(5), len(demands))
    )
    need(fits, "two-degree4-slices")


def perfect_matchings(vertices):
    if not vertices:
        yield ()
        return
    first = vertices[0]
    for index in range(1, len(vertices)):
        second = vertices[index]
        rest = vertices[1:index] + vertices[index + 1:]
        for tail in perfect_matchings(rest):
            yield ((first, second),) + tail


def require_colours(colours, order):
    need(len(colours) == 3, "matching-colour-count")
    used_edges = set()
    for matching in colours:
        vertices = tuple(v for edge in matching for v in edge)
        need(len(vertices) == order, "matching-size")
        need(set(vertices) == set(range(order)), "matching-vertex-coverage")
        need(len(set(vertices)) == order, "matching-vertex-repeat")
        edges = {tuple(sorted(edge)) for edge in matching}
        need(all(a != b for a, b in edges), "matching-loop")
        need(not (used_edges & edges), "matching-edge-repeat")
        used_edges.update(edges)


def bipartition(colours, order):
    adjacency = [[] for unused in range(order)]
    for matching in colours:
        for a, b in matching:
            adjacency[a].append(b)
            adjacency[b].append(a)
    need(all(len(row) == 3 for row in adjacency), "cubic-degree")
    colour = [-1] * order
    for root in range(order):
        if colour[root] != -1:
            continue
        colour[root] = 0
        stack = [root]
        while stack:
            vertex = stack.pop()
            for other in adjacency[vertex]:
                if colour[other] == -1:
                    colour[other] = 1 - colour[vertex]
                    stack.append(other)
                elif colour[other] == colour[vertex]:
                    return None
    return tuple(colour)


def triples_from_colours(colours, order):
    triples = [[None, None, None] for unused in range(order)]
    for coordinate, matching in enumerate(colours):
        for label, edge in enumerate(matching):
            for vertex in edge:
                triples[vertex][coordinate] = label
    need(all(value is not None for row in triples for value in row),
         "unassigned-coordinate-value")
    return tuple(tuple(row) for row in triples)


def require_slice(triples, degree):
    need(len(set(triples)) == len(triples), "slice-duplicate")
    need(len(triples) == 2 * degree, "slice-size")
    for coordinate in range(3):
        counts = Counter(row[coordinate] for row in triples)
        need(len(counts) == degree and set(counts.values()) == {2},
             "slice-coordinate-degree")


def place_component(triples, twin_coordinate):
    remaining = tuple(i for i in range(4) if i != twin_coordinate)
    words = []
    for high in (0, 1):
        for triple in triples:
            word = [None] * 4
            word[twin_coordinate] = high
            for coordinate, value in zip(remaining, triple):
                word[coordinate] = value
            words.append(tuple(word))
    return tuple(words)


def check_common_twins(profiles, stats):
    pool = tuple(perfect_matchings(tuple(range(6))))
    need(len(pool) == 15, "six-vertex-perfect-matching-count")
    masks = tuple(frozenset(matching) for matching in pool)
    edge_distinct = 0
    accepted = 0
    component_placements = 0
    first_triples = None
    q = (Fraction(3, 5), Fraction(4, 5))
    for ia, a in enumerate(pool):
        tick()
        for ib, b in enumerate(pool):
            if masks[ia] & masks[ib]:
                continue
            used = masks[ia] | masks[ib]
            for ic, c in enumerate(pool):
                if used & masks[ic]:
                    continue
                colours = (a, b, c)
                require_colours(colours, 6)
                edge_distinct += 1
                sides = bipartition(colours, 6)
                if sides is None:
                    continue
                accepted += 1
                triples = triples_from_colours(colours, 6)
                require_slice(triples, 3)
                for pair in combinations(range(3), 2):
                    need(len({project(t, pair) for t in triples}) == 6,
                         "common-triple-pair-injectivity")
                z = tuple(q if side == 0 else (-q[0], -q[1])
                          for side in sides)
                for matching in colours:
                    for u, v in matching:
                        need(gadd(z[u], z[v]) == ZERO,
                             "complex-edge-alternation")
                for twin_coordinate in range(4):
                    component = place_component(triples, twin_coordinate)
                    require_pair_multiplicity(component, 2)
                    for cut in CUTS:
                        need(block_count(component, cut) == 3,
                             "twin-component-actual-cut")
                    component_placements += 1
                forced_remainder = tuple(
                    next(iter(set(range(4)) -
                              {t[coordinate] for t in triples}))
                    for coordinate in range(3)
                )
                need(forced_remainder == (3, 3, 3),
                     "six-to-eight-remainder-labels")
                leftovers = (forced_remainder, forced_remainder)
                need(len(set(leftovers)) == 1,
                     "six-to-eight-leftovers-not-identical")
                if first_triples is None:
                    first_triples = triples
    need(accepted == 120, "bipartite-six-vertex-coloured-count")
    need(first_triples is not None, "missing-six-triple-control")
    for profile in profiles:
        fits_eight_overlap = any(
            profile[a] >= 4 and profile[b] >= 4
            for a, b in combinations(range(5), 2)
        )
        need(not fits_eight_overlap, "eight-overlap-degree-demand")
    stats["edge_distinct_six_vertex_colour_triples"] = edge_distinct
    stats["bipartite_six_vertex_colour_triples"] = accepted
    stats["twin_component_physical_placements"] = component_placements
    stats["eight_overlap_degree_profiles_checked"] = len(profiles)
    return first_triples, pool


def rectangle_closure(initial):
    words = set(initial)
    while True:
        tick()
        additions = set()
        for row_coordinates, column_coordinates in CUTS:
            rows = {}
            for word in words:
                rows.setdefault(project(word, row_coordinates), set()).add(
                    project(word, column_coordinates)
                )
            need(all(len(columns) <= 2 for columns in rows.values()),
                 "closure-row-overflow")
            for left, right in combinations(rows, 2):
                if not (rows[left] & rows[right]):
                    continue
                columns = rows[left] | rows[right]
                need(len(columns) <= 2, "closure-incompatible-columns")
                for row in (left, right):
                    for column in columns:
                        word = [None] * 4
                        for coordinate, value in zip(row_coordinates, row):
                            word[coordinate] = value
                        for coordinate, value in zip(
                                column_coordinates, column):
                            word[coordinate] = value
                        additions.add(tuple(word))
        additions -= words
        if not additions:
            return frozenset(words)
        words.update(additions)
        need(len(words) <= 16, "binary-closure-universe")
        counters = pair_counters(tuple(words))
        need(all(value <= 2 for counts in counters.values()
                 for value in counts.values()),
             "closure-pair-overflow")


def partition_key(column):
    groups = (
        tuple(i for i, value in enumerate(column) if value == 0),
        tuple(i for i, value in enumerate(column) if value == 1),
    )
    return tuple(sorted(groups))


def check_low_slices(stats):
    columns = tuple(
        tuple(0 if i in zeros else 1 for i in range(4))
        for zeros in combinations(range(4), 2)
    )
    classification = Counter()
    relevant_low_distance = 0
    closures = 0
    examined = 0
    for chosen in product(columns, repeat=3):
        tick()
        examined += 1
        triples = tuple(zip(*chosen))
        keys = tuple(partition_key(column) for column in chosen)
        distinct = len(set(keys))
        classification[distinct] += 1
        if distinct == 2:
            need(any(
                sum(x != y for x, y in zip(a, b)) == 1
                for a, b in combinations(triples, 2)
            ), "equal-partitions-distance-one")
        relevant = keys[0] != keys[1] and keys[0] != keys[2]
        if not relevant:
            continue
        if keys[1] == keys[2]:
            reference = triples[0]
            need(any(
                other[0] != reference[0] and
                other[1:] == reference[1:]
                for other in triples[1:]
            ), "specified-low-distance-one")
            relevant_low_distance += 1
            continue
        need(distinct == 3, "low-slice-partition-routing")
        a_slice = tuple((0,) + triple for triple in triples)
        b = a_slice[0][1]
        extensions = tuple(word for word in a_slice if word[1] == b)
        need(len(extensions) == 2, "low-low-two-extensions")
        left, right = extensions
        need(left[2] != right[2] and left[3] != right[3],
             "low-low-both-complements-differ")
        seed = a_slice + (
            (1, b, left[2], right[3]),
            (1, b, right[2], left[3]),
        )
        closed = rectangle_closure(seed)
        parity = sum(a_slice[0]) % 2
        expected = frozenset(
            word for word in product((0, 1), repeat=4)
            if sum(word) % 2 == parity
        )
        need(closed == expected, "actual-eight-word-parity-closure")
        require_pair_multiplicity(tuple(closed), 2)
        for cut in CUTS:
            need(block_count(closed, cut) == 2,
                 "eight-word-physical-cut-blocks")
        closures += 1
    need(examined == 216, "labelled-low-slice-count")
    need(dict(classification) == {1: 24, 2: 144, 3: 48},
         "low-slice-partition-classification")
    need(relevant_low_distance == 48, "relevant-low-distance-count")
    need(closures == 48, "all-distinct-closure-count")
    stats["labelled_low_slice_partition_triples"] = examined
    stats["specified_low_distance_rejections"] = relevant_low_distance
    stats["actual_eight_word_closures"] = closures


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1],
            a[0] * b[1] + a[1] * b[0])


def gconj(a):
    return (a[0], -a[1])


def gnorm(a):
    return a[0] * a[0] + a[1] * a[1]


def gaussian_sum(values):
    result = ZERO
    for value in values:
        result = gadd(result, value)
    return result


def cut_is_scaled_unitary(amplitudes, cut):
    row_coordinates, column_coordinates = cut
    rows = tuple(sorted({
        project(word, row_coordinates) for word in amplitudes
    }))
    columns = tuple(sorted({
        project(word, column_coordinates) for word in amplitudes
    }))
    if len(rows) != 4 or len(columns) != 4:
        return False
    matrix = {
        (project(word, row_coordinates),
         project(word, column_coordinates)): value
        for word, value in amplitudes.items()
    }
    for a, b in product(rows, repeat=2):
        value = gaussian_sum(
            gmul(matrix.get((a, c), ZERO),
                 gconj(matrix.get((b, c), ZERO)))
            for c in columns
        )
        if value != (TWO if a == b else ZERO):
            return False
    for a, b in product(columns, repeat=2):
        value = gaussian_sum(
            gmul(gconj(matrix.get((r, a), ZERO)),
                 matrix.get((r, b), ZERO))
            for r in rows
        )
        if value != (TWO if a == b else ZERO):
            return False
    return True


def orthogonality_exponent_row(words, cut, p, q, r, s):
    row_coordinates, column_coordinates = cut
    need(project(p, row_coordinates) == project(q, row_coordinates),
         "phase-first-actual-row")
    need(project(r, row_coordinates) == project(s, row_coordinates),
         "phase-second-actual-row")
    need(project(p, row_coordinates) != project(r, row_coordinates),
         "phase-distinct-actual-rows")
    need(project(p, column_coordinates) == project(r, column_coordinates),
         "phase-first-shared-column")
    need(project(q, column_coordinates) == project(s, column_coordinates),
         "phase-second-shared-column")
    need(project(p, column_coordinates) != project(q, column_coordinates),
         "phase-distinct-columns")
    coefficients = Counter()
    coefficients[p] += 1
    coefficients[s] += 1
    coefficients[r] -= 1
    coefficients[q] -= 1
    return tuple(coefficients[word] for word in words)


def require_integer_certificate(rows, coefficients):
    need(len(rows) == len(coefficients), "phase-certificate-length")
    need(all(type(value) is int for value in coefficients),
         "noninteger-phase-certificate")
    residual = tuple(
        sum(c * row[index] for c, row in zip(coefficients, rows))
        for index in range(len(rows[0]))
    )
    need(all(value == 0 for value in residual), "integer-exponents")
    need(sum(coefficients) % 2 == 1, "phase-sign-not-contradictory")


def require_all_physical_cuts(flags):
    need(len(flags) == 3 and all(flags), "missing-physical-cut")


def check_complex_phases(stats):
    words = tuple(
        word for word in product((0, 1), repeat=4)
        if sum(word) % 2 == 0
    )
    require_pair_multiplicity(words, 2)
    for cut in CUTS:
        need(block_count(words, cut) == 2, "phase-support-actual-cut")
    a = (0, 0, 0, 0)
    b = (0, 0, 1, 1)
    c = (0, 1, 0, 1)
    f = (1, 0, 1, 0)
    g = (1, 1, 0, 0)
    h = (1, 1, 1, 1)
    rows = (
        orthogonality_exponent_row(words, CUTS[0], a, b, g, h),
        orthogonality_exponent_row(words, CUTS[1], a, c, f, h),
        orthogonality_exponent_row(words, CUTS[2], b, c, f, g),
    )
    require_integer_certificate(rows, (1, -1, 1))
    wrong_residual = tuple(sum(row[index] for row in rows)
                           for index in range(len(words)))
    need(any(value != 0 for value in wrong_residual),
         "wrong-real-only-certificate-control")
    need(all(value % 2 == 0 for value in wrong_residual),
         "wrong-certificate-is-not-F2-only")
    q = (Fraction(3, 5), Fraction(4, 5))
    need(gnorm(q) == 1 and q[1] != 0, "nonreal-unit-phase")
    one = (Fraction(1), Fraction(0))
    minus_one = (Fraction(-1), Fraction(0))
    amplitudes = {
        word: q if word[0] == 0 else
        (minus_one if word in (f, g) else one)
        for word in words
    }
    need(all(gnorm(value) == 1 for value in amplitudes.values()),
         "two-cut-control-unit-moduli")
    flags = tuple(cut_is_scaled_unitary(amplitudes, cut) for cut in CUTS)
    need(flags == (True, True, False),
         "nonreal-two-cut-positive-and-third-cut-negative")
    stats["complex_phase_integer_relations"] = len(rows)
    stats["nonreal_scaled_unitary_control_cuts"] = sum(flags)
    return rows, flags


def check_no_low_low_graphs(profiles, stats):
    ordinary_graphs = 0
    profile_pairs = 0
    for left in profiles:
        for right in profiles:
            tick()
            profile_pairs += 1
            row_options = tuple(
                tuple(combinations(
                    tuple(b for b in range(5)
                          if not (left[a] == 2 and right[b] == 2)),
                    left[a],
                ))
                for a in range(5)
            )
            valid = []
            for rows in product(*row_options):
                degrees = [0] * 5
                for row in rows:
                    for b in row:
                        degrees[b] += 1
                if tuple(degrees) == right:
                    valid.append(frozenset(
                        (a, b) for a, row in enumerate(rows) for b in row
                    ))
            ordinary = max(left) == 3 and max(right) == 3
            need(bool(valid) == ordinary, "no-low-low-profile-feasibility")
            if ordinary:
                expected = frozenset(
                    (a, b) for a in range(5) for b in range(5)
                    if (left[a] == 2) != (right[b] == 2)
                )
                need(valid == [expected], "ordinary-graph-forced-cross-status")
                ordinary_graphs += 1
    zero_twin_statuses = tuple(
        status for status in product((0, 1), repeat=4)
        if all(status[i] != status[j] for i, j in PAIRS)
    )
    need(not zero_twin_statuses, "zero-twin-four-status-obstruction")
    required_words = 3 * (2 * 2)
    capacities = tuple(product(range(3), repeat=4))
    need(required_words == 12, "one-twin-low-word-count")
    need(max(map(sum, capacities)) == 8, "one-twin-pair-capacity")
    need(all(sum(values) < required_words for values in capacities),
         "one-twin-capacity-contradiction")
    stats["no_low_low_ordered_profile_pairs"] = profile_pairs
    stats["ordinary_no_low_low_graphs"] = ordinary_graphs
    stats["one_twin_pair_occupancy_vectors"] = len(capacities)


def remap_word(word, coordinate_order):
    result = [None] * 4
    for source, target in enumerate(coordinate_order):
        result[target] = word[source]
    return tuple(result)


def check_component_alphabets_and_common_p(stats):
    alphabet = frozenset(range(5))
    subsets = tuple(frozenset(values)
                    for values in combinations(range(5), 3))
    choices = tuple(
        (a, b) for a, b in product(subsets, repeat=2)
        if a | b == alphabet and len(a & b) == 1
    )
    need(len(choices) == 30, "ordered-component-alphabet-pair-count")
    base_cases = 0
    physical_cases = 0
    forced_word_labels = 0
    first_words = None
    for (ki, kj), (li, lj) in product(choices, repeat=2):
        tick()
        base_cases += 1
        for bi, bj in ((ki, kj), (li, lj)):
            degrees = tuple(
                2 * (int(value in bi) + int(value in bj))
                for value in range(5)
            )
            need(tuple(sorted(degrees)) == (2, 2, 2, 2, 4),
                 "two-components-force-exceptional-party")
        forced = []
        for a, b in product((0, 1), repeat=2):
            allowed = tuple(
                (a, b, c, d)
                for c, d in product(range(6), repeat=2)
                if c not in ki and c not in kj and
                d not in li and d not in lj
            )
            need(allowed == ((a, b, 5, 5),),
                 "same-P-forced-outside-completion")
            forced.append(allowed[0])
        forced = tuple(forced)
        if first_words is None:
            first_words = forced
        for twins in PAIRS:
            remaining = tuple(i for i in range(4) if i not in twins)
            coordinate_order = twins + remaining
            words = tuple(remap_word(word, coordinate_order)
                          for word in forced)
            require_bound_claims(words, actual_claims(words))
            counters = pair_counters(words)
            need(len(counters[twins]) == 4,
                 "four-distinct-maximal-high-pair-labels")
            need(counters[remaining] == Counter({(5, 5): 4}),
                 "same-complementary-outside-pair-collision")
            need(all(pair in counters for pair in PAIRS),
                 "missing-physical-pair-consumer")
            physical_cases += 1
            forced_word_labels += len(words)
    need(base_cases == 900, "two-remaining-coordinate-alphabet-count")
    need(physical_cases == 5400, "all-physical-twin-role-count")
    stats["ordered_component_alphabet_pairs"] = len(choices)
    stats["two_coordinate_alphabet_configurations"] = base_cases
    stats["physical_twin_role_configurations"] = physical_cases
    stats["forced_local_maximal_word_labels"] = forced_word_labels
    return first_words


def require_disjoint_components(left, right):
    need(not (set(left) & set(right)), "component-overlap")


def expect_rejection(results, name, reason, operation):
    try:
        operation()
    except CheckFailure as failure:
        need(failure.reason == reason,
             "wrong-control-reason:" + name + ":" + failure.reason)
        results.append(name)
        return
    raise CheckFailure("control-not-rejected:" + name)


def check_negative_controls(triples, pool, rows, flags, forced_words):
    results = []
    expect_rejection(
        results, "reused-colour-edge", "matching-edge-repeat",
        lambda: require_colours((pool[0], pool[0], pool[0]), 6),
    )
    expect_rejection(
        results, "six-triple-slice-pretends-eight", "slice-duplicate",
        lambda: require_slice(
            triples + ((3, 3, 3), (3, 3, 3)), 4
        ),
    )
    expect_rejection(
        results, "eight-overlap-two-degree-four-symbols", "two-degree4-slices",
        lambda: require_distinct_slice_demands((4, 2, 2, 2, 2), (4, 4)),
    )
    expect_rejection(
        results, "F2-only-real-sign-certificate", "integer-exponents",
        lambda: require_integer_certificate(rows, (1, 1, 1)),
    )
    expect_rejection(
        results, "drop-third-physical-cut", "missing-physical-cut",
        lambda: require_all_physical_cuts(flags),
    )
    left = place_component(triples, 0)
    right = place_component(triples, 1)
    need(bool(set(left) & set(right)), "overlap-control-not-overlapping")
    expect_rejection(
        results, "allow-overlapping-local-components", "component-overlap",
        lambda: require_disjoint_components(left, right),
    )
    claims = actual_claims(forced_words)
    require_bound_claims(forced_words, claims)
    independent_claims = dict(claims)
    independent_claims[(2, 3)] = tuple(product((0, 1), repeat=2))
    need(len(set(independent_claims[(2, 3)])) == 4,
         "independent-projection-control-not-injective")
    expect_rejection(
        results, "independent-P-per-cut-evasion", "same-word-projection",
        lambda: require_bound_claims(forced_words, independent_claims),
    )
    expect_rejection(
        results, "drop-maximal-pair-injectivity", "maximal-pair-collision",
        lambda: require_injective_pair(forced_words, (2, 3)),
    )
    need(len(results) == 8, "intended-reason-control-count")
    return tuple(results)


def main():
    global DEADLINE
    started = monotonic()
    DEADLINE = started + 55.0
    need(len(sys.argv) == 1, "unexpected-command-line-arguments")
    stats = {}
    profiles = check_degrees_and_moments(stats)
    triples, pool = check_common_twins(profiles, stats)
    check_low_slices(stats)
    rows, flags = check_complex_phases(stats)
    check_no_low_low_graphs(profiles, stats)
    forced_words = check_component_alphabets_and_common_p(stats)
    controls = check_negative_controls(
        triples, pool, rows, flags, forced_words
    )
    tick()
    print("RESULT: PASS_EXACT_LOCAL_INTERFACES_ONLY")
    for key in sorted(stats):
        print(key + " = " + str(stats[key]))
    print("intended_reason_controls = " + str(len(controls)))
    for name in controls:
        print("CONTROL_REJECTED_FOR_INTENDED_REASON: " + name)
    print("NOT_AN_AME_CERTIFICATE: no complete global E/P/U was constructed")
    print("NOT_TESTED: actual global tensor mutants for these controls")
    print("NOT_ENUMERATED: global supports, continuous moduli or phases")
    print("COMPLEX_SCOPE: integer exponent identity plus written normalization")
    print("SAME_P_SCOPE: four forced words only, not a full maximal support")
    print("NO_CLAIM: other profiles, all t24, all support48, minimum or novelty")
    print("elapsed_seconds = " + format(monotonic() - started, ".6f"))
    return 0


if __name__ == "__main__":
    try:
        status = main()
    except CheckFailure as failure:
        print("RESULT: INCOMPLETE_OR_FAILED")
        print("reason = " + failure.reason)
        status = 1
    sys.exit(status)

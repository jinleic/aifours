from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from time import monotonic


CUTS = ((0, 1), (0, 2), (0, 3))
PAIR_AXES = tuple(combinations(range(4), 2))
BINARY4 = tuple(product((0, 1), repeat=4))
DEADLINE = None


class CheckError(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)


def need(condition, reason):
    if not condition:
        raise CheckError(reason)


def tick():
    need(DEADLINE is not None, "DEADLINE_NOT_INITIALIZED")
    need(monotonic() <= DEADLINE, "RUNTIME_BUDGET_EXCEEDED")


def unique_words(words):
    seq = tuple(tuple(w) for w in words)
    need(all(len(w) == 4 for w in seq), "WORD_ARITY")
    need(len(set(seq)) == len(seq), "DUPLICATE_TENSOR_WORD")
    return seq


def pair_counters(words):
    seq = unique_words(words)
    return {
        ij: Counter((w[ij[0]], w[ij[1]]) for w in seq)
        for ij in PAIR_AXES
    }


def check_partial_pairs(words):
    counters = pair_counters(words)
    for counter in counters.values():
        need(all(n <= 2 for n in counter.values()), "PAIR_MULTIPLICITY")
    return counters


def check_exact_pairs(words, expected_pair_count):
    counters = pair_counters(words)
    for counter in counters.values():
        need(all(n == 2 for n in counter.values()), "PAIR_MULTIPLICITY")
        need(len(counter) == expected_pair_count, "PAIR_PROJECTION_SIZE")
    return counters


def right_axes(left):
    return tuple(i for i in range(4) if i not in left)


def split_word(word, left):
    right = right_axes(left)
    return (
        tuple(word[i] for i in left),
        tuple(word[i] for i in right),
    )


def merge_word(row, column, left):
    right = right_axes(left)
    result = [None] * 4
    for i, value in zip(left, row):
        result[i] = value
    for i, value in zip(right, column):
        result[i] = value
    need(all(value is not None for value in result), "MERGE_ARITY")
    return tuple(result)


def adjacency(words, left):
    rows = {}
    columns = {}
    for word in unique_words(words):
        row, column = split_word(word, left)
        rows.setdefault(row, set()).add(column)
        columns.setdefault(column, set()).add(row)
    return rows, columns


def close_rectangles(seed):
    support = set(unique_words(seed))
    while True:
        tick()
        check_partial_pairs(support)
        additions = set()
        for left in CUTS:
            rows, columns = adjacency(support, left)
            for row, neighbors in rows.items():
                if len(neighbors) != 2:
                    continue
                c0, c1 = sorted(neighbors)
                for other_row in columns[c0] - {row}:
                    additions.add(merge_word(other_row, c1, left))
                for other_row in columns[c1] - {row}:
                    additions.add(merge_word(other_row, c0, left))
        additions -= support
        if not additions:
            break
        need(all(word in BINARY4 for word in additions), "BINARY_BOX_ESCAPE")
        support.update(additions)
        need(len(support) <= 16, "BINARY_BOX_SIZE")
    check_partial_pairs(support)
    return frozenset(support)


def closed_blocks(words, left):
    rows, columns = adjacency(words, left)
    need(all(len(v) == 2 for v in rows.values()), "BLOCK_ROW_DEGREE")
    need(all(len(v) == 2 for v in columns.values()), "BLOCK_COLUMN_DEGREE")
    blocks = set()
    for row in sorted(rows):
        c0, c1 = sorted(rows[row])
        block_rows = tuple(sorted(columns[c0]))
        need(columns[c1] == set(block_rows), "BLOCK_RECTANGLE_CLOSURE")
        need(len(block_rows) == 2, "BLOCK_ROW_COUNT")
        r0, r1 = block_rows
        need(rows[r0] == {c0, c1}, "BLOCK_RECTANGLE_CLOSURE")
        need(rows[r1] == {c0, c1}, "BLOCK_RECTANGLE_CLOSURE")
        blocks.add((
            merge_word(r0, c0, left),
            merge_word(r0, c1, left),
            merge_word(r1, c0, left),
            merge_word(r1, c1, left),
        ))
    return tuple(sorted(blocks))


def partition_id(labels):
    need(len(labels) == 4, "PARTITION_ARITY")
    need(Counter(labels) == Counter({0: 2, 1: 2}), "PARTITION_BALANCE")
    blocks = (
        tuple(i for i, value in enumerate(labels) if value == 0),
        tuple(i for i, value in enumerate(labels) if value == 1),
    )
    return tuple(sorted(blocks))


def slice_kind(words):
    seq = tuple(sorted(words))
    need(len(seq) == 4 and len(set(seq)) == 4, "SLICE_WORD_COUNT")
    need(all(len(word) == 3 for word in seq), "SLICE_ARITY")
    need(all(value in (0, 1) for word in seq for value in word),
         "SLICE_BINARY_NORMALIZATION")
    ids = []
    for axis in range(3):
        labels = tuple(word[axis] for word in seq)
        ids.append(partition_id(labels))
    if len(set(ids)) == 3:
        return "A"
    need(len(set(ids)) == 2, "DUPLICATE_SLICE_WORD")
    if ids[0] == ids[1]:
        return "E01"
    if ids[0] == ids[2]:
        return "E02"
    return "E12"


def check_low_slice(words, declared_degree=2):
    need(declared_degree == 2, "LOW_DEGREE_TWO_REQUIRED")
    seq = tuple(words)
    need(len(seq) == 2 * declared_degree, "LOW_SLICE_WORD_MULTIPLICITY")
    need(len(set(seq)) == len(seq), "DUPLICATE_SLICE_WORD")
    return slice_kind(seq)


def enumerate_balanced_slices():
    oriented = []
    for zero_positions in combinations(range(4), 2):
        zeros = set(zero_positions)
        oriented.append(tuple(0 if i in zeros else 1 for i in range(4)))
    need(len(oriented) == 6, "ORIENTED_PARTITION_COUNT")
    need(len({partition_id(v) for v in oriented}) == 3,
         "UNORIENTED_PARTITION_COUNT")
    counts = Counter()
    supports = set()
    for labels in product(oriented, repeat=3):
        tick()
        words = tuple(zip(*labels))
        if len(set(words)) != 4:
            counts["DUPLICATE"] += 1
            continue
        kind = check_low_slice(words)
        counts[kind] += 1
        supports.add(frozenset(words))
    expected = Counter({
        "DUPLICATE": 24,
        "A": 48,
        "E01": 48,
        "E02": 48,
        "E12": 48,
    })
    need(counts == expected, "BALANCED_SLICE_CLASSIFICATION")
    need(sum(counts.values()) == 216, "BALANCED_SLICE_EXHAUSTIVENESS")
    need(len(supports) == 8, "BALANCED_SUPPORT_COUNT")
    normalized = tuple(
        sorted(
            (s for s in supports if (0, 0, 0) in s and (1, 1, 0) in s),
            key=lambda s: tuple(sorted(s)),
        )
    )
    need(len(normalized) == 2, "NORMALIZED_LL_SLICE_COUNT")
    need({slice_kind(s) for s in normalized} == {"A", "E01"},
         "NORMALIZED_LL_SLICE_TYPES")
    return counts, normalized


def canonical_edges(n, edges):
    raw = tuple(tuple(edge) for edge in edges)
    need(all(len(edge) == 2 for edge in raw), "GRAPH_EDGE_ARITY")
    need(all(
        isinstance(a, int) and isinstance(b, int)
        and 0 <= a < n and 0 <= b < n and a != b
        for a, b in raw
    ), "GRAPH_EDGE_RANGE")
    normalized = tuple(sorted((min(a, b), max(a, b)) for a, b in raw))
    need(len(set(normalized)) == len(normalized), "GRAPH_DUPLICATE_EDGE")
    return normalized


def check_simple_cubic(n, edges):
    need(n > 0, "GRAPH_NONEMPTY")
    normalized = canonical_edges(n, edges)
    degrees = [0] * n
    for a, b in normalized:
        degrees[a] += 1
        degrees[b] += 1
    need(all(d == 3 for d in degrees), "TWIN_CUBIC_DEGREE")
    return frozenset(normalized)


def graph_coloring(n, edges):
    adjacent = [set() for _ in range(n)]
    for a, b in edges:
        adjacent[a].add(b)
        adjacent[b].add(a)
    color = {}
    for start in range(n):
        if start in color:
            continue
        color[start] = 0
        stack = [start]
        while stack:
            vertex = stack.pop()
            for other in adjacent[vertex]:
                wanted = 1 - color[vertex]
                if other in color:
                    if color[other] != wanted:
                        return None
                else:
                    color[other] = wanted
                    stack.append(other)
    return color


def check_twin_graph(n, edges):
    graph = check_simple_cubic(n, edges)
    color = graph_coloring(n, graph)
    need(color is not None, "TWIN_ODD_CYCLE_NONZERO_Z")
    return graph, color


def perfect_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return ((),)
    if len(vertices) % 2:
        return ()
    first = vertices[0]
    result = []
    for other in vertices[1:]:
        rest = tuple(v for v in vertices if v not in (first, other))
        for matching in perfect_matchings(rest):
            edge = (min(first, other), max(first, other))
            result.append(tuple(sorted((edge,) + matching)))
    return tuple(sorted(set(result)))


def check_three_matchings(n, triple):
    need(n > 0 and n % 2 == 0, "MATCHING_ORDER")
    need(len(triple) == 3, "MATCHING_COLOR_COUNT")
    all_edges = []
    for matching in triple:
        normalized = canonical_edges(n, matching)
        need(len(normalized) == n // 2, "MATCHING_EDGE_COUNT")
        degrees = [0] * n
        for a, b in normalized:
            degrees[a] += 1
            degrees[b] += 1
        need(all(d == 1 for d in degrees), "MATCHING_NOT_PERFECT")
        all_edges.extend(normalized)
    need(len(set(all_edges)) == len(all_edges),
         "TWIN_MATCHING_EDGE_DUPLICATE")
    return check_simple_cubic(n, all_edges)


def enumerate_graphs():
    cubic = {}
    bipartite = {}
    factor_counts = {}
    good_triple = None
    for n in range(1, 7):
        tick()
        cubic[n] = set()
        bipartite[n] = set()
        factor_counts[n] = Counter()
        if n >= 4 and n % 2 == 0:
            possible_edges = tuple(combinations(range(n), 2))
            for edges in combinations(possible_edges, 3 * n // 2):
                tick()
                degrees = [0] * n
                for a, b in edges:
                    degrees[a] += 1
                    degrees[b] += 1
                if any(d != 3 for d in degrees):
                    continue
                graph = frozenset(edges)
                cubic[n].add(graph)
                if graph_coloring(n, graph) is not None:
                    bipartite[n].add(graph)

        reconstructed = set()
        reconstructed_bipartite = set()
        matchings = perfect_matchings(tuple(range(n)))
        for triple in combinations(matchings, 3):
            tick()
            flattened = tuple(edge for matching in triple for edge in matching)
            if len(set(flattened)) != len(flattened):
                continue
            graph = check_three_matchings(n, triple)
            reconstructed.add(graph)
            factor_counts[n][graph] += 1
            if graph_coloring(n, graph) is not None:
                reconstructed_bipartite.add(graph)
                if good_triple is None:
                    good_triple = (n, triple)

        need(reconstructed == cubic[n], "GRAPH_MATCHING_RECONSTRUCTION")
        need(reconstructed_bipartite == bipartite[n],
             "BIPARTITE_MATCHING_RECONSTRUCTION")

    cubic_counts = tuple(len(cubic[n]) for n in range(1, 7))
    bipartite_counts = tuple(len(bipartite[n]) for n in range(1, 7))
    need(cubic_counts == (0, 0, 0, 1, 0, 70), "CUBIC_GRAPH_COUNTS")
    need(bipartite_counts == (0, 0, 0, 0, 0, 10),
         "BIPARTITE_GRAPH_COUNTS")
    minimum_order = min(n for n in range(1, 7) if bipartite[n])
    need(minimum_order == 6, "TWIN_MINIMUM_ORDER")

    unordered_factorizations = 0
    for graph in bipartite[6]:
        checked_graph, color = check_twin_graph(6, graph)
        part0 = {v for v in range(6) if color[v] == 0}
        part1 = set(range(6)) - part0
        need(len(part0) == len(part1) == 3, "K33_PART_SIZES")
        complete = frozenset(
            (min(a, b), max(a, b)) for a in part0 for b in part1
        )
        need(checked_graph == complete, "K33_COMPLETENESS")
        need(factor_counts[6][graph] == 2, "K33_FACTORIZATION_COUNT")
        unordered_factorizations += factor_counts[6][graph]

    need(unordered_factorizations == 20, "LABELED_FACTORIZATION_COUNT")
    need(6 * unordered_factorizations == 120, "ORDERED_FACTORIZATION_COUNT")
    need(good_triple is not None and good_triple[0] == 6,
         "MISSING_POSITIVE_MATCHING_FIXTURE")
    return {
        "minimum_order": minimum_order,
        "cubic": cubic,
        "bipartite": bipartite,
        "cubic_counts": cubic_counts,
        "bipartite_counts": bipartite_counts,
        "good_triple": good_triple,
    }


def check_regular_r12(r12):
    r12 = set(r12)
    need(r12 <= set(product(range(4), repeat=2)), "R12_RANGE")
    need(len(r12) == 12, "R12_PAIR_COUNT")
    row_neighbors = tuple(
        frozenset(b for a0, b in r12 if a0 == a) for a in range(4)
    )
    column_neighbors = tuple(
        frozenset(a for a, b0 in r12 if b0 == b) for b in range(4)
    )
    need(all(len(s) == 3 for s in row_neighbors), "R12_ROW_DEGREE")
    need(all(len(s) == 3 for s in column_neighbors), "R12_COLUMN_DEGREE")
    need(len(set(row_neighbors)) == 4, "REGULAR_ROW_TWIN")
    need(len(set(column_neighbors)) == 4, "REGULAR_COLUMN_TWIN")
    return row_neighbors, column_neighbors


def enumerate_regular_r12():
    universe = set(product(range(4), repeat=2))
    count = 0
    for permutation in permutations(range(4)):
        tick()
        missing = {(a, permutation[a]) for a in range(4)}
        check_regular_r12(universe - missing)
        count += 1
    need(count == 24, "REGULAR_M12_MATCHING_COUNT")
    return count


def check_derived_low_twin_exclusion(words, graph_result):
    need(graph_result["minimum_order"] == 6, "LOW_TWIN_GRAPH_CERTIFICATE")
    need(all(
        not graph_result["bipartite"][n] for n in range(1, 5)
    ), "LOW_TWIN_SMALL_GRAPH_CERTIFICATE")
    seq = unique_words(words)
    for first, second in combinations(seq, 2):
        differences = tuple(i for i in range(4) if first[i] != second[i])
        if len(differences) != 1:
            continue
        axis = differences[0]
        if axis in (2, 3) and 0 in (first[axis], second[axis]):
            raise CheckError("LOW_TWIN_NONZERO_CUBIC_BOUND")


def embed_low_slice(words, fixed_axis):
    need(fixed_axis in (2, 3), "LOW_SLICE_FIXED_AXIS")
    free = tuple(i for i in range(4) if i != fixed_axis)
    result = []
    for word in words:
        full = [None] * 4
        full[fixed_axis] = 0
        for axis, value in zip(free, word):
            full[axis] = value
        result.append(tuple(full))
    return frozenset(result)


def enumerate_ll_pairs(normalized_slices, graph_result):
    outcomes = Counter()
    surviving_supports = set()
    for first, second in product(normalized_slices, repeat=2):
        tick()
        first_full = embed_low_slice(first, 2)
        second_full = embed_low_slice(second, 3)
        seed = first_full | second_full
        need(first_full & second_full == {(0, 0, 0, 0), (1, 1, 0, 0)},
             "LL_SHARED_EDGE_NORMALIZATION")
        try:
            check_partial_pairs(seed)
            check_derived_low_twin_exclusion(seed, graph_result)
            support = close_rectangles(seed)
            need({w for w in support if w[2] == 0} == set(first_full),
                 "LOW_SLICE_CLOSURE_INCONSISTENT")
            need({w for w in support if w[3] == 0} == set(second_full),
                 "LOW_SLICE_CLOSURE_INCONSISTENT")
            check_exact_pairs(support, 4)
            for left in CUTS:
                need(len(closed_blocks(support, left)) == 2,
                     "PARITY_BLOCK_COUNT")
            surviving_supports.add(support)
            outcomes["SURVIVES"] += 1
        except CheckError as error:
            if error.reason not in {
                "PAIR_MULTIPLICITY",
                "LOW_TWIN_NONZERO_CUBIC_BOUND",
            }:
                raise
            outcomes[error.reason] += 1

    need(outcomes == Counter({
        "SURVIVES": 1,
        "PAIR_MULTIPLICITY": 1,
        "LOW_TWIN_NONZERO_CUBIC_BOUND": 2,
    }), "LL_PAIR_CLASSIFICATION")
    parity = frozenset(w for w in BINARY4 if sum(w) % 2 == 0)
    need(surviving_supports == {parity}, "FORCED_PARITY_SUPPORT")
    return parity, outcomes


def check_nonzero_squared_moduli(words, squared_moduli):
    seq = unique_words(words)
    values = tuple(squared_moduli)
    need(len(values) == len(seq), "MODULUS_COUNT")
    need(all(isinstance(q, Fraction) for q in values), "MODULUS_NOT_RATIONAL")
    need(all(q > 0 for q in values), "NONZERO_AMPLITUDE_REQUIRED")


def phase_rows(words, cuts):
    ordered_words = tuple(sorted(unique_words(words)))
    index = {word: i for i, word in enumerate(ordered_words)}
    labelled_rows = []
    for left in cuts:
        for block in closed_blocks(ordered_words, left):
            coefficients = [0] * len(ordered_words)
            for word, sign in zip(block, (1, -1, -1, 1)):
                coefficients[index[word]] += sign
            labelled_rows.append((left, tuple(coefficients)))
    return ordered_words, tuple(labelled_rows)


def full_phase_rows(words, cuts):
    need(len(cuts) == 3 and set(cuts) == set(CUTS),
         "THREE_CUT_PHASE_COVERAGE")
    return phase_rows(words, cuts)


def require_phase_certificate(rows, rhs, coefficients):
    need(len(rows) == len(rhs) == len(coefficients),
         "PHASE_CERTIFICATE_ARITY")
    need(all(isinstance(c, int) for c in coefficients),
         "PHASE_CERTIFICATE_NONINTEGER_WEIGHT")
    need(all(isinstance(b, int) for b in rhs), "PHASE_NONINTEGER_RHS")
    width = len(rows[0])
    need(all(len(row) == width for row in rows), "PHASE_ROW_ARITY")
    for column in range(width):
        value = sum(
            Fraction(c) * row[column]
            for c, row in zip(coefficients, rows)
        )
        need(value == 0, "PHASE_CERTIFICATE_NONZERO_LEFT")
    combined_rhs = sum(c * b for c, b in zip(coefficients, rhs))
    need(combined_rhs % 2 == 1, "PHASE_RHS_NOT_ODD")
    return combined_rhs


def find_odd_integer_relation(rows, rhs):
    for coefficients in product((-1, 0, 1), repeat=len(rows)):
        tick()
        if not any(coefficients):
            continue
        if sum(c * b for c, b in zip(coefficients, rhs)) % 2 != 1:
            continue
        if all(
            sum(c * row[j] for c, row in zip(coefficients, rows)) == 0
            for j in range(len(rows[0]))
        ):
            require_phase_certificate(rows, rhs, coefficients)
            return coefficients
    raise CheckError("PHASE_INTEGER_RELATION_NOT_FOUND")


def sign_witness(rows, rhs):
    for bits in product((0, 1), repeat=len(rows[0])):
        tick()
        if all(
            sum(a * b for a, b in zip(row, bits)) % 2 == target % 2
            for row, target in zip(rows, rhs)
        ):
            return bits
    return None


def check_real_sign_blocks(words, cuts, bits):
    ordered_words = tuple(sorted(words))
    need(len(bits) == len(ordered_words), "SIGN_VECTOR_ARITY")
    signs = {
        word: (-1 if bit else 1)
        for word, bit in zip(ordered_words, bits)
    }
    for left in cuts:
        for block in closed_blocks(ordered_words, left):
            u, v, w, x = tuple(signs[word] for word in block)
            need(u * w + v * x == 0, "REAL_BLOCK_ROW_ORTHOGONALITY")
            need(u * v + w * x == 0, "REAL_BLOCK_COLUMN_ORTHOGONALITY")
            need(Fraction(u * u + v * v, 2) == 1, "REAL_BLOCK_ROW_NORM")
            need(Fraction(w * w + x * x, 2) == 1, "REAL_BLOCK_ROW_NORM")
            need(Fraction(u * u + w * w, 2) == 1, "REAL_BLOCK_COLUMN_NORM")
            need(Fraction(v * v + x * x, 2) == 1, "REAL_BLOCK_COLUMN_NORM")


def check_phase_interface(parity):
    ordered, labelled = full_phase_rows(parity, CUTS)
    need(len(ordered) == 8 and len(labelled) == 6, "PHASE_MATRIX_SIZE")
    rows = tuple(row for _, row in labelled)
    rhs = (1,) * len(rows)
    check_nonzero_squared_moduli(ordered, (Fraction(1, 2),) * len(ordered))
    certificate = find_odd_integer_relation(rows, rhs)
    require_phase_certificate(rows, rhs, certificate)

    position = {word: i for i, word in enumerate(ordered)}

    def difference_of_pairs(positive, negative):
        row = [0] * len(ordered)
        for word in positive:
            row[position[word]] += 1
        for word in negative:
            row[position[word]] -= 1
        return tuple(row)

    X = ((0, 0, 0, 0), (1, 1, 1, 1))
    Y = ((0, 0, 1, 1), (1, 1, 0, 0))
    Z = ((0, 1, 0, 1), (1, 0, 1, 0))
    named = (
        difference_of_pairs(X, Y),
        difference_of_pairs(X, Z),
        difference_of_pairs(Y, Z),
    )
    indices = tuple(rows.index(row) for row in named)
    need({labelled[i][0] for i in indices} == set(CUTS),
         "NAMED_PHASE_RELATIONS_THREE_CUTS")
    named_certificate = [0] * len(rows)
    for index, multiplier in zip(indices, (1, -1, 1)):
        named_certificate[index] += multiplier
    need(require_phase_certificate(rows, rhs, named_certificate) == 1,
         "NAMED_PHASE_CERTIFICATE_RHS")

    need(sign_witness(rows, rhs) is None, "ALL_CUT_SIGN_DIAGNOSTIC")
    omitted_cut_witnesses = []
    for omitted in CUTS:
        selected = tuple(left for left in CUTS if left != omitted)
        selected_words, selected_labelled = phase_rows(parity, selected)
        need(selected_words == ordered, "PHASE_WORD_ORDER_DRIFT")
        selected_rows = tuple(row for _, row in selected_labelled)
        witness = sign_witness(selected_rows, (1,) * len(selected_rows))
        need(witness is not None, "TWO_CUT_POSITIVE_CONTROL")
        check_real_sign_blocks(parity, selected, witness)
        omitted_cut_witnesses.append((omitted, witness))

    return {
        "ordered_words": ordered,
        "labelled_rows": labelled,
        "rows": rows,
        "rhs": rhs,
        "certificate": certificate,
        "named_certificate": tuple(named_certificate),
        "omitted_cut_witnesses": tuple(omitted_cut_witnesses),
    }


def local_count_conditions(x, u):
    return (
        len(x) == len(u) == 4
        and all(1 <= value <= 2 for value in x)
        and all(0 <= value <= 2 for value in u)
        and x == u
    )


def check_count_vectors(x, u):
    x, u = tuple(x), tuple(u)
    need(local_count_conditions(x, u), "COUNT_LOCAL_CONDITIONS")
    need(sum(x) == 6 and sum(u) == 6, "COUNT_GLOBAL_SUM")


def row_degrees(columns):
    return tuple(sum(a in column for column in columns) for a in range(4))


def enumerate_count_interfaces():
    raw = 0
    local = set()
    global_valid = set()
    for x in product(range(4), repeat=4):
        for u in product(range(3), repeat=4):
            tick()
            raw += 1
            if local_count_conditions(x, u):
                local.add((x, u))
                if sum(x) == 6 and sum(u) == 6:
                    check_count_vectors(x, u)
                    global_valid.add((x, u))
    need(raw == 20736, "COUNT_RAW_SPACE")
    need(len(local) == 16, "COUNT_LOCAL_SPACE")
    need(len(global_valid) == 6, "COUNT_GLOBAL_SPACE")

    low_column_options = tuple(
        frozenset(s) for s in combinations(range(4), 2)
    )
    high_column_options = tuple(
        frozenset(s) for s in combinations(range(4), 3)
    )
    low_all = tuple(product(low_column_options, repeat=3))
    high_all = tuple(product(high_column_options, repeat=2))
    need(len(low_all) == 216 and len(high_all) == 16,
         "INCIDENCE_RAW_COUNTS")

    low_valid = tuple(
        columns for columns in low_all
        if all(1 <= d <= 2 for d in row_degrees(columns))
    )
    high_valid = tuple(
        columns for columns in high_all
        if all(1 <= d <= 2 for d in row_degrees(columns))
    )
    need(len(low_valid) == 90, "LOW_INCIDENCE_BOUND_COUNT")
    need(len(high_valid) == 12, "HIGH_INCIDENCE_BOUND_COUNT")

    identical_high = tuple(
        columns for columns in high_all if columns[0] == columns[1]
    )
    need(len(identical_high) == 4, "TYPE_D_HIGH_NEIGHBOR_COUNT")
    for columns in identical_high:
        need(0 in row_degrees(columns), "TYPE_D_LOWER_BOUND_CONTRADICTION")

    joint = 0
    all_type_a = 0
    for low_columns in low_valid:
        for high_columns in high_valid:
            tick()
            x = row_degrees(low_columns)
            u = row_degrees(high_columns)
            if x != u:
                continue
            check_count_vectors(x, u)
            joint += 1
            propagation = all(
                a in high_columns[0] and a in high_columns[1]
                for column in low_columns
                for a in column
            )
            if propagation:
                all_type_a += 1
    need(joint == 180, "JOINT_NECESSARY_INCIDENCE_COUNT")
    need(all_type_a == 0, "ALL_TYPE_A_COUNT_CONTRADICTION")
    return (
        raw, len(local), len(global_valid),
        len(low_all), len(low_valid),
        len(high_all), len(high_valid),
        len(identical_high), joint, all_type_a,
    )


def expect_rejection(name, intended_reason, operation):
    try:
        operation()
    except CheckError as error:
        need(error.reason == intended_reason,
             "MUTANT_WRONG_REASON:" + name + ":" + error.reason)
        return name, error.reason
    raise CheckError("MUTANT_ACCEPTED:" + name)


def run_mutants(parity, normalized_slices, graph_result, phase_result):
    ordered = tuple(sorted(parity))
    rows = phase_result["rows"]
    rhs = phase_result["rhs"]
    certificate = phase_result["certificate"]
    a_slice = next(s for s in normalized_slices if slice_kind(s) == "A")
    extra_word = next(w for w in BINARY4 if w not in parity)
    squared_moduli = [Fraction(1, 2)] * len(ordered)
    squared_moduli[0] = Fraction(0)

    universe12 = set(product(range(4), repeat=2))
    bad_missing = {(0, 0), (1, 0), (2, 2), (3, 3)}
    bad_r12 = universe12 - bad_missing
    k4 = next(iter(graph_result["cubic"][4]))
    matching_order, good_triple = graph_result["good_triple"]
    repeated_triple = (good_triple[0], good_triple[0], good_triple[1])

    operations = (
        (
            "omit_one_physical_cut",
            "THREE_CUT_PHASE_COVERAGE",
            lambda: full_phase_rows(parity, CUTS[:2]),
        ),
        (
            "allow_zero_amplitude",
            "NONZERO_AMPLITUDE_REQUIRED",
            lambda: check_nonzero_squared_moduli(ordered, squared_moduli),
        ),
        (
            "duplicate_pair_extensions",
            "PAIR_MULTIPLICITY",
            lambda: check_exact_pairs(ordered + (extra_word,), 4),
        ),
        (
            "flip_low_degree_to_three",
            "LOW_DEGREE_TWO_REQUIRED",
            lambda: check_low_slice(a_slice, declared_degree=3),
        ),
        (
            "duplicate_missing_r12_neighbor",
            "R12_COLUMN_DEGREE",
            lambda: check_regular_r12(bad_r12),
        ),
        (
            "wrong_phase_rhs",
            "PHASE_RHS_NOT_ODD",
            lambda: require_phase_certificate(
                rows, (0,) * len(rhs), certificate
            ),
        ),
        (
            "local_only_count",
            "COUNT_GLOBAL_SUM",
            lambda: check_count_vectors((2, 2, 2, 2), (2, 2, 2, 2)),
        ),
        (
            "nonbipartite_cubic_nonzero_z",
            "TWIN_ODD_CYCLE_NONZERO_Z",
            lambda: check_twin_graph(4, k4),
        ),
        (
            "repeat_matching_color",
            "TWIN_MATCHING_EDGE_DUPLICATE",
            lambda: check_three_matchings(matching_order, repeated_triple),
        ),
        (
            "duplicate_tensor_word",
            "DUPLICATE_TENSOR_WORD",
            lambda: check_exact_pairs(ordered + (ordered[0],), 4),
        ),
    )
    results = []
    for name, reason, operation in operations:
        tick()
        results.append(expect_rejection(name, reason, operation))
    need(len(results) == 10, "MUTANT_COUNT")
    return tuple(results)


def main():
    global DEADLINE
    started = monotonic()
    DEADLINE = started + 50.0

    graph_result = enumerate_graphs()
    regular_matchings = enumerate_regular_r12()
    slice_counts, normalized_slices = enumerate_balanced_slices()
    parity, ll_outcomes = enumerate_ll_pairs(normalized_slices, graph_result)
    phase_result = check_phase_interface(parity)
    count_result = enumerate_count_interfaces()
    mutants = run_mutants(
        parity, normalized_slices, graph_result, phase_result
    )
    tick()

    print("FINITE_INTERFACE_CHECKS_PASS")
    print("SCOPE: bounded necessary interfaces and exact phase diagnostic only")
    print("NOT: actual AME witness, complete P/E, full4455 exclusion, global minimum")
    print("balanced_slice_counts", tuple(sorted(slice_counts.items())))
    print("normalized_low_slices", len(normalized_slices))
    print("ll_pair_outcomes", tuple(sorted(ll_outcomes.items())))
    print("forced_parity_support", tuple(sorted(parity)))
    print("physical_pair_multiplicities", tuple(
        (ij, tuple(sorted(counter.items())))
        for ij, counter in check_exact_pairs(parity, 4).items()
    ))
    print("blocks_per_cut", tuple(
        (left, len(closed_blocks(parity, left))) for left in CUTS
    ))
    print("simple_cubic_counts_n1_to_n6", graph_result["cubic_counts"])
    print("bipartite_counts_n1_to_n6", graph_result["bipartite_counts"])
    print("minimum_nonempty_cubic_bipartite_order",
          graph_result["minimum_order"])
    print("ordered_k33_factorizations", 120)
    print("regular_m12_matchings", regular_matchings)
    for index, (left, row) in enumerate(phase_result["labelled_rows"]):
        print("phase_row", index, left, row, "rhs_pi", 1)
    print("integer_phase_certificate", phase_result["certificate"])
    print("named_integer_phase_certificate", phase_result["named_certificate"])
    print("two_cut_sign_witnesses", phase_result["omitted_cut_witnesses"])
    print("count_interfaces", count_result)
    for name, reason in mutants:
        print("INTENDED_REJECTION", name, reason)
    print("elapsed_seconds", monotonic() - started)


if __name__ == "__main__":
    try:
        main()
    except CheckError as error:
        print("FINITE_INTERFACE_CHECK_FAILED", error.reason)
        raise SystemExit(1)


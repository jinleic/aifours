"""Independent f388 canonical finite audit. Standard library; no input files.

Run: python3 -B check_f388_independent_finite_v1.py
Also: python3 -O -B check_f388_independent_finite_v1.py

This source is NOTRUN in the authoring session. Its PASS line, if obtained,
concerns only the canonical finite checks, not the universal normal form.
Runtime effects: stdout only. No files, network, children, randomness or imports
of any supplied checker. The cooperative calculation deadline is 55 seconds.
"""

from collections import Counter, defaultdict
from itertools import combinations, product
from sys import argv
from time import monotonic

PARTIES = (1, 2, 3, 4)
INTERNAL = (1, 2, 3, 4)
OUTSIDE = (0, 5)  # o_0 and o_1, respectively
SYMBOLS = (0, 1, 2, 3, 4, 5)
PAIRS = tuple(combinations(PARTIES, 2))
BINARY_PAIRS = tuple(combinations(range(3), 2))
START = monotonic()

# Integer reason codes are part of the corruption-control contract.
DEADLINE = 1
BAD_ARGV = 2
BINARY_INPUT = 10
BINARY_PROJECTION = 11
BINARY_CLASSIFICATION = 12
PACKING_INPUT = 20
PACKING_PAIR_COLLISION = 21
COMMON_COMPLEMENT = 22
LOCAL_RESIDUAL_DEGREE = 23
CANONICAL_TABLE = 24
GAUGE = 25
RESIDUAL_PAIR = 30
FORCED_FIBER = 31
CANONICAL_WORDS = 32
RECTANGLE = 33
LOCAL_DEGREE = 40
SINGLE_INTERSECTION = 41
COMPLEX_UNITARY = 50
MISSING_REJECTION = 60
WRONG_REJECTION = 61


class AuditError(Exception):
    def __init__(self, reason, detail=()):
        self.reason = reason
        self.detail = detail
        super().__init__("reason={} detail={!r}".format(reason, detail))


def need(condition, reason, detail=()):
    if not condition:
        raise AuditError(reason, detail)


def tick():
    need(monotonic() - START < 55, DEADLINE)


def project(word, pair):
    return tuple(word[i - 1] for i in pair)


def epsilon(order):
    return sum(order[i] > order[j]
               for i in range(4) for j in range(i + 1, 4)) % 2


def check_binary(triples):
    need(len(triples) == 4 and len(set(triples)) == 4,
         BINARY_INPUT, (len(triples), len(set(triples))))
    need(all(len(t) == 3 and all(type(x) is int and x in (0, 1) for x in t)
             for t in triples), BINARY_INPUT)
    for i, j in BINARY_PAIRS:
        n = len({(t[i], t[j]) for t in triples})
        need(n == 4, BINARY_PROJECTION, (i, j, n))


def check_packing(words, pairs=PAIRS):
    need(len(words) == 24 and len(set(words)) == 24,
         PACKING_INPUT, (len(words), len(set(words))))
    need(all(len(w) == 4
             and all(type(x) is int and x in SYMBOLS for x in w)
             and sum(x in INTERNAL for x in w) == 2 for w in words),
         PACKING_INPUT)
    for i, j in pairs:
        counts = Counter(project(w, (i, j)) for w in words)
        for (a, b), n in sorted(counts.items()):
            need(n == 1, PACKING_PAIR_COLLISION, (i, j, a, b, n))


def residual_from_packing(words):
    universe = set(product(SYMBOLS, repeat=2))
    return {p: universe - {project(w, p) for w in words} for p in PAIRS}


def check_common_complements(words, residual):
    expected = residual_from_packing(words)
    for i, j in PAIRS:
        actual = residual[(i, j)]
        target = expected[(i, j)]
        if actual != target:
            a, b = min(actual ^ target)
            raise AuditError(COMMON_COMPLEMENT,
                             (i, j, a, b, int((a, b) in actual),
                              int((a, b) in target)))


def check_local_residual_degrees(residual):
    internal_pairs = set(product(INTERNAL, repeat=2))
    for i, j in PAIRS:
        values = residual[(i, j)]
        need(len(values) == 12 and values <= internal_pairs,
             LOCAL_RESIDUAL_DEGREE, (i, j, len(values)))
        for a in INTERNAL:
            degrees = (sum(x == a for x, y in values),
                       sum(y == a for x, y in values))
            need(degrees == (3, 3), LOCAL_RESIDUAL_DEGREE,
                 (i, j, a) + degrees)


def canonical_t():
    return {(i, a, k): int(a not in (i, k))
            for i in PARTIES for a in INTERNAL for k in PARTIES if k != i}


def parity_t(constants):
    # Lexicographic labels are deliberately unrelated to canonical labels.
    table = {}
    for i in PARTIES:
        coordinates = tuple(k for k in PARTIES if k != i)
        triples = tuple(t for t in product((0, 1), repeat=3)
                        if sum(t) % 2 == constants[i - 1])
        check_binary(triples)
        for a, triple in zip(INTERNAL, triples):
            for k, bit in zip(coordinates, triple):
                table[(i, a, k)] = bit
    return table


def packing_from_t(table):
    # Enumerate all internal labels and outside bits. Use both views of (7),
    # not the printed transposition formula and not the literal P table.
    words = []
    for i, j in PAIRS:
        k, l = tuple(p for p in PARTIES if p not in (i, j))
        local = []
        for a, b, bk, bl in product(INTERNAL, INTERNAL, (0, 1), (0, 1)):
            tests = (
                bk == (table[(i, a, k)] ^ epsilon((i, j, k, l))),
                bk == (table[(j, b, k)] ^ epsilon((j, i, k, l))),
                bl == (table[(i, a, l)] ^ epsilon((i, j, l, k))),
                bl == (table[(j, b, l)] ^ epsilon((j, i, l, k))),
            )
            if all(tests):
                word = [None] * 4
                word[i - 1], word[j - 1] = a, b
                word[k - 1], word[l - 1] = OUTSIDE[bk], OUTSIDE[bl]
                local.append(tuple(word))
        need(len(local) == 4, CANONICAL_TABLE, (i, j, len(local)))
        words.extend(local)
    return tuple(sorted(words))


# Independently transcribed permitted literal table, not generated by code.
P_LITERAL = (
    (1, 1, 0, 5), (2, 2, 5, 0), (3, 4, 0, 0), (4, 3, 5, 5),
    (1, 5, 1, 0), (3, 0, 3, 5), (2, 5, 4, 5), (4, 0, 2, 0),
    (1, 0, 5, 1), (4, 5, 0, 4), (2, 0, 0, 3), (3, 5, 5, 2),
    (0, 2, 2, 5), (5, 3, 3, 0), (0, 1, 4, 0), (5, 4, 1, 5),
    (5, 2, 0, 2), (0, 4, 5, 4), (5, 1, 5, 3), (0, 3, 0, 1),
    (0, 5, 3, 3), (5, 0, 4, 4), (0, 0, 1, 2), (5, 5, 2, 1),
)


def check_gauge(constants, target):
    table = parity_t(constants)
    packing = packing_from_t(table)
    check_packing(packing)
    check_local_residual_degrees(residual_from_packing(packing))
    total = sum(constants) % 2
    flips = tuple(c ^ total for c in constants)
    need(all((sum(flips[k - 1] for k in PARTIES if k != i) % 2)
             == constants[i - 1] for i in PARTIES), GAUGE)
    labels = {}
    canonical = canonical_t()
    for i in PARTIES:
        for a in INTERNAL:
            normalized = {k: table[(i, a, k)] ^ flips[k - 1]
                          for k in PARTIES if k != i}
            need(sum(normalized.values()) % 2 == 0, GAUGE, (i, a))
            matches = tuple(b for b in INTERNAL
                            if all(normalized[k] == canonical[(i, b, k)]
                                   for k in normalized))
            need(len(matches) == 1, GAUGE, (i, a, len(matches)))
            labels[(i, a)] = matches[0]
    # Equation (9) is unchanged for every candidate label pair, not merely
    # those label pairs already selected by the packing generator.
    for i, j in PAIRS:
        for a, b in product(INTERNAL, repeat=2):
            for k in PARTIES:
                if k not in (i, j):
                    before = table[(i, a, k)] ^ table[(j, b, k)]
                    after = ((table[(i, a, k)] ^ flips[k - 1])
                             ^ (table[(j, b, k)] ^ flips[k - 1]))
                    need(before == after, GAUGE, (i, j, a, b, k))
    normalized_words = []
    for word in packing:
        new = []
        for i, a in enumerate(word, 1):
            if a in INTERNAL:
                new.append(labels[(i, a)])
            else:
                new.append(OUTSIDE[OUTSIDE.index(a) ^ flips[i - 1]])
        normalized_words.append(tuple(new))
    need(tuple(sorted(normalized_words)) == target, GAUGE, constants)
    return flips


def check_residual_word(word, residual):
    need(len(word) == 4 and all(x in INTERNAL for x in word), PACKING_INPUT)
    for i, j in PAIRS:
        a, b = project(word, (i, j))
        need((a, b) in residual[(i, j)], RESIDUAL_PAIR, (i, j, a, b))


def check_residual_set(words, residual):
    for word in sorted(words):
        check_residual_word(word, residual)


def swap_identity(pair):
    word = list(PARTIES)
    i, j = pair
    word[i - 1], word[j - 1] = word[j - 1], word[i - 1]
    return tuple(word)


def classified_words():
    # A second construction: classify by number of fixed coordinates.
    words = {PARTIES}
    words.update(swap_identity(p) for p in PAIRS)
    for fixed in PARTIES:
        other = tuple(i for i in PARTIES if i != fixed)
        choices = tuple(tuple(a for a in INTERNAL if a not in (fixed, i))
                        for i in other)
        for values in product(*choices):
            word = list(PARTIES)
            for i, a in zip(other, values):
                word[i - 1] = a
            words.add(tuple(word))
    for center in PARTIES:
        for leaf in PARTIES:
            if leaf != center:
                word = [center] * 4
                word[center - 1] = leaf
                words.add(tuple(word))
    return words


def flat_edges(words):
    return {(project(w, (1, 2)), project(w, (3, 4))) for w in words}


def neighborhoods(edges):
    rows, columns = defaultdict(set), defaultdict(set)
    for r, c in edges:
        rows[r].add(c)
        columns[c].add(r)
    return rows, columns


def check_degree_two(edges):
    need(bool(edges), LOCAL_DEGREE)
    rows, columns = neighborhoods(edges)
    for key in sorted(rows):
        need(len(rows[key]) == 2, LOCAL_DEGREE, (0, key, len(rows[key])))
    for key in sorted(columns):
        need(len(columns[key]) == 2, LOCAL_DEGREE,
             (1, key, len(columns[key])))


def check_block_closure(edges):
    check_degree_two(edges)
    rows, columns = neighborhoods(edges)
    for r, s in combinations(sorted(rows), 2):
        common = rows[r] & rows[s]
        if len(common) == 1:
            raise AuditError(SINGLE_INTERSECTION, (r, s, min(common)))
    for r, s in combinations(sorted(columns), 2):
        common = columns[r] & columns[s]
        if len(common) == 1:
            raise AuditError(SINGLE_INTERSECTION, (r, s, min(common)))


def gaussian_product(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)


def gaussian_inner(row, other):
    terms = [gaussian_product(z, (w[0], -w[1]))
             for z, w in zip(row, other)]
    return (sum(z[0] for z in terms), sum(z[1] for z in terms))


def check_local_complex_unitary():
    # Exact Gaussian-integer numerators; the matrix has denominator 5.
    matrix = (((3, 0), (0, 4)), ((0, 4), (3, 0)))
    denominator_squared = 25
    for row in matrix:
        need(all(0 < a * a + b * b < denominator_squared for a, b in row),
             COMPLEX_UNITARY)
    for collection in (matrix, tuple(zip(*matrix))):
        for i, j in product(range(2), repeat=2):
            expected = (denominator_squared, 0) if i == j else (0, 0)
            actual = gaussian_inner(collection[i], collection[j])
            need(actual == expected, COMPLEX_UNITARY, (i, j) + actual)


def expect_rejection(name, action, reason, detail):
    try:
        action()
    except AuditError as error:
        need(error.reason == reason and error.detail == detail,
             WRONG_REJECTION, (reason, detail, error.reason, error.detail))
        print("CONTROL", name, "REJECT", error.reason, repr(error.detail))
        return
    raise AuditError(MISSING_REJECTION, (reason, detail))


def main():
    need(len(argv) == 1, BAD_ARGV, (len(argv) - 1,))
    triples = tuple(product((0, 1), repeat=3))
    accepted, examined = set(), 0
    for choice in combinations(triples, 4):
        tick()
        examined += 1
        try:
            check_binary(choice)
        except AuditError as error:
            need(error.reason == BINARY_PROJECTION, WRONG_REJECTION,
                 (error.reason, error.detail))
        else:
            accepted.add(frozenset(choice))
    parity_classes = {frozenset(t for t in triples if sum(t) % 2 == c)
                      for c in (0, 1)}
    need(examined == 70 and accepted == parity_classes,
         BINARY_CLASSIFICATION, (examined, len(accepted)))

    table = canonical_t()
    packing = packing_from_t(table)
    check_packing(packing)
    check_packing(P_LITERAL)
    need(set(packing) == set(P_LITERAL), CANONICAL_TABLE,
         (len(set(packing) ^ set(P_LITERAL)),))
    residual = residual_from_packing(packing)
    check_common_complements(P_LITERAL, residual)
    check_local_residual_degrees(residual)
    for i, j in PAIRS:
        k, l = tuple(p for p in PARTIES if p not in (i, j))
        expected_missing = {(a, l if a == k else k if a == l else a)
                            for a in INTERNAL}
        missing = set(product(INTERNAL, repeat=2)) - residual[(i, j)]
        need(missing == expected_missing, CANONICAL_TABLE, (i, j))
        print("MISSING_MATCHING", (i, j), tuple(sorted(missing)))

    flips = set()
    gauge_count = 0
    for constants in product((0, 1), repeat=4):
        tick()
        flips.add(check_gauge(constants, packing))
        gauge_count += 1
    need(gauge_count == 16 and len(flips) == 16, GAUGE,
         (gauge_count, len(flips)))

    compatible = set()
    residual_examined = 0
    for word in product(INTERNAL, repeat=4):
        tick()
        residual_examined += 1
        try:
            check_residual_word(word, residual)
        except AuditError as error:
            need(error.reason == RESIDUAL_PAIR, WRONG_REJECTION,
                 (error.reason, error.detail))
        else:
            compatible.add(word)
    histogram = Counter(sum(w[i - 1] == i for i in PARTIES) for w in compatible)
    need(residual_examined == 256 and len(compatible) == 51
         and dict(histogram) == {0: 12, 1: 32, 2: 6, 4: 1},
         CANONICAL_WORDS, (residual_examined, len(compatible),
                           tuple(sorted(histogram.items()))))
    need(compatible == classified_words(), CANONICAL_WORDS,
         (len(compatible ^ classified_words()),))

    identity = PARTIES
    forced = set()
    for i, j in PAIRS:
        complement = tuple(k for k in PARTIES if k not in (i, j))
        fiber = {w for w in compatible if w[i - 1] == i and w[j - 1] == j}
        expected = {identity, swap_identity(complement)}
        need(fiber == expected, FORCED_FIBER, (i, j, len(fiber)))
        forced.update(fiber)
        print("FORCED_FIBER", (i, j), tuple(sorted(fiber)))
    need(len(forced) == 7, FORCED_FIBER, (len(forced),))

    rectangles = (
        ((1, 2), (3, 4), (1, 3, 2, 4)),
        ((1, 3), (2, 4), (1, 2, 3, 4)),
        ((1, 4), (2, 3), (1, 2, 4, 3)),
    )
    for left, right, expected_failure in rectangles:
        a, b = swap_identity(left), swap_identity(right)
        double = list(identity)
        for i, j in (left, right):
            double[i - 1], double[j - 1] = double[j - 1], double[i - 1]
        double = tuple(double)
        need({identity, a, b} <= forced and double not in compatible, RECTANGLE)
        need(project(b, left) == project(identity, left)
             and project(a, right) == project(identity, right)
             and project(double, left) == project(a, left)
             and project(double, right) == project(b, right), RECTANGLE)
        expect_rejection("double_swap_{}_{}".format(left, right),
                         lambda w=double: check_residual_word(w, residual),
                         RESIDUAL_PAIR, expected_failure)

    binary_mutant = ((0, 0, 0), (0, 1, 0), (1, 0, 1), (1, 1, 1))
    need(all(len({(t[i], t[j]) for t in binary_mutant}) == 4
             for i, j in ((0, 1), (1, 2))), BINARY_CLASSIFICATION)
    expect_rejection("binary_two_projections_only",
                     lambda: check_binary(binary_mutant),
                     BINARY_PROJECTION, (0, 2, 2))

    substitutions = {(1, 1, 0, 5): (1, 1, 5, 5),
                     (4, 3, 5, 5): (4, 3, 0, 5)}
    packing_mutant = tuple(substitutions.get(w, w) for w in P_LITERAL)
    check_packing(packing_mutant, ((1, 2), (3, 4)))
    need(all(Counter(w[i] for w in packing_mutant)
             == Counter(w[i] for w in P_LITERAL) for i in range(4)),
         PACKING_INPUT)
    expect_rejection("packing_one_cut_only",
                     lambda: check_packing(packing_mutant),
                     PACKING_PAIR_COLLISION, (1, 3, 1, 5, 2))

    complement_mutant = {p: set(values) for p, values in residual.items()}
    complement_mutant[(1, 3)] = (set(product(INTERNAL, repeat=2))
                               - {(a, a) for a in INTERNAL})
    check_local_residual_degrees(complement_mutant)
    expect_rejection("six_local_graphs_without_common_complement",
                     lambda: check_common_complements(packing, complement_mutant),
                     COMMON_COMPLEMENT, (1, 3, 2, 2, 0, 1))

    cycle = {identity, swap_identity((1, 2)), swap_identity((3, 4)),
             (2, 1, 2, 2), (1, 3, 4, 3), (1, 3, 2, 2)}
    check_residual_set(cycle, residual)
    cycle_edges = flat_edges(cycle)
    need(len(cycle_edges) == 6, LOCAL_DEGREE, (len(cycle_edges),))
    check_degree_two(cycle_edges)
    expect_rejection("canonical_degree_two_six_cycle",
                     lambda: check_block_closure(cycle_edges),
                     SINGLE_INTERSECTION, ((1, 2), (1, 3), (4, 3)))

    # The complete 2x2 block is a genuine local unitary support, but the
    # fourth canonical word is globally forbidden. Do not promote this to
    # a tensor, residual completion, or AME witness.
    double = (2, 1, 4, 3)
    local_square = {identity, swap_identity((1, 2)),
                    swap_identity((3, 4)), double}
    check_block_closure(flat_edges(local_square))
    check_local_complex_unitary()
    expect_rejection("local_complex_unitary_is_not_global_tensor",
                     lambda: check_residual_set(local_square, residual),
                     RESIDUAL_PAIR, (1, 3, 2, 4))

    tick()
    print("BINARY_CHOICES", examined, "ACCEPTED", len(accepted))
    print("GAUGES", gauge_count, "DISTINCT_FLIPS", len(flips))
    print("COMMON_PACKING", len(packing), "LITERAL_EQUAL", True)
    print("RESIDUAL_WORDS", residual_examined, "COMPATIBLE", len(compatible))
    print("FIXED_COORDINATE_HISTOGRAM", tuple(sorted(histogram.items())))
    print("FORCED_FIBERS", len(PAIRS), "FORCED_UNION", len(forced))
    print("LOCAL_COMPLEX_UNITARY", "EXACT_GAUSSIAN_INTEGER_PASS")
    print("RESULT: PASS -- canonical finite checks only")
    print("NOT_CHECKED: all raw P; universal normal-form coverage; full E "
          "support enumeration; arbitrary amplitudes; original target; novelty")


if __name__ == "__main__":
    try:
        main()
    except AuditError as error:
        print("RESULT: FAIL reason={} detail={!r}".format(error.reason, error.detail))
        raise SystemExit(1)

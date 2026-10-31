#!/usr/bin/env python3
"""UNRUN candidate: exact finite-local necessities, not a global AME search.

No files, subprocesses, network, third-party packages, or floating tolerances.
All scientific arithmetic is integer/rational quadratic or cyclotomic arithmetic.
Stdout is JSONL; incomplete/error is nonzero. A parent source audit and a
separate one-shot GO are required before running this candidate.
"""

import itertools
import json
import signal
import sys
import time
from collections import Counter

LIMIT_SECONDS = 39.0  # cooperative monotonic-clock limit; mathematical tests are exact
START = None
STOP_SIGNAL = None
STAGE = "initialization"
PROGRESS = {}


class Violation(Exception):
    pass


class Incomplete(Exception):
    pass


def fail(reason):
    raise Violation(reason)


def demand(condition, reason):
    if not condition:
        fail(reason)


def emit(record):
    print(json.dumps(record, sort_keys=True, separators=(",", ":")), flush=True)


def request_stop(signum, _frame):
    global STOP_SIGNAL
    STOP_SIGNAL = signum


def guard():
    if STOP_SIGNAL is not None:
        raise Incomplete("SIGNAL_" + str(STOP_SIGNAL))
    if time.monotonic() - START >= LIMIT_SECONDS:
        raise Incomplete("INTERNAL_DEADLINE")


def begin(stage):
    global STAGE, PROGRESS
    guard()
    STAGE = stage
    PROGRESS = {}
    emit({"status": "STARTED", "stage": stage})


def completed(details):
    guard()
    emit({"status": "COMPLETE_STAGE", "stage": STAGE, "details": details})


def expect(reason, fn, *args):
    try:
        fn(*args)
    except Violation as error:
        demand(str(error) == reason, "CONTROL_WRONG_REASON:" + reason + ":" + str(error))
        return
    fail("CONTROL_DID_NOT_REJECT:" + reason)


def odd_triple(rows):
    """Find an explicit odd integral dependency supported on three rows."""
    if not rows:
        return None
    width = len(rows[0])
    for i, j, k in itertools.combinations(range(len(rows)), 3):
        for sj in (-1, 1):
            for sk in (-1, 1):
                if all(rows[i][v] + sj * rows[j][v] + sk * rows[k][v] == 0
                       for v in range(width)):
                    return i, j, k, sj, sk
    return None


def check_dependency(rows, y):
    demand(len(rows) == len(y) and bool(rows), "DEPENDENCY_SHAPE")
    width = len(rows[0])
    demand(all(len(row) == width for row in rows), "DEPENDENCY_SHAPE")
    demand(all(sum(y[i] * rows[i][j] for i in range(len(rows))) == 0
               for j in range(width)), "NOT_INTEGER_DEPENDENCY")
    demand(sum(y) % 2 == 1, "EVEN_DEPENDENCY")


def dependency_from_triple(rows, witness):
    demand(witness is not None, "MISSING_ODD_TRIPLE")
    i, j, k, sj, sk = witness
    y = [0] * len(rows)
    y[i], y[j], y[k] = 1, sj, sk
    check_dependency(rows, y)
    return y


def cube_rows(words):
    present = set(words)
    rows = []
    for axis in range(3):
        bit = 1 << axis
        left = {w & ~bit for w in present if not (w & bit)}
        right = {w & ~bit for w in present if w & bit}
        common = sorted(left & right)
        if len(common) == 2:
            r, s = common
            row = [0] * 8
            row[r] += 1
            row[r | bit] -= 1
            row[s] -= 1
            row[s | bit] += 1
            rows.append(tuple(row))
    return rows


def check_slice(words):
    """A necessary local test, conditional on three unit-norm row systems."""
    present = set(words)
    demand(len(present) == len(words) and all(0 <= w < 8 for w in present),
           "SLICE_WORDS")
    for axis in range(3):
        bit = 1 << axis
        left = {w & ~bit for w in present if not (w & bit)}
        right = {w & ~bit for w in present if w & bit}
        demand(len(left) >= 2 and len(right) >= 2, "SLICE_LINE_DEGREE")
        demand(len(left & right) != 1, "SLICE_ONE_OVERLAP")
    if len(present) == 6:
        missing = sorted(set(range(8)) - present)
        distance = (missing[0] ^ missing[1]).bit_count()
        if distance == 1:
            bit = missing[0] ^ missing[1]
            empty_fiber = missing[0] & ~bit
            opposite = empty_fiber ^ (7 ^ bit)
            demand(opposite in present and (opposite | bit) in present,
                   "SLICE_ZERO_FIBER_CONTROL")
            fail("SLICE_ZERO_FIBER_NORM")
        if distance == 3:
            rows = cube_rows(present)
            demand(len(rows) == 3, "SLICE_ODD_PHASE_ROW_COUNT")
            dependency_from_triple(rows, odd_triple(rows))
            fail("SLICE_ODD_PHASE_DEPENDENCY")


def cube_exhaustion():
    begin("binary_three_cube_slices")
    counts = Counter()
    accepted = Counter()
    for mask in range(256):
        if mask % 32 == 0:
            guard()
        words = tuple(w for w in range(8) if mask & (1 << w))
        h = len(words) - 4
        distance = -1
        if len(words) == 6:
            holes = [w for w in range(8) if w not in words]
            distance = (holes[0] ^ holes[1]).bit_count()
        try:
            check_slice(words)
            reason = "LOCAL_ACCEPT"
            accepted[(h, distance)] += 1
        except Violation as error:
            reason = str(error)
        counts[(h, distance, reason)] += 1
    demand(sum(counts.values()) == 256, "CUBE_COVERAGE")
    demand(sum(v for (h, _), v in accepted.items() if h == 1) == 0,
           "CUBE_H1_SURVIVOR")
    demand(accepted[(2, 1)] == 0 and accepted[(2, 2)] == 12
           and accepted[(2, 3)] == 0, "CUBE_H2_DISTANCE")
    demand(counts[(2, 1, "SLICE_ZERO_FIBER_NORM")] == 12,
           "CUBE_DISTANCE1_COVERAGE")
    demand(counts[(2, 3, "SLICE_ODD_PHASE_DEPENDENCY")] == 4,
           "CUBE_DISTANCE3_COVERAGE")
    demand(accepted[(3, -1)] == 8 and accepted[(4, -1)] == 1,
           "CUBE_HIGH_SURVIVORS")
    summary = [{"h": h, "missing_distance": d, "reason": r, "count": n}
               for (h, d, r), n in sorted(counts.items())]
    completed({"masks": 256, "classes": summary})


def moment_constants(t, q):
    n = 36 - t
    return t, 6 * sum(q) - 4 * n, sum(a * b for a, b in itertools.combinations(q, 2)) - 6 * n


def check_moment(t, q, nk):
    total, first, second = moment_constants(t, q)
    demand(len(nk) == 5 and all(isinstance(x, int) and x >= 0 for x in nk), "P_PROFILE_SHAPE")
    demand(sum(nk) == total, "P_TOTAL")
    demand(sum(k * nk[k] for k in range(5)) == first, "P_FIRST_MOMENT")
    demand(sum((k * (k - 1) // 2) * nk[k] for k in range(5)) == second,
           "P_SECOND_MOMENT")


def moment_solutions(t, q):
    total, first, second = moment_constants(t, q)
    out = []
    for n4 in range(total + 1):
        for n3 in range(total - n4 + 1):
            n2 = second - 3 * n3 - 6 * n4
            n1 = first - 2 * n2 - 3 * n3 - 4 * n4
            n0 = total - n1 - n2 - n3 - n4
            nk = (n0, n1, n2, n3, n4)
            if min(nk) >= 0:
                check_moment(t, q, nk)
                out.append(nk)
    return tuple(out)


def degree_types(q, total, max_degree):
    return [d for d in itertools.combinations_with_replacement(range(2, max_degree + 1), q)
            if sum(d) == total]


def moment_exhaustion():
    begin("q_and_P_moments_and_degree_types")
    profiles = {}
    degree_tables = {}
    for t in (26, 28):
        n = 36 - t
        max_q = n // 2
        eligible = {}
        for q in itertools.combinations_with_replacement(range(2, max_q + 1), 4):
            guard()
            if any(a * b < n for a, b in itertools.combinations(q, 2)):
                continue
            if any(not (0 <= 6 * a - n <= t) for a in q):
                continue
            eligible["".join(map(str, q))] = moment_solutions(t, q)
        profiles[str(t)] = eligible
        degree_tables[str(t)] = {str(q): degree_types(q, n, max_q)
                                  for q in range(2, max_q + 1)}
    p26 = profiles["26"]
    demand(set(p26["3444"]) == {(0, 2, 24, 0, 0)}, "MOMENT_3444")
    demand(set(p26["3445"]) == {(0, 1, 20, 5, 0), (0, 0, 23, 2, 1)}, "MOMENT_3445")
    demand(set(p26["4444"]) == {(0, 2, 18, 6, 0), (0, 1, 21, 3, 1),
                                  (0, 0, 24, 0, 2)}, "MOMENT_4444")
    demand(set(p26["4445"]) == {(0, 2, 12, 12, 0), (0, 1, 15, 9, 1),
                                  (0, 0, 18, 6, 2)}, "MOMENT_4445")
    demand(not profiles["28"]["3333"] and not profiles["28"]["3334"],
           "MOMENT_T28_TWO_FOURS")
    demand(set(degree_tables["26"]["4"]) == {(2, 2, 2, 4), (2, 2, 3, 3)},
           "T26_Q4_DEGREES")
    demand(degree_tables["26"]["5"] == [(2, 2, 2, 2, 2)], "T26_Q5_DEGREES")
    demand(degree_tables["28"]["4"] == [(2, 2, 2, 2)], "T28_Q4_DEGREES")
    h26 = tuple(x for x in itertools.combinations_with_replacement((0, 2, 3, 4), 5)
                if sum(x) == 4)
    h28 = tuple(x for x in itertools.combinations_with_replacement((0, 2, 3, 4), 4)
                if sum(x) == 6)
    demand(set(h26) == {(0, 0, 0, 0, 4), (0, 0, 0, 2, 2)}, "T26_Q5_SURPLUS")
    demand(set(h28) == {(0, 0, 2, 4), (0, 0, 3, 3), (0, 2, 2, 2)},
           "T28_Q4_SURPLUS")
    completed({"moment_necessary_profiles": profiles, "degree_types": degree_tables,
               "t26_q5_surplus": h26, "t28_q4_surplus_before_common_holes": h28})


def columns(graph, q):
    return tuple(sum(1 << r for r in range(q) if graph[r] & (1 << c)) for c in range(q))


def connected(graph, q):
    seen_rows = {0}
    seen_cols = set()
    todo = [(0, 0)]
    col_masks = columns(graph, q)
    while todo:
        side, v = todo.pop()
        if side == 0:
            for c in range(q):
                if graph[v] & (1 << c) and c not in seen_cols:
                    seen_cols.add(c)
                    todo.append((1, c))
        else:
            for r in range(q):
                if col_masks[v] & (1 << r) and r not in seen_rows:
                    seen_rows.add(r)
                    todo.append((0, r))
    return len(seen_rows) == q and len(seen_cols) == q


def check_t26_mask(graph):
    q = 4
    demand(len(graph) == q and all(0 <= row < (1 << q) for row in graph), "MASK_SHAPE")
    demand(sum(row.bit_count() for row in graph) == 12, "MASK_WEIGHT")
    cols = columns(graph, q)
    demand(all(x.bit_count() >= 2 for x in graph + cols), "MASK_MIN_DEGREE")
    for side in (graph, cols):
        for a, b in itertools.combinations(side, 2):
            demand((a & b).bit_count() != 1, "MASK_ONE_OVERLAP")
    demand(connected(graph, q), "MASK_DISCONNECTED")
    for side in (graph, cols):
        opposite = columns(side, q)
        low = [row for row in side if row.bit_count() == 2]
        for a, b in itertools.combinations(low, 2):
            demand(a & b == 0, "MASK_LOW_PAIR_DISJOINT")
        for row in low:
            neighbors = [c for c in range(q) if row & (1 << c)]
            a, b = (opposite[c] for c in neighbors)
            demand(a == b and a.bit_count() >= 3, "MASK_LOW_TWINS")


def mask_exhaustion():
    begin("t26_order4_all_12_entry_masks")
    all_types = Counter()
    accepted = Counter()
    reasons = Counter()
    for number, holes in enumerate(itertools.combinations(range(16), 4)):
        if number % 64 == 0:
            guard()
        graph = [15] * 4
        for hole in holes:
            graph[hole // 4] ^= 1 << (hole % 4)
        graph = tuple(graph)
        key = "".join(map(str, sorted(x.bit_count() for x in graph))) + "/" + \
              "".join(map(str, sorted(x.bit_count() for x in columns(graph, 4))))
        all_types[key] += 1
        try:
            check_t26_mask(graph)
            accepted[key] += 1
        except Violation as error:
            reasons[str(error)] += 1
    demand(sum(all_types.values()) == 1820, "MASK_ENUMERATION_COVERAGE")
    demand(dict(accepted) == {"3333/3333": 24, "2244/3333": 36,
                               "3333/2244": 36}, "MASK_DEGREE_CLASSIFICATION")
    completed({"total": 1820, "all_degree_types": dict(sorted(all_types.items())),
               "necessary_accepted_degree_types": dict(sorted(accepted.items())),
               "first_rejection_reasons": dict(sorted(reasons.items()))})


def two_regular_graphs(q):
    options = [sum(1 << c for c in pair) for pair in itertools.combinations(range(q), 2)]
    for number, graph in enumerate(itertools.product(options, repeat=q)):
        if number % 256 == 0:
            PROGRESS["graph_tuples_visited"] = number
            guard()
            if q == 5 and number and number % 20480 == 0:
                emit({"status": "PARTIAL", "stage": STAGE, "progress": dict(PROGRESS)})
        if all(sum(bool(row & (1 << c)) for row in graph) == 2 for c in range(q)):
            yield graph


def positive_patterns(row_h, col_h):
    """All weights: zero-h vertices cannot meet a positive edge."""
    q = len(row_h)
    ri = [i for i, h in enumerate(row_h) if h]
    ci = [j for j, h in enumerate(col_h) if h]
    patterns = []
    for entries in itertools.product(range(3), repeat=len(ri) * len(ci)):
        matrix = [[0] * q for _ in range(q)]
        for (i, j), value in zip(itertools.product(ri, ci), entries):
            matrix[i][j] = value
        if (tuple(map(sum, matrix)) == tuple(row_h)
                and tuple(sum(matrix[i][j] for i in range(q)) for j in range(q)) == tuple(col_h)):
            patterns.append(tuple(tuple(row) for row in matrix))
    return patterns


def check_weighted_pair(graph, weights, row_h, col_h, common_xx):
    q = len(row_h)
    demand(len(graph) == q and len(col_h) == q and len(weights) == q
           and all(len(row) == q for row in weights), "PAIR_SHAPE")
    demand(all(0 <= row < (1 << q) and row.bit_count() == 2 for row in graph),
           "PAIR_ROW_DEGREE")
    demand(all(col.bit_count() == 2 for col in columns(graph, q)), "PAIR_COLUMN_DEGREE")
    for i in range(q):
        for j in range(q):
            demand(weights[i][j] in (0, 1, 2), "PAIR_WEIGHT_RANGE")
            demand(not weights[i][j] or graph[i] & (1 << j), "PAIR_POSITIVE_NONEDGE")
    demand(tuple(map(sum, weights)) == tuple(row_h), "PAIR_ROW_SURPLUS")
    demand(tuple(sum(weights[i][j] for i in range(q)) for j in range(q)) == tuple(col_h),
           "PAIR_COLUMN_SURPLUS")
    if common_xx:
        demand(q == 4 and bool(graph[1] & 2) and weights[1][1] == 0,
               "PAIR_XX_COMMON_HOLE")


def q4_exhaustion():
    begin("t28_q4_XY_pair_graphs")
    profiles = {"X": (4, 2, 0, 0), "Y": (3, 3, 0, 0)}
    cases = {}
    for left in ("X", "Y"):
        for right in ("X", "Y"):
            rh, ch = profiles[left], profiles[right]
            patterns = positive_patterns(rh, ch)
            graphs = raw = accepted = rejected_xx = 0
            shapes = Counter()
            for graph in two_regular_graphs(4):
                graphs += 1
                for weights in patterns:
                    if any(weights[i][j] and not (graph[i] & (1 << j))
                           for i in range(4) for j in range(4)):
                        continue
                    check_weighted_pair(graph, weights, rh, ch, False)
                    raw += 1
                    if left == right == "X" and not (graph[1] & 2):
                        rejected_xx += 1
                        expect("PAIR_XX_COMMON_HOLE", check_weighted_pair,
                               graph, weights, rh, ch, True)
                        continue
                    check_weighted_pair(graph, weights, rh, ch, left == right == "X")
                    accepted += 1
                    hh = tuple(tuple(weights[i][j] for j in range(2)) for i in range(2))
                    shapes[str(hh)] += 1
                    demand(all(not (graph[i] & (1 << j)) for i in range(2) for j in range(2, 4)),
                           "Q4_HIGH_LOW_EDGE")
                    demand(all(not (graph[i] & (1 << j)) for i in range(2, 4) for j in range(2)),
                           "Q4_LOW_HIGH_EDGE")
                    allowed = {("X", "X"): {((2, 2), (2, 0))},
                               ("X", "Y"): {((2, 2), (1, 1))},
                               ("Y", "X"): {((2, 1), (2, 1))},
                               ("Y", "Y"): {((2, 1), (1, 2)), ((1, 2), (2, 1))}}
                    demand(hh in allowed[(left, right)], "Q4_HIGH_BLOCK_SHAPE")
            demand(graphs == 90 and accepted > 0, "Q4_GRAPH_COVERAGE")
            if left == right == "X":
                demand(rejected_xx > 0, "Q4_XX_CONTROL_CLASS_MISSING")
            cases[left + right] = {"two_regular_graphs": graphs, "raw_weighted": raw,
                                   "accepted_with_XX_condition": accepted,
                                   "rejected_by_XX_condition": rejected_xx,
                                   "accepted_high_weight_blocks": dict(sorted(shapes.items()))}
    completed(cases)


def q5_exhaustion():
    begin("t26_q5_q5_pair_cases")
    profiles = {"4": (4, 0, 0, 0, 0), "22": (2, 2, 0, 0, 0)}
    case_names = tuple(itertools.product(("4", "22"), repeat=2))
    patterns = {key: positive_patterns(profiles[key[0]], profiles[key[1]]) for key in case_names}
    counts = Counter()
    shapes = {key: Counter() for key in case_names}
    graphs = 0
    for graph in two_regular_graphs(5):
        graphs += 1
        PROGRESS["two_regular_graphs"] = graphs
        for key in case_names:
            for weights in patterns[key]:
                if any(weights[i][j] and not (graph[i] & (1 << j))
                       for i in range(5) for j in range(5)):
                    continue
                check_weighted_pair(graph, weights, profiles[key[0]], profiles[key[1]], False)
                counts[key] += 1
                hi_rows = [i for i, h in enumerate(profiles[key[0]]) if h]
                hi_cols = [j for j, h in enumerate(profiles[key[1]]) if h]
                hh = tuple(tuple(weights[i][j] for j in hi_cols) for i in hi_rows)
                shapes[key][str(hh)] += 1
                if key == ("22", "22"):
                    demand(hh in {((2, 0), (0, 2)), ((0, 2), (2, 0)),
                                  ((1, 1), (1, 1))}, "Q5_HIGH_BLOCK_SHAPE")
    demand(graphs > 0 and counts[("4", "4")] == 0, "Q5_GRAPH_COVERAGE")
    demand(all(counts[key] > 0 for key in case_names if key != ("4", "4")),
           "Q5_NONEMPTY_WEIGHT_CLASSES")
    result = {left + "/" + right: {"weighted_graphs": counts[(left, right)],
                                      "high_weight_blocks": dict(sorted(shapes[(left, right)].items()))}
              for left, right in case_names}
    completed({"labeled_two_regular_graphs": graphs, "cases": result,
               "interpretation": "local necessary pair graphs only"})


def pair_label(word, pair):
    return ((word >> pair[0]) & 1) * 2 + ((word >> pair[1]) & 1)


def check_balanced(words):
    demand(len(words) == 8 and len(set(words)) == 8 and all(0 <= w < 16 for w in words),
           "BALANCED_WORDS")
    for pair in itertools.combinations(range(4), 2):
        counts = Counter(pair_label(word, pair) for word in words)
        demand(all(counts[v] == 2 for v in range(4)), "PAIR_BALANCE")


def phase_rows_for_support(words):
    """Rows of the common unit-phase system, including all six orientations."""
    words = tuple(sorted(words))
    rows = []
    labels = []
    for pair in itertools.combinations(range(4), 2):
        other = tuple(i for i in range(4) if i not in pair)
        groups = [dict() for _ in range(4)]
        for index, word in enumerate(words):
            r, c = pair_label(word, pair), pair_label(word, other)
            demand(c not in groups[r], "SUPPORT_DUPLICATE_CELL")
            groups[r][c] = index
        for r, s in itertools.combinations(range(4), 2):
            common = sorted(set(groups[r]) & set(groups[s]))
            demand(len(common) != 1, "SUPPORT_ONE_OVERLAP")
            if len(common) == 2:
                c, d = common
                row = [0] * 8
                row[groups[r][c]] += 1
                row[groups[s][c]] -= 1
                row[groups[r][d]] -= 1
                row[groups[s][d]] += 1
                rows.append(tuple(row))
                labels.append((pair, r, s, c, d))
    return rows, labels


def parity_descriptor(words):
    for size in (3, 4):
        for indices in itertools.combinations(range(4), size):
            values = {sum((w >> i) & 1 for i in indices) % 2 for w in words}
            if len(values) == 1:
                return indices, next(iter(values))
    return None


def binary8_exhaustion():
    begin("binary_8word_all_six_pair_balance_and_phases")
    examined = 0
    balanced = 0
    types = Counter()
    certificates = []
    for words in itertools.combinations(range(16), 8):
        examined += 1
        if examined % 128 == 0:
            PROGRESS["eight_word_sets_examined"] = examined
            guard()
        try:
            check_balanced(words)
        except Violation as error:
            demand(str(error) == "PAIR_BALANCE", "BALANCED_ENUMERATION_ERROR")
            continue
        balanced += 1
        descriptor = parity_descriptor(words)
        demand(descriptor is not None, "BALANCED_PARITY_CLASSIFICATION")
        types[str(len(descriptor[0]))] += 1
        rows, labels = phase_rows_for_support(words)
        witness = odd_triple(rows)
        y = dependency_from_triple(rows, witness)
        selected = [i for i, coefficient in enumerate(y) if coefficient]
        for signs in itertools.product((-1, 1), repeat=3):
            oriented = list(rows)
            adjusted = list(y)
            for i, sign in zip(selected, signs):
                oriented[i] = tuple(sign * value for value in rows[i])
                adjusted[i] *= sign
            check_dependency(oriented, adjusted)
        certificates.append({"words": words, "parity_subset": descriptor[0],
                             "parity": descriptor[1],
                             "dependency": [{"equation": labels[i], "row": rows[i],
                                             "coefficient": y[i]} for i in selected]})
    demand(examined == 12870 and balanced == 10 and dict(types) == {"3": 8, "4": 2},
           "BALANCED_SUPPORT_COVERAGE")
    completed({"eight_word_sets": examined, "pair_balanced_sets": balanced,
               "parity_support_types": dict(sorted(types.items())),
               "odd_integral_phase_certificates": certificates})


def qmul(a, b):
    return a[0] * b[0] + 2 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def qdot(a, b):
    products = [qmul(x, y) for x, y in zip(a, b)]
    return sum(p[0] for p in products), sum(p[1] for p in products)


def check_real_gram(matrix, norm):
    demand(matrix and all(len(row) == len(matrix) for row in matrix), "GRAM_SHAPE")
    for row in matrix:
        demand(qdot(row, row) == (norm, 0), "GRAM_NORM")
    for a, b in itertools.combinations(matrix, 2):
        demand(qdot(a, b) == (0, 0), "GRAM_OFFDIAGONAL")


def cmul(a, b):
    # a+b*omega, omega^2+omega+1=0.
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def cconj(a):
    return a[0] - a[1], -a[1]


def check_cyclotomic_gram(matrix, norm):
    demand(matrix and all(len(row) == len(matrix) for row in matrix), "CGRAM_SHAPE")
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            products = [cmul(a, cconj(b)) for a, b in zip(matrix[i], matrix[j])]
            value = (sum(p[0] for p in products), sum(p[1] for p in products))
            demand(value == ((norm, 0) if i == j else (0, 0)), "CGRAM_ENTRY")


def check_cube_example(values):
    demand(len(values) == 8, "EXAMPLE_SLICE_SHAPE")
    for axis in range(3):
        bit = 1 << axis
        left = [values[w] for w in range(8) if not (w & bit)]
        right = [values[w | bit] for w in range(8) if not (w & bit)]
        demand(qdot(left, left) == (4, 0) and qdot(right, right) == (4, 0),
               "EXAMPLE_SLICE_NORM")
        demand(qdot(left, right) == (0, 0), "EXAMPLE_SLICE_INNER")


def fixtures():
    m = [[0, 5, 5, 5], [-5, 0, 5, -5], [-7, 1, -4, 3], [1, 7, -3, -4]]
    m = [[(x, 0) for x in row] for row in m]
    r = [[(3, 0), (3, 0), (0, 0), (0, 0)],
         [(1, 0), (-1, 0), (0, -2), (0, -2)],
         [(-2, 0), (2, 0), (0, 1), (0, -2)],
         [(-2, 0), (2, 0), (0, -2), (0, 1)]]
    o3 = [[(0, 0), (0, 1), (0, 1)],
          [(0, 1), (1, 0), (-1, 0)],
          [(0, 1), (-1, 0), (1, 0)]]
    o4 = [[(0, 1), (0, 1), (0, 0), (0, 0)],
          [(0, 0), (0, 0), (0, 1), (0, 1)],
          [(1, 0), (-1, 0), (1, 0), (-1, 0)],
          [(1, 0), (-1, 0), (-1, 0), (1, 0)]]
    c4 = [[0, 1, 1, 1], [-1, 0, 1, -1],
          [-1, -1, 0, 1], [-1, 1, -1, 0]]
    c4 = [[(x, 0) for x in row] for row in c4]
    h2 = [[(1, 0), (1, 0)], [(1, 0), (-1, 0)]]
    one, omega, omega2 = (1, 0), (0, 1), (-1, -1)
    f3 = [[one, one, one], [one, omega, omega2], [one, omega2, omega]]
    cube = [(0, 0), (0, 1), (0, -1), (0, 0),
            (1, 0), (1, 0), (1, 0), (-1, 0)]
    return m, r, o3, o4, c4, h2, f3, cube


def illustrative_checks():
    begin("exact_illustrative_local_gram_checks")
    m, r, o3, o4, c4, h2, f3, cube = fixtures()
    for matrix, norm in ((m, 75), (r, 18), (o3, 4), (o4, 4), (c4, 3), (h2, 2)):
        check_real_gram(matrix, norm)
    check_cyclotomic_gram(f3, 3)
    check_cube_example(cube)
    demand(sum(x == (0, 0) for row in m for x in row) == 2, "M_ZERO_COUNT")
    demand(sum(x == (0, 0) for row in r for x in row) == 2, "R_ZERO_COUNT")
    demand(sum(x == (0, 0) for row in o3 for x in row) == 1, "O3_ZERO_COUNT")
    demand(sum(x == (0, 0) for row in o4 for x in row) == 4, "O4_ZERO_COUNT")
    demand(sum(x == (0, 0) for row in c4 for x in row) == 4, "C4_ZERO_COUNT")
    for matrix, norm in ((m, 75), (r, 18), (o3, 4), (o4, 4), (c4, 3), (h2, 2)):
        demand(all(0 < qmul(x, x)[0] < norm and qmul(x, x)[1] == 0
                   for row in matrix for x in row if x != (0, 0)), "LOCAL_NONUNIT_ENTRY")
    demand(28 + 2 * 9 + 4 == 50 and 28 + 14 + 2 * 4 == 50,
           "LOCAL_DIRECT_SUM_SUPPORT_COUNTS")
    completed({"M_integer_gram": 75, "R_scaled_sqrt2_gram": 18,
               "t26_three_by_three_gram": 4, "t26_2244_gram": 4,
               "t26_3333_gram": 3, "H2_numerator_gram": 2,
               "F3_cyclotomic_gram": 3, "cube_scaled_gram": 4,
               "scope": "local matrices and slice, NOT an AME tensor"})


def reason_controls():
    begin("targeted_reason_controls")
    cube_words = tuple(range(8))
    expect("SLICE_ONE_OVERLAP", check_slice, tuple(x for x in cube_words if x not in (0, 1, 6)))
    expect("SLICE_ZERO_FIBER_NORM", check_slice, tuple(x for x in cube_words if x not in (0, 1)))
    expect("SLICE_ODD_PHASE_DEPENDENCY", check_slice, tuple(x for x in cube_words if x not in (0, 7)))
    check_slice(tuple(x for x in cube_words if x not in (0, 3)))
    expect("P_TOTAL", check_moment, 26, (3, 4, 4, 4), (0, 2, 23, 0, 0))
    expect("P_FIRST_MOMENT", check_moment, 26, (3, 4, 4, 4), (0, 2, 23, 1, 0))
    expect("P_SECOND_MOMENT", check_moment, 26, (3, 4, 4, 4), (1, 0, 25, 0, 0))
    check_t26_mask((3, 12, 15, 15))
    expect("MASK_ONE_OVERLAP", check_t26_mask, (7, 12, 14, 15))
    x = (4, 2, 0, 0)
    valid_graph = (3, 3, 12, 12)
    valid_weights = ((2, 2, 0, 0), (2, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0))
    check_weighted_pair(valid_graph, valid_weights, x, x, True)
    bad_weights = ((1, 2, 0, 0),) + valid_weights[1:]
    expect("PAIR_ROW_SURPLUS", check_weighted_pair, valid_graph, bad_weights, x, x, True)
    no_common_hole_graph = (3, 5, 10, 12)
    check_weighted_pair(no_common_hole_graph, valid_weights, x, x, False)
    expect("PAIR_XX_COMMON_HOLE", check_weighted_pair, no_common_hole_graph, valid_weights, x, x, True)
    expect("PAIR_BALANCE", check_balanced, tuple(range(8)))
    expect("NOT_INTEGER_DEPENDENCY", check_dependency, [(2,)], [1])
    expect("EVEN_DEPENDENCY", check_dependency, [(1,), (-1,)], [1, 1])
    m, _, _, _, _, _, _, _ = fixtures()
    m[0][1] = (-5, 0)
    expect("GRAM_OFFDIAGONAL", check_real_gram, m, 75)
    completed({"targeted_reasons": ["SLICE_ONE_OVERLAP", "SLICE_ZERO_FIBER_NORM",
                                   "SLICE_ODD_PHASE_DEPENDENCY", "P_TOTAL", "P_FIRST_MOMENT",
                                   "P_SECOND_MOMENT", "MASK_ONE_OVERLAP", "PAIR_ROW_SURPLUS",
                                   "PAIR_XX_COMMON_HOLE", "PAIR_BALANCE", "NOT_INTEGER_DEPENDENCY",
                                   "EVEN_DEPENDENCY", "GRAM_OFFDIAGONAL"],
               "positive_controls": ["distance_two_cube", "t26_2244_mask", "XX_common_hole_pair"]})


def main():
    global START
    START = time.monotonic()
    try:
        signal.signal(signal.SIGTERM, request_stop)
        signal.signal(signal.SIGINT, request_stop)
        emit({"status": "STARTED", "stage": "run", "internal_limit_seconds": LIMIT_SECONDS,
              "scope": "finite local necessary conditions only"})
        reason_controls()
        illustrative_checks()
        cube_exhaustion()
        moment_exhaustion()
        mask_exhaustion()
        q4_exhaustion()
        binary8_exhaustion()
        q5_exhaustion()
        guard()
        emit({"status": "COMPLETE_LOCAL_NECESSITIES", "elapsed_seconds": time.monotonic() - START,
              "not_claimed": "global P/E enumeration or AME feasibility"})
        return 0
    except Incomplete as error:
        emit({"status": "INCOMPLETE", "reason": str(error), "stage": STAGE,
              "progress": dict(PROGRESS), "elapsed_seconds": time.monotonic() - START})
        return 2
    except Violation as error:
        emit({"status": "FAILED", "reason": str(error), "stage": STAGE,
              "progress": dict(PROGRESS), "elapsed_seconds": time.monotonic() - START})
        return 1
    except BaseException as error:
        emit({"status": "FAILED_EXCEPTION", "type": type(error).__name__, "reason": str(error),
              "stage": STAGE, "progress": dict(PROGRESS), "elapsed_seconds": time.monotonic() - START})
        return 1


if __name__ == "__main__":
    sys.exit(main())

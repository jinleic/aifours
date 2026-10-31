#!/usr/bin/env python3
"""F562 small physical interfaces only. No full P/E or AME witness.
Execution was NOT performed by the preparing FINITE reviewer.
Only argv/stdout/stderr and a cooperative monotonic clock are used.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product
from time import monotonic
import sys

PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
CUTS = ((0, 1), (0, 2), (0, 3))


class Defect(Exception):
    pass


class Deadline(Exception):
    pass


class Budget:
    def __init__(self, seconds):
        self.start = monotonic()
        self.end = self.start + seconds

    def tick(self):
        if monotonic() >= self.end:
            raise Deadline()


def need(condition, reason):
    if not condition:
        raise Defect(reason)


def projection(words, pair):
    return Counter((w[pair[0]], w[pair[1]]) for w in words)


def coverage(pairs):
    need(len(pairs) == 6 and set(pairs) == set(PAIRS),
         "PHYSICAL_PAIR_COVERAGE")


def reported_views(words, reports):
    coverage(tuple(reports))
    for pair in PAIRS:
        need(reports[pair] == projection(words, pair),
             "PAIR_VIEW_NOT_COMMON_WORDS")


def audit_rounding(component, rounded, pairs=PAIRS):
    coverage(pairs)
    need(len(set(component)) == len(component), "DUPLICATE_COMPONENT_WORD")
    need(len(set(rounded)) == len(rounded), "DUPLICATE_ROUNDED_WORD")
    need(set(rounded) <= set(component), "ROUNDING_NOT_SUBSET")
    need(2 * len(rounded) == len(component), "ROUNDING_SIZE")
    for pair in pairs:
        before = projection(component, pair)
        after = projection(rounded, pair)
        need(all(v == 2 for v in before.values()), "COMPONENT_MULTIPLICITY")
        need(set(before) == set(after), "ROUNDING_PAIR_SUPPORT")
        need(all(v == 1 for v in after.values()), "ROUNDING_PAIR_MULTIPLICITY")


def moment_values(expected=(60, 49)):
    q = (4, 4, 5, 5)
    values = (sum(6 * x - 12 for x in q),
              sum(q[i] * q[j] - 12 for i, j in PAIRS))
    need(values == expected, "MOMENT_VALUE_MISMATCH")
    return values


def degree_interfaces(budget, results):
    first, second = moment_values()
    regimes = set()
    for n0, n1, n4 in product(range(25), repeat=3):
        budget.tick()
        remaining = 24 - n0 - n1 - n4
        n3 = first - n1 - 4 * n4 - 2 * remaining
        n2 = remaining - n3
        if min(remaining, n2, n3) < 0:
            continue
        if n2 + 3 * n3 + 6 * n4 != second:
            continue
        row = (n0, n1, n2, n3, n4)
        need(3 * n0 + n1 + n4 == 1, "MOMENT_REGIME_IDENTITY")
        regimes.add(row)
    need(regimes == {(0, 1, 10, 13, 0), (0, 0, 13, 10, 1)},
         "MAXIMAL_REGIME_LIST")
    degrees = {}
    for q, constant in ((4, 8), (5, 7)):
        local = {}
        for r in range(2, 7):
            local[r] = {
                (sigma, tau, f)
                for sigma, tau, f in product(range(2), range(7), range(7))
                if sigma + tau + f <= 6 - r
                and tau + 2 * f - sigma == constant - 2 * r
            }
        need({r for r in local if local[r]} == {2, 3, 4}, "DEGREE_BOUND")
        if q == 5:
            need({sigma for sigma, tau, f in local[4]} == {1},
                 "FIVE_EXCEPTION_NEEDS_SINGLETON")
        degrees[q] = {tuple(sorted(rs, reverse=True))
                      for rs in product((2, 3, 4), repeat=q) if sum(rs) == 12}
    need(degrees[4] == {(3, 3, 3, 3), (4, 3, 3, 2), (4, 4, 2, 2)},
         "FOUR_SYMBOL_PROFILES")
    need(degrees[5] == {(3, 3, 2, 2, 2), (4, 2, 2, 2, 2)},
         "FIVE_SYMBOL_PROFILES")
    for row in regimes:
        allowed = {(e3, e4) for e3, e4 in product((0, 1), repeat=2)
                   if e3 + e4 <= row[1]}
        need((1, 1) not in allowed, "TWO_FIVE_EXCEPTIONS")
    results["moment_values"] = (first, second)
    results["maximal_regimes"] = sorted(regimes)
    results["degree_profiles"] = {q: sorted(v) for q, v in degrees.items()}


def audit_xy(rows):
    need(len(rows) == 4 and all(x in (0, 2) and y in (0, 2)
                              for x, y in rows), "XY_DOMAIN")
    need(sum(x for x, y in rows) == sum(y for x, y in rows) == 6,
         "XY_SUM")
    need(all(x + y > 0 for x, y in rows), "ZERO_RESIDUAL_DEGREE")
    need(sorted((x + y for x, y in rows), reverse=True) == [4, 4, 2, 2],
         "XY_PROFILE")
    ax = next(i for i, row in enumerate(rows) if row == (2, 0))
    ay = next(i for i, row in enumerate(rows) if row == (0, 2))
    need(ax != ay, "XY_ZERO_SYMBOLS_EQUAL")
    return ax, ay


def xy_interfaces():
    accepted = []
    for rows in product(((0, 0), (0, 2), (2, 0), (2, 2)), repeat=4):
        if sum(x for x, y in rows) != 6 or sum(y for x, y in rows) != 6:
            continue
        if any(x + y == 0 for x, y in rows):
            continue
        accepted.append((rows, audit_xy(rows)))
    need(len(accepted) == 12, "XY_ENUMERATION_COUNT")
    return accepted


def direct_interfaces(cases, budget, results):
    # Physical word order is (party1, party2, party3, party4).
    # These are only local three-word assignments, never a full P.
    sample = None
    total_local = 0
    quotient_pairs = 0
    for rows, (ax, ay) in cases:
        types = []
        representatives = []
        forced = (ax, 5)
        for h in (3, 4):
            views = set()
            representative = None
            count = 0
            for partners in permutations((4, 5, ax)):
                if any(partners[t] not in {4, 5, ay} for t in (0, 1)):
                    continue
                for b in product(range(6), repeat=3):
                    budget.tick()
                    words = tuple((partners[t], b[t], h, k)
                                  for t, k in enumerate((3, 4, 5)))
                    need(all(v == 1 for v in projection(words, (0, 2)).values()),
                         "LOCAL_13_NOT_INJECTIVE")
                    need(all(v == 1 for v in projection(words, (2, 3)).values()),
                         "LOCAL_34_NOT_INJECTIVE")
                    view = frozenset(projection(words, (0, 3)))
                    need(forced in view, "DIRECT_FORCED_14_MISSING")
                    views.add(view)
                    representative = words if representative is None else representative
                    count += 1
            need(count == 432 and len(views) == 2, "DIRECT_LOCAL_ASSIGNMENT_COUNT")
            total_local += count
            types.append(views)
            representatives.append(representative)
        for a, b in product(*types):
            need(forced in a & b, "DIRECT_DUPLICATE_14_NOT_FORCED")
            quotient_pairs += 1
        words = representatives[0] + representatives[1]
        need(all(v == 1 for v in projection(words, (0, 2)).values()),
             "JOIN_13_NOT_INJECTIVE")
        need(all(v == 1 for v in projection(words, (2, 3)).values()),
             "JOIN_34_NOT_INJECTIVE")
        need(projection(words, (0, 3))[forced] == 2, "JOIN_14_NOT_DUPLICATED")
        sample = words if sample is None else sample
    results["xy_cases"] = len(cases)
    results["local_three_word_assignments"] = total_local
    results["cross_h_14_type_pairs"] = quotient_pairs
    return sample


def signed_colors(n, edges):
    adjacent = [set() for _ in range(n)]
    for a, b in edges:
        adjacent[a].add(b)
        adjacent[b].add(a)
    color = {0: 0}
    queue = deque([0])
    while queue:
        a = queue.popleft()
        for b in adjacent[a]:
            if b not in color:
                color[b] = 1 - color[a]
                queue.append(b)
            else:
                need(color[b] != color[a], "ODD_CYCLE_Z")
    need(len(color) == n, "MATCHING_GRAPH_DISCONNECTED")
    return tuple(color[i] for i in range(n))


def colored_patterns(n, budget):
    m = n // 2
    ps = tuple(permutations(range(m)))
    for rest in combinations(range(1, n), m - 1):
        left = (0,) + rest
        right = tuple(v for v in range(n) if v not in left)
        for p0 in ps:
            for p1 in ps:
                budget.tick()
                if any(a == b for a, b in zip(p0, p1)):
                    continue
                for p2 in ps:
                    if any(c == a or c == b for a, b, c in zip(p0, p1, p2)):
                        continue
                    yield left, right, (p0, p1, p2)


def audit_triplets(triples, n):
    need(len(triples) == n, "TRIPLE_COUNT")
    need(len(set(triples)) == n, "DUPLICATE_TRIPLE")
    for j in range(3):
        need(all(v == 2 for v in Counter(t[j] for t in triples).values()),
             "COORDINATE_NOT_TWICE")
    for j, k in combinations(range(3), 2):
        need(len({(t[j], t[k]) for t in triples}) == n,
             "TRIPLE_TWO_COORDINATE_NOT_INJECTIVE")


def inspect_pattern(n, left, right, matchings):
    m = n // 2
    edges = tuple((left[i], right[p[i]]) for p in matchings for i in range(m))
    need(len(set(edges)) == 3 * m, "MATCHING_GRAPH_NOT_SIMPLE")
    color = signed_colors(n, edges)
    need({i for i, c in enumerate(color) if c == 0} == set(left),
         "BIPARTITION_DEDUP")
    for a in left:
        neighbors = {b for x, b in edges if x == a}
        need(len(neighbors) == 3, "LEFT_NOT_CUBIC")
        if n == 6:
            need(neighbors == set(right), "N6_NOT_K33")
        else:
            need(len(set(right) - neighbors) == 1, "N8_MISSING_NOT_MATCHING")
    for b in right:
        need(sum(b == y for x, y in edges) == 3, "RIGHT_NOT_CUBIC")
    triples = [[None] * 3 for _ in range(n)]
    for i, a in enumerate(left):
        triples[a] = [i, i, i]
    for j, p in enumerate(matchings):
        for i, v in enumerate(p):
            triples[right[v]][j] = i
    triples = tuple(map(tuple, triples))
    audit_triplets(triples, n)
    for j, p in enumerate(matchings):
        groups = defaultdict(list)
        for vertex, t in enumerate(triples):
            groups[t[j]].append(vertex)
        actual = {tuple(sorted(vs)) for vs in groups.values()}
        expected = {tuple(sorted((left[i], right[p[i]]))) for i in range(m)}
        need(actual == expected, "TRIPLE_MATCHING_CONSUMER_MISMATCH")
    return triples, color


def insert_twin(triple, symbol, coordinate):
    return triple[:coordinate] + (symbol,) + triple[coordinate:]


def component_and_rounding(triples, color, coordinate, flip):
    component = tuple(insert_twin(t, s, coordinate) for t in triples for s in (0, 1))
    rounded = tuple(insert_twin(t, color[v] ^ flip, coordinate)
                    for v, t in enumerate(triples))
    return component, rounded


def check_actual_block(words, cut, block):
    other = tuple(i for i in range(4) if i not in cut)
    rows = [tuple(block[r][0][i] for i in cut) for r in range(2)]
    cols = [tuple(block[0][c][i] for i in other) for c in range(2)]
    need(len(set(rows)) == len(set(cols)) == 2, "BLOCK_AXES")
    need(all(w in words for row in block for w in row), "BLOCK_CELL_ABSENT")
    for r, c in product(range(2), repeat=2):
        w = block[r][c]
        need(tuple(w[i] for i in cut) == rows[r]
             and tuple(w[i] for i in other) == cols[c], "BLOCK_PHYSICAL_ROUTING")
    for r in rows:
        need({tuple(w[i] for i in other) for w in words
              if tuple(w[i] for i in cut) == r} == set(cols), "BLOCK_NOT_CLOSED")
    for c in cols:
        need({tuple(w[i] for i in cut) for w in words
              if tuple(w[i] for i in other) == c} == set(rows), "BLOCK_NOT_CLOSED")


def phase_contradiction(words, selected):
    need(set(selected) == set(CUTS), "PHASE_CUT_COVERAGE")
    relations = []
    for cut in CUTS:
        block = selected[cut]
        check_actual_block(words, cut, block)
        row = Counter()
        for r, c in product(range(2), repeat=2):
            row[block[r][c]] += 1 if r == c else -1
        relations.append(row)
    coefficients = {w: sum(k * row[w] for k, row in zip((1, -1, 1), relations))
                    for w in words}
    need(all(v == 0 for v in coefficients.values()), "PHASE_LEFT_NOT_ZERO")
    need(sum((1, -1, 1)) % 2 == 1, "PHASE_RIGHT_NOT_ODD")


def phase_interfaces(results):
    words = tuple(w for w in product((0, 1), repeat=4) if sum(w) % 2 == 0)
    coverage(PAIRS)
    for pair in PAIRS:
        counts = projection(words, pair)
        need(len(counts) == 4 and set(counts.values()) == {2}, "EVEN_SUPPORT_PAIR")
    block_count = 0
    for cut in CUTS:
        other = tuple(i for i in range(4) if i not in cut)
        cells = {(tuple(w[i] for i in cut), tuple(w[i] for i in other)): w
                 for w in words}
        supports = defaultdict(set)
        for row, col in cells:
            supports[row].add(col)
        groups = defaultdict(list)
        for row, cols in supports.items():
            groups[tuple(sorted(cols))].append(row)
        need(len(groups) == 2, "EVEN_SUPPORT_BLOCK_COUNT")
        for cols, rows in groups.items():
            need(len(cols) == len(rows) == 2, "EVEN_SUPPORT_NOT_K22")
            block = tuple(tuple(cells[(r, c)] for c in cols) for r in sorted(rows))
            check_actual_block(words, cut, block)
            block_count += 1
    a, b, c = (0, 0, 0, 0), (0, 0, 1, 1), (0, 1, 0, 1)
    f, g, h = (1, 0, 1, 0), (1, 1, 0, 0), (1, 1, 1, 1)
    selected = {CUTS[0]: ((a, b), (g, h)),
                CUTS[1]: ((a, c), (f, h)),
                CUTS[2]: ((b, c), (f, g))}
    phase_contradiction(words, selected)
    results["even_binary_words"] = len(words)
    results["closed_physical_blocks"] = block_count
    return words, selected


def reject(name, reason, operation, controls):
    try:
        operation()
    except Defect as error:
        need(str(error) == reason, "WRONG_CONTROL_REASON:" + name + ":" + str(error))
        controls[name] = reason
    else:
        raise Defect("MUTATION_NOT_REJECTED:" + name)


def controls_interfaces(seed, local_words, phase_data, controls):
    triples, color = seed
    component, rounded = component_and_rounding(triples, color, 2, 0)
    audit_rounding(component, rounded)
    extra = tuple(len(Counter(t[j] for t in triples)) for j in range(3))
    partial = triples + (extra, extra)
    reject("partial_twins_6_inside_8", "DUPLICATE_TRIPLE",
           lambda: audit_triplets(partial, 8), controls)
    reject("odd_cycle_z", "ODD_CYCLE_Z",
           lambda: signed_colors(3, ((0, 1), (1, 2), (2, 0))), controls)
    words, selected = phase_data
    missing = {cut: selected[cut] for cut in CUTS[:-1]}
    reject("missed_third_phase_cut", "PHASE_CUT_COVERAGE",
           lambda: phase_contradiction(words, missing), controls)
    reports = {pair: projection(local_words, pair) for pair in PAIRS}
    reports[(0, 3)] = Counter((i, 5) for i in range(6))
    reject("independent_maximal_margins", "PAIR_VIEW_NOT_COMMON_WORDS",
           lambda: reported_views(local_words, reports), controls)
    reject("equal_xy_zeros", "ZERO_RESIDUAL_DEGREE",
           lambda: audit_xy(((0, 0), (2, 2), (2, 2), (2, 2))), controls)
    mono = tuple(insert_twin(t, 0, 2) for t in triples)
    reject("monochrome_rounding", "ROUNDING_PAIR_SUPPORT",
           lambda: audit_rounding(component, mono), controls)
    reject("dropped_physical_pair", "PHYSICAL_PAIR_COVERAGE",
           lambda: audit_rounding(component, rounded, PAIRS[:-1]), controls)
    reports = {pair: projection(component, pair) for pair in PAIRS}
    pair = (0, 3)
    reports[pair] = Counter({(5 if a == 0 else a, b): v
                             for (a, b), v in reports[pair].items()})
    reject("independent_pair_gauge", "PAIR_VIEW_NOT_COMMON_WORDS",
           lambda: reported_views(component, reports), controls)
    reject("wrong_pair_moment", "MOMENT_VALUE_MISMATCH",
           lambda: moment_values((60, 48)), controls)
    need(len(controls) == 9, "CONTROL_COVERAGE")


def run(seconds):
    budget = Budget(seconds)
    results, controls = {}, {}
    try:
        degree_interfaces(budget, results)
        cases = xy_interfaces()
        local_words = direct_interfaces(cases, budget, results)
        phase_data = phase_interfaces(results)
        seed_pattern = next(colored_patterns(6, budget))
        seed = inspect_pattern(6, *seed_pattern)
        controls_interfaces(seed, local_words, phase_data, controls)
        counts = {}
        rounds = 0
        dispatches = 0
        for n in (6, 8):
            count = 0
            for pattern in colored_patterns(n, budget):
                budget.tick()
                triples, color = inspect_pattern(n, *pattern)
                for coordinate, flip in product(range(4), (0, 1)):
                    budget.tick()
                    component, rounded = component_and_rounding(
                        triples, color, coordinate, flip)
                    audit_rounding(component, rounded)
                    rounds += 1
                    dispatches += 6
                count += 1
                results["partial_patterns_n" + str(n)] = count
            counts[n] = count
        need(counts == {6: 120, 8: 20160}, "COLORED_PATTERN_COUNTS")
        need(rounds == 162240 and dispatches == 973440, "ROUNDING_COVERAGE_COUNTS")
        results["completed_colored_patterns"] = counts
        results["rounding_components_and_orientations"] = rounds
        results["six_pair_dispatches"] = dispatches
        budget.tick()
    except Deadline:
        status, exit_code = "INCOMPLETE_DEADLINE", 2
    except Defect as error:
        status, exit_code = "CHECK_FAILED:" + str(error), 1
    else:
        status, exit_code = "FINITE_INTERFACES_COMPLETE", 0
    print("STATUS=" + status)
    print("SCOPE=small_interfaces_only_not_a_full_P_E_or_AME_witness")
    print("TWO_COMPONENT_FIXTURE=NOT_TESTED_NO_SUCH_FIXTURE_CONSTRUCTED")
    for name, value in results.items():
        print(str(name) + "=" + repr(value))
    for name, reason in controls.items():
        print("CONTROL[" + name + "]=" + reason)
    print("elapsed_seconds=" + repr(monotonic() - budget.start))
    return exit_code


if __name__ == "__main__":
    if len(sys.argv) == 1:
        seconds = 50
    elif len(sys.argv) == 3 and sys.argv[1] == "--max-seconds":
        try:
            seconds = int(sys.argv[2])
        except ValueError:
            raise SystemExit("max-seconds must be an integer in 1..50")
        if not 1 <= seconds <= 50:
            raise SystemExit("max-seconds must be an integer in 1..50")
    else:
        raise SystemExit("usage: f562_finite_check.py [--max-seconds SECONDS]")
    raise SystemExit(run(seconds))

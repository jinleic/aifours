#!/usr/bin/env python3
"""F763: exact finite LOCAL incidence primitives for N=49,t=28.

UNRUN author source.  Not a tensor/phase/P-set enumerator, an AME witness,
source authentication, or a proof of the global t bound.  A complete JSON
record means the finite loops ended; it does not adopt the author's theorem.
Only stdout is used; there are no input files, network or subprocesses.
Cooperative deadline 45 seconds; a parent may admit a single externally
supervised run with ceiling at most 55 seconds after reading the WHOLE source.
"""
from collections import Counter
from itertools import combinations, permutations, product
import json
import signal
import sys
import time

START = time.monotonic()
DEADLINE = START + 45.0


class Stop(Exception):
    pass


class Finding(Exception):
    def __init__(self, rule, detail=None):
        super().__init__(rule)
        self.rule = rule
        self.detail = detail


def tick():
    if time.monotonic() >= DEADLINE:
        raise Stop("cooperative_45_second_deadline")


def on_signal(number, _frame):
    raise Stop("signal_" + str(number))


def require(condition, rule, detail=None):
    if not condition:
        raise Finding(rule, detail)


def bits(mask, n):
    return [i for i in range(n) if mask & (1 << i)]


def partitions4(items):
    a, b, c, d = items
    return (((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c)))


def support_reason(mask):
    """Necessary conditions for a CONNECTED 4x4, 13-entry unitary support.

    No complex numbers are assigned.  No singleton overlaps is necessary in
    BOTH orientations; a repeated degree-two neighborhood isolates a 2x2
    block in a unitary.  The latter and twin columns apply only because this
    procedure concerns a connected order-four component.
    """
    if mask < 0 or mask >> 16 or mask.bit_count() != 13:
        return "CELL_COUNT"
    rows = [(mask >> (4 * i)) & 15 for i in range(4)]
    cols = [sum(((rows[i] >> j) & 1) << i for i in range(4)) for j in range(4)]
    if min(x.bit_count() for x in rows + cols) < 2:
        return "LINE_DEGREE"
    for name, lines in (("ROW", rows), ("COL", cols)):
        for i, j in combinations(range(4), 2):
            if (lines[i] & lines[j]).bit_count() == 1:
                return name + "_ONE_OVERLAP"
            if lines[i] == lines[j] and lines[i].bit_count() == 2:
                return name + "_LOW_PAIR_ISOLATES"
    for name, lines, opposite in (("ROW", rows, cols), ("COL", cols, rows)):
        for line in lines:
            if line.bit_count() == 2:
                u, v = bits(line, 4)
                if opposite[u] != opposite[v]:
                    return name + "_TWIN_NEIGHBORHOODS"
                if opposite[u].bit_count() < 3:
                    return name + "_TWIN_ISOLATES"
    reached = {0}
    frontier = [0]
    while frontier:
        vertex = frontier.pop()
        neighbors = ([4 + j for j in bits(rows[vertex], 4)] if vertex < 4
                     else bits(cols[vertex - 4], 4))
        for neighbor in neighbors:
            if neighbor not in reached:
                reached.add(neighbor)
                frontier.append(neighbor)
    if len(reached) != 8:
        return "DISCONNECTED"
    return None


def line_type(degrees):
    degrees = tuple(sorted(degrees, reverse=True))
    if degrees == (4, 3, 3, 3):
        return "A"
    if degrees == (4, 4, 3, 2):
        return "B"
    return "OTHER"


def support_types(mask):
    rows = [(mask >> (4 * i)) & 15 for i in range(4)]
    cols = [sum(((rows[i] >> j) & 1) << i for i in range(4)) for j in range(4)]
    return (line_type(x.bit_count() for x in rows),
            line_type(x.bit_count() for x in cols))


def gram_reason(matrix, scale):
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        return "MATRIX_SHAPE"
    for i in range(4):
        for j in range(4):
            target = scale * scale if i == j else 0
            if sum(matrix[i][k] * matrix[j][k] for k in range(4)) != target:
                return "ROW_GRAM"
            if sum(matrix[k][i] * matrix[k][j] for k in range(4)) != target:
                return "COL_GRAM"
    return None


def support_and_control():
    # Product of three elementary rational orthogonal rotations, written out
    # here from scratch.  BOTH integer Gram matrices must equal 125^2 I.
    matrix = [[0, 0, 75, 100], [0, 75, -80, 60],
              [75, -80, -48, 36], [-100, -60, -36, 27]]
    require(gram_reason(matrix, 125) is None, "POSITIVE_RATIONAL_GRAMS")
    positive = sum((1 << (4 * i + j)) for i in range(4) for j in range(4)
                   if matrix[i][j] != 0)
    require(support_reason(positive) is None, "POSITIVE_RATIONAL_SUPPORT")
    changed = [row[:] for row in matrix]
    changed[0][2] += 1
    require(gram_reason(changed, 125) == "ROW_GRAM", "MUTANT_GRAM_REASON")
    # Three zeros produce an explicit forbidden one-position row overlap.
    bad = 0xffff ^ sum(1 << x for x in (0, 1, 6))
    require(support_reason(bad) == "ROW_ONE_OVERLAP", "MUTANT_OVERLAP_REASON")
    survivors = []
    rejects = Counter()
    types = Counter()
    for missing in combinations(range(16), 3):
        mask = 0xffff ^ sum(1 << x for x in missing)
        reason = support_reason(mask)
        if reason:
            rejects[reason] += 1
            continue
        row_type, col_type = support_types(mask)
        require(row_type == col_type and row_type in ("A", "B"),
                "MISMATCHED_13_SUPPORT", {"mask": mask, "types": [row_type, col_type]})
        types[row_type] += 1
        survivors.append(mask)
    require(sum(rejects.values()) + len(survivors) == 560, "SUPPORT_COVERAGE")
    # Independent elementary count: 3 absent cells either nonattacking
    # (4*4*6=96), or an L (4*4*3*3=144).
    require(types == Counter({"A": 96, "B": 144}), "SUPPORT_COUNT", dict(types))
    return survivors, {"all_13_supports": 560, "necessary_survivors": len(survivors),
        "matched_types": dict(types), "rejected_by_first_reason": dict(rejects),
        "rational_unitary": {"numerator": matrix, "denominator": 125,
            "row_and_column_gram_target": 15625,
            "support_mask": positive, "scope": "one-cut unitary only"},
        "mutants": {"changed_matrix_entry": "ROW_GRAM", "one_overlap": "ROW_ONE_OVERLAP"}}


def slice_reason(missing):
    if len(missing) != 2 or any(not isinstance(x, int) or x < 0 or x > 7 for x in missing):
        return "VERTEX_RANGE"
    if missing[0] == missing[1]:
        return "REPEATED_VERTEX"
    return None


def cube_checks():
    require(slice_reason((0, 0)) == "REPEATED_VERTEX", "MUTANT_SLICE_REASON")
    patterns = Counter()
    for missing in combinations(range(8), 2):
        require(slice_reason(missing) is None, "CUBE_INPUT")
        remaining = set(range(8)) - set(missing)
        pattern = []
        for axis in range(3):
            counts = sorted(sum((v >> axis) & 1 == bit for v in remaining) for bit in (0, 1))
            expected = "B" if ((missing[0] >> axis) & 1) == ((missing[1] >> axis) & 1) else "A"
            observed = "B" if counts == [2, 4] else "A" if counts == [3, 3] else "OTHER"
            require(observed == expected, "S6_SLICE_COUNTS", [missing, axis, counts])
            pattern.append(observed)
        require(pattern.count("B") < 3, "S6_ALL_THREE_B", missing)
        patterns["".join(pattern)] += 1
    five_possible = 0
    for vertices in combinations(range(8), 5):
        s = set(vertices)
        counts = [(sum(not (v & (1 << axis)) for v in s),
                   sum(bool(v & (1 << axis)) for v in s)) for axis in range(3)]
        edges = [sum(v ^ (1 << axis) in s for v in s if not v & (1 << axis))
                 for axis in range(3)]
        if all(min(pair) >= 2 for pair in counts) and all(x != 1 for x in edges):
            five_possible += 1
    require(five_possible == 0, "FIVE_CUBE_COUNTEREXAMPLE", five_possible)
    return {"six_vertex_slices": 28, "ordered_axis_type_counts": dict(sorted(patterns.items())),
            "five_vertex_slices": 56, "five_vertex_necessary_survivors": five_possible,
            "mutant": "REPEATED_VERTEX"}


def graph_components(edges):
    neighbors = [set() for _ in range(8)]
    for e in edges:
        i, j = divmod(e, 4)
        neighbors[i].add(4 + j)
        neighbors[4 + j].add(i)
    unseen = set(range(8))
    sizes = []
    while unseen:
        stack = [min(unseen)]
        component = set()
        while stack:
            v = stack.pop()
            if v in component:
                continue
            component.add(v)
            stack.extend(neighbors[v] - component)
        unseen.difference_update(component)
        sizes.append(len(component))
    return sorted(sizes)


def weight_of(weights, edge):
    i, j = divmod(edge, 4)
    return weights[2 * i + j] if i < 2 and j < 2 else 0


def pair_reason(edges, weights):
    if len(edges) != 8 or len(weights) != 4 or any(e not in range(16) for e in edges):
        return "PAIR_SHAPE"
    if any(sum((4 * i + j) in edges for j in range(4)) != 2 for i in range(4)):
        return "ROW_DEGREE"
    if any(sum((4 * i + j) in edges for i in range(4)) != 2 for j in range(4)):
        return "COL_DEGREE"
    if any(w not in (0, 1, 2) for w in weights):
        return "WEIGHT_RANGE"
    if any(weights[2 * i + j] and (4 * i + j) not in edges
           for i in range(2) for j in range(2)):
        return "ABSENT_POSITIVE_WEIGHT"
    if any(sum(weight_of(weights, 4 * i + j) for j in range(4)) != (3, 2, 0, 0)[i]
           for i in range(4)):
        return "ROW_EXCESS"
    if any(sum(weight_of(weights, 4 * i + j) for i in range(4)) != (3, 2, 0, 0)[j]
           for j in range(4)):
        return "COL_EXCESS"
    return None


def pair_models():
    models = []
    degree_graphs = 0
    high = {0, 1, 4, 5}
    low = {10, 11, 14, 15}
    for choice in combinations(range(16), 8):
        edges = frozenset(choice)
        if any(sum((4 * i + j) in edges for j in range(4)) != 2 for i in range(4)):
            continue
        if any(sum((4 * i + j) in edges for i in range(4)) != 2 for j in range(4)):
            continue
        degree_graphs += 1
        for weights in product(range(3), repeat=4):
            if pair_reason(edges, weights) is not None:
                continue
            x = weights[0]
            h_edge = 5 not in edges
            if not h_edge:
                require(edges == high | low and graph_components(edges) == [4, 4],
                        "NON_H_NOT_TWO_K22", [sorted(edges), weights])
                require(x in (1, 2), "NON_H_WEIGHT", weights)
            else:
                require(x == 1 and graph_components(edges) == [8],
                        "H_NOT_EIGHT_CYCLE", [sorted(edges), weights])
            require(weights == (x, 3 - x, 3 - x, x - 1), "WEIGHT_EQUATIONS")
            models.append({"edges": edges, "weights": weights, "x": x,
                           "H": h_edge, "type": "A" if x == 2 else "B"})
    shapes = Counter((m["type"] + ("_H" if m["H"] else "_nonH")) for m in models)
    require(shapes == Counter({"A_nonH": 1, "B_nonH": 1, "B_H": 4}),
            "HIGH_PAIR_MODEL_COUNT", dict(shapes))
    actual_a = next(m for m in models if m["type"] == "A")
    require(pair_reason(actual_a["edges"], (2, 0, 1, 1)) == "ROW_EXCESS",
            "MUTANT_PAIR_WEIGHT_REASON")
    return models, {"all_8_of_16_graphs": 12870, "two_regular_graphs": degree_graphs,
                    "weighted_models": len(models), "shapes": dict(shapes),
                    "mutant": "ROW_EXCESS"}


K4 = tuple(combinations(range(4), 2))


def edge_mask(edges):
    return sum(1 << K4.index(tuple(sorted(edge))) for edge in edges)


def is_independent(vertices, hmask):
    return all(not (hmask & (1 << i)) or not ((vertices >> a) & 1 and (vertices >> b) & 1)
               for i, (a, b) in enumerate(K4))


def p_capacity_reason(hmask, used, slots):
    if used & ~hmask:
        return "USED_PAIR_NOT_H"
    degrees = [0] * 4
    for i, (a, b) in enumerate(K4):
        if used & (1 << i):
            degrees[a] += 1
            degrees[b] += 1
    if max(degrees) > 4:
        return "S_SYMBOL_CAPACITY"
    singles = sum(4 - degree for degree in degrees)
    needed = singles + used.bit_count()
    if needed > slots:
        return "P_WORD_CAPACITY"
    return None


def moment_reason(a, cap):
    if len(a) != 5 or any(not isinstance(x, int) or x < 0 for x in a):
        return "MOMENT_SHAPE"
    if sum(a) != 21 or sum(k * a[k] for k in range(5)) != 52:
        return "MOMENT_TOTAL"
    if sum((k * (k - 1) // 2) * a[k] for k in range(5)) != 70:
        return "MOMENT_PAIR"
    if a[4] > cap:
        return "ALL_HIGH_INDEPENDENT_SET_BOUND"
    return None


def four_four_four_four():
    matchings = [edge_mask(x) for x in (((0, 1), (2, 3)), ((0, 2), (1, 3)),
                                        ((0, 3), (1, 2)))]
    scenarios = 0
    feasible = []
    feasible_p_allocations = 0
    for cutset in range(7):
        bmask = 0
        for j in range(3):
            if cutset & (1 << j):
                bmask |= matchings[j]
        for hmask in range(64):
            if hmask & ~bmask:
                continue
            scenarios += 1
            require(all(not all(hmask & (1 << K4.index(tuple(sorted(e))))
                                for e in combinations(triangle, 2))
                        for triangle in combinations(range(4), 3)), "H_TRIANGLE")
            for used in range(64):
                if used & ~hmask:
                    continue
                if p_capacity_reason(hmask, used, 12) is None:
                    feasible_p_allocations += 1
                    feasible.append((bmask, hmask, used))
    require(feasible, "P_CAPACITY_HAS_NO_ABSTRACT_FEASIBLE_PATTERN")
    for bmask, hmask, used in feasible:
        require(hmask.bit_count() == 4 and bmask == hmask == used,
                "P_CAPACITY_COUNTEREXAMPLE", [bmask, hmask, used])
        independent_count = sum(is_independent(v, hmask) for v in range(16))
        require(independent_count == 7, "H_INDEPENDENT_SET_COUNT", [hmask, independent_count])
    cycle = feasible[0][1]
    three = cycle & (cycle - 1)
    require(p_capacity_reason(cycle, three, 12) == "P_WORD_CAPACITY", "MUTANT_P_CAPACITY")
    require(moment_reason((6, 1, 1, 3, 10), 7) == "ALL_HIGH_INDEPENDENT_SET_BOUND",
            "MUTANT_INDEPENDENT_SET")
    unconstrained = bounded = 0
    for a4 in range(22):
        tick()
        for a3 in range(22 - a4):
            for a2 in range(22 - a4 - a3):
                for a1 in range(22 - a4 - a3 - a2):
                    a0 = 21 - a1 - a2 - a3 - a4
                    a = (a0, a1, a2, a3, a4)
                    if (sum(k * a[k] for k in range(5)) == 52 and
                            sum((k * (k - 1) // 2) * a[k] for k in range(5)) == 70):
                        unconstrained += 1
                        if a4 <= 7:
                            bounded += 1
    require(bounded == 0, "MOMENT_BOUND_COUNTEREXAMPLE", bounded)
    return {"labeled_cut_H_scenarios": scenarios, "abstract_P_allocations": feasible_p_allocations,
            "feasible_masks_B_H_used": [list(x) for x in feasible],
            "independent_sets_per_feasible_H": 7,
            "moments": {"word_count": 21, "high_incidences": 52, "high_pairs": 70,
                        "unbounded_vectors": unconstrained, "bounded_vectors": bounded},
            "mutants": {"three_used_edges": "P_WORD_CAPACITY",
                        "moment_vector_6_1_1_3_10": "ALL_HIGH_INDEPENDENT_SET_BOUND"},
            "boundary": "P packing is a necessary relaxation, not a P-set construction"}


def rectangle_reason(star, rectangle):
    cells = set(rectangle)
    if len(cells) != 4 or any(a not in range(3) or b not in range(3) for a, b in cells):
        return "RECTANGLE_SHAPE"
    aa, bb = {a for a, _ in cells}, {b for _, b in cells}
    if len(aa) != 2 or len(bb) != 2 or cells != set(product(aa, bb)):
        return "NOT_RECTANGLE"
    if star in cells:
        return "STAR_IN_RECTANGLE"
    return None


def is_rectangle(cells):
    aa, bb = {a for a, _ in cells}, {b for _, b in cells}
    return len(aa) == len(bb) == 2 and set(cells) == set(product(aa, bb))


def absent_split_reason(main_rows, groups):
    for axis in (0, 1):
        absent = set(range(4)) - {divmod(e, 4)[axis] for e in main_rows}
        for symbol in absent:
            occupied = [i for i, group in enumerate(groups)
                        if any(divmod(e, 4)[axis] == symbol for e in group)]
            if len(occupied) != 1:
                return "ABSENT_Q4_SPLIT"
    return None


def absent_degree_reason(main_rows, row_groups, col_groups):
    for axis in (0, 1):
        absent = set(range(4)) - {divmod(e, 4)[axis] for e in main_rows}
        for symbol in absent:
            group = next(i for i, rows in enumerate(row_groups)
                         if any(divmod(e, 4)[axis] == symbol for e in rows))
            cols = col_groups[group]
            if len({a for a, _ in cols}) != 2 or len({b for _, b in cols}) != 2:
                return "ABSENT_Q4_ACTUAL_DEGREE"
    return None


def degree_reason(words, star):
    """Common partner degrees, cross-pair multiplicities and five-cube rule."""
    ac, ad, bc, bd = ([0] * 12 for _ in range(4))
    sa, sb, sc, sd = ([0] * n for n in (3, 3, 4, 4))
    for a, b, c, d in words:
        sa[a] += 1; sb[b] += 1; sc[c] += 1; sd[d] += 1
        ac[4 * a + c] += 1; ad[4 * a + d] += 1
        bc[4 * b + c] += 1; bd[4 * b + d] += 1
    for a in range(3):
        degree = 2 if a == star[0] else 3
        if sum(x > 0 for x in ac[4*a:4*a+4]) != degree:
            return "DEG_A_C"
        if sum(x > 0 for x in ad[4*a:4*a+4]) != degree:
            return "DEG_A_D"
    for b in range(3):
        degree = 2 if b == star[1] else 3
        if sum(x > 0 for x in bc[4*b:4*b+4]) != degree:
            return "DEG_B_C"
        if sum(x > 0 for x in bd[4*b:4*b+4]) != degree:
            return "DEG_B_D"
    for c in range(4):
        if sum(ac[4*a+c] > 0 for a in range(3)) != 2:
            return "DEG_C_A"
        if sum(bc[4*b+c] > 0 for b in range(3)) != 2:
            return "DEG_C_B"
    for d in range(4):
        if sum(ad[4*a+d] > 0 for a in range(3)) != 2:
            return "DEG_D_A"
        if sum(bd[4*b+d] > 0 for b in range(3)) != 2:
            return "DEG_D_B"
    if sc != [7, 6, 4, 4] or sd != [7, 6, 4, 4]:
        return "Q4_SLICE_SIZE"
    if sa[star[0]] == 5 or sb[star[1]] == 5:
        return "FIVE_VERTEX_CUBE"
    target_a = (2, 2, 2, 2, 3, 3, 3, 4)
    target_b = (2, 2, 2, 2, 2, 3, 4, 4)
    types = []
    for counts in (ac, ad, bc, bd):
        multiplicities = tuple(sorted(x for x in counts if x))
        if multiplicities == target_a:
            types.append("A")
        elif multiplicities == target_b:
            types.append("B")
        else:
            return "CROSS_PAIR_MULTIPLICITIES"
    if types[0] != types[3] or types[1] != types[2]:
        return "CROSS_CUT_MATCHED_TYPES"
    return None


def other_cut_reason(words):
    # Same 21 E words, but only necessary combinatorial component tests;
    # there is no phase, P-set or quantum-tensor search here.
    for i, j, k, l in ((0, 2, 1, 3), (0, 3, 1, 2)):
        rows, cols = {}, {}
        for word in words:
            row, col = (word[i], word[j]), (word[k], word[l])
            rows.setdefault(row, set()).add(col)
            cols.setdefault(col, set()).add(row)
        if len(rows) != 8 or len(cols) != 8:
            return "OTHER_CUT_LINE_COUNT"
        for lines in (list(rows.values()), list(cols.values())):
            for u, v in combinations(lines, 2):
                if len(u & v) == 1:
                    return "OTHER_CUT_ONE_OVERLAP"
        unseen = {(0, x) for x in rows} | {(1, x) for x in cols}
        components = []
        while unseen:
            stack = [next(iter(unseen))]
            seen = set()
            while stack:
                node = stack.pop()
                if node in seen:
                    continue
                seen.add(node)
                side, key = node
                adjacent = rows[key] if side == 0 else cols[key]
                stack.extend((1 - side, x) for x in adjacent if (1 - side, x) not in seen)
            unseen.difference_update(seen)
            rr = [key for side, key in seen if side == 0]
            cc = [key for side, key in seen if side == 1]
            edge_count = sum(len(rows[key]) for key in rr)
            components.append((len(rr), len(cc), edge_count))
        if sorted(components) != [(2, 2, 4), (2, 2, 4), (4, 4, 13)]:
            return "OTHER_CUT_COMPONENTS"
    return None


def three_three_four_four(supports, models):
    grid = set(product(range(3), repeat=2))
    rectangles = [frozenset(product(a, b)) for a in combinations(range(3), 2)
                  for b in combinations(range(3), 2)]
    by_rows = {}
    for mask in supports:
        degrees = tuple(((mask >> (4*i)) & 15).bit_count() for i in range(4))
        by_rows.setdefault(degrees, []).append(mask)
    require(rectangle_reason((2, 1), {(0, 0), (0, 1), (1, 0), (2, 2)}) == "NOT_RECTANGLE",
            "MUTANT_RECTANGLE_REASON")
    require(absent_split_reason((0, 1, 4, 5), ((10, 11), (14, 15))) == "ABSENT_Q4_SPLIT",
            "MUTANT_SPLIT_REASON")
    # Fabricated one-cut incidence mutant: star A=0 sees only C=2 in its
    # low rows.  It is NOT asserted to satisfy any other premise.
    rmut = [(1, 1), (1, 2), (2, 1), (2, 2)]
    mainmask = 0xffff ^ ((1 << 4) | (1 << 9) | (1 << 14))
    mutant_words = [(a, b, *divmod(e, 4)) for row, e in enumerate((0, 1, 4, 5))
                    for col, (a, b) in enumerate(rmut) if mainmask & (1 << (4*row+col))]
    mutant_words += [(a, b, *divmod(e, 4)) for e in (10, 11) for a, b in ((0, 1), (0, 2))]
    mutant_words += [(a, b, *divmod(e, 4)) for e in (14, 15) for a, b in ((1, 0), (2, 0))]
    require(degree_reason(mutant_words, (0, 0)) == "DEG_A_C", "MUTANT_ACTUAL_DEGREE")
    counters = Counter()
    rejected = Counter()
    survivors = []
    for star in sorted(grid):
        for rect in rectangles:
            if rectangle_reason(star, rect) is not None:
                continue
            tick()
            outside = sorted(grid - {star} - set(rect))
            require(len(outside) == 4 and not is_rectangle(outside),
                    "OUTSIDE_L_RECTANGLE", [star, sorted(rect), outside])
            counters["star_rectangle_pairs"] += 1
            columns = sorted(rect)
            for model in models:
                edges = model["edges"]
                core = (0, 1, 4)  # TT, TS, ST, with their actual weighted degrees
                require(all(e in edges for e in core), "HIGH_CORE_ABSENT")
                for extra in sorted(edges - set(core)):
                    main = core + (extra,)
                    row_degrees = tuple(2 + weight_of(model["weights"], e) for e in main)
                    masks = by_rows.get(row_degrees, ())
                    counters["extra_row_choices"] += 1
                    if not masks:
                        counters["extra_row_without_compatible_13_support"] += 1
                        continue
                    low_rows = sorted(edges - set(main))
                    for row_groups in partitions4(low_rows):
                        tick()
                        reason = absent_split_reason(main, row_groups)
                        if reason:
                            amount = 6 * len(masks)
                            counters["complete_labeled_assignments"] += amount
                            rejected[reason] += amount
                            continue
                        for col_partition in partitions4(outside):
                            for flip in (0, 1):
                                col_groups = (col_partition[flip], col_partition[1-flip])
                                counters["complete_labeled_assignments"] += len(masks)
                                reason = absent_degree_reason(main, row_groups, col_groups)
                                if reason:
                                    rejected[reason] += len(masks)
                                    continue
                                low_words = [(a, b, *divmod(edge, 4))
                                             for grp in range(2) for edge in row_groups[grp]
                                             for a, b in col_groups[grp]]
                                for mask in masks:
                                    words = low_words + [(a, b, *divmod(edge, 4))
                                        for row, edge in enumerate(main)
                                        for col, (a, b) in enumerate(columns)
                                        if mask & (1 << (4*row+col))]
                                    require(len(words) == len(set(words)) == 21, "LOCAL_WORD_IDENTITY")
                                    reason = degree_reason(words, star)
                                    if reason is None:
                                        reason = other_cut_reason(words)
                                    if reason:
                                        rejected[reason] += 1
                                    else:
                                        counters["necessary_incidence_survivors"] += 1
                                        if len(survivors) < 3:
                                            survivors.append({"star": list(star), "R": columns,
                                                "pair_type": model["type"], "H": model["H"],
                                                "main_rows": list(main), "support_mask": mask,
                                                "low_row_groups": row_groups, "low_column_groups": col_groups,
                                                "E_words_only_not_a_witness": sorted(words)})
    require(counters["star_rectangle_pairs"] == 45, "STAR_RECTANGLE_COVERAGE")
    require(sum(rejected.values()) + counters["necessary_incidence_survivors"] ==
            counters["complete_labeled_assignments"], "ASSIGNMENT_ACCOUNTING")
    return {"coverage": dict(counters), "rejected_by_first_necessary_reason": dict(rejected),
            "first_survivors_if_any": survivors,
            "mutants": {"not_rectangle": "NOT_RECTANGLE", "absent_split": "ABSENT_Q4_SPLIT",
                        "star_partner_degree": "DEG_A_C"},
            "boundary": "necessary E-incidence constraints; no phases or P completions"}


def low_mask_reason(mask):
    if mask < 0 or mask >> 8:
        return "LOW_MASK_SHAPE"
    for axis in range(3):
        for bit in (0, 1):
            count = sum(1 for v in range(8) if mask & (1 << v) and ((v >> axis) & 1) == bit)
            if count not in (0, 2):
                return "LOW_PAIR_MULTIPLICITY"
    return None


def high_partner_reason(n, degree):
    if n not in (0, 2, 4):
        return "N_OUT_OF_RANGE"
    high = degree - n // 2
    if high < 0 or high > 2:
        return "PARTNER_CAPACITY"
    if high == 1:
        return "SINGLE_HIGH_WORD"
    return None


def sector_reason(words):
    if len(words) != 13 or len(set(words)) != 13:
        return "SECTOR_SIZE"
    for axis in (1, 2, 3):
        if sum(word[axis] == 0 for word in words) != 7:
            return "T_S_OCCURRENCE"
    types = []
    for i, j in ((1, 2), (1, 3), (2, 3)):
        counts = tuple(sum(word[i] == a and word[j] == b for word in words)
                       for a in (0, 1) for b in (0, 1))
        if counts == (4, 3, 3, 3):
            types.append("A")
        elif counts == (3, 4, 4, 2):
            types.append("B")
        else:
            return "Q4_HIGH_PAIR_WEIGHTS"
    if types.count("B") == 3:
        return "S6_ALL_THREE_B"
    for i, j, k, l in ((0, 1, 2, 3), (0, 2, 1, 3), (0, 3, 1, 2)):
        mask = sum(1 << (4 * (2*word[i] + word[j]) + 2*word[k] + word[l]) for word in words)
        reason = support_reason(mask)
        if reason is not None:
            return "SECTOR_CUT_" + reason
    return None


def low_sectors(degrees, n_values, options):
    # Every q4-low/other-symbol E pair is exactly a two-word line.
    # In particular no two DISTINCT binary triples can realize n_a=2.
    feasible = 0
    for masks in product(*(options[n] for n in n_values)):
        valid = True
        for i, j in ((0, 1), (0, 2), (1, 2)):
            counts = [0] * 4
            for mask in masks:
                for v in bits(mask, 8):
                    counts[2*((v >> i) & 1) + ((v >> j) & 1)] += 1
            if counts != [2, 2, 2, 2]:
                valid = False
                break
        if valid:
            feasible += 1
    return feasible


def three_four_four_four(models):
    options = {}
    for n in (0, 2, 4):
        options[n] = [sum(1 << v for v in choice) for choice in combinations(range(8), n)
                      if low_mask_reason(sum(1 << v for v in choice)) is None]
    require(not options[2], "N2_LOW_SECTOR_COUNTEREXAMPLE")
    require(low_mask_reason((1 << 0) | (1 << 1)) == "LOW_PAIR_MULTIPLICITY",
            "MUTANT_LOW_PAIR")
    require(high_partner_reason(4, 3) == "SINGLE_HIGH_WORD", "MUTANT_SINGLE_HIGH")
    bad_sector = list(product(range(2), repeat=4))[3:]
    require(sector_reason(bad_sector) == "T_S_OCCURRENCE", "MUTANT_SECTOR_COUNT")
    profiles = []
    low_feasible_profiles = []
    for degrees in sorted(set(permutations((2, 2, 4))) | set(permutations((2, 3, 3)))):
        for n_values in product((0, 2, 4), repeat=3):
            if sum(n_values) != 8:
                continue
            reasons = [high_partner_reason(n, d) for n, d in zip(n_values, degrees)]
            low_count = low_sectors(degrees, n_values, options)
            feasible = low_count > 0 and all(reason is None for reason in reasons)
            record = {"degrees": list(degrees), "n": list(n_values),
                      "high_partner_reasons": reasons, "low_supports": low_count,
                      "necessary_feasible": feasible}
            profiles.append(record)
            if feasible:
                active = [i for i, (n, d) in enumerate(zip(n_values, degrees)) if d - n//2 == 2]
                require(len(active) == 2, "HIGH_SECTOR_NOT_TWO_A_SYMBOLS", record)
                record["active_high_A_symbols"] = active
                low_feasible_profiles.append(record)
    require(low_feasible_profiles, "NO_ABSTRACT_LOW_PROFILE")
    sector_reasons = Counter()
    sector_types = Counter()
    sector_survivors = []
    vertices = list(product(range(2), repeat=4))
    for missing in combinations(range(16), 3):
        words = [vertices[i] for i in range(16) if i not in missing]
        reason = sector_reason(words)
        if reason:
            sector_reasons[reason] += 1
        else:
            types = []
            for i, j in ((1, 2), (1, 3), (2, 3)):
                counts = tuple(sum(w[i] == a and w[j] == b for w in words)
                               for a in (0, 1) for b in (0, 1))
                types.append("A" if counts == (4, 3, 3, 3) else "B")
            sector_types["".join(types)] += 1
            if len(sector_survivors) < 3:
                sector_survivors.append(words)
    require(sum(sector_reasons.values()) + sum(sector_types.values()) == 560,
            "BINARY_SECTOR_COVERAGE")
    # All six labeled q4-pair models are used on the three distinct cuts.
    tri_edges = ((0, 1), (0, 2), (1, 2))
    cases = Counter()
    for choices in product(models, repeat=3):
        tick()
        if sum(m["type"] == "B" for m in choices) > 2:
            continue
        h = [e for e, m in zip(tri_edges, choices) if m["H"]]
        cases["H" + str(len(h))] += 1
        if len(h) == 1:
            statuses = [s for s in product((0, 1), repeat=3)
                        if all(s[a] == s[b] for (a, b), model in zip(tri_edges, choices)
                               if not model["H"])]
            for (a, b), model in zip(tri_edges, choices):
                if not model["H"]:
                    continue
                cross = [(x // 4, x % 4) for x in model["edges"]
                         if (x // 4 < 2) != (x % 4 < 2)]
                require(len(cross) == 2, "H_CROSS_EDGES")
                for u, v in cross:
                    require(not any(s[a] == (u >= 2) and s[b] == (v >= 2)
                                    for s in statuses), "H1_SYNCHRONIZATION_COUNTEREXAMPLE")
        elif len(h) == 2:
            center = next(x for x in range(3) if sum(x in edge for edge in h) == 2)
            leaves = [x for x in range(3) if x != center]
            leaf_index = tri_edges.index(tuple(leaves))
            require(not choices[leaf_index]["H"], "H2_LEAVES_NOT_SYNCHRONIZED")
            for leaf in leaves:
                edge = tuple(sorted((center, leaf)))
                model = choices[tri_edges.index(edge)]
                row = [(divmod(e, 4), 2 + weight_of(model["weights"], e))
                       for e in model["edges"]]
                projected = [(pair[1] if center == edge[0] else pair[0], mult)
                             for pair, mult in row
                             if pair[0 if center == edge[0] else 1] == 1]
                require(sorted(projected, key=lambda x: x[0]) in ([(0, 4), (2, 2)], [(0, 4), (3, 2)]),
                        "H2_CENTRAL_S_PAIR", projected)
            # Each two-word low event is exactly the same set by leaf status
            # synchronization; the other four words have fixed (S,T,T),
            # but the q3 coordinate has only three symbols.
            require(4 > 3, "H2_FIXED_TRIPLE_CAPACITY")
        else:
            require(len(h) == 0, "THREE_B_CUTS_OR_H_EDGES")
    return {"low_mask_option_counts": {str(n): len(options[n]) for n in options},
            "all_degree_n_profiles": profiles, "low_feasible_profiles": low_feasible_profiles,
            "closed_binary_sector_13_supports_examined": 560,
            "sector_rejections": dict(sector_reasons), "sector_survivor_types": dict(sector_types),
            "first_sector_survivors_if_any_not_phase_witnesses": sector_survivors,
            "labeled_highpair_graph_scenarios_by_H": dict(cases),
            "mutants": {"two_distinct_low_words": "LOW_PAIR_MULTIPLICITY",
                        "degree3_n4": "SINGLE_HIGH_WORD", "bad_sector": "T_S_OCCURRENCE"},
            "boundary": "H=0 closure uses the separately reviewed no-four-qubit-AME lemma; "
                        "sector supports are necessary only and do not certify phases"}


def main():
    signal.signal(signal.SIGINT, on_signal)
    signal.signal(signal.SIGTERM, on_signal)
    output = {"status": "INCOMPLETE", "scope": "LOCAL_N49_T28_NECESSARY_PRIMITIVES_ONLY",
              "not_established": ["global t bound", "universal phase feasibility", "AME witness",
                                  "global minimum 50", "source identity", "novelty", "parent adoption"],
              "internal_deadline_seconds": 45, "external_ceiling_seconds": 55}
    try:
        tick()
        supports, output["support_4x4"] = support_and_control()
        tick()
        output["cube_slices"] = cube_checks()
        tick()
        models, output["high_pair_graphs"] = pair_models()
        tick()
        output["profile_4444"] = four_four_four_four()
        tick()
        output["profile_3444"] = three_four_four_four(models)
        tick()
        output["profile_3344"] = three_three_four_four(supports, models)
        tick()
        output["status"] = "COMPLETE_LOCAL_ENUMERATION_NOT_GLOBAL_PROOF"
        output["elapsed_seconds"] = round(time.monotonic() - START, 6)
        print(json.dumps(output, sort_keys=True, separators=(",", ":")), flush=True)
        return 0
    except Stop as error:
        output["status"] = "INCOMPLETE"
        output["reason"] = str(error)
        output["elapsed_seconds"] = round(time.monotonic() - START, 6)
        print(json.dumps(output, sort_keys=True, separators=(",", ":")), flush=True)
        return 3
    except Finding as error:
        output["status"] = "FINDING_OR_SOURCE_DEFECT_NOT_PASS"
        output["rule"] = error.rule
        output["detail"] = error.detail
        output["elapsed_seconds"] = round(time.monotonic() - START, 6)
        print(json.dumps(output, sort_keys=True, separators=(",", ":")), flush=True)
        return 2
    except Exception as error:
        output["status"] = "INCOMPLETE_SOURCE_ERROR"
        output["exception"] = type(error).__name__
        output["message"] = str(error)
        output["elapsed_seconds"] = round(time.monotonic() - START, 6)
        print(json.dumps(output, sort_keys=True, separators=(",", ":")), flush=True)
        return 4


if __name__ == "__main__":
    sys.exit(main())

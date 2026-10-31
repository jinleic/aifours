#!/usr/bin/env python3
"""F554 independent bounded necessary-interface checker. CHILD STATUS: NOT RUN.

Fixed argv: python3 -B -I f554-independent-finite-v1.py
Standard library only; no file reads/writes, network, subprocesses, randomness,
packages, or search for a joint eleven-row array. Only final stdout is emitted.
The cooperative limit is 55 seconds; an incomplete run is never a PASS.

Domain: all 92,400 cell words beginning at infinity in cell L, with remaining
finite multiplicities (I,J,K,L)=(3,3,3,2). Each word is lifted to an actual
permutation of eleven finite vertices; its augmented TWELVE-vertex Hamilton
cycle and directed square are built before metrics are projected to cells.
Deterministic lifts represent cell words, NOT all labeled Hamilton cycles.
All schedule enumeration is explicitly a NECESSARY projection, not an array.
"""

import itertools
import json
import time
from collections import Counter

I, J, K, L = range(4)
NAMES = ("I", "J", "K", "L")
VERTICES = tuple(range(12))
CELLS = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (0, 10, 11))
CELL = {v: q for q, vertices in enumerate(CELLS) for v in vertices}
B = frozenset(CELLS[I] + CELLS[J])
D = frozenset(CELLS[I] + CELLS[K])
E = frozenset(CELLS[J] + CELLS[K])
OPPOSITE = ((I, L), (L, I), (J, K), (K, J))
SQUARE_EDGES = (3, 10, 12, 5)  # IJ, JL, LK, KI as full-cell bit masks.
SOURCE_ROWS = {
    "f4": (10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9),
    "f2": (10, 1, 2, 3, 7, 11, 4, 5, 6, 8, 9),
    "f0": (10, 4, 3, 7, 11, 5, 6, 8, 9, 1, 2),
    "hE": (4, 1, 7, 10, 5, 2, 8, 11, 6, 3, 9),
}
START = time.monotonic()


class CheckFailure(Exception):
    def __init__(self, reason):
        self.reason = reason
        super().__init__(reason)


def need(condition, reason):
    if not condition:
        raise CheckFailure(reason)


def deadline():
    need(time.monotonic() - START < 55.0, "INCOMPLETE_DEADLINE_55_SECONDS")


def permutation_orbits(successor):
    need(set(successor) == set(VERTICES), "SUCCESSOR_DOMAIN")
    need(set(successor.values()) == set(VERTICES), "SUCCESSOR_BIJECTION")
    unseen = set(VERTICES)
    result = []
    while unseen:
        start = min(unseen)
        orbit = []
        v = start
        while v not in orbit:
            need(v in unseen, "SUCCESSOR_COMPONENT_COLLISION")
            orbit.append(v)
            v = successor[v]
        need(v == start, "SUCCESSOR_NOT_A_CYCLE")
        unseen.difference_update(orbit)
        result.append(tuple(orbit))
    return tuple(result)


def require_hamilton(successor):
    orbits = permutation_orbits(successor)
    need(len(orbits) == 1 and len(orbits[0]) == 12,
         "DISCONNECTED_SUCCESSOR")
    return orbits[0]


def explicit_square_from_linear_row(row):
    # A square of the augmented cycle is NOT the square of an 11-cycle.
    return frozenset(
        [(row[i], row[i + 2]) for i in range(9)]
        + [(row[-1], row[0]), (0, row[1]), (row[-2], 0)]
    )


def validate_square(row, square):
    need(square == explicit_square_from_linear_row(row), "C2_EVENT_SET")


def actual_cycle(row):
    row = tuple(row)
    need(len(row) == 11 and set(row) == set(range(1, 12)),
         "NOT_ELEVEN_DISTINCT_FINITE_VERTICES")
    h = (0,) + row
    successor = {h[i]: h[(i + 1) % 12] for i in range(12)}
    require_hamilton(successor)
    arcs = frozenset(successor.items())
    square_successor = {v: successor[successor[v]] for v in VERTICES}
    square = frozenset(square_successor.items())
    validate_square(row, square)
    need(sorted(map(len, permutation_orbits(square_successor))) == [6, 6],
         "C2_NOT_TWO_DERIVED_SIX_CYCLES")
    return row, h, arcs, square


def singleton_vertices(h, cut):
    return frozenset(
        v for i, v in enumerate(h)
        if (h[i - 1] in cut) == (h[(i + 1) % 12] in cut)
        and (v in cut) != (h[i - 1] in cut)
    )


def projection(cycle):
    row, h, arcs, square = cycle
    # These cell metrics consume actual directed arc sets, not a free ledger.
    cell_word = tuple(CELL[v] for v in h)
    adj = Counter((CELL[a], CELL[b]) for a, b in arcs)
    sq = Counter((CELL[a], CELL[b]) for a, b in square)
    layouts = []
    for q in range(4):
        lengths = []
        for i in range(12):
            if cell_word[i] == q and cell_word[i - 1] != q:
                length = 1
                while cell_word[(i + length) % 12] == q:
                    length += 1
                lengths.append(length)
        key = tuple(sorted(lengths))
        need(key in ((3,), (1, 2), (1, 1, 1)), "UNKNOWN_CELL_RUN_LAYOUT")
        layouts.append({(3,): "F", (1, 2): "P", (1, 1, 1): "Q"}[key])
    single = {
        "B": singleton_vertices(h, B),
        "D": singleton_vertices(h, D),
        "E": singleton_vertices(h, E),
    }
    diag = tuple(adj[pair] for pair in OPPOSITE)
    sqdiag = tuple(sq[pair] for pair in OPPOSITE)
    cross_e = sum((a in E) != (b in E) for a, b in arcs)
    square_cross_e = sum((a in E) != (b in E) for a, b in square)
    fullmask = sum(1 << q for q in range(4) if layouts[q] == "F")
    return {
        "row": row, "h": h, "arcs": arcs, "square": square,
        "word": cell_word, "adj": adj, "sq": sq,
        "layouts": tuple(layouts), "single": single,
        "diag": diag, "sqdiag": sqdiag, "fullmask": fullmask,
        "cross_e": cross_e, "square_cross_e": square_cross_e,
    }


def opposite_join_counts(m):
    return m["diag"][0] + m["diag"][1], m["diag"][2] + m["diag"][3]


def check_fullmask(mask):
    n_il = bool(mask & (1 << I)) + bool(mask & (1 << L))
    n_jk = bool(mask & (1 << J)) + bool(mask & (1 << K))
    need(n_il == n_jk, "FULL_CELL_E_SIDE_BALANCE")


def check_residual(m):
    need(not m["single"]["B"] and not m["single"]["D"],
         "RESIDUAL_ORIGINAL_CUT_SINGLETON")
    d_il, d_jk = opposite_join_counts(m)
    need(d_il <= 1 and d_jk <= 1, "OPPOSITE_JOIN_CAPACITY")
    for q in range(4):
        need(m["sq"][(q, q)] == int(m["layouts"][q] == "F"),
             "INTERNAL_C2_FULL_RUN_IDENTITY")
    h = m["h"]
    for k, (left, right) in enumerate(OPPOSITE):
        third_cells = {I, J, K, L} - {left, right}
        centered = sum(
            CELL[h[i - 1]] == left
            and CELL[h[(i + 1) % 12]] == right
            and CELL[h[i]] in third_cells
            for i in range(12)
        )
        need(m["sqdiag"][k] == 2 * m["diag"][k] + centered,
             "DIRECTED_DIAGONAL_C2_IDENTITY")
    if d_il == d_jk == 1:
        need("Q" not in m["layouts"], "REGULAR_ALL_SINGLETON_CELL")
        check_fullmask(m["fullmask"])
        f = m["fullmask"].bit_count()
        need(m["cross_e"] == 6 - f, "REGULAR_E_CROSS_COUNT")
        need(len(m["single"]["E"]) == 4 - f,
             "REGULAR_E_SINGLETON_COUNT")
        need(m["square_cross_e"] == 4,
             "REGULAR_E_SQUARE_CROSS_COUNT")
    if m["layouts"] == ("Q",) * 4:
        need(d_il == d_jk == 0 and m["cross_e"] == 12,
             "ALL_Q_NOT_E_ALTERNATING")
        cycle_order = (I, J, L, K)
        position = {q: i for i, q in enumerate(cycle_order)}
        signs = {
            (position[m["word"][(i + 1) % 12]]
             - position[m["word"][i]]) % 4
            for i in range(12)
        }
        need(signs in ({1}, {3}), "ALL_Q_CELL_ORIENTATION")
        need(m["sqdiag"] in ((3, 3, 3, 3),), "ALL_Q_C2_DIAGONALS")


def finite_cell_words():
    counts = [3, 3, 3, 2]
    prefix = [L]  # infinity has already occupied one L position.

    def extend():
        if len(prefix) == 12:
            yield tuple(prefix)
            return
        for q in range(4):
            if counts[q]:
                counts[q] -= 1
                prefix.append(q)
                yield from extend()
                prefix.pop()
                counts[q] += 1

    yield from extend()


def lift_cell_word(word):
    finite = (iter(CELLS[I]), iter(CELLS[J]), iter(CELLS[K]), iter((10, 11)))
    return tuple(next(finite[q]) for q in word[1:])


def check_alternating_family_row(m, family):
    own, other = (B, D) if family == "B" else (D, B)
    need(len(singleton_vertices(m["h"], own)) == 12,
         "NOT_ALTERNATING_FAMILY_ROW")
    need(not singleton_vertices(m["h"], other),
         "OTHER_CUT_SINGLETON_IN_ALTERNATING_FAMILY")
    changes = sum((a in other) != (b in other) for a, b in m["arcs"])
    need(changes % 2 == 0, "ODD_CUT_BOUNDARY")
    j = changes // 2
    need(1 <= j <= 3, "OTHER_CUT_RUN_RANGE")
    x, y, jk, kj = m["diag"]
    need(x + y == j, "FAMILY_DIAGONAL_RUN_SUM")
    need((jk, kj) == ((x, y) if family == "B" else (y, x)),
         "FAMILY_DIRECTED_CELL_BALANCE")
    need(not any(m["sqdiag"]), "ALTERNATING_OPPOSITE_C2_EVENT")
    for q in range(4):
        need(m["sq"][(q, q)] == 3 - j, "ALTERNATING_INTERNAL_C2_COUNT")
    if j == 3:
        need((x, y) in ((3, 0), (0, 3)), "RUN_THREE_ORIENTATION")
    return j, x, y


def expect_reason(function, reason):
    try:
        function()
    except CheckFailure as error:
        need(error.reason == reason, "MUTANT_REJECTED_FOR_WRONG_REASON")
        return
    raise CheckFailure("MUTANT_NOT_REJECTED")


def check_local_layout_columns(rows, t):
    metrics = [projection(actual_cycle(row)) for row in rows]
    need(len(metrics) == 5, "NOT_FIVE_RESIDUAL_CYCLES")
    target = Counter({"F": t - 12, "P": 30 - 2 * t, "Q": t - 13})
    target += Counter()  # discard zero entries for Counter equality.
    for q in range(4):
        need(Counter(m["layouts"][q] for m in metrics) == target,
             "LOCAL_CELL_LAYOUT_TABLE")
    return metrics


def check_necessary_joint_projection(rows, t):
    metrics = check_local_layout_columns(rows, t)
    for m in metrics:
        check_residual(m)
    sums = tuple(sum(opposite_join_counts(m)[k] for m in metrics)
                 for k in range(2))
    need(sums == (18 - t, 18 - t), "OPPOSITE_JOIN_BUDGET")
    if t == 14:
        q_slots = [next(i for i, m in enumerate(metrics)
                        if m["layouts"][q] == "Q") for q in range(4)]
        need(len(set(q_slots)) == 1, "ALL_SINGLETON_CYCLE_SYNCHRONIZATION")
    return metrics


def rotate_to_infinity(h):
    k = h.index(0)
    normalized = tuple(h[k:]) + tuple(h[:k])
    return normalized[1:]


def row_from_paths(word, cell_paths):
    assignment = [None] * 12
    for q in range(4):
        starts = [i for i in range(12)
                  if word[i] == q and word[i - 1] != q
                  and word[(i + 1) % 12] == q]
        need(len(starts) == 1, "FIXTURE_NONTRIVIAL_RUN")
        start = starts[0]
        path = tuple(cell_paths[q])
        need(len(path) in (2, 3), "FIXTURE_PATH_LENGTH")
        for j, v in enumerate(path):
            assignment[(start + j) % 12] = v
        remaining = set(CELLS[q]) - set(path)
        unfilled = [i for i in range(12) if word[i] == q
                    and assignment[i] is None]
        need(len(unfilled) == len(remaining), "FIXTURE_VERTEX_ASSIGNMENT")
        for i, v in zip(unfilled, sorted(remaining)):
            assignment[i] = v
    need(all(v is not None for v in assignment), "FIXTURE_UNFILLED_VERTEX")
    return rotate_to_infinity(tuple(assignment))


def internal_cover_fixture(t):
    full_word = projection(actual_cycle(SOURCE_ROWS["f4"]))["word"]
    pair_word = projection(actual_cycle(SOURCE_ROWS["f0"]))["word"]
    full_paths = {q: [tuple(CELLS[q])] for q in range(4)}
    if t == 14:
        for q in range(4):
            a, b, c = CELLS[q]
            full_paths[q].append((b, a, c))
    full_count = t - 12
    rows = [row_from_paths(full_word, {q: full_paths[q][k] for q in range(4)})
            for k in range(full_count)]
    remaining = {}
    for q in range(4):
        used = {(a, b) for path in full_paths[q]
                for a, b in zip(path, path[1:])}
        remaining[q] = sorted(set(itertools.permutations(CELLS[q], 2)) - used)
    pair_count = 6 - 2 * full_count
    need(all(len(remaining[q]) == pair_count for q in range(4)),
         "FIXTURE_INTERNAL_ARC_REMAINDER")
    rows.extend(row_from_paths(pair_word, {q: remaining[q][k] for q in range(4)})
                for k in range(pair_count))
    if t == 14:
        rows.append(SOURCE_ROWS["hE"])
    return tuple(rows)


def vertex_packet(rows):
    metrics = [projection(actual_cycle(row)) for row in rows]
    internal = Counter()
    singles = Counter()
    middles = Counter()
    for m in metrics:
        internal.update((a, b) for a, b in m["arcs"] if CELL[a] == CELL[b])
        h = m["h"]
        for i, v in enumerate(h):
            before = CELL[h[i - 1]] == CELL[v]
            after = CELL[h[(i + 1) % 12]] == CELL[v]
            if not before and not after:
                singles[v] += 1
            if before and after:
                middles[v] += 1
    universe = Counter((a, b) for cell in CELLS
                       for a, b in itertools.permutations(cell, 2))
    need(internal == universe, "INTERNAL_DIRECTED_ARC_PARTITION")
    need(len(rows) == 5, "VERTEX_LEDGER_NOT_FIVE_CYCLES")
    for v in VERTICES:
        need(singles[v] == 1 + middles[v], "VERTEX_SINGLE_MIDDLE_IDENTITY")
    return {"binding": tuple(tuple(row) for row in rows),
            "singles": singles, "middles": middles}


def bind_vertex_packets(single_packet, middle_packet):
    need(single_packet["binding"] == middle_packet["binding"],
         "VERTEX_LEDGER_CYCLE_IDENTITY")
    for v in VERTICES:
        need(single_packet["singles"][v] == 1 + middle_packet["middles"][v],
             "VERTEX_SINGLE_MIDDLE_IDENTITY")


def relabel_within_cells(rows):
    mapping = {}
    for cell in CELLS:
        for i, v in enumerate(cell):
            mapping[v] = cell[(i + 1) % 3]
    return tuple(rotate_to_infinity(tuple(mapping[v] for v in (0,) + row))
                 for row in rows)


def verify_actual_array(rows, assume_mc):
    # Reusable direct validator. It is NOT a search and has NO supplied
    # eleven-row witness. Calling it on an unverified projection is forbidden.
    need(len(rows) == 11, "NOT_ELEVEN_ACTUAL_ROWS")
    cycles = [actual_cycle(row) for row in rows]
    finite_universe = Counter(itertools.permutations(range(1, 12), 2))
    adjacency = Counter((row[i], row[i + 1])
                        for row in rows for i in range(10))
    need(adjacency == finite_universe, "ORIGINAL_ADJACENCY_NOT_EXHAUSTED")
    distance = Counter((row[i], row[i + 2])
                       for row in rows for i in range(9))
    need(all(count == 1 for count in distance.values()),
         "ORIGINAL_DISTANCE_TWO_COLLISION")
    missing = set(finite_universe) - set(distance)
    closing = Counter((row[-1], row[0]) for row in rows)
    need(all(count == 1 for count in closing.values()), "CLOSING_PAIR_COLLISION")
    if not assume_mc:
        # No unconditional square-partition import from merely being T2(11).
        return {"actual_T2": True, "M_equals_C": missing == set(closing),
                "square_partition_imported": False}
    need(missing == set(closing), "M_NOT_EQUAL_TO_C")
    universe = Counter(itertools.permutations(VERTICES, 2))
    need(Counter(edge for cycle in cycles for edge in cycle[2]) == universe,
         "AUGMENTED_ADJACENCY_PARTITION")
    need(Counter(edge for cycle in cycles for edge in cycle[3]) == universe,
         "AUGMENTED_SQUARE_PARTITION")
    return {"actual_T2": True, "M_equals_C": True,
            "square_partition_imported": True}


def enumerate_schedules(regular_masks, physical_signatures):
    allowed = tuple(sorted(regular_masks))
    q_assignments = 0
    capacity_survivors = 0
    physical_q_survivors = 0
    q_masks = {sum(1 << q for q, layout in enumerate(signature[0])
                   if layout == "Q") for signature in physical_signatures}
    for slots in itertools.product(range(5), repeat=4):
        q_assignments += 1
        cap_il = sum(i != slots[I] and i != slots[L] for i in range(5))
        cap_jk = sum(i != slots[J] and i != slots[K] for i in range(5))
        if min(cap_il, cap_jk) < 4:
            continue
        capacity_survivors += 1
        masks = [sum(1 << q for q in range(4) if slots[q] == i)
                 for i in range(5)]
        if all(mask in q_masks for mask in masks):
            physical_q_survivors += 1
            need(len(set(slots)) == 1, "T14_Q_NOT_SYNCHRONIZED")
    need((q_assignments, capacity_survivors, physical_q_survivors)
         == (625, 25, 5), "Q_ASSIGNMENT_COMPLETE_DOMAIN_COUNTS")
    result = {"q_slot_assignments": q_assignments,
              "diagonal_capacity_survivors": capacity_survivors,
              "physical_q_mask_survivors": physical_q_survivors}
    for t, row_count, incidence in ((13, 5, 1), (14, 4, 2)):
        counts = Counter()
        total = 0
        for masks in itertools.product(allowed, repeat=row_count):
            if any(sum(bool(mask & (1 << q)) for mask in masks) != incidence
                   for q in range(4)):
                continue
            total += 1
            sizes = tuple(sorted((mask.bit_count() for mask in masks), reverse=True))
            counts[str(sizes)] += 1
            if sizes == ((2, 2, 0, 0, 0) if t == 13 else (4, 2, 2, 0)):
                pairs = [mask for mask in masks if mask.bit_count() == 2]
                need(len(pairs) == 2 and pairs[0] ^ pairs[1] == 15,
                     "COMPLEMENTARY_EDGE_MATCHING")
            if t == 14 and sizes == (2, 2, 2, 2):
                edge_counts = [masks.count(edge) for edge in SQUARE_EDGES]
                need(edge_counts[0] == edge_counts[2]
                     and edge_counts[1] == edge_counts[3]
                     and edge_counts[0] + edge_counts[1] == 2,
                     "FOUR_EDGE_MULTIPLICITY")
        need(total == (45 if t == 13 else 90), "FULL_MASK_SCHEDULE_COUNT")
        result[str(t)] = {"regular_slot_schedules": total,
                          "full_count_patterns": dict(sorted(counts.items()))}
    result["14"]["including_five_hE_slot_positions"] = 450
    return result


def family_summaries(types):
    summaries = set()
    for members in itertools.product(sorted(types), repeat=3):
        js = tuple(sorted(member[0] for member in members))
        summaries.add((js, sum(member[0] for member in members),
                       sum(member[1] for member in members),
                       sum(member[2] for member in members)))
    return sorted(summaries)


def check_family_cross_bounds(b_types, d_types):
    run_pairs = {13: set(), 14: set()}
    accepted = Counter()
    for jb, rb, x, y in family_summaries(b_types):
        for jd, rd, u, v in family_summaries(d_types):
            t = rb + rd
            if t not in (13, 14):
                continue
            cs = (x + u, x + v, y + u, y + v)
            upper = max(cs) <= 8
            interval = all(t - 8 <= c <= 8 for c in cs)
            doubled = all(2 * t - 16 <= 2 * c <= 16 for c in cs)
            imbalance = abs(x - y) + abs(u - v) <= 16 - t
            need(upper == interval == doubled == imbalance,
                 "CROSS_BOUND_EQUIVALENCE")
            if not interval:
                continue
            residual = tuple(9 - c for c in cs)
            need(all(1 <= a <= 17 - t for a in residual),
                 "RESIDUAL_ORIENTATION_INTERVAL")
            need(residual[0] + residual[3] == 18 - t
                 and residual[1] + residual[2] == 18 - t,
                 "RESIDUAL_OPPOSITE_PAIR_BALANCE")
            accepted[str(t)] += 1
            run_pairs[t].add((rb, rd))
            if t == 14:
                need(rb != 9 and rd != 9, "T14_RUN_NINE_SURVIVES")
                if sorted(jb + jd) == [1, 1, 3, 3, 3, 3]:
                    need(jb == jd == (1, 3, 3), "RUN_ONE_FAMILY_SPLIT")
                    need(sorted((x, y)) == sorted((u, v)) == [3, 4],
                         "RUN_ONE_DIRECTED_TOTALS")
            if t == 13 and rb == 9:
                need(sorted((x, y)) == [3, 6] and (u, v) == (2, 2),
                     "T13_RUN_NINE_RESTRICTION")
            if t == 13 and rd == 9:
                need(sorted((u, v)) == [3, 6] and (x, y) == (2, 2),
                     "T13_RUN_NINE_RESTRICTION")
    need(run_pairs[14] == {(6, 8), (7, 7), (8, 6)},
         "T14_RUN_PAIR_NECESSARY_DOMAIN")
    return {"accepted_type_summary_pairs": dict(accepted),
            "run_pairs": {str(t): sorted(run_pairs[t]) for t in run_pairs},
            "normalization": "T-8 <= c <= 8; equivalently 2T-16 <= 2c <= 16"}


def controls(examples):
    result = {}
    for name, expected_f in (("f4", 4), ("f2", 2), ("f0", 0)):
        m = projection(actual_cycle(SOURCE_ROWS[name]))
        check_residual(m)
        need(opposite_join_counts(m) == (1, 1)
             and m["fullmask"].bit_count() == expected_f,
             "SOURCE_EXPLICIT_REGULAR_ROW")
    h_e = actual_cycle(SOURCE_ROWS["hE"])
    m_e = projection(h_e)
    check_residual(m_e)
    need(m_e["layouts"] == ("Q",) * 4, "SOURCE_EXPLICIT_ALL_Q_ROW")
    # A bijective successor is not automatically a Hamilton successor.
    h = h_e[1]
    bad_successor = {}
    for start in (0, 4, 8):
        block = h[start:start + 4]
        bad_successor.update({block[i]: block[(i + 1) % 4] for i in range(4)})
    need(len(permutation_orbits(bad_successor)) == 3,
         "DISCONNECTED_MUTANT_SETUP")
    expect_reason(lambda: require_hamilton(bad_successor), "DISCONNECTED_SUCCESSOR")
    degree_only_mutant_accepts = (
        set(bad_successor) == set(VERTICES)
        and set(bad_successor.values()) == set(VERTICES)
    )
    need(degree_only_mutant_accepts, "DISCONNECTED_MUTANT_NOT_DISCRIMINATING")
    result["disconnected_cover"] = {"status": "DISCRIMINATED",
        "reason": "DISCONNECTED_SUCCESSOR", "orbit_sizes": [4, 4, 4]}
    row, h, _, correct_square = actual_cycle(SOURCE_ROWS["f2"])
    reverse_square = frozenset((h[i], h[(i - 2) % 12]) for i in range(12))
    cyclic_eleven_square = frozenset(
        [(row[i], row[(i + 2) % 11]) for i in range(11)]
        + [(0, row[1]), (row[-2], 0)]
    )
    for name, mutant in (("C2_wrong_direction", reverse_square),
                         ("C2_wrong_eleven_vertex_wrap", cyclic_eleven_square)):
        expect_reason(lambda mutant=mutant: validate_square(row, mutant), "C2_EVENT_SET")
        need(mutant != correct_square, "C2_MUTANT_NOT_DISCRIMINATING")
        result[name] = {"status": "DISCRIMINATED", "reason": "C2_EVENT_SET",
                        "missing": sorted(correct_square - mutant),
                        "extra": sorted(mutant - correct_square)}
    # Actual individually valid Hamilton rows with deliberately incoherent Q slots.
    independent_rows = []
    for q in range(4):
        opposite = {I: L, L: I, J: K, K: J}[q]
        layout = tuple("Q" if r == q else "F" if r == opposite else "P"
                       for r in range(4))
        row_example = examples.get((layout, 0, 0))
        if row_example is None:
            independent_rows = []
            break
        independent_rows.append(row_example)
    if independent_rows:
        independent_rows.append(SOURCE_ROWS["f4"])
        check_local_layout_columns(independent_rows, 14)
        expect_reason(lambda: check_necessary_joint_projection(independent_rows, 14),
                      "OPPOSITE_JOIN_BUDGET")
        result["independent_per_cell_Q_slots"] = {
            "status": "DISCRIMINATED", "reason": "OPPOSITE_JOIN_BUDGET",
            "rows": independent_rows,
            "limit": "Five actual individual rows, NOT a compatible decomposition."}
    else:
        result["independent_per_cell_Q_slots"] = {
            "status": "NOTTESTED", "reason": "No intended physical fixture found."}
    wrong_masks = []
    for mask in range(16):
        even_only_mutant = mask.bit_count() in (0, 2, 4)
        try:
            check_fullmask(mask)
            correct = True
        except CheckFailure as error:
            need(error.reason == "FULL_CELL_E_SIDE_BALANCE", "FULL_MASK_WRONG_REASON")
            correct = False
        if even_only_mutant and not correct:
            wrong_masks.append(mask)
    need(wrong_masks == [6, 9], "FULL_MASK_MUTANT_DISCRIMINATION")
    result["wrong_full_cell_pair_balance"] = {
        "status": "DISCRIMINATED_INTERFACE_ONLY", "reason": "FULL_CELL_E_SIDE_BALANCE",
        "rejected_masks": wrong_masks,
        "physical_mutant_status": "NOTTESTED: these masks have no regular-row realization"}
    vertex_results = {}
    for t in (13, 14):
        rows = internal_cover_fixture(t)
        metrics = check_necessary_joint_projection(rows, t)
        packet = vertex_packet(rows)
        if t == 14:
            regular_rows = tuple(row for row, m in zip(rows, metrics)
                                 if m["layouts"] != ("Q",) * 4)
            for v in VERTICES:
                regular_single = sum(
                    CELL[h[i - 1]] != CELL[v]
                    and CELL[h[(i + 1) % 12]] != CELL[v]
                    for row in regular_rows
                    for h in [(0,) + row] for i in [h.index(v)]
                )
                need(regular_single == packet["middles"][v],
                     "T14_REGULAR_VERTEX_SINGLE_MIDDLE_IDENTITY")
        foreign = vertex_packet(relabel_within_cells(rows))
        expect_reason(lambda: bind_vertex_packets(packet, foreign),
                      "VERTEX_LEDGER_CYCLE_IDENTITY")
        mismatched = [v for v in VERTICES
                      if packet["singles"][v] != 1 + foreign["middles"][v]]
        need(bool(mismatched), "FOREIGN_VERTEX_LEDGER_NOT_DISCRIMINATING")
        # A cell-total-only mutant misses the per-vertex error.
        need(all(sum(packet["singles"][v] for v in cell)
                 == 3 + sum(foreign["middles"][v] for v in cell)
                 for cell in CELLS), "AGGREGATE_MUTANT_SETUP")
        vertex_results[str(t)] = {
            "rows": rows, "singles": dict(sorted(packet["singles"].items())),
            "middles": dict(sorted(packet["middles"].items())),
            "mixed_ledger_wrong_vertices": mismatched,
            "limit": "Internal arcs partitioned; global cross arcs NOT certified."}
    result["vertex_counts_from_different_cycles"] = {
        "status": "DISCRIMINATED", "reason": "VERTEX_LEDGER_CYCLE_IDENTITY",
        "fixtures": vertex_results}
    result["drop_M_equals_C_actual_square_import"] = {
        "status": "NOTTESTED",
        "reason": "No actual eleven-row T2(11) with M != C is supplied. A flag-only or fake-ledger control would not discriminate the scientific implication.",
        "implementation": "verify_actual_array never imports the partition unless original row conditions and M=C are directly checked."}
    return result


def main():
    physical_signatures = set()
    examples = {}
    regular_masks = set()
    b_types, d_types = set(), set()
    metrics_histogram = Counter()
    words = residual_words = all_q_words = b_words = d_words = 0
    for word in finite_cell_words():
        words += 1
        if words % 128 == 0:
            deadline()
        # Important order: actual vertices -> Hamilton/actual square -> projection.
        m = projection(actual_cycle(lift_cell_word(word)))
        sb, sd = len(m["single"]["B"]), len(m["single"]["D"])
        if sb == 12 and sd == 0:
            b_words += 1
            b_types.add(check_alternating_family_row(m, "B"))
        if sd == 12 and sb == 0:
            d_words += 1
            d_types.add(check_alternating_family_row(m, "D"))
        if sb or sd:
            continue
        residual_words += 1
        check_residual(m)
        d_il, d_jk = opposite_join_counts(m)
        signature = (m["layouts"], d_il, d_jk)
        physical_signatures.add(signature)
        examples.setdefault(signature, m["row"])
        if d_il == d_jk == 1:
            regular_masks.add(m["fullmask"])
        if m["layouts"] == ("Q",) * 4:
            all_q_words += 1
        key = ("".join(m["layouts"]), m["diag"], m["sqdiag"],
               m["cross_e"], m["square_cross_e"], len(m["single"]["E"]))
        metrics_histogram[key] += 1
    need(words == 92400, "FINITE_CELL_WORD_DOMAIN_COUNT")
    need(regular_masks == {0, 3, 5, 10, 12, 15}, "REGULAR_FULL_MASK_DOMAIN")
    need(all_q_words == 2, "ALL_Q_CELL_WORD_DOMAIN_COUNT")
    schedules = enumerate_schedules(regular_masks, physical_signatures)
    deadline()
    orientation = check_family_cross_bounds(b_types, d_types)
    paths = tuple(itertools.permutations(range(3)))
    three_path_covers = 0
    required = Counter(itertools.permutations(range(3), 2))
    for triple in itertools.product(paths, repeat=3):
        edges = Counter(edge for path in triple for edge in zip(path, path[1:]))
        three_path_covers += edges == required
    need(three_path_covers == 0, "THREE_HAMILTON_PATHS_COVER_K3")
    mutation_controls = controls(examples)
    deadline()
    return {
        "status": "COMPLETE_NECESSARY_INTERFACE_CHECKS_ONLY",
        "elapsed_seconds": time.monotonic() - START,
        "all_finite_cell_words": words,
        "residual_no_B_or_D_singleton_words": residual_words,
        "all_Q_words": all_q_words,
        "B_alternating_other_cut_no_singleton_words": b_words,
        "D_alternating_other_cut_no_singleton_words": d_words,
        "B_physical_types_j_IL_LI": sorted(b_types),
        "D_physical_types_j_IL_LI": sorted(d_types),
        "physical_layout_signatures": len(physical_signatures),
        "regular_full_masks": sorted(regular_masks),
        "same_cycle_directed_metrics_histogram": [
            {"layouts_diagAdj_diagC2_crossE_crossC2E_singleE": key, "count": count}
            for key, count in sorted(metrics_histogram.items())],
        "schedules": schedules,
        "family_orientation": orientation,
        "three_path_ordered_tuples": 216,
        "three_path_covers": three_path_covers,
        "controls": mutation_controls,
        "NOT_CERTIFIED": [
            "Code correctness beyond this one implementation",
            "Any joint labeled five-cycle or eleven-cycle decomposition",
            "Any actual T2(11) witness or unrestricted nonexistence",
            "Universal M=C", "Full exclusion of T=13 or T=14",
            "Physical discrimination of the full-mask-only mutation",
            "Discrimination of dropping M=C on a genuine T2(11)",
            "Novelty, source equivalence, independent-family, human or kernel review",
        ],
    }


if __name__ == "__main__":
    try:
        output = main()
    except CheckFailure as error:
        print(json.dumps({"status": "FAILED_OR_INCOMPLETE",
                          "reason": error.reason,
                          "elapsed_seconds": time.monotonic() - START}, sort_keys=True))
        raise SystemExit(1)
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))

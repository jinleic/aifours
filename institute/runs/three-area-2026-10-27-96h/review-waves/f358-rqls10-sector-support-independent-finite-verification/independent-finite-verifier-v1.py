#!/usr/bin/env python3
"""Independent finite incidence audit; no physical-realization conclusion."""

from collections import Counter
from itertools import combinations
from math import gcd
from time import monotonic
import sys


N = 10
Z = tuple(range(N))
CELLS = tuple((r, c) for r in Z for c in Z)
CELL_SET = frozenset(CELLS)
KEYS = tuple((kind, k) for kind in ("R", "C", "T") for k in Z)
UNITS = tuple(u for u in Z if gcd(u, N) == 1)
START = monotonic()
DEADLINE = START + 60.0

EXTRA_BASE = (0, 1, 3, 8)

PROOF_BASES = (
    ("R0", "R", 0, ((0, 0), (0, 1), (0, 3), (0, 8))),
    ("R5", "R", 5, ((5, 3), (5, 5), (5, 6), (5, 8))),
    ("T0", "T", 0, ((0, 0), (1, 9), (5, 5), (6, 4))),
    ("R1", "R", 1, ((1, 1), (1, 2), (1, 4), (1, 9))),
)

PROOF_LABELS = {
    (0, 0): 0,
    (0, 1): 1,
    (0, 3): 3,
    (0, 8): 8,
    (1, 1): 2,
    (1, 2): 3,
    (1, 4): 5,
    (1, 9): 0,
    (5, 3): 8,
    (5, 5): 0,
    (5, 6): 1,
    (5, 8): 3,
    (6, 4): 0,
}

PROOF_EXTRA_LEAVES = (
    ("C", 3, (0, 3), (5, 3)),
    ("C", 8, (0, 8), (5, 8)),
    ("T", 3, (0, 3), (5, 8)),
    ("T", 8, (0, 8), (5, 3)),
    ("C", 1, (1, 1), (0, 1)),
    ("C", 4, (6, 4), (1, 4)),
)


class AuditError(Exception):
    pass


def need(condition, reason):
    if not condition:
        raise AuditError(reason)


def tick():
    need(monotonic() <= DEADLINE, "TIME_LIMIT: exceeded 60 seconds")


def cell_text(x):
    return "(" + str(x[0]) + "," + str(x[1]) + ")"


def cells_text(xs):
    return "{" + ",".join(cell_text(x) for x in sorted(xs)) + "}"


def mask_text(s):
    return "{" + ",".join(str(x) for x in sorted(s)) + "}"


def edge(x, y):
    return (x, y) if x < y else (y, x)


def validate_latin(square):
    need(len(square) == N, "LATIN_SHAPE: expected 10 rows")
    need(all(len(row) == N for row in square),
         "LATIN_SHAPE: expected 10 columns")
    for r in Z:
        need(all(type(x) is int and x in Z for x in square[r]),
             "LATIN_SYMBOL: row=" + str(r))
        need(sorted(square[r]) == list(Z), "LATIN_ROW: row=" + str(r))
    for c in Z:
        need(sorted(square[r][c] for r in Z) == list(Z),
             "LATIN_COLUMN: column=" + str(c))
    for s in Z:
        positions = {(r, c) for r, c in CELLS if square[r][c] == s}
        need(len(positions) == N,
             "LATIN_TRANSVERSAL_SIZE: symbol=" + str(s))
        need({r for r, c in positions} == set(Z),
             "LATIN_TRANSVERSAL_ROWS: symbol=" + str(s))
        need({c for r, c in positions} == set(Z),
             "LATIN_TRANSVERSAL_COLUMNS: symbol=" + str(s))


def full_contexts(square):
    out = {}
    for kind, k in KEYS:
        if kind == "R":
            selected = {(k, c) for c in Z}
        elif kind == "C":
            selected = {(r, k) for r in Z}
        else:
            selected = {(r, c) for r, c in CELLS if square[r][c] == k}
        out[kind, k] = frozenset(selected)
    return out


def incidence(square):
    matrix = [[0] * (N * N) for _ in range(3 * N)]
    for r, c in CELLS:
        j = N * r + c
        matrix[r][j] = 1
        matrix[N + c][j] = 1
        matrix[2 * N + square[r][c]][j] = 1
    return matrix


def validate_incidence(matrix, square):
    need(len(matrix) == 3 * N and
         all(len(row) == N * N for row in matrix),
         "INCIDENCE_SHAPE: expected 30 by 100")
    contexts = full_contexts(square)
    for i, key in enumerate(KEYS):
        for j, x in enumerate(CELLS):
            actual = matrix[i][j]
            expected = int(x in contexts[key])
            need(type(actual) is int and actual in (0, 1),
                 "INCIDENCE_BINARY: context=" + key[0] + str(key[1]))
            need(actual == expected,
                 "INCIDENCE_ENTRY: context=" + key[0] + str(key[1]) +
                 " cell=" + cell_text(x) +
                 " expected=" + str(expected) + " actual=" + str(actual))
    for j in range(N * N):
        need(sum(matrix[i][j] for i in range(3 * N)) == 3,
             "INCIDENCE_COLUMN_DEGREE: cell=" + cell_text(CELLS[j]))


def dense_rank(matrix):
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    width = len(work[0])
    pivot = 0
    for col in range(width):
        tick()
        found = next((i for i in range(pivot, len(work))
                      if work[i][col]), None)
        if found is None:
            continue
        work[pivot], work[found] = work[found], work[pivot]
        for i in range(pivot + 1, len(work)):
            if work[i][col]:
                work[i] = [a ^ b for a, b in zip(work[i], work[pivot])]
        pivot += 1
        if pivot == len(work):
            break
    return pivot


def packed_rank(matrix):
    pivots = {}
    for row in matrix:
        tick()
        value = sum(entry << j for j, entry in enumerate(row))
        while value:
            top = value.bit_length() - 1
            if top in pivots:
                value ^= pivots[top]
            else:
                pivots[top] = value
                break
    return len(pivots)


def require_rank(matrix, expected, name):
    a = dense_rank(matrix)
    b = packed_rank(matrix)
    transposed = [list(row) for row in zip(*matrix)] if matrix else []
    c = dense_rank(transposed)
    need(a == b == c,
         "RANK_ALGORITHM_DISAGREEMENT: " + name +
         " values=" + str((a, b, c)))
    need(a == expected,
         "RANK_MISMATCH: " + name +
         " expected=" + str(expected) + " actual=" + str(a))
    return a


def support(s):
    selected = frozenset(s)
    return frozenset((r, c) for r, c in CELLS
                     if (c - r) % N in selected)


def forced(square, x, y):
    return (x != y and
            (x[0] == y[0] or x[1] == y[1] or
             square[x[0]][x[1]] == square[y[0]][y[1]]))


def forced_edges(square, selected):
    return frozenset(edge(x, y) for x, y in combinations(sorted(selected), 2)
                     if forced(square, x, y))


def progressions(s):
    return tuple((a, b, c)
                 for a, c in combinations(sorted(s), 2)
                 for b in sorted(s)
                 if b != a and b != c and (a + c - 2 * b) % N == 0)


def affine_mask(s, u, t):
    return tuple(sorted((u * x + t) % N for x in s))


def orbit(s):
    return frozenset(affine_mask(s, u, t) for u in UNITS for t in Z)


def audit_ap(s, triple, full, square, relation=None, right_override=None):
    a, b, c = triple
    need(len({a, b, c}) == 3 and {a, b, c} <= set(s) and
         (a + c - 2 * b) % N == 0, "AP_TRIPLE: invalid progression")
    selected = support(s)
    left = set(full["R", 0] & selected)
    right = set(full["C", b] & selected)
    if right_override is not None:
        right = set(right_override)
    common = (0, b)
    actual_intersection = left & right
    need(actual_intersection == {common},
         "AP_INTERSECTION: expected=" + cells_text({common}) +
         " actual=" + cells_text(actual_intersection))
    need(left == {(0, x) for x in s}, "AP_CONTEXT: incorrect row basis")
    need(right == set(full["C", b] & selected),
         "AP_CONTEXT: incorrect column basis")
    need(len(left) == len(right) == 4, "AP_CONTEXT_SIZE: expected four")
    x1, x2 = (0, a), (0, c)
    y1, y2 = ((b - c) % N, b), ((b - a) % N, b)
    need(len({x1, x2, common}) == 3 and
         len({y1, y2, common}) == 3, "AP_DISTINCT: repeated proof cell")
    for x in (x1, common, x2, y1, common, y2):
        need(x in selected, "AP_MEMBERSHIP: " + cell_text(x))
    need({x1, x2} <= left - {common} and
         {y1, y2} <= right - {common},
         "AP_REMAINDERS: incorrect cross-pair endpoints")
    need(square[x1[0]][x1[1]] == square[y1[0]][y1[1]] == a,
         "AP_LABEL: first forced pair")
    need(square[x2[0]][x2[1]] == square[y2[0]][y2[1]] == c,
         "AP_LABEL: second forced pair")
    if relation is None:
        relation = forced_edges(square, selected)
    need(edge(x1, y1) in relation and edge(x2, y2) in relation,
         "AP_ORTHOGONALITY: missing forced cross-pair")


def intersecting_context_certificate(selected, full, relation):
    sector = [set(full[key] & selected) for key in KEYS]
    for i, left in enumerate(sector):
        for j in range(i + 1, len(sector)):
            right = sector[j]
            common = left & right
            if len(common) != 1:
                continue
            pairs = tuple((x, y)
                          for x in sorted(left - common)
                          for y in sorted(right - common)
                          if edge(x, y) in relation)
            if len(pairs) >= 2:
                return (KEYS[i], KEYS[j], tuple(sorted(common)), pairs)
    return None


def audit_extra(s, full, square, u=1, t=0,
                supplied_labels=None, supplied_relation=None):
    need(tuple(sorted(s)) == affine_mask(EXTRA_BASE, u, t),
         "PROOF_SUPPORT: wrong affine representative")
    selected = support(s)

    def image(x):
        return (u * x[0] % N, (u * x[1] + t) % N)

    def context_image(kind, k):
        return (u * k + (t if kind in ("C", "T") else 0)) % N

    labels = PROOF_LABELS if supplied_labels is None else supplied_labels
    need(set(labels) == set(PROOF_LABELS),
         "PROOF_LABEL_DOMAIN: wrong cell set")
    for original in sorted(PROOF_LABELS):
        x = image(original)
        need(x in selected, "PROOF_MEMBERSHIP: " + cell_text(x))
        expected = (u * labels[original] + t) % N
        actual = square[x[0]][x[1]]
        need(actual == expected,
             "PROOF_LABEL: " + cell_text(x) +
             " expected=" + str(expected) + " actual=" + str(actual))

    relation = (forced_edges(square, selected) if supplied_relation is None
                else frozenset(supplied_relation))
    leaves = set()
    named = {}

    def leaf(x, y):
        need(edge(x, y) in relation,
             "PROOF_ORTHOGONALITY: missing " +
             cell_text(x) + "--" + cell_text(y))
        leaves.add(edge(x, y))

    for name, kind, k, originals in PROOF_BASES:
        basis = {image(x) for x in originals}
        expected_basis = set(full[kind, context_image(kind, k)] & selected)
        need(basis == expected_basis and len(basis) == 4,
             "PROOF_CONTEXT: " + name + " is not the exact sector context")
        named[name] = basis
        for x, y in combinations(sorted(basis), 2):
            leaf(x, y)

    for kind, k, old_x, old_y in PROOF_EXTRA_LEAVES:
        x, y = image(old_x), image(old_y)
        reason_context = full[kind, context_image(kind, k)]
        need(x != y and x in reason_context and y in reason_context,
             "PROOF_RELATION_REASON: invalid named context")
        leaf(x, y)

    need(len({image(x) for x in PROOF_LABELS}) == 13,
         "PROOF_CELL_COUNT: expected 13")
    need(len(leaves) == 30, "PROOF_LEAF_COUNT: expected 30")

    # The following checks audit the finite interfaces of the written
    # dimension-four argument. They do not construct or test any vectors.
    known = set(relation)

    def dependency(old_x, old_y):
        need(edge(image(old_x), image(old_y)) in known,
             "PROOF_WIRING: missing dependency " +
             cell_text(old_x) + "--" + cell_text(old_y))

    plane_a = {image((0, 3)), image((0, 8))}
    plane_b = {image((5, 3)), image((5, 8))}
    need(named["R0"] - plane_a == {image((0, 0)), image((0, 1))},
         "PROOF_WIRING: wrong R0 complementary pair")
    need(plane_b <= named["R5"] and image((5, 5)) in
         named["R5"] - plane_b, "PROOF_WIRING: wrong R5 plane")
    for x in ((0, 3), (0, 8)):
        for y in ((5, 3), (5, 8)):
            dependency(x, y)
    dependency((5, 3), (5, 5))
    dependency((5, 8), (5, 5))

    # Conditional rule: orthogonal two-planes in a 4D ONB setting are
    # complements; hence 01 lies in span(53,58), which is orthogonal to 55.
    first_derived = edge(image((0, 1)), image((5, 5)))
    need(first_derived not in relation,
         "PROOF_WIRING: first derived edge unexpectedly direct")
    known.add(first_derived)

    need(named["T0"] - {image((0, 0)), image((5, 5))} ==
         {image((1, 9)), image((6, 4))},
         "PROOF_WIRING: wrong T0 complementary pair")
    dependency((0, 1), (0, 0))
    dependency((0, 1), (5, 5))
    dependency((1, 1), (0, 1))
    dependency((1, 1), (1, 9))
    need(image((0, 1)) != image((1, 9)),
         "PROOF_WIRING: distinct-cell hypothesis collapsed")

    # Conditional rule also uses the ORIGINAL global nonparallel-ray
    # hypothesis: the coefficient on 64 in the (19,64) expansion is nonzero.
    second_derived = edge(image((1, 1)), image((6, 4)))
    need(second_derived not in relation,
         "PROOF_WIRING: second derived edge unexpectedly direct")
    known.add(second_derived)

    for x in ((1, 1), (1, 4), (1, 9)):
        dependency((6, 4), x)
    need(named["R1"] -
         {image((1, 1)), image((1, 4)), image((1, 9))} ==
         {image((1, 2))}, "PROOF_WIRING: wrong terminal complement")
    need(image((6, 4)) not in named["R1"] and
         image((6, 4)) != image((1, 2)),
         "PROOF_WIRING: terminal cells are not distinct")
    return (13, len(leaves), 2)


def audit_affine(balanced, full, square):
    covered_extra = set()
    maps_checked = 0
    for u in UNITS:
        for t in Z:
            tick()
            images = {x: (u * x[0] % N, (u * x[1] + t) % N)
                      for x in CELLS}
            need(set(images.values()) == set(CELLS),
                 "AFFINE_BIJECTION: not all cells covered")
            for x in CELLS:
                y = images[x]
                need((y[1] - y[0]) % N ==
                     (u * (x[1] - x[0]) + t) % N,
                     "AFFINE_DIFFERENCE: incorrect support routing")
                need(square[y[0]][y[1]] ==
                     (u * square[x[0]][x[1]] + t) % N,
                     "AFFINE_LABEL: incorrect symbol routing")
            for kind, k in KEYS:
                target = (u * k + (t if kind in ("C", "T") else 0)) % N
                need({images[x] for x in full[kind, k]} ==
                     set(full[kind, target]),
                     "AFFINE_CONTEXT: incorrect context routing")
            for x, y in combinations(CELLS, 2):
                need(forced(square, x, y) ==
                     forced(square, images[x], images[y]),
                     "AFFINE_RELATION: orthogonality incidence changed")
            for s in sorted(balanced):
                mapped_s = affine_mask(s, u, t)
                need(mapped_s in balanced,
                     "AFFINE_BALANCE: balanced support left family")
                need({images[x] for x in support(s)} == set(support(mapped_s)),
                     "AFFINE_SUPPORT: membership equivalence failed")
            mapped_extra = affine_mask(EXTRA_BASE, u, t)
            need(audit_extra(mapped_extra, full, square, u, t) == (13, 30, 2),
                 "AFFINE_PROOF: incorrect transformed proof counts")
            covered_extra.add(mapped_extra)
            maps_checked += 1
    need(maps_checked == 40, "AFFINE_MAP_COUNT: expected 40")
    need(covered_extra == set(orbit(EXTRA_BASE)),
         "AFFINE_PROOF_COVERAGE: missing an extra-orbit support")
    return maps_checked


def expect_failure(name, expected_reason, operation):
    try:
        operation()
    except AuditError as exc:
        actual_reason = str(exc)
        need(actual_reason == expected_reason,
             "CONTROL_WRONG_REASON: " + name +
             " expected=" + repr(expected_reason) +
             " actual=" + repr(actual_reason))
        print("CONTROL:", name, "REJECTED:", actual_reason)
        return
    raise AuditError("CONTROL_ACCEPTED_MUTATION: " + name)


def main():
    need(len(sys.argv) == 1,
         "USAGE: python3 -B independent-finite-verifier-v1.py")
    need(UNITS == (1, 3, 7, 9), "UNIT_SET: incorrect units")

    rank_controls = (
        ([[0, 0], [0, 0]], 0),
        ([[1, 1], [1, 1]], 1),
        ([[1, 0], [0, 1]], 2),
        ([[1, 1, 0], [0, 1, 1], [1, 0, 1]], 2),
    )
    for i, (matrix, expected) in enumerate(rank_controls):
        require_rank(matrix, expected, "positive-" + str(i))

    cyclic = [[(r + c) % N for c in Z] for r in Z]
    traded = [row[:] for row in cyclic]
    for r in (0, 5):
        traded[r][0], traded[r][5] = traded[r][5], traded[r][0]
    validate_latin(cyclic)
    validate_latin(traded)
    changed = {(r, c) for r, c in CELLS if cyclic[r][c] != traded[r][c]}
    need(changed == {(0, 0), (0, 5), (5, 0), (5, 5)},
         "TRADE_CELLS: incorrect changed-cell set")
    need(tuple(traded[r][c] for r, c in
               ((0, 0), (0, 5), (5, 0), (5, 5))) == (5, 0, 0, 5),
         "TRADE_VALUES: incorrect intercalate exchange")

    cyclic_matrix = incidence(cyclic)
    traded_matrix = incidence(traded)
    validate_incidence(cyclic_matrix, cyclic)
    validate_incidence(traded_matrix, traded)
    cyclic_rank = require_rank(cyclic_matrix, 27, "cyclic")
    traded_rank = require_rank(traded_matrix, 28, "traded")
    full = full_contexts(cyclic)

    all_masks = frozenset(combinations(Z, 4))
    need(len(all_masks) == 210, "MASK_UNIVERSE: expected 210")
    balanced = set()
    parity_balanced = {s for s in all_masks
                       if sum(x % 2 == 0 for x in s) == 2}
    for s in sorted(all_masks):
        tick()
        selected = support(s)
        need(len(selected) == 40, "SUPPORT_SIZE: expected 40")
        counts = tuple(len(selected & full[key]) for key in KEYS)
        need(counts[:20] == (4,) * 20,
             "ROW_COLUMN_COUNTS: not all four")
        direct_symbol_expected = tuple(
            2 * sum(x % 2 == label % 2 for x in s) for label in Z)
        need(counts[20:] == direct_symbol_expected,
             "SYMBOL_COUNTS: direct count differs from parity formula")
        if counts == (4,) * 30:
            balanced.add(s)
            complement_counts = tuple(
                len((CELL_SET - selected) & full[key]) for key in KEYS)
            need(complement_counts == (6,) * 30,
                 "COMPLEMENT_COUNTS: not all six")
    need(balanced == parity_balanced and len(balanced) == 100,
         "BALANCED_SET: incorrect complete support set")

    ap_masks = set()
    context_exclusions = set()
    histogram = Counter()
    ap_certificates = 0
    for s in sorted(balanced):
        tick()
        selected = support(s)
        relation = forced_edges(cyclic, selected)
        need(len(relation) == 180,
             "FORCED_GRAPH_COUNT: expected 180 original edges")
        triples = progressions(s)
        histogram[len(triples)] += 1
        if triples:
            ap_masks.add(s)
        for triple in triples:
            audit_ap(s, triple, full, cyclic, relation)
            ap_certificates += 1
        certificate = intersecting_context_certificate(
            selected, full, relation)
        if certificate is not None:
            context_exclusions.add(s)
    need(dict(histogram) == {0: 40, 1: 40, 2: 20},
         "AP_HISTOGRAM: expected 40,40,20")
    need(len(ap_masks) == 60 and ap_certificates == 80,
         "AP_COUNTS: expected 60 masks and 80 progression certificates")
    need(context_exclusions == ap_masks,
         "INTERSECTING_CONTEXT_SET: differs from AP mask set")

    partition = {}
    remaining = set(balanced)
    while remaining:
        tick()
        representative = min(remaining)
        members = set(orbit(representative))
        need(members <= balanced, "ORBIT_BALANCE: escaped balanced family")
        need(members <= remaining, "ORBIT_PARTITION: overlapping orbit")
        partition[representative] = frozenset(members)
        remaining -= members
    expected_orbits = {
        (0, 1, 2, 3): 20,
        (0, 1, 2, 5): 40,
        (0, 1, 3, 4): 10,
        (0, 1, 3, 8): 20,
        (0, 1, 5, 6): 10,
    }
    need({s: len(members) for s, members in partition.items()} ==
         expected_orbits, "ORBIT_PARTITION: incorrect complete partition")
    need(ap_masks == set(orbit((0, 1, 2, 3))) |
         set(orbit((0, 1, 2, 5))),
         "AP_ORBITS: complete AP set differs")

    extra = set(orbit(EXTRA_BASE))
    survivor_a = set(orbit((0, 1, 3, 4)))
    survivor_b = set(orbit((0, 1, 5, 6)))
    survivors = balanced - ap_masks - extra
    need(len(extra) == 20 and not (extra & ap_masks),
         "EXTRA_ORBIT: wrong size or overlaps AP masks")
    need(len(survivor_a) == len(survivor_b) == 10 and
         not (survivor_a & survivor_b),
         "SURVIVOR_ORBITS: incorrect sizes or overlap")
    need(survivors == survivor_a | survivor_b and len(survivors) == 20,
         "SURVIVOR_SET: incorrect complete residual")
    need(len(ap_masks | extra) == 80,
         "EXCLUSION_COUNT: expected 80 support-level exclusions")
    need(audit_extra(EXTRA_BASE, full, cyclic) == (13, 30, 2),
         "PROOF_COUNTS: incorrect representative proof counts")
    maps_checked = audit_affine(balanced, full, cyclic)

    wrong_latin = [row[:] for row in cyclic]
    wrong_latin[0][0] = 1
    expect_failure(
        "wrong_latin_label",
        "LATIN_ROW: row=0",
        lambda: validate_latin(wrong_latin),
    )

    wrong_labels = dict(PROOF_LABELS)
    wrong_labels[5, 8] = 4
    expect_failure(
        "wrong_proof_label",
        "PROOF_LABEL: (5,8) expected=4 actual=3",
        lambda: audit_extra(EXTRA_BASE, full, cyclic,
                            supplied_labels=wrong_labels),
    )

    missing_relation = set(forced_edges(cyclic, support(EXTRA_BASE)))
    removed_edge = edge((0, 3), (5, 8))
    need(removed_edge in missing_relation,
         "CONTROL_SETUP: orthogonality edge was not present")
    missing_relation.remove(removed_edge)
    expect_failure(
        "removed_orthogonality",
        "PROOF_ORTHOGONALITY: missing (0,3)--(5,8)",
        lambda: audit_extra(EXTRA_BASE, full, cyclic,
                            supplied_relation=missing_relation),
    )

    ap_control_mask = (0, 1, 2, 3)
    damaged_column = set(full["C", 1] & support(ap_control_mask))
    need((0, 1) in damaged_column,
         "CONTROL_SETUP: common context cell was not present")
    damaged_column.remove((0, 1))
    expect_failure(
        "removed_context_intersection",
        "AP_INTERSECTION: expected={(0,1)} actual={}",
        lambda: audit_ap(ap_control_mask, (0, 1, 2), full, cyclic,
                         right_override=damaged_column),
    )

    corrupted_matrix = [row[:] for row in cyclic_matrix]
    need(corrupted_matrix[0][0] == 1,
         "CONTROL_SETUP: incidence entry was not one")
    corrupted_matrix[0][0] = 0
    expect_failure(
        "corrupt_incidence_entry",
        "INCIDENCE_ENTRY: context=R0 cell=(0,0) expected=1 actual=0",
        lambda: validate_incidence(corrupted_matrix, cyclic),
    )
    expect_failure(
        "corrupt_rank_entry",
        "RANK_MISMATCH: cyclic expected=27 actual=28",
        lambda: require_rank(corrupted_matrix, 27, "cyclic"),
    )
    expect_failure(
        "wrong_rank_claim",
        "RANK_MISMATCH: cyclic expected=26 actual=27",
        lambda: require_rank(cyclic_matrix, 26, "cyclic"),
    )

    tick()
    print("LATIN: cyclic and explicit four-cell trade valid")
    print("F2_RANKS: cyclic=" + str(cyclic_rank) +
          " traded=" + str(traded_rank))
    print("MASKS: total=210 balanced=100 complement_counts=6")
    print("AP: masks=60 histogram=0:40,1:40,2:20 certificates=80")
    print("INTERSECTING_CONTEXT_TEST: exactly the same 60 AP masks")
    for representative in sorted(partition):
        members = partition[representative]
        print("ORBIT:", mask_text(representative),
              "size=" + str(len(members)),
              "members=" + ";".join(mask_text(s) for s in sorted(members)))
    print("EXTRA: AP-free orbit size=20")
    print("RESIDUAL: two disjoint orbits size=10+10")
    print("REPRESENTATIVE_PROOF: cells=13 direct_leaves=30 "
          "conditional_steps=2")
    print("AFFINE: maps=" + str(maps_checked) +
          " all cells/pairs/contexts/balanced supports checked")
    print("CONTROLS: 7 intended-reason rejections")
    print("ELAPSED_SECONDS:", format(monotonic() - START, ".6f"))
    print("RESULT: PASS_FINITE_ONLY")
    print("LIMIT: no physical unitary sufficiency, phase realization, "
          "ray witness, or global RQLS no-go established")


if __name__ == "__main__":
    try:
        main()
    except AuditError as exc:
        print("RESULT: FAIL_FINITE_ONLY", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)

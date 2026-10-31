#!/usr/bin/env python3
"""Independent exact small-n 2n+3 support classification controls.

Enumerate unordered multisets of row masks, with exact row-label weights.
No author program or author receipt is loaded. All matrix arithmetic is rational.
"""

from collections import Counter
from datetime import datetime
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import platform
import sys


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def mask_size(x):
    return x.bit_count()


def no_unique_intersections(masks):
    return all(mask_size(a & b) != 1 for a, b in combinations(masks, 2))


def columns(rows, n):
    return tuple(sum(((row >> j) & 1) << i for i, row in enumerate(rows)) for j in range(n))


def graph_conditions(rows, n):
    cs = columns(rows, n)
    return (all(mask_size(x) >= 2 for x in rows + cs)
            and no_unique_intersections(rows) and no_unique_intersections(cs))


def components(rows, n):
    unseen = set(range(n))
    components_found = []
    while unseen:
        row_set = {min(unseen)}
        col_set = set()
        while True:
            new_cols = {j for i in row_set for j in range(n) if rows[i] & (1 << j)}
            new_rows = {i for i in range(n) if any(rows[i] & (1 << j) for j in new_cols)}
            if new_rows == row_set and new_cols == col_set:
                break
            row_set, col_set = new_rows, new_cols
        unseen.difference_update(row_set)
        components_found.append((tuple(sorted(row_set)), tuple(sorted(col_set))))
    return components_found


def component_square(rows, n):
    return all(len(rr) == len(cc) for rr, cc in components(rows, n))


def repeated_pair_obstruction(rows):
    # Two orthogonal rows on a common two-set span it; all other rows must vanish
    # there. Three such rows alone are impossible. Return a witness if violated.
    degree_two = Counter(x for x in rows if mask_size(x) == 2)
    for pair, k in sorted(degree_two.items()):
        if k >= 3:
            return {"kind": "three_rows_in_two_columns", "pair_mask": pair, "rows": k}
        if k == 2:
            outside = [i for i, row in enumerate(rows) if row != pair and row & pair]
            if outside:
                return {"kind": "two_rows_span_pair_but_other_row_meets_it",
                        "pair_mask": pair, "outside_rows": outside}
    return None


def singleton_pair_neighbor_obstruction(rows):
    # Applicable after the no-unique-row-intersection check: every neighbor of
    # a two-entry row uses both its columns. One neighbor would exhaust its norm
    # by orthonormality of the two columns; it cannot then have higher degree.
    counts = Counter(x for x in rows if mask_size(x) == 2)
    for pair, k in sorted(counts.items()):
        if k != 1:
            continue
        adjacent = [i for i, row in enumerate(rows) if row != pair and row & pair]
        if len(adjacent) < 2:
            return {"pair_mask": pair, "neighbor_rows": adjacent}
    return None


def rational_block(size):
    if size == 2:
        return [[Fraction(3, 5), Fraction(4, 5)],
                [Fraction(-4, 5), Fraction(3, 5)]]
    if size == 3:
        # I - 2J/3: a real, full orthogonal reflection.
        return [[Fraction(1 if i == j else -2, 3) for j in range(3)] for i in range(3)]
    raise RuntimeError("unexpected component size")


def exact_gram(matrix):
    n = len(matrix)
    return all(sum(matrix[k][i] * matrix[k][j] for k in range(n)) == int(i == j)
               and sum(matrix[i][k] * matrix[j][k] for k in range(n)) == int(i == j)
               for i in range(n) for j in range(n))


def exact_realization(rows, n):
    parts = components(rows, n)
    sizes = sorted(len(rr) for rr, _ in parts)
    require(sizes == [2] * ((n - 3) // 2) + [3], "unexpected survivor component sizes")
    mat = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for rr, cc in parts:
        require(len(rr) == len(cc) and len(rr) in (2, 3), "bad survivor block")
        require(all(rows[i] & (1 << j) for i in rr for j in cc), "survivor not full")
        block = rational_block(len(rr))
        for a, i in enumerate(rr):
            for b, j in enumerate(cc):
                mat[i][j] = block[a][b]
    support = tuple(sum((mat[i][j] != 0) << j for j in range(n)) for i in range(n))
    require(support == rows and exact_gram(mat), "exact rational realization failed")


def multiset_weight(group):
    result = factorial(len(group))
    for count in Counter(group).values():
        result //= factorial(count)
    return result


def scan(n):
    # 3 units of row excess split uniquely as 3, 2+1, or 1+1+1.
    specifications = [((2, n - 1), (5, 1)),
                      ((2, n - 2), (3, 1), (4, 1)),
                      ((2, n - 3), (3, 3))]
    available = {d: tuple(sum(1 << j for j in choice) for choice in combinations(range(n), d))
                 for d in (2, 3, 4, 5)}
    counters = Counter()
    examples = {}
    for spec in specifications:
        # Number of all row-labelled patterns, including those pruned below.
        row_assignment = factorial(n)
        for _, k in spec:
            row_assignment //= factorial(k)
        total = row_assignment
        total_multisets = 1
        lists = []
        for degree, k in spec:
            number = len(available[degree])
            total *= number ** k
            total_multisets *= comb(number + k - 1, k) if number or k == 0 else 0
            groups = []
            for group in combinations_with_replacement(available[degree], k):
                # A within-group unique overlap is already a mathematical
                # impossibility; prune it before building the Cartesian product.
                if no_unique_intersections(group):
                    groups.append((group, multiset_weight(group)))
            lists.append(groups)
        counters["all_labeled_patterns"] += total
        counters["all_row_multisets"] += total_multisets
        for selection in product(*lists):
            rows = sum((entry[0] for entry in selection), ())
            weight = row_assignment
            for _, w in selection:
                weight *= w
            counters["labeled_after_within_degree_prune"] += weight
            counters["multisets_after_within_degree_prune"] += 1
            if not no_unique_intersections(rows):
                continue
            counters["row_no_unique_labeled"] += weight
            cs = columns(rows, n)
            if not all(mask_size(x) >= 2 for x in cs):
                continue
            counters["column_minimum_labeled"] += weight
            if not no_unique_intersections(cs):
                continue
            counters["both_overlap_filters_labeled"] += weight
            if not component_square(rows, n):
                counters["rectangular_rejected_labeled"] += weight
                if "rectangular" not in examples:
                    examples["rectangular"] = list(rows)
                continue
            counters["square_graph_survivors_labeled"] += weight
            obstruction = repeated_pair_obstruction(rows)
            if obstruction:
                counters["duplicate_pair_rejected_labeled"] += weight
                if "duplicate_pair" not in examples:
                    examples["duplicate_pair"] = {"row_masks": list(rows), "obstruction": obstruction}
                continue
            counters["after_duplicate_pair_labeled"] += weight
            obstruction = singleton_pair_neighbor_obstruction(rows)
            if obstruction:
                counters["two_neighbor_rejected_labeled"] += weight
                if "two_neighbor" not in examples:
                    examples["two_neighbor"] = {"row_masks": list(rows), "obstruction": obstruction}
                continue
            counters["exactly_realized_labeled"] += weight
            counters["exactly_realized_multisets"] += 1
            exact_realization(rows, n)
    keys = ("all_labeled_patterns", "all_row_multisets", "labeled_after_within_degree_prune",
            "multisets_after_within_degree_prune", "row_no_unique_labeled",
            "column_minimum_labeled", "both_overlap_filters_labeled",
            "rectangular_rejected_labeled", "square_graph_survivors_labeled",
            "duplicate_pair_rejected_labeled", "after_duplicate_pair_labeled",
            "two_neighbor_rejected_labeled", "exactly_realized_labeled", "exactly_realized_multisets")
    return {"n": n, **{key: counters[key] for key in keys}, "examples": examples}


def controls():
    rectangle = (0b00111, 0b00111, 0b11000, 0b11000, 0b11000)
    require(graph_conditions(rectangle, 5), "rectangular control must pass overlap and degree filters")
    require(not component_square(rectangle, 5), "rectangular control must fail component square test")
    dims = [[len(rr), len(cc)] for rr, cc in components(rectangle, 5)]
    require(sorted(dims) == [[2, 3], [3, 2]], "rectangular component dimensions wrong")
    # Connected square support, passes all graph filters, yet three orthogonal
    # rows would have to lie in a two-dimensional coordinate subspace.
    false_positive = (0b00011, 0b00011, 0b00011, 0b11111, 0b11111)
    require(graph_conditions(false_positive, 5) and component_square(false_positive, 5),
            "unitarity obstruction control must pass graph tests")
    witness = repeated_pair_obstruction(false_positive)
    require(witness is not None and witness["kind"] == "three_rows_in_two_columns",
            "two-dimensional rank obstruction not detected")
    require(mask_size(false_positive[0] | false_positive[1] | false_positive[2]) == 2,
            "rank witness does not occupy exactly two columns")
    require(not no_unique_intersections((0b0011, 0b0110)), "unique-overlap control missed")
    for size in (2, 3):
        require(exact_gram(rational_block(size)), "rational full-block positive control failed")
    # Orthogonal 3x3 with eight entries: a positive lower-excess control.
    f = Fraction
    eight = [[f(3, 5), f(4, 13), f(48, 65)],
             [f(-4, 5), f(3, 13), f(36, 65)],
             [f(0), f(-12, 13), f(5, 13)]]
    require(exact_gram(eight) and sum(v != 0 for row in eight for v in row) == 8,
            "eight-entry 3x3 positive control failed")
    return {"rectangle": {"n": 5, "row_masks": list(rectangle), "nnz": 12,
                          "passes_degree_and_overlap": True, "component_dimensions": dims,
                          "component_square_rejects": True},
            "square_graph_but_not_unitary": {"n": 5, "row_masks": list(false_positive),
                          "nnz": 16, "passes_degree_overlap_component_checks": True,
                          "rank_obstruction": witness},
            "unique_overlap_rejected": True,
            "exact_rational_full_2_and_3_blocks": True,
            "exact_rational_3_by_3_eight_entry_block": True}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: excess-check-v1.py NEW_RECEIPT.json")
    dest = Path(sys.argv[1])
    if dest.exists():
        raise SystemExit("refusing to overwrite receipt")
    control_results = controls()
    cases = [scan(n) for n in (3, 4, 5, 6)]
    for case in cases:
        n = case["n"]
        expected = 0 if n % 2 == 0 else (
            comb(n, 3) ** 2
            * (factorial(n - 3) // (2 ** ((n - 3) // 2) * factorial((n - 3) // 2))) ** 2
            * factorial((n - 3) // 2))
        require(case["exactly_realized_labeled"] == expected, "classification count mismatch")
    result = {"schema": 1,
              "scope": "All labeled n=3,4,5,6 masks with nnz=2n+3 and row minimum two; necessary filters followed by exact rational realization of every final survivor. Not an all-n proof or a general graph-sufficiency claim.",
              "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "clock_before_receipt_creation": datetime.now().astimezone().isoformat(timespec="seconds"),
              "python": platform.python_version(), "platform": platform.platform(),
              "cases": cases, "controls": control_results}
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    with dest.open("x", encoding="utf-8") as out:
        out.write(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()

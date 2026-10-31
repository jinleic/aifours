#!/usr/bin/env python3
"""Independent bounded 2n, 2n+1, 2n+2 controls using our own utility module."""
from collections import Counter
from datetime import datetime
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import combinations_with_replacement, product
from math import factorial
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
HELPER = HERE / "excess-check-v1.py"
spec = spec_from_file_location("excess_own_helper", HELPER)
base = module_from_spec(spec)
spec.loader.exec_module(base)


def realize(rows, n, excess):
    parts = base.components(rows, n)
    dims = sorted(len(rr) for rr, _ in parts)
    expected = [2] * (n // 2) if excess == 0 else [2] * ((n - 3) // 2) + [3]
    base.require(dims == expected, "lower-excess component form failed")
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    f = Fraction
    eight = [[f(3, 5), f(4, 13), f(48, 65)],
             [f(-4, 5), f(3, 13), f(36, 65)],
             [f(0), f(-12, 13), f(5, 13)]]
    for rr, cc in parts:
        base.require(len(rr) == len(cc), "component is not square")
        if len(rr) == 2:
            base.require(all(rows[i] & (1 << j) for i in rr for j in cc), "2x2 not full")
            row_order, col_order, block = rr, cc, base.rational_block(2)
        else:
            missing = [(i, j) for i in rr for j in cc if not rows[i] & (1 << j)]
            base.require(len(rr) == 3 and len(missing) == 1, "3x3 is not eight-entry")
            i0, j0 = missing[0]
            row_order = tuple(i for i in rr if i != i0) + (i0,)
            col_order = (j0,) + tuple(j for j in cc if j != j0)
            block = eight
        for a, i in enumerate(row_order):
            for b, j in enumerate(col_order):
                matrix[i][j] = block[a][b]
    support = tuple(sum((matrix[i][j] != 0) << j for j in range(n)) for i in range(n))
    base.require(support == rows and base.exact_gram(matrix), "exact realization failed")


def scan(n, excess):
    specs = {
        0: [((2, n),)],
        1: [((2, n - 1), (3, 1))],
        2: [((2, n - 1), (4, 1)), ((2, n - 2), (3, 2))],
    }[excess]
    choices = {d: tuple(mask for mask in range(1 << n) if mask.bit_count() == d)
               for d in (2, 3, 4)}
    counts = Counter()
    example = None
    for groups in specs:
        row_weight = factorial(n)
        for _, k in groups:
            row_weight //= factorial(k)
        tested = row_weight
        option_lists = []
        for degree, k in groups:
            tested *= len(choices[degree]) ** k
            option_lists.append([(group, base.multiset_weight(group))
                                 for group in combinations_with_replacement(choices[degree], k)
                                 if base.no_unique_intersections(group)])
        counts["all_labeled_patterns"] += tested
        for selection in product(*option_lists):
            rows = sum((group for group, _ in selection), ())
            weight = row_weight
            for _, w in selection:
                weight *= w
            counts["multisets_after_within_degree_prune"] += 1
            if not base.no_unique_intersections(rows):
                continue
            counts["row_no_unique_labeled"] += weight
            cols = base.columns(rows, n)
            if not all(c.bit_count() >= 2 for c in cols):
                continue
            if not base.no_unique_intersections(cols):
                continue
            counts["both_overlap_filters_labeled"] += weight
            if not base.component_square(rows, n):
                counts["rectangular_rejected_labeled"] += weight
                if example is None:
                    example = list(rows)
                continue
            counts["square_graph_survivors_labeled"] += weight
            if base.repeated_pair_obstruction(rows):
                counts["duplicate_pair_rejected_labeled"] += weight
                continue
            if base.singleton_pair_neighbor_obstruction(rows):
                counts["two_neighbor_rejected_labeled"] += weight
                continue
            base.require(excess != 1, "an excess-one pattern passed necessary unitary conditions")
            realize(rows, n, excess)
            counts["exactly_realized_labeled"] += weight
            counts["exactly_realized_multisets"] += 1
    keys = ("all_labeled_patterns", "multisets_after_within_degree_prune", "row_no_unique_labeled",
            "both_overlap_filters_labeled", "rectangular_rejected_labeled", "square_graph_survivors_labeled",
            "duplicate_pair_rejected_labeled", "two_neighbor_rejected_labeled", "exactly_realized_labeled",
            "exactly_realized_multisets")
    return {"n": n, "excess": excess, **{k: counts[k] for k in keys},
            "rectangular_example_row_masks": example}


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: excess-lower-check-v1.py NEW_RECEIPT.json")
    dest = Path(sys.argv[1])
    if dest.exists():
        raise SystemExit("refusing to overwrite receipt")
    cases = [scan(n, excess) for n in (3, 4, 5, 6) for excess in (0, 1, 2)]
    result = {"scope": "All labeled n=3..6 row-minimum-two masks at excess 0,1,2; necessary filters and exact rational realizations, not an all-n proof.",
              "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "own_helper_sha256": hashlib.sha256(HELPER.read_bytes()).hexdigest(),
              "clock_before_receipt_creation": datetime.now().astimezone().isoformat(timespec="seconds"),
              "cases": cases}
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    with dest.open("x", encoding="utf-8") as out:
        out.write(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()

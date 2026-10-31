#!/usr/bin/env python3
"""Check every fixed complementary-pair slice is a weighted partial permutation.

This supports the exact rank-invariance obstruction to lowering support by
arbitrary local changes on any two parties of the verified 60-term tensor.
"""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("verifier", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("dense_verifier", args.verifier)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tensor, table_sha = module.load_table(args.table)
    rows = []
    for active in itertools.combinations(range(4), 2):
        fixed = tuple(i for i in range(4) if i not in active)
        slices = {t: [] for t in itertools.product(range(6), repeat=2)}
        for coordinate, coeff in tensor.items():
            frozen = tuple(coordinate[i] for i in fixed)
            local = tuple(coordinate[i] for i in active)
            if coeff == (0, 0):
                raise ValueError("stored zero coefficient")
            slices[frozen].append(local)
        rank_sum = 0
        histogram = collections.Counter()
        for frozen, entries in slices.items():
            row_indices = [p[0] for p in entries]
            col_indices = [p[1] for p in entries]
            if len(set(row_indices)) != len(entries) or len(set(col_indices)) != len(entries):
                raise ValueError(f"slice is not a partial permutation: {active}, {frozen}")
            rank_sum += len(entries)
            histogram[len(entries)] += 1
        rows.append({"active_parties_zero_based": active, "fixed_parties": fixed,
                     "number_of_slices": len(slices), "slice_rank_histogram": dict(sorted(histogram.items())),
                     "sum_of_slice_ranks": rank_sum})
    result = {"table": str(args.table), "table_sha256": table_sha,
              "method": "for each complementary pair, verify every active 6x6 support has at most one entry per row and column",
              "pairs": rows,
              "implication": "For any two arbitrary invertible local 6x6 matrices, every slice rank is unchanged and nonzero count is >= rank, so total support is >= the recorded rank sum.",
              "limitations": "Specific 60-term tensor; no three- or four-party, global-orbit or novelty claim."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()

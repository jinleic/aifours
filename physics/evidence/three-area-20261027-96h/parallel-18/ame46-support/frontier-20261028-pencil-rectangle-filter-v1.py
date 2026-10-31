#!/usr/bin/env python3
"""Bound dimension of rank-one matrix-pencil vectors via rectangular support.

Each pencil cell is owned by at most one coefficient variable, so a rank-one
matrix can only occur when the union support of its nonzero variables is an
exact row-set x column-set rectangle. Exhaustive enumeration of 2^6-1 masks is
an overapproximation: rectangular support is necessary, not sufficient.
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
    report = []
    for spectator in range(4):
        active = [i for i in range(4) if i != spectator]
        for level in range(6):
            choices = []
            for pencil in active:
                row_axis, col_axis = (i for i in active if i != pencil)
                patterns = {j: set() for j in range(6)}
                owners = {}
                for coord, coefficient in tensor.items():
                    if coord[spectator] != level:
                        continue
                    index, cell = coord[pencil], (coord[row_axis], coord[col_axis])
                    if cell in owners or coefficient == (0, 0):
                        raise ValueError("overlapping pencil cells or zero coefficient")
                    owners[cell] = index
                    patterns[index].add(cell)
                if any(not patterns[j] for j in range(6)):
                    raise ValueError("pencil basis matrix missing")
                possible = []
                allowed = set()
                for mask in range(1, 64):
                    indices = [j for j in range(6) if mask & (1 << j)]
                    support = set().union(*(patterns[j] for j in indices))
                    rows = {r for r, c in support}
                    cols = {c for r, c in support}
                    if len(support) == len(rows) * len(cols):
                        possible.append(indices)
                        allowed.update(indices)
                # Every rank-one pencil coefficient vector is in span(allowed).
                # Six independent basis vectors contain at most |allowed| in it.
                bound = 12 - len(allowed)
                choices.append({"pencil_axis": pencil, "possible_rectangular_masks": possible,
                                "allowed_coordinates_for_rank_one": sorted(allowed),
                                "basis_rank_sum_lower_bound": bound})
            report.append({"spectator": spectator, "level": level,
                           "best_bound": max(r["basis_rank_sum_lower_bound"] for r in choices),
                           "choices": choices})
    totals = [{"spectator": i, "support_lower_bound": sum(r["best_bound"] for r in report if r["spectator"] == i)} for i in range(4)]
    result = {"table_sha256": table_sha, "per_slice": report, "totals_by_spectator": totals,
              "scope": "necessary rectangle-support filter; no claim of rank-one realizability, or global optimum"}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    json.dump({"table_sha256": table_sha, "totals_by_spectator": totals,
               "bound_histogram": dict(sorted(collections.Counter(r["best_bound"] for r in report).items())),
               "scope": result["scope"]}, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()

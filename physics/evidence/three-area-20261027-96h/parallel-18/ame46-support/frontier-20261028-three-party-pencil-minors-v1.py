#!/usr/bin/env python3
"""Find support-forced monomial 2x2 minors in each spectator-slice pencil.

For a three-way slice, fix one active index j and regard the other two as a
matrix. A two-entry j-slice whose cross positions are absent from ALL j-slices
has a 2x2 minor c*x_j^2, and forces pencil rank>=2 whenever x_j!=0.
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
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    tensor, table_sha = mod.load_table(args.table)
    report = []
    for spectator in range(4):
        active = [i for i in range(4) if i != spectator]
        for level in range(6):
            choices = []
            for pencil in active:
                row_axis, col_axis = (i for i in active if i != pencil)
                positions = collections.defaultdict(list)
                occupied = set()
                for coordinate, coeff in tensor.items():
                    if coordinate[spectator] != level:
                        continue
                    r, c = coordinate[row_axis], coordinate[col_axis]
                    if (r, c) in occupied:
                        raise ValueError(f"pencil-position collision: {spectator}, {level}, {pencil}, {(r,c)}")
                    positions[coordinate[pencil]].append((r, c, coeff))
                    occupied.add((r, c))
                if any(not positions[k] for k in range(6)):
                    raise ValueError(f"zero pencil basis matrix: {spectator}, {level}, {pencil}")
                certificates = []
                for k in range(6):
                    for (r, c, x), (s, d, y) in itertools.combinations(positions[k], 2):
                        if r != s and c != d and (r, d) not in occupied and (s, c) not in occupied:
                            certificates.append({"pencil_index": k, "row_pair": [r, s], "column_pair": [c, d],
                                                 "coefficient1_Qsqrt2": x, "coefficient2_Qsqrt2": y})
                            break
                rank1_parameter_count = 6 - len(certificates)
                bound = 12 - rank1_parameter_count
                choices.append({"pencil_axis": pencil, "row_axis": row_axis, "col_axis": col_axis,
                                "source_nnz_by_pencil_index": [len(positions[k]) for k in range(6)],
                                "certified_indices": [x["pencil_index"] for x in certificates],
                                "rank_at_least_two_when_any_certified_coordinate_nonzero": True,
                                "basis_rank_sum_lower_bound": bound,
                                "minor_certificates": certificates})
            best = max(x["basis_rank_sum_lower_bound"] for x in choices)
            actual_support = sum(1 for x in tensor if x[spectator] == level)
            report.append({"spectator": spectator, "level": level, "original_slice_support": actual_support,
                           "best_basis_rank_sum_lower_bound": best, "choices": choices})
    totals = [{"spectator": i,
               "support_lower_bound": sum(r["best_basis_rank_sum_lower_bound"] for r in report if r["spectator"] == i)}
              for i in range(4)]
    result = {"table_sha256": table_sha, "per_slice": report, "totals_by_spectator": totals,
              "criterion": "a nonzero certified coordinate makes an isolated x_j^2 minor nonzero over any field; rank-one pencils are confined to the complementary coordinate subspace",
              "limitations": "A valid lower bound, not necessarily the exact minimum basis-rank sum. Specific witness, no four-party/global AME claim."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    json.dump({"table_sha256": table_sha, "totals_by_spectator": totals,
               "bounds_histogram": dict(sorted(collections.Counter(r["best_basis_rank_sum_lower_bound"] for r in report).items())),
               "limits": result["limitations"]}, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()

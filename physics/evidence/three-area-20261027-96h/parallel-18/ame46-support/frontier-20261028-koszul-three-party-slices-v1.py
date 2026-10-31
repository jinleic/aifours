#!/usr/bin/env python3
"""Modular Koszul flattening rank lower bounds for three-party slices.

For each spectator basis level, form wedge-2 flattenings along each remaining
party. Reduction in F_17 with sqrt(2)=6 gives a certified lower bound on
characteristic-zero rank of the corresponding Q(sqrt(2)) matrix. No numerical
linear algebra or random search is used.
"""
import argparse
import collections
import importlib.util
import itertools
import json
from pathlib import Path
import sys

PRIME = 17
ROOT2 = 6
N = 6


def rank_mod(matrix):
    rows, cols = len(matrix), len(matrix[0])
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if matrix[r][col] % PRIME), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        piv = matrix[pivot_row]
        inv = pow(piv[col], -1, PRIME)
        for r in range(pivot_row + 1, rows):
            row = matrix[r]
            scale = row[col] * inv % PRIME
            if not scale:
                continue
            for k in range(col, cols):
                row[k] = (row[k] - scale * piv[k]) % PRIME
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def flatten(tensor, spectator, level, wedge_axis):
    others = tuple(i for i in range(4) if i not in (spectator, wedge_axis))
    b_axis, c_axis = others
    pairs = tuple(itertools.combinations(range(N), 2))
    triples = tuple(itertools.combinations(range(N), 3))
    triple_index = {x: i for i, x in enumerate(triples)}
    matrix = [[0] * (len(pairs) * N) for _ in range(len(triples) * N)]
    for index, (rational, radical) in tensor.items():
        if index[spectator] != level:
            continue
        a, b, c = index[wedge_axis], index[b_axis], index[c_axis]
        value = (rational + ROOT2 * radical) % PRIME
        for j, wedge in enumerate(pairs):
            if a in wedge:
                continue
            sign = -1 if sum(x < a for x in wedge) % 2 else 1
            ordered = tuple(sorted((a,) + wedge))
            row = triple_index[ordered] * N + c
            col = j * N + b
            matrix[row][col] = (matrix[row][col] + sign * value) % PRIME
    return matrix


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("verifier", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if ROOT2 * ROOT2 % PRIME != 2:
        raise ValueError("invalid modular square root")
    spec = importlib.util.spec_from_file_location("dense_verifier", args.verifier)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    tensor, table_sha = module.load_table(args.table)
    results = []
    for spectator in range(4):
        for level in range(N):
            ranks = []
            for wedge_axis in range(4):
                if wedge_axis == spectator:
                    continue
                rank = rank_mod(flatten(tensor, spectator, level, wedge_axis))
                ranks.append({"wedge_axis": wedge_axis, "modular_rank": rank,
                              "tensor_rank_lower_bound": (rank + 9) // 10})
            bound = max(item["tensor_rank_lower_bound"] for item in ranks)
            results.append({"spectator": spectator, "level": level, "flattenings": ranks, "best_lower_bound": bound})
    totals = [{"spectator": axis, "support_lower_bound": sum(r["best_lower_bound"] for r in results if r["spectator"] == axis)} for axis in range(4)]
    result = {"table_sha256": table_sha, "prime": PRIME, "root_of_two": ROOT2,
              "flattening": "Lambda^2(C^6) tensor B* -> Lambda^3(C^6) tensor C, 120 x 90",
              "rank_one_flattening_rank_bound": 10,
              "per_slice": results, "totals_by_spectator": totals,
              "limitations": "Rank modulo one prime is a lower bound, not proof of exact characteristic-zero rank; no four-party or global AME claim."}
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    json.dump({"table_sha256": table_sha, "prime": PRIME, "root_of_two": ROOT2,
               "totals_by_spectator": totals,
               "bound_histogram": dict(sorted(collections.Counter(r["best_lower_bound"] for r in results).items()))}, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()

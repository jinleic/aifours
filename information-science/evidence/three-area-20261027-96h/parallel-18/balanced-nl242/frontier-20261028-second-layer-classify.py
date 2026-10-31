#!/usr/bin/env python3
"""Independently verify and classify every reported two-step four-flip edge."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def read_first_seed(path):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not lines or len(lines[0]) != 128 or any(c not in "0123456789abcdefABCDEF" for c in lines[0]):
        raise ValueError("invalid first seed")
    value = int(lines[0], 16)
    return sum(((value >> (N - 1 - x)) & 1) << x for x in range(N))


def quad_mask(quad):
    if len(quad) != 4 or len(set(quad)) != 4 or any(type(x) is not int or not 0 <= x < N for x in quad):
        raise ValueError("invalid four-flip set")
    return sum(1 << x for x in quad)


def closure(vectors, cap):
    span = {0}
    for value in vectors:
        span |= {old ^ value for old in span}
        if len(span) > cap:
            raise ValueError("initial span exceeds cap")
    return span


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--first-layer", required=True, type=Path)
    parser.add_argument("--neighbors-receipt", required=True, type=Path)
    parser.add_argument("--second-layer", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-span", type=int, default=4096)
    args = parser.parse_args()
    initial = read_first_seed(args.seeds)
    first = json.loads(args.first_layer.read_text(encoding="utf-8"))["seeds"][0]
    neighbor_records = json.loads(args.neighbors_receipt.read_text(encoding="utf-8"))["records"]
    second = json.loads(args.second_layer.read_text(encoding="utf-8"))["seeds"]
    if len(first["preserving_quads"]) != len(neighbor_records) or len(second) != len(neighbor_records):
        raise ValueError("layer count mismatch")
    vectors = [quad_mask(q) for q in first["preserving_quads"]]
    initial_span = closure(vectors, args.max_span)
    phases = [sum(1 << x for x in range(N) if (a & x).bit_count() & 1) for a in range(N)]
    unique_tables = set()
    hist = collections.Counter()
    outside_edges = 0
    target_edges = 0
    unique_quads = set()
    for index, (record, row) in enumerate(zip(neighbor_records, second), 1):
        if record["line_1based"] != index or record["flips"] != first["preserving_quads"][index - 1]:
            raise ValueError("first-layer mapping mismatch")
        first_mask = quad_mask(record["flips"])
        first_value = initial ^ first_mask
        first_text = "".join(str((first_value >> x) & 1) for x in range(N))
        first_hex = f"{int(first_text, 2):0128X}"
        if hashlib.sha256(first_hex.encode("ascii")).hexdigest() != record["hex_sha256"]:
            raise ValueError("neighbor receipt hash mismatch")
        if len(row["preserving_quads"]) != row["peak_preserving_count"]:
            raise ValueError("second-layer count mismatch")
        observed_balanceable = 0
        for quad in row["preserving_quads"]:
            second_mask = quad_mask(quad)
            unique_quads.add(second_mask)
            combined = first_mask ^ second_mask
            if combined not in initial_span:
                outside_edges += 1
            table = initial ^ combined
            spectrum = [N - 2 * (table ^ phase).bit_count() for phase in phases]
            peak = max(map(abs, spectrum))
            if peak > 28:
                raise ValueError("reported preserving edge exceeds peak 28")
            zero = next((a for a, value in enumerate(spectrum) if value == 0), None)
            if zero is not None:
                observed_balanceable += 1
                target_edges += 1
                if target_edges == 1:
                    bits = "".join(str(((table >> x) & 1) ^ ((x & zero).bit_count() & 1)) for x in range(N))
                    name = args.output.parent / "frontier-20261028-second-layer-witness.json"
                    with name.open("x", encoding="utf-8") as file:
                        json.dump({"format": "boolean-truth-v1", "first_quad": record["flips"],
                                   "second_quad": quad, "affine_twist_frequency": zero, "bits": bits}, file, indent=2)
                        file.write("\n")
            unique_tables.add(table)
            hist[peak] += 1
        if observed_balanceable != row["balanceable_count"]:
            raise ValueError("second-layer balanceable count mismatch")
    outside_unique = sum((table ^ initial) not in initial_span for table in unique_tables)
    result = {"first_layer_nodes": len(second), "reported_edges": sum(hist.values()),
              "unique_second_tables": len(unique_tables), "outside_original_span_edges": outside_edges,
              "outside_original_span_unique_tables": outside_unique, "distinct_second_moves": len(unique_quads),
              "peak_histogram": dict(sorted(hist.items())), "balanceable_edges": target_edges,
              "completeness": "reported edges all independently verified; second-layer enumeration completeness not independently replayed"}
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "first_layer_sha256": hashlib.sha256(args.first_layer.read_bytes()).hexdigest(),
               "neighbor_receipt_sha256": hashlib.sha256(args.neighbors_receipt.read_bytes()).hexdigest(),
               "second_layer_sha256": hashlib.sha256(args.second_layer.read_bytes()).hexdigest(),
               "method": "full direct Hamming-character Walsh sums for each reported edge", "result": result}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"first_nodes={result['first_layer_nodes']} edges={result['reported_edges']} "
          f"unique={result['unique_second_tables']} outside_span={outside_unique} "
          f"moves={len(unique_quads)} target={target_edges}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

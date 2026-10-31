#!/usr/bin/env python3
"""Independently verify the expanded four-flip span with elimination and FWHT."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def basis(vectors):
    rows = []
    for value in vectors:
        for row in rows:
            value = min(value, value ^ row)
        if value:
            rows.append(value)
            rows.sort(reverse=True)
    return rows


def walsh(bits):
    values = [1 - 2 * ((bits >> x) & 1) for x in range(N)]
    for dimension in range(9):
        step = 1 << dimension
        for base in range(0, N, step * 2):
            for j in range(step):
                left, right = values[base + j], values[base + j + step]
                values[base + j], values[base + j + step] = left + right, left - right
    return values


def compare(actual, expected):
    for key in ("input_nodes", "distinct_moves", "distinct_points", "points", "all_move_xor_zero", "span_size",
                "span_rank", "peak_histogram", "min_peak", "peak_at_most_28", "target_count", "witness_file_written"):
        if actual[key] != expected[key]:
            raise ValueError(f"expanded span mismatch: {key}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--second-layer", required=True, type=Path)
    parser.add_argument("--expected", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-states", type=int, default=4096)
    args = parser.parse_args()
    lines = [line.strip() for line in args.seeds.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not lines or len(lines[0]) != 128 or any(c not in "0123456789abcdefABCDEF" for c in lines[0]):
        raise ValueError("invalid source seed")
    source = int(lines[0], 16)
    seed = sum(((source >> (N - 1 - x)) & 1) << x for x in range(N))
    nodes = json.loads(args.second_layer.read_text(encoding="utf-8"))["seeds"]
    expected = json.loads(args.expected.read_text(encoding="utf-8"))["result"]
    quads = set()
    for node in nodes:
        if len(node["preserving_quads"]) != node["peak_preserving_count"]:
            raise ValueError("bad node count")
        for q in node["preserving_quads"]:
            if len(q) != 4 or len(set(q)) != 4 or any(type(p) is not int or not 0 <= p < N for p in q):
                raise ValueError("invalid quad")
            quads.add(tuple(sorted(q)))
    points = sorted({x for q in quads for x in q})
    vectors = basis([sum(1 << x for x in q) for q in sorted(quads)])
    if (1 << len(vectors)) > args.max_states:
        raise ValueError("expanded span exceeds cap")
    spectra = collections.Counter()
    targets = 0
    for coefficient in range(1 << len(vectors)):
        value = seed
        for i, vector in enumerate(vectors):
            if (coefficient >> i) & 1:
                value ^= vector
        spectrum = walsh(value)
        peak = max(map(abs, spectrum))
        spectra[peak] += 1
        if peak <= 28 and 0 in spectrum:
            targets += 1
    actual = {"input_nodes": len(nodes), "distinct_moves": len(quads), "distinct_points": len(points),
              "points": points, "all_move_xor_zero": all(q[0] ^ q[1] ^ q[2] ^ q[3] == 0 for q in quads),
              "span_size": 1 << len(vectors), "span_rank": len(vectors),
              "peak_histogram": {str(k): v for k, v in sorted(spectra.items())},
              "min_peak": min(spectra), "peak_at_most_28": sum(v for k, v in spectra.items() if k <= 28),
              "target_count": targets, "witness_file_written": targets > 0}
    compare(actual, expected)
    altered = dict(expected)
    altered["target_count"] += 1
    try:
        compare(actual, altered)
    except ValueError as error:
        if str(error) != "expanded span mismatch: target_count":
            raise RuntimeError("mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("target-count mutation was not rejected")
    receipt = {"seed_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "second_layer_sha256": hashlib.sha256(args.second_layer.read_bytes()).hexdigest(),
               "expected_sha256": hashlib.sha256(args.expected.read_bytes()).hexdigest(),
               "method": "independent Gaussian elimination and FWHT on every span element",
               "actual": actual, "mutated_target_control": "rejected for expected reason"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"moves={len(quads)} points={len(points)} span={actual['span_size']} rank={actual['span_rank']} "
          f"hist={actual['peak_histogram']} target={targets} mutation=REJECTED")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

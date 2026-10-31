#!/usr/bin/env python3
"""Independently enumerate the move span and compute Walsh sums by parity masks."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def seed_tables(path):
    result = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid seed")
        value = int(line, 16)
        result.append(sum(((value >> (N - 1 - x)) & 1) << x for x in range(N)))
    if not result:
        raise ValueError("no seeds")
    return result


def closure(vectors, cap):
    span = {0}
    for vector in vectors:
        span |= {item ^ vector for item in span}
        if len(span) > cap:
            raise ValueError("span exceeds explicit bound")
    return span


def compare_result(actual, reported):
    for key in ("move_count", "distinct_points", "affine_rank", "move_span_rank", "span_size", "exhausted",
                "min_peak", "peak_histogram", "peak_at_most_28", "peak_at_most_28_with_zero",
                "all_quadruple_xor_zero"):
        if actual[key] != reported[key]:
            raise ValueError(f"span summary mismatch: {key}")


def analyze(seed, quads, phase_masks, cap):
    if not quads or any(len(q) != 4 or len(set(q)) != 4 or any(not 0 <= p < N for p in q) for q in quads):
        raise ValueError("invalid four-flip generator")
    if len({tuple(q) for q in quads}) != len(quads):
        raise ValueError("duplicate four-flip generator")
    points = sorted({p for q in quads for p in q})
    differences = closure([point ^ points[0] for point in points], N)
    affine_rank = len(differences).bit_length() - 1
    vectors = [sum(1 << p for p in q) for q in quads]
    span = closure(vectors, cap)
    rank = len(span).bit_length() - 1
    if 1 << rank != len(span):
        raise RuntimeError("closure cardinality is not a power of two")
    histogram = collections.Counter()
    peak28 = zero_peak28 = 0
    for move in span:
        truth = seed ^ move
        spectrum = [N - 2 * (truth ^ phase).bit_count() for phase in phase_masks]
        peak = max(map(abs, spectrum))
        histogram[peak] += 1
        if peak <= 28:
            peak28 += 1
            if 0 in spectrum:
                zero_peak28 += 1
    return {"move_count": len(quads), "distinct_points": len(points), "affine_rank": affine_rank,
            "move_span_rank": rank, "span_size": len(span), "exhausted": True,
            "min_peak": min(histogram), "peak_histogram": {str(k): v for k, v in sorted(histogram.items())},
            "peak_at_most_28": peak28, "peak_at_most_28_with_zero": zero_peak28,
            "all_quadruple_xor_zero": all(q[0] ^ q[1] ^ q[2] ^ q[3] == 0 for q in quads)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--four-flip-result", required=True, type=Path)
    parser.add_argument("--span-result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-states", type=int, default=4096)
    args = parser.parse_args()
    tables = seed_tables(args.seeds)
    quads = json.loads(args.four_flip_result.read_text(encoding="utf-8"))["seeds"]
    reported = json.loads(args.span_result.read_text(encoding="utf-8"))["reports"]
    if len(tables) != len(quads) or len(tables) != len(reported):
        raise ValueError("seed count mismatch")
    phases = [sum(1 << x for x in range(N) if (a & x).bit_count() & 1) for a in range(N)]
    results = []
    for i, (seed, item, expected) in enumerate(zip(tables, quads, reported), 1):
        result = analyze(seed, item["preserving_quads"], phases, args.max_states)
        compare_result(result, expected)
        mutated = dict(expected)
        mutated["peak_at_most_28_with_zero"] = expected["peak_at_most_28_with_zero"] + 1
        try:
            compare_result(result, mutated)
        except ValueError as error:
            if str(error) != "span summary mismatch: peak_at_most_28_with_zero":
                raise RuntimeError("mutation rejected for wrong reason") from error
        else:
            raise RuntimeError("mutated target count was not rejected")
        results.append({"seed_index_1based": i, **result, "wrong_target_count_control": "rejected for expected reason"})
        print(f"seed={i} span={result['span_size']} hist={result['peak_histogram']} "
              f"peak28={result['peak_at_most_28']} target={result['peak_at_most_28_with_zero']} "
              f"mutation=REJECTED", flush=True)
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "four_flip_result_sha256": hashlib.sha256(args.four_flip_result.read_bytes()).hexdigest(),
               "span_result_sha256": hashlib.sha256(args.span_result.read_bytes()).hexdigest(),
               "method": "set-closure span plus 512 direct Hamming-distance parity-mask sums per truth table",
               "results": results}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

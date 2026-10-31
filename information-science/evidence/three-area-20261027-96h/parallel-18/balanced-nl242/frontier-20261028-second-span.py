#!/usr/bin/env python3
"""Exhaust the bounded GF(2) span of all reported second-layer four-flips."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def first_seed(path):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not lines or len(lines[0]) != 128 or any(c not in "0123456789abcdefABCDEF" for c in lines[0]):
        raise ValueError("invalid first seed")
    value = int(lines[0], 16)
    return sum(((value >> (N - 1 - x)) & 1) << x for x in range(N))


def closure(vectors, cap):
    result = {0}
    for value in vectors:
        result |= {x ^ value for x in result}
        if len(result) > cap:
            raise ValueError("span exceeds explicit search cap")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--second-layer", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-states", type=int, default=4096)
    args = parser.parse_args()
    seed = first_seed(args.seeds)
    rows = json.loads(args.second_layer.read_text(encoding="utf-8"))["seeds"]
    quads = set()
    for row in rows:
        if len(row["preserving_quads"]) != row["peak_preserving_count"]:
            raise ValueError("reported second-layer count mismatch")
        for quad in row["preserving_quads"]:
            if len(quad) != 4 or len(set(quad)) != 4 or any(type(x) is not int or not 0 <= x < N for x in quad):
                raise ValueError("invalid quadruple")
            quads.add(tuple(sorted(quad)))
    if not quads:
        raise ValueError("no moves")
    points = sorted({x for quad in quads for x in quad})
    span = closure((sum(1 << x for x in quad) for quad in sorted(quads)), args.max_states)
    phase_masks = [sum(1 << x for x in range(N) if (a & x).bit_count() & 1) for a in range(N)]
    peaks = collections.Counter()
    target_count = 0
    peak28 = 0
    min_peak = 999
    first_target = None
    for mask in span:
        truth = seed ^ mask
        spectrum = [N - 2 * (truth ^ char).bit_count() for char in phase_masks]
        peak = max(map(abs, spectrum))
        peaks[peak] += 1
        min_peak = min(min_peak, peak)
        zero = next((a for a, value in enumerate(spectrum) if value == 0), None)
        if peak <= 28:
            peak28 += 1
            if zero is not None:
                target_count += 1
                if first_target is None:
                    first_target = (mask, truth, zero)
    if first_target is not None:
        mask, truth, zero = first_target
        witness = {"format": "boolean-truth-v1", "source_seed_index_1based": 1,
                   "flip_indices": [x for x in range(N) if (mask >> x) & 1],
                   "affine_twist_frequency": zero,
                   "bits": "".join(str(((truth >> x) & 1) ^ ((x & zero).bit_count() & 1)) for x in range(N))}
        path = args.output.parent / "frontier-20261028-second-span-witness.json"
        with path.open("x", encoding="utf-8") as file:
            json.dump(witness, file, indent=2)
            file.write("\n")
    result = {"input_nodes": len(rows), "distinct_moves": len(quads), "distinct_points": len(points),
              "points": points, "all_move_xor_zero": all(q[0] ^ q[1] ^ q[2] ^ q[3] == 0 for q in quads),
              "span_size": len(span), "span_rank": len(span).bit_length() - 1,
              "peak_histogram": dict(sorted(peaks.items())), "min_peak": min_peak,
              "peak_at_most_28": peak28, "target_count": target_count,
              "witness_file_written": first_target is not None}
    receipt = {"seed_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "second_layer_sha256": hashlib.sha256(args.second_layer.read_bytes()).hexdigest(),
               "method": "exact GF(2) closure and 512 direct Hamming-character Walsh values per span member",
               "result": result}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"nodes={len(rows)} moves={len(quads)} points={len(points)} span={len(span)} "
          f"rank={result['span_rank']} peaks={dict(sorted(peaks.items()))} target={target_count}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

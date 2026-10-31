#!/usr/bin/env python3
"""Analyze and, if small, exhaust the binary span of peak-preserving four-flips."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def seeds(path):
    result = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid published seed")
        value = int(line, 16)
        result.append(sum(((value >> (N - 1 - x)) & 1) << x for x in range(N)))
    return result


def basis(vectors):
    pivots = {}
    for value in vectors:
        while value:
            p = value.bit_length() - 1
            if p in pivots:
                value ^= pivots[p]
            else:
                pivots[p] = value
                break
    return list(pivots.values())


def walsh(bits):
    w = [1 - 2 * ((bits >> x) & 1) for x in range(N)]
    step = 1
    while step < N:
        for base in range(0, N, 2 * step):
            for offset in range(step):
                u, v = w[base + offset], w[base + step + offset]
                w[base + offset], w[base + step + offset] = u + v, u - v
        step *= 2
    return w


def analyze(seed, quads, cap, index, witness_dir):
    if not quads or any(len(q) != 4 or len(set(q)) != 4 or any(not 0 <= p < N for p in q) for q in quads):
        raise ValueError("invalid preserving quadruples")
    if len({tuple(q) for q in quads}) != len(quads):
        raise ValueError("duplicate preserving quadruple")
    points = sorted({p for q in quads for p in q})
    affine_rank = len(basis([p ^ points[0] for p in points[1:]]))
    move_basis = basis([sum(1 << p for p in q) for q in quads])
    rank = len(move_basis)
    result = {"move_count": len(quads), "distinct_points": len(points), "points": points,
              "affine_rank": affine_rank, "move_span_rank": rank,
              "all_quadruple_xor_zero": all(q[0] ^ q[1] ^ q[2] ^ q[3] == 0 for q in quads),
              "span_size": 1 << rank, "cap": cap, "exhausted": False}
    if 1 << rank > cap:
        return result
    current = seed
    last_gray = 0
    peak_hist = collections.Counter()
    target = peak28 = zero_peak28 = 0
    min_peak = 999
    for index_gray in range(1 << rank):
        gray = index_gray ^ (index_gray >> 1)
        if index_gray:
            difference = gray ^ last_gray
            current ^= move_basis[difference.bit_length() - 1]
        last_gray = gray
        spectrum = walsh(current)
        peak = max(map(abs, spectrum))
        peak_hist[peak] += 1
        min_peak = min(min_peak, peak)
        zero = next((a for a, value in enumerate(spectrum) if value == 0), None)
        if peak <= 28:
            peak28 += 1
            if zero is not None:
                zero_peak28 += 1
                if target == 0:
                    target = 1
                    table = "".join(str(((current >> x) & 1) ^ ((x & zero).bit_count() & 1)) for x in range(N))
                    output = witness_dir / f"frontier-20261028-flip-span-witness-seed{index}.json"
                    with output.open("x", encoding="utf-8") as file:
                        json.dump({"format": "boolean-truth-v1", "seed_index_1based": index,
                                   "gray_index": index_gray, "affine_twist_frequency": zero, "bits": table}, file, indent=2)
                        file.write("\n")
    result.update({"exhausted": True, "tested": 1 << rank, "min_peak": min_peak,
                   "peak_histogram": dict(sorted(peak_hist.items())),
                   "peak_at_most_28": peak28, "peak_at_most_28_with_zero": zero_peak28,
                   "witness_file_written": bool(target)})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--four-flip-result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-states", type=int, default=4096)
    args = parser.parse_args()
    if args.max_states < 1:
        raise ValueError("max states must be positive")
    inputs = seeds(args.seeds)
    search = json.loads(args.four_flip_result.read_text(encoding="utf-8"))["seeds"]
    if len(inputs) != len(search):
        raise ValueError("seed count mismatch")
    reports = []
    for index, (seed, item) in enumerate(zip(inputs, search), 1):
        result = analyze(seed, item["preserving_quads"], args.max_states, index, args.output.parent)
        reports.append({"seed_index_1based": index, **result})
        print(f"seed={index} moves={result['move_count']} points={result['distinct_points']} "
              f"affine_rank={result['affine_rank']} span_rank={result['move_span_rank']} "
              f"span_size={result['span_size']} exhausted={result['exhausted']} "
              f"target={result.get('peak_at_most_28_with_zero', 'not-tested')}", flush=True)
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "four_flip_result_sha256": hashlib.sha256(args.four_flip_result.read_bytes()).hexdigest(),
               "method": "binary row elimination and exact FWHT on each span member if within cap", "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

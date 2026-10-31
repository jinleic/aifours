#!/usr/bin/env python3
"""Count peak-worsening sets and their pairwise intersections for each seed."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def seeds(path):
    tables = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid seed")
        value = int(line, 16)
        tables.append([(value >> (N - 1 - x)) & 1 for x in range(N)])
    if not tables:
        raise ValueError("no seeds")
    return tables


def analyze(bits):
    signs = [1 - 2 * bit for bit in bits]
    w = [sum(signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(N))
         for a in range(N)]
    if max(map(abs, w)) != 28 or any(v % 4 for v in w):
        raise ValueError("seed must have 4-divisible Walsh peak 28")
    peaks = [(a, 1 if value > 0 else -1) for a, value in enumerate(w) if abs(value) == 28]
    masks = [sum(1 << index for index, (a, peak_sign) in enumerate(peaks)
                 if peak_sign * signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) < 0)
             for x in range(N)]
    one_hist = collections.Counter(mask.bit_count() for mask in masks)
    pair_hist = collections.Counter((masks[x] & masks[y]).bit_count()
                                    for x in range(N) for y in range(x + 1, N))
    return {"peak_count": len(peaks), "single_bad_peak_min": min(one_hist),
            "single_bad_peak_max": max(one_hist), "single_bad_peak_histogram": dict(sorted(one_hist.items())),
            "pair_common_bad_peak_min": min(pair_hist), "pair_common_bad_peak_max": max(pair_hist),
            "pair_common_bad_peak_histogram": dict(sorted(pair_hist.items())),
            "pair_count": sum(pair_hist.values())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    reports = []
    for index, bits in enumerate(seeds(args.seeds), 1):
        result = analyze(bits)
        reports.append({"seed_index_1based": index, **result})
        print(f"seed={index} single_bad_min={result['single_bad_peak_min']} "
              f"pair_common_bad_min={result['pair_common_bad_peak_min']} "
              f"pair_common_bad_max={result['pair_common_bad_peak_max']} pairs={result['pair_count']}")
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "method": "direct Walsh sums plus bitsets of individually worsening original peaks",
               "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

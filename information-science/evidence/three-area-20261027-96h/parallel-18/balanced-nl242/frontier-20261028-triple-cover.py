#!/usr/bin/env python3
"""Exactly count peak-worsening triples for each published Boolean seed."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def read_seeds(path):
    result = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid 512-bit seed")
        n = int(line, 16)
        result.append([(n >> (N - 1 - x)) & 1 for x in range(N)])
    if not result:
        raise ValueError("no seeds")
    return result


def analyze(bits):
    signs = [1 - 2 * bit for bit in bits]
    w = [sum(signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(N))
         for a in range(N)]
    if max(map(abs, w)) != 28 or any(v % 4 for v in w):
        raise ValueError("seed requires a 4-divisible peak-28 spectrum")
    peaks = [(a, 1 if value > 0 else -1) for a, value in enumerate(w) if abs(value) == 28]
    bad = [sum(1 << index for index, (a, peak_sign) in enumerate(peaks)
               if peak_sign * signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) < 0)
           for x in range(N)]
    counts = collections.Counter()
    first_uncovered = None
    for x in range(N - 2):
        for y in range(x + 1, N - 1):
            common = bad[x] & bad[y]
            for z in range(y + 1, N):
                n = (common & bad[z]).bit_count()
                counts[n] += 1
                if n == 0 and first_uncovered is None:
                    first_uncovered = [x, y, z]
    total = sum(counts.values())
    if total != N * (N - 1) * (N - 2) // 6:
        raise RuntimeError("triple count incomplete")
    return {"peak_count": len(peaks), "triples": total, "uncovered": counts.get(0, 0),
            "minimum_common_bad_peaks": min(counts), "maximum_common_bad_peaks": max(counts),
            "first_uncovered": first_uncovered, "histogram": dict(sorted(counts.items()))}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    reports = []
    for index, bits in enumerate(read_seeds(args.seeds), 1):
        result = analyze(bits)
        reports.append({"seed_index_1based": index, **result})
        print(f"seed={index} triples={result['triples']} uncovered={result['uncovered']} "
              f"min_common={result['minimum_common_bad_peaks']} max_common={result['maximum_common_bad_peaks']}",
              flush=True)
    receipt = {"seed_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "method": "direct 512x512 Walsh sums and exact bitset triple intersections", "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

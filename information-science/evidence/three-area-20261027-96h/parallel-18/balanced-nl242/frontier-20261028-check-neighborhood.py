#!/usr/bin/env python3
"""Independently recount all two-flip/affine-balance neighbors using bit masks."""

import argparse
import hashlib
import json
from pathlib import Path

N = 512
ALL = (1 << N) - 1


def read_seeds(path):
    seeds = []
    for number, line in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError(f"invalid 512-bit hex table at line {number}")
        value = int(line, 16)
        seeds.append([(value >> (N - 1 - x)) & 1 for x in range(N)])
    if not seeds:
        raise ValueError("no seed tables")
    return seeds


def recount(bits):
    signs = [1 - 2 * bit for bit in bits]
    spectrum = [
        sum(sign * (1 - 2 * ((a & x).bit_count() & 1)) for x, sign in enumerate(signs))
        for a in range(N)
    ]
    if max(map(abs, spectrum)) != 28 or any(w == 0 or w % 4 for w in spectrum):
        raise ValueError("seed does not have the required zero-free, 4-divisible peak-28 spectrum")
    plus4 = sum(1 << a for a, w in enumerate(spectrum) if w == 4)
    minus4 = sum(1 << a for a, w in enumerate(spectrum) if w == -4)
    plus28 = sum(1 << a for a, w in enumerate(spectrum) if w == 28)
    minus28 = sum(1 << a for a, w in enumerate(spectrum) if w == -28)
    positive = [
        sum(1 << a for a in range(N) if bits[x] == ((a & x).bit_count() & 1))
        for x in range(N)
    ]
    pairs = balanceable = twists = targets = 0
    histogram = {}
    for x in range(N):
        xp, xm = positive[x], ALL ^ positive[x]
        for y in range(x + 1, N):
            pairs += 1
            yp, ym = positive[y], ALL ^ positive[y]
            zero_mask = (plus4 & xp & yp) | (minus4 & xm & ym)
            if not zero_mask:
                continue
            balanceable += 1
            twists += zero_mask.bit_count()
            violation = (plus28 & xm & ym) | (minus28 & xp & yp)
            if violation:
                peak = 32
            else:
                peak = max(abs(spectrum[a] - 2 * signs[x] * (1 - 2 * ((a & x).bit_count() & 1))
                               - 2 * signs[y] * (1 - 2 * ((a & y).bit_count() & 1)))
                           for a in range(N))
                if peak <= 28:
                    targets += 1
            histogram[str(peak)] = histogram.get(str(peak), 0) + 1
    return {
        "pairs": pairs,
        "balanceable_pairs": balanceable,
        "balanceable_twists": twists,
        "target_pairs": targets,
        "best_peak": min(map(int, histogram)),
        "peak_histogram": histogram,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=Path, required=True)
    parser.add_argument("--search-result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    seeds = read_seeds(args.seeds)
    search = json.loads(args.search_result.read_text(encoding="utf-8"))["seeds"]
    if len(seeds) != len(search):
        raise ValueError("seed count differs from search result")
    audits = []
    keys = ("pairs", "balanceable_pairs", "balanceable_twists", "target_pairs", "best_peak", "peak_histogram")
    for i, bits in enumerate(seeds):
        found = recount(bits)
        mismatches = {key: {"search": search[i][key], "independent": found[key]}
                      for key in keys if search[i][key] != found[key]}
        audits.append({"seed_index_1based": i + 1, "independent": found, "mismatches": mismatches})
        print(f"seed={i + 1} pairs={found['pairs']} balanceable={found['balanceable_pairs']} "
              f"twists={found['balanceable_twists']} min_peak={found['best_peak']} "
              f"target_pairs={found['target_pairs']} mismatches={len(mismatches)}")
    result = {
        "seed_file_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
        "search_result_sha256": hashlib.sha256(args.search_result.read_bytes()).hexdigest(),
        "method": "direct character-sum spectrum and independent 512-bit pair masks",
        "audits": audits,
        "all_match": all(not item["mismatches"] for item in audits),
    }
    with args.output.open("x", encoding="utf-8") as output:
        json.dump(result, output, indent=2)
        output.write("\n")
    if not result["all_match"]:
        raise SystemExit("independent recount mismatch")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

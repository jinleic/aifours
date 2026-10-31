#!/usr/bin/env python3
"""Independently count one- and two-bit peak-preserving moves by scalar inequalities."""

import argparse
import hashlib
import json
from pathlib import Path

N = 512


def read_seeds(path):
    tables = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid seed")
        number = int(line, 16)
        tables.append([(number >> (N - 1 - x)) & 1 for x in range(N)])
    if not tables:
        raise ValueError("no seeds")
    return tables


def count_moves(bits):
    signs = [1 - 2 * v for v in bits]
    w = [sum(signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(N))
         for a in range(N)]
    if max(map(abs, w)) != 28 or any(v % 4 for v in w):
        raise ValueError("seed requires peak 28 and a 4-divisible spectrum")
    peaks = [(a, 1 if v > 0 else -1) for a, v in enumerate(w) if abs(v) == 28]
    single_hist = {"26": 0, "30": 0}
    pair_hist = {"28_or_less": 0, "32": 0}
    for x in range(N):
        violates = any(peak_sign * signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) < 0
                       for a, peak_sign in peaks)
        single_hist["30" if violates else "26"] += 1
        for y in range(x + 1, N):
            violates = any(
                peak_sign * (signs[x] * (1 - 2 * ((a & x).bit_count() & 1))
                             + signs[y] * (1 - 2 * ((a & y).bit_count() & 1))) < 0
                for a, peak_sign in peaks
            )
            pair_hist["32" if violates else "28_or_less"] += 1
    return {"peak_count": len(peaks), "single_flip_peak_histogram": single_hist,
            "two_flip_peak_class_histogram": pair_hist}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--plateau-result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    seeds = read_seeds(args.seeds)
    prior = json.loads(args.plateau_result.read_text(encoding="utf-8"))["reports"]
    if len(seeds) != len(prior):
        raise ValueError("seed count mismatch")
    results = []
    for i, bits in enumerate(seeds):
        result = count_moves(bits)
        actual = result["two_flip_peak_class_histogram"]["28_or_less"]
        if actual != prior[i]["peak_preserving"]:
            raise RuntimeError("independent plateau count differs")
        results.append({"seed_index_1based": i + 1, **result, "agrees_with_mask_counter": True})
        print(f"seed={i + 1} peaks={result['peak_count']} singles={result['single_flip_peak_histogram']} "
              f"pairs={result['two_flip_peak_class_histogram']} agreement=YES")
    output = {"seed_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
              "prior_sha256": hashlib.sha256(args.plateau_result.read_bytes()).hexdigest(),
              "method": "direct character-sum spectrum and per-peak scalar inequalities",
              "results": results}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(output, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

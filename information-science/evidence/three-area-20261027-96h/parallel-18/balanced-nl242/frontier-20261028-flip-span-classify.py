#!/usr/bin/env python3
"""Classify complete Walsh histograms across each exact local flip span."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def load_seeds(path):
    tables = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid seed")
        value = int(line, 16)
        tables.append(sum(((value >> (N - 1 - x)) & 1) << x for x in range(N)))
    if not tables:
        raise ValueError("no seeds")
    return tables


def closure(quads, cap):
    span = {0}
    for quad in quads:
        if len(quad) != 4 or len(set(quad)) != 4 or any(not 0 <= x < N for x in quad):
            raise ValueError("invalid quadruple")
        vector = sum(1 << x for x in quad)
        span |= {v ^ vector for v in span}
        if len(span) > cap:
            raise ValueError("span exceeds cap")
    return span


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--quads", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-states", type=int, default=4096)
    args = parser.parse_args()
    tables = load_seeds(args.seeds)
    records = json.loads(args.quads.read_text(encoding="utf-8"))["seeds"]
    if len(tables) != len(records):
        raise ValueError("seed count mismatch")
    phases = [sum(1 << x for x in range(N) if (a & x).bit_count() & 1) for a in range(N)]
    reports = []
    for index, (seed, record) in enumerate(zip(tables, records), 1):
        span = closure(record["preserving_quads"], args.max_states)
        classes = collections.Counter()
        weight_counts = collections.Counter()
        zero_counts = collections.Counter()
        for move in span:
            table = seed ^ move
            spectrum = [N - 2 * (table ^ mask).bit_count() for mask in phases]
            peak = max(map(abs, spectrum))
            if peak <= 28:
                histogram = tuple(sorted(collections.Counter(map(abs, spectrum)).items()))
                classes[histogram] += 1
                weight_counts[table.bit_count()] += 1
                zero_counts[spectrum.count(0)] += 1
        report = {"seed_index_1based": index, "span_size": len(span),
                  "peak_at_most_28": sum(classes.values()),
                  "absolute_spectrum_classes": [{"histogram": dict(key), "count": value}
                                                for key, value in sorted(classes.items())],
                  "truth_weight_histogram": dict(sorted(weight_counts.items())),
                  "walsh_zero_count_histogram": dict(sorted(zero_counts.items()))}
        reports.append(report)
        print(f"seed={index} span={len(span)} peak28={report['peak_at_most_28']} "
              f"spectrum_classes={len(classes)} weights={dict(sorted(weight_counts.items()))} "
              f"zeros={dict(sorted(zero_counts.items()))}", flush=True)
    receipt = {"seed_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "quad_result_sha256": hashlib.sha256(args.quads.read_bytes()).hexdigest(),
               "method": "GF(2) set closure and direct 512-bit Hamming-character Walsh sums", "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

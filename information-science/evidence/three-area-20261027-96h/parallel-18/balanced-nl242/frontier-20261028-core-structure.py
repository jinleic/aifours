#!/usr/bin/env python3
"""Describe the complete affine core and exact outside Walsh contributions."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def row_basis(vectors):
    pivots = {}
    for v in vectors:
        while v:
            p = v.bit_length() - 1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p] = v
                break
    return list(pivots.values())


def linear_combination(mask, rows):
    result = 0
    for i, row in enumerate(rows):
        if (mask >> i) & 1:
            result ^= row
    return result


def gf2_rank(rows):
    return len(row_basis(rows))


def analyze(seed_line, points):
    if len(seed_line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in seed_line):
        raise ValueError("invalid seed")
    value = int(seed_line, 16)
    bits = [(value >> (N - 1 - x)) & 1 for x in range(N)]
    if len(points) != 15 or len(set(points)) != 15:
        raise ValueError("expected 15 distinct core positions")
    anchor = points[0]
    rows = row_basis([p ^ anchor for p in points[1:]])
    if len(rows) != 4:
        raise ValueError("core does not have affine rank four")
    hull = {anchor ^ linear_combination(u, rows) for u in range(16)}
    missing = hull - set(points)
    if len(missing) != 1:
        raise ValueError("core is not a punctured four-flat")
    origin = next(iter(missing))
    values = [bits[origin ^ linear_combination(u, rows)] for u in range(16)]
    anf = values.copy()
    for i in range(4):
        for u in range(16):
            if (u >> i) & 1:
                anf[u] ^= anf[u ^ (1 << i)]
    degree = max((u.bit_count() for u, bit in enumerate(anf) if bit), default=-1)
    polar = []
    for i in range(4):
        row = 0
        for j in range(4):
            value_ij = values[(1 << i) ^ (1 << j)] ^ values[1 << i] ^ values[1 << j] ^ values[0]
            row |= value_ij << j
        polar.append(row)
    local_walsh = [sum((1 - 2 * values[u]) * (1 - 2 * ((alpha & u).bit_count() & 1))
                       for u in range(16)) for alpha in range(16)]
    global_walsh = [sum((1 - 2 * bits[x]) * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(N))
                    for a in range(N)]
    groups = [collections.Counter() for _ in range(16)]
    for a in range(N):
        alpha = sum(((a & row).bit_count() & 1) << i for i, row in enumerate(rows))
        orientation = 1 - 2 * ((a & origin).bit_count() & 1)
        outside = orientation * global_walsh[a] - local_walsh[alpha]
        groups[alpha][outside] += 1
    signatures = collections.Counter(tuple(sorted(group.items())) for group in groups)
    return {"origin_missing": origin, "linear_basis": rows, "core_points": sorted(points),
            "local_truth_bits": "".join(map(str, values)), "local_anf_degree": degree,
            "local_polar_rank": gf2_rank(polar), "local_walsh_histogram": dict(sorted(collections.Counter(local_walsh).items())),
            "outside_contribution_classes": [{"histogram": dict(key), "alpha_count": count}
                                             for key, count in sorted(signatures.items())],
            "outside_histograms_by_alpha": [dict(sorted(group.items())) for group in groups]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--span-results", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    lines = [line.strip() for line in args.seeds.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    records = json.loads(args.span_results.read_text(encoding="utf-8"))["reports"]
    if len(lines) != len(records):
        raise ValueError("seed and span record counts differ")
    reports = []
    for index, (line, record) in enumerate(zip(lines, records), 1):
        result = analyze(line, record["points"])
        reports.append({"seed_index_1based": index, **result})
        print(f"seed={index} origin={result['origin_missing']} basis={result['linear_basis']} "
              f"degree={result['local_anf_degree']} polar_rank={result['local_polar_rank']} "
              f"local_W={result['local_walsh_histogram']} "
              f"outside_classes={result['outside_contribution_classes']}", flush=True)
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "span_results_sha256": hashlib.sha256(args.span_results.read_bytes()).hexdigest(),
               "method": "exact affine hull, Möbius coefficients and direct local/global character sums", "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

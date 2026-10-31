#!/usr/bin/env python3
"""Verify outside-four-flat character sums directly for all 512 frequencies."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512
X = ((-22, 15), (-6, 1), (10, 5), (26, 11))
Y = ((-22, 16), (10, 4), (26, 12))


def seed_tables(path):
    result = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid seed")
        number = int(line, 16)
        result.append([(number >> (N - 1 - x)) & 1 for x in range(N)])
    if not result:
        raise ValueError("no seed tables")
    return result


def verify_basis(points, origin, basis):
    if len(basis) != 4 or any(type(v) is not int or not 0 < v < N for v in basis):
        raise ValueError("invalid basis")
    values = []
    for mask in range(16):
        x = origin
        for i, b in enumerate(basis):
            if mask & (1 << i):
                x ^= b
        values.append(x)
    if len(set(values)) != 16:
        raise ValueError("basis is not independent")
    if len(points) != 15 or set(values) - set(points) != {origin} or not set(points) < set(values):
        raise ValueError("reported points do not puncture the affine hull at origin")
    return set(values)


def check(bits, points, info):
    origin, basis = info["core_origin"], info["basis"]
    hull = verify_basis(points, origin, basis)
    signs = [1 - 2 * bit for bit in bits]
    groups = [collections.Counter() for _ in range(16)]
    for a in range(N):
        alpha = sum(((a & b).bit_count() & 1) << i for i, b in enumerate(basis))
        orient = 1 - 2 * ((a & origin).bit_count() & 1)
        outside = sum(signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(N) if x not in hull)
        groups[alpha][orient * outside] += 1
    signatures = collections.Counter(tuple(sorted(group.items())) for group in groups)
    if signatures != {X: 6, Y: 10}:
        raise ValueError("outside contribution signature mismatch")
    if info["outside_histograms"] != [dict((str(k), v) for k, v in sorted(g.items())) for g in groups]:
        raise ValueError("outside per-frequency-class histogram mismatch")
    try:
        verify_basis(points, origin, [basis[0], basis[0], basis[2], basis[3]])
    except ValueError as error:
        if str(error) != "basis is not independent":
            raise RuntimeError("basis mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("duplicate-basis control was not rejected")
    return {"origin": origin, "basis": basis, "frequency_classes": 16,
            "frequencies_per_class": 32, "signature_X_count": 6, "signature_Y_count": 10,
            "duplicate_basis_control": "rejected for expected reason"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--spans", required=True, type=Path)
    parser.add_argument("--census", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    seeds = seed_tables(args.seeds)
    spans = json.loads(args.spans.read_text(encoding="utf-8"))["reports"]
    census = json.loads(args.census.read_text(encoding="utf-8"))["reports"]
    if len(seeds) != len(spans) or len(seeds) != len(census):
        raise ValueError("input count mismatch")
    reports = []
    for index, (bits, span, info) in enumerate(zip(seeds, spans, census), 1):
        result = check(bits, span["points"], info)
        reports.append({"seed_index_1based": index, **result})
        print(f"seed={index} alpha_classes=16 X=6 Y=10 direct_outside_sums=PASS basis_mutation=REJECTED")
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "spans_sha256": hashlib.sha256(args.spans.read_bytes()).hexdigest(),
               "census_sha256": hashlib.sha256(args.census.read_bytes()).hexdigest(),
               "method": "512 direct sums on outside points, independent of FWHT core census",
               "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Recount outer interval profiles and verify their elementary impossibility cases."""

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
            raise ValueError("invalid seed")
        value = int(line, 16)
        result.append([(value >> (N - 1 - x)) & 1 for x in range(N)])
    return result


def verify_case(profile, kind):
    if kind == "single":
        if profile != ((-2, 0),) * 16:
            raise ValueError("unexpected single-flip interval profile")
        # Energy 64 forces all sixteen q_i=-2, whose sum is -32 rather than ±8.
        return "energy64 forces sum -32"
    large = [item for item in profile if item[0] < -1 or item[1] > 1]
    if len(large) <= 2 and all(-3 <= lo <= hi <= 1 for lo, hi in profile):
        # At most two |q| can exceed 1, so sum q_i² ≤ 2*9+14=32.
        return "energy at most 32"
    if profile == ((-3, 1),) * 8 + ((-1, -1),) * 8:
        # The fixed block contributes sum -8, energy 8. The other block needs
        # sum 0 or 16 and energy 56. Sum 16 is impossible (q≤1); at sum 0,
        # q²≤3−2q gives energy ≤24, also impossible.
        return "exceptional block violates sum/energy bound"
    raise ValueError("unclassified pair interval profile")


def recount(bits, origin, basis):
    coordinates = []
    for mask in range(16):
        x = origin
        for i, b in enumerate(basis):
            if mask & (1 << i):
                x ^= b
        coordinates.append(x)
    if len(set(coordinates)) != 16:
        raise ValueError("invalid affine core")
    inside = set(coordinates)
    outside = [x for x in range(N) if x not in inside]
    signs = [1 - 2 * bit for bit in bits]
    groups = [[] for _ in range(16)]
    for a in range(N):
        alpha = sum(((a & b).bit_count() & 1) << i for i, b in enumerate(basis))
        groups[alpha].append(a)
    delta = [[-2 * signs[x] * (1 - 2 * ((a & (x ^ origin)).bit_count() & 1))
              for a in range(N)] for x in outside]
    base = [sum(-row[a] // 2 for row in delta) for a in range(N)]
    counts = {"single": collections.Counter(), "pair": collections.Counter()}
    for kind in ("single", "pair"):
        for i, first in enumerate(delta):
            others = (None,) if kind == "single" else range(i + 1, len(delta))
            for j in others:
                second = None if j is None else delta[j]
                profile = []
                for group in groups:
                    values = [base[a] + first[a] + (0 if second is None else second[a]) for a in group]
                    lower, upper = -28 - min(values), 28 - max(values)
                    allowed = [q for q in range(-8, 9) if lower <= 2*q <= upper]
                    if not allowed:
                        raise ValueError("unexpected empty interval")
                    profile.append((allowed[0], allowed[-1]))
                profile = tuple(sorted(profile))
                verify_case(profile, kind)
                counts[kind][profile] += 1
    return counts


def decode_expected(record, kind):
    result = collections.Counter()
    for item in record["profiles"]:
        count = item[kind]
        if count:
            profile = tuple(tuple(pair) for pair in item["q_intervals"])
            verify_case(profile, kind)
            result[profile] += count
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--core-census", required=True, type=Path)
    parser.add_argument("--profiles", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    source = seeds(args.seeds)
    cores = json.loads(args.core_census.read_text(encoding="utf-8"))["reports"]
    expected = json.loads(args.profiles.read_text(encoding="utf-8"))["seeds"]
    if len(source) != 3 or len(cores) != 3 or len(expected) != 3:
        raise ValueError("input count mismatch")
    reports = []
    for index, (bits, core, claimed) in enumerate(zip(source, cores, expected), 1):
        observed = recount(bits, core["core_origin"], core["basis"])
        for kind in ("single", "pair"):
            if observed[kind] != decode_expected(claimed, kind):
                raise ValueError(f"profile catalogue mismatch for {kind}")
        reports.append({"seed_index_1based": index, "single": sum(observed["single"].values()),
                        "pair": sum(observed["pair"].values()),
                        "distinct_single_profiles": len(observed["single"]),
                        "distinct_pair_profiles": len(observed["pair"]),
                        "all_profiles_rejected_by_written_inequalities": True})
        print(f"seed={index} singles={reports[-1]['single']} pairs={reports[-1]['pair']} "
              f"profiles={len(observed['single'])}+{len(observed['pair'])} certificate=PASS", flush=True)
    output = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
              "core_sha256": hashlib.sha256(args.core_census.read_bytes()).hexdigest(),
              "profiles_sha256": hashlib.sha256(args.profiles.read_bytes()).hexdigest(),
              "method": "independent direct outside sums and full interval-profile recount", "reports": reports}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(output, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

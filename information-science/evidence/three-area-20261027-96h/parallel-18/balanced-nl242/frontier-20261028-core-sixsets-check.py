#!/usr/bin/env python3
"""Independently count the local six-sets via pair differences and character sums."""

import argparse
import itertools
import json
from pathlib import Path


def distinct_differences(points):
    if len(points) != 6 or len(set(points)) != 6 or any(type(x) is not int or not 0 <= x < 16 for x in points):
        raise ValueError("expected six distinct 4-bit points")
    return {x ^ y for x, y in itertools.combinations(points, 2)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    tested = valid = 0
    local_tables = set()
    for subset in itertools.combinations(range(16), 6):
        tested += 1
        differences = distinct_differences(subset)
        is_sidon = len(differences) == 15
        char_sums = [sum(1 - 2 * ((a & x).bit_count() & 1) for a in subset) for x in range(16)]
        spectrum_property = all(abs(v) == 2 for v in char_sums[1:])
        if is_sidon != spectrum_property:
            raise RuntimeError("difference and character conditions disagree")
        if not is_sidon:
            continue
        valid += 1
        xor = 0
        for x in subset:
            xor ^= x
        if xor != 0:
            raise RuntimeError("valid six-set has nonzero XOR")
        signs = [2 - char_sums[0] // 2] + [-value // 2 for value in char_sums[1:]]
        if signs[0] != -1 or any(s not in (-1, 1) for s in signs):
            raise RuntimeError("inverse is not a Boolean sign vector")
        transformed = [sum(signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(16))
                       for a in range(16)]
        if transformed != [(-6 if a in subset else 2) for a in range(16)]:
            raise RuntimeError("forward transform mismatch")
        local_tables.add(tuple(signs))
    try:
        distinct_differences([0, 0, 1, 2, 3, 4])
    except ValueError as error:
        if str(error) != "expected six distinct 4-bit points":
            raise RuntimeError("duplicate mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("duplicate mutation not rejected")
    if len(local_tables) != valid:
        raise RuntimeError("distinct six-sets did not give distinct Boolean local tables")
    receipt = {"six_subsets_checked": tested, "pair_difference_sidon_count": valid,
               "character_condition_count": valid, "distinct_boolean_tables": len(local_tables),
               "duplicate_point_control": "rejected for expected reason",
               "method": "all six-subsets, independent pair-difference and direct character/inverse checks"}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(receipt, out, indent=2)
        out.write("\n")
    print(f"sixsets={tested} valid={valid} distinct_boolean_tables={len(local_tables)} control=REJECTED")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

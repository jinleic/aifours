#!/usr/bin/env python3
"""Rebuild the claimed weighted-law integer numerator and denominator independently."""

import argparse
import ast
import collections
import hashlib
import json
import re
from pathlib import Path

EXPECTED = "d223232b8978a18bba5542fcdcdd133cbbc7f321ac057f8278850674b37d2f96"


def hash_int(value):
    return hashlib.sha256(value.to_bytes((value.bit_length() + 7) // 8, "big")).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--weighted", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    raw = args.weighted.read_bytes()
    if hashlib.sha256(raw).hexdigest() != EXPECTED:
        raise ValueError("weighted candidate hash mismatch")
    match = re.search(r"\bweights\s*=\s*\[(.*?)\]", raw.decode("utf-8"), re.S)
    if not match:
        raise ValueError("missing weights")
    weights = ast.literal_eval("[" + match.group(1) + "]")
    if len(weights) != 88 or any(type(w) is not int or w <= 0 for w in weights) or sum(weights) != 6000:
        raise ValueError("invalid weights")
    numerator = pow(3523, 649 * 3523) * pow(2477, 649 * 2477)
    denominator = pow(6000, 549 * 6000)
    for weight, count in sorted(collections.Counter(weights).items()):
        denominator *= pow(weight, 100 * weight * count)
    result = {"candidate_sha256": EXPECTED, "numerator_bits": numerator.bit_length(),
              "denominator_bits": denominator.bit_length(),
              "numerator_big_endian_sha256": hash_int(numerator),
              "denominator_big_endian_sha256": hash_int(denominator),
              "numerator_ge_2_4448_times_denominator": numerator >= (denominator << 4448),
              "method": "exact independently constructed Python integers; multiplicities grouped"}
    if not result["numerator_ge_2_4448_times_denominator"]:
        raise ValueError("claimed exact power margin is false")
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print(f"L_bits={result['numerator_bits']} R_bits={result['denominator_bits']} margin=PASS")
    print(f"L_sha256={result['numerator_big_endian_sha256']} R_sha256={result['denominator_big_endian_sha256']}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

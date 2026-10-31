#!/usr/bin/env python3
"""Independently check every generated local core truth table by direct parity masks."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512
EXPECTED = {4: 30, 12: 46, 20: 226, 28: 210}


def spectrum(truth, phases):
    return [N - 2 * (truth ^ phase).bit_count() for phase in phases]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family", required=True, type=Path)
    parser.add_argument("--generator-receipt", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    lines = args.family.read_text(encoding="ascii").splitlines()
    prior = json.loads(args.generator_receipt.read_text(encoding="utf-8"))
    if len(lines) != prior["count"] or hashlib.sha256(args.family.read_bytes()).hexdigest() != prior["output_sha256"]:
        raise ValueError("family count/hash mismatch")
    phases = [sum(1 << x for x in range(N) if (a & x).bit_count() & 1) for a in range(N)]
    weights = collections.Counter()
    seen = set()
    first = None
    for line in lines:
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid family truth table")
        value = int(line, 16)
        truth = sum(((value >> (N - 1 - x)) & 1) << x for x in range(N))
        if truth in seen:
            raise ValueError("duplicate family truth table")
        seen.add(truth)
        w = spectrum(truth, phases)
        if collections.Counter(map(abs, w)) != EXPECTED or 0 in w:
            raise ValueError("family spectrum differs from expected zero-free NL242 profile")
        weights[truth.bit_count()] += 1
        if first is None:
            first = truth
    if first is None or max(map(abs, spectrum(first ^ 1, phases))) != 30:
        raise RuntimeError("single-bit negative control did not produce peak 30")
    receipt = {"family_sha256": hashlib.sha256(args.family.read_bytes()).hexdigest(),
               "generator_receipt_sha256": hashlib.sha256(args.generator_receipt.read_bytes()).hexdigest(),
               "truth_tables": len(lines), "distinct_truth_tables": len(seen),
               "all_512_walsh_coefficients_per_table_checked": True,
               "all_zero_free_peak28": True, "truth_weight_histogram": dict(sorted(weights.items())),
               "single_bit_mutation_peak": 30,
               "method": "independent 512-bit parity-mask character sums; no FWHT"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"tables={len(lines)} all_zero_free_peak28=YES weights={dict(sorted(weights.items()))} mutation_peak=30")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

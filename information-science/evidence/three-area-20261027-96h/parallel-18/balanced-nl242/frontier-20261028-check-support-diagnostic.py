#!/usr/bin/env python3
"""Independently compare Walsh-support diagnostics with the direct-sum receipt."""

import argparse
import hashlib
import json
from pathlib import Path


def compare(observed, expected):
    for key in ("peak", "support_xor", "layer16_xor", "layer16_count", "zero_count"):
        if observed[key] != expected[key]:
            raise ValueError(f"support diagnostic mismatch: {key}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--search-result", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    expected = json.loads(args.search_result.read_text(encoding="utf-8"))
    if hashlib.sha256(args.candidate.read_bytes()).hexdigest() != audit["input_sha256"]:
        raise ValueError("candidate hash differs from Walsh audit")
    report = audit["reports"][0]
    values = report["walsh_values"]
    if len(values) != 512 or not report["balanced"] or values[0] != 0:
        raise ValueError("candidate is not an audited balanced table")
    support = layer = zeros = 0
    count16 = 0
    for index, value in enumerate(values):
        if value:
            support ^= index
        else:
            zeros += 1
        if abs(value) == 16:
            layer ^= index
            count16 += 1
    observed = {"peak": max(map(abs, values)), "support_xor": support, "layer16_xor": layer,
                "layer16_count": count16, "zero_count": zeros}
    compare(observed, expected)
    mutated = dict(expected)
    mutated["support_xor"] ^= 1
    try:
        compare(observed, mutated)
    except ValueError as error:
        if str(error) != "support diagnostic mismatch: support_xor":
            raise RuntimeError("mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("mutated support XOR passed")
    result = {"candidate_sha256": hashlib.sha256(args.candidate.read_bytes()).hexdigest(),
              "walsh_audit_sha256": hashlib.sha256(args.audit.read_bytes()).hexdigest(),
              "search_result_sha256": hashlib.sha256(args.search_result.read_bytes()).hexdigest(),
              "observed": observed, "mutated_support_xor_control": "rejected for expected reason"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print(f"peak={observed['peak']} support_xor={support} layer16_xor={layer} "
          f"layer16_count={count16} zeros={zeros} mutation=REJECTED")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

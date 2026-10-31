#!/usr/bin/env python3
"""Check candidate truth tables against the published seed, flips and twist."""

import argparse
import hashlib
import json
from pathlib import Path

N = 512


def parse_seeds(path):
    seeds = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid published seed")
        seed = int(line, 16)
        seeds.append([(seed >> (N - 1 - x)) & 1 for x in range(N)])
    return seeds


def validate(payload, seeds):
    index = payload.get("seed_index_1based")
    flips = payload.get("flip_indices")
    twist = payload.get("affine_twist_frequency")
    bits = payload.get("bits")
    if not isinstance(index, int) or not 1 <= index <= len(seeds):
        raise ValueError("invalid seed index")
    if not isinstance(flips, list) or len(flips) != 2 or not all(type(x) is int for x in flips):
        raise ValueError("invalid flip pair")
    if not 0 <= flips[0] < flips[1] < N:
        raise ValueError("flip pair must be distinct and increasing")
    if type(twist) is not int or not 0 <= twist < N:
        raise ValueError("invalid affine twist")
    if not isinstance(bits, str) or len(bits) != N or set(bits) - {"0", "1"}:
        raise ValueError("invalid truth-table bits")
    expected = "".join(str(seeds[index - 1][x] ^ int(x in flips) ^ ((x & twist).bit_count() & 1))
                       for x in range(N))
    if bits != expected:
        raise ValueError("truth table differs from declared seed/flip/twist relation")
    return {"seed_index_1based": index, "flips": flips, "twist": twist}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--candidates", required=True, nargs="+", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    seeds = parse_seeds(args.seeds)
    reports = []
    for path in args.candidates:
        payload = json.loads(path.read_text(encoding="utf-8"))
        relation = validate(payload, seeds)
        mutated = dict(payload)
        mutated["bits"] = ("1" if payload["bits"][0] == "0" else "0") + payload["bits"][1:]
        try:
            validate(mutated, seeds)
        except ValueError as error:
            if str(error) != "truth table differs from declared seed/flip/twist relation":
                raise RuntimeError("mutation rejected for an unexpected reason") from error
        else:
            raise RuntimeError("single-bit mutation was not rejected")
        reports.append({"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                        "relation": relation, "single_bit_mutation": "rejected for expected reason"})
        print(f"{path}: seed={relation['seed_index_1based']} flips={relation['flips']} "
              f"twist={relation['twist']} relation=OK mutation=REJECTED")
    result = {"seed_file_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(), "reports": reports}
    with args.output.open("x", encoding="utf-8") as output:
        json.dump(result, output, indent=2)
        output.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

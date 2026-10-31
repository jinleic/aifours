#!/usr/bin/env python3
"""Write every certified four-flip neighbor of one published seed as search inputs."""

import argparse
import hashlib
import json
from pathlib import Path

N = 512


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--quads", required=True, type=Path)
    parser.add_argument("--seed-index", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    lines = [line.strip() for line in args.seeds.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    data = json.loads(args.quads.read_text(encoding="utf-8"))["seeds"]
    if len(lines) != len(data) or not 1 <= args.seed_index <= len(lines):
        raise ValueError("invalid seed count/index")
    if args.output.exists() or args.receipt.exists():
        raise FileExistsError("refusing to overwrite output or receipt")
    index = args.seed_index - 1
    line = lines[index]
    if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
        raise ValueError("invalid source hex")
    original = int(line, 16)
    quads = data[index]["preserving_quads"]
    if len(quads) != data[index]["peak_preserving_count"]:
        raise ValueError("preserving count mismatch")
    records = []
    for rank, quad in enumerate(quads, 1):
        if len(quad) != 4 or len(set(quad)) != 4 or any(not 0 <= x < N for x in quad):
            raise ValueError("invalid quadruple")
        value = original
        for x in quad:
            value ^= 1 << (N - 1 - x)
        encoded = f"{value:0128X}"
        records.append({"line_1based": rank, "flips": quad,
                        "hex_sha256": hashlib.sha256(encoded.encode("ascii")).hexdigest()})
    with args.output.open("x", encoding="ascii") as file:
        for record in records:
            value = original
            for x in record["flips"]:
                value ^= 1 << (N - 1 - x)
            file.write(f"{value:0128X}\n")
    receipt = {"source_seed_index_1based": args.seed_index,
               "seed_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "quad_result_sha256": hashlib.sha256(args.quads.read_bytes()).hexdigest(),
               "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
               "records": records}
    with args.receipt.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"seed={args.seed_index} expanded_neighbors={len(records)} output={args.output} receipt={args.receipt}")


if __name__ == "__main__":
    main()

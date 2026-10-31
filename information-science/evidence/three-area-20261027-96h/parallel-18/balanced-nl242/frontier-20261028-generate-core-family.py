#!/usr/bin/env python3
"""Generate all 448 exact local peak-28 restrictions for one published seed."""

import argparse
import hashlib
import itertools
import json
from pathlib import Path

N = 512


def walsh(bits):
    values = [1 - 2 * bit for bit in bits]
    d = 1
    while d < len(values):
        for start in range(0, len(values), 2*d):
            for j in range(d):
                left, right = values[start+j], values[start+d+j]
                values[start+j], values[start+d+j] = left+right, left-right
        d *= 2
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--core", required=True, type=Path)
    parser.add_argument("--seed-index", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists() or args.receipt.exists():
        raise FileExistsError("refusing to overwrite output or receipt")
    lines = [line.strip() for line in args.seeds.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    cores = json.loads(args.core.read_text(encoding="utf-8"))["reports"]
    if not 1 <= args.seed_index <= len(lines) or len(lines) != len(cores):
        raise ValueError("seed/core count mismatch")
    source = lines[args.seed_index - 1]
    if len(source) != 128 or any(c not in "0123456789abcdefABCDEF" for c in source):
        raise ValueError("invalid source seed")
    value = int(source, 16)
    bits = [(value >> (N - 1 - x)) & 1 for x in range(N)]
    core = cores[args.seed_index - 1]
    coords = []
    for u in range(16):
        x = core["core_origin"]
        for i, b in enumerate(core["basis"]):
            if (u >> i) & 1:
                x ^= b
        coords.append(x)
    if len(set(coords)) != 16:
        raise ValueError("dependent core basis")
    encoded = []
    records = []
    for subset in itertools.combinations(range(16), 6):
        if len({a ^ b for a, b in itertools.combinations(subset, 2)}) != 15:
            continue
        hats = [sum(1 - 2 * ((a & x).bit_count() & 1) for a in subset) for x in range(16)]
        signs = [2 - hats[0] // 2] + [-v // 2 for v in hats[1:]]
        if any(sign not in (-1, 1) for sign in signs):
            raise RuntimeError("non-Boolean local inverse")
        candidate = bits.copy()
        for u, x in enumerate(coords):
            candidate[x] = (1 - signs[u]) // 2
        spectrum = walsh(candidate)
        if max(map(abs, spectrum)) != 28 or 0 in spectrum:
            raise RuntimeError("local caller failed to yield zero-free peak 28")
        text = "".join(map(str, candidate))
        hex_table = f"{int(text, 2):0128X}"
        encoded.append(hex_table)
        records.append({"line_1based": len(records) + 1, "negative_local_frequencies": list(subset),
                        "truth_sha256": hashlib.sha256(text.encode("ascii")).hexdigest()})
    if len(encoded) != 448 or len(set(encoded)) != 448:
        raise RuntimeError("core family size or uniqueness mismatch")
    with args.output.open("x", encoding="ascii") as file:
        for line in encoded:
            file.write(line + "\n")
    receipt = {"source_seed_index": args.seed_index,
               "seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "core_sha256": hashlib.sha256(args.core.read_bytes()).hexdigest(),
               "output_sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
               "count": len(records), "records": records}
    with args.receipt.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"seed={args.seed_index} exact_core_family={len(encoded)} zero_free_peak28=PASS output={args.output}")
    print(f"receipt={args.receipt}")


if __name__ == "__main__":
    main()

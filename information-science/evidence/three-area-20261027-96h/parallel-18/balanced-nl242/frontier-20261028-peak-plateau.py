#!/usr/bin/env python3
"""Count every peak-preserving two-bit move from each published truth table."""

import argparse
import hashlib
import json
from pathlib import Path

N = 512
ALL = (1 << N) - 1


def read_seeds(path):
    tables = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid published seed")
        value = int(line, 16)
        tables.append([(value >> (N - 1 - x)) & 1 for x in range(N)])
    if not tables:
        raise ValueError("no seed tables")
    return tables


def analyze(bits):
    signs = [1 - 2 * bit for bit in bits]
    w = [sum(sign * (1 - 2 * ((a & x).bit_count() & 1))
             for x, sign in enumerate(signs)) for a in range(N)]
    if max(map(abs, w)) != 28 or any(v % 4 for v in w):
        raise ValueError("requires a 4-divisible spectrum with peak 28")
    p28 = sum(1 << a for a, v in enumerate(w) if v == 28)
    m28 = sum(1 << a for a, v in enumerate(w) if v == -28)
    near = [a for a, v in enumerate(w) if abs(v) <= 4]
    phase_positive = [sum(1 << a for a in range(N)
                          if bits[x] == ((a & x).bit_count() & 1))
                      for x in range(N)]
    weight = sum(bits)
    pairs = preserving = with_zero = 0
    by_weight = {}
    first = []
    for x in range(N):
        xp, xm = phase_positive[x], ALL ^ phase_positive[x]
        for y in range(x + 1, N):
            pairs += 1
            yp, ym = phase_positive[y], ALL ^ phase_positive[y]
            if (p28 & xm & ym) | (m28 & xp & yp):
                continue
            preserving += 1
            new_weight = weight + (1 - 2 * bits[x]) + (1 - 2 * bits[y])
            by_weight[str(new_weight)] = by_weight.get(str(new_weight), 0) + 1
            zero_indices = [a for a in near if w[a] - 2 * signs[x] * (1 - 2 * ((a & x).bit_count() & 1))
                            - 2 * signs[y] * (1 - 2 * ((a & y).bit_count() & 1)) == 0]
            if zero_indices:
                with_zero += 1
            if len(first) < 8:
                first.append({"flips": [x, y], "new_weight": new_weight, "zero_count": len(zero_indices)})
    return {"pairs": pairs, "peak_preserving": preserving, "peak_preserving_with_walsh_zero": with_zero,
            "by_truth_weight": by_weight, "first_moves": first}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    reports = []
    for i, bits in enumerate(read_seeds(args.seeds)):
        result = analyze(bits)
        reports.append({"seed_index_1based": i + 1, **result})
        print(f"seed={i + 1} pairs={result['pairs']} peak_preserving={result['peak_preserving']} "
              f"with_zero={result['peak_preserving_with_walsh_zero']} weights={result['by_truth_weight']}")
    output = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
              "method": "direct character sums and exhaustive peak-violation bitmasks", "reports": reports}
    with args.output.open("x", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2)
        handle.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

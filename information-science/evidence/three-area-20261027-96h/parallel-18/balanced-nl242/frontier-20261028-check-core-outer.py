#!/usr/bin/env python3
"""Independently recount the exact outer-flip/local-truth feasibility search."""

import argparse
import hashlib
import json
from pathlib import Path

N = 512
LOCAL = 16
PATTERNS = 1 << LOCAL
ALL = (1 << PATTERNS) - 1


def parse_seed(path, index):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not 1 <= index <= len(lines):
        raise ValueError("seed index out of range")
    line = lines[index - 1]
    if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
        raise ValueError("invalid seed")
    value = int(line, 16)
    return [(value >> (N - 1 - x)) & 1 for x in range(N)]


def coordinates(origin, basis):
    if len(basis) != 4 or any(type(x) is not int or not 0 < x < N for x in basis):
        raise ValueError("invalid basis")
    result = []
    for u in range(LOCAL):
        position = origin
        for i, vector in enumerate(basis):
            if u & (1 << i):
                position ^= vector
        result.append(position)
    if len(set(result)) != LOCAL:
        raise ValueError("basis is not independent")
    return result


def local_masks():
    phase = [sum(1 << x for x in range(LOCAL) if (a & x).bit_count() & 1) for a in range(LOCAL)]
    data = [[bytearray(PATTERNS // 8) for _ in range(17)] for _ in range(LOCAL)]
    for pattern in range(PATTERNS):
        byte = pattern >> 3
        bit = 1 << (pattern & 7)
        for alpha in range(LOCAL):
            value = LOCAL - 2 * (pattern ^ phase[alpha]).bit_count()
            data[alpha][(value + 16) // 2][byte] |= bit
    masks = [[int.from_bytes(raw, "little") for raw in row] for row in data]
    cumulative = []
    for row in masks:
        running = 0
        entries = []
        for item in row:
            running |= item
            entries.append(running)
        if running != ALL:
            raise RuntimeError("local masks fail to partition all patterns")
        cumulative.append(entries)
    return masks, cumulative


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--core-census", required=True, type=Path)
    parser.add_argument("--seed-index", required=True, type=int)
    parser.add_argument("--single-result", required=True, type=Path)
    parser.add_argument("--pair-result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    bits = parse_seed(args.seeds, args.seed_index)
    core = json.loads(args.core_census.read_text(encoding="utf-8"))["reports"][args.seed_index - 1]
    coords = coordinates(core["core_origin"], core["basis"])
    try:
        coordinates(core["core_origin"], [core["basis"][0], core["basis"][0], core["basis"][2], core["basis"][3]])
    except ValueError as error:
        if str(error) != "basis is not independent":
            raise RuntimeError("basis mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("basis mutation was not rejected")
    outside = [x for x in range(N) if x not in set(coords)]
    if len(outside) != 496:
        raise ValueError("invalid outside cardinality")
    groups = [[] for _ in range(LOCAL)]
    for a in range(N):
        group = sum(((a & b).bit_count() & 1) << i for i, b in enumerate(core["basis"]))
        groups[group].append(a)
    signs = [1 - 2 * b for b in bits]
    char = [[signs[x] * (1 - 2 * ((a & (x ^ core["core_origin"])).bit_count() & 1))
             for a in range(N)] for x in outside]
    baseline_r = [sum(row[a] for row in char) for a in range(N)]
    exact, cumulative = local_masks()
    cache = {}

    def solve(row_x=None, row_y=None):
        intervals = []
        zero_levels = []
        for alpha, group in enumerate(groups):
            values = [baseline_r[a] - (2 * row_x[a] if row_x is not None else 0)
                      - (2 * row_y[a] if row_y is not None else 0) for a in group]
            low, high = -28 - min(values), 28 - max(values)
            indices = [i for i in range(17) if low <= -16 + 2 * i <= high]
            if not indices:
                return 0, 0
            lo, hi = indices[0], indices[-1]
            key = (alpha, lo, hi)
            if key not in cache:
                cache[key] = cumulative[alpha][hi] ^ (cumulative[alpha][lo - 1] if lo else 0)
            intervals.append(cache[key])
            levels = {(-r + 16) // 2 for r in values if -16 <= r <= 16 and r % 2 == 0 and low <= -r <= high}
            zero_levels.append((alpha, levels))
        current = ALL
        for item in sorted(intervals, key=int.bit_count):
            current &= item
            if not current:
                return 0, 0
        zeros = 0
        for alpha, levels in zero_levels:
            for level in levels:
                zeros |= exact[alpha][level]
        return current.bit_count(), (current & zeros).bit_count()

    baseline = solve()
    if baseline != (448, 0):
        raise ValueError(f"baseline positive control disagrees: {baseline}")
    independent = {}
    for mode in ("single", "pair"):
        tested = valid_outer = valid_local = target_outer = target_local = 0
        for i, row in enumerate(char):
            js = (None,) if mode == "single" else range(i + 1, len(char))
            for j in js:
                tested += 1
                valid, target = solve(row, None if j is None else char[j])
                valid_outer += valid > 0
                valid_local += valid
                target_outer += target > 0
                target_local += target
        expected = json.loads((args.single_result if mode == "single" else args.pair_result).read_text(encoding="utf-8"))
        actual = {"tested": tested, "valid_outer_subsets": valid_outer, "valid_outer_local_pairs": valid_local,
                  "target_outer_subsets": target_outer, "target_outer_local_pairs": target_local}
        for key, value in actual.items():
            if expected[key] != value:
                raise ValueError(f"search mismatch for {mode}: {key}")
        if not expected["complete"]:
            raise ValueError("search receipt is not complete")
        independent[mode] = actual
        print(f"seed={args.seed_index} mode={mode} tested={tested} valid_outer={valid_outer} "
              f"target_outer={target_outer} agreement=YES", flush=True)
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "core_census_sha256": hashlib.sha256(args.core_census.read_bytes()).hexdigest(),
               "single_result_sha256": hashlib.sha256(args.single_result.read_bytes()).hexdigest(),
               "pair_result_sha256": hashlib.sha256(args.pair_result.read_bytes()).hexdigest(),
               "seed_index_1based": args.seed_index, "baseline_valid_local": baseline[0],
               "baseline_target_local": baseline[1], "basis_mutation": "rejected for expected reason",
               "method": "direct parity masks and full Python-integer local feasibility intersection",
               "independent": independent}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"baseline=448/0 mutation=REJECTED receipt={args.output}")


if __name__ == "__main__":
    main()

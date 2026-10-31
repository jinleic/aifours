#!/usr/bin/env python3
"""Independently replay bounded splitmix affine-flat draws and exact local masks."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

N = 512
MASK64 = (1 << 64) - 1


def splitmix(state):
    state = (state + 0x9E3779B97F4A7C15) & MASK64
    z = ((state ^ (state >> 30)) * 0xBF58476D1CE4E5B9) & MASK64
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK64
    return state, (z ^ (z >> 31)) & MASK64


def source_seed(path, index):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not 1 <= index <= len(lines) or len(lines[index - 1]) != 128:
        raise ValueError("invalid seed index or length")
    value = int(lines[index - 1], 16)
    return [(value >> (N - 1 - x)) & 1 for x in range(N)]


def local_mask_module(path):
    spec = importlib.util.spec_from_file_location("review_outer_masks", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.local_masks()


def compare(actual, expected):
    for key in ("flats_tested", "valid_flat_draws", "valid_flat_local_pairs", "target_flat_draws", "target_flat_local_pairs"):
        if actual[key] != expected[key]:
            raise ValueError(f"random flat summary mismatch: {key}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--search-result", required=True, type=Path)
    parser.add_argument("--mask-module", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-replay", type=int, default=10000)
    args = parser.parse_args()
    expected = json.loads(args.search_result.read_text(encoding="utf-8"))
    if expected["flats_tested"] > args.max_replay or expected["stopped_for_witness"]:
        raise ValueError("result exceeds replay bound or requires separate witness validation")
    bits = source_seed(args.seeds, expected["seed_index_1based"])
    signs = [1 - 2 * x for x in bits]
    global_w = [sum(signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(N)) for a in range(N)]
    exact, cumulative = local_mask_module(args.mask_module)
    all_patterns = (1 << 65536) - 1
    state = expected["rng_seed"]
    valid_draws = valid_pairs = target_draws = target_pairs = 0
    for _ in range(expected["flats_tested"]):
        state, raw = splitmix(state)
        origin = raw % N
        basis = []
        span = {0}
        while len(basis) < 4:
            state, raw = splitmix(state)
            b = raw % N
            if b in span:
                continue
            basis.append(b)
            span |= {x ^ b for x in span}
        coords = [origin] * 16
        for u in range(16):
            for i, b in enumerate(basis):
                if (u >> i) & 1:
                    coords[u] ^= b
        local_signs = [signs[x] for x in coords]
        local_w = [sum(local_signs[u] * (1 - 2 * ((alpha & u).bit_count() & 1))
                       for u in range(16)) for alpha in range(16)]
        groups = [[] for _ in range(16)]
        for a in range(N):
            alpha = sum(((a & b).bit_count() & 1) << i for i, b in enumerate(basis))
            orient = 1 - 2 * ((a & origin).bit_count() & 1)
            groups[alpha].append(orient * global_w[a] - local_w[alpha])
        constraints = []
        zero_candidates = []
        for alpha, values in enumerate(groups):
            low, high = -28 - min(values), 28 - max(values)
            levels = [i for i in range(17) if low <= -16 + 2*i <= high]
            if not levels:
                constraints = [0]
                break
            lo, hi = levels[0], levels[-1]
            constraints.append(cumulative[alpha][hi] ^ (cumulative[alpha][lo-1] if lo else 0))
            zero_candidates.append((alpha, {(-r + 16)//2 for r in values
                                            if -16 <= r <= 16 and r % 2 == 0 and low <= -r <= high}))
        valid = all_patterns
        for mask in sorted(constraints, key=int.bit_count):
            valid &= mask
            if not valid:
                break
        zero_mask = 0
        for alpha, levels in zero_candidates:
            for level in levels:
                zero_mask |= exact[alpha][level]
        targets = valid & zero_mask
        valid_draws += valid != 0
        valid_pairs += valid.bit_count()
        target_draws += targets != 0
        target_pairs += targets.bit_count()
    actual = {"flats_tested": expected["flats_tested"], "valid_flat_draws": valid_draws,
              "valid_flat_local_pairs": valid_pairs, "target_flat_draws": target_draws,
              "target_flat_local_pairs": target_pairs}
    compare(actual, expected)
    altered = dict(expected)
    altered["valid_flat_local_pairs"] += 1
    try:
        compare(actual, altered)
    except ValueError as error:
        if str(error) != "random flat summary mismatch: valid_flat_local_pairs":
            raise RuntimeError("mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("mutated summary passed")
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "search_result_sha256": hashlib.sha256(args.search_result.read_bytes()).hexdigest(),
               "mask_module_sha256": hashlib.sha256(args.mask_module.read_bytes()).hexdigest(),
               "method": "independent splitmix replay, direct source Walsh and Python local-pattern masks",
               "actual": actual, "mutated_summary_control": "rejected for expected reason"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"flats={actual['flats_tested']} valid_local_pairs={valid_pairs} target_flats={target_draws} "
          f"mutation=REJECTED receipt={args.output}")


if __name__ == "__main__":
    main()

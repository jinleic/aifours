#!/usr/bin/env python3
"""Verify RREF affine-flat enumeration and replay a bounded 9-variable prefix."""

import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path


def flats(n, k):
    for pivots in itertools.combinations(range(n), k):
        nonpivots = [j for j in range(n) if j not in pivots]
        slots = [(i, col) for col in nonpivots for i in range(k) if col > pivots[i]]
        for assignment in range(1 << len(slots)):
            rows = [1 << pivot for pivot in pivots]
            for b, (i, col) in enumerate(slots):
                if (assignment >> b) & 1:
                    rows[i] |= 1 << col
            for rep in range(1 << len(nonpivots)):
                origin = sum(1 << col for i, col in enumerate(nonpivots) if (rep >> i) & 1)
                yield tuple(rows), origin


def space(rows):
    span = {0}
    for row in rows:
        span |= {x ^ row for x in span}
    return frozenset(span)


def small_control():
    candidate = set()
    duplicate = 0
    for rows, origin in flats(5, 2):
        subspace = space(rows)
        if len(subspace) != 4:
            raise RuntimeError("dependent RREF rows")
        flat = frozenset(origin ^ x for x in subspace)
        duplicate += flat in candidate
        candidate.add(flat)
    brute_spaces = {space((a, b)) for a, b in itertools.combinations(range(1, 32), 2)}
    brute = {frozenset(origin ^ x for x in subspace) for subspace in brute_spaces for origin in range(32)}
    if candidate != brute or duplicate:
        raise RuntimeError("small RREF enumeration differs from independent brute set")
    return {"n": 5, "dimension": 2, "subspaces": len(brute_spaces), "affine_flats": len(brute),
            "duplicates": duplicate}


def source_seed(path, index):
    lines = [line.strip() for line in path.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not 1 <= index <= len(lines) or len(lines[index-1]) != 128:
        raise ValueError("invalid seed")
    value = int(lines[index-1], 16)
    return [(value >> (511 - x)) & 1 for x in range(512)]


def load_masks(path):
    spec = importlib.util.spec_from_file_location("local_masks_independent", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.local_masks()


def replay(bits, basis, exact, cumulative):
    signs = [1 - 2*bit for bit in bits]
    global_w = [sum(signs[x] * (1 - 2*((a & x).bit_count() & 1)) for x in range(512)) for a in range(512)]
    total_valid = total_target = 0
    all_patterns = (1 << 65536) - 1
    for rows, start in basis:
        coords = [start] * 16
        for u in range(16):
            for i, vector in enumerate(rows):
                if (u >> i) & 1:
                    coords[u] ^= vector
        local_signs = [signs[x] for x in coords]
        local_w = [sum(local_signs[u] * (1 - 2*((alpha & u).bit_count() & 1)) for u in range(16))
                   for alpha in range(16)]
        groups = [[] for _ in range(16)]
        for a in range(512):
            alpha = sum(((a & vector).bit_count() & 1) << i for i, vector in enumerate(rows))
            orientation = 1 - 2*((a & start).bit_count() & 1)
            groups[alpha].append(orientation * global_w[a] - local_w[alpha])
        valid = all_patterns
        zero_masks = []
        for alpha, group in enumerate(groups):
            low, high = -28 - min(group), 28 - max(group)
            levels = [i for i in range(17) if low <= -16+2*i <= high]
            if not levels:
                valid = 0
                break
            lo, hi = levels[0], levels[-1]
            valid &= cumulative[alpha][hi] ^ (cumulative[alpha][lo-1] if lo else 0)
            zero_masks.append((alpha, {(-r+16)//2 for r in group
                                       if -16 <= r <= 16 and r % 2 == 0 and low <= -r <= high}))
            if not valid:
                break
        zeros = 0
        for alpha, levels in zero_masks:
            for level in levels:
                zeros |= exact[alpha][level]
        total_valid += valid.bit_count()
        total_target += (valid & zeros).bit_count()
    return total_valid, total_target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--search-result", required=True, type=Path)
    parser.add_argument("--mask-module", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-replay", type=int, default=10000)
    args = parser.parse_args()
    control = small_control()
    claimed = json.loads(args.search_result.read_text(encoding="utf-8"))
    if claimed["start_index"] != 0 or claimed["tested"] > args.max_replay or claimed["stopped_for_witness"]:
        raise ValueError("unsupported prefix or witness")
    total_spaces = sum(1 << sum(col > p for col in range(9) if col not in pivots for p in pivots)
                       for pivots in itertools.combinations(range(9), 4))
    total_flats = total_spaces * 32
    if total_flats != claimed["total_flats"]:
        raise ValueError("9-variable RREF count mismatch")
    prefix = list(itertools.islice(flats(9, 4), claimed["tested"]))
    if len(prefix) != claimed["tested"]:
        raise ValueError("prefix shorter than claimed")
    exact, cumulative = load_masks(args.mask_module)
    valid, target = replay(source_seed(args.seeds, claimed["seed_index_1based"]), prefix, exact, cumulative)
    if (valid != claimed["valid_flat_local_pairs"] or target != claimed["target_flat_local_pairs"]
            or claimed["valid_flat_draws"] != claimed["tested"]):
        raise ValueError("independent prefix replay mismatch")
    receipt = {"small_exact_control": control, "subspaces_9_4": total_spaces, "affine_flats_9_4": total_flats,
               "prefix_tested": len(prefix), "valid_local_pairs": valid, "target_local_pairs": target,
               "search_result_sha256": hashlib.sha256(args.search_result.read_bytes()).hexdigest(),
               "seed_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "mask_module_sha256": hashlib.sha256(args.mask_module.read_bytes()).hexdigest(),
               "method": "brute F2^5 flat-set comparison and independent direct-Walsh 9-variable prefix replay"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"small_subspaces={control['subspaces']} small_flats={control['affine_flats']} duplicates={control['duplicates']}")
    print(f"9var_subspaces={total_spaces} flats={total_flats} prefix={len(prefix)} valid={valid} target={target}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

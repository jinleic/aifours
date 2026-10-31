#!/usr/bin/env python3
"""Independent exhaustive census of normalized 3-bit complete mappings."""

import argparse
import collections
import itertools
import json
from pathlib import Path


def gf2_rank(vectors):
    pivots = {}
    for value in vectors:
        while value:
            bit = value.bit_length() - 1
            if bit in pivots:
                value ^= pivots[bit]
            else:
                pivots[bit] = value
                break
    return len(pivots)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    profiles = collections.Counter()
    complete = collections.Counter()
    beta_structure = collections.Counter()
    checked = 0
    for tail in itertools.permutations(range(1, 8)):
        f = (0,) + tail
        checked += 1
        linear = all(f[x ^ y] == (f[x] ^ f[y]) for x in range(8) for y in range(8))
        derivative_sizes = tuple(sorted(len({f[x] ^ f[x ^ h] for x in range(8)}) for h in range(1, 8)))
        profiles[derivative_sizes] += 1
        beta_columns = [f[1 ^ 2] ^ f[1] ^ f[2], f[1 ^ 4] ^ f[1] ^ f[4],
                        f[2 ^ 4] ^ f[2] ^ f[4]]
        rank = gf2_rank(beta_columns)
        structure_count = sum(len({f[x] ^ f[x ^ h] for x in range(8)}) == 1 for h in range(1, 8))
        beta_structure[(rank, structure_count)] += 1
        if len({f[x] ^ x for x in range(8)}) == 8:
            complete["linear" if linear else "nonlinear"] += 1
    result = {"normalized_permutations": checked,
              "derivative_profiles": [{"sizes": list(k), "count": v} for k, v in sorted(profiles.items())],
              "beta_rank_and_nonzero_structures": [{"rank": k[0], "structure_count": k[1], "count": v}
                                                    for k, v in sorted(beta_structure.items())],
              "complete_mapping_counts": dict(complete),
              "method": "itertools permutations, direct derivative sets and direct K+identity test"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
        file.write("\n")
    print(f"permutations={checked} complete_linear={complete['linear']} complete_nonlinear={complete['nonlinear']}")
    print("profiles=" + "; ".join(f"{k}:{v}" for k, v in sorted(profiles.items())))
    print(f"beta_structure={dict(beta_structure)} receipt={args.output}")


if __name__ == "__main__":
    main()

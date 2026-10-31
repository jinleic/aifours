#!/usr/bin/env python3
"""Independently verify every triple and peak-preserving four-flip candidate."""

import argparse
import hashlib
import json
from pathlib import Path

N = 512


def load_seeds(path):
    tables = []
    for line in path.read_text(encoding="ascii").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if len(line) != 128 or any(c not in "0123456789abcdefABCDEF" for c in line):
            raise ValueError("invalid seed")
        value = int(line, 16)
        tables.append([(value >> (N - 1 - x)) & 1 for x in range(N)])
    if not tables:
        raise ValueError("no seeds")
    return tables


def require_equal_edges(observed, reported):
    if observed != reported:
        raise ValueError("uncovered triple set mismatch")


def check(bits, claimed):
    signs = [1 - 2 * bit for bit in bits]
    spectrum = [sum(signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) for x in range(N))
                for a in range(N)]
    if max(map(abs, spectrum)) != 28 or any(v == 0 or v % 4 for v in spectrum):
        raise ValueError("seed must be zero-free, 4-divisible and peak-28")
    if any(abs(v) > 20 for v in spectrum if abs(v) != 28):
        raise ValueError("seed nonpeak exceeds 20")
    peak_indices = [a for a, v in enumerate(spectrum) if abs(v) == 28]
    bad = []
    for x in range(N):
        mask = 0
        for j, a in enumerate(peak_indices):
            if spectrum[a] * signs[x] * (1 - 2 * ((a & x).bit_count() & 1)) < 0:
                mask |= 1 << j
        bad.append(mask)
    uncovered = set()
    triples = 0
    for x in range(N - 2):
        for y in range(x + 1, N - 1):
            common = bad[x] & bad[y]
            for z in range(y + 1, N):
                triples += 1
                if not common & bad[z]:
                    uncovered.add((x, y, z))
    reported = {tuple(item) for item in claimed["uncovered_triples"]}
    if len(reported) != len(claimed["uncovered_triples"]):
        raise ValueError("duplicate reported triple")
    require_equal_edges(uncovered, reported)
    if uncovered:
        mutation = set(reported)
        mutation.remove(next(iter(mutation)))
        try:
            require_equal_edges(uncovered, mutation)
        except ValueError as error:
            if str(error) != "uncovered triple set mismatch":
                raise RuntimeError("wrong mutation error") from error
        else:
            raise RuntimeError("deleted-triple control not detected")
    preserving = set()
    zero_count = 0
    for x, y, z in uncovered:
        for v in range(z + 1, N):
            if (x, y, v) not in uncovered or (x, z, v) not in uncovered or (y, z, v) not in uncovered:
                continue
            quad = (x, y, z, v)
            new_spectrum = [spectrum[a] - 2 * sum(signs[p] * (1 - 2 * ((a & p).bit_count() & 1))
                                                   for p in quad) for a in range(N)]
            if max(map(abs, new_spectrum)) > 28:
                raise RuntimeError("four-clique failed the all-frequency peak bound")
            preserving.add(quad)
            if 0 in new_spectrum:
                zero_count += 1
    reported_quads = {tuple(item) for item in claimed["preserving_quads"]}
    if len(reported_quads) != len(claimed["preserving_quads"]) or preserving != reported_quads:
        raise ValueError("preserving quadruple set mismatch")
    if (triples != claimed["triples"] or len(uncovered) != claimed["uncovered_count"]
            or len(preserving) != claimed["peak_preserving_count"] or zero_count != claimed["balanceable_count"]):
        raise ValueError("summary count mismatch")
    return {"triples": triples, "uncovered_count": len(uncovered), "peak_preserving_count": len(preserving),
            "balanceable_count": zero_count, "deleted_triple_control": "rejected for expected reason"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--search-result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    seeds = load_seeds(args.seeds)
    reports = json.loads(args.search_result.read_text(encoding="utf-8"))["seeds"]
    if len(seeds) != len(reports):
        raise ValueError("seed count mismatch")
    results = []
    for index, (bits, claimed) in enumerate(zip(seeds, reports), 1):
        result = check(bits, claimed)
        results.append({"seed_index_1based": index, **result})
        print(f"seed={index} triples={result['triples']} uncovered={result['uncovered_count']} "
              f"peak_preserving={result['peak_preserving_count']} balanceable={result['balanceable_count']} "
              f"deletion_control=REJECTED", flush=True)
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "search_result_sha256": hashlib.sha256(args.search_result.read_bytes()).hexdigest(),
               "method": "direct Walsh sums, integer triple-set equality and independently checked four-cliques",
               "reports": results}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

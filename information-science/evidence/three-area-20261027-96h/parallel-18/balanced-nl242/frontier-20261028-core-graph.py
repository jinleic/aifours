#!/usr/bin/env python3
"""Classify the entire peak-preserving graph inside the expanded local move code."""

import argparse
import collections
import hashlib
import json
from pathlib import Path

N = 512


def closure(vectors, cap):
    result = {0}
    for v in vectors:
        result |= {x ^ v for x in result}
        if len(result) > cap:
            raise ValueError("move span exceeds bound")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", required=True, type=Path)
    parser.add_argument("--second-layer", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-states", type=int, default=4096)
    args = parser.parse_args()
    lines = [line.strip() for line in args.seeds.read_text(encoding="ascii").splitlines()
             if line.strip() and not line.lstrip().startswith("#")]
    if not lines or len(lines[0]) != 128 or any(c not in "0123456789abcdefABCDEF" for c in lines[0]):
        raise ValueError("invalid seed")
    source = int(lines[0], 16)
    seed = sum(((source >> (N - 1 - x)) & 1) << x for x in range(N))
    rows = json.loads(args.second_layer.read_text(encoding="utf-8"))["seeds"]
    quads = set()
    for row in rows:
        if len(row["preserving_quads"]) != row["peak_preserving_count"]:
            raise ValueError("bad node count")
        for q in row["preserving_quads"]:
            if len(q) != 4 or len(set(q)) != 4 or any(type(x) is not int or not 0 <= x < N for x in q):
                raise ValueError("invalid quad")
            quads.add(tuple(sorted(q)))
    if not quads:
        raise ValueError("no move generators")
    moves = [sum(1 << x for x in q) for q in sorted(quads)]
    span = closure(moves, args.max_states)
    phases = [sum(1 << x for x in range(N) if (a & x).bit_count() & 1) for a in range(N)]
    admissible = set()
    targets = 0
    for delta in span:
        truth = seed ^ delta
        spectrum = [N - 2 * (truth ^ mask).bit_count() for mask in phases]
        if max(map(abs, spectrum)) <= 28:
            admissible.add(delta)
            if 0 in spectrum:
                targets += 1
    degree_hist = collections.Counter()
    edge_twice = 0
    for x in admissible:
        degree = sum((x ^ move) in admissible for move in moves)
        degree_hist[degree] += 1
        edge_twice += degree
    if edge_twice % 2:
        raise RuntimeError("undirected degree sum is odd")
    unseen = set(admissible)
    components = []
    seed_component = None
    while unseen:
        start = next(iter(unseen))
        unseen.remove(start)
        stack = [start]
        size = 0
        contains_seed = False
        while stack:
            vertex = stack.pop()
            size += 1
            contains_seed |= vertex == 0
            for move in moves:
                neighbor = vertex ^ move
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
        components.append(size)
        if contains_seed:
            seed_component = size
    result = {"move_count": len(moves), "span_size": len(span), "admissible_vertices": len(admissible),
              "target_vertices": targets, "edges": edge_twice // 2,
              "degree_histogram": dict(sorted(degree_hist.items())),
              "component_sizes": sorted(components, reverse=True), "seed_component_size": seed_component,
              "scope": "induced graph inside this finite move span; no assertion about outside moves"}
    receipt = {"seeds_sha256": hashlib.sha256(args.seeds.read_bytes()).hexdigest(),
               "second_layer_sha256": hashlib.sha256(args.second_layer.read_bytes()).hexdigest(),
               "method": "exact span closure, full parity-mask Walsh transform and graph traversal", "result": result}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"span={result['span_size']} valid={result['admissible_vertices']} target={targets} "
          f"edges={result['edges']} degrees={result['degree_histogram']} "
          f"components={result['component_sizes']} seed_component={seed_component}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Reconstruct the local 448-state graph from six-set Fourier inverses."""

import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path


def character(a, x):
    return 1 - 2 * ((a & x).bit_count() & 1)


def compare(actual, prior):
    pairs = (("vertices", "admissible_vertices"), ("edges", "edges"),
             ("degree_histogram", "degree_histogram"), ("component_sizes", "component_sizes"))
    for left, right in pairs:
        if actual[left] != prior[right]:
            raise ValueError(f"graph summary mismatch: {left}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core-structure", required=True, type=Path)
    parser.add_argument("--graph-result", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    states = set()
    valid_sixsets = 0
    for subset in itertools.combinations(range(16), 6):
        differences = {a ^ b for a, b in itertools.combinations(subset, 2)}
        if len(differences) != 15:
            continue
        valid_sixsets += 1
        hats = [sum(character(a, x) for a in subset) for x in range(16)]
        signs = [2 - hats[0] // 2] + [-value // 2 for value in hats[1:]]
        if any(value not in (-1, 1) for value in signs) or signs[0] != -1:
            raise RuntimeError("invalid six-set inverse")
        state = sum(((1 - value) // 2) << x for x, value in enumerate(signs))
        states.add(state)
    planes = {sum(1 << x for x in quad) for quad in itertools.combinations(range(1, 16), 4)
              if quad[0] ^ quad[1] ^ quad[2] ^ quad[3] == 0}
    degree_hist = collections.Counter()
    degrees = 0
    for state in states:
        degree = sum((state ^ move) in states for move in planes)
        degree_hist[degree] += 1
        degrees += degree
    if degrees % 2:
        raise RuntimeError("odd graph degree sum")
    unseen = set(states)
    components = []
    while unseen:
        current = unseen.pop()
        todo = [current]
        size = 0
        while todo:
            x = todo.pop()
            size += 1
            for move in planes:
                y = x ^ move
                if y in unseen:
                    unseen.remove(y)
                    todo.append(y)
        components.append(size)
    source = json.loads(args.core_structure.read_text(encoding="utf-8"))["reports"]
    for item in source:
        text = item["local_truth_bits"]
        if len(text) != 16 or set(text) - {"0", "1"}:
            raise ValueError("invalid local source bits")
        value = sum(int(text[x]) << x for x in range(16))
        if value not in states:
            raise ValueError("source local truth not in six-set state space")
    actual = {"sixsets": valid_sixsets, "vertices": len(states), "plane_moves": len(planes),
              "edges": degrees // 2, "degree_histogram": {str(k): v for k, v in sorted(degree_hist.items())},
              "component_sizes": sorted(components, reverse=True), "source_local_restrictions_matched": len(source)}
    prior = json.loads(args.graph_result.read_text(encoding="utf-8"))["result"]
    compare(actual, prior)
    altered = dict(prior)
    altered["edges"] += 1
    try:
        compare(actual, altered)
    except ValueError as error:
        if str(error) != "graph summary mismatch: edges":
            raise RuntimeError("edge mutation rejected for wrong reason") from error
    else:
        raise RuntimeError("edge mutation not rejected")
    receipt = {"core_structure_sha256": hashlib.sha256(args.core_structure.read_bytes()).hexdigest(),
               "graph_result_sha256": hashlib.sha256(args.graph_result.read_bytes()).hexdigest(),
               "method": "independent six-set Fourier inversion and all local plane-move graph edges",
               "actual": actual, "edge_mutation": "rejected for expected reason"}
    with args.output.open("x", encoding="utf-8") as file:
        json.dump(receipt, file, indent=2)
        file.write("\n")
    print(f"sixsets={valid_sixsets} vertices={len(states)} planes={len(planes)} edges={actual['edges']} "
          f"degrees={actual['degree_histogram']} components={actual['component_sizes']} mutation=REJECTED")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

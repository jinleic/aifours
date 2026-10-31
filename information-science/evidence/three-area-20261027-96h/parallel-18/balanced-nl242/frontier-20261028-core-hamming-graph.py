#!/usr/bin/env python3
"""Check all Hamming-four edges among the independently reconstructed local states."""

import argparse
import collections
import hashlib
import itertools
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prior-graph", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    states = []
    for subset in itertools.combinations(range(16), 6):
        if len({a ^ b for a, b in itertools.combinations(subset, 2)}) != 15:
            continue
        hats = [sum(1 - 2 * ((a & x).bit_count() & 1) for a in subset) for x in range(16)]
        signs = [2 - hats[0] // 2] + [-value // 2 for value in hats[1:]]
        if any(s not in (-1, 1) for s in signs):
            raise RuntimeError("six-set inverse is not Boolean")
        states.append(sum(((1 - s) // 2) << x for x, s in enumerate(signs)))
    if len(states) != len(set(states)):
        raise RuntimeError("duplicate local state")
    neighbors = [set() for _ in states]
    nonplane = []
    for i, j in itertools.combinations(range(len(states)), 2):
        difference = states[i] ^ states[j]
        if difference.bit_count() != 4:
            continue
        points = [x for x in range(16) if (difference >> x) & 1]
        xor = 0
        for point in points:
            xor ^= point
        if xor != 0:
            nonplane.append([i, j])
        neighbors[i].add(j)
        neighbors[j].add(i)
    degrees = collections.Counter(len(row) for row in neighbors)
    unseen = set(range(len(states)))
    components = []
    while unseen:
        root = unseen.pop()
        todo = [root]
        size = 0
        while todo:
            node = todo.pop()
            size += 1
            for other in neighbors[node]:
                if other in unseen:
                    unseen.remove(other)
                    todo.append(other)
        components.append(size)
    actual = {"vertices": len(states), "all_hamming4_edges": sum(map(len, neighbors)) // 2,
              "nonplane_edges": len(nonplane), "degree_histogram": dict(sorted(degrees.items())),
              "component_sizes": sorted(components, reverse=True)}
    prior = json.loads(args.prior_graph.read_text(encoding="utf-8"))["actual"]
    if (actual["vertices"] != prior["vertices"] or actual["all_hamming4_edges"] != prior["edges"]
            or {str(k): v for k, v in actual["degree_histogram"].items()} != prior["degree_histogram"]
            or actual["component_sizes"] != prior["component_sizes"] or nonplane):
        raise RuntimeError("all Hamming-four graph disagrees with prior plane-move graph")
    receipt = {"prior_graph_sha256": hashlib.sha256(args.prior_graph.read_bytes()).hexdigest(),
               "method": "all unordered pairs of independently reconstructed six-set inverse truth vectors",
               "actual": actual}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(receipt, out, indent=2)
        out.write("\n")
    print(f"vertices={actual['vertices']} all_hamming4_edges={actual['all_hamming4_edges']} "
          f"nonplane={actual['nonplane_edges']} degrees={actual['degree_histogram']} "
          f"components={actual['component_sizes']}")
    print(f"receipt={args.output}")


if __name__ == "__main__":
    main()

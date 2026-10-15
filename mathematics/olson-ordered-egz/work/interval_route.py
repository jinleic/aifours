#!/usr/bin/env python3
"""Find obstruction to a sufficient disjoint-identity-interval proof route.

A length-(2n-1) group word has 2n prefix products. Equal prefix products
bound an identity-product interval. This assay asks whether n colors alone
force disjoint such intervals whose total length is n. A coloring obstruction
refutes only this proof route, not Olson's conjecture.
"""
import argparse
import json
from pathlib import Path


def interval_lengths(colors):
    reachable = [{0}] + [set() for _ in colors[1:]]
    for end in range(1, len(colors)):
        reachable[end].update(reachable[end - 1])
        for start in range(end):
            if colors[start] == colors[end]:
                reachable[end].update(length + end - start for length in reachable[start])
    return sorted(reachable[-1])


def restricted_growth_words(length, alphabet):
    word = [0] * length
    def visit(index, largest):
        if index == length:
            yield tuple(word)
            return
        for value in range(min(largest + 1, alphabet - 1) + 1):
            word[index] = value
            yield from visit(index + 1, max(largest, value))
    yield from visit(1, 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-order', type=int, default=5)
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    records = []
    for n in range(2, arguments.max_order + 1):
        checked = 0
        obstruction = None
        for colors in restricted_growth_words(2 * n, n):
            checked += 1
            reachable = interval_lengths(colors)
            if n not in reachable:
                obstruction = {'prefix_colors': colors, 'attainable_total_interval_lengths': reachable}
                break
        records.append({'n': n, 'canonical_colorings_checked': checked, 'obstruction': obstruction})
        if obstruction:
            break
    result = {'scope': 'Disjoint-contiguous-identity-interval sufficient route only; NOT an Olson counterexample',
              'records': records}
    arguments.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

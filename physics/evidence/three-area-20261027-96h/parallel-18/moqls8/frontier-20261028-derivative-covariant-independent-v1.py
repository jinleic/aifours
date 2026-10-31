#!/usr/bin/env python3
"""Independent exact derivative-set classification of a restricted MOQLS family.

No C++ graph code or checker is imported. Exhaustion is only over the 5040
normalized permutations of the additive 3-bit group, not over all MOQLS(8).
"""
import argparse
import hashlib
import itertools
import json
import pathlib
import time


def derivative_masks(f):
    result = []
    for h in range(1, 8):
        mask = 0
        for x in range(8):
            mask |= 1 << (f[x] ^ f[x ^ h])
        result.append(mask)
    return tuple(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.monotonic()
    funcs = [(0,) + p for p in itertools.permutations(range(1, 8))]
    masks = [derivative_masks(f) for f in funcs]
    nonlinear = [not all(mask.bit_count() == 1 for mask in derivative) for derivative in masks]
    adj = [set() for _ in funcs]
    edges = [0, 0, 0]
    checked = 0
    complete_pairs = True
    next_outer = len(funcs)
    for i, di in enumerate(masks):
        if time.monotonic() - start > 40:
            complete_pairs = False
            next_outer = i
            break
        for j in range(i + 1, len(funcs)):
            checked += 1
            dj = masks[j]
            # Pair-product ONB criterion independently reduced to disjoint
            # derivative-value SETS at each nonzero group difference.
            if all(not (u & v) for u, v in zip(di, dj)):
                adj[i].add(j)
                edges[int(nonlinear[i]) + int(nonlinear[j])] += 1
    triangles = [0, 0, 0, 0]
    fours = [0, 0, 0, 0, 0]
    example_nonclassical_triangle = None
    complete_cliques = complete_pairs
    if complete_pairs:
        for i in range(len(funcs)):
            if time.monotonic() - start > 40:
                complete_cliques = False
                next_outer = i
                break
            for j in adj[i]:
                for k in adj[i].intersection(adj[j]):
                    degree = int(nonlinear[i]) + int(nonlinear[j]) + int(nonlinear[k])
                    triangles[degree] += 1
                    if degree and example_nonclassical_triangle is None:
                        example_nonclassical_triangle = [list(funcs[u]) for u in (i, j, k)]
                    for ell in adj[i].intersection(adj[j], adj[k]):
                        fours[degree + int(nonlinear[ell])] += 1
    result = {
        'kind': 'INDEPENDENT_DERIVATIVE_MASK_EXHAUSTION_RESTRICTED_SUBCLASS',
        'checker_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'normalized_permutations': len(funcs), 'nonlinear': sum(nonlinear),
        'pairs_checked': checked, 'edge_counts_by_nonlinear_members_0_1_2': edges,
        'triangle_counts_by_nonlinear_members_0_1_2_3': triangles,
        'four_clique_counts_by_nonlinear_members_0_1_2_3_4': fours,
        'pair_search_complete': complete_pairs, 'clique_search_complete': complete_cliques,
        'first_unchecked_outer_index': next_outer,
        'example_nonclassical_triangle_if_any': example_nonclassical_triangle,
        'arithmetic': 'integer bitmask derivative sets and ordered set intersections',
        'duration_seconds': time.monotonic() - start,
        'scope': 'All normalized permutations in the common-coordinate character subclass only; not all ordinary MOQLS families.'
    }
    with pathlib.Path(args.output).open('x', encoding='utf-8') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps(result, indent=2))
    if not (complete_pairs and complete_cliques):
        raise SystemExit(2)


if __name__ == '__main__':
    main()

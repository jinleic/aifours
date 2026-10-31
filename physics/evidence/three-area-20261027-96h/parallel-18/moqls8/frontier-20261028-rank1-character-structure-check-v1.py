#!/usr/bin/env python3
"""Exact full rank-one polar-class 3-bit character-square structure check.

No source from the other search programs is imported. This checks actual
64 vector sign lists and their ray/inner-product graphs, not a four-family.
"""
import argparse
import collections
import hashlib
import itertools
import json
import pathlib
import time


def rank_binary(values):
    pivots = {}
    for value in values:
        while value:
            bit = value.bit_length() - 1
            if bit in pivots:
                value ^= pivots[bit]
            else:
                pivots[bit] = value
                break
    return len(pivots)


def polar_rank(f):
    if len(f) != 8 or len(set(f)) != 8 or f[0] != 0:
        raise ValueError('not a normalized permutation')
    return rank_binary([f[3] ^ f[1] ^ f[2], f[5] ^ f[1] ^ f[4], f[6] ^ f[2] ^ f[4]])


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def classify(f):
    if polar_rank(f) != 1:
        raise ValueError('polar rank is not one')
    rows = []
    for i in range(8):
        rows.append([tuple(-1 if (((i & f[x]).bit_count() + (j & x).bit_count()) & 1)
                           else 1 for x in range(8)) for j in range(8)])
    for i in range(8):
        for j in range(8):
            for k in range(8):
                if dot(rows[i][j], rows[i][k]) != (8 if j == k else 0):
                    raise ValueError('actual row Gram failed')
                if dot(rows[j][i], rows[k][i]) != (8 if j == k else 0):
                    raise ValueError('actual column Gram failed')
    counts = collections.Counter(v for row in rows for v in row)
    # Every sign vector has first component +1, so ± phase ambiguity is fixed.
    if len(counts) != 16 or set(counts.values()) != {4}:
        raise ValueError('16 rays / multiplicity four failed')
    E = set(rows[0])
    other = set(counts) - E
    if len(other) != 8:
        raise ValueError('two complete ray bases failed')
    rowtypes = []
    for row in rows:
        rays = set(row)
        if rays == E:
            rowtypes.append('E')
        elif rays == other:
            rowtypes.append('F')
        else:
            raise ValueError('row is not one of two common bases')
    if rowtypes.count('E') != 4 or rowtypes.count('F') != 4:
        raise ValueError('row basis multiplicities failed')
    E, other = list(E), list(other)
    if any(dot(E[i], E[j]) != (8 if i == j else 0) for i in range(8) for j in range(8)):
        raise ValueError('first basis Gram failed')
    if any(dot(other[i], other[j]) != (8 if i == j else 0) for i in range(8) for j in range(8)):
        raise ValueError('second basis Gram failed')
    adjacency = [set() for _ in range(16)]
    for i in range(8):
        for j in range(8):
            val = abs(dot(E[i], other[j]))
            if val not in (0, 4):
                raise ValueError('cross overlaps are not 0 or 1/2')
            if val:
                adjacency[i].add(8+j)
                adjacency[8+j].add(i)
    if any(len(neighbors) != 4 for neighbors in adjacency):
        raise ValueError('cross-graph degree is not four')
    sizes = []
    unseen = set(range(16))
    while unseen:
        stack = [unseen.pop()]
        size = 0
        while stack:
            v = stack.pop()
            size += 1
            new = adjacency[v] & unseen
            unseen.difference_update(new)
            stack.extend(new)
        sizes.append(size)
    if sorted(sizes) != [8, 8]:
        raise ValueError('cross-graph is not two K4,4 components')
    return {'rays': len(counts), 'multiplicity': 4, 'E_rows': 4, 'F_rows': 4,
            'cross_degree': 4, 'component_sizes': sorted(sizes)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.monotonic()
    n = 0
    first = None
    for p in itertools.permutations(range(1, 8)):
        f = (0,) + p
        if polar_rank(f) != 1:
            continue
        summary = classify(f)
        if first is None:
            first = list(f)
        n += 1
    if n != 1176:
        raise ValueError('rank-one census not complete')
    try:
        classify(tuple(range(8)))
    except ValueError as exc:
        if str(exc) != 'polar rank is not one':
            raise
        negative = str(exc)
    else:
        raise ValueError('identity negative control was accepted')
    try:
        polar_rank((0,1,2,3,4,5,6,6))
    except ValueError as exc:
        invalid = str(exc)
    else:
        raise ValueError('nonpermutation negative control was accepted')
    result = {
        'result': 'PASS_EXACT_COMPLETE_RANK1_CHARACTER_STRUCTURE',
        'checker_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'rank_one_normalized_permutations_checked': n,
        'actual_row_and_column_gram_entries_per_function': 1024,
        'summary_for_every_function': summary,
        'first_normalized_permutation': first,
        'identity_negative_control': negative,
        'nonpermutation_negative_control': invalid,
        'seconds': time.monotonic() - start,
        'scope': 'All rank-one 3-bit normalized permutation character QLS only; no full MOQLS witness or universal no-go.'
    }
    with pathlib.Path(args.output).open('x', encoding='utf-8') as handle:
        json.dump(result, handle, indent=2)
        handle.write('\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

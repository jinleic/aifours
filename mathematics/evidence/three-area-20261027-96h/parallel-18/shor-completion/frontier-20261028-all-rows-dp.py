#!/usr/bin/env python3
"""Exact cyclic row packing upper bounds from literal Shor anchors.

State=the most recent eleven tail bits.  All permitted first-eleven masks
are determined from the row's forced original tails and old column A.  A
returned witness is rechecked directly against all cyclic forbidden gaps.
"""
import hashlib
import json
import sys

GAPS = (3, 5, 8, 11)
WIDTH = 11
MASK = (1 << WIDTH) - 1
ANCHORS = {'0': {0, 1, 7, 13, 14}, '3/8': {0, 2, 4, 6}, '11': {0, 1, 2}}


def optimum(n, required):
    first = {a for a in required if a < WIDTH}
    for i in set(range(WIDTH)) - first:
        if not any(abs(i - a) in GAPS for a in first):
            raise AssertionError(('additional initial state possible', i, first))
    if any(abs(i-j) in GAPS for i in first for j in first if i != j):
        raise AssertionError('inconsistent initial anchors')
    mask = sum(1 << (WIDTH - 1 - i) for i in first)
    best, parents = {mask: len(first)}, []
    max_states = 1
    for i in range(WIDTH, n):
        updated, parent = {}, {}
        wrap_blocked = any((n-(i-a)) in GAPS for a in first)
        for old, score in best.items():
            if i not in required:
                new = (old << 1) & MASK
                if score > updated.get(new, -1):
                    updated[new], parent[new] = score, (old, 0)
            if not wrap_blocked and not any(old & (1 << (d-1)) for d in GAPS):
                new = ((old << 1) | 1) & MASK
                if score+1 > updated.get(new, -1):
                    updated[new], parent[new] = score+1, (old, 1)
        if not updated:
            raise AssertionError(('empty frontier', n, i, required))
        best, parents = updated, parents + [parent]
        max_states = max(max_states, len(best))
    final = max(best, key=best.get)
    size = best[final]
    result = list(first)
    for i in range(n-1, WIDTH-1, -1):
        final, bit = parents[i-WIDTH][final]
        if bit:
            result.append(i)
    result.sort()
    forbidden = set(GAPS) | {n-d for d in GAPS}
    if len(result) != size or not required <= set(result):
        raise AssertionError('traceback does not retain required tails')
    if any((x-y) % n in forbidden for x in result for y in result if x != y):
        raise AssertionError('traceback violates a cyclic gap')
    return {'max_atoms': size, 'max_states': max_states,
            'witness_sha256': hashlib.sha256(','.join(map(str, result)).encode()).hexdigest(),
            'witness_start': result[:15], 'witness_end': result[-8:]}


def check(n):
    if n < 26:
        raise ValueError('n>=26 required')
    details = {row: optimum(n, anchors) for row, anchors in ANCHORS.items()}
    original_head_capacity = (details['0']['max_atoms'] + 2*details['3/8']['max_atoms']
                              + details['11']['max_atoms'])
    return {'n': n, 'rows': details, 'max_atoms_in_four_old_rows': original_head_capacity,
            'mandatory_outside_prefix_atoms': n-original_head_capacity}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('usage: all-rows-dp.py N [N ...]')
    ns = [int(x) for x in sys.argv[1:]]
    if len(ns) > 30 or max(ns) > 10000:
        raise SystemExit('bounded run: at most30 orders, max10000')
    print(json.dumps([check(n) for n in ns], indent=2))

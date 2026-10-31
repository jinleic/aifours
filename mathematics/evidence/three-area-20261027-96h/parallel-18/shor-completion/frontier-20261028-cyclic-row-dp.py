#!/usr/bin/env python3
"""Exact cyclic Shor row packing by width-11 dynamic programming.

The fixed old row requires 0,1,7,13,14.  The old suffix-zero column
forces the four forbidden cyclic differences 3,5,8,11.  This computes the
maximum cardinality for a specified order, not existence of a completion.
"""
import json
import sys

DIFFS = (3, 5, 8, 11)
ANCHORS = (0, 1, 7, 13, 14)
WIDTH = 11
ALL_BITS = (1 << WIDTH) - 1


def solve(n):
    if n < 26:
        raise ValueError('the literal row requires n>=26')
    first = {0, 1, 7}
    # These three forced positions exclude all other positions 0..10.
    for pos in set(range(WIDTH)) - first:
        if not any(abs(pos - a) in DIFFS for a in first):
            raise AssertionError(('unexpected initial candidate', pos))
    mask = sum(1 << (WIDTH - 1 - i) for i in first)
    best = {mask: len(first)}
    parents = []
    max_states = 1
    for i in range(WIDTH, n):
        future = {}
        parent = {}
        cyclic_banned = any((n - (i - a)) in DIFFS for a in first)
        for old_mask, score in best.items():
            if i not in ANCHORS:
                new_mask = (old_mask << 1) & ALL_BITS
                if score > future.get(new_mask, -1):
                    future[new_mask] = score
                    parent[new_mask] = (old_mask, 0)
            if (not cyclic_banned and
                    not any(old_mask & (1 << (d - 1)) for d in DIFFS)):
                new_mask = ((old_mask << 1) | 1) & ALL_BITS
                if score + 1 > future.get(new_mask, -1):
                    future[new_mask] = score + 1
                    parent[new_mask] = (old_mask, 1)
        if not future:
            raise AssertionError(('empty DP frontier', n, i))
        parents.append(parent)
        best = future
        max_states = max(max_states, len(best))
    final_mask = max(best, key=best.get)
    max_count = best[final_mask]
    indices = list(first)
    for i in range(n - 1, WIDTH - 1, -1):
        final_mask, bit = parents[i - WIDTH][final_mask]
        if bit:
            indices.append(i)
    indices.sort()
    if len(indices) != max_count or not set(ANCHORS) <= set(indices):
        raise AssertionError('DP traceback mismatch')
    if any((x - y) % n in set(DIFFS) | {n-d for d in DIFFS}
           for x in indices for y in indices if x != y):
        raise AssertionError('DP witness has a forbidden difference')
    return {'n': n, 'max_row0_atoms': max_count,
            'previous_forced_holes_bound': (n - 2) // 4,
            'mandatory_new_prefix_atoms_from_this_row': n - 3*(n//4) - max_count,
            'max_states': max_states, 'witness': indices}


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('usage: cyclic-row-dp.py ORDER [ORDER ...]')
    orders = [int(x) for x in sys.argv[1:]]
    if len(orders) > 30 or max(orders) > 20000:
        raise SystemExit('bounded run: at most30 orders, maximum20000')
    print(json.dumps([solve(n) for n in orders], indent=2))

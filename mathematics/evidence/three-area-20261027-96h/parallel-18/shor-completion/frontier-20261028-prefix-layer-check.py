#!/usr/bin/env python3
"""Exact finite checks for the all-order prefix-layer argument.

Checks actual two-atom ambiguity certificates for n=1..25 and validates the
fixed row-hole certificates for 26<=n<=MAX_N. The proof extends these finite
checks symbolically; this program alone does not certify all orders.
"""
import json
import sys

A = (0, 3, 8, 11)
ROWS = {0: (0, 1, 7, 13, 14), 3: (0, 2, 4, 6),
        8: (0, 2, 4, 6), 11: (0, 1, 2)}
D = (1, 2, 4, 6, 7, 12, 13, 14)
E = (3, 5, 8, 11)


def word(i, j):
    return 'a' * i + 'b' + 'a' * j


def small_order_certificate(n):
    d, e = next((d, e) for d in D for e in E if (d + e) % n == 0)
    t, p, q = next((t, p, q) for t, js in ROWS.items() for p in js for q in js
                   if p - q == d)
    v, w = next((v, w) for v in A for w in A if v - w == e)
    left = [word(t, p), word(v, 0)]
    right = [word(t, q)] + ['a' * n] * ((d + e) // n) + [word(w, 0)]
    if left == right or ''.join(left) != ''.join(right):
        raise AssertionError('bad small-order ambiguity')
    return {'n': n, 'row_tail_difference': d, 'column_head_difference': e,
            'long_gap': p + v, 'short_gap': q + w,
            'n_pads': (d + e) // n}


def hole_certificate(n, row, target):
    anchors = ROWS[row]
    witnesses = []
    for a in A:
        candidate = (target - a) % n
        conflict = next(((old, x, y) for old in anchors for x in A for y in A
                         if candidate != old % n
                         and (candidate + x - old - y) % n == 0), None)
        if conflict is None:
            raise AssertionError((n, row, target, a, candidate))
        witnesses.append({'possible_tail': candidate,
                          'conflicting_old_tail': conflict[0],
                          'possible_head': conflict[1], 'old_head': conflict[2]})
    return witnesses


def check(max_n):
    if not 26 <= max_n <= 10000:
        raise ValueError('require 26 <= MAX_N <= 10000')
    certs = [small_order_certificate(n) for n in range(1, 26)]
    holes = {0: (6, 19), 11: (6, 7)}
    for n in range(26, max_n + 1):
        for row, targets in holes.items():
            for target in targets:
                hole_certificate(n, row, target)
    return {'small_orders_with_actual_equal-word_certificates': len(certs),
            'small_order_differences': [[x['n'], x['row_tail_difference'],
                                         x['column_head_difference'], x['n_pads']]
                                        for x in certs],
            'checked_hole_n_range': [26, max_n],
            'holes_by_old_head_residue': holes,
            'sample_n': max_n,
            'sample_certificates': {str(row): {str(t): hole_certificate(max_n, row, t)
                                                for t in targets}
                                    for row, targets in holes.items()},
            'scope': 'finite checks of an independently stated all-order proof, not a completion verdict'}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: prefix-layer-check.py MAX_N')
    print(json.dumps(check(int(sys.argv[1])), indent=2, sort_keys=True))

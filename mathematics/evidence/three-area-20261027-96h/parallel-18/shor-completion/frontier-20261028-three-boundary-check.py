#!/usr/bin/env python3
"""Independently check the literal-code 3-atom obstruction at one order.

This script enumerates a bounded, mathematically specified residue family.
It directly compares every generated raw ambiguity and independently checks
all two-atom residue keys; it does not establish the original open problem.
"""
import json
import sys

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
ROWS = {0: Y, 3: (0, 2, 4, 6), 8: (0, 2, 4, 6), 11: (0, 1, 2)}
OLD = tuple((i, j) for i, js in ROWS.items() for j in js)


def atom(i, j):
    return 'a' * i + 'b' + 'a' * j


def keys_unique(pairs, n):
    keys = set()
    for i, j in pairs:
        for k, l in pairs:
            key = (i % n, (j + k) % n, l % n)
            if key in keys:
                return False
            keys.add(key)
    return True


def derive_witness(n, r, s):
    first = next((t, p, q) for t, js in ROWS.items() for p in js for q in js
                 if p != q and (p - q) % n == r)
    second = next((j, v, w) for j in Y for v in A for w in A
                  if (j + v - w) % n == s)
    t, p, q = first
    j, v, w = second
    left_gaps = (p, j + v)
    right_gaps = (q + r, s + w)
    if any((x - y) % n for x, y in zip(left_gaps, right_gaps)):
        raise AssertionError('incompatible residues')
    common = tuple(max(x, y) for x, y in zip(left_gaps, right_gaps))
    left = [atom(t, p)] + ['a' * n] * ((common[0] - left_gaps[0]) // n)
    left += [atom(0, j)] + ['a' * n] * ((common[1] - left_gaps[1]) // n)
    left += [atom(v, 0)]
    right = [atom(t, q)] + ['a' * n] * ((common[0] - right_gaps[0]) // n)
    right += [atom(r, s)] + ['a' * n] * ((common[1] - right_gaps[1]) // n)
    right += [atom(w, 0)]
    allowed = {atom(i, j) for i, j in OLD} | {'a' * n, atom(r, s)}
    if (left == right or ''.join(left) != ''.join(right)
            or not set(left + right) <= allowed or atom(r, s) not in right
            or atom(r, s) in left):
        raise AssertionError('invalid witness')
    return {'first': first, 'second': second,
            'pad_counts': [(common[k] - left_gaps[k]) // n for k in range(2)]
                        + [(common[k] - right_gaps[k]) // n for k in range(2)],
            'word_length': len(''.join(left))}


def check(n):
    if n < 37:
        raise ValueError('the disjoint-residue counting claim requires n>=37')
    heads = {(p - q) % n for js in ROWS.values() for p in js for q in js if p != q}
    tails = {(j + v - w) % n for j in Y for v in A for w in A}
    old_cols = {j % n for _, j in OLD}
    tails_outside = tails - old_cols
    if len(OLD) != 16 or len(heads) != 16 or len(tails) != 33 or len(tails_outside) != 25:
        raise AssertionError('unexpected literal residue counts')
    if heads & {i % n for i in A} or tails_outside & old_cols:
        raise AssertionError('new row/column not disjoint')
    if not keys_unique(OLD, n):
        raise AssertionError('old two-boundary keys collide')
    count = 0
    for r in sorted(heads):
        for s in sorted(tails_outside):
            if not keys_unique(OLD + ((r, s),), n):
                raise AssertionError('a candidate fails the claimed two-atom filter')
            derive_witness(n, r, s)
            count += 1
    return {'pure_a_exponent': n, 'old_pairs': len(OLD),
            'forbidden_new_head_residues': sorted(heads),
            'all_forbidden_tail_residues': sorted(tails),
            'tail_residues_outside_old_columns': sorted(tails_outside),
            'two_boundary_clear_three_boundary_ambiguous': count,
            'example_candidate': [1, 3],
            'example_verified_witness': derive_witness(n, 1, 3),
            'scope': 'bounded exact residue scan and raw-word equality only; no completion verdict'}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: three-boundary-check.py PURE_A_EXPONENT')
    print(json.dumps(check(int(sys.argv[1])), indent=2, sort_keys=True))

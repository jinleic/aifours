#!/usr/bin/env python3
"""Check a bounded range of explicit noncompletable Shor supercodes.

Each outside-prefix candidate gets an actual equal-word ambiguity witness;
old-prefix saturation is checked through endpoint packing. Base UD is checked
independently by set-valued Sardinas-Patterson residual iteration.
"""
import json
import sys

A = (0, 3, 8, 11)
OLD = {(0, j) for j in (0, 1, 7, 13, 14)}
OLD |= {(i, j) for i in (3, 8) for j in (0, 2, 4, 6)}
OLD |= {(11, j) for j in (0, 1, 2)}


def atom(i, j):
    return b'a' * i + b'b' + b'a' * j


def rows(n):
    if n % 16 or n < 32:
        raise ValueError('n must be a multiple of16, at least32')
    m = n // 16
    zero = {0, 1, 7, 13, 14, 20, 26}
    eleven = {0, 1, 2, 14, 16, 18, 20}
    for k in range(m - 2):
        t = 32 + 16 * k
        zero.update((t - 2, t, t + 4, t + 10))
        eleven.update((t - 2, t, t + 2, t + 4))
    middle = {16 * k + d for k in range(m) for d in (0, 2, 4, 6)}
    return {0: zero, 3: middle, 8: middle, 11: eleven}


def ud_by_residual_sets(words):
    """Standard SP set recurrence, independently implemented without witnesses."""
    words = set(words)
    if b'' in words:
        return False
    current = {y[len(x):] for x in words for y in words
               if len(y) > len(x) and y.startswith(x)}
    seen = set()
    while current:
        if current & words:
            return False
        current -= seen
        if not current:
            return True
        seen |= current
        nxt = set()
        for suffix in current:
            for word in words:
                if len(suffix) > len(word) and suffix.startswith(word):
                    nxt.add(suffix[len(word):])
                if len(word) > len(suffix) and word.startswith(suffix):
                    nxt.add(word[len(suffix):])
        current = nxt
    return True


def check(n):
    R = rows(n)
    pairs = {(i, j) for i, js in R.items() for j in js}
    if not OLD <= pairs or len(pairs) != n - 2:
        raise AssertionError('base layer does not have required original atoms/count')
    for i, js in R.items():
        image = [(j + a) % n for j in js for a in A]
        if len(image) != len(set(image)):
            raise AssertionError(('row packing collision', n, i))
        absent = set(range(n)) - set(image)
        required = {0: {6, 19}, 3: set(), 8: set(), 11: {6, 7}}[i]
        if not required <= absent:
            raise AssertionError(('row-hole certificate failed', n, i))
    words = {atom(i, j) for i, j in pairs} | {b'a' * n}
    if not ud_by_residual_sets(words):
        raise AssertionError(('base is not UD', n))

    differences = {}
    for t, js in R.items():
        for p in js:
            for q in js:
                if p != q:
                    differences[(p - q) % n] = (t, p, q)
    tilings = {}
    for u in (3, 8):
        mapping = {}
        for j in R[u]:
            for v in A:
                key = (j + v) % n
                if key in mapping:
                    raise AssertionError('not a tiling')
                mapping[key] = (j, v)
        if len(mapping) != n:
            raise AssertionError('incomplete tiling')
        tilings[u] = mapping

    witnesses = 0
    for r in range(n):
        if r in A:
            continue
        u = next((u for u in (3, 8) if (r - u) % n in differences), None)
        if u is None:
            raise AssertionError(('uncovered new prefix', n, r))
        t, p, q = differences[(r - u) % n]
        for s in range(n):
            j, v = tilings[u][s]
            left_gaps = (p + u, j + v)
            right_gaps = (q + r, s)
            common = tuple(max(x, y) for x, y in zip(left_gaps, right_gaps))
            if any((x - y) % n for x, y in zip(left_gaps, right_gaps)):
                raise AssertionError('seam residues differ')
            left = [atom(t, p)] + [b'a' * n] * ((common[0] - left_gaps[0]) // n)
            left += [atom(u, j)] + [b'a' * n] * ((common[1] - left_gaps[1]) // n)
            left += [atom(v, 0)]
            right = [atom(t, q)] + [b'a' * n] * ((common[0] - right_gaps[0]) // n)
            right += [atom(r, s)] + [b'a' * n] * ((common[1] - right_gaps[1]) // n)
            right += [atom(0, 0)]
            if left == right or b''.join(left) != b''.join(right):
                raise AssertionError(('bad new-prefix ambiguity', n, r, s))
            witnesses += 1
    return {'n': n, 'one_b_atoms': len(pairs), 'base_ud_by_SP': True,
            'row_sizes': {str(i): len(R[i]) for i in A},
            'outside_prefix_raw_ambiguity_witnesses': witnesses,
            'old_prefixes_saturated_by_row_packing': True}


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: dead-end-family-check.py MAX_N')
    limit = int(sys.argv[1])
    if not 32 <= limit <= 512:
        raise SystemExit('require 32 <= MAX_N <= 512')
    print(json.dumps([check(n) for n in range(32, limit + 1, 16)], indent=2))

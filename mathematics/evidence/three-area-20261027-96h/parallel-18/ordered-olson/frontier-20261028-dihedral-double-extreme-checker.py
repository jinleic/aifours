#!/usr/bin/env python3
"""Independently check both extreme selector modes and the interior witness."""

import argparse
import hashlib
import itertools
import json


def calculate(word, chosen, p):
    sign = 1
    rotation = 0
    parity = 0
    for i in chosen:
        exponent, kind = word[i]
        rotation = (rotation + sign*exponent) % p
        if kind:
            parity ^= 1
            sign = -sign
    return rotation, parity


def check(row):
    p, word = row['p'], row['word']
    rlen = 2*p+1
    expected = [[0, 1]]*(2*p-1) + [[1, 1], [2 % p, 1]] + [[1, 0]]*(2*p-3) + [[2 % p, 0]]
    if word != expected or len(word) != 4*p-1:
        raise ValueError('actual full word does not match family')
    reflection_results = [calculate(word, [j for j in range(rlen) if j != i], p) for i in range(rlen)]
    expected_reflections = [((-2 if i == 2*p-1 else -1) % p, 0) for i in range(rlen)]
    if reflection_results != expected_reflections or any(x == (0, 0) for x in reflection_results):
        raise ValueError('reflection-only extreme product mismatch')
    if row['reflection_only_identity_omissions']:
        raise ValueError('incorrect declared reflection-only successes')
    rotations = list(range(rlen, len(word)))
    successes = [list(pair) for pair in itertools.combinations(range(rlen), 2)
                 if calculate(word, list(pair) + rotations, p) == (0, 0)]
    if successes != row['all_rotation_identity_reflection_pairs']:
        raise ValueError('all-rotations extreme pair list mismatch')
    if p >= 5 and successes:
        raise ValueError('all-rotation extreme unexpectedly succeeds')
    if p == 3 and len(successes) != 2*p-1:
        raise ValueError('p=3 boundary negative control mismatch')
    chosen = row['interior_selector_zero_based']
    if len(chosen) != 2*p or chosen != sorted(set(chosen)) or any(i < 0 or i >= len(word) for i in chosen):
        raise ValueError('interior selector indices invalid')
    if calculate(word, chosen, p) != (0, 0) or row['interior_selector_product'] != [0, 0]:
        raise ValueError('interior selector product invalid')
    return len(successes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    records = data['records']
    if [row['p'] for row in records] != [3, 5, 7, 11, 13]:
        raise ValueError('unexpected bounded domains')
    counts = [{'p': row['p'], 'all_rotation_two_reflection_successes': check(row)} for row in records]
    print(json.dumps({'result': 'PASS_INDEPENDENT_FULL_WORD_CHECK',
                      'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'domains': counts, 'all_interior_selectors_valid': True,
                      'scope': 'bounded checks of two selector modes; no original avoiding word'}, sort_keys=True))


if __name__ == '__main__':
    main()

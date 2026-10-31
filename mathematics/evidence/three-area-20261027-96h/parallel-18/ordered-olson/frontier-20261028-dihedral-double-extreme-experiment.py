#!/usr/bin/env python3
"""Bounded exact checks of the full-word two-extreme obstruction family."""

import argparse
import itertools
import json


def product(word, indices, p):
    x = bit = 0
    for i in indices:
        y, b = word[i]
        x = (x + (y if bit == 0 else -y)) % p
        bit ^= b
    return x, bit


def assay(p):
    # p is a declared odd prime in the small fixed scientific corpus.
    reflections = [(0, 1)]*(2*p-1) + [(1, 1), (2 % p, 1)]
    rotations = [(1, 0)]*(2*p-3) + [(2 % p, 0)]
    word = reflections + rotations
    if len(word) != 4*p-1 or len(reflections) != 2*p+1 or len(rotations) != 2*p-2:
        raise RuntimeError('bad original word layout')
    reflection_only = []
    for omit in range(len(reflections)):
        indices = [i for i in range(len(reflections)) if i != omit]
        if product(word, indices, p) == (0, 0):
            reflection_only.append(omit)
    all_rotation_two_reflection = []
    rotation_indices = list(range(len(reflections), len(word)))
    for i, j in itertools.combinations(range(len(reflections)), 2):
        if product(word, [i, j] + rotation_indices, p) == (0, 0):
            all_rotation_two_reflection.append([i, j])
    witness = list(range(p+1)) + list(range(len(reflections), len(reflections)+p-2)) + [len(word)-1]
    witness_product = product(word, witness, p)
    if len(witness) != 2*p or witness != sorted(set(witness)) or witness_product != (0, 0):
        raise RuntimeError('interior-selector witness invalid')
    if reflection_only:
        raise RuntimeError('reflection-only obstruction failed')
    if p >= 5 and all_rotation_two_reflection:
        raise RuntimeError('all-rotation/two-reflection obstruction failed')
    if p == 3 and not all_rotation_two_reflection:
        raise RuntimeError('p=3 boundary negative-control not detected')
    return {'p': p, 'word': word, 'original_word_length': len(word),
            'reflection_only_omissions_checked': len(reflections),
            'reflection_only_identity_omissions': reflection_only,
            'all_rotation_reflection_pairs_checked': (len(reflections)*(len(reflections)-1))//2,
            'all_rotation_identity_reflection_pairs': all_rotation_two_reflection,
            'interior_selector_zero_based': witness, 'interior_selector_product': witness_product}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    records = [assay(p) for p in (3, 5, 7, 11, 13)]
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump({'scope': 'two fixed extreme selector modes; not a full-word counterexample',
                   'records': records}, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'result': 'PASS_BOUNDED_DOUBLE_EXTREMES',
                      'domains': [{'p': row['p'],
                                   'reflection_only_successes': len(row['reflection_only_identity_omissions']),
                                   'all_rotation_two_reflection_successes': len(row['all_rotation_identity_reflection_pairs']),
                                   'interior_selector_verified': row['interior_selector_product'] == (0, 0)}
                                  for row in records], 'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()

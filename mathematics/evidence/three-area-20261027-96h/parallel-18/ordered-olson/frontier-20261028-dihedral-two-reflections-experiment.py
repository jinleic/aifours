#!/usr/bin/env python3
"""Bounded exact tests of a 2p-2 rotations plus two reflections selector.

This is a finite corpus and does not prove the ordered Olson conjecture.
"""

import argparse
import hashlib
import json
import random


def multiply(a, b, prime):
    x, epsilon = a
    y, delta = b
    return ((x + (y if epsilon == 0 else -y)) % prime, (epsilon + delta) % 2)


def analyze(word, prime):
    rotation_indices = [i for i, (_, bit) in enumerate(word) if bit == 0]
    reflection_indices = [i for i, (_, bit) in enumerate(word) if bit == 1]
    fixed = rotation_indices[:2 * prime - 2]
    if len(fixed) != 2 * prime - 2:
        raise ValueError('too few rotations')
    if len(reflection_indices) <= prime:
        raise ValueError('too few reflections for this stated envelope')
    marked = set(fixed)
    prefix = 0
    z = []
    for index, (exponent, bit) in enumerate(word):
        if bit == 0 and index in marked:
            prefix = (prefix + exponent) % prime
        elif bit == 1:
            z.append((index, (exponent + 2 * prefix) % prime))
    total = prefix
    complete = len({value for _, value in z}) == prime
    selected_pair = None
    for left in range(len(z)):
        for right in range(left + 1, len(z)):
            if (z[right][1] - z[left][1]) % prime == total:
                selected_pair = (z[left][0], z[right][0])
                break
        if selected_pair is not None:
            break
    promised = (total == 0 or complete)
    if promised and selected_pair is None:
        raise RuntimeError('pigeonhole/coverage condition failed to find a pair')
    selected = sorted(fixed + list(selected_pair)) if selected_pair is not None else None
    direct = None
    if selected is not None:
        if len(selected) != 2 * prime or len(set(selected)) != len(selected):
            raise RuntimeError('incorrect original selector cardinality')
        direct = (0, 0)
        for i in selected:
            direct = multiply(direct, word[i], prime)
        if direct != (0, 0):
            raise RuntimeError('actual increasing-index group product is not identity')
    return {'rotation_count': len(rotation_indices), 'reflection_count': len(reflection_indices),
            'selected_rotations': fixed, 'rotation_sum_mod_p': total,
            'prefix_adjusted_reflections': z, 'full_prefix_coverage': complete,
            'selector_promised_by_theorem': promised,
            'selected_reflections': selected_pair, 'selected_original_indices': selected,
            'direct_product': direct}


def explicit_alternating(prime):
    word = []
    selected_rotation_count = 2 * prime - 2
    for j in range(2 * prime):
        prefix_count = min(j, selected_rotation_count)
        word.append(((j - 2 * prefix_count) % prime, 1))
        if j < 2 * prime - 1:
            word.append((1, 0))
    return word


def random_word(prime, rotations, rng):
    n = 4 * prime - 1
    positions = set(rng.sample(range(n), rotations))
    return [(rng.randrange(prime), 0 if i in positions else 1) for i in range(n)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    seed = 2026102802
    rng = random.Random(seed)
    domains = []
    examples = []
    for prime in (3, 5, 7):
        n = 4 * prime - 1
        explicit = explicit_alternating(prime)
        if len(explicit) != n:
            raise RuntimeError('explicit family not a full original word')
        analysis = analyze(explicit, prime)
        if analysis['rotation_sum_mod_p'] == 0 or not analysis['full_prefix_coverage']:
            raise RuntimeError('explicit alternating family did not meet stated nonzero/full premise')
        examples.append({'kind': 'all-variable-family-specialization', 'prime': prime,
                         'word': explicit, 'analysis': analysis,
                         'word_sha256': hashlib.sha256(json.dumps(explicit, separators=(',', ':')).encode()).hexdigest()})
        for rotations in range(2 * prime - 2, 3 * prime - 1):
            counts = {'total': 0, 'promised': 0, 'sum_zero': 0, 'full_coverage': 0,
                      'additional_pair_found': 0}
            representative = None
            for trial in range(80):
                word = random_word(prime, rotations, rng)
                result = analyze(word, prime)
                counts['total'] += 1
                counts['sum_zero'] += int(result['rotation_sum_mod_p'] == 0)
                counts['full_coverage'] += int(result['full_prefix_coverage'])
                counts['promised'] += int(result['selector_promised_by_theorem'])
                counts['additional_pair_found'] += int(result['selected_reflections'] is not None and
                                                       not result['selector_promised_by_theorem'])
                if result['selector_promised_by_theorem'] and representative is None:
                    representative = {'trial': trial, 'word': word, 'analysis': result,
                                      'word_sha256': hashlib.sha256(json.dumps(word, separators=(',', ':')).encode()).hexdigest()}
            domains.append({'prime': prime, 'rotation_count': rotations, 'counts': counts,
                            'representative': representative})
    data = {'scope': 'bounded exact sample and explicit family checks; not proof of original conjecture',
            'seed': seed, 'explicit_families': examples, 'domains': domains}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'result': 'PASS_BOUNDED_ACTUAL_WORDS', 'seed': seed,
                      'total_random_words': sum(x['counts']['total'] for x in domains),
                      'theorem_promised_words': sum(x['counts']['promised'] for x in domains),
                      'additional_found_outside_sufficient_condition': sum(x['counts']['additional_pair_found'] for x in domains),
                      'explicit_family_instances': len(examples), 'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()

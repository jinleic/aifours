#!/usr/bin/env python3
"""Replay bounded dihedral words and check ordered cross-cut support bounds."""

import argparse
import itertools
import json
import random


def product(word, indices, p):
    value = bit = 0
    for i in indices:
        exponent, parity = word[i]
        value = (value + (exponent if bit == 0 else -exponent)) % p
        bit ^= parity
    return value, bit


def inspect(word, p):
    rotations = [i for i, (_, bit) in enumerate(word) if bit == 0][:2*p-2]
    reflections = [i for i, (_, bit) in enumerate(word) if bit == 1]
    if len(rotations) != 2*p-2:
        raise ValueError('wrong number of selected rotations')
    total = sum(word[i][0] for i in rotations) % p
    potentials = [(i, (word[i][0] + 2*sum(word[j][0] for j in rotations if j < i)) % p)
                  for i in reflections]
    full = len({z for _, z in potentials}) == p
    old_condition = total == 0 or full
    good_cuts = []
    for cut in range(1, len(potentials)):
        before = potentials[:cut]
        after = potentials[cut:]
        left = {z for _, z in before}
        right = {z for _, z in after}
        lower = max(0, len(left)+len(right)-p)
        pairs = [(i, j) for i, x in before for j, y in after if (y-x) % p == total]
        if len(pairs) < lower:
            raise ValueError('cross-cut pair lower bound failed')
        if lower:
            for i, j in pairs:
                if product(word, sorted(rotations+[i, j]), p) != (0, 0):
                    raise ValueError('cross-cut candidate is not actual identity')
            good_cuts.append({'cut_after_reflection_count': cut, 'left_support': sorted(left),
                              'right_support': sorted(right), 'lower_bound': lower,
                              'actual_cross_cut_pairs': len(pairs), 'first_pair': pairs[0]})
    return {'rotation_sum': total, 'old_condition': old_condition,
            'full_potential_support': full, 'good_cuts': good_cuts,
            'potentials': potentials, 'selected_rotations': rotations}


def proper_support_family(p):
    h = (p-1)//2
    labels = list(range(h+1))*2
    word = [(z, 1) for z in labels] + [(1, 0)]*(3*p-2)
    if len(word) != 4*p-1:
        raise ValueError('family original word length incorrect')
    result = inspect(word, p)
    cut = next((row for row in result['good_cuts'] if row['cut_after_reflection_count'] == h+1), None)
    if result['old_condition'] or cut is None:
        raise ValueError('family not a strict fixed-I improvement')
    return {'p': p, 'word': word, 'analysis': result, 'specified_middle_cut': cut}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rng = random.Random(2026102802)
    rows = []
    for p in (3, 5, 7):
        for r in range(2*p-2, 3*p-1):
            improved = 0
            any_cut = 0
            representative = None
            for trial in range(80):
                positions = set(rng.sample(range(4*p-1), r))
                word = [(rng.randrange(p), 0 if i in positions else 1) for i in range(4*p-1)]
                result = inspect(word, p)
                any_cut += int(bool(result['good_cuts']))
                if result['good_cuts'] and not result['old_condition']:
                    improved += 1
                    if representative is None:
                        representative = {'trial': trial, 'word': word, 'analysis': result}
            rows.append({'p': p, 'rotation_count': r, 'sampled': 80,
                         'at_least_one_cut_certificate': any_cut,
                         'strict_fixed_I_improvements': improved,
                         'first_improvement': representative})
    data = {'scope': 'bounded actual-word cut-support checks; not universal selector verification',
            'seed': 2026102802, 'domains': rows,
            'proper_support_family_checks': [proper_support_family(p) for p in (3, 5, 7)]}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(data, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'result': 'PASS_BOUNDED_CROSSCUT',
                      'sampled_words': sum(row['sampled'] for row in rows),
                      'words_with_cut_certificate': sum(row['at_least_one_cut_certificate'] for row in rows),
                      'strict_fixed_I_improvements': sum(row['strict_fixed_I_improvements'] for row in rows),
                      'all_prime_family_specializations_checked': len(data['proper_support_family_checks']),
                      'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()

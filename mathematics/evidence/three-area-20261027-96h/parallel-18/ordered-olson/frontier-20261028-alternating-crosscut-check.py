#!/usr/bin/env python3
"""Directly check a symbolic alternating D_(2p) cross-cut family at bounded primes."""

import argparse
import json


def direct(word, selected, p):
    x = parity = 0
    for i in selected:
        y, bit = word[i]
        x = (x + y if parity == 0 else x - y) % p
        parity ^= bit
    return x, parity


def max_separated(bits):
    m = len(bits)
    best = [0]*(m+1)
    for i in range(m-1, -1, -1):
        best[i] = best[i+1]
        for j in range(i+1, m):
            if bits[i] == bits[j]:
                best[i] = max(best[i], 1+best[j+1])
    return best[0]


def check(p):
    h = (p-1)//2
    vals = [j % (h+1) for j in range(p)] * 2
    selected_rotations_count = 2*p-2
    word = []
    for j in range(2*p):
        prefix_count = min(j, selected_rotations_count)
        word.append(((vals[j]-2*prefix_count) % p, 1))
        if j < 2*p-1:
            word.append((1, 0))
    if len(word) != 4*p-1:
        raise ValueError('wrong original word length')
    rotations = [i for i, (_, bit) in enumerate(word) if bit == 0][:selected_rotations_count]
    refs = [i for i, (_, bit) in enumerate(word) if bit == 1]
    z = [(word[i][0] + 2*sum(word[j][0] for j in rotations if j < i)) % p for i in refs]
    if z != vals:
        raise ValueError('actual prefix potentials mismatch')
    S = sum(word[i][0] for i in rotations) % p
    A, B = set(z[:p]), set(z[p:])
    if S == 0 or len(set(z)) == p or len(A)+len(B) <= p:
        raise ValueError('not a strict improvement')
    possible = [(i, j) for i in range(p) for j in range(p, 2*p) if (z[j]-z[i]) % p == S]
    if not possible:
        raise ValueError('missing ordered crosscut pair')
    i, j = possible[0]
    chosen = sorted(rotations + [refs[i], refs[j]])
    if len(chosen) != 2*p or len(set(chosen)) != len(chosen) or direct(word, chosen, p) != (0, 0):
        raise ValueError('actual selector invalid')
    max_pairs = max_separated([bit for _, bit in word])
    if max_pairs >= 2*p-1:
        raise ValueError('alternating word unexpectedly satisfies separated-packet condition')
    return {'p': p, 'word': word, 'potential_support': sorted(set(z)),
            'rotation_sum': S, 'left_support': sorted(A), 'right_support': sorted(B),
            'cut_pairs': len(possible), 'chosen_indices_zero_based': chosen,
            'chosen_direct_product': (0, 0), 'maximum_separated_pairs': max_pairs,
            'needed_separated_pairs': 2*p-1}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    cases = [check(p) for p in (3, 5, 7, 11, 13)]
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump({'scope': 'bounded direct checks of an all-prime family, not full conjecture',
                   'cases': cases}, stream, indent=2)
        stream.write('\n')
    print(json.dumps({'result': 'PASS_ALTERNATING_STRICT_IMPROVEMENT',
                      'domains': [{'p': c['p'], 'potential_support_size': len(c['potential_support']),
                                   'cut_pairs': c['cut_pairs'],
                                   'maximum_separated_pairs': c['maximum_separated_pairs'],
                                   'needed_separated_pairs': c['needed_separated_pairs']}
                                  for c in cases], 'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()

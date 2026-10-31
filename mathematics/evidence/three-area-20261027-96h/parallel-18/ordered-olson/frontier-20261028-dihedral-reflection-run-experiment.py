#!/usr/bin/env python3
"""Exact bounded checks of a long-reflection-run adaptive selector."""

import argparse
from collections import defaultdict, deque
import heapq
import itertools
import json
import random


def direct(word, indices, p):
    exponent = parity = 0
    for i in indices:
        x, bit = word[i]
        exponent = (exponent + x if parity == 0 else exponent - x) % p
        parity ^= bit
    return exponent, parity


def rotation_pairs(word):
    groups = defaultdict(deque)
    for i, (value, bit) in enumerate(word):
        if bit == 0:
            groups[value].append(i)
    heap = [(-len(indices), value) for value, indices in groups.items()]
    heapq.heapify(heap)
    pairs = []
    while len(heap) >= 2:
        count_a, a = heapq.heappop(heap)
        count_b, b = heapq.heappop(heap)
        pairs.append(tuple(sorted((groups[a].popleft(), groups[b].popleft()))))
        if count_a+1 < 0:
            heapq.heappush(heap, (count_a+1, a))
        if count_b+1 < 0:
            heapq.heappush(heap, (count_b+1, b))
    return pairs


def reflection_runs(word):
    runs = []
    start = None
    for i, (_, bit) in enumerate(word + [(0, 0)]):
        if bit == 1 and start is None:
            start = i
        elif bit == 0 and start is not None:
            runs.append(tuple(range(start, i)))
            start = None
    return runs


def process(word, p, label):
    rotations = [i for i, (_, bit) in enumerate(word) if bit == 0]
    R = len(rotations)
    t = R-(2*p-2)
    pairs = rotation_pairs(word)
    runs = reflection_runs(word)
    suitable = [run for run in runs if len(run) >= p+1 and
                len({word[i][0] for i in run})+t >= p]
    eligible = t >= 0 and len(pairs) >= t and bool(suitable)
    result = {'p': p, 'label': label, 'word': word, 'R': R, 't': t,
              'all_rotation_pairs': pairs, 'eligible': eligible,
              'reflection_run': None, 'omitted_rotations': None, 'selected_indices': None}
    if not eligible:
        return result
    run = suitable[0]
    differences = {}
    for i, j in itertools.combinations(run, 2):
        differences.setdefault((word[j][0]-word[i][0]) % p, (i, j))
    distinct = len({word[i][0] for i in run})
    if len(differences) < distinct:
        raise ValueError('ordered reflection difference lower bound failed')
    states = {0: ()}
    for a, b in pairs[:t]:
        new = {}
        for total, path in states.items():
            new.setdefault((total+word[a][0]) % p, path+(a,))
            new.setdefault((total+word[b][0]) % p, path+(b,))
        states = new
    if len(states) < min(p, t+1):
        raise ValueError('actual omission-sum growth bound failed')
    total_rotation = sum(word[i][0] for i in rotations) % p
    chosen = next(((omitted_sum, diff, pair) for omitted_sum in states
                   for diff, pair in differences.items()
                   if (total_rotation-omitted_sum) % p == diff), None)
    if chosen is None:
        raise ValueError('required actual sum/difference intersection absent')
    omitted_sum, _, refpair = chosen
    omitted = states[omitted_sum]
    chosen_indices = sorted([i for i in rotations if i not in set(omitted)] + list(refpair))
    if len(chosen_indices) != 2*p or len(set(chosen_indices)) != 2*p or direct(word, chosen_indices, p) != (0, 0):
        raise ValueError('actual ordered selector incorrect')
    result.update({'reflection_run': run, 'omitted_rotations': omitted,
                   'selected_reflections': refpair, 'selected_indices': chosen_indices,
                   'distinct_reflection_values': distinct,
                   'omission_support_size': len(states), 'difference_support_size': len(differences)})
    return result


def random_word(p, R, rng):
    F = 4*p-1-R
    remainder = [0]*R + [1]*(F-(p+1))
    rng.shuffle(remainder)
    cut = rng.randrange(len(remainder)+1)
    bits = remainder[:cut] + [1]*(p+1) + remainder[cut:]
    return [(rng.randrange(p), bit) for bit in bits]


def structured(p):
    T = [(2*j) % p for j in range(1, p)]
    last = (-2) % p
    result = [(0, 0)]*p + [(y, 1) for y in T+[last, last]]
    for j in range(1, p):
        result.append((1, 0))
        result.append(((last-2*min(j, p-2)) % p, 1))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rng = random.Random(2026102805)
    cases = []
    for p in (3, 5, 7, 11):
        for R in range(2*p-2, 3*p-1):
            for trial in range(40):
                cases.append(process(random_word(p, R, rng), p, {'kind': 'random', 'R': R, 'trial': trial}))
    families = [process(structured(p), p, {'kind': 'structured'}) for p in (3, 5, 7, 11)]
    if not all(row['eligible'] for row in families):
        raise ValueError('structured all-prime family failed the hypotheses')
    data = {'scope': 'bounded actual-word corpus, not universal proof', 'seed': 2026102805,
            'random_cases': cases, 'structured_cases': families}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(data, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'result': 'PASS_BOUNDED_REFLECTION_RUN', 'random_words': len(cases),
                      'eligible_random_words': sum(c['eligible'] for c in cases),
                      'structured_words': len(families),
                      'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact bounded actual-word checks of the same-reflection-gap selector."""

import argparse
from collections import defaultdict, deque
import heapq
import itertools
import json
import random


def direct(word, selected, p):
    exponent = bit = 0
    for i in selected:
        x, kind = word[i]
        exponent = (exponent + (x if bit == 0 else -x)) % p
        bit ^= kind
    return exponent, bit


def gap_pairs(word):
    gaps = defaultdict(lambda: defaultdict(deque))
    gap = 0
    for i, (exponent, kind) in enumerate(word):
        if kind:
            gap += 1
        else:
            gaps[gap][exponent].append(i)
    result = []
    for gap in sorted(gaps):
        queue = []
        for exponent, ids in gaps[gap].items():
            heapq.heappush(queue, (-len(ids), exponent))
        while len(queue) >= 2:
            count_a, a = heapq.heappop(queue)
            count_b, b = heapq.heappop(queue)
            left, right = gaps[gap][a].popleft(), gaps[gap][b].popleft()
            result.append(tuple(sorted((left, right))))
            if count_a + 1 < 0:
                heapq.heappush(queue, (count_a+1, a))
            if count_b + 1 < 0:
                heapq.heappush(queue, (count_b+1, b))
    return result


def actual_case(word, p, label):
    rotations = [i for i, (_, kind) in enumerate(word) if kind == 0]
    refs = [i for i, (_, kind) in enumerate(word) if kind == 1]
    pairs = gap_pairs(word)
    needed = p-1
    result = {'p': p, 'label': label, 'word': word, 'rotation_count': len(rotations),
              'reflection_count': len(refs), 'all_gap_pairs': pairs, 'eligible': len(pairs) >= needed,
              'fixed_omissions': [], 'selectors': []}
    if not result['eligible']:
        return result
    chosen_pairs = pairs[:needed]
    covered = {i for pair in chosen_pairs for i in pair}
    omitted_count = len(rotations)-(2*p-2)
    fixed = [i for i in rotations if i not in covered][:omitted_count-needed]
    if len(fixed) != omitted_count-needed or omitted_count < needed:
        raise ValueError('omission accounting failed')
    result['fixed_omissions'] = fixed
    for left, right in itertools.combinations(refs, 2):
        def signed(i):
            return (-1 if left < i < right else 1)*word[i][0]
        full = (word[left][0]-word[right][0]+sum(signed(i) for i in rotations)) % p
        fixed_sum = sum(signed(i) for i in fixed) % p
        states = {fixed_sum: ()}
        for a, b in chosen_pairs:
            next_states = {}
            for value, path in states.items():
                next_states.setdefault((value+signed(a)) % p, path+(a,))
                next_states.setdefault((value+signed(b)) % p, path+(b,))
            states = next_states
        if len(states) != p or full not in states:
            raise ValueError('omission support did not cover F_p')
        omitted = set(fixed) | set(states[full])
        selected = sorted([i for i in rotations if i not in omitted] + [left, right])
        if len(selected) != 2*p or len(set(selected)) != len(selected) or direct(word, selected, p) != (0, 0):
            raise ValueError('actual original selector failed')
        result['selectors'].append({'reflections': [left, right], 'indices': selected})
    return result


def structured_word(p):
    return [(v, 0) for _ in range(p-1) for v in (1, 2)] + \
           [element for _ in range(p-1) for element in ((0, 1), (1, 0))] + [(0, 1)]*3


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rng = random.Random(2026102804)
    cases = []
    for p in (3, 5, 7, 11):
        for R in (3*p-3, 3*p-2):
            for trial in range(40):
                n = 4*p-1
                positions = set(rng.sample(range(n), R))
                word = [(rng.randrange(p), 0 if i in positions else 1) for i in range(n)]
                cases.append(actual_case(word, p, {'kind': 'random', 'R': R, 'trial': trial}))
    structured = [actual_case(structured_word(p), p, {'kind': 'structured'}) for p in (3, 5, 7, 11)]
    data = {'scope': 'bounded actual-word verification; not proof for all p or words',
            'seed': 2026102804, 'random_cases': cases, 'structured_cases': structured}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(data, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'result': 'PASS_BOUNDED_SAME_GAP', 'random_words': len(cases),
                      'eligible_random_words': sum(c['eligible'] for c in cases),
                      'random_reflection_pairs_verified': sum(len(c['selectors']) for c in cases),
                      'structured_words': len(structured),
                      'structured_reflection_pairs_verified': sum(len(c['selectors']) for c in structured),
                      'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()

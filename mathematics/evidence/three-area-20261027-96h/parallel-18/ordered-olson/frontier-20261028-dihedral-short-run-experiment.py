#!/usr/bin/env python3
"""Bounded actual-word checks for the adaptive short-reflection-run selector."""

import argparse
from collections import defaultdict, deque
import heapq
import itertools
import json
import random


def direct(word, selected, p):
    value = parity = 0
    for i in selected:
        x, kind = word[i]
        value = (value+x if parity == 0 else value-x) % p
        parity ^= kind
    return value, parity


def unequal_pairs(word):
    groups = defaultdict(deque)
    for i, (x, kind) in enumerate(word):
        if not kind:
            groups[x].append(i)
    heap = [(-len(ids), x) for x, ids in groups.items()]
    heapq.heapify(heap)
    result = []
    while len(heap) >= 2:
        ca, a = heapq.heappop(heap)
        cb, b = heapq.heappop(heap)
        result.append(tuple(sorted((groups[a].popleft(), groups[b].popleft()))))
        if ca+1 < 0:
            heapq.heappush(heap, (ca+1, a))
        if cb+1 < 0:
            heapq.heappush(heap, (cb+1, b))
    return result


def runs(word):
    result = []
    i = 0
    while i < len(word):
        if word[i][1] == 0:
            i += 1
            continue
        j = i
        while j < len(word) and word[j][1] == 1:
            j += 1
        result.append(tuple(range(i, j)))
        i = j
    return result


def process(word, p, label):
    rotations = [i for i, (_, kind) in enumerate(word) if kind == 0]
    R = len(rotations)
    t = R-(2*p-2)
    pairs = unequal_pairs(word)
    s = min(t, len(pairs), p-1) if t >= 0 else 0
    candidate = None
    for run in runs(word):
        if len(run) < 2:
            continue
        diffs = {}
        for i, j in itertools.combinations(run, 2):
            diffs.setdefault((word[j][0]-word[i][0]) % p, (i, j))
        if min(p, s+1)+len(diffs) > p:
            candidate = (run, diffs)
            break
    eligible = t >= 0 and candidate is not None
    result = {'p': p, 'label': label, 'word': word, 'R': R, 't': t, 's': s,
              'all_rotation_pairs': pairs, 'eligible': eligible, 'reflection_run': None,
              'fixed_omissions': None, 'chosen_pair_omissions': None,
              'selected_reflections': None, 'selected_indices': None}
    if not eligible:
        return result
    run, differences = candidate
    chosen_pairs = pairs[:s]
    used = {i for pair in chosen_pairs for i in pair}
    outside = [i for i in rotations if i not in used]
    fixed = outside[:t-s]
    if len(fixed) != t-s:
        raise ValueError('insufficient outside positions for fixed omissions')
    states = {sum(word[i][0] for i in fixed) % p: ()}
    for a, b in chosen_pairs:
        new = {}
        for value, path in states.items():
            new.setdefault((value+word[a][0]) % p, path+(a,))
            new.setdefault((value+word[b][0]) % p, path+(b,))
        states = new
    if len(states) < min(p, s+1):
        raise ValueError('actual omission-sum lower bound failed')
    total = sum(word[i][0] for i in rotations) % p
    match = next(((omitted, diff, pair) for omitted in states for diff, pair in differences.items()
                  if (total-omitted) % p == diff), None)
    if match is None:
        raise ValueError('required sum/difference intersection absent')
    omitted_sum, _, refs = match
    variable = states[omitted_sum]
    omitted = set(fixed) | set(variable)
    selected = sorted([i for i in rotations if i not in omitted] + list(refs))
    if len(selected) != 2*p or len(set(selected)) != 2*p or direct(word, selected, p) != (0, 0):
        raise ValueError('actual original selector invalid')
    result.update({'reflection_run': run, 'fixed_omissions': fixed,
                   'chosen_pair_omissions': variable, 'selected_reflections': refs,
                   'selected_indices': selected, 'difference_support_size': len(differences),
                   'omission_support_size': len(states)})
    return result


def structured(p):
    word = [(1, 0)]*(2*p-2) + [(0, 1)]*2
    word.extend(item for _ in range(p-1) for item in ((2, 0), (0, 1)))
    word.append((0, 1))
    return word


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    rng = random.Random(2026102806)
    cases = []
    for p in (3, 5, 7, 11):
        for R in range(2*p-2, 3*p-1):
            for trial in range(40):
                locations = set(rng.sample(range(4*p-1), R))
                word = [(rng.randrange(p), 0 if i in locations else 1) for i in range(4*p-1)]
                cases.append(process(word, p, {'kind': 'random', 'R': R, 'trial': trial}))
    families = [process(structured(p), p, {'kind': 'structured'}) for p in (5, 7, 11, 13)]
    if not all(row['eligible'] for row in families):
        raise ValueError('structured family failed sufficient hypotheses')
    data = {'scope': 'bounded actual-word checks, not a universal selector proof', 'seed': 2026102806,
            'random_cases': cases, 'structured_cases': families}
    with open(args.output, 'x', encoding='utf-8') as stream:
        json.dump(data, stream, separators=(',', ':'))
        stream.write('\n')
    print(json.dumps({'result': 'PASS_BOUNDED_SHORT_RUN', 'random_words': len(cases),
                      'eligible_random_words': sum(c['eligible'] for c in cases),
                      'structured_words': len(families), 'output': args.output}, sort_keys=True))


if __name__ == '__main__':
    main()

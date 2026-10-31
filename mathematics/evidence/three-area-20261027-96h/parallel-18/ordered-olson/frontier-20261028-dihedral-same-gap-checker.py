#!/usr/bin/env python3
"""Independent direct replay of same-gap original-word selector evidence."""

import argparse
from collections import Counter, defaultdict
import copy
import hashlib
import itertools
import json
import random


def direct(word, indices, p):
    exponent = 0
    sign = 1
    parity = 0
    for i in indices:
        x, kind = word[i]
        exponent = (exponent + sign*x) % p
        if kind:
            sign = -sign
            parity ^= 1
    return exponent, parity


def inspect(case):
    p, word = case['p'], case['word']
    if len(word) != 4*p-1 or any(kind not in (0, 1) or x < 0 or x >= p for x, kind in word):
        raise ValueError('malformed original word')
    rotations = [i for i, (_, kind) in enumerate(word) if kind == 0]
    refs = [i for i, (_, kind) in enumerate(word) if kind == 1]
    if len(rotations) != case['rotation_count'] or len(refs) != case['reflection_count']:
        raise ValueError('wrong type counts')
    gap = 0
    grouped = defaultdict(list)
    gap_of = {}
    for i, (x, kind) in enumerate(word):
        if kind:
            gap += 1
        else:
            grouped[gap].append(x)
            gap_of[i] = gap
    max_pairs = 0
    for values in grouped.values():
        largest = max(Counter(values).values())
        max_pairs += min(len(values)//2, len(values)-largest)
    if len(case['all_gap_pairs']) != max_pairs:
        raise ValueError('gap matching count is not maximum')
    if case['eligible'] != (max_pairs >= p-1):
        raise ValueError('incorrect eligibility')
    used = set()
    for pair in case['all_gap_pairs']:
        if len(pair) != 2 or pair[0] >= pair[1] or any(i in used or i not in gap_of for i in pair):
            raise ValueError('gap pair reuse or order')
        a, b = pair
        if gap_of[a] != gap_of[b] or word[a][0] == word[b][0]:
            raise ValueError('gap pair condition false')
        used.update(pair)
    if not case['eligible']:
        if case['fixed_omissions'] or case['selectors']:
            raise ValueError('ineligible case has selectors')
        return 0
    chosen_pairs = case['all_gap_pairs'][:p-1]
    covered = {i for pair in chosen_pairs for i in pair}
    fixed = case['fixed_omissions']
    t = len(rotations)-(2*p-2)
    if len(fixed) != t-(p-1) or len(set(fixed)) != len(fixed):
        raise ValueError('fixed omission count invalid')
    if any(i not in rotations or i in covered for i in fixed):
        raise ValueError('fixed omission not outside paired rotations')
    expected = set(itertools.combinations(refs, 2))
    actual = [tuple(x['reflections']) for x in case['selectors']]
    if len(actual) != len(expected) or set(actual) != expected:
        raise ValueError('not every reflection pair has one selector')
    for record in case['selectors']:
        left, right = record['reflections']
        selected = record['indices']
        if len(selected) != 2*p or selected != sorted(set(selected)) or any(i < 0 or i >= len(word) for i in selected):
            raise ValueError('bad selector indices')
        if [i for i in selected if word[i][1]] != [left, right]:
            raise ValueError('wrong selected reflections')
        omitted = set(rotations)-set(selected)
        if not set(fixed).issubset(omitted) or any(len(set(pair) & omitted) != 1 for pair in chosen_pairs):
            raise ValueError('paired omission constraint failed')
        if direct(word, selected, p) != (0, 0):
            raise ValueError('actual increasing-index product is not identity')
        # Independent reachable-set confirmation for this reflection pair.
        reachable = {sum((-1 if left < i < right else 1)*word[i][0] for i in fixed) % p}
        for a, b in chosen_pairs:
            sa = (-1 if left < a < right else 1)*word[a][0]
            sb = (-1 if left < b < right else 1)*word[b][0]
            reachable = {(x+y) % p for x in reachable for y in (sa, sb)}
        if len(reachable) != p:
            raise ValueError('actual omission support is not full field')
    return len(actual)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    rng = random.Random(data['seed'])
    total_pairs = eligible = 0
    for case in data['random_cases']:
        p, R = case['p'], case['label']['R']
        locations = set(rng.sample(range(4*p-1), R))
        expected = [[rng.randrange(p), 0 if i in locations else 1] for i in range(4*p-1)]
        if expected != case['word']:
            raise ValueError('random seed replay mismatch')
        total_pairs += inspect(case)
        eligible += int(case['eligible'])
    for case in data['structured_cases']:
        p = case['p']
        expected = [[v, 0] for _ in range(p-1) for v in (1, 2)] + \
                   [element for _ in range(p-1) for element in ([0, 1], [1, 0])] + [[0, 1]]*3
        if case['word'] != expected:
            raise ValueError('structured family word mismatch')
        total_pairs += inspect(case)
    original = next(c for c in data['structured_cases'] if c['p'] == 5)
    bad = copy.deepcopy(original)
    bad['selectors'][0]['indices'][1] = bad['selectors'][0]['indices'][0]
    try:
        inspect(bad)
    except ValueError as exc:
        if str(exc) != 'bad selector indices':
            raise ValueError('mutation rejected for unintended reason') from exc
    else:
        raise ValueError('duplicate selector mutation not rejected')
    print(json.dumps({'result': 'PASS_INDEPENDENT_SAME_GAP_REPLAY',
                      'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'random_words_replayed': len(data['random_cases']),
                      'eligible_random_words': eligible,
                      'structured_words_checked': len(data['structured_cases']),
                      'all_reflection_pair_selectors_checked': total_pairs,
                      'duplicate_selector_control_rejected': True,
                      'scope': 'finite actual words; not an all-prime proof or novelty certificate'}, sort_keys=True))


if __name__ == '__main__':
    main()

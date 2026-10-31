#!/usr/bin/env python3
"""Independent full seed replay and direct selector check for reflection runs."""

import argparse
from collections import Counter, defaultdict
import copy
import hashlib
import itertools
import json
import random


def direct(word, indices, p):
    x, sign, parity = 0, 1, 0
    for i in indices:
        value, kind = word[i]
        x = (x+sign*value) % p
        if kind:
            parity ^= 1
            sign = -sign
    return x, parity


def all_runs(word):
    output = []
    i = 0
    while i < len(word):
        if word[i][1] == 0:
            i += 1
            continue
        j = i
        while j < len(word) and word[j][1] == 1:
            j += 1
        output.append(list(range(i, j)))
        i = j
    return output


def validate(case):
    p, word = case['p'], case['word']
    if len(word) != 4*p-1:
        raise ValueError('wrong original word length')
    rotations = [i for i, (_, kind) in enumerate(word) if kind == 0]
    if len(rotations) != case['R'] or case['t'] != len(rotations)-(2*p-2):
        raise ValueError('wrong rotation count')
    counts = Counter(word[i][0] for i in rotations)
    bound = min(len(rotations)//2, len(rotations)-max(counts.values(), default=0))
    pairs = case['all_rotation_pairs']
    if len(pairs) != bound:
        raise ValueError('rotation matching count is not maximum')
    used = set()
    for a, b in pairs:
        if a >= b or a in used or b in used or a not in rotations or b not in rotations:
            raise ValueError('rotation pair reuse or order')
        if word[a][0] == word[b][0]:
            raise ValueError('rotation pair exponents equal')
        used.update((a, b))
    t = case['t']
    candidates = [run for run in all_runs(word) if len(run) >= p+1 and
                  len({word[i][0] for i in run})+t >= p]
    expected_eligible = t >= 0 and bound >= t and bool(candidates)
    if case['eligible'] != expected_eligible:
        raise ValueError('wrong hypothesis status')
    if not expected_eligible:
        if case['selected_indices'] is not None:
            raise ValueError('ineligible record has selector')
        return False
    run = case['reflection_run']
    if run not in candidates:
        raise ValueError('saved reflection run invalid')
    selected = case['selected_indices']
    if len(selected) != 2*p or selected != sorted(set(selected)) or any(i < 0 or i >= len(word) for i in selected):
        raise ValueError('bad selector indices')
    selected_reflections = [i for i in selected if word[i][1] == 1]
    if selected_reflections != case['selected_reflections'] or len(selected_reflections) != 2 or any(i not in run for i in selected_reflections):
        raise ValueError('wrong actual reflection pair')
    omitted = sorted(set(rotations)-set(selected))
    if omitted != sorted(case['omitted_rotations']) or len(omitted) != t:
        raise ValueError('wrong omitted rotations')
    if any(len(set(pair) & set(omitted)) != 1 for pair in pairs[:t]):
        raise ValueError('one-per-pair omission violated')
    if direct(word, selected, p) != (0, 0):
        raise ValueError('actual ordered product not identity')
    differences = {(word[j][0]-word[i][0]) % p for i, j in itertools.combinations(run, 2)}
    if len(differences) < len({word[i][0] for i in run}):
        raise ValueError('reflection difference bound false')
    sums = {0}
    for a, b in pairs[:t]:
        sums = {(x+word[i][0]) % p for x in sums for i in (a, b)}
    if len(sums) < min(p, t+1):
        raise ValueError('omission-sum bound false')
    possible = {(sum(word[i][0] for i in rotations)-x) % p for x in sums}
    if not possible.intersection(differences):
        raise ValueError('actual support intersection empty')
    return True


def random_word(p, R, rng):
    F = 4*p-1-R
    remainder = [0]*R + [1]*(F-(p+1))
    rng.shuffle(remainder)
    cut = rng.randrange(len(remainder)+1)
    return [[rng.randrange(p), bit] for bit in remainder[:cut] + [1]*(p+1) + remainder[cut:]]


def verify_structured_prior_failures(case):
    p, word = case['p'], case['word']
    rotations = [i for i, (_, bit) in enumerate(word) if bit == 0]
    I = rotations[:2*p-2]
    S = sum(word[i][0] for i in I) % p
    refs = [i for i, (_, bit) in enumerate(word) if bit == 1]
    z = [(i, (word[i][0]+2*sum(word[j][0] for j in I if j < i)) % p) for i in refs]
    if S == 0 or len({v for _, v in z}) != p-1:
        raise ValueError('structured fixed-I prior condition differs')
    if any((b-a) % p == S for (_, a), (_, b) in itertools.combinations(z, 2)):
        raise ValueError('structured fixed-I unexpectedly has a two-reflection selector')
    runs = []
    for _, bit in word:
        if not runs or runs[-1][0] != bit:
            runs.append([bit, 1])
        else:
            runs[-1][1] += 1
    if sum(length % 2 for _, length in runs) <= 3:
        raise ValueError('structured quotient lacks odd-run separation obstruction')
    gap = 0
    groups = defaultdict(list)
    for value, bit in word:
        if bit:
            gap += 1
        else:
            groups[gap].append(value)
    if any(len(set(values)) > 1 for values in groups.values()):
        raise ValueError('structured family unexpectedly has same-gap unequal pairs')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results')
    args = parser.parse_args()
    raw = open(args.results, 'rb').read()
    data = json.loads(raw)
    rng = random.Random(data['seed'])
    verified = 0
    for case in data['random_cases']:
        expected = random_word(case['p'], case['label']['R'], rng)
        if expected != case['word']:
            raise ValueError('random seed replay mismatch')
        verified += int(validate(case))
    for case in data['structured_cases']:
        if not validate(case) or not verify_structured_prior_failures(case):
            raise ValueError('structured family failed')
    example = next(c for c in data['structured_cases'] if c['p'] == 5)
    damaged = copy.deepcopy(example)
    damaged['selected_indices'][1] = damaged['selected_indices'][0]
    try:
        validate(damaged)
    except ValueError as exc:
        if str(exc) != 'bad selector indices':
            raise ValueError('mutation rejected for unintended reason') from exc
    else:
        raise ValueError('duplicate selector mutation was not rejected')
    print(json.dumps({'result': 'PASS_INDEPENDENT_REFLECTION_RUN_REPLAY',
                      'input_sha256': hashlib.sha256(raw).hexdigest(),
                      'random_words_replayed': len(data['random_cases']),
                      'qualifying_actual_selectors_verified': verified,
                      'structured_instances_verified': len(data['structured_cases']),
                      'structured_fixed_I_and_old_certificates_fail': True,
                      'duplicate_selector_control_rejected': True,
                      'scope': 'finite actual inputs; not an all-prime proof or novelty determination'}, sort_keys=True))


if __name__ == '__main__':
    main()
